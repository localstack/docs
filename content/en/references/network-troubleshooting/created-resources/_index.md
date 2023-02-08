---
title: Accessing a resource created by LocalStack
weight: 3
tags:
- troubleshooting
- networking
---

You are trying to access a resource that was created by LocalStack, for example an OpenSearch cluster or RDS database.

When created, these resources are accessible from a URL, or they will return a hostname that use to access the resource.
In general, the environment variable `HOSTNAME_EXTERNAL` can be used to control what hostname is returned, though currently not in every case.
For more details about specific situations, see below.

{{<alert title="Note">}}
An additional environment variable is available: `LOCALSTACK_HOSTNAME`.
This is primarily used for communication within LocalStack and should not be used.
We are currently working on streamlining the configuration under different scenarios.
{{</alert>}}

# From your host

{{< figure src="../images/3.svg" width="400" >}}

**Example**: you have created an OpenSearch cluster and wish to access it from the computer that is running LocalStack.

The `HOSTNAME_EXTERNAL` environment variable can be set to configure the hostname returned.
See the [service-specific documentation]({{<ref "user-guide/aws/feature-coverage">}}) for more details.

# From a container LocalStack created

{{< figure src="../images/6.svg" width="400" >}}

See the [advice given when using the endpoint url]({{<ref "endpoint-url#from-a-container-localstack-created" >}}).

In addition, the Lambda service supports an additional environment variable `HOSTNAME_FROM_LAMBDA` which can be used if LocalStack is reachable given a specific hostname.
For example, when running LocalStack in a [user-defined network](https://docs.docker.com/network/bridge/), the LocalStack container can be reached from other containers in the network with the service name.
Setting `HOSTNAME_FROM_LAMBDA` to this value may resolve problems with lambda functions accessing resources created by LocalStack.

# From your container

{{< figure src="../images/9.svg" width="400" >}}

See the [advice given when using the endpoint url]({{<ref "endpoint-url#from-your-container" >}}).

# From a separate host

{{< figure src="../images/12.svg" width="400" >}}

LocalStack must listen to the address of the host, or `0.0.0.0`.

See our [FAQ article on accessing LocalStack from another computer]({{<ref "getting-started/faq#how-can-i-access-localstack-from-an-alternative-computer">}}).
