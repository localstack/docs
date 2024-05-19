---
title: "Pinpoint"
linkTitle: "Pinpoint"
description: Get started with Pinpoint on LocalStack
tags: ["Pro image"]
persistence: supported

---

## Introduction

Pinpoint is a customer engagement service to facilitate communication across multiple channels, including email, SMS, and push notifications. Pinpoint allows developers to create and manage customer segments based on various attributes, such as user behavior and demographics, while integrating with other AWS services to send targeted messages to customers.

LocalStack allows you to mock the Pinpoint APIs in your local environment. The supported APIs are available on our [API coverage page](https://docs.localstack.cloud/references/coverage/coverage_pinpoint/), which provides information on the extent of Pinpoint's integration with LocalStack.

## Getting started

This guide is designed for users new to Pinpoint and assumes basic knowledge of the AWS CLI and our [`awslocal`](https://github.com/localstack/awscli-local) wrapper script.

Start your LocalStack container using your preferred method. We will demonstrate how to create a Pinpoint application, retrieve all applications, and list tags for the resource.

### Create an application

Create a Pinpoint application using the [`CreateApp`](https://docs.aws.amazon.com/pinpoint/latest/apireference/apps-application-id.html) API. Execute the following command:

{{< command >}}
$ awslocal pinpoint create-app \
    --create-application-request Name=ExampleCorp,tags={"Stack"="Test"}
{{< /command >}}

The following output would be retrieved:

```bash
{
    "ApplicationResponse": {
        "Arn": "arn:aws:mobiletargeting:us-east-1:000000000000:apps/4487a55ac6fb4a2699a1b90727c978e7",
        "Id": "4487a55ac6fb4a2699a1b90727c978e7",
        "Name": "ExampleCorp",
        "CreationDate": 1706609789.906863
    }
}
```

### List applications

You can list all applications using the [`GetApps`](https://docs.aws.amazon.com/pinpoint/latest/apireference/apps.html) API. Execute the following command:

{{< command >}}
$ awslocal pinpoint get-apps
{{< /command >}}

The following output would be retrieved:

```bash
{
    "ApplicationsResponse": {
        "Item": [
            {
                "Arn": "arn:aws:mobiletargeting:us-east-1:000000000000:apps/4487a55ac6fb4a2699a1b90727c978e7",
                "Id": "4487a55ac6fb4a2699a1b90727c978e7",
                "Name": "ExampleCorp",
                "CreationDate": 1706609789.906863
            }
        ]
    }
}
```

### List tags for the application

You can list all tags for the application using the [`GetApp`](https://docs.aws.amazon.com/pinpoint/latest/apireference/apps-application-id.html) API. Execute the following command:

{{< command >}}
$ awslocal pinpoint list-tags-for-resource \
    --resource-arn arn:aws:mobiletargeting:us-east-1:000000000000:apps/4487a55ac6fb4a2699a1b90727c978e7
{{< /command >}}

Replace the `resource-arn` with the ARN of the application you created earlier. The following output would be retrieved:

```bash
{
    "TagsModel": {
        "tags": {
            "Stack": "Test"
        }
    }
}
```
