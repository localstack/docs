---
title: "EventBridge Pipes"
linkTitle: "EventBridge Pipes"
description: Get started with EventBridge Pipes on LocalStack
tags: ["Pro image"]
---

## Introduction

EventBridge Pipes allows users to create point-to-point integrations between event producers and consumers with transform, filter and enrichment steps. Pipes are particularly useful for scenarios involving real-time data processing, application integration, and automated workflows, while simplifying the process of routing events between AWS services. Pipes offer a point-to-point connection from one source to one target (one-to-one). In contrast, EventBridge Event Bus offers a one-to-many integration where an event router delivers one event to zero or more destinations.

LocalStack allows you to use the Pipes APIs in your local environment to create Pipes with SQS queues and Kinesis streams as source and target. You can also filter events using EventBridge event patterns and enrich events using Lambda.

The supported APIs are available on our [API coverage page](https://docs.localstack.cloud/references/coverage/coverage_pipes/), which provides information on the extent of Pipe's integration with LocalStack. 

{{< alert title="Note" color="info" >}}
The implementation of EventBridge Pipes is currently in **Alpha** stage and under active development. If you would like support for more APIs or report bugs, please make an issue on [GitHub](https://github.com/localstack/localstack/issues/new/choose).
{{< /alert >}}

## Getting started

This guide is designed for users new to EventBridge Pipes and assumes basic knowledge of the AWS CLI and our [`awslocal`](https://github.com/localstack/awscli-local) wrapper script.

Start your LocalStack container using your preferred method. We will demonstrate how to create a Pipe with SQS queues as source and target, and send events to the source queue which will be routed to the target queue. 

### Create an SQS queue

Create two SQS queues that will be used as source and target for the Pipe. Run the following command to create a queue using the [`CreateQueue`](https://docs.aws.amazon.com/AWSSimpleQueueService/latest/APIReference/API_CreateQueue.html) API:

{{< command >}}
$ awslocal sqs create-queue --queue-name source-queue
$ awslocal sqs create-queue --queue-name target-queue
{{< /command >}}

You can fetch their queue ARNs using the [`GetQueueAttributes`](https://docs.aws.amazon.com/AWSSimpleQueueService/latest/APIReference/API_GetQueueAttributes.html) API:

{{< command >}}
$ SOURCE_QUEUE_ARN=$(awslocal sqs get-queue-attributes --queue-url http://sqs.us-east-1.localhost.localstack.cloud:4566/000000000000/source-queue --attribute-names QueueArn --output text)
$ TARGET_QUEUE_ARN=$(awslocal sqs get-queue-attributes --queue-url http://sqs.us-east-1.localhost.localstack.cloud:4566/000000000000/target-queue --attribute-names QueueArn --output text)
{{< /command >}}

### Create a Pipe

You can now create a Pipe, using the [`CreatePipe`](https://docs.aws.amazon.com/eventbridge/latest/APIReference/API_CreatePipe.html) API. Run the following command, by specifying the source and target queue ARNs we created earlier:

{{< command >}}
$ awslocal pipes create-pipe --name sample-pipe \
        --source $SOURCE_QUEUE_ARN \
        --target $TARGET_QUEUE_ARN \
        --role-arn arn:aws:iam::000000000000:role/pipes-role
{{< /command >}}

The following output would be retrieved:

```bash
{
    "Arn": "arn:aws:pipes:us-east-1:000000000000:pipe/sample-pipe",
    "CreationTime": "2024-01-26T11:55:27.069088+05:30",
    "CurrentState": "CREATING",
    "DesiredState": "RUNNING",
    "LastModifiedTime": "2024-01-26T11:55:27.069088+05:30",
    "Name": "sample-pipe"
}
```

### Describe the Pipe

You can use the [`DescribePipe`](https://docs.aws.amazon.com/eventbridge/latest/APIReference/API_DescribePipe.html) API to get information about the Pipe:

{{< command >}}
$ awslocal pipes describe-pipe --name sample-pipe
{{< /command >}}

The following output would be retrieved:

```bash
{
    "Arn": "arn:aws:pipes:us-east-1:000000000000:pipe/sample-pipe",
    "CreationTime": "2024-01-26T11:55:27.069088+05:30",
    "CurrentState": "RUNNING",
    "DesiredState": "RUNNING",
    "EnrichmentParameters": {},
    "LastModifiedTime": "2024-01-26T11:55:27.069088+05:30",
    "Name": "sample-pipe",
    "RoleArn": "arn:aws:iam::000000000000:role/pipe-role",
    "Source": "arn:aws:sqs:us-east-1:000000000000:source-queue",
    "SourceParameters": {
        "SqsQueueParameters": {
            "BatchSize": 10
        }
    },
    "StateReason": "USER_INITIATED",
    "Tags": {},
    "Target": "arn:aws:sqs:us-east-1:000000000000:target-queue",
    "TargetParameters": {}
}
```

### Send events to the source queue

You can now send events to the source queue, which will be routed to the target queue. Run the following command to send an event to the source queue:

{{< command >}}
$ awslocal sqs send-message \
    --queue-url http://sqs.us-east-1.localhost.localstack.cloud:4566/000000000000/source-queue \
    --message-body "message-1"
{{< /command >}}

### Receive events from the target queue

You can fetch the message from the target queue using the [`ReceiveMessage`](https://docs.aws.amazon.com/AWSSimpleQueueService/latest/APIReference/API_ReceiveMessage.html) API:

{{< command >}}
$ awslocal sqs receive-message \
    --queue-url http://sqs.us-east-1.localhost.localstack.cloud:4566/000000000000/target-queue
{{< /command >}}

## Limitations

The EventBridge Pipes implementation in LocalStack is currently in alpha and has the following limitations:

* Lack of input transformers.
* Absence of failure handling mechanisms.
* No provision for handling partial batch failures.
* Batch handling may have parity issues.
* Lack of concurrency support, resulting in slower processing of numerous events.
* Lack of lifecycle management for pipe states, such as inadequate locking and basic state transition testing.
