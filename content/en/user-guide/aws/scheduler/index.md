---
title: "EventBridge Scheduler"
linkTitle: "EventBridge Scheduler"
description: Get started with EventBridge Scheduler on LocalStack
tags: ["Free"]
---

## Introduction

EventBridge Scheduler is a service that enables you to schedule the execution of your AWS Lambda functions, Amazon ECS tasks, and Amazon Batch jobs.
You can use EventBridge Scheduler to create schedules that run at a specific time or at regular intervals.
You can also use EventBridge Scheduler to create schedules that run within a flexible time window.

LocalStack allows you to use the Scheduler APIs in your local environment to create and run schedules.
The supported APIs are available on our [API coverage page]({{< ref "coverage_scheduler" >}}), which provides information on the extent of EventBridge Scheduler's integration with LocalStack.

## Getting started

This guide is designed for users new to EventBridge Scheduler and assumes basic knowledge of the AWS CLI and our [`awslocal`](https://github.com/localstack/awscli-local) wrapper script.

Start your LocalStack container using your preferred method.
We will demonstrate how you can create a new schedule, list all schedules, and tag a schedule using the EventBridge Scheduler APIs.

### Create a new SQS queue

You can create a new SQS queue using the [`CreateQueue`](https://docs.aws.amazon.com/AWSSimpleQueueService/latest/APIReference/API_CreateQueue.html) API.
Run the following command to create a new SQS queue:

{{< command >}}
$ awslocal sqs create-queue --queue-name local-notifications
{{< /command >}}

You can fetch the Queue ARN using the [`GetQueueAttributes`](https://docs.aws.amazon.com/AWSSimpleQueueService/latest/APIReference/API_GetQueueAttributes.html) API.
Run the following command to fetch the Queue ARN by specifying the Queue URL:

{{< command >}}
$ awslocal sqs get-queue-attributes \
    --queue-url http://sqs.us-east-1.localhost.localstack.cloud:4566/000000000000/local-notifications \
    --attribute-names All
{{< /command >}}

Save the Queue ARN for later use.

### Create a new schedule

You can create a new schedule using the [`CreateSchedule`](https://docs.aws.amazon.com/eventbridge/latest/APIReference/API_CreateSchedule.html) API.
Run the following command to create a new schedule:

{{< command >}}
$ awslocal scheduler create-schedule \
    --name sqs-templated-schedule \
    --schedule-expression 'rate(5 minutes)' \
    --target '{"RoleArn": "arn:aws:iam::000000000000:role/schedule-role", "Arn":"arn:aws:sqs:us-east-1:000000000000:local-notifications", "Input": "test" }' \
    --flexible-time-window '{ "Mode": "OFF"}'
{{< /command >}}

The following output is displayed:

```bash
{
    "ScheduleArn": "arn:aws:scheduler:us-east-1:000000000000:schedule/default/sqs-templated-schedule"
}
```

### List all schedules

You can list all schedules using the [`ListSchedules`](https://docs.aws.amazon.com/eventbridge/latest/APIReference/API_ListSchedules.html) API.
Run the following command to list all schedules:

{{< command >}}
$ awslocal scheduler list-schedules
{{< /command >}}

The following output is displayed:

```bash
{
    "Schedules": [
        {
            "Arn": "arn:aws:scheduler:us-east-1:000000000000:schedule/default/sqs-templated-schedule",
            "CreationDate": "2024-07-11T23:13:15.296906+05:30",
            "GroupName": "default",
            "LastModificationDate": "2024-07-11T23:13:15.296906+05:30",
            "Name": "sqs-templated-schedule",
            "State": "ENABLED",
            "Target": {
                "Arn": "arn:aws:sqs:us-east-1:000000000000:local-notifications"
            }
        }
    ]
}
```

### Tag a schedule

You can tag a schedule using the [`TagResource`](https://docs.aws.amazon.com/eventbridge/latest/APIReference/API_TagResource.html) API.
Run the following command to tag a schedule:

{{< command >}}
$ awslocal scheduler tag-resource \
    --resource-arn arn:aws:scheduler:us-east-1:000000000000:schedule/default/sqs-templated-schedule \
    --tags Key=Name,Value=Test
{{< /command >}}

You can view the tags associated with a schedule using the [`ListTagsForResource`](https://docs.aws.amazon.com/eventbridge/latest/APIReference/API_ListTagsForResource.html) API.
Run the following command to list the tags associated with a schedule:

{{< command >}}
$ awslocal scheduler list-tags-for-resource \
    --resource-arn arn:aws:scheduler:us-east-1:000000000000:schedule/default/sqs-templated-schedule
{{< /command >}}

The following output is displayed:

```bash
{
    "Tags": [
        {
            "Key": "Name",
            "Value": "Test"
        }
    ]
}
```

## Current Limitations

EventBridge Scheduler in LocalStack only provides mocked functionality.
It does not emulate actual features such as schedule execution or target triggering for Lambda functions or SQS queues.
