---
title: "Chaos Engineering: Simulating Outages using Chaos API"
linkTitle: "Chaos Engineering: Simulating Outages using Chaos API"
description: Use the Chaos API to simulate service disruptions and assess how well your infrastructure can deploy and recover from unexpected situations.
type: tutorials
teaser: ""
services:
- ecs
- ec2
- agw
- ddb
platform:
- Javascript
deployment:
- terraform
tags:
- API Gateway
- DynamoDB
- ECS
- Chaos Engineering
pro: true
leadimage: "banner.png"
---

## Introduction

[LocalStack Chaos API]({{< ref "chaos-api" >}}) is capable of simulating infrastructure faults to allow conducting controlled chaos engineering tests on AWS infrastructure.
Its purpose is to uncover vulnerabilities and improve system robustness.
Chaos API offers a means to deliberately introduce failures and observe their impacts, helping developers to better equip their systems against actual outages.

## Getting started

In this tutorial we study the effects of outages on a sample AWS application.
We use the Chaos API to simulate the outage and design a mitigation to make the application resilient against database outages.

This tutorial is designed for users new to the Chaos API and assumes basic knowledge of the AWS CLI and our [`awslocal`](https://github.com/localstack/awscli-local) wrapper script.
In this example, we will use the Chaos API to create controlled outages in a DynamoDB database.
The aim is to test the software's behavior and error handling capabilities.

For this particular example, we'll be using a [sample application repository](https://github.com/localstack-samples/samples-chaos-engineering/tree/master/chaos-api).
Clone the repository, and follow the instructions below to get started.

### Prerequisites

The general prerequisites for this guide are:

- LocalStack Pro with [LocalStack Auth Token]({{<ref "getting-started/auth-token">}})
- [AWS CLI]({{<ref "user-guide/integrations/aws-cli">}}) with the [`awslocal` wrapper]({{<ref "user-guide/integrations/aws-cli#localstack-aws-cli-awslocal">}})
- [Docker](https://docs.docker.com/get-docker/) and [Docker Compose](https://docs.docker.com/compose/install/)

Start LocalStack by using the `docker-compose.yml` file from the repository.
Ensure to set your Auth Token as an environment variable during this process.
The cloud resources will be automatically created upon the LocalStack start.

{{< command >}}
$ LOCALSTACK_AUTH_TOKEN=<YOUR_LOCALSTACK_AUTH_TOKEN>
$ docker compose up
{{< /command >}}

### Architecture

The following diagram shows the architecture that this application builds and deploys:

{{< figure src="arch-1.png" width="800">}}

### Preflight checks

Before starting any outages, it's important to verify that our application is functioning correctly.
Start by creating an entity and saving it.
To do this, use `cURL` to call the API Gateway endpoint for the POST method:

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

### Simulating the outage

Next, we will configure the Chaos API to target all APIs of the DynamoDB resource.
The Chaos API is powerful enough to refine outages to particular operations like `PutItem` or `GetItem`, but the objective here is to simulate a failure of entire database service.
The following configuration will cause all API calls to fail with a 100% failure rate, each resulting in an HTTP 500 status code and a `SomethingWentWrong` error.

{{<command>}}
curl --location --request PATCH 'http://localhost.localstack.cloud:4566/_localstack/chaos/faults' \
--header 'Content-Type: application/json' \
--data '
[
    {
        "service": "dynamodb",
        "probability": 0.8,
        "error": {
            "statusCode": 500,
            "code": "SomethingWentWrong"
        }
    }
]'
{{</ command >}}

This makes the database become inaccessible.
No external client or a LocalStack service can retrieve or add new products, resulting in the API Gateway returning an Internal Server Error.

Downtime and data loss are critical issues to avoid in enterprise applications.
Fortunately, encountering this issue early in the development phase allows developers to implement effective error handling and develop mechanisms to prevent data loss during a database outage.

### Designing a more resilient system

{{< figure src="arch-2.png" width="800">}}

A possible solution involves setting up an SNS topic, an SQS queue, and a Lambda function.
The Lambda function will be responsible for retrieving queued items and attempting to re-execute the `PutItem` operation on the database.
If DynamoDB remains unavailable, the item will be placed back in the queue for a later retry.

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

```text
2023-11-06T22:21:40.789 DEBUG --- [   asgi_gw_2] l.services.fis.handler     : FIS handler called with configs: {'dynamodb': {None: [(100, 'DynamoDbException', '500')]}}
2023-11-06T22:21:40.789  INFO --- [   asgi_gw_2] localstack.request.aws     : AWS dynamodb.PutItem => 500 (DynamoDbException)
2023-11-06T22:21:40.834 DEBUG --- [   asgi_gw_4] l.services.sns.publisher   : Topic 'arn:aws:sns:us-east-1:000000000000:ProductEventsTopic' publishing '5520d37a-fc21-4a73-b1bf-f9b9afce5908' to subscribed
'arn:aws:sqs:us-east-1:000000000000:ProductEventsQueue' with protocol 'sqs' (subscription 'arn:aws:sns:us-east-1:000000000000:ProductEventsTopic:0a4abf8c-744a-404a-9ff9-f132e25d1b30')
```

This element will remain in the queue until the outage is resolved.

### Ending the outage

To stop the outage, use the following configuration:

{{< command >}}
curl --location --request POST 'http://localhost.localstack.cloud:4566/_localstack/chaos/faults' \
--header 'Content-Type: application/json' \
--data '[]'
{{< /command >}}

With the outage now ended, the Product that initially failed to reach the database to finally be stored successfully.
This can be confirmed by scanning the database.

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

### Introducing network latency

The LocalStack Chaos API can also introduce a network latency for all connections.
This can be done with the following configuration:

{{< command >}}
$ curl --location --request POST 'http://localhost.localstack.cloud:4566/_localstack/chaos/effects' \
--header 'Content-Type: application/json' \
--data '{
    "latency": 5000
}'
{{< /command >}}

With this configured, you can use the same sample stack to observe and understand the effects of a 5-second delay on each service call.

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
An error occurred (InternalError) when calling the GetResources operation (reached max retries: 4)
</disable-copy>
{{< /command >}}
