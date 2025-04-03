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
