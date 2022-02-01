---
title: "External Service Port Range"
weight: 5
description: >
    The range of ports used by services not directly provided by LocalStack
---

Services like [OpenSearch]({{< ref "opensearch" >}}) or [Elasticsearch]({{< ref "elasticsearch" >}}) use external software which binds to separate ports.

Depending on the configuration of the individual LocalStack service, these services can either be accessed by using the proxy functionality of Localstack which assigns local domains to these external services.
For example, if OpenSearch is configured to use the [`OPENSEARCH_ENDPOINT_STRATEGY=domain`]({{< ref "opensearch#endpoints" >}}), a cluster can be reached by using the domain name `<domain-name>.<region>.<engine-type>.localhost.localstack.cloud`.
Messages coming to those domains are then relayed to the servers running on ports which do not have to be accessible from outside the Docker container.

Another option is using the *external service port range*, which - e.g. in OpenSearch - is enabled by using the [`OPENSEARCH_ENDPOINT_STRATEGY=port`]({{< ref "opensearch#endpoints" >}})).  
The external service port range is a set of pre-defined ports (by default `4510-4559`). LocalStack will chose a free port withing this range when starting an external service.
These ports need to be accessible from outside the Docker container and in turn allows to directly access an external service (as opposed to using LocalStack as a proxy).

The port range is configurable by using the environment variables `EXTERNAL_SERVICE_PORTS_START` and `EXTERNAL_SERVICE_PORTS_END`. This results in the external service port range `(EXTERNAL_SERVICE_PORTS_START, EXTERNAL_SERVICE_PORTS_END]` (i.e. the `EXTERNAL_SERVICE_PORTS_END` is _not_ included in the range).
