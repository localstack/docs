---
title: "Lake Formation"
linkTitle: "Lake Formation"
description: Get started with Lake Formation on LocalStack
tags: ["Ultimate"]
---

## Introduction

Lake Formation is a managed service that allows users to build, secure, and manage data lakes.
Lake Formation allows users to define and enforce fine-grained access controls, manage metadata, and discover and share data across multiple data sources.

LocalStack allows you to use the Lake Formation APIs in your local environment to register resources, grant permissions, and list resources and permissions.
The supported APIs are available on our [API coverage page]({{< ref "coverage_lakeformation" >}}), which provides information on the extent of Lake Formation's integration with LocalStack.

## Getting started

This guide is designed for users new to Lake Formation and assumes basic knowledge of the AWS CLI and our [`awslocal`](https://github.com/localstack/awscli-local) wrapper script.

Start your LocalStack container using your preferred method.
We will demonstrate how to register an S3 bucket as a resource in Lake Formation, grant permissions to a user, and list the resources and permissions.

### Register the resource

Create a new S3 bucket named `test-bucket` using the `mb` command:

{{< command >}}
$ awslocal s3 mb s3://test-bucket
{{</ command >}}

You can now register the S3 bucket as a resource in Lake Formation using the [`RegisterResource`](https://docs.aws.amazon.com/lake-formation/latest/dg/API_RegisterResource.html) API.
Create a file named `input.json` with the following content:

```json
{
    "ResourceArn": "arn:aws:s3:::test-bucket",
    "UseServiceLinkedRole": true
}
```

Run the following command to register the resource:

{{< command >}}
awslocal lakeformation register-resource \
    --cli-input-json file://input.json
{{</ command >}}

### List resources

You can list the registered resources using the [`ListResources`](https://docs.aws.amazon.com/lake-formation/latest/dg/API_ListResources.html) API.
Execute the following command to list the resources:

{{< command >}}
awslocal lakeformation list-resources
{{</ command >}}

The following output is displayed:

```bash
{
    "ResourceInfoList": [
        {
            "ResourceArn": "arn:aws:s3:::test-bucket",
            "LastModified": "2024-07-11T23:27:30.699312+05:30"
        }
    ]
}
```

### Grant permissions

You can grant permissions to a user or group using the [`GrantPermissions`](https://docs.aws.amazon.com/lake-formation/latest/dg/API_GrantPermissions.html) API.
Create a file named `permissions.json` with the following content:

```json
{
    "CatalogId": "000000000000",
    "Principal": {
        "DataLakePrincipalIdentifier": "arn:aws:iam::000000000000:user/lf-developer"
    },
    "Resource": {
        "Table": {
            "CatalogId": "000000000000",
            "DatabaseName": "tpc",
            "TableWildcard": {}
        }
    },
    "Permissions": [
        "SELECT"
    ],
    "PermissionsWithGrantOption": []
}
```

Run the following command to grant permissions:

{{< command >}}
$ awslocal lakeformation grant-permissions \
    --cli-input-json file://check.json
{{</ command >}}

### List permissions

You can list the permissions granted to a user or group using the [`ListPermissions`](https://docs.aws.amazon.com/lake-formation/latest/dg/API_ListPermissions.html) API.
Execute the following command to list the permissions:

{{< command >}}
$ awslocal lakeformation list-permissions
{{</ command >}}
