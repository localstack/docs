---
title: "Transparent Endpoint Injection"
linkTitle: "Transparent Endpoint Injection"
weight: 10
description: >
  Transparently inject local endpoints into AWS SDKs and redirect your AWS calls to LocalStack
aliases:
  - /tools/local-endpoint-injection/
---

In the community (open source) edition,
the application code needs to configure the `endpoint URL` of each AWS SDK client instance to target LocalStack
using the environment variable `AWS_ENDPOINT_URL` available within Lambda functions in LocalStack.
For example, a Python boto3 client can be configured as follows:

```python
client = boto3.client("lambda", endpoint_url=os.environ['AWS_ENDPOINT_URL'])
```

For [supported AWS SDKs](https://docs.aws.amazon.com/sdkref/latest/guide/feature-ss-endpoints.html#ss-endpoints-sdk-compat) 
(including boto3 since [1.28.0](https://github.com/boto/boto3/blob/develop/CHANGELOG.rst#L892)), this configuration happens automatically without any custom code changes.


In LocalStack Pro,
no application code changes are required to let your application connect to local cloud APIs instead of real AWS because
LocalStack provides an integrated DNS server that resolves AWS API calls to target LocalStack.

More details can be found in the subsection below.
