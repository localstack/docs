---
title: "CI Keys"
linkTitle: "CI Keys"
weight: 160
description: A CI key is used to access LocalStack in CI or other machine environments.
aliases:
  - /user-guide/ci/ci-keys/
---

LocalStack requires a **CI Key** for use in Continuous Integration (CI) or similar machine environments.
Each instance startup in a CI or comparable environment consumes one CI token.

CI Keys are administered on the [CI Keys page](https://app.localstack.cloud/workspace/ci-keys) of the LocalStack Web Application. These keys are linked to specific CI pipelines or projects, rather than individual developers.

<img src="ci-keys.png" alt="A screenshot of the LocalStack web app. The screenshot shows the page to manage CI keys" title="CI keys page" width="900" />

CI Keys are not meant for individual developers. To grant a developer access to LocalStack and its advanced features, assign a license to them on the [Users & Licenses page](https://app.localstack.cloud/workspace/members).

{{< callout >}}
We have recently introduced Auth Tokens to replace _developer_ API keys. However, this change does not affect **CI Keys**, which remain the sole method for activating a LocalStack instance in Continuous Integration (CI) or other automated test environments.
{{< /callout >}}

## Managing CI keys

To create a new CI key, input a meaningful name in the provided field and click the 'Generate CI Key' button. For better management, it's advisable to use a distinct CI key for each project or CI pipeline. You can manage existing CI keys by renaming, rotating, or deleting them through the options available in the list.

The top section of the CI page displays the usage of CI tokens for the current period. Each period lasts one month, and the token count resets at the beginning of a new period. The dates for the current period are indicated near the usage graph. While there's no limit to the number of CI keys a workspace can have, all the keys contribute to the same quota.
