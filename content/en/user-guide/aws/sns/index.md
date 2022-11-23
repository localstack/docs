---
title: "Simple Notification Service (SNS)"
linkTitle: "Simple Notification Service (SNS)"
categories: ["LocalStack Community"]
description: Get started with Amazon Simple Notification Service (Amazon SNS)
aliases:
  - /aws/sns/
---

AWS Simple Notification Service (SNS) is a central service used to coordinate the delivery of messages to subscribing endpoints or clients. SNS is a serverless messaging services that can distribute massive number of messages to multiple subscribers, and can be used to send messages to mobile devices, email addresses, and HTTP(s) endpoints.

SNS particularly employs the Publish/Subscribe, an asychronous messaging pattern that decouples services that produce events from services that process events. SNS is available over LocalStack Community and the supported APIs are available over our [feature coverage page]({{< ref "feature-coverage" >}}).

## Getting started

In this getting started guide, you'll learn how to make a basic usage of SNS over LocalStack. This guide is intended for users who wish to get more acquainted with SNS, and assumes you have basic knowledge of the AWS CLI (and our `awslocal` wrapper script). To get started, start your LocalStack instance using your preferred method:

1. Create a SNS topic, named `test-topic`, using the `awslocal` wrapper script
   {{< command >}}
   $ awslocal sns create-topic --name test-topic
   {{< /command >}}

2. Set the SNS topic attribute using the SNS topic you created previously:
   {{< command >}}
   $ awslocal sns set-topic-attributes --topic-arn arn:aws:sns:us-east-1:000000000000:test-topic --attribute-name DisplayName --attribute-value MyTopicDisplayName
   {{< /command >}}

3. List all the SNS topics:
   {{< command >}}
   $ awslocal sns list-topics
   {{< /command >}}

4. Get attributes for a single SNS topic:
   {{< command >}}
   $ awslocal sns get-topic-attributes --topic-arn arn:aws:sns:us-east-1:000000000000:test-topic
   {{< /command >}}

5. Publish messages to SNS topic, assuming you have a file named `message.txt` in your current directory:
   {{< command >}}
   $ awslocal sns publish --topic-arn "arn:aws:sns:us-east-1:000000000000:test-topic" --message file://message.txt
   {{< /command >}}

6. Subscribe to the SNS topic:
   {{< command >}}
   $ awslocal sns subscribe --topic-arn arn:aws:sns:us-east-1:000000000000:test-topic --protocol email --notification-endpoint test@gmail.com
   {{< /command >}}

7. Set SNS Subscription attributes, using the `SubscriptionArn` from the previous step:
   {{< command >}}
   $ awslocal sns set-subscription-attributes --subscription-arn arn:aws:sns:us-east-1:000000000000:test-topic:b6f5e924-dbb3-41c9-aa3b-589dbae0cfff --attribute-name RawMessageDelivery --attribute-value true
   {{< /command >}}

8. List all the SNS subscriptions:
   {{< command >}}
   $ awslocal sns list-subscriptions
   {{< /command >}}

9. Unsubscribe from SNS topic:
   {{< command >}}
   $ awslocal sns unsubscribe --subscription-arn arn:aws:sns:us-east-1:000000000000:test-topic:b6f5e924-dbb3-41c9-aa3b-589dbae0cfff
   {{< /command >}}

10. Delete an SNS topic:
   {{< command >}}
   $ awslocal sns delete-topic --topic-arn "arn:aws:sns:us-east-1:000000000000:test-topic"
   {{< /command >}}

## Using LocalStack Pro

