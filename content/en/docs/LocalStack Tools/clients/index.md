---
title: "Client Libraries"
weight: 50
categories: []
description: >
  Client libraries for interfacing with LocalStack
---

LocalStack client libraries make it easier for your programs to interface with LocalStack.

| Platform | Library | Description |
| -------- | ------- | ----------- |
| Python   | [localstack-python-client](https://github.com/localstack/localstack-python-client) | alternatively, you can also use boto3 and use the `endpoint_url` parameter when creating a connection, as described [here]({{< ref "/docs/Integrations/sdks/python/index.md">}}). |
| .NET     | [localstack-dotnet-client](https://github.com/localstack-dotnet/localstack-dotnet-client) | alternatively, you can also use AWS SDK for .NET and change `ClientConfig` properties when creating a service client. |

If you need a client library for your platform, please let us know on our [discussions page](https://github.com/localstack/localstack/discussions).
