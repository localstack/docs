---
title: "IoT"
linkTitle: "IoT"
categories: ["LocalStack Pro"]
description: >
  Get started with AWS IoT on LocalStack
aliases:
  - /aws/iot/
---

## Introduction

AWS IoT provides cloud services to manage IoT fleet and integrate them with other AWS services 

LocalStack Pro supports IoT Core, IoT Data, IoT Analytics and related APIs as well as an in-built MQTT broker.
Common operations for creating and updating things, groups, policies, certificates and other entities are implemented with full CloudFormation support.
The supported APIs are available on our [API coverage page](https://docs.localstack.cloud/references/coverage/coverage_iot/).

## Getting Started

This guide is for users that are new to IoT and assumes a basic knowledge of the AWS CLI and LocalStack [`awslocal`](https://github.com/localstack/awscli-local) wrapper.

Start LocalStack using your preferred method.

LocalStack ships an MQTT (Message Queuing Telemetry Transport) broker powered by [Mosquitto](https://mosquitto.org/) which supports both pure MQTT and MQTT-over-WSS (WebSockets Secure) protocols.
To retrieve the MQTT endpoint, use the [`DescribeEndpoint`](https://docs.aws.amazon.com/iot/latest/apireference/API_DescribeEndpoint.html) operation.

{{< command >}}
$ awslocal iot describe-endpoint
{
    "endpointAddress": "localhost.localstack.cloud:4510"
}
{{< / command >}}

{{< alert title="Hint" color="success" >}}
LocalStack lazy-loads services by default.
The MQTT broker may not be automatically available on a fresh launch of LocalStack.
You should make a `DescribeEndpoint` call to ensure the broker is running and identify the port.
{{< /alert >}}

This endpoint can then be used with any MQTT client to publish and subscribe to topics.
In this example, we will use the [Hive MQTT CLI](https://hivemq.github.io/mqtt-cli/docs/installation/).

Run the following command to subscribe to an MQTT topic.

{{< command >}}
$ mqtt subscribe \
        --host localhost.localstack.cloud \
        --port 4510 \
        --topic climate
{{< /command >}}

In another terminal, publish a message to this topic.

{{< command >}}
$ mqtt publish \
        --host localhost.localstack.cloud \
        --port 4511 \
        --topic climate \
        -m "temperature=30°C;humidity=60%"
{{< /command >}}

This message will be pushed to all subscribers of this topic, including the one in the first terminal.

## Using Authentication

LocalStack IoT maintains its own root certificate authority which is refreshed at every run.
The root CA certificate can be retrieved from the internal endpoint `/_aws/iot/LocalStackIoTRootCA.pem`.

When using the AWS IoT SDKs


## Lifecycle Events

LocalStack publishes the [lifecycle events](https://docs.aws.amazon.com/iot/latest/developerguide/life-cycle-events.html) to the standard endpoints.

- `$aws/events/presence/connected/clientId`: when a client connects
- `$aws/events/presence/disconnected/clientId`: when a client disconnects
- `$aws/events/subscriptions/subscribed/clientId`: when a client subscribes to a topic
- `$aws/events/subscriptions/unsubscribed/clientId`: when a client unsubscribes from a topic

Currently the `principalIdentifier` and `sessionIdentifier` fields in event payload contain dummy values.

## Registry Events for Things

LocalStack can publish the [registry events](https://docs.aws.amazon.com/iot/latest/developerguide/registry-events.html), if [you enable it](https://docs.aws.amazon.com/iot/latest/developerguide/iot-events.html#iot-events-enable).

{{< command >}}
$ awslocal iot update-event-configurations --event-configurations '{"THING":{"Enabled": true}}'
{{< / command >}}

You can then subscribe or use topic rules on the follow topics:

- `$aws/events/thing/<thingName>/created`: when a new thing is created
- `$aws/events/thing/<thingName>/updated`: when a thing is updated
- `$aws/events/thing/<thingName>/deleted`: when a thing is deleted

## Topic Rules

It is also possible to use advanced features like SQL queries for IoT topic rules.

For example, you can use the [`CreateTopicRule`](https://docs.aws.amazon.com/iot/latest/apireference/API_CreateTopicRule.html) operation to define a topic rule with a SQL query `SELECT * FROM 'my/topic' where attr=123` which will execute a trigger whenever a message with attribute `attr=123` is received on the MQTT topic `my/topic`.

Supported triggers include Kinesis, Lambda, SQS, Firehose and DynamoDB v2.
