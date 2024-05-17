---
title: "Identity and Access Management (IAM)"
linkTitle: "Identity and Access Management (IAM)"
description: Get started with AWS Identity and Access Management (IAM) on LocalStack
persistence: supported

---

## Introduction

Identity and Access Management (IAM) is a web service provided by Amazon Web Services (AWS) that enables users to control access to AWS resources securely. IAM allows organizations to create and manage AWS users, groups, and roles, defining granular permissions to access specific AWS services and resources. By centralizing access control, administrators can enforce the principle of least privilege, ensuring users have only the necessary permissions for their tasks.

LocalStack allows you to use the IAM APIs in your local environment to create and manage users, groups, and roles, granting permissions that adhere to the principle of least privilege. The supported APIs are available on our [API coverage page](https://docs.localstack.cloud/references/coverage/coverage_iam/), which provides information on the extent of IAM's integration with LocalStack.

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
```

You can save the `AccessKeyId` and `SecretAccessKey` values, and export them in the environment to run commands under the `test` user. Run the following command:

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
