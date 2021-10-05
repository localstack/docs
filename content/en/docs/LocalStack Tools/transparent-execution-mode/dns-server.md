---
title: "DNS Server"
categories: ["LocalStack Pro", "Tools", "DNS"]
weight: 6
description: >
  Use LocalStack as DNS server to redirect AWS queries to LocalStack
---

## Overview

LocalStack Pro supports transparent execution mode, which means that your application code automatically accesses the LocalStack APIs as opposed to the real APIs on AWS.

When the system starts up, the log output contains the IP address of the local DNS server. Typically, this address by default is either `0.0.0.0` (see example below) or `127.0.0.1` if LocalStack cannot bind to `0.0.0.0` due to a conflicting service.
```
Starting DNS servers (tcp/udp port 53 on 0.0.0.0)...
```

## Configuration

The DNS server can be configured to match your usecase.

* The DNS server can be configured using the `DNS_ADDRESS` environment variable.
    To bind the server to `127.0.0.1`, you can set:

    ```bash
    DNS_ADDRESS=127.0.0.1
    ```

* You can disable the DNS server (which will prevent LocalStack from binding port 53) using:

    ```bash
    DNS_ADDRESS=0
    ```

* You can also specify which exact URLs should be redirected to LocalStack by defining a hostname regex like:

    ```bash
    DNS_LOCAL_NAME_PATTERNS='.*(ecr|lambda).*.amazonaws.com'
    ```

    Using this configuration, the LocalStack DNS server only redirects ECR and Lambda domains to LocalStack, and the rest will be resolved via `$DNS_SERVER`. This can be used for hybrid setups, where certain API calls (e.g., ECR, Lambda) target LocalStack, whereas other services will target real AWS.

    **Note:** We generally do not recommend connecting to real AWS from within LocalStack, in fact you should avoid using real AWS credentials anywhere in your LocalStack apps. Use this configuration with caution.

* There is the possibility to manually set the DNS server all not-redirected queries will be forwarded to:

    ```
    DNS_SERVER=1.1.1.1
    ```

    Per default, LocalStack uses the Google DNS resolver at `8.8.8.8`.

## Limitations

When you configure transparent execution mode using DNS, you may still have to configure your application's AWS SDK to **accept self-signed certificates**. This is a technical limitation caused by the SSL certificate validation mechanism, due to the fact that we are repointing AWS domain names (e.g., `*.amazonaws.com`) to `localhost`. For example, the following command will fail with an SSL error:
```
$ aws kinesis list-streams
SSL validation failed for https://kinesis.us-east-1.amazonaws.com/ [SSL: CERTIFICATE_VERIFY_FAILED] certificate verify failed: self signed certificate (_ssl.c:1076)
```
... whereas the following command works:
```
$ PYTHONWARNINGS=ignore aws --no-verify-ssl kinesis list-streams
{
    "StreamNames": []
}
```
Disabling SSL validation depends on the programming language and version of the AWS SDK used. For example, the [`boto3` AWS SDK for Python](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/core/session.html#boto3.session.Session.client) provides a parameter `verify=False` to disable SSL verification. Similar parameters are available for most other AWS SDKs.

## System DNS configuration

In order to use transparent execution mode, the system needs to be configured to use the predefined DNS server.
This is necessary if you want to test code running directly on your system against LocalStack, instead of AWS.
The configuration depends on the operating system.

**Note**: Please be careful when changing the network configuration on your system, as this may have undesired side effects.

### Mac OS

In Mac OS it can be configured in the Network System Settings, under Linux this is usually achieved by configuring `/etc/resolv.conf` as follows:
```
nameserver 0.0.0.0
```
The example above needs to be adjusted to the actual IP address of the DNS server. You can also configure a custom IP address by setting the `DNS_ADDRESS` environment variable (e.g., `DNS_ADDRESS=127.0.0.1`).

### Linux

In Linux, the configuration depends on your network manager / DNS configuration.

#### systemd-resolved

On many modern systemd-based distributions, like Ubuntu, systemd-resolved is used for name resolution.
LocalStack provides a CLI command for exactly this scenario.
To use systemd-resolved and the LocalStack domain resolution, try the following steps.

* Start LocalStack Pro with `DNS_ADDRESS=127.0.0.1` as environment variable.
This makes LocalStack bind port 53 on 127.0.0.1, whereas systemd-resolved binds its stub resolver to 127.0.0.53:53, which prevents a conflict.
Once LocalStack is started, you can test the DNS server using `dig @127.0.0.1 s3.amazonaws.com` versus `dig @127.0.0.53 s3.amazonaws.com`, the former should return an A record `127.0.0.1`, the latter the real AWS DNS result.

* Run:
    ```bash
    $ localstack dns systemd-resolved
    ```

    To revert, please run:
    ```bash
    $ localstack dns systemd-resolved --revert
    ```

    **Note**: You need sudo privileges to execute this command.

    This command sets the DNS server of the bridge interface of the docker network LocalStack currently runs in to the LocalStack container's IP address.
    (The command does not work with host networking or without LocalStack running for this reason.)
    Also, it configures the DNS route to exclusively (and only) route the following DNS names (and its subdomains) to the LocalStack DNS:

    ```
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

2. Configure the DNS resolver for the bridge network:
    ```
    # resolvectl dns <network_name> <container_ip>
    ```

3. Set the DNS route to route only the above mentioned domain names (and subdomains) to LocalStack:
    ```
    # resolvectl domain <network_name> ~amazonaws.com ~aws.amazon.com ~cloudfront.net ~localhost.localstack.cloud
    ```

In both cases, you can use `resolvectl query s3.amazonaws.com` or `resolvectl query example.com` to check which interface your DNS request is routed through, to confirm only the above mentioned domains (and its subdomains) are routed to LocalStack.

When correctly configured, either using the LocalStack CLI command or manually, only the requests for the mentioned domain names are routed to LocalStack, all other queries will resolve as usual.

#### Other resolution settings

Depending on your Linux distribution, the settings to set a DNS server can be quite different.
In some systems, directly editing `/etc/resolv.conf` is possible, like described in [Mac OS]({{< ref "#mac-os" >}}).
If your `/etc/resolv.conf` is overwritten by some service, it might be possible to install and enable/start `resolvconf` and specify the nameserver in `/etc/resolvconf/resolv.conf.d/head` with `nameserver 127.0.0.1`.
This will prepend this line in the resolv.conf file even after changes.

**Note**: Using this options, every DNS request is forwarded to LocalStack, which will forward queries it does not need to modify (in essence all but certain aws domains).
LocalStack will not store or share any forwarded DNS requests, except maybe in the local logs on exceptions / in debug mode.
