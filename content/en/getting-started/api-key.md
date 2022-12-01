---
title: "API Key"
weight: 5
categories: ["LocalStack Pro & Enterprise"]
description: >
  Configure your API key to start LocalStack
aliases:
  - /get-started/pro/
---

The LocalStack API key is a unique identifier to authenticate your LocalStack instance. You can find your API key in the [LocalStack Web app](https://app.localstack.cloud/account/apikeys). This guide demonstrates how you can use your new LocalStack licenses and go over some best practices regarding the usage, activation, and safety of your LocalStack API key.

## Getting your API key

To get started, you need to have a LocalStack license. If you don't have one, you can [sign up for a free trial](https://localstack.cloud/pricing/) without any credit card required. The free trial will last 14 days, and you can use it to test all the features of LocalStack. After a free trial, you can find your API key in the [LocalStack Web app](https://app.localstack.cloud) in the **Account** → **Subscriptions** section.

{{< alert title="API Key Security" >}}
- Avoid sharing your API key with anyone. Ensure that you do not commit it to any source code management systems (like Git repositories).

- If you push an API key to a public repository, it has potentially been exposed and might remain in the history (even if you try to rewrite it).

- If you accidentally publish your API key, please [contact us](https://localstack.cloud/contact/) immediately to get your API key rotated!

- If you want to use your API key in your CI environment, check out our [CI documentation]({{< ref "user-guide/ci" >}}) to see the proper way to handle secrets in your CI environment to store your API key securely.
{{< /alert >}}

## Using your API key

LocalStack expects your API key to be present in the environment variable `LOCALSTACK_API_KEY`. Before starting LocalStack, define the environment variable - for example, using the following command in a MacOS or Linux environment:

{{< command >}}
$ export LOCALSTACK_API_KEY=<your-api-key>
{{< / command >}}

{{< alert >}}
If you are using LocalStack with an API Key, you need to pull `localstack/localstack-pro` image as part of your LocalStack setup. Going forward, `localstack/localstack-pro` image will contain our Pro-supported services and APIs.
{{< /alert >}}

### Starting LocalStack via CLI

To start LocalStack using the LocalStack CLI, you don't have to perform any further steps (after exporting the environment variable).

{{< command >}}
$ localstack start
{{< / command >}}

LocalStack will detect the API key and properly pass it to the LocalStack container.

### Starting LocalStack via Docker

To start LocalStack using Docker, you have to specify the API key using the `-e` flag for environment variables:

{{< command "hl_lines=5" >}}
$ docker run \
  --rm -it \
  -p 4566:4566 \
  -p 4510-4559:4510-4559 \
  -e LOCALSTACK_API_KEY=${LOCALSTACK_API_KEY:- } \
  localstack/localstack-pro
{{< / command >}}

For more information about starting LocalStack, take a look at our general [Getting Started]({{< ref "getting-started" >}}) guide.

### Starting LocalStack via Docker-Compose

To start LocalStack using `docker-compose`, you have to include the `LOCALSTACK_API_KEY` environment variable in your `docker-compose.yml` file:

```yaml
environment:
  - LOCALSTACK_API_KEY=${LOCALSTACK_API_KEY- }
```

It sets the API key we defined before (by using the `export` command) into your LocalStack container, such that the key activation can take place.

## Licensing-related configuration

If you want to make sure that LocalStack is only started if you can activate LocalStack Pro or Enterprise, or if you wish to suppress licensing-related error messages, take a look at our [configuration guide]({{< ref "configuration.md#localstack-pro">}}) regarding LocalStack Pro.

## Checking license activation

The easiest way to check if LocalStack is activated is to query the health endpoint for a list of the running services:

{{< command >}}
$ curl localhost:4566/_localstack/health | jq
{{< / command >}}

If a Pro-only [service]({{< ref "aws" >}}) -- like [XRay]({{< ref "XRay-Tracing" >}}) -- is running, LocalStack has started successfully. You can also check the logs of the LocalStack container to see if the activation was successful.

{{< command >}}
[...] Successfully activated API key
{{< / command >}}

Otherwise, check our collected most [common activation issues](#common-activation-issues).

## Common activation issues

Navigate to our [FAQ page]({{< ref "faq" >}}) if your are having troubles with the LocalStack API key activation If you have any further problems concerning your API key activation, or if the steps do not help, do not hesitate to [contact us](https://localstack.cloud/contact/).
