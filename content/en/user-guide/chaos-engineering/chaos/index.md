---
title: "Chaos Plugin"
linkTitle: "Choas Plugin"
description: Simulate outages and network failures to test the resiliency of your infrastructure
tags: ["Enterprise plan"]
---

## Introduction

LocalStack Chaos plugin allows you to mimic outages across any AWS region or service.
Intentionally triggering service outages and monitoring the system's response in situations where the infrastructure is compromised offers a powerful way to test.
This strategy helps gauge the effectiveness of the system's deployment procedures and its resilience against infrastructure disruptions, which is a key element of chaos engineering.

You can use LocalStack Chaos plugin to cause API failures for following or any combination thereof:
- Service
- Region
- Operation

You can customise the HTTP error code and message that LocalStack responds with.
If required, you can make the failures occur probabilistically.

Furthermore, the Chaos plugin can also be configured to add a network latency for all calls.

{{< alert title="Note">}}
Chaos plugin is available as part of the LocalStack Enterprise plan.
If you'd like to try it out, please [contact us](https://www.localstack.cloud/demo) to request access.
{{< /alert >}}

## Prerequisites

The prerequisites for this guide are:

- LocalStack Pro with [LocalStack CLI](https://docs.localstack.cloud/getting-started/installation/#localstack-cli) & [LocalStack Auth Token](https://docs.localstack.cloud/getting-started/auth-token/)
- [Docker](https://docs.docker.com/get-docker/) and [Docker Compose](https://docs.docker.com/compose/install/)
- [Python](https://www.python.org/downloads/)


## Configuration

The chaos effects supported by Chaos plugin are broadly categorised into two groups.
**Faults** lead to an application-level HTTP error, and **Network Effects** introduce network-level effects to the connections.

### Faults

Faults can be configured using the endpoint at `/_localstack/chaos/faults`.
The configuration schema consists of an array of one or more rules, where each rule specifies the conditions for the fault to occur.
When active, rules are evaluated sequentially on every request to LocalStack until the first match.

The schema for the configuration is as follows.

```json
[
    {
        "region": "(str) Region name, e.g. 'ap-south-1'. If omitted, all regions are affected.",
        "service": "(str) Name of the service, e.g. 'kinesis'. If omitted, all services are affected.",
        "operation": "(str) Name of the operation, e.g. 'PutRecord'. If omitted, all operations are affected.",
        "probability": "(num) Probability of invoking this rule, e.g. 0.5. If omitted, 1 is used.",
        "error": {
            "statusCode": "(int) HTTP status code to use in response, e.g. 503. If omitted, 503 is used.",
            "code": "(str) Descriptive error code used in response. If omitted, 'ServiceUnavailable' is used."
        }
    },
    ...
]
```

The endpoint allows the following operations:
- `GET`: Get current configuration
- `POST`: Add new configuration
- `PATCH`: Add a rule
- `DELETE`: Delete a rule

An empty array `[]` disables the faults entirely, while an empty rule in the array `[{}]` causes all AWS operations to lead to faults.

### Network Effects

Network effects are configured using the endpoint `/_localstack/chaos/effects`.
Currently the Chaos plugin only supports a latency factor.

```json
{
    "latency": "(int) Network latency in milliseconds. By default, 0 is used."
}
```

This endpoint allows the following operations:
- `GET`: Get current configuration
- `POST`: Add new configuration


## Examples

To cause faults, make a POST request as follows:

{{< command >}}
curl --location --request POST 'http://localhost.localstack.cloud:4566/_localstack/chaos/faults' \
--header 'Content-Type: application/json' \
--data '
[
    {
        "service": "s3",
        "region": "us-east-1"
    },
    {
        "service": "s3",
        "region": "ap-south-1"
    },
    {
        "service": "lambda",
    }
]'
{{< /command >}}

In this example, S3 is affected in us-east-1 and ap-south-1, and Lambda is affected in all regions.
All calls to these services in these regions will return a 503 Service Unavailable error.


To see this in action, try to create an S3 bucket in us-east-1:

{{< command >}}
$ awslocal s3 mb s3://test-bucket --region us-east-1
<disable-copy>
make_bucket failed: s3://test-bucket An error occurred (ServiceUnavailableException) when calling the CreateBucket operation (reached max retries: 4): Service 's3' not accessible due to an outage
</disable-copy>
{{< /command >}}

However, the same operation, when run in eu-central-1 will work as expected.

{{< command >}}
$ awslocal s3 mb s3://test-bucket --region eu-central-1
<disable-copy>
make_bucket: test-bucket
</disable-copy>
{{< /command >}}

Faults can be disabled by setting an empty rule list in the configuration.
The following request will clear the current configuration:

{{< command >}}
curl --location --request POST 'http://localhost.localstack.cloud:4566/_localstack/chaos/faults' \
--header 'Content-Type: application/json' \
--data '[]'
{{< /command >}}

To retrieve the current configuration, make the following GET call:

{{< command >}}
curl --location --request GET 'http://localhost.localstack.cloud:4566/_localstack/chaos/faults'
{{</ command >}}

To add a new rule to the current configuration, make a PATCH call as follows:

{{< command >}}
curl --location --request PATCH 'http://localhost.localstack.cloud:4566/_localstack/chaos/faults' \
--header 'Content-Type: application/json' \
--data '
[
    {
        "service": "kinesis",
        "operation": "PutRecord",
        "probability": 0.3,
        "error": {
            "statusCode": 400,
            "code": "ProvisionedThroughputExceededException"
        }
    }
]'
{{</ command >}}

This new rule will cause probabilistic failures for Kinesis PutRecord operation.
Here, the returned error is also customised to be HTTP 400 ProvisionedThroughputExceededException.

To remove a rule from the configuration, make a DELETE call as follows:

{{< command >}}
curl --location --request DELETE 'http://localhost.localstack.cloud:4566/_localstack/chaos/faults' \
--header 'Content-Type: application/json' \
--data '[{"service": "lambda"}]'
{{</ command >}}

The rule to be removed must be exactly the same as in the existing configuration.


## Limitations

Faults do not affect internal cross-service communication.
For example, if you configure faults for Kinesis, its integration with DynamoDB Streams will remain unaffected.
