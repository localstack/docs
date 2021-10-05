---
title: "Patched AWS SDKs for Lambdas"
categories: ["LocalStack Pro", "Tools"]
weight: 6
description: >
  Using patched SDKs in Lambdas to transparently redirect AWS API calls to LocalStack
---

## Overview
The Lambda runtime in LocalStack uses patched AWS SDKs, which are configured to target the local APIs instead of the real AWS.
This behavior is enabled by default for most Lambda runtimes when using LocalStack Pro.

Assuming you had a Python Lambda handler that attempts to list all S3 buckets. In the past, you had to manually configure the `endpoint_url` parameter on the boto3 client (and potentially use environment switches for dev/prod in your test code):
```
import boto3
def handler(event, context):
    client = boto3.client("s3", endpoint_url="http://localhost:4566")
    print(client.list_buckets())
```

With the patched AWS SDKs, it now becomes possible to deploy your unmodified production code to LocalStack, simply creating a boto3 client with default settings. The invocations of the boto3 client will be automatically forwarded to the local APIs:
```
import boto3
def handler(event, context):
    client = boto3.client("s3")
    print(client.list_buckets())
```

{{< alert >}}
**Note:** This functionality only works when using the SDKs provided by the Lambda execution environment itself.
If you choose to ship your own SDKs with your Lambda or using a layer, it will fallback to the [DNS based transparent execution](../dns-server) if enabled, since those SDK versions will not be patched.
{{< /alert >}}

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

This feature is currently not supported for custom Lambda container images.
