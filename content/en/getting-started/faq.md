---
title: "Frequently Asked Questions"
linkTitle: "FAQ"
weight: 7
description: >
  This page answers the frequently asked questions about LocalStack Pro, Enterprise, and Community Editions. 
cascade:
  type: docs
---

### How do I check if my API key is valid and activated?

The easiest way to check if LocalStack Pro or Enterprise is activated is to check the health endpoint of LocalStack for a list of the running services:

{{< command >}}
$ curl localhost:4566/health | jq
{{< / command >}}

If a Pro-only [service]({{< ref "aws" >}}) -- like [XRay]({{< ref "XRay-Tracing" >}}) -- is running, LocalStack Pro or Enterprise has started successfully. If your API key is invalid, you will see an error message like this in the logs of LocalStack:

```bash
Activation key "abc..."(10) is invalid or expired! Reason: ...
```

If this error occurs, something is wrong with your API key or license. Make sure your API key is set correctly (check for typos!) and your license is valid. If the API key still does not work, please [contact us](https://localstack.cloud/contact/).
