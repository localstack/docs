---
title: "Transparent Execution Modes"
linkTitle: "Transparent Execution"
weight: 10
description: >
  Transparently redirect your AWS calls to LocalStack
---

There are two different options to transparently use LocalStack Pro instead of real AWS APIs in your application.
In contrast, the community (open source) edition requires the application code to configure each AWS SDK client instance with the target `endpoint URL` to point to the respective ports on `localhost` (see list of default ports [here](https://github.com/localstack/localstack)) or, in the case of Lambdas running in the context of LocalStack, the `endpoint URL` should point to `${LOCALSTACK_HOSTNAME}:${EDGE_PORT}`.