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
You may use [cURL](https://curl.se/) or your preferred HTTP client to access these endpoints.

{{< callout "tip" >}}
You can use the Swagger UI below to interact with the API right from your browser.
This may require changing the LocalStack [security settings]({{< ref "configuration#security" >}}) by allowing `https://docs.localstack.cloud` as CORS origin.
{{< /callout >}}

{{< swaggerui src="/openapi.json" >}}
