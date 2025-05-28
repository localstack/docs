---
title: "Resource Groups"
linkTitle: "Resource Groups"
tags: ["Free"]
description: >
  Get started with Resource Groups on LocalStack
---

## Introduction

Resource Groups allow developers to organize and manage their AWS resources more efficiently.
Resource Groups allow for a unified view of their resources allowing developers to perform specific actions, such as resource tagging, access control, and policy enforcement across multiple resources simultaneously.
Resource Groups in AWS provide two types of queries that developers can use to build groups: Tag-based queries and CloudFormation stack-based queries.
With Tag-based queries, developers can organize resources based on common attributes or characteristics, while CloudFormation stack-based queries allow developers to group resources that are deployed together as part of a CloudFormation stack.

LocalStack allows you to use the Resource Groups APIs in your local environment to group and categorize resources based on criteria such as tags, resource types, regions, or custom attributes.
The supported APIs are available on our [API coverage page](https://docs.localstack.cloud/references/coverage/coverage_resource-groups/), which provides information on the extent of Resource Group's integration with LocalStack.

## Getting Started

This guide is designed for users new to Resource Groups and assumes basic knowledge of the AWS CLI and our [`awslocal`](https://github.com/localstack/awscli-local) wrapper script.

Start your LocalStack container using your preferred method.
We will demonstrate how to create a Resource Group using the AWS CLI.
We will use tag-based query to create a resource group.
However, you can also use CloudFormation stack-based queries to create a resource group.

### Create a Resource Group

Resource Groups in AWS are built around the concept of queries, which serve as a fundamental component.
The tag-based queries list the resource types in the format `AWS::<service>::<resource>` (e.g. `AWS::Lambda::Function` along with specified tags.
A tag-based group is created based on a query of type `TAG_FILTERS_1_0`.

Use the [`CreateGroup`](https://docs.aws.amazon.com/resource-groups/latest/APIReference/API_CreateGroup.html) API to create a Resource Group.
Run the following command to create a Resource Group named `my-resource-group`:

{{< command >}}
$ awslocal resource-groups create-group \
    --name my-resource-group \
    --resource-query '{"Type":"TAG_FILTERS_1_0","Query":"{\"ResourceTypeFilters\":[\"AWS::EC2::Instance\"],\"TagFilters\":[{\"Key\":\"Stage\",\"Values\":[\"Test\"]}]}"}'
{{< /command >}}

You can also specify `AWS::AllSupported` as the `ResourceTypeFilters` value to include all supported resource types in the group.

### Update a Resource Group

To update a Resource Group, use the [`UpdateGroup`](https://docs.aws.amazon.com/resource-groups/latest/APIReference/API_UpdateGroup.html) API.
Execute the following command to update the Resource Group `my-resource-group`:

{{< command >}}
awslocal resource-groups update-group \
    --group-name my-resource-group \
    --description "EC2 S3 buckets and RDS DBs that we are using for the test stage"
{{< /command >}}

Furthermore, you can also update the query and tags associated with a Resource Group using the [`UpdateGroup`](https://docs.aws.amazon.com/resource-groups/latest/APIReference/API_UpdateGroup.html) API.
Run the following command to update the query and tags of the Resource Group `my-resource-group`:

{{< command >}}
awslocal resource-groups update-group-query \
    --group-name my-resource-group \
    --resource-query '{"Type":"TAG_FILTERS_1_0","Query":"{\"ResourceTypeFilters\":[\"AWS::EC2::Instance\",\"AWS::S3::Bucket\",\"AWS::RDS::DBInstance\"],\"TagFilters\":[{\"Key\":\"Stage\",\"Values\":[\"Test\"]}]}"}'
{{< /command >}}

### Delete a Resource Group

To delete a Resource Group, use the [`DeleteGroup`](https://docs.aws.amazon.com/resource-groups/latest/APIReference/API_DeleteGroup.html) API.
Run the following command to delete the Resource Group `my-resource-group`:

{{< command >}}
$ awslocal resource-groups delete-group \
    --group-name my-resource-group
{{< /command >}}
