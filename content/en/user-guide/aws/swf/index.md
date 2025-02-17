---
title: "Simple Workflow Service (SWF)"
linkTitle: "Simple Workflow Service (SWF)"
description: >
  Get started with Simple Workflow Service (SWF) on LocalStack
---

## Introduction

Simple Workflow Service (SWF) is a fully managed service offered by Amazon Web Services (AWS) that enables you to build and manage applications with distributed components and complex workflows.
SWF allows you to define workflows in a way that's separate from the actual application code, making it easier to modify and adapt workflows without changing the application logic.
SWF also provides a programming framework to design, coordinate, and execute workflows that involve multiple tasks, steps, and decision points.

LocalStack allows you to use the SWF APIs in your local environment to monitor and manage workflow design, task coordination, activity implementation, and error handling.
The supported APIs are available on our [API coverage page](https://docs.localstack.cloud/references/coverage/coverage_swf/), which provides information on the extent of SWF's integration with LocalStack.

## Getting started

This guide is designed for users new to Simple Workflow Service and assumes basic knowledge of the AWS CLI and our [`awslocal`](https://github.com/localstack/awscli-local) wrapper script.

Start your LocalStack container using your preferred method.
We will demonstrate how to register an SWF domain and workflow using the AWS CLI.

### Registering a domain

You can register an SWF domain using the [`RegisterDomain`](https://docs.aws.amazon.com/amazonswf/latest/apireference/API_RegisterDomain.html) API.
Execute the following command to register a domain named `test-domain`:

{{< command >}}
$ awslocal swf register-domain \
    --name test-domain \
    --workflow-execution-retention-period-in-days 1
{{< /command >}}

You can use the [`DescribeDomain`](https://docs.aws.amazon.com/amazonswf/latest/apireference/API_DescribeDomain.html) API to verify that the domain was registered successfully.
Run the following command to describe the `test-domain` domain:

{{< command >}}
$ awslocal swf describe-domain \
    --name test-domain
{{< /command >}}

The following output would be retrieved:

```bash
{
    "domainInfo": {
        "name": "test-domain",
        "status": "REGISTERED",
        "arn": "arn:aws:swf:us-east-1:000000000000:/domain/test-domain"
    },
    "configuration": {
        "workflowExecutionRetentionPeriodInDays": "1"
    }
}
```

### List the domains

You can list all registered domains using the [`ListDomains`](https://docs.aws.amazon.com/amazonswf/latest/apireference/API_ListDomains.html) API.
Run the following command to list all registered domains:

{{< command >}}
$ awslocal swf list-domains --registration-status REGISTERED
{{< /command >}}

To deprecate a domain, use the [`DeprecateDomain`](https://docs.aws.amazon.com/amazonswf/latest/apireference/API_DeprecateDomain.html) API.
Run the following command to deprecate the `test-domain` domain:

{{< command >}}
$ awslocal swf deprecate-domain \
    --name test-domain
{{< /command >}}

You can now list the deprecated domains using the `--registration-status DEPRECATED` flag:

{{< command >}}
$ awslocal swf list-domains --registration-status DEPRECATED
{{< /command >}}

### Registering a workflow

You can register a workflow using the [`RegisterWorkflowType`](https://docs.aws.amazon.com/amazonswf/latest/apireference/API_RegisterWorkflowType.html) API.
Execute the following command to register a workflow named `test-workflow`:

{{< command >}}
$ awslocal swf register-workflow-type \
    --domain test-domain \
    --name test-workflow \
    --default-task-list name=test-task-list \
    --default-task-start-to-close-timeout 30 \
    --default-execution-start-to-close-timeout 60 \
    --default-child-policy TERMINATE \
    --workflow-version "1.0"
{{< /command >}}

You can use the [`DescribeWorkflowType`](https://docs.aws.amazon.com/amazonswf/latest/apireference/API_DescribeWorkflowType.html) API to verify that the workflow was registered successfully.
Run the following command to describe the `test-workflow` workflow:

{{< command >}}
$ awslocal swf describe-workflow-type \
    --domain test-domain \
    --workflow-type name=test-workflow,version=1.0
{{< /command >}}

The following output would be retrieved:

```bash
{
    "typeInfo": {
        "workflowType": {
            "name": "test-workflow",
            "version": "1.0"
        },
        "status": "REGISTERED",
        "creationDate": 1420066800.0
    },
    "configuration": {
        "defaultTaskStartToCloseTimeout": "30",
        "defaultExecutionStartToCloseTimeout": "60",
        "defaultTaskList": {
            "name": "test-task-list"
        },
        "defaultChildPolicy": "TERMINATE"
    }
}
```

### Registering an activity

You can register an activity using the [`RegisterActivityType`](https://docs.aws.amazon.com/amazonswf/latest/apireference/API_RegisterActivityType.html) API.
Execute the following command to register an activity named `test-activity`:

{{< command >}}
$ awslocal swf register-activity-type \
    --domain test-domain \
    --name test-activity \
    --default-task-list name=test-task-list \
    --default-task-start-to-close-timeout 30 \
    --default-task-heartbeat-timeout 30 \
    --default-task-schedule-to-start-timeout 30 \
    --default-task-schedule-to-close-timeout 30 \
    --activity-version "1.0"
{{< /command >}}

You can use the [`DescribeActivityType`](https://docs.aws.amazon.com/amazonswf/latest/apireference/API_DescribeActivityType.html) API to verify that the activity was registered successfully.
Run the following command to describe the `test-activity` activity:

{{< command >}}
$ awslocal swf describe-activity-type \
    --domain test-domain \
    --activity-type name=test-activity,version=1.0
{{< /command >}}

The following output would be retrieved:

```bash
{
    "typeInfo": {
        "activityType": {
            "name": "test-activity",
            "version": "1.0"
        },
        "status": "REGISTERED",
        "creationDate": 1420066800.0
    },
    "configuration": {
        "defaultTaskStartToCloseTimeout": "30",
        "defaultTaskHeartbeatTimeout": "30",
        "defaultTaskList": {
            "name": "test-task-list"
        },
        "defaultTaskScheduleToStartTimeout": "30",
        "defaultTaskScheduleToCloseTimeout": "30"
    }
}
```

### Starting a workflow execution

You can start a workflow execution using the [`StartWorkflowExecution`](https://docs.aws.amazon.com/amazonswf/latest/apireference/API_StartWorkflowExecution.html) API.
Execute the following command to start a workflow execution for the `test-workflow` workflow:

{{< command >}}
$ awslocal swf start-workflow-execution \
    --domain test-domain \
    --workflow-type name=test-workflow,version=1.0 \
    --workflow-id test-workflow-id \
    --task-list name=test-task-list \
    --input '{"foo": "bar"}'
{{< /command >}}

The following output would be retrieved:

```bash
{
    "runId": "0602601afc71403abb934d8094c51668"
}
```
