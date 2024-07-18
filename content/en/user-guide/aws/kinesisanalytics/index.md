---
title: "Kinesis Data Analytics"
linkTitle: "Kinesis Data Analytics"
description: >
  Get started with Kinesis Data Analytics on LocalStack
tags: ["Pro image"]
---

## Introduction

Kinesis Data Analytics is a service offered by Amazon Web Services (AWS) that enables you to process and analyze streaming data in real-time.
Kinesis Data Analytics allows you to apply transformations, filtering, and enrichment to streaming data using standard SQL syntax.
You can also run Java or Scala programs against streaming sources to perform various operations on the data using Apache Flink.

LocalStack allows you to use the Kinesis Data Analytics APIs in your local environment.
The API coverage is available on:

* [Kinesis Data Analytics V1](https://docs.localstack.cloud/references/coverage/coverage_kinesisanalytics/)
* [Kinesis Data Analytics V2](https://docs.localstack.cloud/references/coverage/coverage_kinesisanalyticsv2/)

This provides information on the extent of Kinesis Data Analytics integration with LocalStack.

## Getting started

This guide is designed for users new to Kinesis Data Analytics and assumes basic knowledge of the AWS CLI and our [`awslocal`](https://github.com/localstack/awscli-local) wrapper script.

Start your LocalStack container using your preferred method.
We will demonstrate how to create a Kinesis Analytics application using AWS CLI.

### Create an application

You can create a Kinesis Analytics application using the [`CreateApplication`](https://docs.aws.amazon.com/kinesisanalytics/latest/APIReference/API_CreateApplication.html) API by running the following command:

{{< command >}}
$ awslocal kinesisanalytics create-application \
    --application-name test-analytics-app
{{< /command >}}

The following output would be retrieved:

```bash
{
    "ApplicationSummary": {
        "ApplicationName": "test-analytics-app",
        "ApplicationARN": "arn:aws:kinesisanalytics:us-east-1:000000000000:application/test-analytics-app",
        "ApplicationStatus": "READY"
    }
}
```

### Describe the application

You can describe the application using the [`DescribeApplication`](https://docs.aws.amazon.com/kinesisanalytics/latest/APIReference/API_DescribeApplication.html) API by running the following command:

{{< command >}}
$ awslocal kinesisanalytics describe-application \
    --application-name test-analytics-app
{{< /command >}}

The following output would be retrieved:

```bash
{
    "ApplicationDetail": {
        "ApplicationName": "test-analytics-app",
        "ApplicationARN": "arn:aws:kinesisanalytics:us-east-1:000000000000:application/test-analytics-app",
        "ApplicationStatus": "READY",
        "CreateTimestamp": 1718194721.567,
        "InputDescriptions": [],
        "OutputDescriptions": [],
        "ReferenceDataSourceDescriptions": [],
        "CloudWatchLoggingOptionDescriptions": [],
        "ApplicationVersionId": 1
    }
}
```

### Tag the application

Add tags to the application using the [`TagResource`](https://docs.aws.amazon.com/kinesisanalytics/latest/APIReference/API_TagResource.html) API by running the following command:

{{< command >}}
$ awslocal kinesisanalytics tag-resource \
    --resource-arn arn:aws:kinesisanalytics:us-east-1:000000000000:application/test-analytics-app \
    --tags Key=test,Value=test
{{< /command >}}

You can list the tags for the application using the [`ListTagsForResource`](https://docs.aws.amazon.com/kinesisanalytics/latest/APIReference/API_ListTagsForResource.html) API by running the following command:

{{< command >}}
$ awslocal kinesisanalytics list-tags-for-resource \
    --resource-arn arn:aws:kinesisanalytics:us-east-1:000000000000:application/test-analytics-app
{{< /command >}}

The following output would be retrieved:

```bash
{
    "Tags": [
        {
            "Key": "test",
            "Value": "test"
        }
    ]
}
```

## Current Limitations

* LocalStack supports basic emulation for the version 1 of the Kinesis Data Analytics API.
  However, the queries are not fully supported and lack parity with AWS.
* LocalStack supports CRUD mocking for the version 2 of the Kinesis Data Analytics API.