LocalStack Pro users can access our [LocalStack App's](https://app.localstack.cloud) web user-interface to work with SNS and other AWS services. It is a convenient way to work with SNS, and allows you to create and manage SNS topics, subscriptions, and messages, in a fashion similar to the AWS console. While using the LocalStack App, ensure you have the LocalStack instance running.

1. Login to the [web user-interface](https://app.localstack.cloud) and select the `SNS` service from the `Resources` drop-down.
2. Click on the `Create Topic` button to create a new SNS topic.
3. Enter the `Name`, `Attribute`, and `Tags` to create the SNS topic and click `Create`.
4. You will be able to see the SNS topic in the `SNS Topics` page. Run the following command locally to test the SNS topic:
   {{< command >}}
   $ awslocal sns list-topics
   {{< /command >}}
5. Use the web user-interface to perform further operations on the SNS topic, such as deleting the topic, visualizing the topic attributes, and creating a new subscription.

## LocalStack Specifics
We provide additional features to help you develop, debug and test your SNS applications. They are exposed as internal endpoints that you can access to have more informations about specific internal data.  

### Accessing published Platform Messages

For testing purposes, LocalStack keeps in memory all messages published to a platform endpoint to allow easy retrieval. Check out the [AWS docs about SNS mobile push notifications](https://docs.aws.amazon.com/sns/latest/dg/sns-mobile-application-as-subscriber.html) to know more about this.

These messages can be accessed in JSON format at `GET /_aws/sns/platform-endpoint-messages`. You can specify query parameters to select and filter specific `accountId`, `region` and `endpointArn`.

__Query parameters__

| Parameter | Required | Description |
| - | - | - |
| `accountId` | No | The AWS account ID from which the messages have been published. If not specified, it will use the default `000000000000` |
| `region` | No | The AWS region from which the messages have been published. If not specified, it will use the default `us-east-1` |
| `endpointArn` | No | The target EndpointArn to which the messages have been published. If specified, the response will contain only messages sent to this target. Otherwise, it will return all endpoints with their messages. |

__Response format and attributes__

| Attribute | Description |
| - | - |
| `platform_endpoint_messages` | Contains endpoints ARN as field names. Each endpoint will have its messages in an Array. |
| `region` | The region of the endpoints and messages. | 

<br>

We will create a platform endpoint in SNS and publish a message to show how to retrieve the message from the internal endpoint. 
{{< command >}}
$ awslocal sns create-platform-application --name app-test --platform APNS --attributes {}
{
    "PlatformApplicationArn": "arn:aws:sns:us-east-1:000000000000:app/APNS/app-test"
}

$ awslocal sns create-platform-endpoint --platform-application-arn "arn:aws:sns:us-east-1:000000000000:app/APNS/app-test" --token my-fake-token
{
    "EndpointArn": "arn:aws:sns:us-east-1:000000000000:endpoint/APNS/app-test/c25f353e-856b-4b02-a725-6bde35e6e944"
}

$ awslocal sns publish --target-arn "arn:aws:sns:us-east-1:000000000000:endpoint/APNS/app-test/c25f353e-856b-4b02-a725-6bde35e6e944" --message '{"APNS_PLATFORM": "{\"aps\": {\"content-available\": 1}}"}' --message-structure json
{
    "MessageId": "ed501a7a-caab-45aa-a941-2fcc64b5c227"
}

$ curl "http://localhost:4566/_aws/sns/platform-endpoint-messages" | jq .
{
  "platform_endpoint_messages": {
    "arn:aws:sns:us-east-1:000000000000:endpoint/APNS/app-test/c25f353e-856b-4b02-a725-6bde35e6e944": [
      {
        "TargetArn": "arn:aws:sns:us-east-1:000000000000:endpoint/APNS/app-test/c25f353e-856b-4b02-a725-6bde35e6e944",
        "Message": "{\"APNS_PLATFORM\": \"{\\\"aps\\\": {\\\"content-available\\\": 1}}\"}",
        "MessageAttributes": null,
        "MessageStructure": "json",
        "Subject": null
      }
    ]
  },
  "region": "us-east-1"
}
{{< /command >}}

You can also reset the saved messages at `DELETE /_aws/sns/platform-endpoint-messages`, with those same filters.

{{< command >}}
$ curl -X "DELETE" "http://localhost:4566/_aws/sns/platform-endpoint-messages"
$ curl "http://localhost:4566/_aws/sns/platform-endpoint-messages" | jq .
{
  "platform_endpoint_messages": {},
  "region": "us-east-1"
}
{{< /command >}}
