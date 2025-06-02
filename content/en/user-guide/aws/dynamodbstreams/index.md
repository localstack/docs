---
title: DynamoDB Streams
linkTitle: DynamoDB Streams
description: Get started with DynamoDB Streams on LocalStack
---

## Introduction

DynamoDB Streams captures data modification events in a DynamoDB table.
The stream records are written to a DynamoDB stream, which is an ordered flow of information about changes to items in a table.
DynamoDB Streams records data in near-real time, enabling you to develop workflows that process these streams and respond based on their contents.

LocalStack supports DynamoDB Streams, allowing you to create and manage streams in a local environment.
The supported APIs are available on our [DynamoDB Streams coverage page]({{< ref "coverage_dynamodbstreams" >}}), which provides information on the extent of DynamoDB Streams integration with LocalStack.

## Getting started

This guide is designed for users new to DynamoDB Streams and assumes basic knowledge of the AWS CLI and our [`awslocal`](https://github.com/localstack/awscli-local) wrapper script.

Start your LocalStack container using your preferred method.
We will demonstrate the following process using LocalStack:

- A user adds an entry to a DynamoDB table.
- A new stream record is generated in DynamoDB Streams when an entry is added.
- This stream record triggers a Lambda function.
- If the record indicates a new entry in the DynamoDB table, the Lambda function extracts the data.

### Create a DynamoDB table

You can create a DynamoDB table named `BarkTable` using the [`CreateTable`](https://docs.aws.amazon.com/amazondynamodb/latest/APIReference/API_CreateTable.html) API.
Run the following command to create the table:

{{< command >}}
$ awslocal dynamodb create-table \
    --table-name BarkTable \
    --attribute-definitions AttributeName=Username,AttributeType=S AttributeName=Timestamp,AttributeType=S \
    --key-schema AttributeName=Username,KeyType=HASH  AttributeName=Timestamp,KeyType=RANGE \
    --provisioned-throughput ReadCapacityUnits=5,WriteCapacityUnits=5 \
    --stream-specification StreamEnabled=true,StreamViewType=NEW_AND_OLD_IMAGES
{{< /command >}}

The `BarkTable` has a stream enabled which you can trigger by associating a Lambda function with the stream.
You can notice that in the `LatestStreamArn` field of the response:

```bash
...
"LatestStreamArn": "arn:aws:dynamodb:000000000000:us-east-1:table/BarkTable/stream/timestamp
...
```

### Create a Lambda function

You can now create a Lambda function (`publishNewBark`) to process stream records from `BarkTable`.
Create a new file named `index.js` with the following code:

```javascript
'use strict';
var AWS = require("aws-sdk");

exports.handler = (event, context, callback) => {

    event.Records.forEach((record) => {
        console.log('Stream record: ', JSON.stringify(record, null, 2));

        if (record.eventName == 'INSERT') {
            var who = JSON.stringify(record.dynamodb.NewImage.Username.S);
            var when = JSON.stringify(record.dynamodb.NewImage.Timestamp.S);
            var what = JSON.stringify(record.dynamodb.NewImage.Message.S);
            var params = {
                Subject: 'A new bark from ' + who,
                Message: 'Woofer user ' + who + ' barked the following at ' + when + ':\n\n ' + what,
            };
        }
    });
    callback(null, `Successfully processed ${event.Records.length} records.`);
};
```

You can now create a Lambda function using the [`CreateFunction`](https://docs.aws.amazon.com/lambda/latest/dg/API_CreateFunction.html) API.
Run the following command to create the Lambda function:

{{< command >}}
$ zip index.zip index.js
$ awslocal lambda create-function \
    --function-name publishNewBark \
    --zip-file fileb://index.zip \
    --role roleARN \
    --handler index.handler \
    --timeout 50 \
    --runtime nodejs16.x \
    --role arn:aws:iam::000000000000:role/lambda-role
{{< /command >}}

### Invoke the Lambda function

To test the Lambda function, you can invoke it using the [`Invoke`](https://docs.aws.amazon.com/lambda/latest/dg/API_Invoke.html) API.
Create a new file named `payload.json` with the following content:

```json
{
    "Records": [
        {
            "eventID": "7de3041dd709b024af6f29e4fa13d34c",
            "eventName": "INSERT",
            "eventVersion": "1.1",
            "eventSource": "aws:dynamodb",
            "awsRegion": "us-east-1",
            "dynamodb": {
                "ApproximateCreationDateTime": 1479499740,
                "Keys": {
                    "Timestamp": {
                        "S": "2016-11-18:12:09:36"
                    },
                    "Username": {
                        "S": "John Doe"
                    }
                },
                "NewImage": {
                    "Timestamp": {
                        "S": "2016-11-18:12:09:36"
                    },
                    "Message": {
                        "S": "This is a bark from the Woofer social network"
                    },
                    "Username": {
                        "S": "John Doe"
                    }
                },
                "SequenceNumber": "13021600000000001596893679",
                "SizeBytes": 112,
                "StreamViewType": "NEW_IMAGE"
            },
            "eventSourceARN": "arn:aws:dynamodb:000000000000:us-east-1 ID:table/BarkTable/stream/2016-11-16T20:42:48.104"
        }
    ]
}
```

Run the following command to invoke the Lambda function:

{{< command >}}
$ awslocal lambda invoke \
    --function-name publishNewBark \
    --payload file://payload.json \
    --cli-binary-format raw-in-base64-out output.txt
{{< /command >}}

In the `output.txt` file, you should see the following output:

```text
"Successfully processed 1 records."
```

### Add event source mapping

To add the DynamoDB stream as an event source for the Lambda function, you need the stream ARN.
You can get the stream ARN using the [`DescribeTable`](https://docs.aws.amazon.com/amazondynamodb/latest/APIReference/API_DescribeTable.html) API.
Run the following command to get the stream ARN:

{{< command >}}
awslocal dynamodb describe-table --table-name BarkTable
{{< /command >}}

You can now create an event source mapping using the [`CreateEventSourceMapping`](https://docs.aws.amazon.com/lambda/latest/dg/API_CreateEventSourceMapping.html) API.
Run the following command to create the event source mapping:

{{< command >}}
awslocal lambda create-event-source-mapping \
    --function-name publishNewBark \
    --event-source arn:aws:dynamodb:us-east-1:000000000000:table/BarkTable/stream/2024-07-12T06:18:37.101  \
    --batch-size 1 \
    --starting-position TRIM_HORIZON
{{< /command >}}

Make sure to replace the `event-source` value with the stream ARN you obtained from the previous command.
You should see the following output:

```bash
{
    "UUID": "7ae3426a-eda6-4c10-a596-100c59bd6787",
    ...
    "EventSourceArn": "arn:aws:dynamodb:us-east-1:000000000000:table/BarkTable/stream/2024-07-12T06:18:37.101",
    "FunctionArn": "arn:aws:lambda:us-east-1:000000000000:function:publishNewBark",
    ...
    "FunctionResponseTypes": []
}
```

You can now test the event source mapping by adding an item to the `BarkTable` table using the [`PutItem`](https://docs.aws.amazon.com/amazondynamodb/latest/APIReference/API_PutItem.html) API.
Run the following command to add an item to the table:

{{< command >}}
$ awslocal dynamodb put-item \
    --table-name BarkTable \
    --item Username={S="Jane Doe"},Timestamp={S="2016-11-18:14:32:17"},Message={S="Testing...1...2...3"}
{{< /command >}}

You can find Lambda function being triggered in the LocalStack logs.

### Inspect the stream

You can list the streams using the [`ListStreams`](https://docs.aws.amazon.com/amazondynamodb/latest/APIReference/API_ListStreams.html) API.
Run the following command to list the streams:

{{< command >}}
awslocal dynamodbstreams list-streams
{{< /command >}}

The following output shows the list of streams:

```bash
{
    "Streams": [
        {
            "StreamArn": "arn:aws:dynamodb:us-east-1:000000000000:table/BarkTable/stream/2024-07-12T06:18:37.101",
            "TableName": "BarkTable",
            "StreamLabel": "2024-07-12T06:18:37.101"
        }
    ]
}
```

You can also describe the stream using the [`DescribeStream`](https://docs.aws.amazon.com/amazondynamodb/latest/APIReference/API_DescribeStream.html) API.
Run the following command to describe the stream:

{{< command >}}
$ awslocal dynamodbstreams describe-stream --stream-arn arn:aws:dynamodb:us-east-1:000000000000:table/BarkTable/stream/2024-07-12T06:18:37.101
{{< /command >}}

Replace the `stream-arn` value with the stream ARN you obtained from the previous command.
