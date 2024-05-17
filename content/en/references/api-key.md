---
title: "API Key (Deprecated)"
linkTitle: "API Key (Deprecated)"
weight: 200
description: >
  Configure your API key to start LocalStack
aliases:
  - /get-started/pro/
  - /getting-started/api-key/
---

{{< callout "warning" >}}
-   LocalStack is transitioning from API Keys to Auth Tokens for activation. Auth Tokens streamline license management and remove the need for developers to adjust their setup when license changes occur.
-   For detailed information and guidance on migrating your LocalStack setup to Auth Tokens, please consult our [Auth Token documentation]({{< ref "auth-token" >}}).
-   API Keys will remain functional for LocalStack Pro and Enterprise users until the next major release. Following this release, LocalStack Pro and Enterprise will exclusively use Auth Tokens.
{{< /callout >}}

The LocalStack API key is a unique identifier to activate your LocalStack license needed to start LocalStack Pro.
You can find your API key in the [LocalStack Web app](https://app.localstack.cloud/account/apikeys).
This guide demonstrates how you can use your new LocalStack licenses and go over some best practices regarding the usage, activation, and safety of your LocalStack API key.

{{< callout "warning" >}}
- Avoid sharing your API key with anyone. Ensure that you do not commit it to any source code management systems (like Git repositories).
- If you push an API key to a public repository, it has potentially been exposed and might remain in the history (even if you try to rewrite it).
- If you accidentally publish your API key, please [contact us](https://localstack.cloud/contact/) immediately to get your API key rotated!
- If you want to use your API key in your CI environment, check out our [CI documentation]({{< ref "user-guide/ci" >}}) to see the proper way to handle secrets in your CI environment to store your API key securely.
{{< /callout >}}

### Starting LocalStack via CLI

LocalStack expects your API key to be present in the environment variable `LOCALSTACK_API_KEY`. You can define the `LOCALSTACK_API_KEY` environment variable before or while starting LocalStack using the `localstack` CLI.

{{< tabpane >}}
{{< tab header="macOS/Linux" lang="shell" >}}
export LOCALSTACK_API_KEY=<YOUR_API_KEY>
localstack start
{{< /tab >}}
{{< tab header="Windows" lang="powershell" >}}
$env:LOCALSTACK_API_KEY="<YOUR_API_KEY>"; localstack start
{{< /tab >}}
{{< /tabpane >}}

You can optionally run your LocalStack container in background mode by adding the `-d` flag to the `localstack start` command.

The `localstack` CLI will detect the API key and properly pass it to the LocalStack container.

{{< callout >}}
If you are using LocalStack with an API Key, you need to pull the [LocalStack Pro image](https://docs.localstack.cloud/references/docker-images/#localstack-pro-image) that includes the Pro services and several other advanced features.
{{< /callout >}}

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

For more information about starting LocalStack with Docker, take a look at our [Docker installation](https://docs.localstack.cloud/getting-started/installation/#docker) guide.

### Starting LocalStack via Docker-Compose

To start LocalStack using `docker-compose`, you have to include the `LOCALSTACK_API_KEY` environment variable in your `docker-compose.yml` file:

```yaml
environment:
  - LOCALSTACK_API_KEY=${LOCALSTACK_API_KEY- }
```

You can set the API key manually, or you can use the `export` command to set the API key in your current shell session. The API key will be passed into your LocalStack container, such that the key activation can take place.

## Licensing-related configuration

If you want to make sure that LocalStack is only started if you can activate LocalStack Pro or Enterprise, or if you wish to suppress licensing-related error messages, take a look at our [configuration guide]({{< ref "configuration.md#localstack-pro">}}) regarding LocalStack Pro.

## Checking license activation

The easiest way to check if LocalStack is activated is to query the health endpoint for a list of the running services:

{{< command >}}
$ curl localhost:4566/_localstack/health | jq
{{< / command >}}

If a Pro-only [service]({{< ref "aws" >}}) -- like [XRay]({{< ref "xray" >}}) -- is running, LocalStack has started successfully. You can also check the logs of the LocalStack container to see if the activation was successful.

{{< command >}}
[...] Successfully activated API key
{{< / command >}}

Otherwise, check our collected most [common activation issues](#common-activation-issues).

## Common activation issues

Since LocalStack v2.0.0, the image `localstack/localstack-pro` requires a successful key activation to start.
If the key activation fails, LocalStack will quit with an error messages that may look something like this:

```
===============================================
API key activation failed! 🔑❌

The API key you provided in the `LOCALSTACK_API_KEY` environment variable '"foo..."(6)' could not beactivated against our licensing server. Server message: Unable to verify API key.

Due to this error, Localstack has quit. LocalStack pro features can only be used with a valid license.

- Please check that your API key is set up correctly and that you are using the correct key.
  You can find your API key in our webapp at https://app.localstack.cloud.
- If you want to continue using LocalStack without pro features you can set `ACTIVATE_PRO=0`.
```

There are several reasons a key activation can fail:
* Missing credentials: Using `localstack/localstack-pro` requires per default to have an API key set.
* Invalid key: there is no valid license associated with the key, for example because the license has expired.
* License server cannot be reached: LocalStack will try to perform an offline license activation if the license server cannot be reached, but will require a re-activation every 24 hours.

If you are using the `localstack/localstack-pro` image, but cannot activate your license key, we recommend falling back to the community image `localstack/localstack`.
If that is not an option, you can set `ACTIVATE_PRO=0` which will attempt to start LocalStack without pro features.
