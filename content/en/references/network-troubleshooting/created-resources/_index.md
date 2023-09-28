---
title: Accessing a resource created by LocalStack
weight: 3
tags:
- troubleshooting
- networking
---

If you have created a resource using LocalStack, such as an OpenSearch cluster or RDS database, you may need to access it from your application. Typically, these resources are accessible through a URL or a hostname provided by LocalStack. While the environment variable `HOSTNAME_EXTERNAL` can often control the returned hostname, this approach may only work for some cases. This guide will explore different scenarios and provide detailed instructions on accessing resources created by LocalStack under different scenarios.

{{<alert title="Note">}}
An additional environment variable is available: `LOCALSTACK_HOSTNAME`. It is primarily used for communication within LocalStack and should not be used. We are currently working on streamlining the configuration under different scenarios.
{{</alert>}}

## From your host

{{< figure src="../images/3.svg" width="400" >}}

For example, suppose you have created an OpenSearch cluster using LocalStack and want to access it from the same computer. In such a case, you can set the `HOSTNAME_EXTERNAL` environment variable to specify the desired hostname that will be returned. Check out the [service-specific documentation]({{<ref "user-guide/aws/feature-coverage">}}) for more details.

## From a container LocalStack created

{{< figure src="../images/6.svg" width="400" >}}

Check out our documentation while [using the endpoint URL]({{<ref "endpoint-url#from-a-container-localstack-created" >}}).

<details>
<summary>For LocalStack versions before 2.3.0</summary>
The Lambda service in LocalStack also supports the <code>HOSTNAME_FROM_LAMBDA</code> environment variable, which can be handy if LocalStack is reachable through a specific hostname.
Suppose you're running LocalStack in a <a href="https://docs.docker.com/network/bridge/">user-defined network</a> using Docker, where the LocalStack container can be accessed from other containers in the network using its service name.
In that case, you can set the <code>HOSTNAME_FROM_LAMBDA</code> environment variable to this value to help resolve any issues with lambda functions accessing resources created by LocalStack.
</details>

## From your container

{{< figure src="../images/9.svg" width="400" >}}

Check out our documentation [on using the endpoint URL]({{<ref "endpoint-url#from-your-container" >}}).

## From a separate host

{{< figure src="../images/12.svg" width="400" >}}

LocalStack must listen to the address of the host, or `0.0.0.0`.

Check out our [FAQ article on accessing LocalStack from another computer]({{<ref "getting-started/faq#how-can-i-access-localstack-from-an-alternative-computer">}}).
