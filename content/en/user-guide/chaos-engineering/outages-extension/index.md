---
title: "Outages Extension"
linkTitle: "Outages Extension"
weight: 3 
description: Use LocalStack Outages Extension to mimic service outages by testing your infrastructure's ability to deploy robustly and recover from unexpected events.
tags: ["Enterprise plan"]
---

## Introduction

The [LocalStack Outages Extension](https://pypi.org/project/localstack-extension-outages/) allows you to mimic outages across any AWS region or service.
By integrating the Outages Extension using the [LocalStack Extension mechanism](https://docs.localstack.cloud/user-guide/extensions/), you can assess 
your infrastructure's robustness. Intentionally triggering service outages and monitoring the system's response in situations 
where the infrastructure is compromised offers a powerful way to test. This strategy helps gauge the effectiveness of the system's
deployment procedures and its resilience against infrastructure disruptions, which is a key element of chaos engineering.


{{< alert title="Note">}}
Outages Extension is currently available as part of the **LocalStack Enterprise** plan. If you'd like to try it out, please [contact us](https://www.localstack.cloud/demo) to request access.
{{< /alert >}}

### Prerequisites

The general prerequisites for this guide are:

- LocalStack Pro with [LocalStack CLI](https://docs.localstack.cloud/getting-started/installation/#localstack-cli) & [LocalStack Auth Token](https://docs.localstack.cloud/getting-started/auth-token/)
- [Docker](https://docs.docker.com/get-docker/) and [Docker Compose](https://docs.docker.com/compose/install/)
- [Python](https://www.python.org/downloads/)


### Installing the extension

To install the LocalStack Outages Extension, first set up your LocalStack Auth Token in your environment. Once the token is configured, use the command below to install the extension:

{{< command >}}
$ export LOCALSTACK_AUTH_TOKEN=<YOUR_LOCALSTACK_AUTH_TOKEN>
$ localstack extensions install localstack-extension-outages
{{< /command >}}

Alternatively, you can enable automatic installation of the extension by setting the environment variable `EXTENSION_AUTO_INSTALL=localstack-extension-outages` when you start the LocalStack container.

Follow our [Managing Extensions documentation](https://docs.localstack.cloud/user-guide/extensions/managing-extensions/) for more information on how to install & manage extensions.

### Configuration

The extension is set up through an API endpoint, where the setup involves specifying a set of rules that are applied in order. 
Each rule includes two key pieces of information: the service name and its region. You have the option to use the `*` wildcard 
for flexibility in either attribute.

To initiate an outage for specific service/region combinations, you can make a POST request as described below:

{{< command >}}
curl --location --request POST 'http://outages.localhost.localstack.cloud:4566/outages' \
--header 'Content-Type: application/json' \
--data '
[
    {
        "service": "kms",
        "region": "us-east-1"
    },
    {
        "service": "s3",
        "region": "us-*"
    },
    {
        "service": "lambda",
        "region": "*"
    }
]'
{{< /command >}}


Once activated, any API requests to the impacted services and regions will result in an HTTP 503 Service Unavailable error.

In the given example, the services and regions affected include:

- KMS in us-east-1
- S3 in all US regions, including us-east-1, us-east-2, us-west-1, us-west-2, us-gov-east-1, and us-gov-west-1
- Lambda across all regions

To demonstrate this works as expected, we can try to create an S3 bucket in a US-based region:

{{< command >}}
$ awslocal s3 mb s3://test-bucket --region us-east-1
<disable-copy>
make_bucket failed: s3://test-bucket An error occurred (ServiceUnavailableException) when calling the CreateBucket operation (reached max retries: 4): Service 's3' not accessible in 'us-east-1' region due to an outage
</disable-copy>
{{< /command >}}

However, the same command executed for `eu-central-1` is unaffected:

{{< command >}}
$ awslocal s3 mb s3://test-bucket --region eu-central-1
<disable-copy>
make_bucket: test-bucket
</disable-copy>
{{< /command >}}

Outages may be stopped by using empty list in the configuration. The following request will clear the current configuration:

{{< command >}}
curl --location --request POST 'http://outages.localhost.localstack.cloud:4566/outages' \
--header 'Content-Type: application/json' \
--data '[]'
{{< /command >}}

To retrieve the current configuration, make the following GET call:

{{< command >}}
curl --location --request GET 'http://outages.localhost.localstack.cloud:4566/outages'
{{</ command >}}

To add a new service/region rule pair to the configuration, make a PATCH call as follows:

{{< command >}}
curl --location --request PATCH 'http://outages.localhost.localstack.cloud:4566/outages' \
--header 'Content-Type: application/json' \
--data '[{"service": "transcribe", "region": "us-west-1"}]'
{{</ command >}}

To remove a service/region rule pair from the configuration, make a DELETE call as follows:

{{< command >}}
curl --location --request DELETE 'http://outages.localhost.localstack.cloud:4566/outages' \
--header 'Content-Type: application/json' \
--data '[{"service": "transcribe", "region": "us-west-1"}]'
{{</ command >}}
