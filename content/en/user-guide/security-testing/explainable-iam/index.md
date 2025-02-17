---
title: "Explainable IAM"
linkTitle: "Explainable IAM"
weight: 2
description: Discover IAM Policy Engine logs related to failed policy evaluation
tags: ["Pro image"]
---

## Introduction

The IAM Policy Engine logs output related to failed policy evaluation directly to the LocalStack logs.
You can enable `DEBUG=1` to gain visibility into these log messages, allowing you to identify the additional policies required for your request to succeed.

## Getting started

This guide is designed for users new to Explainable IAM and assumes basic knowledge of the AWS CLI and our [`awslocal`](https://github.com/localstack/awscli-local) wrapper script.

Start your LocalStack container with the `DEBUG=1` and `ENFORCE_IAM=1` environment variables set:

{{< command >}}
$ DEBUG=1 ENFORCE_IAM=1 localstack start
{{< /command >}}

In this guide, we will create a policy for creating Lambda functions by only allowing the `lambda:CreateFunction` permission.
However we have not included the `iam:PassRole` permission, and we will use the Policy Engine's log to point out adding the necessary permission.

### Create a new user

Create a policy document named `policy_1.json` and add the following content:

```json
{
  "Version": "2012-10-17",
  "Statement": [
    {
      "Sid": "FirstStatement",
      "Effect": "Allow",
      "Action": "lambda:CreateFunction",
      "Resource": "*"
    }
  ]
}
```

You can now create a new user named `test-user`, and put the policy in place by executing the following commands:

{{< command >}}
$ awslocal iam create-user --user-name test-user
<disable-copy>
{
    "User": {
        "Path": "/",
        "UserName": "test-user",
        "UserId": "x8a2eu4mc91yqtjazvhp",
        "Arn": "arn:aws:iam::000000000000:user/test-user",
        "CreateDate": "2022-07-05T16:08:25.741000+00:00"
    }
}
</disable-copy>
$ awslocal iam put-user-policy --user-name test-user --policy-name policy1 --policy-document file://policy_1.json
{{< /command >}}

You can further create an access key for the user by executing the following command:

{{< command >}}
$ awslocal iam create-access-key --user-name test-user
{{< /command >}}

Export the access key and secret key as environment variables:

{{< command >}}
$ export AWS_ACCESS_KEY_ID=...
$ export AWS_SECRET_ACCESS_KEY=...
{{< /command >}}

### Attempt to create a Lambda function

You can now attempt to create a Lambda function using the newly created user's credentials:

{{< command >}}
$ awslocal lambda create-function \
    --function-name test-function \
    --role arn:aws:iam::000000000000:role/lambda-role \
    --runtime python3.8 \
    --handler handler.handler \
    --zip-file fileb://function.zip
<disable-copy>
An error occurred (AccessDeniedException) when calling the CreateFunction operation: Access to the specified resource is denied
</disable-copy>
{{< / command >}}

You can inspect the LocalStack logs, to observe the presence of five log entries directly related to the denied request:

```bash
INFO:localstack_ext.services.iam.policy_engine.handler: Request for service lambda for operation CreateFunction denied.
DEBUG:localstack_ext.services.iam.policy_engine.handler: Necessary permissions for this action: ["Action 'lambda:CreateFunction' for 'arn:aws:lambda:us-east-1:000000000000:function:test-function'", "Action 'iam:PassRole' for 'arn:aws:iam::000000000000:role/lambda-role'"]
DEBUG:localstack_ext.services.iam.policy_engine.handler: 0 permissions have been explicitly denied: []
DEBUG:localstack_ext.services.iam.policy_engine.handler: 1 permissions have been explicitly allowed: ["Action 'lambda:CreateFunction' for 'arn:aws:lambda:us-east-1:000000000000:function:test-function'"]
DEBUG:localstack_ext.services.iam.policy_engine.handler: 1 permissions have been implicitly denied: ["Action 'iam:PassRole' for 'arn:aws:iam::000000000000:role/lambda-role'"]
```

Upon examination, it becomes apparent that the action `iam:PassRole` is not allowed; rather, it is implicitly denied for your user concerning the resource `arn:aws:iam::000000000000:role/lambda-role`.
This implies that there is no explicit deny statement in the relevant policies, but there is also no allow statement, resulting in the implicit denial of the action.
You can incorporate this action into the policy.

### Incorporate the action into the policy

For illustrative purposes, we will keep the example straightforward, using the same wildcard resource.
Edit the `policy_1.json` file to include the `iam:PassRole` action:

```json
{
  "Version": "2012-10-17",
  "Statement": [
    {
      "Sid": "FirstStatement",
      "Effect": "Allow",
      "Action": ["lambda:CreateFunction", "iam:PassRole"],
      "Resource": "*"
    }
  ]
}
```

Re-run the Lambda [`CreateFunction`](https://docs.aws.amazon.com/lambda/latest/dg/API_CreateFunction.html) API.
You will notice that the request is now successful, and the function is created.

## Soft Mode

Enabling `IAM_SOFT_MODE=1` allows you to review the logs and assess whether your requests would have been denied or granted while executing your entire stack without disruptions.

Using this, you can avoid the need for redeployment to address each missing permission individually, streamlining the debugging process and enhancing the efficiency of your IAM configurations.
