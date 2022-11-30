---
title: "Multi-Account Setups"
linkTitle: "Multi-Account Setups"
categories: ["LocalStack Pro"]
tags: ["multi-tenant", "multi-account", "account-id", "namespaces"]
aliases:
  - /aws/multi-account-setups/
weight: 5
description: >
  Using LocalStack in multi-tenant setups
---

{{< alert title="Warning" color="warning" >}}
Known limitations of multi-accounts:
- Not supported for setups that use cross-account and cross-service access.
- Not supported in Kinesis.

Please see <https://github.com/localstack/localstack/issues/7041> for more information.
{{< /alert >}}

LocalStack ships with multi-account support which allows namespacing based on AWS account ID and region name.

The AWS account ID to be used must be sent as part of the request.
There is no server-side configuration required.

LocalStack uses the value in the AWS Access Key ID field for the purpose of namespacing over account ID.
This field can be configured in the AWS CLI in multiple ways: please refer to AWS CLI documentation [here](https://docs.aws.amazon.com/cli/latest/userguide/cli-configure-quickstart.html#cli-configure-quickstart-precedence).
This field must either contain a valid 12-digit or an alpha-numeric string.
In the first case, the value is assumed to be the account ID.
In the second case, the default account ID `000000000000` is used as fallback.

LocalStack will also ignore possible production AWS Access Key IDs (starting with `ASIA...` or `AKIA...`) and fallback to default.

In the future LocalStack shall support proper access key IDs issued by the local IAM service, which will then be internally translated to corresponding account IDs.

{{< alert title="Warning" color="warning">}}
Older releases of LocalStack allowed account IDs to be overridden via the `TEST_AWS_ACCOUNT_ID` environment variable.
This functionality has been removed.
{{< /alert >}}

In following examples, we configure the AWS CLI account ID via environment variable.

{{< command >}}
$ AWS_ACCESS_KEY_ID=000000000001 awslocal ec2 create-key-pair --key-name green-hospital

$ AWS_ACCESS_KEY_ID=000000000002 awslocal ec2 create-key-pair --key-name red-medicine

$ AWS_ACCESS_KEY_ID=000000000001 awslocal ec2 describe-key-pairs
{
    "KeyPairs": [
        {
            "KeyFingerprint": "6b:e3:a3:41:4b:60:f3:6d:7b:84:3e:17:e3:ad:d0:15",
            "KeyName": "green-hospital"
        }
    ]
}

$ AWS_ACCESS_KEY_ID=000000000002 awslocal ec2 describe-key-pairs
{
    "KeyPairs": [
        {
            "KeyFingerprint": "16:4c:64:13:36:41:7c:75:d0:51:f0:db:ed:d7:c8:95",
            "KeyName": "red-medicine"
        }
    ]
}
{{< / command >}}

If no explicit Account ID is set, LocalStack falls back to default. In this example, no resources are returned.

{{< command >}}
$ awslocal ec2 describe-key-pairs
{
    "KeyPairs": []
}
{{< /command >}}
