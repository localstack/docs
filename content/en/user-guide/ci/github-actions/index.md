---
title: "GitHub Actions"
linkTitle: "GitHub Actions"
weight: 5
description: >
  Use LocalStack in [GitHub Actions](https://docs.github.com/en/actions)
---

This page contains easily customisable snippets to show you how to manage LocalStack in a GitHub Actions pipeline.

## Snippets

### Start up Localstack

```yaml
- name: Start LocalStack
  uses: LocalStack/setup-localstack@v0.2.0
  with:
    image-tag: 'latest'
    install-awslocal: 'true'
```
### Configuration

To set LocalStack configuration options, you can use the `configuration` input parameter. For example, to set the `DEBUG` configuration option, you can use the following configuration:

```yml
- name: Start LocalStack
  uses: LocalStack/setup-localstack@v0.2.0
  with:
    image-tag: 'latest'
    install-awslocal: 'true'
    configuration: DEBUG=1
```

You can add extra configuration options by separating them with a comma.

### Configure a CI key

To enable LocalStack Pro+, you need to add your LocalStack CI API key to the project's environment variables. The LocalStack container will automatically pick it up and activate the licensed features. 

Go to the [CI Key Page](https://app.localstack.cloud/workspace/ci-keys) page and copy your CI key. To add the CI key to your GitHub project, follow these steps:

- Navigate to your repository **Settings > Secrets** and press **New repository secret**.
- Enter `LOCALSTACK_API_KEY` as the name of the secret and paste your CI key as the value. 
Click **Add secret** to save your secret.

<img src="github-create-secret.png" alt="Adding the LocalStack CI key as secret in GitHub" title="Adding the LocalStack CI key as secret in GitHub" width="900" />
<br>
<br>

Additionally, you need to modify your GitHub Action workflow to use the `localstack/localstack-pro` image and use the `LOCALSTACK_API_KEY` environment variable.

```yaml
- name: Start LocalStack
  uses: LocalStack/setup-localstack@v0.2.0
  with:
    image-tag: 'latest'
    install-awslocal: 'true'
    use-pro: 'true'
  env:
    LOCALSTACK_API_KEY: ${{ secrets.LOCALSTACK_API_KEY }}
```

### Dump Localstack logs
```yaml
- name: Show localstack logs
  run: |
    localstack logs | tee localstack.log
```

### Store Localstack state

You can preserve your AWS infrastructure with Localstack in various ways.

#### Cloud Pods
```yaml
...
# Localstack is up and running already
- name: Load the Cloud Pod 
  continue-on-error: true  # Allow it to fail as pod does not exist at first run
  uses: LocalStack/setup-localstack@v0.2.0
  with:
    state-backend: cloud-pods
    state-name: <cloud-pod-name>
    state-action: load
    skip-startup: 'true'

...

- name: Save the Cloud Pod 
  uses: LocalStack/setup-localstack@v0.2.0
  with:
    state-backend: cloud-pods
    state-name: <cloud-pod-name>
    state-action: save
...
```

Find more information about cloud pods [here](/user-guide/state-management/cloud-pods/).

#### Ephemeral Instance (Preview)

Our Github Action contains the prebuilt functionality to spin up an ephemeral instance.

First you need to deploy the preview:
```yaml
name: Create PR Preview

on:
  pull_request:
    types: [opened, synchronize, reopened]

jobs:
  test:
    runs-on: ubuntu-latest
    timeout-minutes: 15
    permissions:
      pull-requests: write
    steps:
      ...

      - name: Deploy Preview
        uses: LocalStack/setup-localstack@v0.2.0
        env:
          AWS_DEFAULT_REGION: us-east-1
          AWS_REGION: us-east-1
          AWS_ACCESS_KEY_ID: test
          AWS_SECRET_ACCESS_KEY: test
        with:
          state-backend: ephemeral
          state-action: start
          github-token: ${{ secrets.GITHUB_TOKEN }}
          skip-ephemeral-stop: 'true' # We want our instance keep running
          preview-cmd: bin/deploy.sh
```

Find out more about ephemeral instances [here](/user-guide/cloud-sandbox/).

#### Artifact
```yaml
...
- name: Start LocalStack and Load State
  uses: LocalStack/setup-localstack@v0.2.0
  continue-on-error: true  # Allow it to fail as pod does not exist at first run
  with:
    install-awslocal: 'true'
    state-backend: cloud-pods
    state-action: load
    state-name: my-ls-state
  env:
    LOCALSTACK_API_KEY: ${{ secrets.LOCALSTACK_API_KEY }}

...

- name: Save LocalStack State
  uses: LocalStack/setup-localstack@v0.2.0
  with:
    install-awslocal: 'true'
    state-backend: cloud-pods
    state-action: save
    state-name: my-ls-state
  env:
    LOCALSTACK_API_KEY: ${{ secrets.LOCALSTACK_API_KEY }}
...
```

More information about state import and export [here](/user-guide/state-management/export-import-state).

## Current Limitations

### Running Lambdas targeting the `arm64` architecture

Deploying Lambdas targeting the `arm64` architecture on GitHub Actions can pose challenges.
While the [`LAMBDA_IGNORE_ARCHITECTURE` configuration](https://docs.localstack.cloud/references/configuration/#lambda) is an option for cross-architecture compatible Lambdas, it may not be suitable for statically compiled Lambdas.
To address this, users are recommended to leverage Docker's [`setup-qemu-action`](https://github.com/docker/setup-qemu-action) to enable emulation for the `arm64` architecture.
It's important to note that using this approach may result in significantly slower build times.
