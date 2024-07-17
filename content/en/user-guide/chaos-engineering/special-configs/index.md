---
title: "Special Configurations"
linkTitle: "Special Configurations"
weight: 4
description: Set up LocalStack for chaos engineering using environment variables.
tags: ["Enterprise plan"]
---

## Introduction

LocalStack allows users to inject intentional errors, particularly in Kinesis and DynamoDB.
You can introduce controlled chaos into your development environment enhance to enhance service resilience.
By configuring environment variables, you can simulate disruptions.
This simple setup helps improve the response mechanisms of these key AWS services, ensuring robust architecture under challenging conditions with minimal initial configuration.

This guide demonstrates the `DYNAMODB_ERROR_PROBABILITY` and `KINESIS_ERROR_PROBABILITY` configuration flags.
The guide assumes basic knowledge of the AWS CLI and our [`awslocal`](https://github.com/localstack/awscli-local) wrapper script.

## Kinesis Error Probability

The `KINESIS_ERROR_PROBABILITY` setting allows users to introduce `ProvisionedThroughputExceededException` errors randomly into Kinesis API responses.
The value for this setting ranges from 0.0 (default) to 1.0.

To demonstrate, set up LocalStack with `KINESIS_ERROR_PROBABILITY` at 0.5, indicating a 50% chance of receiving a `ProvisionedThroughputExceededException` from Kinesis.

{{< command >}}
$ KINESIS_ERROR_PROBABILITY=0.5 localstack start
{{< /command >}}

Next, create a Kinesis stream using the AWS CLI with the [`CreateStream`](https://docs.aws.amazon.com/kinesis/latest/APIReference/API_CreateStream.html) API.
For example, to create a stream named "ProductsStream" with one shard, use:

{{< command >}}
$ awslocal kinesis create-stream \
        --stream-name ProductsStream \
        --shard-count 1
{{< /command >}}

Assuming you have a product JSON converted into a Base64-encoded string, you can add this record to the stream like so:

{{< command >}}
$ awslocal kinesis put-record \
        --stream-name ProductsStream \
        --partition-key "12345" \
        --data "eyJwcm9kdWN0SWQiOiIxMjMiLCJwcm9kdWN0TmFtZSI6IlN1cGVyV2lkZ2V0IiwicHJvZHVjdFByaWNlIjoiMTk5Ljk5In0="
{{< /command >}}

After performing similar operations repeatedly, you can check the logs to verify that the configuration is working as intended.
Remember, records will only be added during successful calls.

```bash
2023-11-09T23:33:49.867  INFO --- [   asgi_gw_0] localstack.request.aws     : AWS kinesis.CreateStream => 200
2023-11-09T23:34:01.003  INFO --- [   asgi_gw_0] localstack.request.aws     : AWS kinesis.PutRecord => 200
2023-11-09T23:34:05.114  INFO --- [   asgi_gw_0] localstack.request.aws     : AWS kinesis.PutRecord => 200
2023-11-09T23:34:08.178  INFO --- [   asgi_gw_0] localstack.request.aws     : AWS kinesis.PutRecord => 400 (ProvisionedThroughputExceededException)
2023-11-09T23:34:08.346  INFO --- [   asgi_gw_0] localstack.request.aws     : AWS kinesis.PutRecord => 200
2023-11-09T23:34:09.726  INFO --- [   asgi_gw_0] localstack.request.aws     : AWS kinesis.PutRecord => 400 (ProvisionedThroughputExceededException)
2023-11-09T23:34:10.499  INFO --- [   asgi_gw_0] localstack.request.aws     : AWS kinesis.PutRecord => 200
2023-11-09T23:34:11.982  INFO --- [   asgi_gw_0] localstack.request.aws     : AWS kinesis.PutRecord => 200
```

## DynamoDB Error Probability

The `DYNAMODB_ERROR_PROBABILITY` setting, similar to the Kinesis configuration, allows for random `ProvisionedThroughputExceededException` responses from the DynamoDB service.
It also accepts a decimal value between 0.0 (default) and 1.0.

To start LocalStack with a high error probability for DynamoDB, set `DYNAMODB_ERROR_PROBABILITY` to 0.8:

{{< command >}}
$ DYNAMODB_ERROR_PROBABILITY=0.8 localstack start
{{< /command >}}

Next, create a DynamoDB table using the AWS CLI with the [`CreateTable`](https://docs.aws.amazon.com/amazondynamodb/latest/APIReference/API_CreateTable.html) API.
For example, to create a table named "Products" with a primary key of "ProductId", use:

```bash
$ awslocal dynamodb create-table \
        --table-name Products \
        --attribute-definitions AttributeName=ProductId,AttributeType=S \
        --key-schema AttributeName=ProductId,KeyType=HASH \
        --provisioned-throughput ReadCapacityUnits=1,WriteCapacityUnits=1
```

You can add items to the table using the [`PutItem`](https://docs.aws.amazon.com/amazondynamodb/latest/APIReference/API_PutItem.html) API.
For example, to add a product with an ID of "123", a name of "SuperWidget", and a price of "199.99", use:

```bash
awslocal dynamodb put-item \
            --table-name Products \
            --item '{
            "ProductId": {"S": "123"},
            "ProductName": {"S": "SuperWidget"},
            "ProductPrice": {"N": "199.99"}
        }'
```

The logs will now show a higher frequency of `ProvisionedThroughputExceededException` errors, followed by successful attempts due to the `boto3` retry mechanism:

```bash
2023-11-09T23:59:12.836  INFO --- [   asgi_gw_0] localstack.request.aws     : AWS dynamodb.CreateTable => 200
2023-11-09T23:59:27.889  INFO --- [   asgi_gw_1] localstack.request.aws     : AWS dynamodb.PutItem => 400 (ProvisionedThroughputExceededException)
2023-11-09T23:59:27.968  INFO --- [   asgi_gw_0] localstack.request.aws     : AWS dynamodb.PutItem => 400 (ProvisionedThroughputExceededException)
2023-11-09T23:59:28.089  INFO --- [   asgi_gw_1] localstack.request.aws     : AWS dynamodb.PutItem => 400 (ProvisionedThroughputExceededException)
2023-11-09T23:59:28.410  INFO --- [   asgi_gw_0] localstack.request.aws     : AWS dynamodb.PutItem => 200
2023-11-09T23:59:35.845  INFO --- [   asgi_gw_1] localstack.request.aws     : AWS dynamodb.PutItem => 400 (ProvisionedThroughputExceededException)
2023-11-09T23:59:35.911  INFO --- [   asgi_gw_0] localstack.request.aws     : AWS dynamodb.PutItem => 400 (ProvisionedThroughputExceededException)
2023-11-09T23:59:36.028  INFO --- [   asgi_gw_1] localstack.request.aws     : AWS dynamodb.PutItem => 400 (ProvisionedThroughputExceededException)
2023-11-09T23:59:36.249  INFO --- [   asgi_gw_0] localstack.request.aws     : AWS dynamodb.PutItem => 400 (ProvisionedThroughputExceededException)
2023-11-09T23:59:36.673  INFO --- [   asgi_gw_1] localstack.request.aws     : AWS dynamodb.PutItem => 400 (ProvisionedThroughputExceededException)
2023-11-09T23:59:37.484  INFO --- [   asgi_gw_0] localstack.request.aws     : AWS dynamodb.PutItem => 400 (ProvisionedThroughputExceededException)
2023-11-09T23:59:39.101  INFO --- [   asgi_gw_0] localstack.request.aws     : AWS dynamodb.PutItem => 400 (ProvisionedThroughputExceededException)
2023-11-09T23:59:42.326  INFO --- [   asgi_gw_1] localstack.request.aws     : AWS dynamodb.PutItem => 400 (ProvisionedThroughputExceededException)
2023-11-09T23:59:48.737  INFO --- [   asgi_gw_1] localstack.request.aws     : AWS dynamodb.PutItem => 400 (ProvisionedThroughputExceededException)
2023-11-10T00:00:01.606  INFO --- [   asgi_gw_1] localstack.request.aws     : AWS dynamodb.PutItem => 200
```

Despite these errors, the retry mechanism ensures that all items are eventually added to the DynamoDB table.
