---
title: "Fault Injection Simulator (FIS)"
linkTitle: "Fault Injection Simulator (FIS)"
description: >
  Get started with Fault Injection Simulator (FIS) on LocalStack
tags: ["Pro image"]
---

## Introduction

Fault Injection Simulator (FIS) is a service provided by Amazon Web Services (AWS) that enables you to test the resilience of your applications and infrastructure by injecting faults and failures into your AWS resources.
FIS inject faults such as network latency, resource unavailability, and service errors to assess the impact on your application's performance and availability.
The full list of such possible fault injections - called **actions** - is available in the [AWS docs](https://docs.aws.amazon.com/fis/latest/userguide/fis-actions-reference.html).

LocalStack allows you to use the FIS APIs in your local environment to introduce faults in other services, in order to check how your setup behaves when parts of it stop working locally.
The supported APIs are available on our [API coverage page](https://docs.localstack.cloud/references/coverage/coverage_fis/), which provides information on the extent of FIS API's integration with LocalStack.

## FIS Concepts

In general, FIS calls contain the following details:

1. Type of fault to introduce - referred to as **action**.
1. Resources to be impacted - known as **target**.
1. Duration of the disruption.
After the designated time, FIS is expected to restore systems to their original state or cease introducing faults.

FIS actions can be categorized into two main types:

1. Single-time events — For example, the `aws:ec2:stop-instances` FIS action, which sends a [`StopInstances`](https://docs.aws.amazon.com/AWSEC2/latest/APIReference/API_StopInstances.html) API to specific EC2 instances.
Some of these events can automatically be undone after a defined time, such as sending a [`StartInstances`](https://docs.aws.amazon.com/AWSEC2/latest/APIReference/API_StartInstances.html) command to the affected instances.
1. Inducing API errors in response to a specified percentage of API calls.
For instance, using `aws:fis:inject-api-unavailable-error` to introduce an HTTP 503 error.
Notably, AWS currently supports this exclusively for EC2 API calls.

## Getting started

This guide is designed for users new to FIS and assumes basic knowledge of the AWS CLI and our [`awslocal`](https://github.com/localstack/awscli-local) wrapper script.

Start your LocalStack container using your preferred method.
We will demonstrate how to create an FIS Experiment that fails KMS [`ListKeys`](https://docs.aws.amazon.com/kms/latest/APIReference/API_ListKeys.html) API with a HTTP 400 code using the AWS CLI.

### Create an FIS Experiment

<!--
TODO

Remove the use of localstack: action, instead use an AWS one
-->

Create a new file named `create-experiment.json`.
This file should contain a JSON configuration that will be utilized during the subsequent invocation of the [`CreateExperimentTemplate`](https://docs.aws.amazon.com/fis/latest/APIReference/API_CreateExperimentTemplate.html) API.

```json
{
	"actions": {
		"Some test action": {
			"actionId": "localstack:generic:api-error",
			"parameters": {
				"service": "kms",
				"operation": "ListKeys",
				"percentage": "100",
				"exception": "SomeTerribleException",
				"errorCode": "400"
			}
		}
	},
	"description": "template for a test action",
	"stopConditions": [{
		"source": "none"
	}],
	"roleArn": "arn:aws:iam:123456789012:role/ExperimentRole"
}
```

This configuration will result in a 100% failure rate for KMS [`ListKeys`](https://docs.aws.amazon.com/kms/latest/APIReference/API_ListKeys.html) API calls, each accompanied by a HTTP 400 status code.
Note that the settings pertaining to `stopConditions` and `roleArn` hold no significance for LocalStack's FIS emulation.
Nonetheless, they are obligatory fields according to AWS specifications and must be included.

Run the following command to create an FIS Experiment Template using the configuration file we just created:

{{< command >}}
$ awslocal fis create-experiment-template --cli-input-json file://create-experiment.json
{{< /command >}}


The following output would be retrieved:

```json
{
    "experimentTemplate": {
        "id": "7b9ec603-1d20-4a8f-8eda-b1c3e7b28540",
        "description": "template for a test action",
        "actions": {
            "Some test action": {
                "actionId": "localstack:generic:api-error",
                "parameters": {
                    "service": "kms",
                    "operation": "ListKeys",
                    "percentage": "100",
                    "exception": "SomeTerribleException",
                    "errorCode": "400"
                }
            }
        },
        "stopConditions": [
            {
                "source": "none"
            }
        ],
        "creationTime": 1661772176.772892,
        "lastUpdateTime": 1661772176.772892,
        "roleArn": "arn:aws:iam:123456789012:role/ExperimentRole"
    }
}
```

You can list all the templates you have created using the [`ListExperimentTemplates`](https://docs.aws.amazon.com/fis/latest/APIReference/API_ListExperimentTemplates.html) API:

{{< command >}}
$ awslocal fis list-experiment-templates
{{< /command >}}

### Start the FIS Experiment

Now let us check that KMS ListKeys actually works before we introduce our API disruprions:

You can verify that KMS is working by running by using the [`ListKeys`](https://docs.aws.amazon.com/kms/latest/APIReference/API_ListKeys.html) API.
Run the following command:

{{< command >}}
$ awslocal kms list-keys
{{< /command >}}

Your output may vary, but if you have recently initialized LocalStack from a fresh state, the expected result should be an empty list.
The following output would be retrieved:

```bash
{
    "Keys": []
}
```

You can start the FIS Experiment using the [`StartExperiment`](https://docs.aws.amazon.com/fis/latest/APIReference/API_StartExperiment.html) API.
Run the following command and specify the ID of the experiment template you created earlier:

```sh 
$ awslocal fis start-experiment \
    --experiment-template-id 7b9ec603-1d20-4a8f-8eda-b1c3e7b28540
```

The following output would be retrieved:

```json
{
    "experiment": {
        "id": "8b98db02-1c46-49fd-8075-8ff3368fb0a3",
        "experimentTemplateId": "7b9ec603-1d20-4a8f-8eda-b1c3e7b28540",
        "roleArn": "arn:aws:iam:123456789012:role/ExperimentRole",
        "state": {
            "status": "running"
        },
        "actions": {
            "Some test action": {
                "actionId": "localstack:generic:api-error",
                "parameters": {
                    "service": "kms",
                    "operation": "ListKeys",
                    "percentage": "100",
                    "exception": "SomeTerribleException",
                    "errorCode": "400"
                }
            }
        },
        "stopConditions": [
            {
                "source": "none"
            }
        ],
        "creationTime": 1661772189.015712,
        "startTime": 1661772189.015712
    }
}
```

You can use the [`ListExperiments`](https://docs.aws.amazon.com/fis/latest/APIReference/API_ListExperiments.html) API to check the status of your experiment.
Run the following command:

{{< command >}}
$ awslocal fis list-experiments
{{< /command >}}

You can fetch the details of your experiment using the [`GetExperiment`](https://docs.aws.amazon.com/fis/latest/APIReference/API_GetExperiment.html) API.
Run the following command and specify the ID of the experiment you created earlier:

{{< command >}}
$ awslocal fis get-experiment \
    --id 8b98db02-1c46-49fd-8075-8ff3368fb0a3
{{< /command >}}

### Test the FIS Experiment

You can now test that the FIS Experiment is working as expected by trying to list the KMS keys using the [`ListKeys`](https://docs.aws.amazon.com/kms/latest/APIReference/API_ListKeys.html) API.
Run the following command:

{{< command >}}
$ awslocal kms list-keys
{{< /command >}}

If everything happened as expected (or did not happen, in this case), the following output would be retrieved:

```bash
An error occurred (SomeTerribleException) when calling the ListKeys operation: Failing as per Fault Injection Simulator configuration
```

You can double-check to be sure whether other API calls to KMS or different services are impacted.
For instance, you can try using:

{{< command >}}
$ awslocal kms list-aliases
$ awslocal sqs list-queues
{{< /command >}}

To halt the experiment and return everything to its usual state, you can use the [`StopExperiment`](https://docs.aws.amazon.com/fis/latest/APIReference/API_StopExperiment.html) API.
Run the following command and specify the ID of the experiment you created earlier:

{{< command >}}
$ awslocal fis stop-experiment \
    --id 8b98db02-1c46-49fd-8075-8ff3368fb0a3
{{< /command >}}

The [`ListKeys`](https://docs.aws.amazon.com/kms/latest/APIReference/API_ListKeys.html) API should now return an empty list again.

## LocalStack features

LocalStack provides the `localstack:generic:api-error` action, which functions similarly to actions like `aws:fis:inject-api-unavailable-error` found in AWS.
This action enables users to introduce errors into API calls.


Contrasting with AWS, where such functionality is currently limited to EC2 API calls and a handful of error types, the `localstack:generic:api-error` in LocalStack FIS empowers users to configure a wide range of faults for any API call.
Within its `parameters` section, you can configure the following:

| Parameter    | Description                                                                                       | Default Value           |
|--------------|---------------------------------------------------------------------------------------------------|-------------------------|
| `region`     | The region name where faults will be introduced, e.g., "us-west-1". | Experiment's region     |
| `service`    | The service name to limit faults to, e.g., "kms". | All services            |
| `operation`  | The operation name for the specified service to limit faults to, e.g., "ListKeys". | All operations          |
| `percentage` | The percentage of API calls to fail among matching calls. | "100"                   |
| `exception`  | The name of the exception to raise for affected API calls. | "InternalError"         |
| `errorCode`  | The HTTP error code to return for impacted API calls. | "500"                   |

This table summarizes the configurable parameters for the `localstack:generic:api-error` action in LocalStack FIS.

## Current Limitations

1. LocalStack currently supports only a subset of FIS actions available in AWS.
Unsupported actions will result in an error.
The range of supported actions is continuously expanding, with the capability to add new actions upon request.
1. LocalStack does not provide support for the target selection mechanism utilized by AWS.
For more information, refer to the [selection mode documentation](https://docs.aws.amazon.com/fis/latest/userguide/targets.html#target-selection-mode).
1. At present, LocalStack does not consider [`RoleARN`s](https://docs.aws.amazon.com/fis/latest/APIReference/API_ExperimentTemplate.html#fis-Type-ExperimentTemplate-roleArn).
In AWS, FIS executes actions based on permissions granted by the specified `RoleARN`s.
