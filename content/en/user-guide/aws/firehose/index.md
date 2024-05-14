---
title: "Kinesis Data Firehose"
linkTitle: "Kinesis Data Firehose"
description: >
  Get started with Kinesis Data Firehose on LocalStack
aliases:
- /user-guide/aws/kinesis-firehose/
---

{{< callout >}}
Amazon recently renamed Kinesis Data Firehose to Data Firehose.
{{< /callout >}}

## Introduction

Kinesis Data Firehose is a service provided by AWS that allows you to extract, transform and load streaming data into various destinations, such as Amazon S3, Amazon Redshift, and Elasticsearch. With Kinesis Data Firehose, you can ingest and deliver real-time data from different sources as it automates data delivery, handles buffering and compression, and scales according to the data volume.

LocalStack allows you to use the Kinesis Data Firehose APIs in your local environment to load and transform real-time data. The supported APIs are available on our [API coverage page](https://docs.localstack.cloud/references/coverage/coverage_firehose/), which provides information on the extent of Kinesis Data Firehose's integration with LocalStack.

## Getting started

This guide is designed for users new to Kinesis Data Firehouse and assumes basic knowledge of the AWS CLI and our [`awslocal`](https://github.com/localstack/awscli-local) wrapper script.

Start your LocalStack container using your preferred method. We will demonstrate how to use Firehose to load Kinesis data into Elasticsearch with S3 Backup with the AWS CLI.

### Create an Elasticsearch domain

You can create an Elasticsearch domain using the [`create-elasticsearch-domain`](https://docs.aws.amazon.com/cli/latest/reference/es/create-elasticsearch-domain.html) command. Execute the following command to create a domain named `es-local`:

{{< command >}}
$ awslocal es create-elasticsearch-domain --domain-name es-local
{{< / command >}}

Save the value of the `Endpoint` field from the response, as it will be required further down to confirm the setup.

### Create the source Kinensis stream

Now let us create our target S3 bucket and our source Kinesis stream:

Before creating the stream, we need to create an S3 bucket to store our backup data. You can do this using the [`mb`](https://docs.aws.amazon.com/cli/latest/reference/s3/mb.html) command:

{{< command >}}
$ awslocal s3 mb s3://kinesis-activity-backup-local
{{< / command >}}

You can now use the [`CreateStream`](https://docs.aws.amazon.com/kinesis/latest/APIReference/API_CreateStream.html) API to create a Kinesis stream named `kinesis-es-local-stream` with two shards:

{{< command >}}
$ awslocal kinesis create-stream \
  --stream-name kinesis-es-local-stream \
  --shard-count 2
{{< / command >}}

### Create a Firehouse delivery stream

You can now create the Firehose delivery stream. In this configuration, Elasticsearch serves as the destination, while S3 serves as the repository for our AllDocuments backup. Within the `kinesis-stream-source-configuration`, it is required to specify the ARN of our Kinesis stream and the role that will allow you the access to the stream.

The `elasticsearch-destination-configuration` sets vital parameters, which includes the access role, `DomainARN` of the Elasticsearch domain where you wish to publish, and the settings including the `IndexName` and `TypeName` for the Elasticsearch setup. Additionally to backup all documents to S3, the `S3BackupMode` parameter is set to `AllDocuments`, which is accompanied by `S3Configuration`.

{{< callout >}}
Within LocalStack's default configuration, IAM roles remain unverified and no strict validation is applied on ARNs. However, when operating within the AWS environment, you need to check the access rights of the specified role for the task.
{{< /callout >}}

You can use the [`CreateDeliveryStream`](https://docs.aws.amazon.com/firehose/latest/APIReference/API_CreateDeliveryStream.html) API to create a Firehose delivery stream named `activity-to-elasticsearch-local`:

{{< command >}}
$ awslocal firehose create-delivery-stream \
  --delivery-stream-name activity-to-elasticsearch-local \
  --delivery-stream-type KinesisStreamAsSource \
  --kinesis-stream-source-configuration "KinesisStreamARN=arn:aws:kinesis:us-east-1:000000000000:stream/kinesis-es-local-stream,RoleARN=arn:aws:iam::000000000000:role/Firehose-Reader-Role" \
  --elasticsearch-destination-configuration "RoleARN=arn:aws:iam::000000000000:role/Firehose-Reader-Role,DomainARN=arn:aws:es:us-east-1:000000000000:domain/es-local,IndexName=activity,TypeName=activity,S3BackupMode=AllDocuments,S3Configuration={RoleARN=arn:aws:iam::000000000000:role/Firehose-Reader-Role,BucketARN=arn:aws:s3:::kinesis-activity-backup-local}"
{{< / command >}}

On successful execution, the command will return the `DeliveryStreamARN` of the created delivery stream:

```json
{
    "DeliveryStreamARN": "arn:aws:firehose:us-east-1:000000000000:deliverystream/activity-to-elasticsearch-local"
}
```

### Testing the setup

Before testing the integration, it's necessary to confirm if the local Elasticsearch cluster is up. You can use the [`describe-elasticsearch-domain`](https://docs.aws.amazon.com/cli/latest/reference/es/describe-elasticsearch-domain.html) command to check the status of the Elasticsearch cluster. Run the following command:

{{< command >}}
$ awslocal es describe-elasticsearch-domain \
  --domain-name es-local | jq ".DomainStatus.Processing"
{{< / command >}}

Once the command returns `false`, you can move forward with data ingestion. The data can be added to the source Kinesis stream or directly to the Firehose delivery stream.

You can add data to the Kinesis stream using the [`PutRecord`](https://docs.aws.amazon.com/kinesis/latest/APIReference/API_PutRecord.html) API. The following command adds a record to the stream:

{{< command >}}
$ awslocal kinesis put-record \
  --stream-name kinesis-es-local-stream \
  --data '{ "target": "barry" }' \
  --partition-key partition
{{< / command >}}

{{< callout "tip" >}}
For users using AWS CLI v2, consider adding `--cli-binary-format raw-in-base64-out` to the command mentioned above.
{{< /callout >}}

You can use the [`PutRecord`](https://docs.aws.amazon.com/firehose/latest/APIReference/API_PutRecord.html) API to add data to the Firehose delivery stream. The following command adds a record to the stream:

{{< command >}}
$ awslocal firehose put-record \
  --delivery-stream-name activity-to-elasticsearch-local \
  --record '{ "Data": "eyJ0YXJnZXQiOiAiSGVsbG8gd29ybGQifQ==" }'
{{< / command >}}

To review the entries in Elasticsearch, you can employ `cURL` for simplicity. Remember to replace the URL with the `Endpoint` field from the initial `create-elasticsearch-domain` operation.

{{< command >}}
$ curl -s http://es-local.us-east-1.es.localhost.localstack.cloud:443/activity/_search | jq '.hits.hits'
{{< / command >}}

You will get an output similar to the following:

```json
[
  {
    "_index": "activity",
    "_type": "activity",
    "_id": "f38e2c49-d101-46aa-9ce2-0d2ea8fcd133",
    "_score": 1,
    "_source": {
      "target": "Hello world"
    }
  },
  {
    "_index": "activity",
    "_type": "activity",
    "_id": "d2f1c125-b3b0-4c7c-ba90-8acf4075a682",
    "_score": 1,
    "_source": {
      "target": "barry"
    }
  }
]
```

If you receive a comparable output, your Firehose delivery stream setup is accurate! Additionally, take a look at the designated S3 bucket to ensure the backup process is functioning correctly.

## Examples

The following code snippets and sample applications provide practical examples of how to use Kinesis Data Firehose in LocalStack for various use cases:

- [Search application with Lambda, Kinesis, Firehose, ElasticSearch, S3](https://github.com/localstack/sample-fuzzy-movie-search-lambda-kinesis-elasticsearch)
- [Streaming Data Pipeline with Kinesis, Tinybird, CloudWatch, Lambda](https://github.com/localstack/serverless-streaming-data-pipeline)
