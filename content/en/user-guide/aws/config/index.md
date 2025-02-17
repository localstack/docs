---
title: "Config"
linkTitle: "Config"
description: Get started with Config on LocalStack
persistence: supported

---

## Introduction

AWS Config is a service provided by Amazon Web Services (AWS) that enables you to assess, audit, and manage the configuration state of your AWS resources.
Config provides a comprehensive view of the resource configuration across your AWS environment, helping you ensure compliance with security policies, track changes, and troubleshoot operational issues.
Config continuously records configuration changes and allows you to retain a historical record of these changes.

LocalStack allows you to use the Config APIs in your local environment to assesses resource configurations and notifies you of any non-compliant items to mitigate potential security risks.
The supported APIs are available on our [API coverage page](https://docs.localstack.cloud/references/coverage/coverage_config/), which provides information on the extent of Config's integration with LocalStack.

## Getting started

This guide is designed for users new to Config and assumes basic knowledge of the AWS CLI and our [`awslocal`](https://github.com/localstack/awscli-local) wrapper script.

Start your LocalStack container using your preferred method.
We will demonstrate how to specify the resource types you want Config to record and grant it the needful permissions to access an S3 bucket and SNS topic with the AWS CLI.

### Create an S3 bucket and SNS topic

The S3 bucket will be used to receive a configuration snapshot on request and configuration history.
The SNS topic will be used to notify you when a configuration snapshot is available.
You can create a new S3 bucket and SNS topic using the AWS CLI:

{{< command >}}
$ awslocal s3 mb s3://config-test
$ awslocal sns create-topic --name config-test-topic
{{< /command >}}

### Create a new configuration recorder

You can now create a new configuration recorder to record configuration changes for specified resource types, using the [`PutConfigurationRecorder`](https://docs.aws.amazon.com/config/latest/APIReference/API_PutConfigurationRecorder.html) API.
Run the following command to create a new configuration recorder:

{{< command >}}
$ awslocal configservice put-configuration-recorder \
    --configuration-recorder name=default,roleARN=arn:aws:iam::000000000000:role/config-role
{{< /command >}}

We have specified the `roleARN` parameter to grant the configuration recorder the needful permissions to access the S3 bucket and SNS topic.
In LocalStack, IAM roles are not enforced, so you can specify any role ARN you like.
The `name` parameter has been set to `default`, and you can optionally specify a `recordingGroup` parameter to specify the resource types you want to record.

### Create a delivery channel

You can now create a delivery channel object to deliver configuration information to an S3 bucket and an SNS topic.
You have already created the S3 bucket and SNS topic, so you can now create the delivery channel object using the [`PutDeliveryChannel`](https://docs.aws.amazon.com/config/latest/APIReference/API_PutDeliveryChannel.html) API.

We're going to create a delivery channel with the following configuration.
You can inline the JSON into the `awslocal` command.

```json
{
    "name": "default",
    "s3BucketName": "config-test",
    "snsTopicARN": "arn:aws:sns:us-east-1:000000000000",
    "configSnapshotDeliveryProperties": {
        "deliveryFrequency": "Twelve_Hours"
    }
}
```

Run the following command to create the delivery channel:

{{< command >}}
$ awslocal configservice put-delivery-channel \
    --delivery-channel '{
    "name": "default",
    "s3BucketName": "config-test",
    "snsTopicARN": "arn:aws:sns:us-east-1:000000000000",
    "configSnapshotDeliveryProperties": {
        "deliveryFrequency": "Twelve_Hours"
    }
}'
{{< /command >}}

### Start the configuration recorder

You can now start recording configurations of the local AWS resources you have selected to record in your running LocalStack container.
You can use the [`StartConfigurationRecorder`](https://docs.aws.amazon.com/config/latest/APIReference/API_StartConfigurationRecorder.html) API to start the configuration recorder.
Run the following command to start the configuration recorder:

{{< command >}}
$ awslocal configservice start-configuration-recorder \
    --configuration-recorder-name default
{{< /command >}}

You can list the delivery channels and configuration recorders using the [`DescribeDeliveryChannels`](https://docs.aws.amazon.com/config/latest/APIReference/API_DescribeDeliveryChannels.html) and [`DescribeConfigurationRecorderStatus`](https://docs.aws.amazon.com/config/latest/APIReference/API_DescribeConfigurationRecorderStatus.html) APIs respectively.

{{< command >}}
$ awslocal configservice describe-delivery-channels
$ awslocal configservice describe-configuration-recorder-status
{{< /command >}}

## Current Limitations

AWS Config is currently mocked in LocalStack.
You can create, read, update, and delete AWS Config resources (like delivery channels or configuration recorders),
but LocalStack will currently not record any configuration changes to service resources.
If you need this feature, please consider opening a [feature request on GitHub](https://github.com/localstack/localstack/issues/new).
