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

LocalStack Pro supports multiple AWS accounts on a single running instance.
In contrast, LocalStack Community has a non-configurable AWS Account ID (`000000000000`).

AWS resources can be addressed by accounts using the `AWS_ACCESS_KEY_ID` variable.
As can be seen in the example below, all created resources are namespaced by account ID.

{{< command >}}
$ AWS_ACCESS_KEY_ID=001 awslocal ec2 create-key-pair --key-name green-hospital

$ AWS_ACCESS_KEY_ID=002 awslocal ec2 create-key-pair --key-name red-medicine

$ AWS_ACCESS_KEY_ID=001 awslocal ec2 describe-key-pairs
{
    "KeyPairs": [
        {
            "KeyFingerprint": "6b:e3:a3:41:4b:60:f3:6d:7b:84:3e:17:e3:ad:d0:15",
            "KeyName": "green-hospital"
        }
    ]
}

$ AWS_ACCESS_KEY_ID=002 awslocal ec2 describe-key-pairs
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
Thus, in this example, not setting an explicit Account ID will return no resources.

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

Multi-accounts is currently supported by following services:
- ACM
- Batch
- CloudWatch
- EC2 (partial)
- ECS
- ELB
- IAM
- KMS
- CloudWatch
- Organisations
- Resource Groups
- Secrets Manager
- SES
- SSM (partial)
- SWF
- Xray
