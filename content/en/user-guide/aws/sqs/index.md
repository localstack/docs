---
title: "Simple Queue Service (SQS)"
categories: ["LocalStack Community"]
description: >
  Get started with Amazon Simple Queue Service (SQS) on LocalStack
aliases:
  - /aws/sqs/
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

Adding the `Accept: application/json` header will make the server return JSON:

{{< command >}}
curl -H "Accept: application/json" "http://localhost:4566/000000000000/my-queue?Action=SendMessage&MessageBody=hello%2Fworld" 
{"SendMessageResponse": {"SendMessageResult": {"MD5OfMessageBody": "c6be4e95a26409675447367b3e79f663", "MessageId": "748297f2-4abd-4ec2-afc0-4d1a497fe604"}, "ResponseMetadata": {"RequestId": "XEA5L5AX16RTPET25U3TIRIASN6KNIT820WIT3EY7RCH7164W68T"}}}
{{< / command >}}


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

AWS only allows one call to `PurgeQueue` every 60 seconds.
See the [DeleteQueue API Reference](https://docs.aws.amazon.com/AWSSimpleQueueService/latest/APIReference/API_PurgeQueue.html).
LocalStack disables this behavior by default, but it can be enabled by starting LocalStack with `SQS_DELAY_PURGE_RETRY=1`.

### Enabling QueueDeletedRecently errors

AWS does not allow creating a queue with the same name for 60 seconds after it was deleted.
See the [DeleteQueue API Reference](https://docs.aws.amazon.com/AWSSimpleQueueService/latest/APIReference/API_DeleteQueue.html).
LocalStack disables this behavior by default, but it can be enabled by starting LocalStack with `SQS_DELAY_RECENTLY_DELETED=1`.

## Developer endpoints

Our SQS implementation provides additional endpoints for developers under `/_aws/sqs`, that allow you to inspect queues without side effects.
For instance, sometimes you want to peek into queues without actually performing a `ReceiveMessage` operation.

### Peeking into queues

The endpoint `/_aws/sqs/messages` allows you to access all messages within a queue without triggering the visibility timeout our modifying access metrics.
This can be used, for example, in tests to wait until a particular message has arrived in the queue.
The endpoint is fully compatible with the `ReceiveMessage` operation from the SQS API.
The endpoint returns all messages in the queue, and all attributes and system attributes by default.
It ignores any other parameters from the `ReceiveMessage` operation, except the `QueueUrl`.

Here are some examples of how to call the endpoint.
You can either call the endpoint with the query argument `QueueUrl`, or use the path-based endpoint.
These two calls would be equivalent:

* `http://localhost:4566/_aws/sqs/messages?QueueUrl=http://queue.localhost.localstack.cloud:4566/000000000000/my-queue`
* `http://localhost:4566/_aws/sqs/messages/us-east-1/000000000000/my-queue`

#### XML response
You can call the endpoint directly to return the raw AWS XML response.

{{< tabpane >}}
{{< tab header="cURL" lang="bash" >}}
curl "http://localhost:4566/_aws/sqs/messages?QueueUrl=http://queue.localhost.localstack.cloud:4566/000000000000/my-queue"
{{< /tab >}}
{{< tab header="Python Requests" lang="python" >}}
import requests

response = requests.get(
    url="http://localhost:4566/_aws/sqs/messages",
    params={"QueueUrl": "http://queue.localhost.localstack.cloud:4566/000000000000/my-queue"},
)
print(response.text)  # outputs the response XML
{{< /tab >}}
{{< / tabpane >}}

Example output:
```xml
<?xml version='1.0' encoding='utf-8'?>
<ReceiveMessageResponse xmlns="http://queue.amazonaws.com/doc/2012-11-05/">
    <ReceiveMessageResult>
        <Message>
            <MessageId>6a736e5d-4997-4895-8c96-b65a2d7dd600</MessageId>
            <MD5OfBody>5d41402abc4b2a76b9719d911017c592</MD5OfBody>
            <Body>hello</Body>
            <Attribute>
                <Name>SenderId</Name>
                <Value>000000000000</Value>
            </Attribute>
            <Attribute>
                <Name>SentTimestamp</Name>
                <Value>1672853965675</Value>
            </Attribute>
            <Attribute>
                <Name>ApproximateReceiveCount</Name>
                <Value>0</Value>
            </Attribute>
            <Attribute>
                <Name>ApproximateFirstReceiveTimestamp</Name>
                <Value>1672855121076</Value>
            </Attribute>
            <ReceiptHandle>SQS/BACKDOOR/ACCESS</ReceiptHandle>
        </Message>
        <Message>
            <MessageId>173c5aee-503a-4249-90be-159e0d427b48</MessageId>
            <MD5OfBody>7d793037a0760186574b0282f2f435e7</MD5OfBody>
            <Body>world</Body>
            <Attribute>
                <Name>SenderId</Name>
                <Value>000000000000</Value>
            </Attribute>
            <Attribute>
                <Name>SentTimestamp</Name>
                <Value>1672853968176</Value>
            </Attribute>
            <Attribute>
                <Name>ApproximateReceiveCount</Name>
                <Value>0</Value>
            </Attribute>
            <Attribute>
                <Name>ApproximateFirstReceiveTimestamp</Name>
                <Value>1672855121076</Value>
            </Attribute>
            <ReceiptHandle>SQS/BACKDOOR/ACCESS</ReceiptHandle>
        </Message>
    </ReceiveMessageResult>
    <ResponseMetadata>
        <RequestId>KR3H1IN3JQ4LO1592IMGK2JLH8HW3J0Y4LRY1TVW2SAFGZFVXJGI</RequestId>
    </ResponseMetadata>
</ReceiveMessageResponse>
```

#### JSON response

If you prefer a JSON response, you can add the `Accept: application/json` header.
{{< tabpane >}}
{{< tab header="cURL" lang="bash" >}}
curl -H "Accept: application/json" \
    "http://localhost:4566/_aws/sqs/messages?QueueUrl=http://queue.localhost.localstack.cloud:4566/000000000000/my-queue"
{{< /tab >}}
{{< tab header="Python Requests" lang="python" >}}
import requests

response = requests.get(
    url="http://localhost:4566/_aws/sqs/messages",
    params={"QueueUrl": "http://queue.localhost.localstack.cloud:4566/000000000000/my-queue"},
)
print(response.text)  # outputs the response XML
{{< /tab >}}
{{< / tabpane >}}

The output JSON will look something like this:

```json
{
  "ReceiveMessageResponse": {
    "ReceiveMessageResult": {
      "Message": [
        {
          "MessageId": "6a736e5d-4997-4895-8c96-b65a2d7dd600",
          "MD5OfBody": "5d41402abc4b2a76b9719d911017c592",
          "Body": "hello",
          "Attribute": [
            {
              "Name": "SenderId",
              "Value": "000000000000"
            },
            {
              "Name": "SentTimestamp",
              "Value": "1672853965675"
            },
            {
              "Name": "ApproximateReceiveCount",
              "Value": "0"
            },
            {
              "Name": "ApproximateFirstReceiveTimestamp",
              "Value": "1672855535794"
            }
          ],
          "ReceiptHandle": "SQS/BACKDOOR/ACCESS"
        },
        {
          "MessageId": "173c5aee-503a-4249-90be-159e0d427b48",
          "MD5OfBody": "7d793037a0760186574b0282f2f435e7",
          "Body": "world",
          "Attribute": [
            {
              "Name": "SenderId",
              "Value": "000000000000"
            },
            {
              "Name": "SentTimestamp",
              "Value": "1672853968176"
            },
            {
              "Name": "ApproximateReceiveCount",
              "Value": "0"
            },
            {
              "Name": "ApproximateFirstReceiveTimestamp",
              "Value": "1672855535794"
            }
          ],
          "ReceiptHandle": "SQS/BACKDOOR/ACCESS"
        }
      ]
    },
    "ResponseMetadata": {
      "RequestId": "TF87187MUBXJHA39J4Y6OVQG57J51OEEMX62UWYBUQJKC8YVID3P"
    }
  }
}
```

#### Using an AWS client

Since the endpoint is compatible with the SQS `ReceiveMessage` operation, you can use the endpoint as endpoint URL parameter in your AWS client call.

{{< tabpane >}}
{{< tab header="aws-cli" lang="bash" >}}
aws --endpoint-url=http://localhost:4566/_aws/sqs/messages sqs receive-message \
  --queue-url=http://queue.localhost.localstack.cloud:4566/000000000000/my-queue
{{< /tab >}}
{{< tab header="Boto3" lang="python" >}}
import boto3
sqs = boto3.client("sqs", endpoint_url="http://localhost:4566/_aws/sqs/messages")
response = sqs.receive_message(QueueUrl="http://queue.localhost.localstack.cloud:4566/000000000000/my-queue")
print(response)
{{< /tab >}}
{{< / tabpane >}}

Example output:
```json
{
    "Messages": [
        {
            "MessageId": "6a736e5d-4997-4895-8c96-b65a2d7dd600",
            "ReceiptHandle": "SQS/BACKDOOR/ACCESS",
            "MD5OfBody": "5d41402abc4b2a76b9719d911017c592",
            "Body": "hello",
            "Attributes": {
                "SenderId": "000000000000",
                "SentTimestamp": "1672853965675",
                "ApproximateReceiveCount": "0",
                "ApproximateFirstReceiveTimestamp": "1672854900237"
            }
        },
        {
            "MessageId": "173c5aee-503a-4249-90be-159e0d427b48",
            "ReceiptHandle": "SQS/BACKDOOR/ACCESS",
            "MD5OfBody": "7d793037a0760186574b0282f2f435e7",
            "Body": "world",
            "Attributes": {
                "SenderId": "000000000000",
                "SentTimestamp": "1672853968176",
                "ApproximateReceiveCount": "0",
                "ApproximateFirstReceiveTimestamp": "1672854900237"
            }
        }
    ]
}
```

## Known limitations and differences to AWS

* The `ApproximateReceiveCount` attribute of a message will be reset to 0 when the message moves to a DLQ.
