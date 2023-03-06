---
title: "DNS Server"
categories: ["LocalStack Pro", "Tools", "DNS"]
weight: 6
description: >
  Use LocalStack as DNS server to redirect AWS queries to LocalStack
aliases:
  - /tools/transparent-endpoint-injection/dns-server/
---

LocalStack Pro supports transparent execution mode, which means that your application code automatically accesses the LocalStack APIs as opposed to the real APIs on AWS.

When the system starts up, the log output contains the IP address of the local DNS server. Typically, this address by default is either `0.0.0.0` (see example below) or `127.0.0.1` if LocalStack cannot bind to `0.0.0.0` due to a conflicting service.

```text
Starting DNS servers (tcp/udp port 53 on 0.0.0.0)...
```

## Configuration

The DNS server can be configured to match your usecase using the `DNS_ADDRESS` environment variable.

To bind the server to `127.0.0.1`, you can set:

```bash
DNS_ADDRESS=127.0.0.1
```

You can disable the DNS server (which will prevent LocalStack from binding port 53) using:

```bash
DNS_ADDRESS=0
```

You can also specify which exact URLs should be redirected to LocalStack by defining a hostname regex like:

```bash
DNS_LOCAL_NAME_PATTERNS='.*(ecr|lambda).*.amazonaws.com'
```

Using this configuration, the LocalStack DNS server only redirects ECR and Lambda domains to LocalStack, and the rest will be resolved via `$DNS_SERVER`. This can be used for hybrid setups, where certain API calls (e.g., ECR, Lambda) target LocalStack, whereas other services will target real AWS.

{{< alert title="Warning" color="warning">}}
We generally do not recommend connecting to real AWS from within LocalStack, in fact you should avoid using real AWS credentials anywhere in your LocalStack apps. Use this configuration with caution.
{{< /alert >}}

There is the possibility to manually set the DNS server all not-redirected queries will be forwarded to:

```bash
DNS_SERVER=1.1.1.1
```

Per default, LocalStack uses the Google DNS resolver at `8.8.8.8`.

## Self-signed certificates

When you configure transparent execution mode using DNS, you may still have to configure your application's AWS SDK to accept self-signed certificates.
This is a technical limitation caused by the SSL certificate validation mechanism, due to the fact that we are repointing AWS domain names (e.g., `*.amazonaws.com`) to `localhost`. For example, the following command will fail with an SSL error:

{{< command >}}
$ aws kinesis list-streams
SSL validation failed for https://kinesis.us-east-1.amazonaws.com/ [SSL: CERTIFICATE_VERIFY_FAILED] certificate verify failed: self signed certificate (_ssl.c:1076)
{{< / command >}}

whereas the following command works:

{{< command >}}
$ PYTHONWARNINGS=ignore aws --no-verify-ssl kinesis list-streams
{
    "StreamNames": []
}
{{< / command >}}

