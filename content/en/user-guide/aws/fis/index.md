---
title: "Fault Injection Service (FIS)"
linkTitle: "Fault Injection Service (FIS)"
description: >
  Get started with Fault Injection Service (FIS) on LocalStack
tags: ["Pro image"]
---

## Introduction

Fault Injection Service (FIS) is a service provided by Amazon Web Services that enables you to test the resilience of your applications and infrastructure by injecting faults and failures into your AWS resources.
FIS simulates faults such as resource unavailability and service errors to assess the impact on your application's performance and availability.
The full list of such possible fault injections is available in the [AWS docs](https://docs.aws.amazon.com/fis/latest/userguide/fis-actions-reference.html).

LocalStack allows you to use the FIS APIs in your local environment to introduce faults in other services, in order to check how your setup behaves when parts of it stop working locally.
The supported APIs are available on our [API coverage page](https://docs.localstack.cloud/references/coverage/coverage_fis/), which provides information on the extent of FIS API's integration with LocalStack.

## Concepts

FIS defines the following elements:

1. Action: Type of fault to introduce
1. Target: Resources to be impacted
1. Duration of the disruption.

Together this is termed as an Experiment.
After the designated time, FIS restores systems to their original state and/or ceases introducing faults.

FIS actions can be categorized into two main types:

1. Single-time events — For example, the `aws:ec2:stop-instances` FIS action, which sends a [`StopInstances`](https://docs.aws.amazon.com/AWSEC2/latest/APIReference/API_StopInstances.html) API to specific EC2 instances.
Some of these events can automatically be undone after a defined time, such as sending a [`StartInstances`](https://docs.aws.amazon.com/AWSEC2/latest/APIReference/API_StartInstances.html) command to the affected instances.
1. Inducing API errors in response to a specified percentage of API calls.
For instance, using `aws:fis:inject-api-unavailable-error` to introduce an HTTP 503 error.

## Getting started

This guide is designed for users new to FIS and assumes basic knowledge of the AWS CLI and our [`awslocal`](https://github.com/localstack/awscli-local) wrapper script.

Start your LocalStack container using your preferred method.
We will demonstrate how to create an experiment that stops EC2 instances.

### Creating an experiment

Create a new file named `create-experiment.json`.
This file should contain a JSON configuration that will be utilized during the subsequent invocation of the [`CreateExperimentTemplate`](https://docs.aws.amazon.com/fis/latest/APIReference/API_CreateExperimentTemplate.html) API.

```json
{
    "actions": {
        "StopInstance": {
            "actionId": "aws:ec2:stop-instances",
            "targets": {
                "Instances": "InstancesToStop"
            },
            "description": "stop instances"
        }
    },
    "targets": {
        "InstancesToStop": {
            "resourceType": "aws:ec2:instance",
            "resourceTags": {
                "foo": "bar"
            },
            "selectionMode": "COUNT(1)"
        }
    },
    "description": "template for a test action",
    "stopConditions": [
        {
            "source": "none"
        }
    ],
    "roleArn": "arn:aws:iam:123456789012:role/ExperimentRole"
}
```

This configuration will result in EC2 [`StopInstances`](https://docs.aws.amazon.com/AWSEC2/latest/APIReference/API_StopInstances.html) operation being invoked against EC2 instances that have the resource tags `Key=foo Value=bar`.
Settings pertaining to `stopConditions` and `roleArn` hold no significance for in LocalStack FIS emulation.
Nonetheless, they are obligatory fields according to AWS specifications and must be included.

Run the following command to create an FIS experiment template using the configuration file we just created:

{{< command >}}
$ awslocal fis create-experiment-template --cli-input-json file://create-experiment.json
{{< /command >}}

The following output would be retrieved:

```json
{
    "experimentTemplate": {
        "id": "ad16589a-4a91-4aee-88df-c33446605882",
        "description": "template for a test action",
        "targets": {
            "InstancesToStop": {
                "resourceType": "aws:ec2:instance",
                "resourceTags": {
                    "foo": "bar"
                },
                "selectionMode": "COUNT(1)"
            }
        },
        "actions": {
            "StopInstance": {
                "actionId": "aws:ec2:stop-instances",
                "description": "stop instances",
                "targets": {
                    "Instances": "InstancesToStop"
                }
            }
        },
        "stopConditions": [
            {
                "source": "none"
            }
        ],
        "creationTime": 1718268196.305881,
        "lastUpdateTime": 1718268196.305881,
        "roleArn": "arn:aws:iam:123456789012:role/ExperimentRole"
    }
}
```

You can list all the templates you have created using the [`ListExperimentTemplates`](https://docs.aws.amazon.com/fis/latest/APIReference/API_ListExperimentTemplates.html):

{{< command >}}
$ awslocal fis list-experiment-templates
{{< /command >}}

### Starting the experiment

Now let us start an EC2 instance that will match the criteria we specified in the experiment template.

{{< command >}}
$ awslocal ec2 run-instances --image-id ami-024f768332f0 --count 1 --tag-specifications '{"ResourceType": "instance", "Tags": [{"Key": "foo", "Value": "bar"}]}'
{{< /command >}}

You can start the experiment using the [`StartExperiment`](https://docs.aws.amazon.com/fis/latest/APIReference/API_StartExperiment.html).
Run the following command and specify the ID of the experiment template you created earlier:

{{< command >}}
$ awslocal fis start-experiment --experiment-template-id ad16589a-4a91-4aee-88df-c33446605882
{{< /command >}}

The following output would be retrieved:

```json
{
    "experiment": {
        "id": "efee7c02-8733-4d7c-9628-1b60bbec9759",
        "experimentTemplateId": "ad16589a-4a91-4aee-88df-c33446605882",
        "roleArn": "arn:aws:iam:123456789012:role/ExperimentRole",
        "state": {
            "status": "running"
        },
        "targets": {
            "InstancesToStop": {
                "resourceType": "aws:ec2:instance",
                "resourceTags": {
                    "foo": "bar"
                },
                "selectionMode": "COUNT(1)"
            }
        },
        "actions": {
            "StopInstance": {
                "actionId": "aws:ec2:stop-instances",
                "description": "stop instances",
                "targets": {
                    "Instances": "InstancesToStop"
                }
            }
        },
        "stopConditions": [
            {
                "source": "none"
            }
        ],
        "creationTime": 1718268311.209798,
        "startTime": 1718268311.209798
    }
}
```

You can use the [`ListExperiments`](https://docs.aws.amazon.com/fis/latest/APIReference/API_ListExperiments.html) to check the status of your experiment.
Run the following command:

{{< command >}}
$ awslocal fis list-experiments
{{< /command >}}

You can fetch the details of your experiment using the [`GetExperiment`](https://docs.aws.amazon.com/fis/latest/APIReference/API_GetExperiment.html) API.
Run the following command and specify the ID of the experiment you created earlier:

{{< command >}}
$ awslocal fis get-experiment --id efee7c02-8733-4d7c-9628-1b60bbec9759
{{< /command >}}

### Verifying the outcome

You can now test that the experiment is working as expected by trying to obtain the state of the EC2 instance using [`DescribeInstanceStatus`](https://docs.aws.amazon.com/AWSEC2/latest/APIReference/API_DescribeInstanceStatus.html).
Run the following command:

{{< command >}}
$ awslocal ec2 describe-instance-status --instance-ids i-3c40b52ab72f99c63 --output json --query InstanceStatuses[0].InstanceState
{{< /command >}}

If everything happened as expected, the following output would be retrieved:

```json
{
    "Code": 80,
    "Name": "stopped"
}
```

## Supported Actions

LocalStack FIS currently supports the following actions:

- **`aws:ec2:stop-instances`**: Runs EC2 StopInstances on the target EC2 instances.
- **`aws:ec2:terminate-instances`**: Runs EC2 TerminateInstances on the target EC2 instances.
- **`aws:rds:reboot-db-instances`**: Runs EC2 RebootInstances on the target EC2 instances.
- **`aws:ssm:send-command`**: Runs the Systems Manager SendCommand on the target EC2 instances.

{{< callout "note" >}}
If you would like support for more FIS actions, please make a feature request on [GitHub](https://github.com/localstack/localstack/issues/new/choose).
{{< /callout >}}

The following actions are deprecated and marked for removal:

- **`localstack:generic:api-error`**: Raise a custom HTTP error.
    This action accepts the following parameters.
  - `region`: The region name where faults will be introduced, e.g. `us-west-1`.
    Default: region of the experiment
  - `service`: The service name to limit faults to, e.g. `kms`.
    Default: all services
  - `operation`: The operation name for the specified service to limit faults to, e.g. `ListKeys`
  - `percentage`: The percentage of API calls to fail among matching calls.
    Default: 100
  - `exception`: The name of the exception to raise for affected API calls.
    Default: `InternalError`
  - `errorCode`: The HTTP error code to return for impacted API calls.
    Default: 500
- **`localstack:kms:inject-api-internal-error`**: Special case of the previous action which injects an InternalError for KMS operations.
- **`localstack:log-debug`**: Prints a debug message in the LocalStack logs when experiment is started and stopped.
- **`localstack:generic:latency`**: Introduces a latency in the network call.

## Current Limitations

- LocalStack does not implement the [selection mode](https://docs.aws.amazon.com/fis/latest/userguide/targets.html#target-selection-mode) mechanism available on AWS.
- LocalStack ignores [`RoleARN`](https://docs.aws.amazon.com/fis/latest/APIReference/API_ExperimentTemplate.html#fis-Type-ExperimentTemplate-roleArn).
On AWS, FIS executes actions based on permissions granted by the specified `RoleARN`.
