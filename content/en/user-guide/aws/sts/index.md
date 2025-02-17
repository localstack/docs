---
title: "Security Token Service (STS)"
linkTitle: "Security Token Service (STS)"
aliases:
- /user-guide/aws/security-token-service/
description: Get started with Security Token Service on LocalStack
persistence: supported

---

## Introduction

Security Token Service (STS) is a service provided by Amazon Web Services (AWS) that enables you to grant temporary, limited-privilege credentials to users and applications.
STS implements fine-grained access control and reduce the exposure of your long-term credentials.
The temporary credentials, known as security tokens, can be used to access AWS services and resources based on the permissions specified in the associated policies.

LocalStack allows you to use the STS APIs in your local environment to request security tokens, manage permissions, integrate with identity providers, and more.
The supported APIs are available on our [API coverage page](https://docs.localstack.cloud/references/coverage/coverage_sts/), which provides information on the extent of STS's integration with LocalStack.

## Getting started

This guide is designed for users new to STS and assumes basic knowledge of the AWS CLI and our [`awslocal`](https://github.com/localstack/awscli-local) wrapper script.

Start your LocalStack container using your preferred method.
We will demonstrate how to assume an IAM Role and assume the role as well as creating an IAM user and getting using the STS with the AWS CLI.

### Create an IAM User and get temporary Credentials

You can create an IAM User and Role using the [`CreateUser`](https://docs.aws.amazon.com/STS/latest/APIReference/API_CreateUser.html) API.
The IAM User will be used to assume the IAM Role.
Run the following command to create an IAM User, named `localstack-user`:

{{< command >}}
$ awslocal iam create-user \
    --user-name localstack-user
{{< /command >}}

You can generate long-term access keys for the IAM user using the [`CreateAccessKey`](https://docs.aws.amazon.com/STS/latest/APIReference/API_CreateAccessKey.html) API.
Run the following command to create an access key for the IAM user:

{{< command >}}
$ awslocal iam create-access-key \
    --user-name localstack-user
{{< /command >}}

The following output would be retrieved:

```bash
{
    "AccessKey": {
        "UserName": "localstack-user",
        "AccessKeyId": "ACCESS_KEY_ID",
        "Status": "Active",
        "SecretAccessKey": "SECRET_ACCESS_KEY",
        "CreateDate": "2023-08-24T17:16:16Z"
    }
}
```

Using STS, you can also fetch temporary credentials for this user using the [`GetSessionToken`](https://docs.aws.amazon.com/STS/latest/APIReference/API_GetSessionToken.html) API.
Run the following command using your long-term credentials to get your temporary credentials:

{{< command >}}
$ awslocal sts get-session-token
{{< /command >}}

The following output would be retrieved:

```bash
{
    "Credentials": {
        "AccessKeyId": "ACCESS_KEY_ID",
        "SecretAccessKey": "SECRET_ACCESS_KEY",
        "SessionToken": "SESSION_TOKEN",
        "Expiration": "TIMESTAMP"
    }
}
```

### Create an IAM Role

You can now create an IAM Role, named `localstack-role`, using the [`CreateRole`](https://docs.aws.amazon.com/STS/latest/APIReference/API_CreateRole.html) API.
Run the following command to create the IAM Role:

{{< command >}}
$ awslocal iam create-role \
    --role-name localstack-role \
    --assume-role-policy-document '{"Version":"2012-10-17","Statement":[{"Effect":"Allow","Principal":{"AWS":"arn:aws:iam::000000000000:root"},"Action":"sts:AssumeRole"}]}'
{{< /command >}}

The following output would be retrieved:

```bash
{
    "Role": {
        "Path": "/",
        "RoleName": "localstack-role",
        "RoleId": "AROAQAAAAAAAEDP262HSR",
        "Arn": "arn:aws:iam::000000000000:role/localstack-role",
        "CreateDate": "2023-08-24T17:17:13.632000Z",
        "AssumeRolePolicyDocument": {
            "Version": "2012-10-17",
            "Statement": [
                {
                    "Effect": "Allow",
                    "Principal": {
                        "AWS": "arn:aws:iam::000000000000:root"
                    },
                    "Action": "sts:AssumeRole"
                }
            ]
        }
    }
}
```

You can attach the policy to the IAM role using the [`AttachRolePolicy`](https://docs.aws.amazon.com/STS/latest/APIReference/API_AttachRolePolicy.html) API.
Run the following command to attach the policy to the IAM role:

{{< command >}}
$ awslocal iam attach-role-policy \
    --role-name localstack-role \
    --policy-arn arn:aws:iam::aws:policy/AdministratorAccess
{{< /command >}}

### Assume an IAM Role

You can assume an IAM Role using the [`AssumeRole`](https://docs.aws.amazon.com/STS/latest/APIReference/API_AssumeRole.html) API.
Run the following command to assume the IAM Role:

{{< command >}}
$ awslocal sts assume-role \
    --role-arn arn:aws:iam::000000000000:role/localstack-role \
    --role-session-name localstack-session
{{< /command >}}

The following output would be retrieved:

```bash
{
    "Credentials": {
        "AccessKeyId": "ACCESS_KEY_ID",
        "SecretAccessKey": "SECRET_ACCESS_KEY",
        "SessionToken": "SESSION_TOKEN",
        "Expiration": "TIMESTAMP",
    },
    "AssumedRoleUser": {
        "AssumedRoleId": "AROAQAAAAAAAEDP262HSR:localstack-session",
        "Arn": "arn:aws:sts::000000000000:assumed-role/localstack-role/localstack-session"
    },
    "PackedPolicySize": 6
}
```

You can use the temporary credentials in your applications for temporary access.

### Get caller identity

You can get the caller identity to identify the principal your current credentials are valid for using the [`GetCallerIdentity`](https://docs.aws.amazon.com/STS/latest/APIReference/API_GetCallerIdentity.html) API.
Run the following command to get the caller identity for the credentials set in your environment:

{{< command >}}
$ awslocal sts get-caller-identity
{{< /command >}}

The following output would be retrieved:

```bash
{
    "UserId": "AKIAIOSFODNN7EXAMPLE",
    "Account": "000000000000",
    "Arn": "arn:aws:iam::000000000000:root"
}
```
