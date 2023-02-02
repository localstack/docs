---
title: Accessing a resource created by LocalStack
weight: 3
tags:
- troubleshooting
- networking
---

You are trying to access a resource that was created by LocalStack, for example an OpenSearch cluster or RDS database.

When created, these resources are accessible from a URL, or they will return a hostname that you can access.
In general, the environment variable `LOCALSTACK_HOSTNAME` can be used to control what hostname is returned.
For more details about specific situations, see below.

# From your host

{{< figure src="../images/3.svg" width="400" >}}

**Example**: you have created an OpenSearch cluster and wish to access it from the computer that is running LocalStack.

The `LOCALSTACK_HOSTNAME` environment variable can be set to configure the hostname returned.
See the [service-specific documentation]({{<ref "user-guide/aws/feature-coverage">}}) for more details.

# From a container LocalStack created

{{< figure src="../images/6.svg" width="400" >}}

See the [advice given when using the endpoint url]({{<ref "endpoint-url#from-a-container-localstack-created" >}}).

# From your container

{{< figure src="../images/9.svg" width="400" >}}

See the [advice given when using the endpoint url]({{<ref "endpoint-url#from-your-container" >}}).

# From a separate host

{{< figure src="../images/12.svg" width="400" >}}

LocalStack must listen to the address of the host, or `0.0.0.0`.

See our [FAQ article on accessing LocalStack from another computer]({{<ref "getting-started/faq#how-can-i-access-localstack-from-an-alternative-computer">}}).
