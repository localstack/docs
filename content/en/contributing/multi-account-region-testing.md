---
title: "Multi account and region testing"
weight: 8
description: >
  How to test multi-account and multi-region compatibility.
---

LocalStack supports multi accounts and regions compatibility. 
This document describes how to test your changes against cross accounts and regions.

We regularly run the circleci test jobs of the LocalStack community repository to check the compatibility of cross accounts against the changes. To achieve that, we have a [scheduled workflow](https://github.com/localstack/localstack/blob/master/.circleci/config.yml) on [LocalStack](https://github.com/localstack/localstack), which executes the tests with randomised account and region credentials every night at 1:00am UTC.

## Manually trigger the workflow

To manually trigger the scheduled workflow in case you have the permissions, you can change set the value of `randomize-aws-credentials` to `true` in the [workflow](https://github.com/localstack/localstack/blob/master/.circleci/config.yml#L13). This will trigger the tests with randomised account and region credentials.

{{< alert title="Note">}}
Make sure to change the value back to `false` after the tests are completed. 
{{< /alert >}}

## Test changes locally with non-default credentials

In order to test your changes on your machine for multi-accounts and region compatibility in case you have the permissions, i.e. for non-default values other than `000000000000` for account ID or `us-east-1` for region, set the following environment variables to any random non-default values, for example:  

- `TEST_AWS_ACCOUNT_ID=111111111111`
- `TEST_AWS_ACCESS_KEY_ID=111111111111`
- `TEST_AWS_REGION=us-west-1`
- `TEST_AWS_SECRET_ACCESS_KEY=test1`

You can additionally prefer to create a commit eg: [da3f8d5](https://github.com/localstack/localstack/pull/9751/commits/da3f8d5f2328adb7c5c025722994fea4433c08ba) to test the pipeline for non-default credentials against your changes.

{{< alert title="Note">}}
Make sure to revert these changes after the tests are completed. 
{{< /alert >}}
