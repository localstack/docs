---
title: "Live Policy Stream"
linkTitle: "Live Policy Stream"
weight: 3
description: Generate a live stream of policies as requests are coming into LocalStack
---

## Introduction

Live Policy Stream produces a continuous flow of policies and the associated principals or resources. With each request, it starts by displaying the principal or resource that the policy should be linked to. This will either be a service resource in the case of resource-based policies, or an IAM principal in other scenarios. Following that, it presents the recommended policy.


## Getting started

To test Live Policy Stream, start localstack with following flags enabled:

```
DEBUG=1
LOCALSTACK_API_KEY=<...>
ENFORCE_IAM=1
```
If we want to use the policy stream feature, but without the enforcement, we need to set `IAM_SOFT_MODE=1`.

Here is the command you can run in your terminal 

```
DEBUG=1 ENFORCE_IAM=1 IAM_SOFT_MODE=1 localstack start
```

Now open a new terminal window tab and run the following to enable live policy stream:

```
localstack aws iam stream
```

In another tab, we will create aws resources and see required policies needed for it. In the following example we are creating sns topic

```
awslocal sns create-topic --name test-topic
```

On the other tab the necessary policy will be generated. You can attach this policy to the IAM role which can then create the resource: 

```
Attached to identity: "arn:aws:iam::000000000000:root"

Policy:
{
  "Version": "2012-10-17",
  "Statement": [
    {
      "Sid": "Test3a92fb6c",
      "Effect": "Allow",
      "Action": "sns:CreateTopic",
      "Resource": "arn:aws:sns:us-east-1:000000000000:test-topic"
    }
  ]
}
```




