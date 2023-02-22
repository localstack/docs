---
title: "Amazon MQ"
categories: ["LocalStack Pro"]
description: >
  Get started with Amazon MQ on LocalStack
aliases:
  - /aws/mq/
---

Amazon MQ is a fully managed service for open-source message brokers.
Basic support is included in LocalStack Pro, please refer to the [feature-coverage]({{< ref "feature-coverage" >}}) for more information.

## Getting started
In the following, we outline basic MQ usage. Please also refer to the sample here: [Localstack Pro Samples](https://github.com/localstack/localstack-pro-samples/tree/master/mq-broker).
Assuming you have [`awslocal`]({{< ref "aws-cli" >}}) installed, you can try the following commands:

{{< command >}}
$ awslocal mq create-broker --broker-name test-broker --deployment-mode SINGLE_INSTANCE --engine-type ACTIVEMQ --engine-version='5.16.6' --host-instance-type 'mq.t2.micro' --auto-minor-version-upgrade --publicly-accessible --users='{"ConsoleAccess": true, "Groups": ["testgroup"],"Password": "QXwV*$iUM9USHnVv&!^7s3c@", "Username": "admin"}'
{
    "BrokerArn": "arn:aws:mq:us-east-1:000000000000:broker:test-broker:b-f503abb7-66bc-47fb-b1a9-8d8c51ef6545",
    "BrokerId": "b-f503abb7-66bc-47fb-b1a9-8d8c51ef6545"
}
{{< / command >}}

Using the Describe-Broker endpoint, it is possible to get more detailed information about an instance. The ConsoleURL is especially handy, because it provides the address to the web console (accessible via the user "admin" and password "admin").
{{< command >}}
$ awslocal mq describe-broker --broker-id b-f503abb7-66bc-47fb-b1a9-8d8c51ef6545
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
{{< / command >}}

Since the broker is now actively listening, we can send a message to a sample queue using curl.
{{< command >}}
$ curl -XPOST -d "body=message" http://admin:admin@localhost:4513/api/message\?destination\=queue://orders.input
{{< / command >}}


## Localstack limitations and differences to AWS
Only basic functionality is supported right now, main limitations are the following:
* Only ActiveMQ (version 5.16.6) is supported
* Users are not actively enforced (but needed to make proper calls)
* While it is possible to create configurations, they are not actively enforced in a broker
* Persistence and Cloud Pods are not supported
* Limited API coverage
