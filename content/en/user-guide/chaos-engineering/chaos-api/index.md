---
title: "Chaos API"
linkTitle: "Chaos API"
description: Simulate outages and network failures to test the resiliency of your infrastructure
tags: ["Enterprise plan"]
---

## Introduction

LocalStack Chaos API allows you to mimic outages across any AWS region or service.
Intentionally triggering service outages and monitoring the system's response in situations where the infrastructure is compromised offers a powerful way to test.
This strategy helps gauge the effectiveness of the system's deployment procedures and its resilience against infrastructure disruptions, which is a key element of chaos engineering.

You can use LocalStack Chaos API to cause API failures for any combination of the following:

- Service
- Region
- Operation

You can customise the HTTP error code and message that LocalStack responds with.
If required, you can make the failures occur probabilistically.

Furthermore, the Chaos API can also be configured to add a network latency for all calls.

{{< alert title="Note">}}
Chaos API is available as part of the LocalStack Enterprise plan.
If you'd like to try it out, please [contact us](https://www.localstack.cloud/demo) to request access.
{{< /alert >}}

## Prerequisites

The prerequisites for this guide are:

- LocalStack Pro with [LocalStack CLI](https://docs.localstack.cloud/getting-started/installation/#localstack-cli) & [LocalStack Auth Token](https://docs.localstack.cloud/getting-started/auth-token/)
- [Docker](https://docs.docker.com/get-docker/) and [Docker Compose](https://docs.docker.com/compose/install/)
- [Python](https://www.python.org/downloads/)

## Configuration

The disruption types supported by Chaos API are broadly categorised into two groups.
**Service Faults** lead to an application-level HTTP error in an AWS service, and **Network Effects** introduce network-level effects to all connections.

### Service Faults

Service faults can be configured using the endpoint at `/_localstack/chaos/faults`.
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
Currently the Chaos API only supports a latency factor.

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
$ curl --location --request POST 'http://localhost.localstack.cloud:4566/_localstack/chaos/faults' \
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

In this example, S3 is affected in `us-east-1` and `ap-south-1,` and Lambda is affected in all regions.
All calls to these services in these regions will return a 503 Service Unavailable error.

To see this in action, try to create an S3 bucket in `us-east-1`:

{{< command >}}
$ awslocal s3 mb s3://test-bucket --region us-east-1
<disable-copy>
make_bucket failed: s3://test-bucket An error occurred (ServiceUnavailableException) when calling the CreateBucket operation (reached max retries: 4): Service 's3' not accessible due to an outage
</disable-copy>
{{< /command >}}

However, the same operation, when run in `eu-central-1` will work as expected.

{{< command >}}
$ awslocal s3 mb s3://test-bucket --region eu-central-1
<disable-copy>
make_bucket: test-bucket
</disable-copy>
{{< /command >}}

Faults can be disabled by setting an empty rule list in the configuration.
The following request will clear the current configuration:

{{< command >}}
$ curl --location --request POST 'http://localhost.localstack.cloud:4566/_localstack/chaos/faults' \
--header 'Content-Type: application/json' \
--data '[]'
{{< /command >}}

To retrieve the current configuration, make the following GET call:

{{< command >}}
$ curl --location --request GET 'http://localhost.localstack.cloud:4566/_localstack/chaos/faults'
{{</ command >}}

To add a new rule to the current configuration, make a PATCH call as follows:

{{< command >}}
$ curl --location --request PATCH 'http://localhost.localstack.cloud:4566/_localstack/chaos/faults' \
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
$ curl --location --request DELETE 'http://localhost.localstack.cloud:4566/_localstack/chaos/faults' \
--header 'Content-Type: application/json' \
--data '[{"service": "lambda"}]'
{{</ command >}}

The rule to be removed must be exactly the same as in the existing configuration.

## Comparison with Fault Injection Service

AWS [Fault Injection Service (FIS)]({{< ref "fis" >}}) also allows controlled chaos engineering experiments on infrastructure.
While similar in purpose, there are notable differences between FIS and LocalStack Chaos API.

This table highlights those differences, offering a detailed comparison of how each service approaches chaos engineering, their capabilities, and their integration options.

| **Aspect**                        | **AWS Fault Injection Service (FIS)**                                                                                                              | **LocalStack Chaos API**                                                                                                                          |
|-----------------------------------|----------------------------------------------------------------------------------------------------------------------------------------------------|---------------------------------------------------------------------------------------------------------------------------------------------------|
| **Fault Types**                   | • EC2 Stop/Terminate Instances<br>• RDS Reboot Instances<br>• SSM Send Command<br>• Inject API errors (e.g., `aws:fis:inject-api-internal-error` for EC2 only)  | • API failures (HTTP error codes and messages for any service)<br>• Network effects (latency)<br>• Can be probabilistic and customized.          |
| **Procedural vs Declarative**     | • Capable of running procedural experiments where it invokes API actions affecting AWS resources (e.g., `aws:ec2:stop-instances`).                    | • Focuses on declarative effects impacting the AWS API, such as returning errors or adding latency, without invoking AWS resource actions.       |
| **Experiment Execution**          | • Requires creating and running controlled experiments with predefined templates. Systems are restored after disruption duration.                   | • Faults are applied dynamically based on configuration rules. Can inject faults on-the-fly without predefining experiments.                     |
| **Customization**                 | • Limited to predefined actions (e.g., stopping EC2 instances, inducing specific errors like InternalError for EC2).                                | • Highly customizable, including probabilistic failures, custom error codes, HTTP status codes, and errors for any AWS operation.               |
| **Service Coverage**              | • Covers specific AWS services such as EC2, RDS, and SSM.                                                                                           | • Covers all AWS services and operations (e.g., S3, Lambda, Kinesis) with no service-specific restrictions.                                      |
| **Network Effects**               | • Not supported.                                                                                                                                   | • Supports adding network latency to simulate slow network conditions.                                                                            |
| **API Interaction**               | • `create-experiment-template` to create templates<br>• `start-experiment` to begin experiments<br> | • `POST` to `/chaos/faults` to configure faults<br>• `POST` to `/chaos/effects` to introduce network effects.<br> |
| **Probabilistic Failure Injection** | • Not available.                                                                                                                                  | • Supports probabilistic failure injection, introducing partial failures, which mimic intermittent outages.                                       |
| **Broader Fault Injection**       | • Limited to predefined actions (e.g., stop instances, reboot databases, inject errors for specific services).                                      | • Broader fault injection for any AWS operation (e.g., PutObject for S3, Invoke for Lambda).                                                     |
