---
title: "Outages Extension"
linkTitle: "Outages Extension"
weight: 1 
description: Simulating service outages to evaluate the resilience of infrastructure provisioning is a core practice of chaos engineering, testing the system's deployment robustness and recovery from anomalies.
---

## Introduction

Causing outages to certain services and observing the system's recovery process when incomplete infrastructure is provided
is generally a good approach to test infrastructure provisioning resilience. This tests the system's deployment mechanisms and its
ability to cope with and recover from infrastructure anomalies, which is a crucial aspect of chaos engineering aimed at
verifying the reliability of infrastructure as code (IaC) and automated provisioning processes.

## Getting started

In this example we will be using a popular IaC tool, Terraform, to define our desired infrastructure in a declarative manner.
To follow along, please refer to this use-case dedicated [repository](https://github.com/localstack-samples/samples-chaos-engineering/tree/main/extension-outages).

To get started with observing Terraform's behavior during partial outages, you would begin by writing a basic Terraform 
configuration file that defines the required cloud resources, such as virtual machines, networks, or databases on AWS. 
Of course, you can structure your configuration with variables and modules to keep it maintainable and readable. 

The configuration file used in this example belongs to a sample application repository, but for the sake of focusing strictly
on infrastructure, we will use it in a stand-alone approach.

Once your configuration is ready, apply it to initiate the provisioning process. During this process, we intentionally cause 
outages to specific services, for example, by stopping an ECS instance creation or disrupting a database service. By monitoring
the Terraform output and the state of AWS resources, you can observe how Terraform handles these interruptions—whether it 
retries operations, rolls back changes, or fails partially—and how it logs such events. 

This exercise provides valuable insights into the resilience of your infrastructure provisioning under adverse conditions 
and helps you refine your Terraform scripts for better fault tolerance and error handling in real-world scenarios.

## Installing the extension

In order to use the Outages Extension, a Pro license is necessary. There are two ways you can employ the actions of this extension:
- By using the configuration flag `EXTENSION_AUTO_INSTALL=localstack-extension-outages` at the container startup. You can use this 
 by including it in your docker run (or docker-compose file) as an environment variable.

- By explicitly installing the extension:

Before installing the extension, make sure you're logged into LocalStack. If not, log in using the following command:

```bash
$ localstack login
```

Initialize the extensions' folder:

```bash
$ localstack extensions init
```

You can then install the extension using the command:

```bash
$ localstack extensions install localstack-extension-outages
```

## Running Terraform

First we run out first iteration of our infrastructure and make sure everything works. The Terraform configuration file
can be run independently of the application, but that means the application will not be available. To fully run the whole stack
you can refer to the sample [repository](https://github.com/localstack-samples/sample-terraform-ecs-apigateway).

```bash
$ tflocal init
$ tflocal plan
$ tflocal apply
```

{{< figure src="outages-1.png" >}}

Now let's apply some new changes to some of the resources, by increasing the number of tasks from the specified `task_definition`
that we want the ECS service to run and maintain, from 3 to 5. Let's say we also want to upgrade the `openapi` specification version that
API Gateway uses, from 3.0.1 to 3.1.0.
We run the Terraform `plan` command, but before `apply` an outage affecting the ECS and API Gateway V2 services occurs. To simulate this
we run the following command:

```bash
curl --location --request POST 'http://outages.localhost.localstack.cloud:4566/outages' \
                                                             --header 'Content-Type: application/json' \
                                                             --data '
                                                         [
                                                         {
                                                         "service": "ecs",
                                                         "region": "us-east-1"
                                                         },
                                                         {
                                                         "service": "apigatewayv2",
                                                         "region": "us-east-1"
                                                         }
                                                         ]'
```

We can observe the LocalStack logs to see that between the successful calls, the controlled outages appear with a `ServiceUnavailableException` with
a 503 HTTP status code, affecting the specified AWS APIs.

```
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

Now, depending on each infrastructure provisioning tool and provider, there will be retries to apply the changes to these resources, or
the action would fail. This is where the infrastructure team needs to observe this behaviour, process the information and plan ahead in case
this situation ever occurs in production.

An entire region can also be take down just by running the following command:

```bash
curl --location --request POST 'http://outages.localhost.localstack.cloud:4566/outages' \
                                                             --header 'Content-Type: application/json' \
                                                             --data '
                                                         [
                                                         {
                                                         "service": "*",
                                                         "region": "us-east-1"
                                                         }
                                                         ]'
```

Outages may be stopped by using empty list in the configuration. The following request will clear the current configuration:

```bash
curl --location --request POST 'http://outages.localhost.localstack.cloud:4566/outages' \
--header 'Content-Type: application/json' \
--data '[]'
```

To retrieve the current configuration, make the following GET call:
```bash
curl --location --request GET 'http://outages.localhost.localstack.cloud:4566/outages'
```

To add a new service/region rule pair to the configuration, make a PATCH call as follows:
```bash
curl --location --request PATCH 'http://outages.localhost.localstack.cloud:4566/outages' \
--header 'Content-Type: application/json' \
--data '[{"service": "transcribe", "region": "us-west-1"}]'
```

To remove a service/region rule pair from the configuration, make a DELETE call as follows:

```bash
curl --location --request DELETE 'http://outages.localhost.localstack.cloud:4566/outages' \
--header 'Content-Type: application/json' \
--data '[{"service": "transcribe", "region": "us-west-1"}]'
```
