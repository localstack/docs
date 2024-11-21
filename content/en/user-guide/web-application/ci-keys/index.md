---
title: "CI Keys (Deprecated)"
linkTitle: "CI Keys (Deprecated)"
weight: 160
description: A CI Key is used to access LocalStack in CI or other machine environments.
aliases:
  - /user-guide/ci/ci-keys/
---

{{< callout "warning">}}
LocalStack CI Keys are now deprecated, and the option to issue or retrieve a CI Key has been removed from the LocalStack Web Application.
Users are advised to switch to **CI Auth Tokens**, which are designed for use in CI environments and other non-developer contexts.
CI Auth Tokens can be managed on the [Auth Tokens page](https://app.localstack.cloud/workspace/auth-tokens).

To migrate to CI Auth Tokens, follow these steps:

1. Retrieve your CI Auth Token from the [Auth Tokens page](https://app.localstack.cloud/workspace/auth-tokens).
2. Remove the existing CI key labeled as `LOCALSTACK_API_KEY` from your CI provider's secrets.
3. Enter the Auth Token value into the `LOCALSTACK_AUTH_TOKEN` environment variable of your CI provider.

In early 2025, we will completely phase out legacy CI keys.
After the sunsetting period, legacy CI keys will no longer activate or function with LocalStack.
{{< /callout >}}

## Introduction

LocalStack requires a **CI Key** for use in Continuous Integration (CI) or similar machine environments.
Each instance startup in a CI or comparable environment consumes one CI token.

CI Keys are administered on the [CI Keys page](https://app.localstack.cloud/workspace/ci-keys) of the LocalStack Web Application.
These keys are linked to specific CI pipelines or projects, rather than individual developers.

CI Keys are not meant for individual developers.
To grant a developer access to LocalStack and its advanced features, assign a license to them on the [Users & Licenses page](https://app.localstack.cloud/workspace/members).

{{< callout >}}
We have recently introduced Auth Tokens to replace _developer_ API keys.
However, this change does not affect **CI Keys**, which remain the sole method for activating a LocalStack instance in Continuous Integration (CI) or other automated test environments.
{{< /callout >}}

## Managing CI keys

To create a new CI key, input a meaningful name in the provided field and click the 'Generate CI Key' button.
For better management, it's advisable to use a distinct CI key for each project or CI pipeline.
You can manage existing CI keys by renaming, rotating, or deleting them through the options available in the list.

The top section of the CI page displays the usage of CI tokens for the current period.
Each period lasts one month, and the token count resets at the beginning of a new period.
The dates for the current period are indicated near the usage graph.
While there's no limit to the number of CI keys a workspace can have, all the keys contribute to the same quota.
