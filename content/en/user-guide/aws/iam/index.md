---
title: "Identity and Access Management (IAM)"
linkTitle: "Identity and Access Management (IAM)"
categories: ["LocalStack Pro"]
description: >
  Get started with AWS Identity and Access Management (IAM) on LocalStack
aliases:
  - /aws/iam/
---

By default, LocalStack does not enforce security policies for client requests. In LocalStack Pro, the IAM security enforcement feature can be used to test your security policies and create a more realistic environment that more closely resembles real AWS.

{{< alert >}}**Note**:
The environment configuration `ENFORCE_IAM=1` is required to enable this feature. (By default, IAM enforcement is disabled, and all APIs can be accessed without authentication.)
{{< /alert >}}

### Creating IAM Users and Access Keys

By default, if no custom credentials are configured, requests made to LocalStack are running under the administrative root user:

{{< command >}}
$ awslocal sts get-caller-identity
{
    "UserId": "AKIAIOSFODNN7EXAMPLE",
    "Account": "000000000000",
    "Arn": "arn:aws:iam::000000000000:root"
}
{{< / command >}}

The following example illustrates how we can create a new user named `test`, then create an access key pair for the user, and assert that the user is recognized via `get-caller-identity` after the access keys are configured in the environment.

{{< command >}}
$ awslocal iam create-user --user-name test
...
$ awslocal iam create-access-key --user-name test
...
  "AccessKeyId": "AKIA4HPFP0TZHP3Z5VI6",
  "SecretAccessKey": "mwi/8Zhg8ypkJQmkdBq87UA3MbSa3x0HWnkcC/Ua",
...
$ export AWS_ACCESS_KEY_ID=AKIA4HPFP0TZHP3Z5VI6 AWS_SECRET_ACCESS_KEY=mwi/8Zhg8ypkJQmkdBq87UA3MbSa3x0HWnkcC/Ua
$ awslocal sts get-caller-identity
{
    "UserId": "b2yxf5g824zklfx5ry8o",
    "Account": "000000000000",
    "Arn": "arn:aws:iam::000000000000:user/test"
}
{{< / command >}}

### Enforcing IAM policies

Below is a simple example that illustrates the use of IAM policy enforcement. It first creates a user and obtains access/secret keys, then attempts to create a bucket with that user (which fails), and then finally attaches a policy to the user to allow `s3:CreateBucket`, which allows the bucket to be created.

For the following example we'll need two separate terminal sessions: terminal 1 for the administrative IAM commands (using the default root IAM user), and terminal 2 for the commands running under the test IAM user we're going to create.

Run these commands in **terminal 1**:
{{< command >}}
$ awslocal iam create-user --user-name test
...
$ awslocal iam create-access-key --user-name test
...
  "AccessKeyId": "AKIA4HPFP0TZHP3Z5VI6",
  "SecretAccessKey": "mwi/8Zhg8ypkJQmkdBq87UA3MbSa3x0HWnkcC/Ua",
...
{{< / command >}}

Then we switch to **terminal 2**, configure the access keys of user `test` in the environment, and then attempt to create an S3 bucket:
{{< command >}}
$ export AWS_ACCESS_KEY_ID=AKIA4HPFP0TZHP3Z5VI6 AWS_SECRET_ACCESS_KEY=mwi/8Zhg8ypkJQmkdBq87UA3MbSa3x0HWnkcC/Ua
$ awslocal s3 mb s3://mybucket
make_bucket failed: s3://mybucket An error occurred (AccessDeniedException) when calling the CreateBucket operation: Access to the specified resource is denied
{{< / command >}}

As expected, the bucket creation fails with `AccessDeniedException`, as user `test` lacks the required permissions. Now switch back to **terminal 1** and run these commands:
{{< command >}}
$ awslocal iam create-policy --policy-name p1 --policy-document '{"Version":"2012-10-17","Statement":[{"Effect":"Allow","Action":"s3:CreateBucket","Resource":"*"}]}'
...
$ awslocal iam attach-user-policy --user-name test --policy-arn arn:aws:iam::000000000000:policy/p1
{{< / command >}}

Now switch back to **terminal 2** and see how the bucket creation now succeeds with the `test` IAM user:
{{< command >}}
# confirm that we're using the credentials of the `test` user
$ awslocal sts get-caller-identity
...
    "Arn": "arn:aws:iam::000000000000:user/test"
