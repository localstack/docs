---
title: "Kinesis Data Firehose"
linkTitle: "Kinesis Data Firehose"
categories: ["LocalStack Community"]
description: >
  Kinesis Data Firehose
---

Kinesis Data Firehose is a service to extract, transform and load (ETL service) data to multiple destinations.
LocalStack supports Firehose with Kinesis as source, and S3, ElasticSearch or HttpEndpoints as targets.

## Examples

Firehose is a quite powerful service.
We will provide some examples to illustrate the possibilities of Firehose in LocalStack.

### Using Firehose to load Kinesis data into ElasticSearch with S3 Backup

As example, we want to deliver data sent to a Kinesis stream into ElasticSearch via Firehose, while making a full backup into a S3 bucket.
We will assume LocalStack is already [started correctly]({{< ref "get-started" >}}) and we have `awslocal` [installed]({{< ref "aws-cli" >}}).

First we will create our source kinesis stream:

{{< command >}}
$ awslocal kinesis create-stream ...
{{< / command >}}

And our target S3 bucket and ElasticSearch domain:

{{< command >}}
$ awslocal s3 mb ...
{{< / command >}}


{{< command >}}
$ awslocal es create-domain ...
{{< / command >}}

We need the Endpoint returned here later for the confirmation of our setup.

Next, we will create our firehose delivery stream with ElasticSearch as destination, and S3 as target for our AllDocuments backup.
We set the ARN of our kinesis stream in the kinesis-stream-source-configuration as well as the role we want to use for accessing the stream.

{{< alert >}}
**Note:** In LocalStack, per default, the IAM roles will not be verified, so you can provide any ARN here. In AWS, you need to check the access rights of the specified role for the task.
{{< /alert >}}



{{< command >}}
$ awslocal firehose create-delivery-stream...
{{< / command >}}
