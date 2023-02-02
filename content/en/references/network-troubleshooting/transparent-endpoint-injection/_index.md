---
title: Transparent endpoint injection
weight: 2
tags:
- troubleshooting
- networking
---

You are trying to access LocalStack, but you are making requests to AWS (`*.amazonaws.com`) and are relying on transparent endpoint injection to redirect the requests.

# From your host

{{< figure src="../images/2.svg" width="400" >}}

If you are using LocalStack with an [API key]({{<ref "getting-started/api-key">}}), then you can use the [DNS server]({{<ref "user-guide/tools/local-endpoint-injection/dns-server">}}) to perform requests to LocalStack as if it were AWS.

If you are using the community version of LocalStack, you can provide your own DNS server to achieve the same result, but this is not managed by LocalStack.

In both cases, SSL verification must be disabled. See the [limitations of the DNS server]({{<ref "user-guide/tools/local-endpoint-injection/dns-server#limitations" >}}) for more information.

# From a lambda function
{{< figure src="../images/5.svg" width="400" >}}

* TODO
