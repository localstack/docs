---
title: "XRay Tracing"
linkTitle: "XRay Tracing"
categories: ["LocalStack Pro"]
description: >
  Get started with XRay Tracing on LocalStack
aliases:
  - /aws/xray-tracing/
---

LocalStack Pro allows to instrument your applications using [XRay](https://aws.amazon.com/xray/) tracing. This helps in optimizing the interactions between service calls, and facilitates debugging of performance bottlenecks.

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

You can also checkout another of our examples with Xray and Lambda, deployed via the Serverless framework, [`here`](https://github.com/localstack/localstack-pro-samples/tree/master/lambda-xray)

{{< alert >}}
**Note:** To use XRay in Lambdas, please note that you'll need to configure `LAMBDA_XRAY_INIT=1` - this will ensure that the XRay daemon process is fully initialized when spawning Lambda containers (may slightly increase startup times).
{{< /alert >}}
