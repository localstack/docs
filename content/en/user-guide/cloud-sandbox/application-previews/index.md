---
title: "Application Preview"
linkTitle: "Application Preview"
weight: 2
description: Create an Application Preview to deploy your application changes in an Ephemeral Instance
---

## Introduction

Application Preview allows you to generate an preview environment from GitHub Pull Request (PR) builds. You can use Application Preview to temporarily deploy your AWS-powered application to a LocalStack Ephemeral Instance and preview your application changes. Currently, the Application Preview are only supported for GitHub repositories using GitHub Actions.

{{< callout >}}
Application Preview is currently available on invite-only preview.
If you'd like to try it out, please [contact us](https://www.localstack.cloud/demo) to request access.
{{< /callout >}}

## Getting started

This guide is designed for users new to Application Preview and assumes basic knowledge of GitHub Actions. We will configure a CI pipeline that runs on pull requests using GitHub Actions.

To get started with a ready-to-use template, you can fork the [`bref-localstack-sample`](https://github.com/localstack-samples/bref-localstack-sample) repository. The sample application deploys a serverless PHP application using Bref and the Serverless Framework.

### Prerequisites

- [LocalStack Account](https://app.localstack.cloud/)
- [GitHub Account](https://github.com)

### Create the Application Preview

To create an Application Preview, you can use the [`LocalStack/setup-localstack/ephemeral/startup` action](https://github.com/localstack/setup-localstack).

The sample repository has been configured to use the workflow described above. For your custom repository, create a new file named `ci-pipeline.yml` in the `.github/workflows` directory. This file will contain the CI pipeline that runs on every pull request. This pipeline deploys the application to a LocalStack Ephemeral Instance.

The workflow file to create the Application Preview looks like this:

```yaml
name: Create PR Preview

on:
  pull_request:
    types: [opened, synchronize, reopened]

jobs:
  test:
    runs-on: ubuntu-latest
    timeout-minutes: 15
    steps:
      - name: Checkout
        uses: actions/checkout@v4

      - name: Deploy Preview
        uses: LocalStack/setup-localstack@v0.2.0
        with:
          github-token: ${{ secrets.GITHUB_TOKEN }}
          localstack-api-key: ${{ secrets.LOCALSTACK_API_KEY }}
          preview-cmd: |
            # Add your custom deployment commands here. 
            # Below is an example for the Bref Serverless application.
            export AWS_DEFAULT_REGION=us-east-1
            npm install --include=dev
            npm run build
            composer require bref/bref
            mv .env.example .env
            php artisan key:generate
            npm run serverless -- deploy --stage dev

            pip install awscli-local[ver1]
            apiId=$(awslocal apigatewayv2 get-apis| jq -r '.Items[0].ApiId')
            echo "Open URL: $AWS_ENDPOINT_URL/restapis/$apiId/dev/_user_request_/"
```

You will also need to configure the `LOCALSTACK_API_KEY` as a repository secret. You can find the API key on the [LocalStack Web Application](https://app.localstack.cloud/account/apikeys). The `GITHUB_TOKEN` is automatically created by GitHub and you can use it without any additional configuration.

### Attach the Preview URL

You can now attach the Preview URL to the pull request by using the [`LocalStack/setup-localstack/finish` action](https://github.com/localstack/setup-localstack).

The sample repository has been configured to use the workflow described above. For your custom repository, create a new file named `ci-finalize.yml` in the `.github/workflows` directory. This file contains the CI pipeline that attaches a comment to the pull request with the Preview URL of the deployed application.

The workflow file to attach the Preview URL looks like this:

```yaml
name: Finalize PR Preview

on:
  workflow_run:
    workflows: ["Create PR Preview"]
    types:
      - completed

jobs:
  test:
    runs-on: ubuntu-latest
    steps:
      - name: Finalize PR comment
        uses: LocalStack/setup-localstack/finish@v0.2.0
        with:
          github-token: ${{ secrets.GITHUB_TOKEN }}
          include-preview: true
```

### Open a Pull Request

Once your changes are in your repository, open a new pull request. GitHub will receive the request and trigger your workflow. You can track the workflow's status and logs in the **Checks** section of the pull request.

After a short delay, the workflow will update the pull request with the URL of your preview environment. Just click on it to see the changes in real-time.

Each time the branch is updated, the same workflow will automatically refresh the preview environment.
