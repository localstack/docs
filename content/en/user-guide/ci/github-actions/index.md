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
  uses: LocalStack/setup-localstack@main
  with:
    image-tag: 'latest'
    install-awslocal: 'true'
```
### Configuration

To set LocalStack configuration options, you can use the `configuration` input parameter. For example, to set the `DEBUG` configuration option, you can use the following configuration:

```yml
- name: Start LocalStack
  uses: LocalStack/setup-localstack@main
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
  uses: LocalStack/setup-localstack@main
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

#### Artifact
```yaml
...
# Localstack is up and running already

- uses: actions/download-artifact@v4
  with:
    name: ls-state
  continue-on-error: true  # Allow it to fail as pod does not exist at first run

- name: Load the State
  env:
    LOCALSTACK_API_KEY: ${{ secrets.LOCALSTACK_API_KEY }}
  run: | 
    localstack state import ls-state.zip

...

- name: Save the State
  env:
    LOCALSTACK_API_KEY: ${{ secrets.LOCALSTACK_API_KEY }}
  run: | 
    localstack state export ls-state.zip

- uses: actions/upload-artifact@v4
  with:
    name: ls-state
    if-no-files-found: ignore
    path: ${{ github.workspace }}/ls-state.zip
    overwrite: true
...
```

More information about state import and export [here](/user-guide/state-management/export-import-state).

#### Cloud Pods
```yaml
...
# Localstack is up and running already
- name: Load the Cloud Pod 
  continue-on-error: true  # Allow it to fail as pod does not exist at first run
  uses: LocalStack/setup-localstack/cloud-pods@main
  with:
    name: <cloud-pod-name>
    action: load

...

- name: Save the Cloud Pod 
  uses: LocalStack/setup-localstack/cloud-pods@main
  with:
    name: <cloud-pod-name>
    action: save
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
        uses: LocalStack/setup-localstack/preview@main
        env:
          AWS_DEFAULT_REGION: us-east-1
          AWS_REGION: us-east-1
          AWS_ACCESS_KEY_ID: test
          AWS_SECRET_ACCESS_KEY: test
        with:
          github-token: ${{ secrets.GITHUB_TOKEN }}
          localstack-api-key: ${{ secrets.LOCALSTACK_API_KEY }}
          preview-cmd: |
            # Add your custom deployment commands here. 
            # Below is an example script which will run against the instance.
            bin/deploy.sh
```
And in a separate workflow add the counter part to comment the link on the Pull Request.

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
    permissions:
      pull-requests: write
    steps:
      - name: Finalize PR comment
        uses: LocalStack/setup-localstack/finish@main
        with:
          github-token: ${{ secrets.GITHUB_TOKEN }}
          include-preview: true
```

Find out more about ephemeral instances [here](/user-guide/cloud-sandbox/).

## Current Limitations

### Running Lambdas targeting the `arm64` architecture

Deploying Lambdas targeting the `arm64` architecture on GitHub Actions can pose challenges.
While the [`LAMBDA_IGNORE_ARCHITECTURE` configuration](https://docs.localstack.cloud/references/configuration/#lambda) is an option for cross-architecture compatible Lambdas, it may not be suitable for statically compiled Lambdas.
To address this, users are recommended to leverage Docker's [`setup-qemu-action`](https://github.com/docker/setup-qemu-action) to enable emulation for the `arm64` architecture.
It's important to note that using this approach may result in significantly slower build times.
