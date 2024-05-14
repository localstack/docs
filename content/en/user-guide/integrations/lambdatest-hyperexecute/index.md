---
title: LambdaTest HyperExecute
linktitle: LambdaTest HyperExecute
description: Executing LocalStack tests on LambdaTest's HyperExecute
---

[HyperExecute](https://www.lambdatest.com/hyperexecute) is a test orchestration platform designed to optimize the execution of automated tests in the cloud. It supports a wide range of testing frameworks and integrates seamlessly with CI/CD pipelines, such as GitHub Actions. You can use HyperExecute to run your LocalStack tests on your local machine or in the CI pipeline using a single configuration file.

{{< callout >}}
LambdaTest provides specialized runners for LocalStack. The default runners don't provide a Docker socket, which is required for LocalStack to work properly. If you want to use LocalStack with HyperExecute, you need to get in touch with the LambdaTest team to get access to the specialized runners.
{{< /callout >}}

## Getting started

To get started with HyperExecute, you need to fulfill the following prerequisites:

- [HyperExecute CLI](https://www.lambdatest.com/support/docs/hyperexecute-cli-run-tests-on-hyperexecute-grid/)
- [GitHub Personal Access Token](https://docs.github.com/en/authentication/keeping-your-account-and-data-secure/managing-your-personal-access-tokens)
- [LambdaTest Account](https://hyperexecute.lambdatest.com/) and Access Key for HyperExecute (`he`)

### Configuring the HyperExecute environment

Create a new file named `he.yml` in the root directory of your project and add the following content:

```yaml
version: "0.1"
runson: linux
autosplit: true
parallelism: 2
concurrency: 2
scenarioCommandStatusOnly: true
runtime:
  language: python
  version: 3.10
pre:
  - pip install localstack awscli awscli-local
  - localstack start -d
  - localstack wait -t 60
  - awslocal s3 mb s3://test-bucket
  - awslocal sqs create-queue --queue-name test-queue
  - awslocal sns create-topic --name test-topic
```

The above minimal configuration file starts LocalStack and creates an S3 bucket, SQS queue, and SNS topic.

{{< callout >}}
To use the LocalStack Pro image, configure a LocalStack Auth Token by appending `LOCALSTACK_AUTH_TOKEN=${{ .secrets.LOCALSTACK_AUTH_TOKEN }}` to the `localstack start` command. Subsequently, you need to add your LocalStack Auth Token to your HyperExecute Portal as a secret.
{{< /callout >}}

### Enabling test execution on HyperExecute

To enable test execution on HyperExecute, you need to add the following content to your GitHub Actions workflow file:

```yaml
version: "0.1"
runson: linux
...
pre:
  ...
  - bin/deploy.sh
testDiscovery:
type: raw
mode: dynamic
command: pytest --co -q tests | sed '$d'
testRunnerCommand: pytest $test
sourcePayload:
  platform: git
  link: https://github.com/localstack-samples/sample-serverless-image-resizer-s3-lambda
  ref: main
  accessToken: ${{ .secrets.PAT }}
```

Before running the tests, add your Personal Access Token (PAT) to your HyperExecute Portal as a secret. In this minimal configuration, you will set up our [`Serverless image resizer`](https://github.com/localstack-samples/sample-serverless-image-resizer-s3-lambda) application and run the tests using `pytest`. The `bin/deploy.sh` script is responsible for deploying the application to LocalStack. HyperExecute will automatically detect the tests and run them in parallel.

### Running the tests locally

You can run the tests locally using the following command:

{{< command >}}
$ hyperexecute --user '<user-name>' --key '<HE-key>' --config he.yaml   
{{< /command >}}

Swap `<user-name>` and `<HE-key>` with your HyperExecute username and access key. You can find your access key in the HyperExecute Portal.

### Running the tests in the CI pipeline

In this example, we will use GitHub Actions to run the tests in the CI pipeline. To do so, you need to add the following content to your GitHub Actions workflow file in `.github/workflows/main.yml`:

```yaml
name: Running tests on HyperExecute

on:
  push:
    branches:
      - main
  pull_request:
    branches:
      - main

jobs:
  HE:
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v4
      - run: |
            wget https://downloads.lambdatest.com/hyperexecute/linux/hyperexecute
            chmod +x hyperexecute
            ./hyperexecute \
                --user {{ secrets.username }} \
                --key ${{ secrets.HE }} \
                --config he.yaml
```

Add your username and access key to your GitHub repository secrets. You can find your access key in the HyperExecute Portal. If you are using the LocalStack Pro image, you need to add your LocalStack Auth Token to your GitHub repository secrets.
