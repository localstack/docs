---
title: "External Service Port Range"
weight: 50
description: >
    The range of ports used by services not directly provided by LocalStack
---

## Introduction

LocalStack provides local cloud services, such as [OpenSearch]({{< ref "opensearch" >}}) or [Elasticsearch]({{< ref "elasticsearch" >}}), which utilize external software bound to specific ports. This documentation discusses two approaches to access these external services within LocalStack and explores the concept of an _external service port range_.

## Proxy Functionality for External Services

LocalStack offers a proxy functionality to access external services indirectly. In this approach, LocalStack assigns local domains to the external services based on the individual service's configuration. 

For instance, if OpenSearch is configured to use the [`OPENSEARCH_ENDPOINT_STRATEGY=domain`]({{< ref "opensearch#endpoints" >}}) setting, a cluster can be reached using the domain name `<domain-name>.<region>.<engine-type>.localhost.localstack.cloud`. Incoming messages to these domains are relayed to servers running on ports that do not require external accessibility.

## Direct Access with External Service Port Range

An alternative approach to accessing external services is by utilizing the _external service port range_. This method, applicable to services like OpenSearch, is activated using the [`OPENSEARCH_ENDPOINT_STRATEGY=port`]({{< ref "opensearch#endpoints" >}}) configuration. The external service port range is pre-defined and set to `4510-4559` by default.

When a LocalStack service starts an external service, it automatically selects an available port from within the specified range. The primary advantage of this approach is that these ports are accessible from outside the Docker container, allowing direct access to the external service without the need for LocalStack to act as a proxy.

## Configuring the External Service Port Range

To configure the external service port range, you can make use of the environment variables `EXTERNAL_SERVICE_PORTS_START` and `EXTERNAL_SERVICE_PORTS_END`. The range is defined as `(EXTERNAL_SERVICE_PORTS_START, EXTERNAL_SERVICE_PORTS_END]`, wherein the `EXTERNAL_SERVICE_PORTS_END` value is not included in the range.

By adjusting these environment variables, you can customize the port range according to your requirements, granting you greater flexibility in managing external service access.

## Running multiple LocalStack containers with Custom Port Mapping

If you wish to run multiple instances of LocalStack simultaneously, it is essential to ensure that the edge port (default: `4566`) and external service ports are mapped to non-overlapping ranges. Here's how you can achieve this using the LocalStack CLI:

{{< command >}}
$ GATEWAY_LISTEN=0.0.0.0:4566 EXTERNAL_SERVICE_PORTS_START=4510 EXTERNAL_SERVICE_PORTS_END=4559 MAIN_CONTAINER_NAME=localstack_main_1 localstack start
$ GATEWAY_LISTEN=0.0.0.0:4666 EXTERNAL_SERVICE_PORTS_START=4610 EXTERNAL_SERVICE_PORTS_END=4659 MAIN_CONTAINER_NAME=localstack_main_2 localstack start
$ GATEWAY_LISTEN=0.0.0.0:4766 EXTERNAL_SERVICE_PORTS_START=4710 EXTERNAL_SERVICE_PORTS_END=4759 MAIN_CONTAINER_NAME=localstack_main_3 localstack start
{{< /command >}}

By customizing the `GATEWAY_LISTEN` and `EXTERNAL_SERVICE_PORTS_START`/`EXTERNAL_SERVICE_PORTS_END` values for each instance, you can ensure that they operate on distinct port ranges, preventing any conflicts and enabling smooth execution of multiple LocalStack instances.
