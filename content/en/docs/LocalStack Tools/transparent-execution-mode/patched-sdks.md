---
title: "Patched AWS SDKs for Lambdas"
categories: ["LocalStack Pro", "Tools"]
weight: 6
description: >
  Using patched SDKs in Lambdas to redirect AWS API calls to LocalStack
---

## Overview
Lambdas executed within LocalStack use by default patched SDKs, which are configured to use LocalStack instead of the real AWS.
This behavior is on by default when using LocalStack Pro.

This functionality only works when using the SDKs provided by the lambda execution environment itself.
If you choose to ship your own SDKs with your lambda or using a layer, it will fallback to the [DNS based transparent execution](../dns-server) if enabled, since those SDK versions will not be patched.

This feature works by patching the AWS SDKs in the docker images, which provide the execution environment for Lambdas within LocalStack.

The main advantage of this mode is, that no DNS magic is involved, and SSL certificate checks do not have to be disabled.

## Configuration

If you want to disable this behavior, and use the DNS server to resolve the endpoints for AWS, you can disable this behavior using:

```
TRANSPARENT_LOCAL_ENDPOINTS=0 
```

## Supported Runtimes
Currently, LocalStack supports patching the SDKs for the following runtimes:

* Python (using boto3)
* NodeJS
* Ruby
* Java

Also, these patched SDKs are only available in the following [Lambda execution modes](../../../understanding-localstack/lambda-executors):

* docker
* docker-reuse

Custom Lambda Container images are also not supported currently.
