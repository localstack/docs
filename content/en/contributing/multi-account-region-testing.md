---
title: "Multi-account and Multi-region Testing"
weight: 8
description: >
  How to test multi-account and multi-region compatibility.
---

LocalStack supports multi accounts and regions compatibility. 
This document describes how to test your changes against cross accounts and regions.

We regularly run the circleci test jobs of the LocalStack community repository to check the compatibility of cross accounts against the changes. To achieve that, we have a [scheduled workflow](https://github.com/localstack/localstack/blob/master/.circleci/config.yml) on [LocalStack](https://github.com/localstack/localstack), which executes the tests with randomised account and region credentials every night at 1:00am UTC.


## Tips to make your changes compatible with multi-accounts and regions

In order to make your changes compatible with multi-accounts and regions, you should follow the below tips:

- For cross accounts, in inter service communication for many integrations, you can specify a role, with which permissions the source service makes a request to the target service, to access other services resource. This role should be in source account. When writing an AWS validated test case, you need to properly configure IAM roles. 

    For example: 
    In the test case `test_api_gateway_kinesis_integration` we have specified a [role](https://github.com/localstack/localstack/blob/ae31f63bb6d8254edc0c85a66e3c36cd0c7dc7b0/tests/aws/services/apigateway/test_apigateway_basic.py#L2017-L2022) in the apigateway which has permissions to access the target kinesis account.
    ```python
    result = self.connect_api_gateway_to_kinesis(
            client,
            api_name,
            stream_name,
            region_name,
            role_arn,
        )
    ```

- While having an inter service communication in cross-accounts, you can create the client using `with_assumed_role(…)`:

    For example:
    ```python
    result = self.connect_api_gateway_to_kinesis(
            client,
            api_name,
            stream_name,
            region_name,
            role_arn,
        )
    ```
    
- When there is no role specified, you should use the source arn conceptually if cross-account is allowed. 

    For example:
    This can be seen in a case where we [added](https://github.com/localstack/localstack/blob/ae31f63bb6d8254edc0c85a66e3c36cd0c7dc7b0/localstack/utils/aws/message_forwarding.py#L42) `account_id` to [send events to the target](https://github.com/localstack/localstack/blob/ae31f63bb6d8254edc0c85a66e3c36cd0c7dc7b0/localstack/utils/aws/message_forwarding.py#L31) service like sqs, sns, lambda, etc. 

- You should always refer the official AWS API docs and check how the the application is communicating to each other. 
    
    For example: 
    Firehose to s3 refer to [Offical AWS Docs](https://docs.aws.amazon.com/firehose/latest/dev/controlling-access.html#cross-account-delivery-s3).


## Manually trigger the workflow

To manually trigger the scheduled workflow in case you have the permissions, you can change set the value of `randomize-aws-credentials` to `true` in the [workflow](https://github.com/localstack/localstack/blob/master/.circleci/config.yml#L13). This will trigger the tests with randomised account and region credentials.

## Test changes locally with non-default credentials

In order to test your changes on your machine for multi-accounts and region compatibility in case you have the permissions, i.e. for non-default values other than `000000000000` for account ID or `us-east-1` for region, set the following environment variables to any random non-default values, for example:  

- `TEST_AWS_ACCOUNT_ID=111111111111`
- `TEST_AWS_ACCESS_KEY_ID=111111111111`
- `TEST_AWS_REGION=us-west-1`
- `TEST_AWS_SECRET_ACCESS_KEY=test1`

You can additionally prefer to create a commit eg: [da3f8d5](https://github.com/localstack/localstack/pull/9751/commits/da3f8d5f2328adb7c5c025722994fea4433c08ba) to test the pipeline for non-default credentials against your changes. Note that within the tests we must use `account_id`, `secondary_account_id`, `region_name`, `secondary_region_name` fixtures and avoid importing `localstack.constants.TEST_*` values. 

{{< alert title="Note">}}
Make sure to revert these changes after the tests are completed. 
{{< /alert >}}
