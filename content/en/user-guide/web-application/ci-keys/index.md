---
title: "CI Keys"
linkTitle: "CI Keys"
weight: 40
description: >
  A CI key is used to access LocalStack in CI or other machine environments.
cascade:
  type: docs
---

The use of LocalStack in CI or other machine environments requires the use of a CI key.
Each start in a CI or other machine environment consumes 1 CI token.
A quota of these CI tokens is included in paid LocalStack plans.

CI keys are not intended to be used by individual developers.
To give a developer access to LocalStack and advanced features assign a license to them on the <a href=https://app.localstack.cloud/workspace/members>Users & Licenses</a> page.

{{< alert title="Note" >}}
We recently introduced auth tokens to replace _developer_ API keys. **CI keys** are unaffected by this transition and are still the only way to activate a LocalStack instance for use in CI or other automated contexts.
{{< /alert >}}

## Managing CI keys
CI keys are managed on the 'CI Keys' page.
CI keys are not assigned to a specific developer but are attributed to a specific CI pipeline or project.

<img src="ci-keys.png" alt="A screenshot of the LocalStack web app. The screenshot shows the page to manage CI keys" title="CI keys page" width="900" />

The top of the page shows the consumption of CI tokens in the current period.
A period lasts one month and the counter is reset at the start of each period.
The start and end dates of the current period are shown next to the graph.

The number of CI keys in a workspace is not limited, but all API keys count towards the same quota.

For easier tracking, we recommend to use a separate CI key for each project or CI pipeline.
To create a CI key, enter a descriptive name in the form field and press the 'Generate CI Key' button.

Existing CI keys can be renamed, rotated or deleted by selecting the action from the list.