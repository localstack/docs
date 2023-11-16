---
title: "Auth Token"
weight: 20
description: >
  Configure your auth token to start LocalStack
---

LocalStack uses auth tokens to to authenticate users and to activate your LocalStack license.
You can find your auth token on the [Getting Started page in the web app](https://app.localstack.cloud/getting-started) or on the [Auth Token page](https://app.localstack.cloud/workspace/auth-token)

## Managing your License

To get started, you need to have a LocalStack license. If you don't have one, you can [sign up for a free trial](https://localstack.cloud/pricing/) without any credit card required. The free trial will last 14 days, and you can use it to test all the features of LocalStack.

You can assign licenses to users on the [Users & Licenses](https://app.localstack.cloud/workspace/members) page or you can check your assigned license on the [My License](https://app.localstack.cloud/workspace/my-license) page.


{{< alert title="Important" color="danger" >}}
- Avoid sharing your auth token with anyone. Ensure that you do not commit it to any source code management systems (like Git repositories).
- If you push an auth token to a public repository, it has potentially been exposed and might remain in the history (even if you try to rewrite it).
- If you accidentally publish your auth token, you can rotate it on the [Auth Token](https://app.localstack.cloud/workspace/auth-token) page
- Use in CI or other machine environments requires a CI key. Check out our [CI documentation]({{< ref "user-guide/ci" >}}) to see the proper way to handle secrets in your CI environment to store your CI key securely.
{{< /alert >}}

### Starting LocalStack via CLI

LocalStack expects your auth token to be present in the environment variable `LOCALSTACK_AUTH_TOKEN`. You can define the `LOCALSTACK_AUTH_TOKEN` environment variable before or while starting LocalStack using the `localstack` CLI.

{{< tabpane >}}
{{< tab header="macOS/Linux" lang="shell" >}}
export LOCALSTACK_AUTH_TOKEN=<YOUR_AUTH_TOKEN>
localstack start
{{< /tab >}}
{{< tab header="Windows" lang="powershell" >}}
$env:LOCALSTACK_AUTH_TOKEN="<YOUR_AUTH_TOKEN>"; localstack start
{{< /tab >}}
{{< /tabpane >}}

You can optionally run your LocalStack container in background mode by adding the `-d` flag to the `localstack start` command.

The `localstack` CLI will detect the auth token and properly pass it to the LocalStack container.

{{< alert title="Note" >}}
If you are using LocalStack with an auth token, you need to pull the [LocalStack Pro image](https://docs.localstack.cloud/references/docker-images/#localstack-pro-image) that includes the Pro services and several other advanced features.
{{< /alert >}}

### Starting LocalStack via Docker

To start LocalStack using Docker, you have to specify the auth token using the `-e` flag for environment variables:

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

You can set the auth token manually, or you can use the `export` command to set the auth token in your current shell session. The auth token will be passed into your LocalStack container, such that the key activation can take place.

## Licensing-related configuration

If you want to make sure that LocalStack is only started if you can activate LocalStack Pro or Enterprise, or if you wish to suppress licensing-related error messages, take a look at our [configuration guide]({{< ref "configuration.md#localstack-pro">}}) regarding LocalStack Pro.

## Checking license activation

The easiest way to check if LocalStack is activated is to query the health endpoint for a list of the running services:

{{< command >}}
$ curl localhost:4566/_localstack/health | jq
{{< / command >}}

If a Pro-only [service]({{< ref "aws" >}}) -- like [XRay]({{< ref "xray" >}}) -- is running, LocalStack has started successfully. You can also check the logs of the LocalStack container to see if the activation was successful.

{{< command >}}
[...] Successfully activated license
{{< / command >}}

Otherwise, check our collected most [common activation issues](#common-activation-issues).

## Common activation issues

Since LocalStack v2.0.0, the image `localstack/localstack-pro` requires a successful license activation to start.
If the license activation fails, LocalStack will quit with an error messages that may look something like this:

```
===============================================
License activation failed! 🔑❌

Reason: The credentials defined in your environment are invalid. Please make sure to either set the LOCALSTACK_AUTH_TOKEN variable to a valid auth token, or the LOCALSTACK_API_KEY variable to a valid LocalStack API key. You can find your auth token or API key in the LocalStack web app https://app.localstack.cloud.

Due to this error, Localstack has quit. LocalStack pro features can only be used with a valid license.

- Please check that your credentials are set up correctly and that you have an active license.
  You can find your credentials in our webapp at https://app.localstack.cloud.
- If you want to continue using LocalStack without pro features you can set `ACTIVATE_PRO=0`.
```

There are several reasons a key activation can fail:
* Missing credentials: Using `localstack/localstack-pro` requires per default to have an auth token or legacy API key set.
* Invalid license: there is no valid license associated with your user account, for example because the license has expired.
* License server cannot be reached: LocalStack will try to perform an offline license activation if the license server cannot be reached, but will require a re-activation every 24 hours.

If you are using the `localstack/localstack-pro` image, but cannot activate your license, we recommend falling back to the community version `localstack/localstack`.
If that is not an option, you can set `ACTIVATE_PRO=0` which will attempt to start LocalStack without pro features.

Navigate to our [FAQ page]({{< ref "faq" >}}) if your are having troubles with the LocalStack license activation.
If you have any further problems concerning your license activation, or if the steps do not help, do not hesitate to [contact us](https://localstack.cloud/contact/).
