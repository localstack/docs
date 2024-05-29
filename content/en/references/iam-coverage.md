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

## Inter Service Enforcement

|Source Service|Target Service|Feature                |Operation                                                   |Implemented|Tested|
|--------------|--------------|-----------------------|------------------------------------------------------------|-----------|------|
|sns           |sqs           |SNS subscription       |sqs.SendMessage                                             |Yes        |Yes   |
|sns           |lambda        |SNS subscription       |lambda.Invoke                                               |Yes        |Yes   |
|lambda        |sqs           |Event destinations     |sqs.SendMessage                                             |Yes        |Yes   |
|lambda        |logs          |Storing Lambda logs    |logs.CreateLogGroup, logs.CreateLogStream, logs.PutLogEvents|Yes        |No    |
|lambda        |sns           |Event destinations     |sns.Publish                                                 |Yes        |No    |
|lambda        |sqs           |Event source mapping   |                                                            |Yes        |Yes   |
|lambda        |kinesis       |Event source mapping   |                                                            |Yes        |Yes   |
|lambda        |dynamodb      |Event source mapping   |                                                            |Yes        |Yes   |
|lambda        |kafka         |Event source mapping   |                                                            |No         |No    |
|events        |lambda        |Event rule target      |                                                            |Yes        |Yes   |
|sns           |ses           |SNS subscription       |                                                            |Yes        |Yes   |
|sns           |firehose      |SNS subscription       |                                                            |Yes        |Yes   |
|events        |sns           |Event rule target      |                                                            |Yes        |Yes   |
|events        |sqs           |Event rule target      |                                                            |Yes        |Yes   |
|events        |logs          |Event rule target      |                                                            |Yes        |Yes   |
|events        |firehose      |Event rule target      |                                                            |Yes        |Yes   |
|events        |events        |Event rule target      |                                                            |Yes        |Yes   |
|events        |kinesis       |Event rule target      |                                                            |Yes        |Yes   |
|events        |stepfunctions |Event rule target      |                                                            |Yes        |Yes   |
|apigateway    |lambda        |API integration        |                                                            |Yes        |Yes   |
|apigateway    |dynamodb      |API integration        |                                                            |Yes        |Yes   |
|apigateway    |kinesis       |API integration        |                                                            |Yes        |Yes   |
|apigateway    |s3            |API integration        |                                                            |No         |No    |
|apigateway    |sns           |API integration        |                                                            |No         |Yes   |
|apigateway    |sqs           |API integration        |                                                            |Yes        |Yes   |
|apigateway    |stepfunctions |API integration        |                                                            |No         |No    |
|apigateway    |appsync       |API integration        |                                                            |No         |No    |
|cloudformation|*             |Resource Modification  |                                                            |No         |No    |
|lambda        |sts           |Assuming execution role|                                                            |Yes        |Yes   |
|s3            |sqs           |Bucket notification    |                                                            |Yes        |Yes   |
|s3            |sns           |Bucket notification    |                                                            |Yes        |Yes   |

## Supported Policy Types
| Permission Type             | Details                                             |
|-----------------------------|-----------------------------------------------------|
| **Identity Based Permissions** |                                                     |
|                             | - Roles                                             |
|                             | - Users                                             |
| **Resource Based Permissions** |                                                     |
|                             | - Lambda                                            |
|                             | - ECR (Elastic Container Registry)                  |
|                             | - EFS (Elastic File System)                         |
|                             | - SQS (Simple Queue Service)                        |
|                             | - SNS (Simple Notification Service)                 |
|                             | - KMS (Key Management Service)                      |
|                             | - S3 (Simple Storage Service)                       |
|                             | - Backup                                            |
|                             | - Events                                            |
|                             | - Secrets Manager                                   |
|                             | - IAM/STS (Identity and Access Management/Security Token Service) |
| **Permission Boundaries**   |                                                     |
|                             | - Roles                                             |
|                             | - Users                                             |

## Supported Policy Features

| Category       | Description                                                                          |
|----------------|--------------------------------------------------------------------------------------|
| **Version**    | Not evaluated, but only `"2012-10-17"` supported/tested.                             |
| **Id**         | The policy ID is currently ignored.                                                  |
| **Statements** | Supported with the following policy elements:                                        |
| **Effect**     | Fully supported. Allow + Deny                                                        |
| **Sid**        | Currently ignored                                                                    |
| **Action, NotAction** | Supported including placeholder `*`                                            |
| **Principal, NotPrincipal** | Supported principals:                                                     |
|                | - Service                                                                            |
|                | - (Assumed) role (ARN only)                                                          |
|                | - User (ARN only)                                                                    |
|                | Organizations, Federated, CanonicalUsers etc. are currently _not_ supported           |
| **Resource, NotResource** | In general supported, including placeholders `*` and `?`.              |
|                | No support for policy variables                                                      |
| **Condition**  | Supported condition operators:                                                       |
|                | - StringEquals                                                                       |
|                | - StringEqualsIgnoreCase                                                             |
|                | - StringLike                                                                         |
|                | - ArnLike/ArnEquals                                                                  |
|                | Supported condition keys:                                                            |
|                | - aws:SourceArn                                                                      |

## Current Limitations

- CloudFormation stack permissions do not work as expected.
