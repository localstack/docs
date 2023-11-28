---
title: "DNS Server"
categories: ["LocalStack Pro", "Tools", "DNS"]
weight: 6
description: >
  Use LocalStack as DNS server to redirect AWS queries to LocalStack
aliases:
  - /tools/local-endpoint-injection/dns-server/
---

LocalStack includes a DNS server that enables seamless connectivity to LocalStack from different environments using `localhost.localstack.cloud` (Community + Pro).
The DNS server is available on all IPv4 addresses within the LocalStack container (i.e., listening to `0.0.0.0`) and resolves `localhost.localstack.cloud` to the LocalStack container.
Therefore, containers that are configured to use the DNS server can reach LocalStack using `localhost.localstack.cloud`.
This configuration happens automatically for containers created by LocalStack, including compute resources such as Lambda, ECS, and EC2.
Your container can be configured to use the DNS server as demonstrated in the [Network Troubleshooting guide]({{< ref "references/network-troubleshooting/endpoint-url#from-your-container" >}}).
If you wish to use the DNS server on your host system, follow the instructions under [System DNS configuration]({{< ref "dns-server#system-dns-configuration" >}}).

LocalStack Pro additionally offers a transparent execution mode (active by default), which enables seamless connectivity to LocalStack without changing your application code.
The DNS server resolves AWS domains such as `*.amazonaws.com` including subdomains to the LocalStack container.
Therefore, your application seamlessly accesses the LocalStack APIs instead of the real AWS APIs.
For local testing, you might need to disable SSL validation as explained under [Self-signed certificates]({{< ref "dns-server#self-signed-certificates" >}}).

{{< alert title="Notes" >}}
On your host machine, `localhost.localstack.cloud` resolves to `localhost` using a public DNS entry by LocalStack unless your router has [DNS rebind protection]({{< ref "dns-server#dns-rebind-protection" >}}) enabled.
{{< / alert >}}


## Configuration

This section explains the most important configuration options summarized under [Configuration]({{< ref "configuration#dns" >}}).

### Transparent endpoint injection (Pro)

If you do not want Lambda functions to use the transparent endpoint execution mode in LocalStack Pro, opt out using:

```bash
DISABLE_TRANSPARENT_ENDPOINT_INJECTION=1
```

This option disables DNS resolution of AWS domains to the LocalStack container and prevents Lambda from disabling SSL validation.
With disabled transparent endpoint execution mode, the AWS SDK within Lambda functions might connect to the real AWS API.
The transparent endpoint execution mode is only available in LocalStack Pro.

### DNS Server bind address

If you experience problems when running LocalStack and the DNS server is the issue, you can disable the DNS server using:

```bash
DNS_ADDRESS=0
```

{{< alert title="Warning" color="warning" >}}
We do not recommend disabling the DNS server since this disables resolving `localhost.localstack.cloud` to the LocalStack container.
{{< / alert >}}

This option is primarily used by [LocalStack developers]({{< ref "contributing/development-environment-setup" >}}) in host mode because binding port 53 requires root privileges and port 53 might be occupied.

### Fallback DNS server

If you want to use another upstream DNS resolver than Google (default `8.8.8.8`),
specify the fallback DNS server where all non-redirected queries (i.e., not matching `DNS_LOCAL_NAME_PATTERNS`) will be forwarded to:

```bash
DNS_SERVER=1.1.1.1
```

### Custom redirects

If you want to resolve only certain AWS URLs to LocalStack,
specify a comma-separated list of hostname regex patterns such as:

```bash
DNS_LOCAL_NAME_PATTERNS='.*(ecr|lambda).*.amazonaws.com'
```

