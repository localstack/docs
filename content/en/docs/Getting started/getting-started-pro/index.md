---
title: "LocalStack Pro"
categories: ["LocalStack Pro"]
description: >
  Use your API key to start LocalStack Pro.
---

This guide shows how to use your shiny new LocalStack Pro license, and go over some best-practices regarding usage, activation, and safety of your LocalStack Pro API key.

## Requirements

First, you need an API key for LocalStack Pro.
[You can get your key by signing up on our website](https://localstack.cloud/pricing/).\
Don't worry, you can sign-up without any payment details and try LocalStack Pro within your free trial for 14 days.

## Getting your API key

You can find your API key in the [LocalStack Web Interface](https://app.localstack.cloud) in the `Account → Subscriptions` section.

{{< alert title="API Key Security" >}}
- Do not share your API key with anyone. Especially make sure that you do not commit it to any source code management systems (like Git repositories).
  If you push an API key to a repository, it has potentially ben exposed to the public and it might remain in the history (even if you try to rewrite the history).

- If you accidentally publish your API key, please [contact us](https://localstack.cloud/contact/) to get your API key rotated!

- If you want to use your API key in your CI environment, please check out our [CI documentation]({{< ref "LocalStack in CI" >}}) to see the proper way to handle secrets in your CI environment.
{{< /alert >}}

## Using your API key

LocalStack Pro expects your API key to be present in the environment variable `LOCALSTACK_API_KEY`.
Before starting LocalStack, please define the environment variable in your terminal like this:

```sh
$ export LOCALSTACK_API_KEY=<your-api-key>
```

### Starting LocalStack Pro using the CLI

When starting LocalStack using the LocalStack CLI, you dot not have to perform any further steps (after exporting the environment variable).
```sh
$ localstack start
```

LocalStack will detect the API key and properly pass it to the LocalStack container.

### Starting LocalStack Pro using Docker

When starting LocalStack using a `docker run` command, you have to specify the API key using the `-e` flag for environment variables like this:

{{< highlight bash "hl_lines=5" >}}
docker run \
  --rm -it \
  -p 4566:4566 \
  -p 4571:4571 \
  -e LOCALSTACK_API_KEY=${LOCALSTACK_API_KEY:- } \
  localstack/localstack
{{< / highlight >}}

For more information about starting LocalStack, take a look at our general [Getting Started]({{< ref "Getting started" >}}) guide.

### Starting LocalStack Pro using Docker-Compose

When starting LocalStack using `docker-compose`, you have to make sure your API key is passed properly to the LocalStack container.
For this, you have to make sure to include the `LOCALSTACK_API_KEY` environment variable in your `docker-compose.yml` like this:

```yaml
environment:
  - LOCALSTACK_API_KEY=${LOCALSTACK_API_KEY- }
```

This statement sets the API key we defined before (by using the `export` command) into your LocalStack container, such that the key activation can take place.

## Licensing-related configuration

If you want to make sure that LocalStack is only started if LocalStack Pro can be activated, or if you want to supporess licensing-related error messages, take a look at our [configuration guide]({{< ref "configuration.md#localstack-pro">}}) regarding LocalStack Pro.

## Checking license activation

The easiest way to check if LocalStack Pro is activated is to check the health endpoing of LocalStack for a list of the running services:

```
curl localhost:4566/health | jq
```

If a Pro-only [service]({{< ref "Local AWS Services" >}}) -- like [XRay]({{< ref "XRay-Tracing" >}}) -- is running, LocalStack Pro has started successfully.

**Note**: This only works if your `SERVICES` config variable contains LocalStack Pro services.
If in doubt, try starting LocalStack without this variable set, so all services can start.

Otherwise, please check our collected most [common activation issues](#common-activation-issues).

## Common activation issues

### Invalid API key

If your API key is invalid, you will see an error message like this in the logs of LocalStack:

```
Activation key "abc..."(10) is invalid or expired! Reason: ...
```

If this error occurs, something is wrong with your API key or license.
Please make sure your API key is set correctly (check for typos!) and your license is valid.
If the API key still does not work, please [contact us](https://localstack.cloud/contact/).

### No connection to the LocalStack API

If your log output contains lines like:

```
WARNING:localstack_ext.bootstrap.licensing: Error activating API key "abc..."(10):
...
ConnectionRefusedError: [Errno 111] Connection refused
```

LocalStack cannot contact our API to perform the license activation.
Please confirm with your network administrator that no policies block the connection to our backend.

### Cannot resolve api.localstack.cloud

Log output like the following indicates that your machine cannot resolve the domain of the LocalStack API.

```
WARNING:localstack_ext.bootstrap.licensing: Error activating API key "abc..."(10):
...
socket.gaierror: [Errno -3] Temporary failure in name resolution
```

Please confirm this by using a tool like `dig`:

```sh
dig api.localstack.cloud
```

If the result has some other status than `status: NOERROR`, your machine cannot resolve this domain.

Some corporate DNS servers might filter requests to certain domains.
Please contact your network administrator in order to whitelist `localstack.cloud` domains.

### Your issue isn't listed here?
If you have any problems concerning your API key activation not mentioned here, or if these steps do not help, please do not hesitate to [contact us](https://localstack.cloud/contact/).
