---
title: "Simple Notification Service (SNS)"
linkTitle: "Simple Notification Service (SNS)"
categories: ["LocalStack Community"]
description: Get started with Amazon Simple Notification Service (Amazon SNS)
---

AWS Simple Notification Service (SNS) is a central service used to coordinate the delivery of messages to subscribing endpoints or clients. SNS is a serverless messaging services that can distribute massive number of messages to multiple subscribers, and can be used to send messages to mobile devices, email addresses, and HTTP(s) endpoints.

SNS particularly employs the Publish/Subscribe, an asychronous messaging pattern that decouples services that produce events from services that process events. SNS is available over LocalStack Community and the supported APIs are available over our [configuration page]({{< ref "configuration" >}}).

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