Using this configuration, the LocalStack DNS server only resolves ECR and Lambda domains to LocalStack, and the rest will be resolved via the `DNS_SERVER` (i.e., the real DNS entry by default).
This can be used for hybrid setups, where certain API calls (e.g., ECR, Lambda) target LocalStack, whereas other services will target real AWS.
The regex pattern follows Python flavored-regex and can be tested at [regex101.com](https://regex101.com/r/OzIsQa/1).

[The regex101 link is maintained by Joel Scheuner (requires linking to GitHub or Google account).
It redirects to the main page if the saved example would not work.]: #

{{< alert title="Warning" color="warning">}}
Use this configuration with caution because we generally do not recommend connecting to real AWS from within LocalStack. 
{{< /alert >}}


## Self-signed certificates

In the transparent execution mode using DNS in LocalStack Pro, you may still have to configure your application's AWS SDK to accept self-signed certificates.
This is a technical limitation caused by the SSL certificate validation mechanism, due to the fact that we are repointing AWS domain names (e.g., `*.amazonaws.com`) to `localhost`.
For example, the following command will fail with an SSL error:

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

Disabling SSL validation depends on the programming language and version of the AWS SDK used.
For example, the [`boto3` AWS SDK for Python](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/core/session.html#boto3.session.Session.client) provides a parameter `verify=False` to disable SSL verification.
Similar parameters are available for most other [AWS SDKs](https://docs.aws.amazon.com/sdkref/latest/guide/version-support-matrix.html).

For Node.js, you can set this environment variable in your application, to allow the AWS SDK to talk to the local APIs via SSL:

```node.js
process.env.NODE_TLS_REJECT_UNAUTHORIZED = "0"
```

{{< alert title="Warning" color="warning">}}
Disabling SSL validation may have undesired side effects and security implications.
Make sure to use this only for local testing, and never in production.
{{< /alert >}}


## Customizing internal endpoint resolution

The DNS name `localhost.localstack.cloud` (and any subdomains like `mybucket.s3.localhost.localstack.cloud`) is used internally in LocalStack to route requests, e.g., between a Lambda container and the LocalStack APIs.

Please refer to the steps in the [Route53 docs]({{< ref "route53" >}}) for more details on how the internal DNS name can be customized.


## DNS rebind protection

If you rely on your local network's DNS, your router/DNS server might block requests due to the DNS Rebind Protection.
This feature is enabled by default in pfSense, OPNSense, OpenWRT, AVM FritzBox, and potentially also other devices.
Some of the vendors might allow upstream responses in the 127.0.0.0/8 range (like OpenWRT).

{{< alert title="Note" >}}
If you are using the LocalStack DNS server, DNS rebind protection should not cause any issues.
{{< / alert >}}

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

If the DNS resolves the subdomain to your localhost (127.0.0.1), your setup is working.
If not, please check the configuration of your router / DNS if the Rebind Protection is active or [enable the LocalStack DNS on your system]({{< ref "dns-server#system-dns-configuration" >}}).


## System DNS configuration

If you wish to use the DNS server on your host system, you need to expose the LocalStack DNS server and configure your operating system.
This is necessary if you want to test unmodified application code directly on your system against LocalStack and cannot configure the endpoint URL.

{{< alert title="Warning" color="warning">}}
Please be careful when changing the network configuration on your system, as this may have undesired side effects.
Restore the default configuration after testing.
{{< /alert >}}

1. Expose the LocalStack DNS server:

    a) The LocalStack CLI automatically publishes port 53 if it can be bound on the host.

    b) For Docker Compose, add the following port mappings to your `docker-compose.yml`:

     ```yaml
     ports:
       - "127.0.0.1:53:53"                # Expose DNS server to host
       - "127.0.0.1:53:53/udp"            # Expose DNS server to host
     ```

{{< alert title="Notes" >}}
If port 53 is already bound, `docker-compose up` fails with the error:
```plain
Error response from daemon: Ports are not available: exposing port UDP 127.0.0.1:53 -> 0.0.0.0:0: command failed
```

To find out if a program is listening on a port, run the following command:

```bash
# sudo is required if the port is < 1024
# [sudo] lsof -P -i :<port> | grep LISTEN
sudo lsof -P -i :53 | grep LISTEN
```

In macOS, a common process that listens on port 53 is `mDNSResponder`.
Docker for Mac 4.24 has a [known issue](https://docs.docker.com/desktop/release-notes/#4240) and suggests the following workaround:
> Deactivate network acceleration by adding `"kernelForUDP": false`, in the `settings.json` file located at `~/Library/Group Containers/group.com.docker/settings.json`.

Additionally, ensure that "Internet Sharing" is disabled in the system preferences as suggested in [this GitHub issue](https://github.com/docker/for-mac/issues/7008#issuecomment-1748344545).

{{< / alert >}}

2. Configure LocalStack to use a `DNS_SERVER` other than the host, for example using [CloudFlare DNS](https://www.cloudflare.com/learning/dns/what-is-1.1.1.1/) `DNS_SERVER=1.1.1.1`.
3. Configure your system to use the LocalStack DNS depending on your operating system:

### macOS

Search for "DNS servers" in the system preferences and add a new DNS server with the IP `127.0.0.1`.
Updates in the system settings are automatically reflected in `/etc/resolv.conf` and should add such an entry such as `nameserver 127.0.0.1`.

<img src="macs-dns-server-configuration.png" alt="macOS DNS server configuration" title="Configure DNS server in macOS system preferences" width="500" />

### Linux

In Linux, the configuration depends on your network manager/DNS configuration.

#### systemd-resolved

[//]: # (TODO: fix docs for Linux)
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
    Use `docker inspect localstack-main` to get the IP address and network, then `docker inspect network` to get the interface name.
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
In some systems, directly editing `/etc/resolv.conf` is possible, like described in [macOS]({{< ref "#mac-os" >}}).
If your `/etc/resolv.conf` is overwritten by some service, it might be possible to install and enable/start `resolvconf` and specify the nameserver in `/etc/resolvconf/resolv.conf.d/head` with `nameserver 127.0.0.1`.
This will prepend this line in the resolv.conf file even after changes.

{{< alert title="Note">}}
Using these options, every DNS request is forwarded to LocalStack, which will forward queries it does not need to modify (in essence all but certain AWS domains).
LocalStack does not share or store any forwarded DNS requests, except for local exception logging in debug mode.
{{< /alert >}}
