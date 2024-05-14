---
title: "Transparent Endpoint Injection"
linkTitle: "Transparent Endpoint Injection"
weight: 10
description: >
  Transparently resolve your AWS calls to LocalStack
tags: ["Pro image"]
---

LocalStack provides Transparent Endpoint Injection,
which enables seamless connectivity to LocalStack without modifying your application code targeting AWS.
The [DNS Server]({{< ref "dns-server" >}}) resolves AWS domains such as `*.amazonaws.com` including subdomains to the LocalStack container.
Therefore, your application seamlessly accesses the LocalStack APIs instead of the real AWS APIs.
For local testing, you might need to disable SSL validation as explained under [Self-signed certificates](#self-signed-certificates).

## Motivation

Previously, your application code targeting AWS needs to be modified to target LocalStack.
For example, the AWS SDK client for Python called boto3 needs to be configured using the environment variable `AWS_ENDPOINT_URL`, which is available within Lambda functions in LocalStack:

```python
client = boto3.client("lambda", endpoint_url=os.environ['AWS_ENDPOINT_URL'])
```

For [supported AWS SDKs](https://docs.aws.amazon.com/sdkref/latest/guide/feature-ss-endpoints.html#ss-endpoints-sdk-compat) 
(including boto3 since [1.28.0](https://github.com/boto/boto3/blob/develop/CHANGELOG.rst#L892)),
this configuration happens automatically without any custom code changes.

Currently, no application code changes are required to let your application connect to local cloud APIs because
Transparent Endpoint Injection uses the integrated [DNS Server]({{< ref "dns-server" >}}) to resolve AWS API calls to target LocalStack.

## Configuration

This section explains the most important configuration options summarized under [Configuration]({{< ref "configuration#dns" >}}).

### Disable transparent endpoint injection

If you do not to use Transparent Endpoint Injection in LocalStack Pro, opt out using:

```bash
DISABLE_TRANSPARENT_ENDPOINT_INJECTION=1
```

This option disables DNS resolution of AWS domains to the LocalStack container and prevents Lambda from disabling SSL validation.
If Transparent Endpoint Injection is _not_ used, the AWS SDK within Lambda functions might connect to the real AWS API.
Transparent Endpoint Injection is only available in LocalStack Pro.

Alternatively, specific AWS endpoints can be resolved to AWS while continuing to use Transparent Endpoint Injection.
Refer to the [DNS server configuration]({{< ref "dns-server#configuration" >}}) for skipping selected domain name patterns.

{{< callout "warning" >}}
Use this configuration with caution because we generally do not recommend connecting to real AWS from within LocalStack.
{{< /callout >}}


## Self-signed certificates

In LocalStack Pro and Lambda, Transparent Endpoint Injection automatically disables SSL certificate validation of the AWS SDK for the
most common Lambda runtimes including Python, Node.js, and Java (SDK v1).
For other services and unsupported Lambda runtimes, you may have to configure your AWS clients to accept self-signed certificates because
we are repointing AWS domain names (e.g., `*.amazonaws.com`) to `localhost.localstack.cloud`.
For example, the following command fails with an SSL error:

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

If you are using the Java AWS SDK v2 in Lambda, you can opt in to automatically disable SSL validation using the configuration `LAMBDA_DISABLE_JAVA_SDK_V2_CERTIFICATE_VALIDATION=1`.

{{< callout "warning" >}}
Disabling SSL validation may have undesired side effects and security implications.
Make sure to use this only for local testing, and never in production.
{{< /callout >}}
