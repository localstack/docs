---
title: "IAM Coverage"
linkTitle: "IAM Coverage"
weight: 13
description: >
    This page lists the IAM Enforcement Feature Coverage for LocalStack's emulation of AWS services.
cascade:
  type: docs
---

## Supported Services

In principle, LocalStack supports all operations. However, not all services and their operations have been tested yet. The table below lists all IAM services and operations that have been tested, noting if they were ever denied or allowed during testing. It only includes operations performed with a principal, not as root, so test setups are excluded.

|Name          |operation                   |Access denied|Access allowed|
|--------------|----------------------------|-------------|--------------|
|acm           |ListCertificates            |Yes          |Yes           |
|apigateway    |DeleteRestApi               |No           |Yes           |
|apigateway    |CreateRestApi               |Yes          |Yes           |
|backup        |DescribeBackupVault         |Yes          |Yes           |
|batch         |CreateComputeEnvironment    |No           |Yes           |
|cloudformation|ListStacks                  |Yes          |Yes           |
|cloudwatch    |PutMetricData               |Yes          |Yes           |
|dynamodb      |DescribeTable               |No           |Yes           |
|dynamodb      |CreateTable                 |Yes          |Yes           |
|dynamodb      |DeleteTable                 |No           |Yes           |
|ecr           |DescribeImages              |Yes          |No            |
|efs           |DescribeFileSystems         |Yes          |Yes           |
|es            |DescribeElasticsearchDomains|Yes          |Yes           |
|events        |DeleteEventBus              |No           |Yes           |
|events        |PutEvents                   |Yes          |Yes           |
|events        |CreateEventBus              |Yes          |Yes           |
|kinesis       |CreateStream                |Yes          |Yes           |
|kinesis       |DeleteStream                |No           |Yes           |
|kms           |CreateKey                   |Yes          |Yes           |
|kms           |DescribeKey                 |Yes          |Yes           |
|lambda        |DeleteFunction              |No           |Yes           |
|lambda        |Invoke                      |Yes          |Yes           |
|lambda        |GetLayerVersion             |Yes          |Yes           |
|lambda        |CreateFunction              |Yes          |Yes           |
|logs          |CreateLogGroup              |Yes          |Yes           |
|logs          |PutLogEvents                |No           |Yes           |
|logs          |CreateLogStream             |No           |Yes           |
|logs          |DeleteLogGroup              |No           |Yes           |
|redshift      |DescribeClusters            |Yes          |Yes           |
|redshift-data |ListDatabases               |Yes          |Yes           |
|s3            |UploadPart                  |No           |Yes           |
|s3            |GetObject                   |Yes          |Yes           |
|s3            |DeleteBucket                |No           |Yes           |
|s3            |CreateBucket                |Yes          |Yes           |
|s3            |ListBuckets                 |Yes          |Yes           |
|s3            |CreateMultipartUpload       |Yes          |Yes           |
|s3            |CompleteMultipartUpload     |No           |Yes           |
|s3            |DeleteObject                |No           |Yes           |
|s3            |ListObjects                 |Yes          |Yes           |
|s3            |PutObject                   |Yes          |Yes           |
|secretsmanager|CreateSecret                |Yes          |Yes           |
|secretsmanager|GetSecretValue              |Yes          |Yes           |
|secretsmanager|DeleteSecret                |No           |Yes           |
|sns           |Publish                     |No           |Yes           |
|sqs           |GetQueueAttributes          |Yes          |No            |
|sqs           |CreateQueue                 |Yes          |Yes           |
|sqs           |SendMessage                 |Yes          |Yes           |
|sqs           |ReceiveMessage              |Yes          |Yes           |
|sqs           |DeleteQueue                 |No           |Yes           |
|stepfunctions |DeleteStateMachine          |No           |Yes           |
|stepfunctions |CreateStateMachine          |Yes          |Yes           |
|sts           |GetCallerIdentity           |No           |Yes           |

