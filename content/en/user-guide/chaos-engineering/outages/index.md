---
title: "Outages"
linkTitle: "Outages"
weight: 2 
description: Mimic service outages and test your infrastructure's ability to recover from unexpected events
tags: ["Enterprise plan"]
---

## Introduction

LocalStack Outages allows you to mimic outages across any AWS region or service.
Intentionally triggering service outages and monitoring the system's response in situations where the infrastructure is compromised offers a powerful way to test.
This strategy helps gauge the effectiveness of the system's deployment procedures and its resilience against infrastructure disruptions, which is a key element of chaos engineering.

{{< alert title="Note">}}
Outages is available as part of the LocalStack Enterprise plan.
If you'd like to try it out, please [contact us](https://www.localstack.cloud/demo) to request access.
{{< /alert >}}

## Prerequisites

The prerequisites for this guide are:

- LocalStack Pro with [LocalStack CLI](https://docs.localstack.cloud/getting-started/installation/#localstack-cli) & [LocalStack Auth Token](https://docs.localstack.cloud/getting-started/auth-token/)
- [Docker](https://docs.docker.com/get-docker/) and [Docker Compose](https://docs.docker.com/compose/install/)
- [Python](https://www.python.org/downloads/)


## Configuration

Outages is configured using a REST API endpoint at `/_localstack/outages`.

Configuration consists of an array of rules.
Each rule specifies the conditions for a network outage to occur and its effects.
Rules are evaluated sequentially.

The schema for the configuration is as follows.

```json
[
    {
        "service": "(str) Name of the service, e.g. 'kinesis'. This is a required field.",
        "region": "(str) Region name, e.g. 'ap-south-1'. If omitted, all regions are affected.",
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

## Examples

To initiate an outage for specific service/region combinations, you can make a POST request as described below:

{{< command >}}
curl --location --request POST 'http://localhost.localstack.cloud:4566/_localstack/outages' \
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

In the above example, S3 is affected in us-east-1 and ap-south-1, and Lambda is affected in all regions.
All calls to these services in these regions will return a 503 Service Unavailable error.


To demonstrate this works as expected, we can try to create an S3 bucket in us-east-1:

{{< command >}}
$ awslocal s3 mb s3://test-bucket --region us-east-1
<disable-copy>
make_bucket failed: s3://test-bucket An error occurred (ServiceUnavailableException) when calling the CreateBucket operation (reached max retries: 4): Service 's3' not accessible due to an outage
</disable-copy>
{{< /command >}}

However, the same operation, when run in eu-central-1 is unaffected:

{{< command >}}
$ awslocal s3 mb s3://test-bucket --region eu-central-1
<disable-copy>
make_bucket: test-bucket
</disable-copy>
{{< /command >}}

Outages can be stopped by setting an empty rule list in the configuration.
The following request will clear the current configuration:

{{< command >}}
curl --location --request POST 'http://localhost.localstack.cloud:4566/_localstack/outages' \
--header 'Content-Type: application/json' \
--data '[]'
{{< /command >}}

To retrieve the current configuration, make the following GET call:

{{< command >}}
curl --location --request GET 'http://localhost.localstack.cloud:4566/_localstack/outages'
{{</ command >}}

To add a new rule to the current configuration, make a PATCH call as follows:

{{< command >}}
curl --location --request PATCH 'http://localhost.localstack.cloud:4566/_localstack/outages' \
--header 'Content-Type: application/json' \
--data '[{"service": "kinesis", "operation": "PutRecord", "probability": 0.3, "error": {"statusCode": 400, "code": "ProvisionedThroughputExceededException"}}]'
{{</ command >}}

This new rule will cause probabilistic failures for Kinesis PutRecord operation.
Here, the returned error is also customised to be HTTP 400 ProvisionedThroughputExceededException.

To remove a rule from the configuration, make a DELETE call as follows:

{{< command >}}
curl --location --request DELETE 'http://localhost.localstack.cloud:4566/_localstack/outages' \
--header 'Content-Type: application/json' \
--data '[{"service": "lambda"}]'
{{</ command >}}

The rule to be removed must be exactly the same as in the existing configuration.
