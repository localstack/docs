---
title: "External Service Port Range"
weight: 5
description: >
    The range of ports used by services not directly provided by LocalStack
---

Services like [OpenSearch]({{< ref "opensearch" >}}) or [Elasticsearch]({{< ref "elasticsearch" >}}) use external software which binds to separate ports.

One way to access those services is using the proxying functionality from Localstack which assigns local domains to the external services.
Messages coming to those domain are then relayed to the servers running on hidden ports.

Another option is using the *external service port range*, which, e.g. in OpenSearch, is enabled by using the endpoint strategy `port` (see [OpenSearch Endpoints]({{< ref "opensearch#endpoints" >}})).  
The external service port range is a set of pre-defined ports (`4510-4530`) which can be chosen from to start external services.
This way services like OpenSearch can be accessed directly as opposed to using the LocalStack proxy.
