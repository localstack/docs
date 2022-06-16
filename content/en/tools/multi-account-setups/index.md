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

LocalStack Community only supports a single AWS Account ID, `000000000000` by default.
By contrast, LocalStack Pro ships with multi-account support which adds namespacing based on AWS Account ID

Namespaced AWS resources can be accessed by using the `AWS_ACCESS_KEY_ID` variable when making requests.
No additional server-side configuration is required.

{{< alert >}}
**Important:**
Multi-account is not supported for the `us-east-1` region.
See [limitation note](#limitations).
{{< /alert >}}

{{< command >}}
$ export AWS_DEFAULT_REGION=eu-central-1

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

In absence of an explicit value for Account ID, LocalStack reverts to the default value of `000000000000`.
In the current example, not setting an explicit Account ID will return no resources.

{{< command >}}
$ awslocal ec2 describe-key-pairs
{
    "KeyPairs": []
}
{{< /command >}}

{{< alert >}}
**Note:**
LocalStack uses the `AWS_ACCESS_KEY_ID` client-side variable for Account ID.
In future LocalStack may support proper access key IDs issued by the local IAM service, which will then internally be translated to corresponding account IDs.
{{< /alert >}}

### Limitations

In order to use multi-accounts, the region must be configured to something other than `us-east-1`.
Note that `us-east-1` is the default region and must be explicitly overridden.
For the AWS CLI, this can be done using the `AWS_DEFAULT_REGION` or the `--region` argument.
More information can be found on [AWS CLI documentation](https://docs.aws.amazon.com/cli/latest/userguide/cli-chap-configure.html).
