---
title: "IoT"
linkTitle: "IoT"
date: 2021-09-28
weight: 5
categories: ["LocalStack Pro"]
description: >
  IoT
---

Basic support for [IoT](https://aws.amazon.com/iot/) (including IoT Analytics, IoT Data, and related APIs) is provided in the Pro version. The main endpoints for creating and updating entities are currently implemented, as well as the CloudFormation integrations for creating them.

The IoT API ships with a built-in MQTT message broker. In order to get the MQTT endpoint, the `describe-endpoint` API can be used; for example, using [`awslocal`](https://github.com/localstack/awscli-local):
```
$ awslocal iot describe-endpoint
{
    "endpointAddress": "localhost:4520"
}
```

This endpoint can then be used with any MQTT client to send/receive messages (e.g., using the endpoint URL `mqtt://localhost:4520`).

LocalStack Pro also supports advanced features like SQL queries for IoT topic rules. For example, you can use the [`CreateTopicRule` API](https://docs.aws.amazon.com/iot/latest/apireference/API_CreateTopicRule.html) to define a topic rule with a SQL query `SELECT * FROM 'my/topic' where attr=123` which will trigger a Lambda function whenever a message with attribute `attr=123` is received on the MQTT topic `my/topic`.