Disabling SSL validation depends on the programming language and version of the AWS SDK used. For example, the [`boto3` AWS SDK for Python](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/core/session.html#boto3.session.Session.client) provides a parameter `verify=False` to disable SSL verification. Similar parameters are available for most other AWS SDKs.

For Node.js, you can set this environment variable in your application, to allow the AWS SDK to talk to the local APIs via SSL:

```node.js
process.env.NODE_TLS_REJECT_UNAUTHORIZED = "0"
```

{{< alert title="Warning" color="warning">}}
Disabling SSL validation may have undesired side effects and security implications.
Make sure to use this only for local testing, and never in production.
{{< /alert >}}

## System DNS configuration

In order to use transparent execution mode, the system needs to be configured to use the predefined DNS server.
This is necessary if you want to test code running directly on your system against LocalStack, instead of AWS.
The configuration depends on the operating system.

{{< alert title="Warning" color="warning">}}
Please be careful when changing the network configuration on your system, as this may have undesired side effects.
{{< /alert >}}


### Mac OS

In Mac OS it can be configured in the Network System Settings, under Linux this is usually achieved by configuring `/etc/resolv.conf` as follows:

```text
nameserver 0.0.0.0
```

The example above needs to be adjusted to the actual IP address of the DNS server. You can also configure a custom IP address by setting the `DNS_ADDRESS` environment variable (e.g., `DNS_ADDRESS=127.0.0.1`).

### Linux

In Linux, the configuration depends on your network manager/DNS configuration.

#### systemd-resolved

On many modern systemd-based distributions, like Ubuntu, systemd-resolved is used for name resolution.
LocalStack provides a CLI command for exactly this scenario.
To use systemd-resolved and the LocalStack domain resolution, try the following steps.

Start LocalStack Pro with `DNS_ADDRESS=127.0.0.1` as environment variable.
This makes LocalStack bind port 53 on 127.0.0.1, whereas systemd-resolved binds its stub resolver to 127.0.0.53:53, which prevents a conflict.
Once LocalStack is started, you can test the DNS server using `dig @127.0.0.1 s3.amazonaws.com` versus `dig @127.0.0.53 s3.amazonaws.com`, the former should return an A record `127.0.0.1`, the latter the real AWS DNS result.

Run:
{{< command >}}
$ localstack dns systemd-resolved
{{< / command >}}

To revert, please run:
{{< command >}}
$ localstack dns systemd-resolved --revert
{{< / command >}}

{{< alert title="Note">}}
You need sudo privileges to execute this command.
{{< /alert >}}

This command sets the DNS server of the bridge interface of the docker network LocalStack currently runs in to the LocalStack container's IP address.
(The command does not work with host networking or without LocalStack running for this reason.)
Also, it configures the DNS route to exclusively (and only) route the following DNS names (and its subdomains) to the LocalStack DNS:

```text
~amazonaws.com
~aws.amazon.com
~cloudfront.net
~localhost.localstack.cloud
```

If you want to perform this action manually, please do the following steps:

1. Find out the bridge interface and container IP of your LocalStack container.
    Use `docker inspect localstack_main` to get the IP address and network, then `docker inspect network` to get the interface name.
    If the interface name is not mentioned, it is usually the first 12 characters of the network ID prefixed with `br-`, like `br-0ae393d3345e`.
    If you use the default bridge network, it is usually `docker0`.

1. Configure the DNS resolver for the bridge network:

    {{< command >}}
    # resolvectl dns <network_name> <container_ip>
    {{< / command >}}

3. Set the DNS route to route only the above mentioned domain names (and subdomains) to LocalStack:

    {{< command >}}
    # resolvectl domain <network_name> ~amazonaws.com ~aws.amazon.com ~cloudfront.net ~localhost.localstack.cloud
    {{< / command >}}

In both cases, you can use `resolvectl query s3.amazonaws.com` or `resolvectl query example.com` to check which interface your DNS request is routed through, to confirm only the above mentioned domains (and its subdomains) are routed to LocalStack.

When correctly configured, either using the LocalStack CLI command or manually, only the requests for the mentioned domain names are routed to LocalStack, all other queries will resolve as usual.

#### Other resolution settings

Depending on your Linux distribution, the settings to set a DNS server can be quite different.
In some systems, directly editing `/etc/resolv.conf` is possible, like described in [Mac OS]({{< ref "#mac-os" >}}).
If your `/etc/resolv.conf` is overwritten by some service, it might be possible to install and enable/start `resolvconf` and specify the nameserver in `/etc/resolvconf/resolv.conf.d/head` with `nameserver 127.0.0.1`.
This will prepend this line in the resolv.conf file even after changes.

{{< alert title="Note">}}
Using these options, every DNS request is forwarded to LocalStack, which will forward queries it does not need to modify (in essence all but certain aws domains).
LocalStack will not store or share any forwarded DNS requests, except maybe in the local logs on exceptions/in debug mode.
{{< /alert >}}

## DNS Rebind Protection

If you rely on your local network's DNS, your router/DNS server might block requests due to the DNS Rebind Protection.
This feature is enabled by default in pfSense, OPNSense, OpenWRT, AVM FritzBox, and potentially also other devices.
Some of the vendors might allow upstream responses in the 127.0.0.0/8 range (like OpenWRT).

You can check if your DNS setup works correctly by resolving a subdomain of `localhost.localstack.cloud`:
{{< command "hl_lines=16">}}
$ dig test.localhost.localstack.cloud

; <<>> DiG 9.16.8-Ubuntu <<>> test.localhost.localstack.cloud
;; global options: +cmd
;; Got answer:
;; ->>HEADER<<- opcode: QUERY, status: NOERROR, id: 45150
;; flags: qr rd ra; QUERY: 1, ANSWER: 2, AUTHORITY: 0, ADDITIONAL: 1

;; OPT PSEUDOSECTION:
; EDNS: version: 0, flags:; udp: 65494
;; QUESTION SECTION:
;test.localhost.localstack.cloud. IN	A

;; ANSWER SECTION:
test.localhost.localstack.cloud. 10786 IN CNAME	localhost.localstack.cloud.
localhost.localstack.cloud. 389	IN	A	127.0.0.1

;; Query time: 16 msec
;; SERVER: 127.0.0.53#53(127.0.0.53)
;; WHEN: Fr Jän 14 11:23:12 CET 2022
;; MSG SIZE  rcvd: 90
{{< /command >}}

If the the DNS resolves the subdomain to your localhost (127.0.0.1), your setup is working.
If not, please check the configuration of your router / DNS if the Rebind Protection is active or [enable the LocalStack DNS on your system]({{< ref "dns-server#system-dns-configuration" >}}).

## Customizing internal endpoint resolution

The DNS name `localhost.localstack.cloud` (and any subdomains like `mybucket.s3.localhost.localstack.cloud`) is used internally in LocalStack to route requests, e.g., between a Lambda container and the LocalStack APIs.

Please refer to the steps in the [Route53 docs]({{< ref "route53" >}}) for more details on how the internal DNS name can be customized.
