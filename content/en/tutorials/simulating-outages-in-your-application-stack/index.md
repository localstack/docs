---
title: "Chaos Engineering: Simulating outages in your application stack"
linkTitle: "Chaos Engineering: Simulating outages in your application stack"
weight: 10
description: >
  Utilize the LocalStack Outages Extension to simulate service disruptions and assess how well your infrastructure can deploy and recover from unexpected situations. This tool helps you test the resilience of your system by creating controlled outage scenarios, allowing you to identify and improve upon weaknesses.
type: tutorials
teaser: ""
services:
- ecs
- ec2
- agw
- ddb
platform:
- Javascript
deployment:
- terraform
tags:
- BASH
- API Gateway
- DynamoDB
- ECS
pro: true
leadimage: "outages.png"
---

> TODO

## Introduction

[LocalStack Outages Extension](https://pypi.org/project/localstack-extension-outages/) can simulate outages for any AWS region or service. You can install and use the Outages Extension through [LocalStack Extension mechanism](https://docs.localstack.cloud/user-guide/extensions/) to test infrastructure resilience by intentionally causing service outages and observing the system's recovery in scenarios with incomplete infrastructure is an effective approach. This method evaluates the system's deployment mechanisms and its ability to handle and recover from infrastructure anomalies, a critical aspect of chaos engineering.

{{< callout "note">}}
Outages Extension is currently available as part of the **LocalStack Enterprise** plan. If you'd like to try it out, please [contact us](https://www.localstack.cloud/demo) to request access.
{{< /callout >}}

## Getting started

This guide is designed for users who are new to Outages Extension. We'll simulate partial outages by interrupting specific services, such as halting an ECS instance creation or disrupting a database service. By closely watching Terraform's responses and the status of AWS resources, you'll learn how Terraform manages these disruptions.

For this particular example, we'll be using a Terraform configuration file from a [sample application repository](https://github.com/localstack-samples/samples-chaos-engineering/tree/main/extension-outages). Clone the repository, and follow the instructions below to get started.

### Prerequisites

The general prerequisites for this guide are:

- LocalStack Pro with [LocalStack CLI](https://docs.localstack.cloud/getting-started/installation/#localstack-cli) & [LocalStack Auth Token](https://docs.localstack.cloud/getting-started/auth-token/)
- [AWS CLI](https://docs.localstack.cloud/user-guide/integrations/aws-cli/) with the [`awslocal` wrapper](https://docs.localstack.cloud/user-guide/integrations/aws-cli/#localstack-aws-cli-awslocal)
- [Docker](https://docs.docker.com/get-docker/) and [Docker Compose](https://docs.docker.com/compose/install/)
- [Terraform](https://www.terraform.io/downloads.html) and [`tflocal` wrapper](https://docs.localstack.cloud/user-guide/integrations/terraform/#tflocal-wrapper-script).

Start LocalStack by using the `docker-compose.yml` file from the repository. Ensure to set your Auth Token as an environment variable during this process.

{{< command >}}
$ LOCALSTACK_AUTH_TOKEN=<YOUR_LOCALSTACK_AUTH_TOKEN>
$ docker compose up
{{< /command >}}

### Installing the extension

To install the LocalStack Outages Extension, first set up your LocalStack Auth Token in your environment. Once the token is configured, use the command below to install the extension:

{{< command >}}
$ localstack extensions install localstack-extension-outages
{{< /command >}}

Alternatively, you can enable automatic installation of the extension by setting the environment variable `EXTENSION_AUTO_INSTALL=localstack-extension-outages` when you start the LocalStack container. This can be done by including it in your `docker` command line interface (CLI) or in your `docker-compose` configuration as an environment variable.

Follow our [Managing Extensions documentation](https://docs.localstack.cloud/user-guide/extensions/managing-extensions/) for more information on how to install & manage extensions.

### Running Terraform

To get started, initialize & apply the Terraform configuration using the `tflocal` CLI to create the local resources. The Terraform configuration file operates independently of the application, meaning the application won't be available during this phase. To deploy the entire stack, including the application, refer to the [sample repository](https://github.com/localstack-samples/sample-terraform-ecs-apigateway).

{{< command >}}
$ tflocal init
$ tflocal plan
$ tflocal apply
{{< /command >}}

The following output would be retrieved:

```bash
Apply complete! Resources: 57 added, 0 changed, 0 destroyed.

Outputs:

api_id = "3eed6d1d"
api_invoke_url = "https://3eed6d1d.execute-api.us-east-1.amazonaws.com"
api_invoke_url_foodstore_foods = "https://3eed6d1d.execute-api.us-east-1.amazonaws.com/foodstore/foods/{foodId}"
api_invoke_url_petstore_pets = "https://3eed6d1d.execute-api.us-east-1.amazonaws.com/petstore/domestic/pets/{petId}"
api_test_page = <sensitive>
container_security_group = "sg-db749514a062de41c"
ecs_cluster_name = "arn:aws:ecs:us-east-1:000000000000:cluster/ecs-cluster"
private_dns_namespace = "60bfac90"
vpc_id = "vpc-f9d6b124"
```

Next, you can update certain resources. This includes increasing the number of tasks in the `task_definition` for the ECS service from 3 to 5 and upgrading the `openapi` specification version used by API Gateway from 3.0.1 to 3.1.0.

### Simulating outages

After running the Terraform `plan` command to preview these changes, you can simulate an outage affecting the ECS and API Gateway V2 services before applying the changes. To do this, execute the following command:

{{< command >}}
$ curl --location --request POST 'http://outages.localhost.localstack.cloud:4566/outages' \
--header 'Content-Type: application/json' \
--data-raw '[
    {
        "service": "ecs",
        "region": "us-east-1"
    },
    {
        "service": "apigatewayv2",
        "region": "us-east-1"
    }
]'
{{< /command >}}

In the LocalStack logs, you'll notice that during the periods between successful calls, the controlled outages are marked by a `ServiceUnavailableException` accompanied by a 503 HTTP status code. These exceptions specifically affect the targeted AWS APIs.

```bash
2023-11-09T21:53:31.801  INFO --- [   asgi_gw_9] localstack.request.aws     : AWS ec2.GetTransitGatewayRouteTableAssociations => 200
2023-11-09T21:53:31.824  INFO --- [   asgi_gw_2] localstack.request.aws     : AWS apigatewayv2.GetVpcLink => 503 (ServiceUnavailableException)
2023-11-09T21:53:31.828  INFO --- [   asgi_gw_6] localstack.request.aws     : AWS servicediscovery.ListTagsForResource => 200
2023-11-09T21:53:31.831  INFO --- [   asgi_gw_8] localstack.request.aws     : AWS ec2.DescribeRouteTables => 200
2023-11-09T21:53:31.834  INFO --- [   asgi_gw_7] localstack.request.aws     : AWS servicediscovery.ListTagsForResource => 200
2023-11-09T21:53:31.836  INFO --- [   asgi_gw_0] localstack.request.aws     : AWS ec2.DescribePrefixLists => 200
2023-11-09T21:53:31.842  INFO --- [   asgi_gw_1] localstack.request.aws     : AWS ec2.DescribeSecurityGroups => 200
2023-11-09T21:53:31.848  INFO --- [   asgi_gw_6] localstack.request.aws     : AWS ec2.GetTransitGatewayRouteTablePropagations => 200
2023-11-09T21:53:31.876  INFO --- [   asgi_gw_9] localstack.request.aws     : AWS ec2.DescribeRouteTables => 200
2023-11-09T21:53:31.879  INFO --- [   asgi_gw_5] localstack.request.aws     : AWS ec2.DescribeRouteTables => 200
2023-11-09T21:53:32.205  INFO --- [   asgi_gw_8] localstack.request.aws     : AWS ecs.DescribeClusters => 503 (ServiceUnavailableException)
2023-11-09T21:53:32.280  INFO --- [   asgi_gw_3] localstack.request.aws     : AWS ecs.DescribeTaskDefinition => 503 (ServiceUnavailableException)
2023-11-09T21:53:32.443  INFO --- [   asgi_gw_0] localstack.request.aws     : AWS ecs.DescribeTaskDefinition => 503 (ServiceUnavailableException)
2023-11-09T21:53:32.584  INFO --- [   asgi_gw_6] localstack.request.aws     : AWS apigatewayv2.GetVpcLink => 503 (ServiceUnavailableException)
2023-11-09T21:53:33.271  INFO --- [   asgi_gw_9] localstack.request.aws     : AWS ecs.DescribeClusters => 503 (ServiceUnavailableException)
2023-11-09T21:53:33.473  INFO --- [   asgi_gw_2] localstack.request.aws     : AWS ecs.DescribeTaskDefinition => 503 (ServiceUnavailableException)
2023-11-09T21:53:33.889  INFO --- [   asgi_gw_7] localstack.request.aws     : AWS ecs.DescribeTaskDefinition => 503 (ServiceUnavailableException)
```

During infrastructure provisioning, depending on the tool and provider used, attempts may be made to reapply changes to resources following a failure, or the action might simply fail.

### Simulating shutdowns

To simulate the shutdown of an entire region, execute the following command:

{{< command >}}
$ curl --location --request POST 'http://outages.localhost.localstack.cloud:4566/outages' \
--header 'Content-Type: application/json' \
--data-raw '[
    {
        "service": "*",
        "region": "us-east-1"
    }
]'
{{< /command >}}

### Other operations

To stop outages, submit an empty list in the configuration using the following `POST` request:

{{< command >}}
$ curl --location --request POST 'http://outages.localhost.localstack.cloud:4566/outages' \
--header 'Content-Type: application/json' \
--data-raw '[]'
{{< /command >}}

To view the current configuration, use this `GET` request:

{{< command >}}
$ curl --location --request GET 'http://outages.localhost.localstack.cloud:4566/outages'
{{< /command >}}

To add a new service/region rule to the configuration, use a `PATCH` request as shown below:

{{< command >}}
$ curl --location --request PATCH 'http://outages.localhost.localstack.cloud:4566/outages' \
--header 'Content-Type: application/json' \
--data-raw '[{"service": "transcribe", "region": "us-west-1"}]'
{{< /command >}}

To remove a service/region rule from the configuration, execute a `DELETE` request as follows:

{{< command >}}
$ curl --location --request DELETE 'http://outages.localhost.localstack.cloud:4566/outages' \
--header 'Content-Type: application/json' \
--data-raw '[{"service": "transcribe", "region": "us-west-1"}]'
{{< /command >}}

### Conclusion

By closely watching Terraform's responses and the status of cloud resources, you'll learn how Terraform manages these disruptions. It's important to note how it attempts to retry operations, whether it rolls back changes or faces partial failures, and how it logs these incidents.

This is crucial for understanding the resilience of your infrastructure provisioning against challenging conditions. It also aids in enhancing your IaC configurations, ensuring they are more robust and effective in handling faults and errors in real-life situations.