...
$ awslocal s3 mb s3://mybucket
make_bucket: mybucket
{{< / command >}}

{{< alert >}}
**Note**: Credentials are currently extracted from the request (usually from the `Authorization` HTTP header), but the request signature itself is not validated - except for some cases, including S3 presigned URLs.
{{< /alert >}}


### Explainable IAM

Since 1.0, our policy engine logs output related to failed policy evaluation to the LocalStack log.
There, you can see which additional policies are necessary for your request to succeed.
You need to enable `DEBUG=1` to see these log messages.

For example, let us try to add a policy for creating Lambda functions, but only pass `lambda:CreateFunction` as allowed action - `iam:PassRole` (which is also required) is missing:

Our policy document `policy_1.json`:
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

Let us create a new user, put the policies, create access keys, and try to create a function with the user:

{{< command >}}
$ awslocal iam create-user --user-name test-user
{
    "User": {
        "Path": "/",
        "UserName": "test-user",
        "UserId": "x8a2eu4mc91yqtjazvhp",
        "Arn": "arn:aws:iam::000000000000:user/test-user",
        "CreateDate": "2022-07-05T16:08:25.741000+00:00"
    }
}
$ awslocal iam put-user-policy --user-name test-user --policy-name policy1 --policy-document file://policy_1.json
$ awslocal iam create-access-key --user-name test-user
$ export AWS_ACCESS_KEY_ID=...
$ export AWS_SECRET_ACCESS_KEY=...
$ awslocal lambda create-function --function-name test-function --role arn:aws:iam::000000000000:role/lambda-role --runtime python3.8 --handler handler.handler --zip-file fileb://function.zip
An error occurred (AccessDeniedException) when calling the CreateFunction operation: Access to the specified resource is denied
{{< / command >}}

When looking in the LocalStack logs, we can now see 5 log entries specific to that (denied) request:

```
INFO:localstack_ext.services.iam.policy_engine.handler: Request for service lambda for operation CreateFunction denied.
DEBUG:localstack_ext.services.iam.policy_engine.handler: Necessary permissions for this action: ["Action 'lambda:CreateFunction' for 'arn:aws:lambda:us-east-1:000000000000:function:test-function'", "Action 'iam:PassRole' for 'arn:aws:iam::000000000000:role/lambda-role'"]
DEBUG:localstack_ext.services.iam.policy_engine.handler: 0 permissions have been explicitly denied: []
DEBUG:localstack_ext.services.iam.policy_engine.handler: 1 permissions have been explicitly allowed: ["Action 'lambda:CreateFunction' for 'arn:aws:lambda:us-east-1:000000000000:function:test-function'"]
DEBUG:localstack_ext.services.iam.policy_engine.handler: 1 permissions have been implicitly denied: ["Action 'iam:PassRole' for 'arn:aws:iam::000000000000:role/lambda-role'"]
```

So we can see the action `iam:PassRole` is not allowed but implicitly denied (meaning there is no explicit deny statement in the applicable policies, but no allow either) for your user for resource `arn:aws:iam::000000000000:role/lambda-role`.
If we now add this to our policy (since it is an example let's do it very simple with the same wildcard resource):

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

the call is correctly executed.

#### Soft Mode

If you enable `IAM_SOFT_MODE=1`, you can look at the logs whether your requests would have been denied or not, while still being able to execute your whole stack without interference.
This is especially useful when trying to find missing permissions over a whole stack (with resources depending on each other) at a time without having to redeploy for every missing permission.

{{< alert >}}
**Note**: As of 1.0, resource based policies and conditions are not yet supported. Please try sticking to identity-based policies where possible.
Inter-service communication evaluation (for example for sts:AssumeRole) also is not supported, which currently reduces the impact of those missing features.
{{< /alert >}}

### Supported APIs

IAM security enforcement is available for all AWS APIs in LocalStack - it has been thoroughly tested, among others, for the following services: ACM, API Gateway, CloudFormation, CloudWatch (metrics/events/logs), DynamoDB, DynamoDB Streams, Elasticsearch Service, EventBus, Kinesis, KMS, Lambda, Redshift, S3, SecretsManager, SNS, SQS.
