---
title: "Simple Queue Service (SQS)"
categories: ["LocalStack Community"]
description: >
  Explaining the different SQS providers and how to configure the service.
---

AWS SQS is a fully managed distributed message queuing service.
SQS is shipped with the LocalStack Community version and is [extensively supported and tested]({{< ref "feature-coverage" >}}).

## Getting started

Trying to run the examples in the [official AWS developer](https://docs.aws.amazon.com/AWSSimpleQueueService/latest/SQSDeveloperGuide/welcome.html) guide against LocalStack is a great place to start.
Assuming you have [`awslocal`]({{< ref "aws-cli" >}}) installed you can also try the following commands:

{{< command >}}
$ awslocal sqs create-queue --queue-name sample-queue
{
    "QueueUrl": "http://localhost:4566/000000000000/sample-queue"
}
{{< / command >}}

{{< command >}}
$ awslocal sqs list-queues
{
    "QueueUrls": [
        "http://localhost:4566/000000000000/sample-queue"
    ]
}
{{< / command >}}

{{< command >}}
$ awslocal sqs send-message --queue-url http://localhost:4566/00000000000/sample-queue --message-body test
{
    "MD5OfMessageBody": "098f6bcd4621d373cade4e832627b4f6",
    "MessageId": "74861aab-05f8-0a75-ae20-74d109b7a76e"
}
{{< / command >}}


## SQS Query API

The [SQS Query API](https://docs.aws.amazon.com/AWSSimpleQueueService/latest/SQSDeveloperGuide/sqs-making-api-requests.html) exposes SQS Queue URLs as endpoints and allows you to make HTTP requests directly against the Queue.
LocalStack also supports the Query API.


LocalStack makes it easy to test SQS Query API calls without having to sign or add `AUTHPARAMS` to your HTTP requests.
For example, you could send a `SendMessage` command using a `MessageBody` attribute with a simple curl command:
{{< command >}}
$ curl "http://localhost:4566/000000000000/sample-queue?Action=SendMessage&MessageBody=hello%2Fworld"

<?xml version='1.0' encoding='utf-8'?>
<SendMessageResponse xmlns="http://queue.amazonaws.com/doc/2012-11-05/"><SendMessageResult><MD5OfMessageBody>c6be4e95a26409675447367b3e79f663</MD5OfMessageBody><MessageId>466144ab-1d03-4ec5-8d70-97535b2957fb</MessageId></SendMessageResult><ResponseMetadata><RequestId>JU40AF5GORK0WSR75MOY3VNQ1KZ3TAI7S5KAJYGK9C5P4W4XKMGF</RequestId></ResponseMetadata></SendMessageResponse>
{{< / command >}}

{{% alert title="JSON output format" color="info" %}}
When the client sets the `Accept: application/json` header, AWS responds with a JSON response instead of XML.
This is currently not supported by LocalStack.
{{% /alert %}}

{{% alert title="Behavior changes in 0.14.2" color="info" %}}
In previous releases, an empty HTTP request to a queue would return a `<GetQueueUrlResponse>`.
This has since been aligned to the behavior of AWS, which returns a `<UnknownOperationException/>`.
To run a `GetQueueUrl` request, add the `?Action=GetQueueUrl&QueueName=<QueueName>"` query string to the URL.
{{% /alert %}}

## Configuration

### Queue URLs

You can control the format of the generated Queue URLs by setting the environment variable `SQS_ENDPOINT_STRATEGY` when starting LocalStack to one of the following values.

| Value | URL format | Description |
| - | - | - |
| `domain` | `<region>.queue.localhost.localstack.cloud:4566/<account_id>/<queue_name>` | This strategy behaves like the [SQS legacy service endpoints](https://docs.aws.amazon.com/general/latest/gr/sqs-service.html#sqs_region), and uses `localhost.localstack.cloud` to resolve to localhost. When using `us-east-1`, the `<region>.` prefix is omitted. |
| `path` | `localhost:4566/queue/<region>/<account_id>/<queue_name>` | An alternative that can be useful if you cannot resolve LocalStack's localhost domain |
| `off` | `localhost:4566/<account_id>/<queue_name>` | Currently the default for backwards compatibility. Since this format does not encode the region, you cannot query queues that exist in different regions with the same name. |

### Enabling QueueDeletedRecently errors

AWS does not allow creating a queue with the same name for 60 seconds after it was deleted.
See the [DeleteQueue API Reference](https://docs.aws.amazon.com/AWSSimpleQueueService/latest/APIReference/API_DeleteQueue.html).
LocalStack disables this behavior by default, but it can be enabled by starting LocalStack with `SQS_DELAY_RECENTLY_DELETED=1`.


## Deprecated providers

LocalStack has two other third-party providers for SQS that have since been deprecated: [moto](https://github.com/spulec/moto) and [elasticmq](https://github.com/softwaremill/elasticmq). To activate the moto provider, start localstack with `PROVIDER_OVERRIDE_SQS=legacy`. If you want to activate elasticmq, you need to set both `PROVIDER_OVERRIDE_SQS=legacy SQS_PROVIDER=elasticmq`.
The two providers are no longer tested or supported.

{{% alert title="Persistence Support" color="info" %}}
As of now the [LocalStack Pro persistence mechanism]({{< ref "persistence-mechanism#persistence-mechanism---pro-version" >}}) is only supported for the default SQS provider.
{{% /alert %}}


## Known limitations and differences to AWS

* The `ApproximateReceiveCount` attribute of a message will be reset to 0 when the message moves to a DLQ.
