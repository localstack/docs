---
title: "X-Ray"
linkTitle: "X-Ray"
categories: ["LocalStack Pro"]
description: >
  Get started with X-Ray on LocalStack
aliases:
  - /aws/xray-tracing/
---

## Introduction

AWS X-Ray is a distributed tracing service that helps to understand cross-service interactions and facilitates
debugging of performance bottlenecks.

LocalStack supports X-Ray via the Pro/Team offering, allowing
you to use the X-Ray APIs in your local environment.
The supported APIs are available on our [API Coverage Page](https://docs.localstack.cloud/references/coverage/coverage_xray/),
which provides information on the extent of X-Ray integration with LocalStack.

## Getting started

This guide is designed for users new to X-Ray and assumes basic
knowledge of the AWS CLI and our `awslocal` wrapper script.

// Provide a short tutorial to use the <Service Name> with AWS CLI/`awslocal`

// TODO: describe short tutorial
For example, a Python Lambda function can be instrumented as follows (based on the example [here](https://docs.aws.amazon.com/lambda/latest/dg/python-tracing.html)):

```python
import boto3
from aws_xray_sdk.core import xray_recorder
from aws_xray_sdk.core import patch
patch(['boto3'])
s3_client = boto3.client('s3')

def lambda_handler(event, context):
    s3_client.create_bucket(Bucket='mybucket')
    xray_recorder.begin_subsegment('my_code')
    # your function code goes here...
    xray_recorder.end_subsegment()
```

Running this code in Lambda on LocalStack will result in two trace segments being created in XRay - one from the instrumented `boto3` client when running `create_bucket(..)`, and one for the custom subsegment denoted `'my_code'`. You can use the regular XRay API calls (e.g., [`GetTraceSummaries`](https://docs.aws.amazon.com/xray/latest/api/API_GetTraceSummaries.html), [`BatchGetTraces`](https://docs.aws.amazon.com/xray/latest/api/API_BatchGetTraces.html)) to retrieve the details (timestamps, IDs, etc) of these segments.

## Examples

// share any examples for this <Service Name> across Dev Hub, Pro Samples, etc

// TODO: link to new pro sample
You can also checkout another of our examples with Xray and Lambda, deployed via the Serverless framework, [`here`](https://github.com/localstack/localstack-pro-samples/tree/master/lambda-xray)

## Limitations

LocalStack supports collecting trace segments but currently does not correlate multiple trace segments with the same
`trace_id` into a single aggregated trace.
