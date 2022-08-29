---
title: "FIS"
linkTitle: "FIS"
categories: ["LocalStack Pro"]
description: >
  Fault Injection Simulator (FIS)
---

Basic support for the Fault Injection Simulator (FIS) service is included in LocalStack Pro. The local FIS API allows you to introduce faults to other services - in order to check how your setup behaves when parts of it stop working.
The full list of such possible fault injections - called "actions" - is available in the [AWS docs](https://docs.aws.amazon.com/fis/latest/userguide/fis-actions-reference.html).

In general, calls to FIS contain the following information:

1. What kind of fault to introduce - "action".
2. What kind of resources to affect - "target".
3. (sometimes) Duration of the interruption. After the specified amount of time FIS is supposed to revert systems to their original state or to stop introducing faults.

FIS actions come in roughly two types:

1. A single-time event, e.g., `aws:ec2:stop-instances` FIS action is a `stop-instances` command sent to target EC2 instances. Results of some of these single-time events can be automatically reverted after a specified period of time, e.g., by sending `start-instances` command to the affected instances.
2. Generation of API errors in response to a specified percentage of API calls, e.g., `aws:fis:inject-api-unavailable-error` to inject an HTTP 503 error. Currently AWS only supports this for EC2 API calls.

# Most notable current FIS limitations in LocalStack
1. Only a subset of FIS actions available in AWS are currently supported in LocalStack (unsupported actions generate an error). The set of supported actions is extended on an ongoing basis, and new actions can easily be added on demand.
2. LocalStack doesn't support target selection mechanism used by AWS. See [selection mode documentation for more info](https://docs.aws.amazon.com/fis/latest/userguide/targets.html#target-selection-mode)
3. LocalStack currently ignores [`roleArn`s](https://docs.aws.amazon.com/fis/latest/APIReference/API_ExperimentTemplate.html#fis-Type-ExperimentTemplate-roleArn). In AWS FIS performs actions under permissions granted to given `roleArn`s.

# What FIS in LocalStack offers in addition to what FIS in AWS does

Localstack offers `localstack:generic:api-error` action. The action is similar to actions like `aws:fis:inject-api-unavailable-error` that are supported in AWS - it allows a user to introduce errors to API calls. The difference with AWS is that AWS FIS currently supports this only for EC2 API calls and then is only able to generate a few errors there, while `localstack:generic:api-error` in LocalStack FIS allows a user to configure any desired faults for any API calls. In its `parameters` section it is possible to set the following:
- "region" - a name of a region to introduce faults to, e.g. "us-west-1". Default: the region you are starting your experiment in.
- "service" - a name of a service to limit the faults to, e.g. "kms". Default: all services.
- "apiCall" - a name of an API call for the specified service to limit the faults to, e.g. "ListKeys". Default: all API calls.
- "percentage" - a percentage of all calls to matching API calls to fail. Default: "100".
- "exception" - a name of an exception to raise for API calls affected by FIS. Default: "InternalError".
- "errorCode" - an HTTP error code to return for an API call affected by FIS. Default: "500".

# Tutorial
First, let's create a file (named `create-experiment.json` in this case) with the following JSON configuration for a later call to FIS CreateExperimentTemplate.
```
{
	"actions": {
		"Some test action": {
			"actionId": "localstack:generic:api-error",
			"parameters": {
				"service": "kms",
				"apiCall": "ListKeys",
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
This config is going to make 100% of KMS ListKeys API calls fail with a 400 HTTP code. Settings for `stopConditions` and `roleArn` here do not matter, as LocalStack doesn't currently act on them in any way. But they have to be present, as these are required fields by the AWS specifications.

The next step is to create a FIS experiment template using our file. Keep in mind that `file://` here is required, without it you are going to get an error.
```
awslocal fis create-experiment-template --cli-input-json file://create-experiment.json
```
The output is going to be something like
```
{
    "experimentTemplate": {
        "id": "7b9ec603-1d20-4a8f-8eda-b1c3e7b28540",
        "description": "template for a test action",
        "actions": {
            "Some test action": {
                "actionId": "localstack:generic:api-error",
                "parameters": {
                    "service": "kms",
                    "apiCall": "ListKeys",
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
You are going to need the ID (`7b9ec603-1d20-4a8f-8eda-b1c3e7b28540` in this case) to start an actual experiment. And if you lose the ID, you can always list all available experiment templates with
```
awslocal fis list-experiment-templates
```
You also can check all the details for the template later using
```
awslocal fis get-experiment-template --id 7b9ec603-1d20-4a8f-8eda-b1c3e7b28540
```
Now let's check that KMS ListKeys actually works before we introduce our API disruprions:
```
awslocal kms list-keys
```
Your output might differ, but for a fresh start of LocalStack the output should just be an empty list:
```
{
    "Keys": []
}
```
Time to start our experiment:
```
awslocal fis start-experiment --experiment-template-id 7b9ec603-1d20-4a8f-8eda-b1c3e7b28540
```
Keep in mind the ID of the experiment in the output (`8b98db02-1c46-49fd-8075-8ff3368fb0a3` in this example), as you would need it to stop the experiment:
```
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
                    "apiCall": "ListKeys",
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
As with the templates, you can always use 
```
awslocal fis list-experiments
```
to list all experiments and then
```
awslocal fis get-experiment --id 8b98db02-1c46-49fd-8075-8ff3368fb0a3
```
to get the details about the experiment again.

Time to check if this has affected our KMS:
```
awslocal kms list-keys
```
If everything worked (or rather failed) as expected, you should see the following:
```
An error occurred (SomeTerribleException) when calling the ListKeys operation: Failing as per Fault Injection Simulator configuration
```
Let's check just in case if other API calls to KMS or other services are affected. For example, can use
```
awslocal kms list-aliases
awslocal sqs list-queues
```
Both should succeed.

To stop the experiment and to let everything get back to normal we can run
```
awslocal fis stop-experiment --id 8b98db02-1c46-49fd-8075-8ff3368fb0a3
```
After that `awslocal kms list-keys` is supposed to succeed again.
