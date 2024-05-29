---
title: "MQ"
linkTitle: "MQ"
description: Get started with MQ on LocalStack
tags: ["Pro image"]
---

## Introduction

MQ is a managed message broker service offered by Amazon Web Services (AWS). It facilitates the exchange of messages between various components of distributed applications, enabling reliable and scalable communication. AWS MQ supports popular messaging protocols like MQTT, AMQP, and STOMP, making it suitable for a wide range of messaging use cases.

LocalStack allows you to use the MQ APIs to implement pub/sub messaging, request/response patterns, or distributed event-driven architectures in your local environment. The supported APIs are available on our [API Coverage Page](https://docs.localstack.cloud/references/coverage/coverage_mq/), which provides information on the extent of MQ integration with LocalStack.

## Getting started

This guide is designed for users new to MQ and assumes basic knowledge of the AWS CLI and our [`awslocal`](https://github.com/localstack/awscli-local)  wrapper script.

Start your LocalStack container using your preferred method. We will demonstrate how to create an MQ broker and send a message to a sample queue.

### Create a broker

You can create a broker using the [`CreateBroker`](https://docs.aws.amazon.com/amazon-mq/latest/api-reference/brokers.html#brokerspost) API. Run the following command to create a broker named `test-broker` with the following configuration:

{{< command >}}
$ awslocal mq create-broker \
    --broker-name test-broker \
    --deployment-mode SINGLE_INSTANCE \
    --engine-type ACTIVEMQ \
    --engine-version='5.16.6' \
    --host-instance-type 'mq.t2.micro' \
    --auto-minor-version-upgrade \
    --publicly-accessible \
    --users='{"ConsoleAccess": true, "Groups": ["testgroup"],"Password": "QXwV*$iUM9USHnVv&!^7s3c@", "Username": "admin"}'
<disable-copy>
{
    "BrokerArn": "arn:aws:mq:us-east-1:000000000000:broker:test-broker:b-f503abb7-66bc-47fb-b1a9-8d8c51ef6545",
    "BrokerId": "b-f503abb7-66bc-47fb-b1a9-8d8c51ef6545"
}
</disable-copy>
{{< / command >}}

### Describe the broker

You can use the [`DescribeBroker`](https://docs.aws.amazon.com/amazon-mq/latest/api-reference/brokers.html#brokersget) API to get more detailed information about the broker. Run the following command to get information about the broker we created above:

{{< command >}}
$ awslocal mq describe-broker --broker-id
<disable-copy> 
b-f503abb7-66bc-47fb-b1a9-8d8c51ef6545
{
    "BrokerArn": "arn:aws:mq:us-east-1:000000000000:broker:test-broker:b-f503abb7-66bc-47fb-b1a9-8d8c51ef6545",
    "BrokerId": "b-f503abb7-66bc-47fb-b1a9-8d8c51ef6545",
    "BrokerInstances": [
        {
            "ConsoleURL": "http://localhost:4513",
            "Endpoints": [
                "stomp://localhost:4515",
                "tcp://localhost:4514"
            ]
        }
    ],
    "BrokerName": "test-broker",
    "BrokerState": "RUNNING",
    "Created": "2022-10-17T07:14:21.065527Z",
    "DeploymentMode": "SINGLE_INSTANCE",
    "EngineType": "ACTIVEMQ",
    "HostInstanceType": "mq.t2.micro",
    "Tags": {}
}
</disable-copy>
{{< / command >}}

### Send a message

Now that the broker is actively listening, we can use curl to send a message to a sample queue. Run the following command to send a message to the `orders.input` queue:

{{< command >}}
$ curl -XPOST -d "body=message" http://admin:admin@localhost:4513/api/message\?destination\=queue://orders.input
{{< / command >}}

## Resource Browser

The LocalStack Web Application provides a Resource Browser for managing MQ brokers. You can access the Resource Browser by opening the LocalStack Web Application in your browser, navigating to the **Resource Browser** section, and then clicking on **MQ** under the **App Integration** section.

<img src="mq-resource-browser.png" alt="MQ Resource Browser" title="MQ Resource Browser" width="900" />
<br>
<br>

The Resource Browser allows you to perform the following actions:

- **Create Broker**: Create a new MQ broker by clicking on the **Create Broker** button and providing the required parameters.
- **View Broker**: View details of an existing MQ broker by clicking on the broker name.
- **Delete Broker**: Select the broker name and click on the **Actions** button followed by **Remove Selected** button.

## Examples

The following code snippets and sample applications provide practical examples of how to use MQ in LocalStack for various use cases:

- [Demo application illustrating the use of MQ with LocalStack](https://github.com/localstack/localstack-pro-samples/tree/master/mq-broker)

## Current Limitations

Currently, our MQ emulation offers only fundamental capabilities, and it comes with certain limitations:

- **ActiveMQ Version Limitation:** Presently, only ActiveMQ version 5.16.6 is supported. RabbitMQ is not supported at this time.
- **IAM User Management:** IAM Users are not actively enforced, although they are necessary for making correct calls within the system.
- **Configuration Enforcement:** While it is feasible to create configurations, they are not actively enforced within the broker. 
- **Persistence and Cloud Pods:** LocalStack does not provide support for Persistence and Cloud Pods at this time.
- **API Coverage:** Please note that there is limited API coverage available as part of the current emulation capabilities.
