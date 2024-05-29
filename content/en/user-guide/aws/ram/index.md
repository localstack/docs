---
title: "Resource Access Manager (RAM)"
linkTitle: "Resource Access Manager (RAM)"
description: Get started with RAM on LocalStack
---

Resource Access Manager (RAM) helps resources to be shared across AWS accounts, within or across organizations.

On AWS, RAM is an abstraction on top of AWS Identity and Access Management (IAM) which can manage resource-based policies to supported resource types.

LocalStack supports RAM in the Pro edition.
The supported API operations can be found on the [API coverage page](https://docs.localstack.cloud/references/coverage/coverage_ram/).

## Getting started

Start the LocalStack container using your preferred method.
This section will illustrate how to create permissions and resource shares using the AWS CLI.

### Create a permission

{{< command >}}
$ awslocal ram create-permission \
    --name example \
    --resource-type appsync:apis \
    --policy-template '{"Effect": "Allow", "Action": "appsync:SourceGraphQL"}'
{{< /command >}}

### Create a resource share

{{< command >}}
$ awslocal ram create-resource-share \
    --name example-resource-share \
    --principals arn:aws:organizations::000000000000:organization/o-truopwybwi \
    --resource-arn arn:aws:appsync:eu-central-1:000000000000:apis/wcgmjril5wuyvhmpildatuaat3
{{< /command >}}

## Current Limitations

RAM on LocalStack currently functions as a CRUD interface only.
Resource shares do not lead to IAM policies being created or attached to resources. 
This means that the specified principals do not end up being granted access to the specified resources.
