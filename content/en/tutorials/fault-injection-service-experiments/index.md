---
title: "Chaos Engineering: Running Experiments with Fault Injection Service"
linkTitle: "Chaos Engineering: Running Experiments with Fault Injection Service"
weight: 8
description: >
  Conduct experiments on your AWS infrastructure to simulate faults and understand their effects, enhancing application resilience.
type: tutorials
teaser: ""
services:
- fis
- agw
- ddb
- lmb
platform:
- Java
deployment:
- awscli
tags:
- BASH
- FIS
- API Gateway
- DynamoDB
- Lambda
pro: true
leadimage: "fis-experiments.png"
---

> TODO


## Introduction

Fault Injection Simulator (FIS) is a service designed for conducting controlled chaos engineering tests on AWS infrastructure. Its purpose is to uncover vulnerabilities and improve system robustness. FIS offers a means to deliberately introduce failures and observe their impacts, helping developers to better equip their systems against actual outages. To read about the FIS service, refer to the dedicated [FIS documentation](https://docs.localstack.cloud/user-guide/aws/fis/).

## Getting started

This tutorial is designed for users new to the Fault Injection Simulator and assumes basic knowledge of the AWS CLI and our
[`awslocal`](https://github.com/localstack/awscli-local) wrapper script. In this example, we will use the FIS to create controlled outages in a DynamoDB database. The aim is to test the software's behavior and error handling capabilities.

For this particular example, we'll be using a [sample application repository](https://github.com/localstack-samples/samples-chaos-engineering/tree/main/FIS-experiments). Clone the repository, and follow the instructions below to get started.

### Prerequisites

The general prerequisites for this guide are:

- LocalStack Pro with [LocalStack Auth Token]({{<ref "getting-started/auth-token">}})
- [AWS CLI]({{<ref "user-guide/integrations/aws-cli">}}) with the [`awslocal` wrapper]({{<ref "user-guide/integrations/aws-cli#localstack-aws-cli-awslocal">}})
- [Docker](https://docs.docker.com/get-docker/) and [Docker Compose](https://docs.docker.com/compose/install/)

Start LocalStack by using the `docker-compose.yml` file from the repository. Ensure to set your Auth Token as an environment variable during this process. The cloud resources will be automatically created upon the LocalStack start.

{{< command >}}
$ LOCALSTACK_AUTH_TOKEN=<YOUR_LOCALSTACK_AUTH_TOKEN>
$ docker compose up
{{< /command >}}

### Application Architecture

The following diagram shows the architecture that this application builds and deploys:

{{< figure src="fis-experiment-1.png" width="800">}}

### Creating an experiment template

Before starting any FIS experiments, it's important to verify that our application is functioning correctly. Start by creating an entity and saving it. To do this, use `cURL` to call the API Gateway endpoint for the POST method:

{{< command >}}
$ curl --location 'http://12345.execute-api.localhost.localstack.cloud:4566/dev/productApi' \
--header 'Content-Type: application/json' \
--data '{
    "id": "prod-2004",
    "name": "Ultimate Gadget",
    "price": "49.99",
    "description": "The Ultimate Gadget is the perfect tool for tech enthusiasts looking for the next level in gadgetry. Compact, powerful, and loaded with features."
}'
<disable-copy>
Product added/updated successfully.
</disable-copy>
{{< /command >}}

You can use the file named `experiment-ddb.json` that contains the FIS experiment configuration. This file will be used in the upcoming call to the [`CreateExperimentTemplate`](https://docs.aws.amazon.com/fis/latest/APIReference/API_CreateExperimentTemplate.html) API within the FIS resource.

```bash
$ cat experiment-ddb.json
{
        "actions": {
                "Test action 1": {
                        "actionId": "localstack:generic:api-error",
                        "parameters": {
                                "service": "dynamodb",
                                "api": "all",
                                "percentage": "100",
                                "exception": "DynamoDbException",
                                "errorCode": "500"
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

This template is designed to target all APIs of the DynamoDB resource. While it's possible to specify particular operations like `PutItem` or `GetItem`, the objective here is to entirely disconnect the database.

As a result, this configuration will cause all API calls to fail with a 100% failure rate, each resulting in an HTTP 500 status code and a `DynamoDbException`.

{{<command>}}
$ awslocal fis create-experiment-template --cli-input-json file://experiment-ddb.json
<disable-copy>
{
    "experimentTemplate": {
        "id": "895591e8-11e6-44c4-adc3-86592010562b",
        "description": "Template for interfering with the DynamoDB service",
        "actions": {
            "Test action 1": {
                "actionId": "localstack:generic:api-error",
                "parameters": {
                    "service": "dynamodb",
                    "api": "all",
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
        "creationTime": 1699308754.415716,
        "lastUpdateTime": 1699308754.415716,
        "roleArn": "arn:aws:iam:000000000000:role/ExperimentRole"
    }   
}
</disable-copy>
{{</ command >}}

Take note of the `id` field in the response. This is the ID of the experiment template that will be used in the next step.

### Starting the experiment

Following the creation of the experiment template, you can create a new experiment using the template's ID.

{{< command >}}
$ awslocal fis start-experiment --experiment-template-id <EXPERIMENT_TEMPLATE_ID>
<disable-copy>
{
    "experiment": {
        "id": "1b1238fd-316d-4956-93e7-5ada677a6f69",
        "experimentTemplateId": "895591e8-11e6-44c4-adc3-86592010562b",
        "roleArn": "arn:aws:iam:000000000000:role/ExperimentRole",
        "state": {
            "status": "running"
        },
        "actions": {
        "Test action 1": {
            "actionId": "localstack:generic:api-error",
            "parameters": {
                "service": "dynamodb",
                "api": "all",
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
        "creationTime": 1699308823.74327,
        "startTime": 1699308823.74327
    }
}
</disable-copy>
{{< /command >}}

Replace the `<EXPERIMENT_TEMPLATE_ID>` placeholder with the ID of the experiment template that was created in the previous step.

### Simulating an outage

Once the experiment starts, the database becomes inaccessible. This means users cannot retrieve or add new products, resulting in the API Gateway returning an Internal Server Error. Downtime and data loss are critical issues to avoid in enterprise applications.

Fortunately, encountering this issue early in the development phase allows developers to implement effective error handling and develop mechanisms to prevent data loss during a database outage.

It's important to note that this approach is not limited to DynamoDB; outages can be simulated for any storage resource.

### Setting up a solution

{{< figure src="fis-experiment-2.png" width="800">}}

A possible solution involves setting up an SNS topic, an SQS queue, and a Lambda function. The Lambda function will be responsible for retrieving queued items and attempting to re-execute the `PutItem` operation on the database. If DynamoDB remains unavailable, the item will be placed back in the queue for a later retry.

{{< command >}}
$ curl --location 'http://12345.execute-api.localhost.localstack.cloud:4566/dev/productApi' \
--header 'Content-Type: application/json' \
--data '{
    "id": "prod-1003",
    "name": "Super Widget",
    "price": "29.99",
    "description": "A versatile widget that can be used for a variety of purposes. Durable, reliable, and affordable."
}'
<disable-copy>                                      
A DynamoDB error occurred. Message sent to queue.      
</disable-copy>
{{< /command >}}

If we review the logs, it will show that the `DynamoDbException` has been managed effectively.

```bash
2023-11-06T22:21:40.789 DEBUG --- [   asgi_gw_2] l.services.fis.handler     : FIS handler called with configs: {'dynamodb': {None: [(100, 'DynamoDbException', '500')]}}
2023-11-06T22:21:40.789  INFO --- [   asgi_gw_2] localstack.request.aws     : AWS dynamodb.PutItem => 500 (DynamoDbException)
2023-11-06T22:21:40.834 DEBUG --- [   asgi_gw_4] l.services.sns.publisher   : Topic 'arn:aws:sns:us-east-1:000000000000:ProductEventsTopic' publishing '5520d37a-fc21-4a73-b1bf-f9b9afce5908' to subscribed 
'arn:aws:sqs:us-east-1:000000000000:ProductEventsQueue' with protocol 'sqs' (subscription 'arn:aws:sns:us-east-1:000000000000:ProductEventsTopic:0a4abf8c-744a-404a-9ff9-f132e25d1b30')
```

This element will remain in the queue until the outage is resolved.

### Stopping the experiment

To stop the experiment, use the following command:

{{< command >}}
$ awslocal fis stop-experiment --id <EXPERIMENT_ID>
<disable-copy>
{
    "experiment": {
        "id": "1b1238fd-316d-4956-93e7-5ada677a6f69",
        "experimentTemplateId": "895591e8-11e6-44c4-adc3-86592010562b",
        "roleArn": "arn:aws:iam:000000000000:role/ExperimentRole",
        "state": {
            "status": "stopped"
        },
        "actions": {
            "Test action 1": {
                "actionId": "localstack:generic:api-error",
                "parameters": {
                    "service": "dynamodb",
                    "api": "all",
                    "percentage": "100",
                    "exception": "DynamoDbException",
                    "errorCode": "500"
                },
                "startTime": 1699308823.750742,
                "endTime": 1699309736.259625
            }
        },
        "stopConditions": [
            {
                "source": "none"
            }
        ],
        "creationTime": 1699308823.74327,
        "startTime": 1699308823.74327,
        "endTime": 1699309736.259646
    }
}
</disable-copy>
{{< /command >}}

Replace the `<EXPERIMENT_ID>` placeholder with the ID of the experiment that was created in the previous step.

The experiment has been terminated, allowing the Product that initially failed to reach the database to finally be stored successfully. This can be confirmed by scanning the database.

{{< command >}}
$ awslocal dynamodb scan --table-name Products
<disable-copy>
{
    "Items": [
        {
        "name": {
            "S": "Super Widget"
        },
        "description": {
            "S": "A versatile widget that can be used for a variety of purposes. Durable, reliable, and affordable."
        },
        "id": {
            "S": "prod-1003"
        },
        "price": {
            "N": "29.99"
        }
    },
    {
        "name": {
            "S": "Ultimate Gadget"
        },
        "description": {
            "S": "The Ultimate Gadget is the perfect tool for tech enthusiasts looking for the next level in gadgetry. Compact, powerful, and loaded with features."
        },
        "id": {
        "S": "prod-2004"
        },
        "price": {
            "N": "49.99"
        }
    }
],
    "Count": 2,
    "ScannedCount": 2,
    "ConsumedCapacity": null
}
</disable-copy>
{{< /command >}}

### Configuring the latency

The LocalStack FIS service can also introduce latency using the following experiment template:

```bash
{
  "description": "template for testing delays in API calls",
  "actions": {
    "latency": {
      "actionId": "localstack:generic:api-error",
      "parameters": {
        "latency": "4"
      }
    }
  },
  "stopConditions": [
    {
      "source": "none"
    }
  ],
  "roleArn": "arn:aws:iam:000000000000:role/ExperimentRole"
}
```
Save this template as `latency-experiment.json` and use it to create an experiment definition through the FIS service:

{{< command >}}
$ awslocal fis create-experiment-template --cli-input-json file://latency-experiment.json
<disable-copy>
{
    "experimentTemplate": {
    "id": "966f5632-4e2c-4567-b99c-436c333e523f",
    "description": "template for testing delays in API calls",
    "actions": {
        "latency": {
            "actionId": "localstack:generic:api-error",
            "parameters": {
                "latency": "4"
            }
        }
    },
    "stopConditions": [
        {
            "source": "none"
        }
    ],
    "creationTime": 1699619228.208613,
    "lastUpdateTime": 1699619228.208613,
    "roleArn": "arn:aws:iam:000000000000:role/ExperimentRole"
    }
}
</disable-copy>
$ awslocal fis start-experiment --experiment-template-id <EXPERIMENT_TEMPLATE_ID>
{{< /command >}}

Replace the `<EXPERIMENT_TEMPLATE_ID>` placeholder with the ID of the experiment template that was created in the previous step.

While the experiment is active, you can use the same sample stack to observe and understand the effects of a 4-second delay on each service call.

{{< command >}}
$ curl --location 'http://12345.execute-api.localhost.localstack.cloud:4566/dev/productApi' \
--header 'Content-Type: application/json' \
--data '{
    "id": "prod-1088",
    "name": "Super Widget",
    "price": "29.99",
    "description": "A versatile widget that can be used for a variety of purposes. Durable, reliable, and affordable."
}'
<disable-copy>
An error occurred (InternalError) when calling the GetResources operation (reached max retries: 4): Failing as per Fault Injection Simulator configuration
</disable-copy>
{{< /command >}}

