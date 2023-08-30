---
title: "Kinesis Data Analytics"
linkTitle: "Kinesis Data Analytics"
description: >
  Get started with Kinesis Data Analytics on LocalStack
---

Kinesis Data Analytics is a service offered by Amazon Web Services (AWS) that enables you to process and analyze streaming data in real-time.
Kinesis Data Analytics allows you to apply transformations, filtering, and enrichment to streaming data using standard SQL syntax.
You can also run Java or Scala programs against streaming sources to perform various operations on the data using Apache Flink.

LocalStack supports Kinesis Data Analytics via the Pro/Team offering, allowing you to use the Kinesis Data Analytics APIs in your local environment to run continuous SQL queries directly over your Kinesis data streams.
The supported APIs are available on our [API coverage page](https://docs.localstack.cloud/references/coverage/coverage_kinesisanalyticsv2/), which provides information on the extent of Kinesis Data Analytics integration with LocalStack.

## Getting started

This guide is designed for users new to Kinesis Data Analytics and assumes basic knowledge of the AWS CLI and our [`awslocal`](https://github.com/localstack/awscli-local) wrapper script.

Start your LocalStack container using your preferred method.
We will demonstrate how to create a Kinesis Analytics application for Apache Flink and the DataStream API using AWS CLI.

### Create Amazon Kinesis Data Streams

Before creating a Kinesis Data Analytics application, you need to create two Kinesis Data Streams.
You can create the streams using the [`CreateStream`](https://docs.aws.amazon.com/kinesis/latest/APIReference/API_CreateStream.html) API.
Execute the following command to create the streams:

{{< command >}}
$ awslocal kinesis create-stream \
      --stream-name ExampleInputStream \
      --shard-count 1
      --region us-west-2

$ awslocal kinesis create-stream \
      --stream-name ExampleOutputStream \
      --shard-count 1
      --region us-west-2
{{< /command >}}

### Download Apache Flink Streaming Java Code

To create a Kinesis Data Analytics application, you need to download the Java application code for Apache Flink.
You can find the code in the [Kinesis Data Analytics for Apache Flink GitHub repository](https://github.com/aws-samples/amazon-kinesis-data-analytics-java-examples).
Clone it on your local machine using [`git clone`](https://git-scm.com/docs/git-clone).

{{< command >}}
$ git clone https://github.com/aws-samples/amazon-kinesis-data-analytics-java-examples
{{< /command >}}

You can navigate to the `amazon-kinesis-data-analytics-java-examples/GettingStarted` directory to find the Java code for the Kinesis Data Analytics application.
The application creates source and sink connectors to access external resources using a `StreamExecutionEnvironment` object.


You can now compile the project using Apache Maven and the Java Development Kit (JDK) to create a JAR file.
Run the following command to compile and package the application into a JAR file:

{{< command >}}
$ mvn package -Dflink.version=1.15.3
{{< /command >}}

After the application is compiled successfully, you can find the JAR file in the `target/aws-kinesis-analytics-java-apps-1.0.jar` directory.

### Upload the Apache Flink Streaming Java Code

You can now create an S3 bucket to upload the JAR file.
Create an S3 bucket using the [`mb`](https://docs.aws.amazon.com/cli/latest/reference/s3/mb.html) command:

{{< command >}}
$ awslocal s3 mb s3://ka-app-code-kafka --region us-west-2
{{< /command >}}

You can now upload the JAR file to the S3 bucket using the [`cp`](https://docs.aws.amazon.com/cli/latest/reference/s3/cp.html) command:

{{< command >}}
$ awslocal s3 cp ./target/aws-kinesis-analytics-java-apps-1.0.jar s3://ka-app-code-kafka --region us-west-2
{{< /command >}}

### Create a Kinesis Data Analytics Application

You can now use the AWS CLI to create the Kinesis Data Analytics application.
Create a JSON file named `create_request.json`, and upload the following code to the file:

```json
{
    "ApplicationName": "test",
    "ApplicationDescription": "my java test app",
    "RuntimeEnvironment": "FLINK-1_15",
    "ServiceExecutionRole": "arn:aws:iam::000000000000:role/KA-stream-rw-role",
    "ApplicationConfiguration": {
        "ApplicationCodeConfiguration": {
            "CodeContent": {
                "S3ContentLocation": {
                    "BucketARN": "arn:aws:s3:::ka-app-code-kafka",
                    "FileKey": "aws-kinesis-analytics-java-apps-1.0.jar"
                }
            },
            "CodeContentType": "ZIPFILE"
        },
        "EnvironmentProperties":  { 
         "PropertyGroups": [ 
            { 
               "PropertyGroupId": "ProducerConfigProperties",
               "PropertyMap" : {
                    "flink.stream.initpos" : "LATEST",
                    "aws.region" : "us-east-1",
                    "AggregationEnabled" : "false"
               }
            },
            { 
               "PropertyGroupId": "ConsumerConfigProperties",
               "PropertyMap" : {
                    "aws.region" : "us-east-1"
               }
            }
         ]
      }
    }
}
```

You can now create the Kinesis Data Analytics application using the [`CreateApplication`](https://docs.aws.amazon.com/kinesisanalytics/latest/apiv2/API_CreateApplication.html) API.
Execute the following command to create the application:

{{< command >}}
$ awslocal kinesisanalyticsv2 create-application \
      --cli-input-json file://create_request.json \
      --region us-west-2
{{< /command >}}

The application is now created.
You can now go ahead and run the application!

### Writing sample data to the input stream

You can now write sample data to the input stream using the following Python script, named `script.py`:

```python3
import datetime
import json
import random
import boto3

STREAM_NAME = "ExampleInputStream"

endpoint_url = "http://localhost.localstack.cloud:4566"

def get_data():
    return {
        'event_time': datetime.datetime.now().isoformat(),
        'ticker': random.choice(['AAPL', 'AMZN', 'MSFT', 'INTC', 'TBV']),
        'price': round(random.random() * 100, 2)}


def generate(stream_name, kinesis_client):
    while True:
        data = get_data()
        print(data)
        kinesis_client.put_record(
            StreamName=stream_name,
            Data=json.dumps(data),
            PartitionKey="partitionkey")


if __name__ == '__main__':
    generate(STREAM_NAME, boto3.client('kinesis', endpoint_url=endpoint_url, region_name='us-west-2'))
```

Run the following command to execute the script:

{{< command >}}
$ python3 script.py
{{< /command >}}
