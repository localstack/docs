---
title: "SQS"
categories: ["LocalStack Community"]
description: >
  Explaining the different SQS providers and how to configure the service.
---

AWS SQS is a fully managed distributed message queuing service.

SQS is shipped with the LocalStack Community version and is [extensively supported](../feature-coverage/).
Trying to run the examples in the [official AWS developer](https://docs.aws.amazon.com/AWSSimpleQueueService/latest/SQSDeveloperGuide/welcome.html) guide against LocalStack is a great place to start.

Assuming you have [`awslocal`](../../integrations/aws-cli/) installed you can also try the following commands:

```bash
$ awslocal sqs create-queue --queue-name sample-queue
{
    "QueueUrl": "http://localhost:4566/000000000000/sample-queue"
}

$ awslocal sqs list-queues
{
    "QueueUrls": [
        "http://localhost:4566/000000000000/sample-queue"
    ]
}

$ awslocal sqs send-message --queue-url http://localhost:4566/00000000000/sample-queue --message-body test

{
    "MD5OfMessageBody": "098f6bcd4621d373cade4e832627b4f6",
    "MessageId": "74861aab-05f8-0a75-ae20-74d109b7a76e"
}
```

When working with the `SERVICES` environment variable, please make sure to include `sqs` in the list of services.
For instance, to load the DynamoDB, SQS, and Kinesis service you'd pass the variable as `SERVICES=dynamodb,sqs,kinesis`.

LocalStack supports two third-party providers for SQS - namely, [moto](https://github.com/spulec/moto) and [elasticmq](https://github.com/softwaremill/elasticmq). By default, `moto` is used. Your desired provider can be set with the environment variable `SQS_PROVIDER`.\
For instance, if you wish to use `elasticmq` you'd pass the environment variable as `SQS_PROVIDER=elasticmq`. 

ElasticMQ only supports a subset of the SQS query (only the REST query interface). However, it provides better scalability for local development and test servers that wish to create realistic scenarios in which lots of messages are sent with a high throughput.
On the other hand, moto has near-complete support for SQS but has limited scalability. 

{{% alert title="Persistence Support" color="info" %}}
As of now the [LocalStack Pro persistence mechanism](../../understanding-localstack/persistence-mechanism/#persistence-mechanism---pro-version) is only supported for `moto`. 
{{% /alert %}}