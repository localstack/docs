---
title: "GitHub Actions"
linkTitle: "GitHub Actions"
weight: 5
description: >
  Use LocalStack in GitHub Actions
---

## Introduction

GitHub Actions is a continuous integration and continuous delivery (CI/CD) platform which uses a configuration file (hosted in the `.github/workflows` directory) to define the build, test, and deployment workflows. LocalStack supports GitHub Actions out of the box and can be easily integrated into your pipeline to run your tests against a local cloud emulator. You can further use GitHub Actions to export and import your LocalStack container state and setup application previews using ephemeral instances. 

## Getting started

This guide is designed for users new to GitHub Actions and assumes basic knowledge of YAML and LocalStack tooling. To setup a GitHub Action job that uses LocalStack, create a new file in your repository under `.github/workflows/` with the name `localstack.yml`.

You can add the following configuration to the `localstack.yml` file to start LocalStack and run your tests against it:

```yml
name: LocalStack Test
on: [ push, pull_request ]

jobs:
  localstack-action-test:
    name: 'Test LocalStack GitHub Action'
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v3

      - name: Start LocalStack
        uses: LocalStack/setup-localstack@main
        with:
          image-tag: 'latest'
          install-awslocal: 'true'

      - name: Run Tests against LocalStack
        run: |
          awslocal s3 mb s3://test
          awslocal s3 ls
          echo "Test Execution complete!" 
```

The above configuration will start LocalStack using the [`setup-localstack` action](https://github.com/localstack/setup-localstack) and run the `awslocal` commands against it. You can add further steps to your build to run your tests against LocalStack.

## Configuration

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

## Configuring a CI key

To enable LocalStack Pro+, you need to add your LocalStack CI API key to the project's environment variables. The LocalStack container will automatically pick it up and activate the licensed features. 

Go to the [CI Key Page](https://app.localstack.cloud/workspace/ci-keys) page and copy your CI key. To add the CI key to your GitHub project, follow these steps:

- Navigate to your repository **Settings**, click **Secrets**, and press **New repository secret**.
- Enter `LOCALSTACK_AUTH_TOKEN` as the name of the secret and paste your CI key as the value.
- Click **Add secret** to save your secret.

<img src="github-create-secret.png" alt="Adding the LocalStack CI key as secret in GitHub" title="Adding the LocalStack CI key as secret in GitHub" width="900" />
<br>
<br>

Additionally, you need to modify your GitHub Action workflow to use the `localstack/localstack-pro` image and use the `LOCALSTACK_AUTH_TOKEN` environment variable. Here is an example:

```yml
- name: Start LocalStack
  uses: LocalStack/setup-localstack@main
  with:
    image-tag: 'latest'
    install-awslocal: 'true'
    configuration: DEBUG=1
    use-pro: 'true'
  env:
    LOCALSTACK_API_KEY: ${{ secrets.LOCALSTACK_API_KEY }}
```

## Limitations

### Running Lambdas targeting the `arm64` architecture

Deploying Lambdas targeting the `arm64` architecture on GitHub Actions can pose challenges. While the [`LAMBDA_IGNORE_ARCHITECTURE` configuration](https://docs.localstack.cloud/references/configuration/#lambda) is an option for cross-architecture compatible Lambdas, it may not be suitable for statically compiled Lambdas. To address this, users are recommended to leverage Docker's [`setup-qemu-action`](https://github.com/docker/setup-qemu-action) to enable emulation for the `arm64` architecture. It's important to note that using this approach may result in significantly slower build times.
