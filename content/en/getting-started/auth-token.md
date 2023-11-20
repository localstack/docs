---
title: "Auth Token"
weight: 20
description: >
  Configure your Auth Token to start LocalStack
---

## Introduction

The Auth Token is a personal identifier used for user authentication outside the LocalStack Web Application, particularly in conjunction with the LocalStack core cloud emulator. Its primary functions are to retrieve the user's license and enable access to advanced features, effectively replacing the older developer API keys.

The Auth Token remains unchanged unless manually rotated by the user, regardless of any license assignment changes. You can locate your Auth Token on the [Getting Started page](https://app.localstack.cloud/getting-started) or the [Auth Token page](https://app.localstack.cloud/workspace/auth-token) in the LocalStack Web Application.

{{< alert title="Important" color="danger" >}}
-   Previously, API keys were required to activate the LocalStack core cloud emulator. These API keys are now being replaced by Auth Tokens.
-   Currently, LocalStack supports both API Keys and Auth Tokens. However, API Keys will be discontinued in the upcoming major release of LocalStack.
-   To update your LocalStack configuration, replace your API Key with an Auth Token. Use the `LOCALSTACK_AUTH_TOKEN` environment variable in place of `LOCALSTACK_API_KEY`.
{{< /alert >}}

## Managing your License

To begin using LocalStack, a license is required. If you don't already have a license, you can opt for a free 14-day trial by [signing up here](https://localstack.cloud/pricing/), with no credit card required. This trial allows full access to all LocalStack features.

For license management, assign licenses to users via the [Users & Licenses page](https://app.localstack.cloud/workspace/members). To view your own assigned license, visit the [My License page](https://app.localstack.cloud/workspace/my-license).

{{< alert title="Important" color="danger" >}}
-   It's crucial to keep your Auth Token confidential. Do not include it in source code management systems, such as Git repositories.
-   Be aware that if an Auth Token is committed to a public repository, it's at risk of exposure, and could remain in the repository's history, even if attempts are made to rewrite it.
-   In case your Auth Token is accidentally published, immediately rotate it on the [Auth Token page](https://app.localstack.cloud/workspace/auth-token).
-   For use in Continuous Integration (CI) or automated test environments, a CI key is necessary. Refer to our [CI documentation]({{< ref "user-guide/ci" >}}) for guidance on securely handling secrets, including storing your CI key in these environments.
{{< /alert >}}

### Starting LocalStack via CLI

LocalStack requires the `LOCALSTACK_AUTH_TOKEN` environment variable to contain your Auth Token. You should set the `LOCALSTACK_AUTH_TOKEN` environment variable either before or during the startup of LocalStack using the `localstack` command-line interface (CLI).

{{< tabpane >}}
{{< tab header="macOS/Linux" lang="shell" >}}
export LOCALSTACK_AUTH_TOKEN=<YOUR_AUTH_TOKEN>
localstack start
{{< /tab >}}
{{< tab header="Windows" lang="powershell" >}}
$env:LOCALSTACK_AUTH_TOKEN="<YOUR_AUTH_TOKEN>"; localstack start
{{< /tab >}}
{{< /tabpane >}}

You have the option to run your LocalStack container in the background by appending the `-d` flag to the `localstack start` command.

The `localstack` CLI automatically detects the Auth Token and appropriately conveys it to the LocalStack container.

{{< alert title="Note" >}}
If you're using LocalStack with an Auth Token, it's necessary to download the [LocalStack Pro image](https://docs.localstack.cloud/references/docker-images/#localstack-pro-image), which includes Pro services and several advanced features.
{{< /alert >}}

### Starting LocalStack via Docker

To start LocalStack via Docker, you need to provide the Auth Token using the `-e` flag, which is used for setting environment variables.

{{< command "hl_lines=5" >}}
$ docker run \
  --rm -it \
  -p 4566:4566 \
  -p 4510-4559:4510-4559 \
  -e LOCALSTACK_AUTH_TOKEN=${LOCALSTACK_AUTH_TOKEN:- } \
  localstack/localstack-pro
{{< / command >}}

For more information about starting LocalStack with Docker, take a look at our [Docker installation](https://docs.localstack.cloud/getting-started/installation/#docker) guide.

### Starting LocalStack via Docker-Compose

To start LocalStack using `docker-compose`, you have to include the `LOCALSTACK_AUTH_TOKEN` environment variable in your `docker-compose.yml` file:

```yaml
environment:
  - LOCALSTACK_AUTH_TOKEN=${LOCALSTACK_AUTH_TOKEN- }
```

You can manually set the Auth Token, or use the `export` command to establish the Auth Token in your current shell session. This ensures the Auth Token is transmitted to your LocalStack container, enabling key activation.

## Licensing-related configuration

To ensure that LocalStack only starts when you can activate LocalStack Pro or Enterprise, or if you want to avoid licensing-related error messages, refer to our [configuration guide](https://docs.localstack.cloud/references/configuration/#localstack-pro) about LocalStack Pro.

## Checking license activation

The simplest method to verify if LocalStack is active is by querying the health endpoint for a list of running services:

{{< command >}}
$ curl localhost:4566/_localstack/health | jq
{{< / command >}}

If you see a Pro-only service, like [XRay](https://docs.localstack.cloud/user-guide/aws/xray), listed as running, it indicates that LocalStack has started successfully. Another way to confirm this is by checking the logs of the LocalStack container for a message indicating successful license activation:

{{< command >}}
[...] Successfully activated license
{{< / command >}}

Otherwise, check our collected most [common activation issues](#common-activation-issues).

## Rotating the Auth Token

Your personal Auth Token provides full access to your workspace and LocalStack license. It's important to treat auth tokens as confidential, avoiding sharing or storing them in source control management systems (SCMs) like Git.

If you believe your Auht Token has been compromised or becomes known to someone else, reset it without delay. When you reset a token, the old one is immediately deactivated, losing its ability to access your license or workspace. It's not possible to restore previous tokens.

To rotate your Auth Token, go to the [Auth Token page](https://app.localstack.cloud/workspace/auth-token) and select the **Reset Auth Token** option.

## Common activation issues

Starting from version 2.0.0, the `localstack/localstack-pro` image in LocalStack demands a successful license activation for startup. If the activation of the license is unsuccessful, LocalStack will exit and display error messages.

```bash
===============================================
License activation failed! 🔑❌

Reason: The credentials defined in your environment are invalid. Please make sure to either set the LOCALSTACK_AUTH_TOKEN variable to a valid auth token, or the LOCALSTACK_API_KEY variable to a valid LocalStack API key. You can find your auth token or API key in the LocalStack web app https://app.localstack.cloud.

Due to this error, Localstack has quit. LocalStack pro features can only be used with a valid license.

- Please check that your credentials are set up correctly and that you have an active license.
  You can find your credentials in our webapp at https://app.localstack.cloud.
- If you want to continue using LocalStack without pro features you can set `ACTIVATE_PRO=0`.
```

Key activation in LocalStack can fail for several reasons:

-   **Missing Credentials:** Using the `localstack/localstack-pro` image typically requires an Auth Token or a legacy API key.
-   **Invalid License:** This occurs if there's no valid license linked to your account, possibly due to expiration.
-   **License Server Unreachable:** LocalStack attempts offline activation if the license server is inaccessible, but this necessitates re-activation every 24 hours.

If you're using the `localstack/localstack-pro` image but are unable to activate your license, consider switching to the community version, `localstack/localstack`. If switching isn't feasible, setting `ACTIVATE_PRO=0` will try to start LocalStack without the Pro features.

Navigate to our [FAQ page]({{< ref "faq" >}}) if your are having troubles with the LocalStack license activation.
If you have any further problems concerning your license activation, or if the steps do not help, do not hesitate to [contact us](https://localstack.cloud/contact/).
