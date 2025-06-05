---
title: "Kinesis Data Streams"
linkTitle: "Kinesis Data Streams"
description: Get started with Kinesis Data Streams on LocalStack
persistence: supported

---

## Introduction

Kinesis Data Streams is an AWS service for ingesting, buffering, and processing data in high throughput data streams.
It is used for applications that require real-time processing and deriving insights from data streams such as logs, metrics, user interactions, and sensor readings.

LocalStack allows you to use the Kinesis Data Streams APIs in your local environment from setting up data streams and configuring data processing to building real-time applications.
The supported APIs are available on our [API coverage page](https://docs.localstack.cloud/references/coverage/coverage_kinesis/).

## Getting started

This guide is designed for users new to Kinesis Data Streams and assumes basic knowledge of the AWS CLI and our [`awslocal`](https://github.com/localstack/awscli-local) wrapper script.

Start your LocalStack container using your preferred method.
We will demonstrate how to create a Lambda function to consume events from a Kinesis stream with the AWS CLI.

### Create a Lambda function

You need to create a Lambda function that receives a Kinesis event input and processes the messages that it contains.
Create a file named `index.mjs` with the following content:

```javascript
console.log('Loading function');

export const handler = (event, context) => {
    event.Records.forEach(record => {
        let payload = Buffer.from(record.kinesis.data, 'base64').toString('ascii');
        console.log('Decoded payload:', payload);
    });
};
```

You can create a Lambda function using the [`CreateFunction`](https://docs.aws.amazon.com/lambda/latest/dg/API_CreateFunction.html) API.
Run the following command to create a Lambda function named `ProcessKinesisRecords`:

{{< command >}}
$ zip function.zip index.mjs
$ awslocal lambda create-function \
    --function-name ProcessKinesisRecords \
    --zip-file fileb://function.zip \
    --handler index.handler \
    --runtime nodejs18.x \
    --role arn:aws:iam::000000000000:role/lambda-kinesis-role
{{< / command >}}

The following output would be retrieved:

```bash
{
    "FunctionName": "ProcessKinesisRecords",
    "FunctionArn": "arn:aws:lambda:us-east-1:000000000000:function:ProcessKinesisRecords",
    "Runtime": "nodejs18.x",
    "Role": "arn:aws:iam::000000000000:role/lambda-kinesis-role",
    "Handler": "index.handler",
    ...
}
```

### Invoke the Lambda function

Create a file named `input.txt` with the following JSON content:

```text
{
    "Records": [
        {
            "kinesis": {
                "kinesisSchemaVersion": "1.0",
                "partitionKey": "1",
                "sequenceNumber": "49590338271490256608559692538361571095921575989136588898",
                "data": "SGVsbG8sIHRoaXMgaXMgYSB0ZXN0Lg==",
                "approximateArrivalTimestamp": 1545084650.987
            },
            "eventSource": "aws:kinesis",
            "eventVersion": "1.0",
            "eventID": "shardId-000000000006:49590338271490256608559692538361571095921575989136588898",
            "eventName": "aws:kinesis:record",
            "invokeIdentityArn": "arn:aws:iam::000000000000:role/lambda-kinesis-role",
            "awsRegion": "us-east-1",
            "eventSourceARN": "arn:aws:kinesis:us-east-1:000000000000:stream/lambda-stream"
        }
    ]
}
```

The JSON contains a sample Kinesis event.
You can use the [`Invoke`](https://docs.aws.amazon.com/lambda/latest/dg/API_Invoke.html) API to invoke the Lambda function with the Kinesis event as input.
Execute the following command:

{{< command >}}
$ awslocal lambda invoke \
    --function-name ProcessKinesisRecords \
    --payload file://input.txt outputfile.txt
{{< / command >}}

### Create a Kinesis Stream

You can create a Kinesis Stream using the [`CreateStream`](https://docs.aws.amazon.com/kinesis/latest/APIReference/API_CreateStream.html) API.
Run the following command to create a Kinesis Stream named `lambda-stream`:

{{< command >}}
$ awslocal kinesis create-stream \
  --stream-name lambda-stream \
  --shard-count 1
{{< / command >}}

You can retrieve the Stream ARN using the [`DescribeStream`](https://docs.aws.amazon.com/kinesis/latest/APIReference/API_DescribeStream.html) API.
Execute the following command:

{{< command >}}
$ awslocal kinesis describe-stream \
  --stream-name lambda-stream
{{< / command >}}

The following output would be retrieved:

```json
{
    "StreamDescription": {
        "Shards": [
            {
                "ShardId": "shardId-000000000000",
                "HashKeyRange": {
                    "StartingHashKey": "0",
                    "EndingHashKey": "340282366920938463463374607431768211455"
                ...
            }
        ],
        "StreamARN": "arn:aws:kinesis:us-east-1:000000000000:stream/lambda-stream",
        "StreamName": "lambda-stream",
        "StreamStatus": "ACTIVE",
        ...
}
```

You can save the `StreamARN` value for later use.

### Add an Event Source in Lambda

You can add an Event Source to your Lambda function using the [`CreateEventSourceMapping`](https://docs.aws.amazon.com/lambda/latest/dg/API_CreateEventSourceMapping.html) API.
Run the following command to add the Kinesis Stream as an Event Source to your Lambda function:

{{< command >}}
$ awslocal lambda create-event-source-mapping \
    --function-name ProcessKinesisRecords \
    --event-source arn:aws:kinesis:us-east-1:000000000000:stream/lambda-stream \
    --batch-size 100 \
    --starting-position LATEST
{{< / command >}}

### Test the Event Source mapping

You can test the event source mapping by adding a record to the Kinesis Stream using the [`PutRecord`](https://docs.aws.amazon.com/kinesis/latest/APIReference/API_PutRecord.html) API.
Run the following command to add a record to the Kinesis Stream:

{{< command >}}
$ awslocal kinesis put-record \
    --stream-name lambda-stream \
    --partition-key 1 \
    --data "Hello, this is a test."
{{< / command >}}

You can fetch the CloudWatch logs for your Lambda function reading records from the stream, using AWS CLI or LocalStack Resource Browser.

### Performance Tuning

For high-volume workloads or large payloads, we recommend switching to the Scala engine via the `KINESIS_MOCK_PROVIDER_ENGINE=scala` flag, delivering up to 10x better performance compared to the default Node.js engine.

Additionally, the following parameters can be tuned:

- Increase `KINESIS_MOCK_MAXIMUM_HEAP_SIZE` beyond the default `512m` to reduce JVM memory pressure.
- Increase `KINESIS_MOCK_INITIAL_HEAP_SIZE` beyond the default `256m` to pre-allocate more JVM heap memory.
- Reduce `KINESIS_LATENCY` artificial response delays from the default `500` milliseconds (or disable entirely with `0`).

Refer to our [Kinesis configuration documentation](https://docs.localstack.cloud/references/configuration/#kinesis) for more details on these parameters.

{{< callout "note" >}}
`KINESIS_MOCK_MAXIMUM_HEAP_SIZE` and `KINESIS_MOCK_INITIAL_HEAP_SIZE` are only applicable when using the Scala engine.
Future versions of LocalStack will likely default to using the `scala` engine over the less-performant `node` version currently in use.
{{< /callout >}}

## Resource Browser

The LocalStack Web Application provides a Resource Browser for managing Kinesis Streams & Kafka Clusters.
You can access the Resource Browser by opening the LocalStack Web Application in your browser, navigating to the **Resources** section, and then clicking on **Kinesis** under the **Analytics** section.

<img src="kinesis-resource-browser.png" alt="Kinesis Resource Browser" title="Kinesis Resource Browser" width="900" />
<br>
<br>

The Resource Browser allows you to perform the following actions:

- **Create Stream**: Create a Kinesis Stream by specifying the **Stream Name**, **Shard Count**, and **Stream Mode**.
- **Create Cluster**: Create a Kafka Cluster by specifying the **Cluster Name**, **Kafka Version**, **Number Of Broker Nodes**, **Instance Type**, and more.
- **View Streams & Clusters**: Click on any of the listed resources to view its details by clicking on the desired Stream & Cluster.
- **Edit Streams & Clusters**: Click on any listed resources to edit its details by clicking on the desired Stream & Cluster.
- **Delete Streams & Clusters**: Select any listed resources to delete them by clicking the **Actions** button and selecting **Remove Selected**.

## Examples

The following code snippets and sample applications provide practical examples of how to use Kinesis in LocalStack for various use cases:

- [Search application with Lambda, Kinesis, Firehose, ElasticSearch, S3](https://github.com/localstack/sample-fuzzy-movie-search-lambda-kinesis-elasticsearch)
- [Streaming Data Pipeline with Kinesis, Tinybird, CloudWatch, Lambda](https://github.com/localstack/serverless-streaming-data-pipeline)

## Limitations

In multi-account setups, each AWS account launches a separate instance of Kinesis Mock, which is very resource intensive when a large number of AWS accounts are used.
An [open Kinesis Mock issue](https://github.com/etspaceman/kinesis-mock/issues/377) is being used to keep track of this feature.
