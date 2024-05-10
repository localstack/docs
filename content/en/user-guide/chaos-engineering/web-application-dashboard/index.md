---
title: "Chaos Engineering Dashboard"
linkTitle: "Chaos Engineering Dashboard"
weight: 3
description: Effortlessly design, activate, and manage Fault Injection Service experiments
tags: ["Pro image"]
---

## Introduction

The Chaos Engineering dashboard in LocalStack offers streamlined testing for cloud applications, enabling you to simulate server errors, service outages, regional disruptions, and network latency with ease, ensuring your app is ready for real-world challenges.

You can find this feature in the LocalStack web app by navigating to [app.localstack.cloud/chaos-engineering](https://app.localstack.cloud/chaos-engineering).

## FIS Dashboard

The FIS Dashboard in LocalStack Web Application allows you to conduct Fault Injection Service experiments on infrastructure stacks.
This control panel offers various FIS experiment options, which includes:

-   **500 Internal Error**: This experiment randomly terminates incoming requests, returning an `Internal Server Error` with a response code of 500.
-   **Service Unavailable**: This test causes all calls to specified services to receive a 503 `Service Unavailable` response.
-   **AWS Region Unavailable**: This experiment simulates regional outages and failovers by disabling entire AWS regions.
-   **Latency**: This test introduces specified latency to every API call, useful for simulating network latency or degraded network performance.

{{< figure src="fis-dashboard.png" width="900" >}}

This LocalStack dashboard is not just an easy-to-use testing tool, it's a foundation for building reusable Fault Injection Service templates.
By defining experiments using this interface, you create a set of customizable templates that can be seamlessly integrated into any future automation workflows.
It's a time-saving feature, ensuring consistent and efficient testing across various stages of your application's development lifecycle.
