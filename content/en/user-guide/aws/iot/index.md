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

LocalStack ships an Message Queuing Telemetry Transport (MQTT) broker powered by [Mosquitto](https://mosquitto.org/) which supports both pure MQTT and MQTT-over-WSS (WebSockets Secure) protocols.
To retrieve the MQTT endpoint, use the [`DescribeEndpoint`](https://docs.aws.amazon.com/iot/latest/apireference/API_DescribeEndpoint.html) operation.

{{< command >}}
$ awslocal iot describe-endpoint
{
    "endpointAddress": "000000000000.iot.eu-central-1.localhost.localstack.cloud:4510"
}
{{< / command >}}

{{< callout "tip" >}}
LocalStack lazy-loads services by default.
The MQTT broker may not be automatically available on a fresh launch of LocalStack.
You should make a `DescribeEndpoint` call to ensure the broker is running and identify the port.
{{< /callout >}}

This endpoint can then be used with any MQTT client to publish and subscribe to topics.
In this example, we will use the [Hive MQTT CLI](https://hivemq.github.io/mqtt-cli/docs/installation/).

Run the following command to subscribe to an MQTT topic.

{{< command >}}
$ mqtt subscribe \
        --host 000000000000.iot.eu-central-1.localhost.localstack.cloud \
        --port 4510 \
        --topic climate
{{< /command >}}

In another terminal, publish a message to this topic.

{{< command >}}
$ mqtt publish \
        --host 000000000000.iot.eu-central-1.localhost.localstack.cloud \
        --port 4510 \
        --topic climate \
        -m "temperature=30°C;humidity=60%"
{{< /command >}}

This message will be pushed to all subscribers of this topic, including the one in the first terminal.

## Authentication

LocalStack IoT maintains its own root certificate authority which is regenerated at every run.
The root CA certificate can be retrieved from <http://localhost.localstack.cloud:4566/_aws/iot/LocalStackIoTRootCA.pem>.

{{< callout >}}
AWS provides its root CA certificate at <https://www.amazontrust.com/repository/AmazonRootCA1.pem>.
For more information, see [this](https://docs.aws.amazon.com/iot/latest/developerguide/server-authentication.html#server-authentication-certs).
{{< /callout >}}

When connecting to the endpoints, you will need to provide this root CA certificate for authentication.
This is illustrated below with Python [AWS IoT SDK](https://docs.aws.amazon.com/iot/latest/developerguide/iot-sdks.html), 

```py
import awscrt
import boto3
from awsiot import mqtt_connection_builder

region = 'eu-central-1'
iot_client = boto3.client('iot', region=region)
endpoint = aws_client.iot.describe_endpoint()["endpointAddress"]
endpoint, port = endpoint.split(':')

event_loop_group = io.EventLoopGroup(1)
host_resolver = io.DefaultHostResolver(event_loop_group)
client_bootstrap = io.ClientBootstrap(event_loop_group, host_resolver)

credentials_provider = awscrt.auth.AwsCredentialsProvider.new_default_chain(
    client_bootstrap=client_bootstrap
)

client_id = 'example-client'

# Path to root CA certificate downloaded from `/_aws/iot/LocalStackIoTRootCA.pem`
ca_filepath = '...'

mqtt_over_wss = mqtt_connection_builder.websockets_with_default_aws_signing(
    region=region,
    credentials_provider=credentials_provider,
    client_bootstrap=client_bootstrap,
    client_id=client_id,
    endpoint=endpoint,
    port=port,
    ca_filepath=ca_filepath,
)

mqtt_over_wss.connect().result()
mqtt_over_wss.subscribe(...)
```

If you are using pure MQTT, you also need to set the client-side X509 certificates and Application Layer Protocol Negotiation (ALPN) for a successful mutual TLS (mTLS) authentication.
This is not required for MQTT-over-WSS since it does not use mTLS.

AWS IoT SDKs automatically set the ALPN when the endpoint port is 443.
However, because LocalStack does not use this port, this must be done manually.
For details on how ALPN works with AWS, see [this page](https://docs.aws.amazon.com/iot/latest/developerguide/protocols.html).

The client certificate and key can be retrieved using `CreateKeysAndCertificate` operation.
The certificate is signed by the LocalStack root CA.

```py
result = iot_client.create_keys_and_certificate(setAsActive=True)

# Path to file with saved content `result["certificatePem"]`
cert_file = '...'  

# Path to file with saved content `result["keyPair"]["PrivateKey"]`
priv_key_file = '...'  

tls_ctx_options = awscrt.io.TlsContextOptions.create_client_with_mtls_from_path(
    cert_file, priv_key_file
)
tls_ctx_options.alpn_list = ["x-amzn-mqtt-ca"]

mqtt = mqtt_connection_builder._builder(
    tls_ctx_options,
    cert_filepath=cert_file,
    pri_key_filepath=priv_key_file,
    client_bootstrap=client_bootstrap,
    client_id=client_id,
    endpoint=endpoint,
    port=port,
    ca_filepath=ca_filepath,
)

mqtt.connect().result()
mqtt.subscribe(...)
```


## Lifecycle Events

LocalStack publishes the [lifecycle events](https://docs.aws.amazon.com/iot/latest/developerguide/life-cycle-events.html) to the standard endpoints.

- `$aws/events/presence/connected/clientId`: when a client connects
- `$aws/events/presence/disconnected/clientId`: when a client disconnects
- `$aws/events/subscriptions/subscribed/clientId`: when a client subscribes to a topic
- `$aws/events/subscriptions/unsubscribed/clientId`: when a client unsubscribes from a topic

Currently the `principalIdentifier` and `sessionIdentifier` fields in event payload contain dummy values.

## Registry Events

LocalStack can publish the [registry events](https://docs.aws.amazon.com/iot/latest/developerguide/registry-events.html), if [you enable it](https://docs.aws.amazon.com/iot/latest/developerguide/iot-events.html#iot-events-enable).

{{< command >}}
$ awslocal iot update-event-configurations \
        --event-configurations '{"THING":{"Enabled": true}}'
{{< / command >}}

You can then subscribe or use topic rules on the follow topics:

- `$aws/events/thing/<thingName>/created`: when a new thing is created
- `$aws/events/thing/<thingName>/updated`: when a thing is updated
- `$aws/events/thing/<thingName>/deleted`: when a thing is deleted

## Topic Rules

It is possible to use actions with SQL queries for IoT Topic Rules.

For example, you can use the [`CreateTopicRule`](https://docs.aws.amazon.com/iot/latest/apireference/API_CreateTopicRule.html) operation to define a topic rule with a SQL query `SELECT * FROM 'my/topic' where attr=123` which will execute a trigger whenever a message with attribute `attr=123` is received on the MQTT topic `my/topic`.

Supported triggers include Kinesis, Lambda, SQS, Firehose and DynamoDB v2.


## Device Shadows

LocalStack supports both unnamed (classic) and named device shadows.

You can use AWS CLI and [MQTT topics](https://docs.aws.amazon.com/iot/latest/developerguide/device-shadow-mqtt.html) to get, update or delete device shadow state information.

The endpoint as returned by `DescribeEndpoint` currently does not support the [device shadow REST API](https://docs.aws.amazon.com/iot/latest/developerguide/device-shadow-rest-api.html#API_GetThingShadow)


## Current Limitations

LocalStack MQTT broker does not support multi-account/multi-region namespacing.
Internally, the MQTT messages are not routed to the appropriate account ID/region even though the endpoint URL may suggest otherwise.
All messages will be routed to the `000000000000` account and the `us-east-1` region.
This prevents features such as topic rules from working properly when not using the this account ID or region.
