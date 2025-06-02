---
title: "Resource Access Manager (RAM)"
linkTitle: "Resource Access Manager (RAM)"
description: Get started with RAM on LocalStack
tags: ["Ultimate"]
---

## Introduction

Resource Access Manager (RAM) helps resources to be shared across AWS accounts, within or across organizations.
On AWS, RAM is an abstraction on top of AWS Identity and Access Management (IAM) which can manage resource-based policies to supported resource types.
The API operations supported by LocalStack can be found on the [API coverage page]({{< ref "coverage_ram" >}}).

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

LocalStack RAM supports emulated sharing for EC2 Subnets only.
Only specified account principals are granted access to the shared subnets, and associated VPC and route tables.
Furthermore, only the sharing aspect is implemented at this time.
No IAM policies are created or attached, and no permission enforcement takes place.

For all other resource types, the functionality is limited to mocking.
