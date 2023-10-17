---
title: "Transparent Endpoint Injection"
linkTitle: "Transparent Endpoint Injection"
weight: 9
description: >
  Transparently inject local endpoints into AWS SDKs and redirect your AWS calls to LocalStack
aliases:
  - /tools/local-endpoint-injection/
  - /tools/local-endpoint-injection/dns-server/
  - /user-guide/tools/transparent-endpoint-injection/patched-sdks/
  - /user-guide/tools/transparent-endpoint-injection/dns-server
---

## Introduction

LocalStack Community edition requires the application code to configure each AWS SDK client instance with the target endpoint URL. This URL should be set to point to the APIs on `localhost` or, in the case of Lambdas running in the context of LocalStack. Hence the endpoint URL should be directed to `http://${LOCALSTACK_HOSTNAME}:${EDGE_PORT}`.

LocalStack Pro/Team version enables your application logic to seamlessly communicate with local APIs, eliminating the need to modify your production code, through an integrated DNS server.

## DNS Server

LocalStack's DNS server maps the domain name `localhost.localstack.cloud` to the LocalStack container. This allows easy connections from your container to LocalStack, as well as from resources like Lambda, ECS, or EC2 to LocalStack. The transparent execution mode allows your application code to automatically interact with LocalStack APIs instead of the real AWS APIs.

Upon container startup, the log output will display the IP address of the local DNS server. If the host allows binding to port 53, the LocalStack CLI will expose port 53 from the container to the host with the IP address set to `127.0.0.1`. If binding to port 53 is not possible on the host, the port won't be exposed.

Regardless of port binding capabilities, the DNS server within the LocalStack container is bound to the address `0.0.0.0`, making it accessible for other containers within the same Docker network to utilize the DNS server.

For more in-depth information, refer to the [Network Troubleshooting guide]({{< ref "references/network-troubleshooting/endpoint-url#from-your-container" >}}).

## Configuration

If you encounter issues while running LocalStack due to problems with the DNS server, you have several options for configuration.

### Disabling the DNS Server

To disable the DNS server, you can set the `DNS_ADDRESS` variable to `0` using this command:

{{< command >}}
$ DNS_ADDRESS=0
{{< / command >}}

{{< alert title="Warning" color="warning" >}}
This configuration is not recommended as it prevents the resolution of `localhost.localstack.cloud` to the LocalStack container.
{{< / alert >}}

### Specifying Redirected URLs

You can define specific URLs to be redirected to LocalStack by setting a hostname regex with the `DNS_LOCAL_NAME_PATTERNS` variable, like this:

{{< command >}}
$ DNS_LOCAL_NAME_PATTERNS='.*(ecr|lambda).*.amazonaws.com'
{{< / command >}}

With this setup, the LocalStack DNS server will only redirect domains related to ECR and Lambda to LocalStack, while other domains will be resolved using the `$DNS_SERVER`. This configuration is useful for hybrid setups where some API calls (e.g., ECR, Lambda) are directed to LocalStack, while others target real AWS.

{{< alert title="Warning" color="warning">}}
We do not recommend connecting to real AWS from within LocalStack. You should avoid using real AWS credentials anywhere in your LocalStack setup.
{{< /alert >}}

### Setting a Custom DNS Server

You have the option to manually specify the DNS server to which queries that are not redirected should be forwarded. For instance:

{{< command >}}
$ DNS_SERVER=1.1.1.1
{{< / command >}}

By default, LocalStack uses the Google DNS resolver at `8.8.8.8`.

## Self-signed certificates

When configuring transparent execution mode using DNS, it's important to note that you might encounter SSL certificate validation issues when working with your application's AWS SDK. This is due to a technical limitation resulting from the SSL certificate validation process, as we redirect AWS domain names (e.g., `*.amazonaws.com`) to `localhost`. For example, the following command will fail with an SSL error:

{{< command >}}
$ aws kinesis list-streams
<disable-copy>
SSL validation failed for https://kinesis.us-east-1.amazonaws.com/ [SSL: CERTIFICATE_VERIFY_FAILED] certificate verify failed: self signed certificate (_ssl.c:1076)
</disable-copy>
{{< / command >}}

