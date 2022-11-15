---
title: "Frequently Asked Questions"
linkTitle: "FAQ"
weight: 7
description: >
  This page answers the frequently asked questions about LocalStack Pro, Enterprise, and Community Editions. 
cascade:
  type: docs
---

## LocalStack Cloud Emulation FAQs

### Is using `localhost.localstack.cloud:4566` to set as the endpoint for AWS services recommended?

`localhost.localstack.cloud` is the recommended endpoint - especially for S3, in order to enable host-based bucket endpoints. For most of the other services, it is fine to use `localhost:4566`. Users can rely on the `localhost.localstack.cloud` domain to be publicly resolvable, and we also publish an SSL certificate that is automatically used inside LocalStack, in order to enable HTTPS endpoints with valid certificates.

Across our docs, we use `localhost:4566` instead of `localhost.localstack.cloud`, to provide a fallback option to users. The primary reason being that some users are behind a corporate firewall or an internet service provider that does not allow resolving `localhost.localstack.cloud` properly.

## LocalStack in CI FAQs

### How are CI credits in LocalStack calculated?

A CI key allows you to use LocalStack in your CI environment. Every activation of a CI key consumes one build credit. This means that with every build triggered through the LocalStack container you will consume one credit. To understand the CI pricing across our product tiers, follow up with our [LocalStack in CI]({{<ref "user-guide/ci">}}) documentation.

## LocalStack API key FAQs

### How do I check if my API key is valid and activated?

The easiest way to check if LocalStack Pro or Enterprise is activated is to check the health endpoint of LocalStack for a list of the running services:

{{< command >}}
$ curl localhost:4566/health | jq
{{< / command >}}

If a Pro-only [service]({{< ref "aws" >}}) -- like [XRay]({{< ref "XRay-Tracing" >}}) -- is running, LocalStack Pro or Enterprise has started successfully. If your API key is invalid, you will see an error message like this in the logs of LocalStack:

```bash
Activation key "abc..."(10) is invalid or expired! Reason: ...
```

If this error occurs, something is wrong with your API key or license. Make sure your API key is set correctly (check for typos!) and your license is valid. If the API key still does not work, please [contact us](https://localstack.cloud/contact/).

## LocalStack Platform FAQs

### What should I do if I cannot connect to LocalStack API?

If your log output contains lines like:

```shell
WARNING:localstack_ext.bootstrap.licensing: Error activating API key "abc..."(10):
...
ConnectionRefusedError: [Errno 111] Connection refused
```

LocalStack cannot contact our API to perform the license activation. Confirm with your network administrator that no policies block the connection to our backend.

### What should I do if I cannot resolve `api.localstack.cloud`?

Log output like the following indicates that your machine cannot resolve the domain of the LocalStack API.

```shell
WARNING:localstack_ext.bootstrap.licensing: Error activating API key "abc..."(10):
...
socket.gaierror: [Errno -3] Temporary failure in name resolution
```

Confirm this by using a tool like `dig`:

{{< command >}}
$ dig api.localstack.cloud
{{< / command >}}

If the result has some other status than `status: NOERROR,` your machine cannot resolve this domain.

Some corporate DNS servers might filter requests to certain domains. Contact your network administrator to safelist` localstack.cloud` domains.
