---
title: Transparent endpoint injection
weight: 2
tags:
- troubleshooting
- networking
---

Suppose you're attempting to access LocalStack, but you're relying on transparent endpoint injection to redirect AWS (`*.amazonaws.com`) requests. In such cases, there are different approaches you can take depending on your setup.

## From your host

{{< figure src="../images/2.svg" width="400" >}}

If you're using LocalStack with an [API key]({{<ref "getting-started/api-key">}}), then you can utilize the [DNS server]({{<ref "user-guide/tools/transparent-endpoint-injection/dns-server">}}) to perform requests to LocalStack as if it were AWS.
You need to make two changes:

* Publish port 53 from the LocalStack docker container to your host.
* Configure your host to use the LocalStack DNS server by default.

For more details, see your [DNS server documentation]({{<ref "user-guide/tools/transparent-endpoint-injection/dns-server">}}).

For the community edition of LocalStack, you can employ your own DNS server to achieve a similar outcome, but it won't be managed by LocalStack. Note that in both cases, SSL verification must be disabled. See the [limitations of the DNS server]({{<ref "user-guide/tools/transparent-endpoint-injection/dns-server#limitations" >}}) for more information.

## From a lambda function

{{< figure src="../images/5.svg" width="400" >}}

Check out our documentation [on using transparent endpoint injection for Lambda in LocalStack]({{<ref "user-guide/tools/transparent-endpoint-injection">}}).
