---
title: "Local Endpoint Injection"
linkTitle: "Local Endpoint Injection"
weight: 10
description: >
  Transparently inject local endpoints into AWS SDKs and redirect your AWS calls to LocalStack
---

In the community (open source) edition, the application code needs to configure each AWS SDK client instance with the target `endpoint URL` to point to the APIs on `localhost` or, in the case of Lambdas running in the context of LocalStack, the `endpoint URL` should point to `http://${LOCALSTACK_HOSTNAME}:${EDGE_PORT}`.

The Pro version provides two options for transparently making your application logic speak to the local APIs instead of real AWS (without having to change your production code):
1. integrated DNS server
2. patched AWS SDKs

More details can be found in the subsections below.
