---
title: "SQS"
date: 2021-09-27
weight: 5
categories: ["LocalStack Community"]
description: >
  Explaining the different SQS providers and how to configure the service.
---

AWS is a fully managed distributed message queuing service.

SQS is shipped with the LocalStack Community version and is [extensively supported](https://github.com/localstack/localstack/blob/master/doc/feature_coverage.md). Trying to run the examples in the [official AWS developer](https://docs.aws.amazon.com/AWSSimpleQueueService/latest/SQSDeveloperGuide/welcome.html) guide against LocalStack is a great place to start.

Assuming you have `awslocal` installed you can also try out the following commands:

When working with the `SERVICES` environment variable, please make sure to include `sqs` in the list of services. For instance, to load the DynamoDB, SQS and Kinesis service you'd pass the variable as `SERVICES=dynamodb,sqs,kinesis`.

LocalStack supports two third party providers for Kinesis. Namely, [moto](https://github.com/spulec/moto) and [elasticmq](https://github.com/softwaremill/elasticmq). By default `moto` is used. Your desired provider can be set with the environment variable `SQS_PROVIDER`. For instance, if you wish to use `elasticmq` you'd pass the environment variable as `SQS_PROVIDER=elasticmq`. 

ElasticMQ only supports a subset of the SQS query (rest interface). However, it provides better scalability for local development/test servers that wish to create realistic scenarios in which messages are sent in high quantity. On the other hand, moto has a near complete support for SQS but has limited scalability. 

{{< alert >}}
**Note:** As of now the persistence mechanism (ref) is only supported for `moto`. 
{{< /alert >}}