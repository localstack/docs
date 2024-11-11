---
title: "Auth Token"
weight: 20
description: >
  Configure your Auth Token to access and activate LocalStack.
---
### Introduction

Auth tokens allow you to activate the LocalStack emulator and are also used access your workspace and additional services like Cloud Pods.

Auth tokens exist in 2 varieties.
A **personal developer Auth Token** and a **CI Auth Token:**

- The **developer Auth Token** is closely associated with a specific user in a specific workspace.
  Every user has an Auth Token.
  It can not be deleted, but it can be rotated for security purposes if required.
  It can be found on the [Auth Tokens page](https://app.localstack.cloud/workspace/auth-tokens)

- The **CI Auth Token** is not tied to a specific user and is intended for use in CI environments and other non developer related contexts.
  CI Auth Tokens live in the workspace, and can be managed by members with the necessary permissions.
  CI Auth Tokens can also be managed on the [Auth Tokens page](https://app.localstack.cloud/workspace/auth-tokens)

{{< callout "warning">}}
- It's crucial to keep your Auth Token confidential.
  Do not include it in source code management systems, such as Git repositories.
- Be aware that if an Auth Token is committed to a public repository, it is at risk of exposure, and could remain in the repository's history, even if attempts are made to rewrite it.
- In case your Auth Token is accidentally published, immediately rotate it on the [Auth Token page](https://app.localstack.cloud/workspace/auth-tokens).
{{< /callout >}}

## Activating LocalStack

To activate LocalStack Pro and to access additional services, simply set the Auth Token in the `LOCALSTACK_AUTH_TOKEN` environment variable.
This will make it also available to Docker/Docker Compose setups.

If you are only starting the LocalStack instance via the LocalStack CLI with `localstack start` then you can configure the Auth Token with `localstack auth set-token <YOUR_AUTH_TOKEN>`.

### Managing your License

To use LocalStack, a license is required.
You can get a license by registering on the [LocalStack Web Application](https://app.localstack.cloud/sign-up).
Choose between a 14-day trial or explore additional features with our paid offering.
During the trial period, you are welcome to use all the features of LocalStack.

After starting your trial or subscribing to a plan, you can manage the license assignments on the [Users & Licenses page](https://app.localstack.cloud/workspace/members):

## Configuring CI environments

CI environments are also configured the same way but **require the use of a CI Auth Token**. A developer Auth Token can not be used in CI.
CI Auth Tokens can also be found on the [Auth Tokens page](https://app.localstack.cloud/workspace/auth-tokens) page and are configured similarly to develop Auth Tokens.

## Activating older versions of localstack ( < v3.0)

Before Auth Tokens were introduced, _API keys_ and the `LOCALSTACK_API_KEY` environment variable were used.

To allow backwards compatibility with the new Auth Tokens, we updated our back-end so that a new Auth Token can be used inside the `LOCALSTACK_API_KEY` variable. Just use the new Auth Token and configure it as you did with the API key in the past.

### Sunsetting legacy API keys (early 2025)

In early 2025 we will start phasing out legacy API keys completely.
After the sunsetting period, it will not be able to activate and use legacy API and legacy CI keys with LocalStack.

During the sunsetting period, the legacy service will undergo scheduled downtimes.
This schedule will be designed to encourage the transition, but to limit the impact on users if they were not able to update yet.

The schedule will be communicated in advance, giving users enough time to make the switch to the new Auth Tokens.


