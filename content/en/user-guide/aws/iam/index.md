---
title: "Identity and Access Management (IAM)"
linkTitle: "Identity and Access Management (IAM)"
description: >
  Get started with AWS Identity and Access Management (IAM) on LocalStack
---

## Introduction

Identity and Access Management (IAM) is a web service provided by Amazon Web Services (AWS) that enables users to control access to AWS resources securely. IAM allows organizations to create and manage AWS users, groups, and roles, defining granular permissions to access specific AWS services and resources. By centralizing access control, administrators can enforce the principle of least privilege, ensuring users have only the necessary permissions for their tasks.

LocalStack supports IAM via the Community offering, allowing you to use the IAM APIs in your local environment to create and manage users, groups, and roles, granting permissions that adhere to the principle of least privilege. The supported APIs are available on our [API coverage page](https://docs.localstack.cloud/references/coverage/coverage_iam/), which provides information on the extent of IAM's integration with LocalStack.

## Getting started

This guide is designed for users new to IAM and assumes basic knowledge of the AWS CLI and our [`awslocal`](https://github.com/localstack/awscli-local) wrapper script.

Start your LocalStack container using your preferred method. We will demonstrate how you can create a new user named `test`, create an access key pair for the user, and assert that the user is recognized after the access keys are configured in the environment.

By default, in the absence of custom credentials configuration, all requests to LocalStack run under the administrative root user. Run the following command to use the [`GetCallerIdentity`](https://docs.aws.amazon.com/cli/latest/reference/sts/get-caller-identity.html) API to confirm that the request is running under the root user:

{{< command >}}
$ awslocal sts get-caller-identity
{{< / command >}}

You can see an output similar to the following:

```bash
{
    "UserId": "AKIAIOSFODNN7EXAMPLE",
    "Account": "000000000000",
    "Arn": "arn:aws:iam::000000000000:root"
}
```

You can now create a new user named `test` using the [`CreateUser`](https://docs.aws.amazon.com/cli/latest/reference/iam/create-user.html) API. Run the following command:

{{< command >}}
$ awslocal iam create-user --user-name test
{{< / command >}}

You can now create an access key pair for the user using the [`CreateAccessKey`](https://docs.aws.amazon.com/cli/latest/reference/iam/create-access-key.html) API. Run the following command:

{{< command >}}
$ awslocal iam create-access-key --user-name test
{{< / command >}}

You can see an output similar to the following:

```bash
{
    "AccessKey": {
        "UserName": "test",
        "AccessKeyId": "LKIAQAAAAAAAGFWKCM5F",
        "Status": "Active",
        "SecretAccessKey": "DUulXk2N2yD6rgoBBR9A/5iXa6dBcLyDknr925Q5",
        "CreateDate": "2023-07-25T09:36:51+00:00"
    }
}
...

You can save te `AccessKeyId` and `SecretAccessKey` values, and export them in the environment to run commands under the `test` user. Run the following command:

{{< command >}}
$ export AWS_ACCESS_KEY_ID=LKIAQAAAAAAAGFWKCM5F AWS_SECRET_ACCESS_KEY=DUulXk2N2yD6rgoBBR9A/5iXa6dBcLyDknr925Q5
$ awslocal sts get-caller-identity
{
    "UserId": "b2yxf5g824zklfx5ry8o",
    "Account": "000000000000",
    "Arn": "arn:aws:iam::000000000000:user/test"
}
{{< / command >}}

You can see that the request is now running under the `test` user.

## Enforcing IAM Policies

The Pro/Team offering provides the IAM security enforcement feature that can be used to test your security policies and create a more realistic environment that more closely resembles real AWS. The environment configuration `ENFORCE_IAM=1` is required while starting LocalStack to enable this feature. In LocalStack, IAM enforcement is disabled, and all APIs can be accessed without authentication.

Presented below is a straightforward example showcasing the implementation of IAM policy enforcement. Initially, it involves creating a user and obtaining access/secret keys. Subsequently, an attempt is made to create a bucket using that user's credentials, which inevitably fails due to insufficient permissions. Lastly, a policy is attached to the user, granting the necessary `s3:CreateBucket` permission, thereby enabling the successful creation of the bucket.

To follow this example, please open two separate terminal sessions: **Terminal 1** for the administrative IAM commands, which will utilize the default root IAM user, and **Terminal 2** for executing the commands under the test IAM user we're about to create. This way, we can demonstrate the differentiation in access permissions between the administrative and test users in real-time.

In **Terminal 1**, execute the following commands:

{{< command >}}
$ awslocal iam create-user --user-name test
...
$ awslocal iam create-access-key --user-name test
...
  "AccessKeyId": "AKIA4HPFP0TZHP3Z5VI6",
  "SecretAccessKey": "mwi/8Zhg8ypkJQmkdBq87UA3MbSa3x0HWnkcC/Ua",
...
{{< / command >}}

Navigate to **Terminal 2**, where we will configure the access keys for the user `test` in the environment. Once the access keys are set, you will attempt to create an S3 bucket using these credentials.

{{< command >}}
$ export AWS_ACCESS_KEY_ID=AKIA4HPFP0TZHP3Z5VI6 AWS_SECRET_ACCESS_KEY=mwi/8Zhg8ypkJQmkdBq87UA3MbSa3x0HWnkcC/Ua
$ awslocal s3 mb s3://mybucket
make_bucket failed: s3://mybucket An error occurred (AccessDeniedException) when calling the CreateBucket operation: Access to the specified resource is denied
{{< / command >}}

As anticipated, the attempt to create the bucket fails with an `AccessDeniedException` error, confirming that user `test` lacks the necessary permissions for this action. 

Let's now return to **Terminal 1** and execute the following commands:

{{< command >}}
$ awslocal iam create-policy --policy-name p1 --policy-document '{"Version":"2012-10-17","Statement":[{"Effect":"Allow","Action":"s3:CreateBucket","Resource":"*"}]}'
...
$ awslocal iam attach-user-policy --user-name test --policy-arn arn:aws:iam::000000000000:policy/p1
{{< / command >}}

Now, let's switch back to **Terminal 2** and observe how the bucket creation succeeds with the `test` IAM user:

{{< command >}}
# confirm that we're using the credentials of the `test` user
$ awslocal sts get-caller-identity
...
    "Arn": "arn:aws:iam::000000000000:user/test"
...
$ awslocal s3 mb s3://mybucket
make_bucket: mybucket
{{< / command >}}

{{< alert title="Note">}}
Currently, credentials are extracted from the request, typically from the `Authorization` HTTP header. However, it's important to note that the request signature is not fully validated, with a few exceptions, such as S3-presigned URLs.
{{< /alert >}}

## Explainable IAM

The IAM policy engine logs output related to failed policy evaluation directly to the LocalStack log. You can enable `DEBUG=1` to gain visibility into these log messages, allowing you to identify the additional policies required for your request to succeed.

For instance, if you attempt to add a policy for creating Lambda functions but only permit `lambda:CreateFunction` as an allowed action while overlooking the necessity of `iam:PassRole`, the policy engine's log will highlight this missing permission.

Create a policy document named `policy_1.json`:

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

You will now proceed with creating a new user, attaching the necessary policies, generating access keys, and attempting to create a function using the newly created user's credentials.

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

Upon inspecting the LocalStack logs, we can now observe the presence of five log entries directly related to the denied request.

```bash
INFO:localstack_ext.services.iam.policy_engine.handler: Request for service lambda for operation CreateFunction denied.
DEBUG:localstack_ext.services.iam.policy_engine.handler: Necessary permissions for this action: ["Action 'lambda:CreateFunction' for 'arn:aws:lambda:us-east-1:000000000000:function:test-function'", "Action 'iam:PassRole' for 'arn:aws:iam::000000000000:role/lambda-role'"]
DEBUG:localstack_ext.services.iam.policy_engine.handler: 0 permissions have been explicitly denied: []
DEBUG:localstack_ext.services.iam.policy_engine.handler: 1 permissions have been explicitly allowed: ["Action 'lambda:CreateFunction' for 'arn:aws:lambda:us-east-1:000000000000:function:test-function'"]
DEBUG:localstack_ext.services.iam.policy_engine.handler: 1 permissions have been implicitly denied: ["Action 'iam:PassRole' for 'arn:aws:iam::000000000000:role/lambda-role'"]
```

So we can see the action `iam:PassRole` is not allowed but implicitly denied (meaning there is no explicit deny statement in the applicable policies, but no allow either) for your user for resource `arn:aws:iam::000000000000:role/lambda-role`.
If we now add this to our policy (since it is an example let's do it very simple with the same wildcard resource):

Upon examination, it becomes apparent that the action `iam:PassRole` is not allowed; rather, it is implicitly denied for your user concerning the resource `arn:aws:iam::000000000000:role/lambda-role`. This implies that there is no explicit deny statement in the relevant policies, but there is also no allow statement, resulting in the implicit denial of the action.

You can incorporate this action into the policy. For illustrative purposes, we will keep the example straightforward, using the same wildcard resource.

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

You will notice that the request is now successful, and the function is created.

### Soft Mode

Enabling `IAM_SOFT_MODE=1` allows you to review the logs and assess whether your requests would have been denied or granted while executing your entire stack without disruptions. You can avoid the need for redeployment to address each missing permission individually, streamlining the debugging process and enhancing the efficiency of your IAM configurations.

## Resource Browser

The LocalStack Web Application provides a Resource Browser for managing IAM users, groups, and roles. You can access the Resource Browser by opening the LocalStack Web Application in your browser, navigating to the **Resources** section, and then clicking on **IAM** under the **Security Identity Compliance** section.

<img src="iam-resource-browser.png" alt="IAM Resource Browser" title="IAM Resource Browser" width="900" />

The Resource Browser allows you to perform the following actions:

- **Create User, Group, Role, and Policy**: Create a new IAM user, group, or role by clicking the top-level **Create** button and filling out the form.
- **View User, Group, Role, and Policy Details**: Click on any of the listed resources to view its details by clicking on the desired User, Group, Role, or Policy.
- **Edit User, Group, Role, and Policy Details**: Click on any listed resources to edit its details by clicking on the desired User, Group, Role, or Policy.
- **Delete User, Group, Role, and Policy**: Select any listed resources to delete them by clicking the **Actions** button and selecting **Remove Selected**.

## Supported APIs

IAM security enforcement is comprehensively available for all AWS APIs in LocalStack and has undergone thorough testing across multiple services. The services that have been rigorously tested include:

- ACM
- API Gateway
- CloudFormation
- CloudWatch (metrics/events/logs)
- DynamoDB
- DynamoDB Streams
- Elasticsearch Service
- EventBus, Kinesis
- KMS
- Lambda
- Redshift
- S3
- SecretsManager
- SNS
- SQS

## Examples

The following code snippets and sample applications provide practical examples of how to use IAM in LocalStack for various use cases:

- [Serverless Container-based APIs with Amazon ECS & API Gateway](https://github.com/localstack/serverless-api-ecs-apigateway-sample)
- [Event-driven architecture with Amazon SNS FIFO, DynamoDB, Lambda, and S3](https://github.com/localstack/event-driven-architecture-with-amazon-sns-fifo)
- [Full-Stack application with AWS Lambda, DynamoDB & S3 for shipment validation](https://github.com/localstack/shipment-list-demo)
- [Enforcement of IAM policies when working with local cloud APIs](https://github.com/localstack/localstack-pro-samples/tree/master/iam-policy-enforcement)
