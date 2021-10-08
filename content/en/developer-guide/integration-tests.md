---
title: "Integration tests"
weight: 5
description: >
  How to run and write integration tests.
---

LocalStack has an extensive set of [integration tests](https://github.com/localstack/localstack/tree/master/tests/integration).
This document describes how to run and write integration tests.

## Running the test suite

To run the tests you can use the make target and set the `TEST_PATH` variable.

```bash
TEST_PATH="tests/integration" make test
```

or run it manually within the virtual environment:

```bash
python -m pytest --log-cli-level=INFO tests/integration
```

### Running individual tests

You can further specify the file and test class you want to run in the test path:

```bash
TEST_PATH="tests/integration/docker/test_docker.py::TestDockerClient" make test
```

### Test against a running LocalStack instance

When you run the integration tests, LocalStack is automatically started (via the pytest conftest mechanism in [tests/integration/conftest.py](https://github.com/localstack/localstack/blob/master/tests/integration/conftest.py)).
You can disable this behavior by setting the environment variable `TEST_SKIP_LOCALSTACK_START=1`.

### Test against real AWS

It can be useful to run an integration test against the real AWS cloud using your credentials.
You can do this by setting the environment variable `TEST_TARGET="AWS_CLOUD"`.


## Writing a test

We use [pytest](https://docs.pytest.org) for our testing framework.
Older tests were written using the unittest framework, but its use is discouraged.

If your test matches the pattern `tests/integration/**/test_*.py` it will be picked up by the integration test suite.

### Functional-style tests

You can write functional style tests by defining a function with the prefix `test_` with basic asserts:

```python
def test_something():
  assert True is not False
```

### Class-style tests

Or you can write class-style tests by grouping tests that logically belong together in a class:

```python
class TestMyThing:
  def test_something(self):
    assert True is not False
```

### Fixtures

We use the pytest fixture concept, and provide several fixtures you can use when writing AWS tests.
For example, to inject a Boto client for SQS, you can specify the `sqs_client` in your test method:

```python
class TestMyThing:
  def test_something(self, sqs_client):
    assert len(sqs_client.list_queues()["QueueUrls"]) == 0
```

We also provide fixtures for certain disposable resources, like buckets:

```bash
def test_something_on_a_bucket(s3_bucket):
  s3_bucket
  # s3_bucket is a boto s3 bucket object that is created before
  # the test runs, and removed after it returns.
```

Another pattern we use is the [factory as fixture](https://docs.pytest.org/en/6.2.x/fixture.html#factories-as-fixtures) pattern.

```bash
def test_something_on_multiple_buckets(s3_create_bucket):
  bucket1 = s3_create_bucket()
  bucket2 = s3_create_bucket()
  # both buckets will be deleted after the test returns
```

You can find the list of available fixtures in the [fixtures.py](https://github.com/localstack/localstack/blob/master/tests/integration/fixtures.py).