However, you can work around this issue using the following command:

{{< command >}}
$ PYTHONWARNINGS=ignore aws --no-verify-ssl kinesis list-streams
<disable-copy>
{
    "StreamNames": []
}
</disable-copy>
{{< / command >}}

Disabling SSL validation depends on the programming language and version of the AWS SDK you are using. For instance, the [AWS SDK for Python (`boto3` )](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/core/session.html#boto3.session.Session.client) offers a `verify=False` parameter to disable SSL verification. Most other AWS SDKs also provide similar parameters for this purpose.

For Node.js, you can allow the AWS SDK to communicate with the local APIs over SSL by setting the following environment variable in your application:

{{< command >}}
process.env.NODE_TLS_REJECT_UNAUTHORIZED = "0"
{{< / command >}}

{{< alert title="Warning" color="warning">}}
Disabling SSL validation may have unintended consequences and security risks. It should only be used for local testing and never in a production environment.
{{< /alert >}}

## System DNS configuration

To enable transparent execution mode, your system should be set up to utilize the predefined DNS server. This configuration is essential if you intend to test code that runs directly on your system against LocalStack instead of AWS. The specific steps for configuration depend on your operating system.

{{< alert title="Warning" color="warning">}}
Exercise caution when modifying your system's network configuration, as it may lead to unintended consequences.
{{< /alert >}}

### macOS

On macOS, you can configure it through the Network System Settings, while on Linux, you usually configure it by adjusting `/etc/resolv.conf` as follows:

```text
nameserver 0.0.0.0
```

The example above should be adapted to the actual IP address of the DNS server. You can also set a custom IP address by defining the `DNS_ADDRESS` environment variable (e.g., `DNS_ADDRESS=127.0.0.1`).

If you need host access to DNS, it's important that Docker can expose port 53 from the LocalStack container to your host. This is only possible if there are no other processes listening on port 53.

One common macOS process that listens on port 53 is `mDNSResponder`, which is a part of the [Bonjour protocol](https://developer.apple.com/bonjour/). You can check if any program is listening on a specific port using the following command:

```bash
# sudo is required if the port is < 1024
[sudo] lsof -P -i :<port> | grep LISTEN
# e.g. sudo lsof -P -i :53 | grep LISTEN
```

If `mDNSResponder` is listening on port 53, the output will resemble the following:

{{< command >}}
$ sudo lsof -P -i :53 | grep LISTEN
<disable-copy>
mDNSRespo 627 _mdnsresponder   54u  IPv4 0xbe20f6c354a1802d      0t0  TCP *:53 (LISTEN)
mDNSRespo 627 _mdnsresponder   55u  IPv6 0xbe20f6c34d8b9d75      0t0  TCP *:53 (LISTEN)
</disable-copy>
{{< / command >}}

If you encounter this situation, you can disable "Internet Sharing" in system preferences, which should in turn disable Bonjour and `mDNSResponder`.

### Linux

Configuring LocalStack on Linux depends on your network manager/DNS configuration. You can either use the LocalStack CLI command or manually configure the DNS server. When correctly configured, only requests for the specified domain names will be routed to LocalStack, while all other queries will resolve as usual.

#### systemd-resolved

On many modern systemd-based distributions, such as Ubuntu, systemd-resolved is used for name resolution. LocalStack provides a CLI command to facilitate this scenario. To use systemd-resolved with LocalStack domain resolution, start LocalStack with `DNS_ADDRESS=127.0.0.1` as environment variable. This configuration allows LocalStack to bind port 53 on 127.0.0.1, while systemd-resolved binds its stub resolver to 127.0.0.53:53, avoiding conflicts.

Once LocalStack is running, you can test the DNS server using the following commands:

{{< command >}}
$ dig @127.0.0.1 s3.amazonaws.com
$ dig @127.0.0.53 s3.amazonaws.com
{{< / command >}}

The first command should return an A record of `127.0.0.1`, while the second should return the actual AWS DNS result.

To set up systemd-resolved and LocalStack, run:

{{< command >}}
$ localstack dns systemd-resolved
{{< / command >}}

To revert the changes, execute:

{{< command >}}
$ localstack dns systemd-resolved --revert
{{< / command >}}

{{< alert title="Note">}}
You need sudo privileges to execute these commands.
{{< /alert >}}

This command configures the DNS server for the bridge interface of the Docker network where LocalStack is running, mapping it to the LocalStack container's IP address. It also sets up the DNS route to exclusively route specific DNS names (and their subdomains) to the LocalStack DNS. The configured domain names include:

- `~amazonaws.com`
- `~aws.amazon.com`
- `~cloudfront.net`
- `~localhost.localstack.cloud`

#### Manual configuration

If you prefer to perform these actions manually, identify the bridge interface and container IP of your LocalStack container using `docker inspect localstack_main` for the IP address and `docker inspect network` for the interface name. 

The interface name is typically the first 12 characters of the network ID, prefixed with `br-` (e.g., `br-0ae393d3345e`) if it's not explicitly mentioned. If you're using the default bridge network, it's typically `docker0`.

Configure the DNS resolver for the bridge network:

{{< command >}}
$ resolvectl dns <network_name> <container_ip>
{{< / command >}}

Set the DNS route to route only the previously mentioned domain names (and their subdomains) to LocalStack:

{{< command >}}
$ resolvectl domain <network_name> ~amazonaws.com ~aws.amazon.com ~cloudfront.net ~localhost.localstack.cloud
{{< / command >}}

In both cases, you can use `resolvectl query s3.amazonaws.com` or `resolvectl query example.com` to check which interface your DNS requests are routed through, ensuring that only the specified domains (and their subdomains) are directed to LocalStack.

#### Other resolution settings

The method for setting a DNS server can vary depending on your Linux distribution. In some systems, you can directly edit `/etc/resolv.conf`, similar to the [macOS configuration]({{< ref "#mac-os" >}}). 

If your `/etc/resolv.conf` gets overwritten by a service, you might be able to install and enable/start `resolvconf` and specify the nameserver in `/etc/resolvconf/resolv.conf.d/head` with `nameserver 127.0.0.1`. This will prepend the specified line in the resolv.conf file, even after changes.

{{< alert title="Note">}}
Using these options, all DNS requests are forwarded to LocalStack, except for queries that don't need modification (typically, all but specific AWS domains). LocalStack does not store or share any forwarded DNS requests, except potentially in local logs in exceptional cases or in debug mode.
{{< /alert >}}

## DNS Rebind Protection

If you depend on your local network's DNS, your router or DNS server might restrict requests due to DNS Rebind Protection. This protective feature is typically enabled by default in routers and DNS servers like pfSense, OPNSense, OpenWRT, AVM FritzBox, and possibly others. Some vendors may permit upstream responses within the 127.0.0.0/8 range, such as OpenWRT.

{{< alert title="Note" >}}
When using the LocalStack DNS server, DNS rebind protection should not pose any issues.
{{< / alert >}}

You can verify the functionality of your DNS setup by resolving a subdomain of `localhost.localstack.cloud` with the following command:

{{< command "hl_lines=16">}}
$ dig test.localhost.localstack.cloud
<disable-copy>
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
</disable-copy>
{{< /command >}}

If the DNS resolves the subdomain to your localhost (127.0.0.1), your setup is functioning correctly. If not, please review your router or DNS configuration to confirm if Rebind Protection is active or [enable the LocalStack DNS on your system]({{< ref "#system-dns-configuration" >}}).

## Customizing internal endpoint resolution

The DNS name `localhost.localstack.cloud`, along with its subdomains like `mybucket.s3.localhost.localstack.cloud`, plays a crucial internal role in LocalStack for routing requests between components, such as a Lambda container and the LocalStack APIs.

For detailed instructions on how to customize this internal DNS name, refer to the [Route53 documentation]({{< ref "route53" >}}).
