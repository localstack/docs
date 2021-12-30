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
