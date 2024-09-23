---
title: Internal Endpoints
weight: 50
tags:
- internal-endpoints
- localstack-endpoints
description: >
  Overview of LocalStack and AWS specific internal endpoints for local development and testing
---

LocalStack provides several internal endpoints for various local AWS services and LocalStack-specific features.
These endpoints are not part of the official AWS API and are available in the `/_localstack` and `/_aws` paths.
You can use [curl](https://curl.se/) or your favourite HTTP REST client to access endpoints.

You can start your LocalStack instance and go to [http://localhost.localstack.cloud:4566/_localstack/swagger](http://localhost.localstack.cloud:4566/_localstack/swagger)
to browse the Swagger UI, visualize and interact with all the API's resources implemented in LocalStack.

### LocalStack endpoints

The API path for the LocalStack internal resources is `/_localstack`.
Several endpoints are available under this path. 
For instance, `/_localstack/health` checks the available and running AWS services in LocalStack while
`/_localstack/diagnose` (enable with the `DEBUG=1` configuration variable), reports extensive and sensitive data from
the LocalStack instance.

{{< callout "tip" >}}
You can use the `/_localstack/health` endpoint to restart or kill the services.
You can use [curl](https://curl.se/) or your HTTP REST client to access the endpoint:
{{< command >}}
$ curl -v --request POST --header "Content-Type: application/json"  --data '{"action":"restart"}' http://localhost:4566/_localstack/health
$ curl -v --request POST --header "Content-Type: application/json"  --data '{"action":"kill"}' http://localhost:4566/_localstack/health
{{< /command >}}
{{< /callout >}}

### AWS endpoints

The API path for the AWS internal resources is `/_aws`.
These endpoints offer LocalStack-specific features in addition to the ones offered by the AWS services. 
For instance, `/aws/sqs/messages` conveniently access all messages withing a SQS queue, without deleting them.
