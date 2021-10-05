---
title: "Getting started with LocalStack Pro"
categories: ["LocalStack Pro", "Getting started"]
weight: 6
description: >
  Use your API key to start LocalStack Pro
---

In this guide we will show you how to use your shiny new LocalStack Pro license, and go over some best-practices regarding usage, activation and safety of your LocalStack Pro API key.

## Requirements

You have to start a trial or [buy a LocalStack license] before you can use LocalStack Pro!

## Getting your API Key

You can find your API key in the [LocalStack Web Interface](https://app.localstack.cloud) under Account => Subscriptions.

{{< alert title="API Key Security" >}}
- Please do not share your API key with anyone, especially do not check it into any git repositories.

- If you need the API key in your CI environment, please check out our [CI documentation]({{< ref "LocalStack in CI" >}}) to see the proper way to handle secrets in your CI environment.

- If you accidentally publish your API key, please [contact us](https://localstack.cloud/contact/) to get your API key rotated!
{{< /alert >}}

## Using your API Key to start LocalStack Pro

LocalStack Pro expects your API key to be present in the environment variable `LOCALSTACK_API_KEY`.
Before starting LocalStack, please define the environment variable like this:

```
$ export LOCALSTACK_API_KEY=foobar
```

### Starting LocalStack using the CLI

When starting LocalStack using the LocalStack CLI, you have to do no further steps (after exporting the environment variable).
```
$ localstack start
```

LocalStack will detect the API key and properly pass it to the LocalStack container.

### Starting LocalStack using Docker Compose

When starting LocalStack using docker-compose, you have to make sure your API key is passed properly to the LocalStack container.
For this, you have to make sure to include the `LOCALSTACK_API_KEY` environment variable in your service config like this:

```yaml
environment:
  - LOCALSTACK_API_KEY=${LOCALSTACK_API_KEY- }
```

This statement sets the API key we defined before using `export ...` into your LocalStack container, so the key activation can take place.

### Starting LocalStack using docker run

When starting LocalStack using a `docker run` command, you have to specify the API key using the `-e` flag for environment variables like this:

{{< highlight bash "hl_lines=5" >}}
docker run \
--rm -it \
-p 4566:4566 \
-p 4571:4571 \
-e LOCALSTACK_API_KEY=${LOCALSTACK_API_KEY:- } \
localstack/localstack
{{< / highlight >}}

For more information about starting LocalStack, please consult [Getting Started]({{< ref "Getting started" >}}).

## Licensing related configuration

You wish to start LocalStack only if LocalStack Pro can be activated or want to supress licensing related error messages?
Please consult our [configuration guide]({{< ref "configuration.md#localstack-pro">}}) regarding LocalStack Pro.

## Checking License activation

The easiest way to check if LocalStack Pro is activated is to check the running services for Pro services:

```
curl localhost:4566/health | jq
```

If a Pro only [service]({{< ref "Local AWS Services" >}}), like Xray, is running, LocalStack Pro has started.

**Note**: This only works if your `SERVICES` config variable contains LocalStack Pro services.
If in doubt, try starting LocalStack without this variable set, so all services can start.

Otherwise, please check our collected most [common activation issues](#common-activation-issues).

## Common activation issues

### Invalid API key

If your API key is invalid, you will get an error message like this:

```
Activation key "abc..."(10) is invalid or expired! Reason: ...
```

If this error occurs, something is wrong with your API key or license.
Please make sure your API key is set correctly (check for typos!) and your License is valid.
If the API key still does not work, please [contact us](https://localstack.cloud/contact/).

### No connection to the LocalStack API

If your log output contains lines like:

```
WARNING:localstack_ext.bootstrap.licensing: Error activating API key "abc..."(10):
...
ConnectionRefusedError: [Errno 111] Connection refused
```

LocalStack cannot contact our API to perform the License activation.
Please confirm with your network administrator that no policies block the connection to our backend.

### Cannot resolve api.localstack.cloud

Log output like this:

```
WARNING:localstack_ext.bootstrap.licensing: Error activating API key "abc..."(10):
...
socket.gaierror: [Errno -3] Temporary failure in name resolution
```

indicates that your machine cannot resolve the domain of the LocalStack API.
Please confirm this using a tool like `dig`:

```
dig api.localstack.cloud
```

If the result has some other status than `status: NOERROR`, your machine cannot resolve this domain.

Some corporate DNS servers will filter requests to certain domains.
Please contact your network administrator to whitelist `localstack.cloud` domains.


If you have any problems concerning your API key activation not mentioned here, or if the steps do not help, please do not hesitate to [contact us](https://localstack.cloud/contact/).
