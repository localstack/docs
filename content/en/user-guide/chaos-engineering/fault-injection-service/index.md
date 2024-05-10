---
title: "Fault Injection Service"
linkTitle: "Fault Injection Service"
weight: 1
description: Use Fault Injection Service to simulate faults in your infrastructure and test its fault tolerance
tags: ["Pro image"]
---

## Introduction

The [Fault Injection Service](https://aws.amazon.com/fis/) is a fully managed service designed to help you improve the resilience of your applications by simulating real-world outages and operational issues.
This service allows you to conduct controlled experiments on your AWS infrastructure, injecting faults and observing how your system responds under various conditions.

By using the Fault Injection Service, you can identify weaknesses, test recovery procedures, and ensure that your applications can withstand unexpected disruptions.
This proactive approach to reliability engineering enables you to enhance system robustness, minimize downtime, and maintain a high level of service availability for your users.

To see the FIS in action within a more complex application stack, please refer to the [Chaos Engineering Tutorials]({{< ref "tutorials" >}}).

{{< alert title="Note">}}
Fault Injection Service emulation is available as part of the LocalStack Enterprise plan.
If you'd like to try it out, please [contact us](https://www.localstack.cloud/demo) to request access.
{{< /alert >}}

## Prerequisites

The prerequisites for this guide are:

- LocalStack Pro with [LocalStack CLI](https://docs.localstack.cloud/getting-started/installation/#localstack-cli) & [LocalStack Auth Token](https://docs.localstack.cloud/getting-started/auth-token/)
- [AWS CLI](https://docs.localstack.cloud/user-guide/integrations/aws-cli/) with the [`awslocal` wrapper](https://docs.localstack.cloud/user-guide/integrations/aws-cli/#localstack-aws-cli-awslocal)
- [Docker](https://docs.docker.com/get-docker/) and [Docker Compose](https://docs.docker.com/compose/install/)

Ensure that you set the Auth Token as an environment variable before beginning:

{{< command >}}
$ LOCALSTACK_AUTH_TOKEN=<YOUR_LOCALSTACK_AUTH_TOKEN>
$ localstack start
{{< /command >}}

## Getting Started

This guide is created with users who are new to FIS in mind, and assumes basic knowledge of the AWS CLI and our `awslocal` wrapper script.

The following demo will depict constructing various FIS experiments designed to trigger different types of failures in a DynamoDB service.

Let's create a simple DynamoDB table called `Students` in the `us-east-1` region.

{{< command >}}
$ awslocal dynamodb create-table \
        --table-name Students \
        --attribute-definitions AttributeName=id,AttributeType=S \
        --key-schema AttributeName=id,KeyType=HASH \
        --billing-mode PAY_PER_REQUEST \
        --region us-east-1
<disable-copy>                                        
{
  "TableDescription": {
    "AttributeDefinitions": [
    {
      "AttributeName": "id",
      "AttributeType": "S"
    }
  ],
    "TableName": "Students",
    "KeySchema": [
      {
        "AttributeName": "id",
        "KeyType": "HASH"
      }
    ],
    "TableStatus": "ACTIVE",
    "CreationDateTime": 1710945576.193,
    "ProvisionedThroughput": {
      "LastIncreaseDateTime": 0.0,
      "LastDecreaseDateTime": 0.0,
      "NumberOfDecreasesToday": 0,
      "ReadCapacityUnits": 0,
      "WriteCapacityUnits": 0
    },
    "TableSizeBytes": 0,
    "ItemCount": 0,
    "TableArn": "arn:aws:dynamodb:us-east-1:000000000000:table/Students",
    "TableId": "c9ae13b6-ecf1-42f2-8d69-0e14d65a4dc3",
    "BillingModeSummary": {
      "BillingMode": "PAY_PER_REQUEST",
      "LastUpdateToPayPerRequestDateTime": 1710945576.193
    }
  }
}
</disable-copy>
{{< /command >}}

The newly created table has two items added:

{{< command >}}
$ awslocal dynamodb put-item --table-name Students --region us-east-1 --item '{
                                          "id": {"S": "1216"},
                                          "first name": {"S": "Liam"},
                                          "last name": {"S": "Davis"},
                                          "year": {"S": "Junior"},
                                          "enrolment date": {"S": "2023-03-19"}
                                      }'
                                      
$ awslocal dynamodb put-item --table-name Students --region us-east-1 --item '{
                                          "id": {"S": "1748"},
                                          "first name": {"S": "John"},
                                          "last name": {"S": "Doe"},
                                          "year": {"S": "Senior"},
                                          "enrolment date": {"S": "2022-03-19"}
                                      }'                                      
{{< /command >}}

And then we can look up one of the students by ID, also using the awslocal CLI:

{{< command >}}
$ awslocal dynamodb get-item --table-name Students --key '{"id": {"S": "1216"}}'
<disable-copy>
{
    "Item": {
        "id": {
            "S": "1216"
        },
        "last name": {
            "S": "Davis"
        },
        "enrolment date": {
            "S": "2023-03-19"
        },
        "first name": {
            "S": "Liam"
        },
        "year": {
            "S": "Junior"
        }
    }
}
</disable-copy>
{{< /command >}}

## Key concepts of FIS

Some of the most important concepts associated with a FIS experiment are:

**1. Experiment Templates**: Experiment templates define the actions, targets, and any stop conditions for your experiment.
They serve as blueprints for conducting fault injection experiments, allowing you to specify what resources are targeted, what faults are injected, and under what conditions the experiment should automatically stop.

**2. Actions**: Actions are the specific fault injection operations that the experiment performs on the target resources.
These can be injecting latency or throttling to API requests, completely blocking access to instances, etc.
Actions define the type of fault, parameters for the fault injection, and the targets affected.

**3. Targets**: Targets are the AWS resources on which the experiment actions will be applied.
To make things even more fine-grained, a specific operation of the service can be targeted.

**4. Stop Conditions**: Stop conditions are criteria that, when met, will automatically stop the experiment. 

**5. IAM Roles and Permissions**: To run experiments, AWS FIS requires specific IAM roles and permissions.
These are necessary for AWS FIS to perform actions on your behalf, like injecting faults into your resources.

**6. Experiment Execution**: When you start an experiment, AWS FIS executes the actions defined in the experiment template against the specified targets, adhering to any defined stop conditions.
The execution process is logged, and detailed information about the experiment's progress and outcome is provided.


## Examples

### Service Unavailability

In a file called `dynamodb-experiment.json` let's define a FIS experiment that causes all calls to the `GetItem` API of the DynamoDB service to return a 503 `Service Unavailable` response.
This failure will happen 100% of the times the method is called.

```json
{
        "actions": {
                "Test disruption": {
                        "actionId": "localstack:generic:api-error",
                        "parameters": {
                                "service": "dynamodb",
				                "operation": "GetItem",
                                "percentage": "100",
                                "exception": "Service Unavailable",
                                "errorCode": "503"
                        }
                }
        },
        "description": "Template for interfering with the DynamoDB service",
        "stopConditions": [{
                "source": "none"
        }],
        "roleArn": "arn:aws:iam:000000000000:role/ExperimentRole"
}
```

And create the experiment:

{{< command >}}
$ awslocal fis create-experiment-template --cli-input-json file://dynamodb-experiment.json
<disable-copy>
{
    "experimentTemplate": {
        "id": "547ec5c3-5ca1-4227-9b9d-a737223d1d42",
        "description": "Template for interfering with the DynamoDB service",
        "actions": {
            "Test disruption": {
                "actionId": "localstack:generic:api-error",
                "parameters": {
                    "service": "dynamodb",
                    "operation": "GetItem",
                    "percentage": "100",
                    "exception": "DynamoDbException",
                    "errorCode": "500"
                }
            }
        },
        "stopConditions": [
            {
                "source": "none"
            }
        ],
        "creationTime": 1710948862.04738,
        "lastUpdateTime": 1710948862.04738,
        "roleArn": "arn:aws:iam:000000000000:role/ExperimentRole"
    }
}
</disable-copy>
{{</ command >}}

The experiment needs to be started in order to be running:

{{< command >}}
$ awslocal fis start-experiment --experiment-template-id 547ec5c3-5ca1-4227-9b9d-a737223d1d42
<disable-copy>
{
    "experiment": {
        "id": "1a01327a-79d5-4202-8132-e56e55c9391b",
        "experimentTemplateId": "547ec5c3-5ca1-4227-9b9d-a737223d1d42",
        "roleArn": "arn:aws:iam:000000000000:role/ExperimentRole",
        "state": {
            "status": "running"
        },
        "actions": {
            "Test disruption": {
                "actionId": "localstack:generic:api-error",
                "parameters": {
                    "service": "dynamodb",
                    "operation": "GetItem",
                    "percentage": "100",
                    "exception": "DynamoDbException",
                    "errorCode": "500"
                }
            }
        },
        "stopConditions": [
            {
                "source": "none"
            }
        ],
        "creationTime": 1710949720.491161,
        "startTime": 1710949720.491161
    }
}
</disable-copy>
{{</ command >}}

The LocalStack logs are confirming the experiment related activity:

```bash
2024-03-20T15:34:22.048  INFO --- [   asgi_gw_0] localstack.request.aws     : AWS fis.CreateExperimentTemplate => 200
2024-03-20T15:48:40.492  INFO --- [   asgi_gw_0] localstack.request.aws     : AWS fis.StartExperiment => 200
```

Let's see it in action:

{{< command >}}
$ awslocal dynamodb get-item --table-name Students --key '{"id": {"S": "1216"}}'
<disable-copy>
An error occurred (DynamoDbException) when calling the GetItem operation (reached max retries: 9): Failing as per Fault Injection Simulator configuration
</disable-copy>
{{</ command >}}

The logs now show several attempts of performing the `GetItem` operation, before returning the error message:

```text
2024-03-20T15:54:16.630  INFO --- [   asgi_gw_0] localstack.request.aws     : AWS dynamodb.GetItem => 500 (DynamoDbException)
2024-03-20T15:54:16.707  INFO --- [   asgi_gw_1] localstack.request.aws     : AWS dynamodb.GetItem => 500 (DynamoDbException)
2024-03-20T15:54:16.825  INFO --- [   asgi_gw_0] localstack.request.aws     : AWS dynamodb.GetItem => 500 (DynamoDbException)
2024-03-20T15:54:17.040  INFO --- [   asgi_gw_1] localstack.request.aws     : AWS dynamodb.GetItem => 500 (DynamoDbException)
2024-03-20T15:54:17.476  INFO --- [   asgi_gw_0] localstack.request.aws     : AWS dynamodb.GetItem => 500 (DynamoDbException)
2024-03-20T15:54:18.301  INFO --- [   asgi_gw_1] localstack.request.aws     : AWS dynamodb.GetItem => 500 (DynamoDbException)
2024-03-20T15:54:19.925  INFO --- [   asgi_gw_0] localstack.request.aws     : AWS dynamodb.GetItem => 500 (DynamoDbException)
2024-03-20T15:54:23.141  INFO --- [   asgi_gw_0] localstack.request.aws     : AWS dynamodb.GetItem => 500 (DynamoDbException)
2024-03-20T15:54:29.559  INFO --- [   asgi_gw_1] localstack.request.aws     : AWS dynamodb.GetItem => 500 (DynamoDbException)
2024-03-20T15:54:42.381  INFO --- [   asgi_gw_1] localstack.request.aws     : AWS dynamodb.GetItem => 500 (DynamoDbException)
```

However, the `PutItem` and other operations are still working as expected:

{{< command >}}
$ awslocal dynamodb put-item --table-name Students --region us-east-1 --item '{
                                          "id": {"S": "9865"},
                                          "first name": {"S": "Jenny"},
                                          "last name": {"S": "Jones"},
                                          "year": {"S": "Sophomore"},
                                          "enrolment date": {"S": "2021-03-19"}
                                          }'
<disable-copy>
2024-03-20T16:00:27.958  INFO --- [   asgi_gw_0] localstack.request.aws     : AWS dynamodb.PutItem => 200
</disable-copy>
{{< /command >}}

Finally, the experiment can be stopped using the experiment's ID with the following command:

```bash
$ awslocal fis stop-experiment --id 1a01327a-79d5-4202-8132-e56e55c9391b
```


### Region Unavailability

This sort of experiment involves disabling entire regions to simulate regional outages and failovers.
Let's see what that would look like, in a separate file, `regional-experiment.json`:

```json
{
  "actions": {
    "regionUnavailable-us-east-1": {
      "actionId": "localstack:generic:api-error",
      "parameters": {
        "region": "us-east-1",
        "errorCode": "503"
      }
    },
    "regionUnavailable-us-west-2": {
      "actionId": "localstack:generic:api-error",
      "parameters": {
        "region": "us-west-2",
        "errorCode": "503"
      }
    }
  },
  "description": "Template for internal server error for regions us-west-2, us-east-1",
  "stopConditions": [{
        "source": "none"
  }],
  "roleArn": "arn:aws:iam:000000000000:role/ExperimentRole"
}
```
This template defines actions to simulate internal server errors (HTTP 503) in both `us-east-1` and `us-west-2` regions, without specific stop conditions.
These outages will affect all the resources within the regions.

The experiment is created and started:

{{< command >}}
$ awslocal fis create-experiment-template --cli-input-json file://regional-experiment.json
<disable-copy>
{
    "experimentTemplate": {
        "id": "19bec43e-9cb4-4bb8-9509-bf71c6e313c4",
        "description": "Template for internal server error for regions us-west-2, us-east-1",
        "actions": {
            "regionUnavailable-us-east-1": {
                "actionId": "localstack:generic:api-error",
                "parameters": {
                    "region": "us-east-1",
                    "errorCode": "503"
                }
            },
            "regionUnavailable-us-west-2": {
                "actionId": "localstack:generic:api-error",
                "parameters": {
                    "region": "us-west-2",
                    "errorCode": "503"
                }
            }
        },
        "stopConditions": [
            {
                "source": "none"
            }
        ],
        "creationTime": 1710951319.333033,
        "lastUpdateTime": 1710951319.333033,
        "roleArn": "arn:aws:iam:000000000000:role/ExperimentRole"
    }
}
</disable-copy>
{{< /command >}}

{{< command >}}
$ awslocal fis start-experiment --experiment-template-id 19bec43e-9cb4-4bb8-9509-bf71c6e313c4
<disable-copy>
{
    "experiment": {
        "id": "1a650841-bc81-4b4b-9317-6ec52df51c1d",
        "experimentTemplateId": "19bec43e-9cb4-4bb8-9509-bf71c6e313c4",
        "roleArn": "arn:aws:iam:000000000000:role/ExperimentRole",
        "state": {
            "status": "running"
        },
        "actions": {
            "regionUnavailable-us-east-1": {
                "actionId": "localstack:generic:api-error",
                "parameters": {
                    "region": "us-east-1",
                    "errorCode": "503"
                }
            },
            "regionUnavailable-us-west-2": {
                "actionId": "localstack:generic:api-error",
                "parameters": {
                    "region": "us-west-2",
                    "errorCode": "503"
                }
            }
        },
        "stopConditions": [
            {
                "source": "none"
            }
        ],
        "creationTime": 1710951725.475228,
        "startTime": 1710951725.475228
    }
}
</disable-copy>
{{< /command >}}

The previously created table in the `us-east-1` region, is not reachable, but this time a different error is thrown, the one that we defined in the latest experiment template:

{{< command >}}
$ awslocal dynamodb get-item --table-name Students --region us-east-1 --key '{"id": {"S": "1216"}}'
<disable-copy>
An error occurred (InternalError) when calling the GetItem operation (reached max retries: 9): Failing as per Fault Injection Simulator configuration
</disable-copy>
{{< /command >}}

However, the `eu-central-1` region is unaffected, and a new table can be created and used in that area.

{{< command >}}
$ awslocal dynamodb create-table \
                        --table-name Students \
                        --attribute-definitions AttributeName=id,AttributeType=S \
                        --key-schema AttributeName=id,KeyType=HASH \
                        --billing-mode PAY_PER_REQUEST \
                        --region eu-central-1
<disable-copy>
{
    "TableDescription": {
        "AttributeDefinitions": [
            {
                "AttributeName": "id",
                "AttributeType": "S"
            }
        ],
        "TableName": "Students",
        "KeySchema": [
            {
                "AttributeName": "id",
                "KeyType": "HASH"
            }
        ],
        "TableStatus": "ACTIVE",
        "CreationDateTime": 1710952212.617,
        "ProvisionedThroughput": {
            "LastIncreaseDateTime": 0.0,
            "LastDecreaseDateTime": 0.0,
            "NumberOfDecreasesToday": 0,
            "ReadCapacityUnits": 0,
            "WriteCapacityUnits": 0
        },
        "TableSizeBytes": 0,
        "ItemCount": 0,
        "TableArn": "arn:aws:dynamodb:eu-central-1:000000000000:table/Students",
        "TableId": "917f7df1-0050-433a-8647-427f072e7409",
        "BillingModeSummary": {
            "BillingMode": "PAY_PER_REQUEST",
            "LastUpdateToPayPerRequestDateTime": 1710952212.617
        }
    }
}
</disable-copy>
{{< /command >}}


```bash
awslocal dynamodb put-item --table-name Students --region eu-central-1 --item '{
                                                                                "id": {"S": "1111"},
                                                                                "first name": {"S": "Alice"},
                                                                                "last name": {"S": "Simpson"},
                                                                                "year": {"S": "Freshman"},
                                                                                "enrolment date": {"S": "2020-03-19"}
                                                                                }'
                                                                                
2024-03-20T16:34:57.164  INFO --- [   asgi_gw_0] localstack.request.aws     : AWS dynamodb.PutItem => 200
```

Just as with the earlier experiment, this one should be stopped by running the following command:

```bash
$ awslocal fis stop-experiment --id e49283c1-c2e0-492b-b69f-9fbd710bc1e3
```

### Service Latency

Let's now add some latency to our DynamoDB API calls.
First the definition of a new experiment template in another file, `latency-experiment.json`:

```json
{
  "actions": {
    "latency": {
      "actionId": "localstack:generic:latency",
      "parameters": {
        "region": "us-east-1",
        "latencyMilliseconds": 5000
      }
    }
  },
  "description": "template for testing delays in DynamoDB API calls",
  "stopConditions": [],
  "roleArn": "arn:aws:iam:000000000000:role/ExperimentRole"
}
```

After saving the file, we can create and start the experiment:

{{< command >}}
$ awslocal fis create-experiment-template --cli-input-json file://latency-experiment.json
<disable-copy>
{
    "experimentTemplate": {
        "id": "1f6e0ce8-57ed-4987-a7e5-b85ba3f5b933",
        "description": "template for testing delays in DynamoDB API calls",
        "actions": {
            "latency": {
                "actionId": "localstack:generic:latency",
                "parameters": {
                    "service": "dynamodb",
                    "region": "us-east-1",
                    "latencyMilliseconds": "5000"
                }
            }
        },
        "stopConditions": [],
        "creationTime": 1711024346.972359,
        "lastUpdateTime": 1711024346.972359,
        "roleArn": "arn:aws:iam:000000000000:role/ExperimentRole"
    }
}
</disable-copy>
{{< /command >}}

{{< command >}}
$ awslocal fis start-experiment --experiment-template-id 1f6e0ce8-57ed-4987-a7e5-b85ba3f5b933
<disable-copy>
{
    "experiment": {
        "id": "dd598567-56e6-4d00-9ef5-15c7e90e7851",
        "experimentTemplateId": "1f6e0ce8-57ed-4987-a7e5-b85ba3f5b933",
        "roleArn": "arn:aws:iam:000000000000:role/ExperimentRole",
        "state": {
            "status": "running"
        },
        "actions": {
            "latency": {
                "actionId": "localstack:generic:latency",
                "parameters": {
                    "service": "dynamodb",
                    "region": "us-east-1",
                    "latencyMilliseconds": "5000"
                }
            }
        },
        "stopConditions": [],
        "creationTime": 1711024425.844646,
        "startTime": 1711024425.844646
    }
}
</disable-copy>
{{< /command >}}

This FIS experiment introduces a delay of 5 seconds to all DynamoDB API calls within the `us-east-1` region.
Tables located in the `eu-central-1` region, or any other service, remain unaffected.
To extend the latency effect to a regional level, the specific service constraint can be omitted, thereby applying the latency to all resources within the selected region.

As always, remember to stop your experiment, so it does not cause unexpected issues down the line:

```bash
$ awslocal fis stop-experiment --id dd598567-56e6-4d00-9ef5-15c7e90e7851
```

Remember to replace the IDs with your own corresponding values.

### Experiment overview

If you want to keep track of all your experiments and make sure nothing is running in the background to hinder any other work, you can get an overview by using the command:

{{< command >}}
$ awslocal fis list-experiments
<disable-copy>
{
    "experiments": [
        {
            "id": "1a01327a-79d5-4202-8132-e56e55c9391b",
            "experimentTemplateId": "547ec5c3-5ca1-4227-9b9d-a737223d1d42",
            "state": {
                "status": "stopped"
            },
            "creationTime": 1710949720.491161
        },
        {
            "id": "1a650841-bc81-4b4b-9317-6ec52df51c1d",
            "experimentTemplateId": "19bec43e-9cb4-4bb8-9509-bf71c6e313c4",
            "state": {
                "status": "stopped"
            },
            "creationTime": 1710951725.475228
        },
        {
            "id": "e49283c1-c2e0-492b-b69f-9fbd710bc1e3",
            "experimentTemplateId": "19bec43e-9cb4-4bb8-9509-bf71c6e313c4",
            "state": {
                "status": "stopped"
            },
            "creationTime": 1710951872.250418
        },
        {
            "id": "dd598567-56e6-4d00-9ef5-15c7e90e7851",
            "experimentTemplateId": "1f6e0ce8-57ed-4987-a7e5-b85ba3f5b933",
            "state": {
                "status": "running"
            },
            "creationTime": 1711024425.844646
        }
    ]
}
</disable-copy>
{{< /command >}}

For more information on LocalStack FIS, please refer to the [FIS service documentation]({{< ref "user-guide/aws/fis" >}}).
