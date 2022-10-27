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

{{% alert title="Known issues" color="warning" %}}
Multi-account support is currently only working as long as no inter-service communication is involved.

See https://github.com/localstack/localstack/issues/7041 for more information
{{% /alert %}}

LocalStack Pro ships with multi-account support which allows namespacing based on AWS Account ID.
By contrast, LocalStack Community only supports a single AWS Account ID: `000000000000`.

Namespaced AWS resources can be accessed by using the `AWS_ACCESS_KEY_ID` variable when making requests.
No additional server-side configuration is required.

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

If an explicit value for Account ID is not set, LocalStack uses the default value of `000000000000`.
In the current example, not setting an explicit Account ID will return no resources.

{{< command >}}
$ awslocal ec2 describe-key-pairs
{
    "KeyPairs": []
}
{{< /command >}}

{{< alert title="Note" color="primary">}}
LocalStack uses the `AWS_ACCESS_KEY_ID` client-side variable for Account ID.
In future LocalStack may support proper access key IDs issued by the local IAM service, which will then internally be translated to corresponding account IDs.
{{< /alert >}}
