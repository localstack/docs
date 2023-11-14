---
title: "Subsequent Configurations"
linkTitle: "Subsequent Configurations"
weight: 1
description: Configuring LocalStack for chaos engineering via environment variables.
---

## Introduction

Injecting controlled chaos into your development environment can significantly bolster the resilience of your services. 
With LocalStack, users have the option to introduce a few intentional errors into their workflows, specifically targeting
the Kinesis and DynamoDB services. By simply configuring environment variables you can simulate disruptions. This minimal 
setup allows you to observe and strengthen the response mechanisms of these critical AWS services, ensuring your 
architecture remains robust under adverse conditions with minimal upfront configuration.

This guide is designed for demonstrating the `DYNAMODB_ERROR_PROBABILITY` and `KINESIS_ERROR_PROBABILITY` configuration flags 
and assumes basic knowledge of the AWS CLI and our [`awslocal`](https://github.com/localstack/awscli-local) wrapper script.
To find out more about all the configuration possibilities please refer to the dedicated [documentation page](https://docs.localstack.cloud/references/configuration/).

## Kinesis Error Probability

By using `KINESIS_ERROR_PROBABILITY`, the user can define random injections of `ProvisionedThroughputExceededException` errors into Kinesis API responses.
This field take a decimal value between 0.0(default) and 1.0.

Let's start LocalStack defining a 50% change of Kinesis returning a `ProvisionedThroughputExceededException` response.

```bash
$ KINESIS_ERROR_PROBABILITY=0.5 localstack start
```

After, we need to create a Kinesis stream using the AWS CLI, using the `create-stream` command. Here's an example that 
creates a Kinesis stream named ProductsStream with a specified number of shards:

```bash
$ awslocal kinesis create-stream --stream-name ProductsStream --shard-count 1
```

Let's assume we have a convert Product JSON into a Base64-encoded string. Now, let's put this record into the stream:

```bash
$ awslocal kinesis put-record --stream-name ProductsStream --partition-key "12345" --data "eyJwcm9kdWN0SWQiOiIxMjMiLCJwcm9kdWN0TmFtZSI6IlN1cGVyV2lkZ2V0IiwicHJvZHVjdFByaWNlIjoiMTk5Ljk5In0="
```

After repeating this operation with similar values, we can observe the logs and notice that our configuration works as expected, however, the records 
will be added only upon successful calls:

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

The `DYNAMODB_ERROR_PROBABILITY` behaves the same as with Kinesis, returning a `ProvisionedThroughputExceededException` response from the DynamoDB service.
This field also takes a decimal value between 0.0(default) and 1.0.

Start LocalStack, defining a 0.8 value for the `DYNAMODB_ERROR_PROBABILITY`:

```bash
$ DYNAMODB_ERROR_PROBABILITY=0.8 localstack start
```

We can now proceed to create a table:

```bash
$ awslocal dynamodb create-table \
        --table-name Products \
        --attribute-definitions AttributeName=ProductId,AttributeType=S \
        --key-schema AttributeName=ProductId,KeyType=HASH \
        --provisioned-throughput ReadCapacityUnits=1,WriteCapacityUnits=1
```

And we can start adding items:

```bash
awslocal dynamodb put-item \
            --table-name Products \
            --item '{
            "ProductId": {"S": "123"},
            "ProductName": {"S": "SuperWidget"},
            "ProductPrice": {"N": "199.99"}
        }'
```

Now the logs will look a little different. We can observe a more aggressive exception throwing behaviour, before the underlying `boto3`
retry mechanism kicks in:

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

Because of the retry mechanism, all items will make it to the DynamoDB table.