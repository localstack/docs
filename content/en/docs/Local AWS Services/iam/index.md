---
title: "Identity and Access Management (IAM)"
linkTitle: "Identity and Access Management (IAM)"
date: 2021-09-28
weight: 5
categories: ["LocalStack Pro"]
description: >
  Identity and Access Management (IAM)
---

By default, LocalStack uses not enforce security policies for client requests. The IAM security enforcement feature can be used to test your security policies and create a more realistic environment that more closely resembles real AWS.

**Please note:** The environment configuration `ENFORCE_IAM=1` is required to enable this feature (by default, IAM enforcement is disabled).

Below is a simple example that illustrates the use of IAM policy enforcement. It first attempts to create an S3 bucket with the default user (which fails), then create a user and attempts to create a bucket with that user (which fails again), and then finally attaches a policy to the user to allow `s3:CreateBucket`, which allows the bucket to be created.
```
$ awslocal s3 mb s3://test
make_bucket failed: s3://test An error occurred (AccessDeniedException) when calling the CreateBucket operation: Access to the specified resource is denied
$ awslocal iam create-user --user-name test
...
$ awslocal iam create-access-key --user-name test
...
  "AccessKeyId": "AKIA4HPFP0TZHP3Z5VI6",
  "SecretAccessKey": "mwi/8Zhg8ypkJQmkdBq87UA3MbSa3x0HWnkcC/Ua",
...
$ export AWS_ACCESS_KEY_ID=AKIA4HPFP0TZHP3Z5VI6 AWS_SECRET_ACCESS_KEY=mwi/8Zhg8ypkJQmkdBq87UA3MbSa3x0HWnkcC/Ua
$ awslocal s3 mb s3://test
make_bucket failed: s3://test An error occurred (AccessDeniedException) when calling the CreateBucket operation: Access to the specified resource is denied
$ awslocal iam create-policy --policy-name p1 --policy-document '{"Version":"2012-10-17","Statement":[{"Effect":"Allow","Action":"s3:CreateBucket","Resource":"*"}]}'
...
$ awslocal iam attach-user-policy --user-name test --policy-arn arn:aws:iam::000000000000:policy/p1
$ awslocal s3 mb s3://test
make_bucket: test
```

### Supported APIs

IAM security enforcement is available for the majority of LocalStack APIs - it has been tested, among others, for the following services: ACM, API Gateway, CloudFormation, CloudWatch (metrics/events/logs), DynamoDB, DynamoDB Streams, Elasticsearch Service, EventBus, Kinesis, KMS, Lambda, Redshift, S3 (partial support), SecretsManager, SNS, SQS.
