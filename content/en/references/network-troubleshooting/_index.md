---
title: Network troubleshooting
weight: 2
tags:
- troubleshooting
- networking
description: >
  How to troubleshoot common network problems
---

## Overview

Below are several scenarios in which you may be trying to use LocalStack.
If you are having difficulties connecting your application code to LocalStack, please visit the links below each section which go into further details.

{{<alert title="Note">}}
LocalStack only binds to IPv4 addresses (e.g. `127.0.0.1`). Check you are not trying to access LocalStack over IPv6.
{{</alert>}}

---

## Accessing LocalStack directly

{{< figure src="./images/overview-1.svg" width="400" >}}

For example with the [AWS CLI]({{< ref "user-guide/integrations/aws-cli" >}}) where you need to specify the URL of LocalStack yourself, such as:

{{< command >}}
aws --endpoint-url http://localhost.localstack.cloud:4566 <command>
# or
awslocal <command>
{{< / command >}}

or using a language SDK, for example with [`boto3`](https://boto3.amazonaws.com/v1/documentation/api/latest/index.html):

```python
import boto3

client = boto3.client("s3", endpoint_url="http://localhost.localstack.cloud:4566")
```

[Click here to learn more...]({{< ref "endpoint-url" >}})

## Accessing LocalStack using transparent endpoint injection

{{< figure src="./images/overview-2.svg" width="400" >}}

You are using a [language SDK]({{< ref "/user-guide/integrations/sdks" >}}) to access LocalStack, for example [`boto3`](https://boto3.amazonaws.com/v1/documentation/api/latest/index.html), and are making requests to `amazonaws.com` and expecting them to reach LocalStack.

[Click here to learn more...]({{< ref "transparent-endpoint-injection" >}})

## Accessing a resource that LocalStack has created by URL

{{< figure src="./images/overview-3.svg" width="270" >}}

You have created a resource in LocalStack such as an RDS or OpenSearch instance.

[Click here to learn more...]({{< ref "created-resources" >}})

## Additional troubleshooting tips

These tips may help diagnose connectivity problems when accessing LocalStack.

### Resolving hostnames

You can use the `nslookup` tool to determine if a domain name resolves to the correct IP address:

{{<command>}}
$ nslookup localhost.localstack.cloud
Server:         192.168.0.2
Address:        192.168.0.2#53

Non-authoritative answer:
Name:   localhost.localstack.cloud
Address: 127.0.0.1
{{</command>}}

### Platform specific issues
#### Linux/macOS

TBD

#### Windows

TBD
