---
title: "IAM Policy Enforcement"
linkTitle: "IAM Policy Enforcement"
weight: 1
description: Enforce IAM policies in LocalStack to test your policies
tags: ["Pro image"]
---

## Introduction

IAM Policy Enforcement feature can be used to test your security policies and create a more realistic environment that more closely resembles real AWS.
The environment configuration `ENFORCE_IAM=1` is required while starting LocalStack to enable this feature.
Per default, IAM enforcement is disabled, and all APIs can be accessed without authentication.

## Getting started

This guide is designed for users new to IAM Policy Enforcement and assumes basic knowledge of the AWS CLI and our [`awslocal`](https://github.com/localstack/awscli-local) wrapper script.

Start your LocalStack container with the `DEBUG=1` and `ENFORCE_IAM=1` environment variables set:

{{< command >}}
$ DEBUG=1 ENFORCE_IAM=1 localstack start
{{< /command >}}

We will demonstrate IAM Policy Enforcement, by creating a user and obtaining the access/secret keys.
We will make an attempt to create a bucket using the user’s credentials, which inevitably fails due to insufficient permissions.

Lastly, a policy is attached to the user, granting the necessary `s3:CreateBucket` permission, thereby enabling the successful creation of the bucket.

### Create a user

To follow this guide, open two separate terminal sessions:  **Terminal 1**  for the administrative IAM commands, which will utilize the default root IAM user, and  **Terminal 2** for executing the commands under the test IAM user you are about to create.
This way, we can demonstrate the differentiation in access permissions between the administrative and test users in real-time.

In **Terminal 1**, execute the following commands to create a `test` user and obtain the access/secret keys:

{{< command >}}
$ awslocal iam create-user --user-name test
<disable-copy>
{
    "User": {
        "Path": "/",
        "UserName": "test",
        "UserId": "d7ryukg7bls4rq1ihq1d",
        "Arn": "arn:aws:iam::000000000000:user/test",
        "CreateDate": "2023-11-03T12:20:12.332000Z"
    }
}
</disable-copy>
$ awslocal iam create-access-key --user-name test
<disable-copy>
{
    "AccessKey": {
        "UserName": "test",
        "AccessKeyId": "LKIAQAAAAAAAHFR7QTN3",
        "Status": "Active",
        "SecretAccessKey": "EYUHpIol7bRJpKd/28c/LI2C4bbEnp82LJCRwXRV",
        "CreateDate": "2023-11-03T12:20:27Z"
    }
}
</disable-copy>
{{< / command >}}

### Attempt to create a bucket

Navigate to **Terminal 2**, where we will configure the access keys for the user `test` in the environment.
Once the access keys are set, you will attempt to create an S3 bucket using these credentials.

{{< command >}}
$ export AWS_ACCESS_KEY_ID=LKIAQAAAAAAAHFR7QTN3 AWS_SECRET_ACCESS_KEY=EYUHpIol7bRJpKd/28c/LI2C4bbEnp82LJCRwXRV
$ awslocal s3 mb s3://mybucket
<disable-copy>
make_bucket failed: s3://mybucket An error occurred (AccessDeniedException) when calling the CreateBucket operation: Access to the specified resource is denied
</disable-copy>
{{< / command >}}

As anticipated, the attempt to create the bucket fails with an `AccessDeniedException` error, confirming that user `test` lacks the necessary permissions for this action.
You can view the LocalStack logs to validate the policy enforcement:

```bash
2023-11-03T12:21:10.971  INFO --- [   asgi_gw_1] l.s.i.p.handler            : Request for service 's3' by principal 'arn:aws:iam::000000000000:user/test' for operation 'CreateBucket' denied.
2023-11-03T12:21:10.972  INFO --- [   asgi_gw_1] localstack.request.aws     : AWS s3.CreateBucket => 403 (AccessDenied)
```

### Attach a policy to the user

Let's now return to **Terminal 1** and execute the following commands to attach a policy to the user `test`:

{{< command >}}
$ awslocal iam create-policy --policy-name p1 --policy-document '{"Version":"2012-10-17","Statement":[{"Effect":"Allow","Action":"s3:CreateBucket","Resource":"*"}]}'
$ awslocal iam attach-user-policy --user-name test --policy-arn arn:aws:iam::000000000000:policy/p1
{{< / command >}}

### Create a bucket

Now, let's switch back to **Terminal 2** and observe how the bucket creation succeeds with the `test` IAM user:

{{< command >}}
$ awslocal s3 mb s3://mybucket
<disable-copy>
make_bucket: mybucket
</disable-copy>
{{< / command >}}

The bucket creation succeeds, confirming that the user `test` now has the necessary permissions to perform this action.
You can view the LocalStack logs to validate the policy enforcement:

```bash
2023-11-03T12:23:11.469  INFO --- [   asgi_gw_1] localstack.request.aws     : AWS iam.CreatePolicy => 200
2023-11-03T12:23:15.753  INFO --- [   asgi_gw_1] localstack.request.aws     : AWS iam.AttachUserPolicy => 200
2023-11-03T12:23:22.795  INFO --- [   asgi_gw_2] localstack.request.aws     : AWS s3.CreateBucket => 200
```

You can further use the IAM Policy Enforcement feature to test your Infrastructure as Code (IaC) deployments and ensure that your policies are correctly enforced.
If the IAM policies are not correctly enforced, you will get an unsuccessful response from the API call, and the LocalStack logs will provide you with the necessary information to debug the issue.

## Feature coverage

The feature coverage is documented in the [IAM coverage documentation]({{ ref "iam-coverage"}}.
