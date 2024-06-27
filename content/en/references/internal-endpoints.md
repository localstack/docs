---
title: Internal Endpoints
weight: 50
type: swagger
tags:
- internal-endpoints
- localstack-endpoints
description: LocalStack REST API for internal and AWS-complementary features
---

LocalStack provides a REST API for internal features such as init hooks, dynamic configuration, diagnostics, etc. and features that complement the AWS services.
These endpoints are available in the `/_localstack` and `/_aws` root paths respectively.
You may use [`cURL`](https://curl.se/) or your preferred HTTP client to access endpoints.

{{< swaggerui src="/openapi.json" >}}
