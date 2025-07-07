# 📖 Parity Metrics Docs Update Report 📖
This PR has been automatically generated to update the AWS parity coverage docs.
It aggregates the latest parity coverage test results from our [test pipeline on GitHub](https://github.com/localstack/localstack/actions/workflows/aws-main.yml?query=branch%3Amaster) as well as from our Pro integration tests.

## 👷🏽 Handle this PR
The following options describe how to interact with this PR / the auto-update:

✔️ **Accept Changes**
If the changes are satisfying, just squash-merge the PR and delete the source branch.

🚫 **Ignore Changes**
If you want to ignore the changes in this PR, just close the PR and *do not delete* the source branch. The PR will not be opened and a new PR will not be created for as long as the generated code does not change (or the branch is deleted). As soon as there are new changes, a new PR will be created.

✏️ **Adapt Changes**
*Don't do this.* The APIs are auto-generated. If you decide that the APIs should look different, you have to change the code-generation.

⏸️ **Pause Updates**
Remove the cron-schedule trigger of the GitHub Action workflow which creates these PRs. The action can then still be triggered manually, but it will not be executed automatically.
