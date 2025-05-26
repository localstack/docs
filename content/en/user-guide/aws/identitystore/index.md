---
title: "Identity Store"
linkTitle: "Identity Store"
description: Get started with Identity Store on LocalStack
tags: ["Ultimate"]
---

## Introduction

Identity Store is a managed service that enables the creation and management of groups within your AWS environment.
Groups are used to manage access to AWS resources, and Identity Store provides a central location to create and manage groups across your AWS accounts.

LocalStack allows you to use the Identity Store APIs to create and manage groups in your local environment.
The supported APIs are available on our [API Coverage Page](https://docs.localstack.cloud/references/coverage/coverage_identitystore/), which provides information on the extent of Identity Store integration with LocalStack.

## Getting started

This guide is aimed at users who are familiar with the AWS CLI and [`awslocal`](https://github.com/localstack/awscli-local) wrapper script.
It will walk you through the basics of setting up and managing groups within the AWS Identity Store using LocalStack.

Start your LocalStack container using your preferred method.
This guide will demonstrate how to create a group within Identity Store, list all groups, and describe a specific group.

### Create a Group in Identity Store

You can create a new group in the Identity Store using the [`CreateGroup`](https://docs.aws.amazon.com/singlesignon/latest/IdentityStoreAPIReference/API_CreateGroup.html) API.
Execute the following command to create a group with an identity store ID of `testls`:

{{< command >}}
$ awslocal identitystore create-group --identity-store-id testls
<disable-copy>
{
    "GroupId": "38cec731-de22-45bf-9af7-b74457bba884",
    "IdentityStoreId": "testls"
}
</disable-copy>
{{< / command >}}

Copy the `GroupId` value from the output, as it will be needed in subsequent steps.

### List all Groups in Identity Store

After creating groups, you might want to list all groups within the Identity Store to manage or review them.
Run the following command to list all groups using the [`ListGroups`](https://docs.aws.amazon.com/singlesignon/latest/IdentityStoreAPIReference/API_ListGroups.html) API:

{{< command >}}
$ awslocal identitystore list-groups --identity-store-id testls
<disable-copy>
{
    "Groups": [
        {
            "GroupId": "38cec731-de22-45bf-9af7-b74457bba884",
            "ExternalIds": [],
            "IdentityStoreId": "testls"
        }
    ]
}
</disable-copy>
{{< / command >}}

This command returns a list of all groups, including the group you created in the previous step.

### Describe a Group in Identity Store

To view details about a specific group, use the [`DescribeGroup`](https://docs.aws.amazon.com/singlesignon/latest/IdentityStoreAPIReference/API_DescribeGroup.html) API.
Run the following command to describe the group you created in the previous step:

{{< command >}}
$ awslocal describe-group --identity-store-id testls --group-id 38cec731-de22-45bf-9af7-b74457bba884
<disable-copy>
{
    "GroupId": "38cec731-de22-45bf-9af7-b74457bba884",
    "ExternalIds": [],
    "IdentityStoreId": "testls"
}
</disable-copy>
{{< / command >}}

This command provides detailed information about the specific group, including its ID and any external IDs associated with it.
