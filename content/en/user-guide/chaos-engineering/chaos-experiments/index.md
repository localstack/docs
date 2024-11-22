---
title: "Chaos Experiments"
linkTitle: "Chaos Experiments"
description: Chaos Experiments allows users to conduct chaos engineering experiments and test system reliability by injecting stress or failure in some part of a system.
tags: ["Enterprise plan"]
aliases:
  - /user-guide/chaos-engineering/web-application-dashboard/
  - /user-guide/chaos-engineering/chaos-application-dashboard/
---

## Introduction

[Chaos Experiments](https://app.localstack.cloud/chaos) in LocalStack offer streamlined testing for cloud applications, enabling you to simulate server errors, service outages, regional disruptions, and network latency with ease, ensuring your app is ready for real-world challenges.

{{< callout "note" >}}
Chaos Experiments is offered as a **preview** feature and under active development.
{{< /callout >}}

Chaos Experiments use the [LocalStack Chaos API]({{< ref "chaos-api" >}}) under the hood to offer a set of customizable templates that can be seamlessly integrated into any automation workflows.

{{< figure src="chaos-experiments.png" width="900" >}}

## Features

Chaos Experiments offer the following features:

* **DynamoDB Error**: Randomly inject `ProvisionedThroughputExceededException` errors into DynamoDB API responses.
* **Kinesis Error**: Randomly inject `ProvisionedThroughputExceededException` errors into Kinesis API responses.
* **500 Internal Error**: Randomly terminate incoming requests, returning an `Internal Server Error` with a response code of 500.
* **Service Unavailable**: Cause a specified percentage of service API calls to receive a 503 `Service Unavailable` response.
* **AWS Region Unavailable**: Simulate regional outages and failovers by disabling entire AWS regions.
* **Latency**: Introduce specified latency to every API call, useful for simulating network latency or degraded network performance.
