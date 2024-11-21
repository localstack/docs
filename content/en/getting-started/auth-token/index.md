---
title: "Auth Token"
weight: 20
description: >
  Configure your Auth Token to access and activate LocalStack.
---

## Introduction

The Auth Token identifies and authenticates users outside the LocalStack Web Application to activate the LocalStack core cloud emulator.
It primarily accesses your workspace and advanced services & features.

Auth tokens come in two types: a **Developer Auth Token** and a **CI Auth Token**:

- The **Developer Auth Token** is linked to a specific user within a specific workspace.
  Every user has their own Auth Token.
  It cannot be deleted but can be rotated for security reasons if needed.
- The **CI Auth Token** is not associated with any specific user and is designed for use in CI environments and other non-developer contexts.
  These tokens are stored in the workspace and can be managed by members with appropriate permissions.

Both the **Developer Auth Token** and **CI Auth Token** can be managed on the [Auth Tokens page](https://app.localstack.cloud/workspace/auth-tokens).

{{< callout "warning">}}
- It's crucial to keep your Auth Token confidential.
  Do not include it in source code management systems, such as Git repositories.
- Be aware that if an Auth Token is committed to a public repository, it is at risk of exposure, and could remain in the repository's history, even if attempts are made to rewrite it.
- In case your Auth Token is accidentally published, immediately rotate it on the [Auth Token page](https://app.localstack.cloud/workspace/auth-tokens).
{{< /callout >}}

## Managing your License

To use LocalStack, a license is required.
You can get a license by registering on the [LocalStack Web Application](https://app.localstack.cloud/sign-up).
Choose between a 14-day trial or explore additional features with our paid offering.
During the trial period, you are welcome to use all the features of LocalStack.

After initiating your trial or acquiring a license, proceed to assign it to a user by following the steps outlined below:

- Visit the [Users & Licenses page](https://app.localstack.cloud/workspace/members).
- Select a user in the **Workspace Members** section for license assignment.
- Define user's role via the **Member Role** dropdown.
  Single users automatically receive the **Admin** role.
- Toggle **Advanced Permissions** to set specific permissions.
  Single users automatically receive full permissions.
- Click **Save** to complete the assignment.
  Single users assign licenses to themselves.

{{< img src="assigning-a-license.png" class="img-fluid shadow rounded" width="800" >}}
<br><br>

If you have joined a workspace, you need to be assigned a license by the workspace administrator.
In case of switching workspaces or licenses, you need to make sure that you are assigned to the correct license.

{{< callout "note" >}}
If you do not assign a license, you will not be able to use LocalStack even if you have a valid Auth token.
{{< /callout >}}

To view your own assigned license, visit the [My License page](https://app.localstack.cloud/workspace/my-license).
You can further navigate to the [Auth Token page](https://app.localstack.cloud/workspace/auth-tokens) to view your **Developer Auth Token** and **CI Auth Token**.

## Configuring your Auth Token

LocalStack requires the `LOCALSTACK_AUTH_TOKEN` environment variable to contain your Auth Token.
You can configure your Auth Token in several ways, depending on your use case.
The following sections describe the various methods of setting your Auth Token.

{{< callout "warning">}}
- It's crucial to keep your Auth Token confidential.
  Do not include it in source code management systems, such as Git repositories.
- Be aware that if an Auth Token is committed to a public repository, it's at risk of exposure, and could remain in the repository's history, even if attempts are made to rewrite it.
- In case your Auth Token is accidentally published, immediately rotate it on the [Auth Token page](https://app.localstack.cloud/workspace/auth-tokens).
{{< /callout >}}

### LocalStack CLI

You should set the `LOCALSTACK_AUTH_TOKEN` environment variable either before or during the startup of LocalStack using the `localstack` command-line interface (CLI).

{{< tabpane >}}
{{< tab header="macOS/Linux" lang="shell" >}}
localstack auth set-token <YOUR_AUTH_TOKEN>
localstack start
{{< /tab >}}
{{< tab header="Windows" lang="powershell" >}}
localstack auth set-token <YOUR_AUTH_TOKEN>
localstack start
{{< /tab >}}
{{< /tabpane >}}

{{< callout "note" >}}
1. You can alternatively set the `LOCALSTACK_AUTH_TOKEN` environment variable in your shell session.
  This ensures the Auth Token is transmitted to your LocalStack container, enabling key activation.
2. The `localstack auth set-token` command is only available for `localstack` CLI and cannot be used with a Docker/Docker Compose setup.
{{< /callout >}}

You have the option to run your LocalStack container in the background by appending the `-d` flag to the `localstack start` command.

The `localstack` CLI automatically detects the Auth Token and appropriately conveys it to the LocalStack container.

{{< callout "note" >}}
If you are using LocalStack with an Auth Token, it's necessary to download the [LocalStack Pro image](https://docs.localstack.cloud/references/docker-images/#localstack-pro-image), which includes Pro services and several advanced features.
{{< /callout >}}

### Docker

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

### Docker Compose

To start LocalStack using `docker compose`, you have to include the `LOCALSTACK_AUTH_TOKEN` environment variable in your `docker-compose.yml` file:

```yaml
environment:
  - LOCALSTACK_AUTH_TOKEN=${LOCALSTACK_AUTH_TOKEN- }
```

You can manually set the Auth Token, or use the `export` command to establish the Auth Token in your current shell session.
This ensures the Auth Token is transmitted to your LocalStack container, enabling key activation.

### CI Environments

CI environments require a CI Auth Token.
Developer Auth Tokens cannot be used in CI.
CI Auth Tokens are available on the [Auth Tokens page](https://app.localstack.cloud/workspace/auth-tokens) and are configured similarly to Developer Auth Tokens.

To set the CI Auth Token, add the Auth Token value in the `LOCALSTACK_AUTH_TOKEN` environment variable of your CI provider, and refer to it when starting LocalStack in your CI workflow.
You can find detailed examples in our [LocalStack in CI documentation](https://docs.localstack.cloud/user-guide/ci/).

## Rotating the Auth Token

Your personal Auth Token provides full access to your workspace and LocalStack license.
It's important to treat auth tokens as confidential, avoiding sharing or storing them in source control management systems (SCMs) like Git.

If you believe your Auth Token has been compromised or becomes known to someone else, reset it without delay.
When you reset a token, the old one is immediately deactivated, losing its ability to access your license or workspace.
It is not possible to restore previous tokens.

To rotate your Auth Token, go to the [Auth Token page](https://app.localstack.cloud/workspace/auth-tokens) and select the **Reset Auth Token** option.

## Licensing configuration & activation

To avoid logging any licensing-related error messages, set `LOG_LICENSE_ISSUES=0` in your environment.
Refer to our [configuration guide](https://docs.localstack.cloud/references/configuration/#localstack-pro) for more information.

The simplest method to verify if LocalStack is active is by querying the health endpoint for a list of running services:

{{< tabpane text=true >}}
{{< tab header="macOS/Linux" lang="shell" >}}

{{< command >}}
$ curl http://localhost:4566/_localstack/info | jq
{{< / command >}}

{{< /tab >}}
{{< tab header="Windows" lang="powershell" >}}

{{< command >}}
$ Invoke-WebRequest -Uri http://localhost:4566/_localstack/info | ConvertFrom-Json
{{< / command >}}

{{< /tab >}}
{{< /tabpane >}}

The following output would be retrieved:

```bash
{
  "version": "3.0.0:6dd3f3d",
  "edition": "pro",
  "is_license_activated": true,
  "session_id": "7132da5f-a380-44ca-8897-6f0fdfd7b1c9",
  "machine_id": "0c49752c",
  "system": "linux",
  "is_docker": true,
  "server_time_utc": "2023-11-21T05:41:33",
  "uptime": 161
}
````

You can notice the `edition` field is set to `pro` and the `is_license_activated` field is set to `true`.
Another way to confirm this is by checking the logs of the LocalStack container for a message indicating successful license activation:

{{< command >}}
[...] Successfully activated license
{{< / command >}}

Otherwise, check our [troubleshooting](#troubleshooting) section.

## FAQ

### How do I activate older versions of LocalStack (Before v3.0)?

Prior to the introduction of Auth Tokens, LocalStack used **API keys** managed through the `LOCALSTACK_API_KEY` environment variable for activation.

For backwards compatibility, we've updated our back-end to accept new Auth Tokens within the `LOCALSTACK_API_KEY` variable.
You can use the new Auth Token in the same way you previously used the API key.

### When will the legacy API keys be phased out?

In early 2025, we will begin phasing out legacy API keys entirely.
After the sunsetting period, legacy API and legacy CI keys will no longer activate or work with LocalStack.

During the sunsetting period, the legacy service will experience scheduled downtimes.
These are planned to encourage users to transition to new Auth Tokens while minimizing impact for those who have not yet updated.

The downtime schedule will be communicated well in advance, allowing users ample time to switch to the new Auth Tokens.

## Troubleshooting

While using Auth Tokens, LocalStack demands a successful license activation for startup.
If the activation of the license is unsuccessful, LocalStack will exit and display error messages.

```bash
===============================================
License activation failed! 🔑❌

Reason: The credentials defined in your environment are invalid. Please make sure to either set the LOCALSTACK_AUTH_TOKEN variable to a valid auth token, or the LOCALSTACK_API_KEY variable to a valid LocalStack API key. You can find your Auth Token or API key in the LocalStack web app https://app.localstack.cloud.

Due to this error, Localstack has quit. LocalStack pro features can only be used with a valid license.

- Please check that your credentials are set up correctly and that you have an active license.
  You can find your credentials in our webapp at https://app.localstack.cloud.
- If you want to continue using LocalStack without pro features you can set `ACTIVATE_PRO=0`.
```

The key activation in LocalStack may fail for several reasons, and the most common ones are listed below in this section.

### Missing Credentials

You need to provide either an Auth Token to start the LocalStack Pro image successfully.
You can find your Auth Token on the [Auth Tokens page](https://app.localstack.cloud/workspace/auth-tokens) in the LocalStack Web Application.

If you are using the `localstack` CLI, you can set the `LOCALSTACK_AUTH_TOKEN` environment variable to your Auth Token or use the following command to set it up:

{{< command >}}
$ localstack auth set-token <YOUR_AUTH_TOKEN>
{{< / command >}}

### Invalid License

The issue may occur if there is no valid license linked to your account due to expiration or if the license has not been assigned.
You can check your license status in the LocalStack Web Application on the [My License page](https://app.localstack.cloud/workspace/my-license).

### License Server Unreachable

LocalStack initiates offline activation when the license server is unreachable, requiring re-activation every 24 hours.
Log output may indicate issues with your machine resolving the LocalStack API domain, which can be verified using a tool like `dig`:

{{< command >}}
$ dig api.localstack.cloud
{{< / command >}}

If the result shows a status other than `status: NOERROR`, your machine is unable to resolve this domain.
Certain corporate DNS servers may filter requests to specific domains.
Kindly reach out to your network administrator to safelist `localstack.cloud` domain.

If you have any further problems concerning your license activation, or if the steps do not help, do not hesitate to [contact us](https://localstack.cloud/contact/).
