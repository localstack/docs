---
title: "Parity Testing"
weight: 7
description: >
  How to run and write Parity tests to verify and improve the correctness of LocalStack compared to AWS.
---

Parity tests are a special form of integration tests that should verify and improve the correctness of LocalStack compared to AWS.

Initially, a parity test is executed against AWS - the test marks certain responses that should be collected and verified for correctness. The result of the initial execution is a **snapshot.json** file that contains the recorded responses.

During a “normal” test execution, the test runs against LocalStack and compares the responses with the recorded content.

## How to write Parity tests

1.  Make sure that the test works against AWS.
    
2.  Add the `snapshot` fixture to your test and identify which responses you want to collect and compare against LocalStack
    
	1.  `snapshot.match(”identifier”, result)` indicates a result that will be recorded and stored in a file with the name `<testfile-name>.snapshot.json`
    
	    The **identifier** can be freely selected, but ideally should give a hint on what is recorded - so typically the name of the function. The **result** is expected to be a `dict`.

	2. Run the test against AWS: use the parameter `--snapshot-update` (or the environment variable `SNAPSHOT_UPDATE=1`) and set the environment variable as `TEST_TARGET=AWS_CLOUD`.

	3. Check the recorded result in `<testfile-name>.snapshot.json` and consider [using transformers](#using-transformers) to make the result comparable.
    
3.  Run the test against AWS. Ensure that the `AWS_CLOUD` is not set as a test target and that the parameter `--snapshot-update` is removed.

Here is an example of a parity test:

```python
def test_invocation(self, lambda_client, snapshot):
				# add transformers to make the results comparable
        snapshot.add_transformer(snapshot.transform.lambda_api()

        result = lambda_client.invoke(
            ....
        )
				# records the 'result' using the identifier 'invoke'
        snapshot.match("invoke", result)
```

## Using Transformers

Transformers should bring AWS response in a comparable form by replacing any request-specific parameters.

Replacements require thoughtful handling so that important information is not lost in translation.

The `snapshot` fixture uses some basic transformations by default, including:

-   Trimming MetaData (we only keep the `HTTPStatusCode` and `content-type` if set).
-   Replacing all UUIDs (that match a regex) with [reference-replacement](#reference-replacement).
-   Replacing everything that matches the ISO8601 pattern with “date”.
-   Replacing any value with datatype `datetime` with “datetime”.
-   Replace all values where the key contains “timestamp” with “timestamp”.
-   Regex replacement of the `account-id`.
-   Regex replacement of the location.


## API Transformer

For each API we will collect “general” transformations, that ideally handle all transformation that is necessary. We have already added a few utility functions, which collect common transformations collected by the API: `snapshot.add_transformer(snapshot.transform.lambda_api()`.


## Transformer Types

The Parity testing framework currently includes some basic transformer types:

-   `KeyValueBasedTransformer` replaces a value directly, or by reference; based on key-value evaluation.
-   `JsonPathTransformer` replaces the JSON path value directly, or by reference. [jsonpath-ng](https://pypi.org/project/jsonpath-ng/) is used for the JSON path evaluation.
-   `RegexTransformer` replaces the regex pattern globally. Please be aware that this will be applied on the json-string. The JSON will be transformed into a string, and the replacement happens globally - use it with care.

## Reference Replacement

Parameters can be replaced by reference. In contrast to the “direct” replacement, the value to be replaced will be **registered, and replaced later on as a “regex” pattern**.

It has the advantage of keeping information, when the same reference is used in several recordings in one test.

Consider the following example:

```python
def test_basic_invoke(
        self, lambda_client, create_lambda, snapshot
    ):
				
        # custom transformers
        snapshot.add_transformer(snapshot.transform.lambda_api())

        # predefined names for functions
        fn_name = f"ls-fn-{short_uid()}"
        fn_name_2 = f"ls-fn-{short_uid()}"

				# create function 1
        response = create_lambda(FunctionName=fn_name, ...  )
        snapshot.match("lambda_create_fn", response)

				# create function 2
	      response = create_lambda(FunctionName=fn_name_2, ...  )
	      snapshot.match("lambda_create_fn_2", response)

				# get function 1
        get_fn_result = lambda_client.get_function(FunctionName=fn_name)
        snapshot.match("lambda_get_fn", get_fn_result)

				# get function 2
        get_fn_result_2 = lambda_client.get_function(FunctionName=fn_name_2)
        snapshot.match("lambda_get_fn_2", get_fn_result_2)
```


The information that the function-name of the first recording (`lambda_create_fn`) is the same as in the record for `lambda_get_fn` is important.

Using reference replacement, this information is preserved in the `snapshot.json` . The reference replacement automatically adds an ascending number, to ensure that different values can be differentiated.

```json 
{
  "test_lambda_api.py::TestLambda::test_basic_invoke": {
    "recorded-date": ...,
    "recorded-content": {
      "lambda_create_fn": {
       ...
        "FunctionName": "<function-name:1>",
        "FunctionArn": "arn:aws:lambda:<region>:111111111111:function:<function-name:1>",
        "Runtime": "python3.9",
        "Role": "arn:aws:iam::111111111111:role/<resource:1>",
        ...
      },
      "lambda_create_fn_2": {
        ...
        "FunctionName": "<function-name:2>",
        "FunctionArn": "arn:aws:lambda:<region>:111111111111:function:<function-name:2>",
        "Runtime": "python3.9",
        "Role": "arn:aws:iam::111111111111:role/<resource:1>",
        ...
      },
      "lambda_get_fn": {
        ...
        "Configuration": {
          "FunctionName": "<function-name:1>",
          "FunctionArn": "arn:aws:lambda:<region>:111111111111:function:<function-name:1>",
          "Runtime": "python3.9",
          "Role": "arn:aws:iam::111111111111:role/<resource:1>",
         ...
      },
      "lambda_get_fn_2": {
        ...
        "Configuration": {
          "FunctionName": "<function-name:2>",
          "FunctionArn": "arn:aws:lambda:<region>:111111111111:function:<function-name:2>",
          "Role": "arn:aws:iam::111111111111:role/<resource:1>",
          ....
        },
      },

    }
  }
}
```


## Pitfalls

Sometimes different transformers might interfere, especially regex transformers and reference transformations can be tricky.

We added debug logs so that each replacement step should be visible in the output to help locate any unexpected behavior.

You can enable the debug logs by setting the env `DEBUG_SNAPSHOT=1`.

```json 
localstack.testing.snapshots.transformer: Registering regex pattern '000000000000' in snapshot with '111111111111'
localstack.testing.snapshots.transformer: Registering regex pattern 'us-east-1' in snapshot with '<region>'localstack.testing.snapshots.transformer: Replacing JsonPath '$.json_encoded_delivery..Body.Signature' in snapshot with '<signature>'
localstack.testing.snapshots.transformer: Registering reference replacement for value: '1ad533b5-ac54-4354-a273-3ea885f0d59d' -> '<uuid:1>'
localstack.testing.snapshots.transformer: Replacing JsonPath '$.json_encoded_delivery..MD5OfBody' in snapshot with '<md5-hash>'
localstack.testing.snapshots.transformer: Replacing regex '000000000000' with '111111111111'
localstack.testing.snapshots.transformer: Replacing regex 'us-east-1' with '<region>'
localstack.testing.snapshots.transformer: Replacing '1ad533b5-ac54-4354-a273-3ea885f0d59d' in snapshot with '<uuid:1>'
```


## Skipping verification of snapshot test

Snapshot verification is enabled by default. If for some reason you want to skip any snapshot verification, you can set the parameter `--snapshot-skip-all`.

If you want to skip verification for or a single test case, you can set the pytest marker `skip_snapshot_verify`. If you set the marker without a parameter, the verification will be skipped entirely for this test case.

However, you can exclude certain paths from the verification only. Simply include a list of json-paths. Those paths will then be excluded from the comparison:

```python 
@pytest.mark.skip_snapshot_verify(
        paths=["$..LogResult", "$..Payload.context.memory_limit_in_mb"]
    )
    def test_something_that_does_not_work_completly_yet(self, lambda_client, snapshot):
        snapshot.add_transformer(snapshot.transform.lambda_api())
        result = lambda_client....
        snapshot.match("invoke-result", result)
```
