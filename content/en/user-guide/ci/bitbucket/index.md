---
title: "BitBucket"
linkTitle: "BitBucket"
weight: 5
description: >
  Use LocalStack in BitBucket Pipelines
---

## Introduction

[BitBucket Pipeline](https://bitbucket.org/product/features/pipelines) is a CI/CD tool that allows you to build, test, and deploy your code directly from BitBucket. This guide will show you how to use LocalStack in BitBucket Pipelines.

## Setting up the BitBucket Pipeline

When you want to integrate LocalStack into your job configuration, you just have to execute the following steps:

- Specify the Docker Socket to allow the LocalStack container to access the Docker daemon.
- Export the `AWS_ENDPOINT_URL` environment variable to point to the LocalStack endpoint.
- Install the `localstack` CLI and `awscli-local` to interact with LocalStack's emulated services.
- Start the LocalStack container in detached mode by specifying the Docker Socket and Docker Host.

The following example BitBucket Pipeline configuration (`bitbucket-pipelines.yaml`) executes these steps, creates a new S3 bucket, and queries the list of S3 buckets:

```yaml
image: python:3.9

definitions:
  services:
    docker:
      memory: 2048

pipelines:
  default:
    - step:
        name: Test Localstack
        services:
          - docker
        script:
          - export PYTHONPATH=$PYTHONPATH:$(pwd)
          - export DOCKER_SOCK=$DOCKER_HOST
          - export AWS_ENDPOINT_URL="http://localhost.localstack.cloud:4566"
          - env
          - echo "${BITBUCKET_DOCKER_HOST_INTERNAL} localhost.localstack.cloud " >> /etc/hosts
          - pip install localstack awscli-local
          - |
            curl "https://awscli.amazonaws.com/awscli-exe-linux-x86_64.zip" -o "awscliv2.zip"
            unzip awscliv2.zip
            ./aws/install
          - docker run -d --rm -p 4566:4566 -p 4510-4559:4510-4559 -e DOCKER_SOCK=tcp://${BITBUCKET_DOCKER_HOST_INTERNAL}:2375 -e DOCKER_HOST=tcp://${BITBUCKET_DOCKER_HOST_INTERNAL}:2375 --name localstack-main localstack/localstack
          - localstack wait -t 60
          - awslocal s3 mb s3://test-bucket
          - awslocal s3 ls
```

## Configuring a CI key

You can enable LocalStack Pro by using the `localstack/localstack-pro` image and adding your CI key to the project's environment variables. The LocalStack container will automatically pick it up and activate the Pro features.

To add a CI key to your BitBucket Pipeline:

- Select a workspace from the BitBucket dashboard.
- Select the **Settings** on the top navigation bar.
- Select **Workspace settings** from the **Settings dropdown** menu.
- On left-hand menu, navigate to **Pipelines** and click on **Workspace variables**.
- Add a new variable with the name `LOCALSTACK_API_KEY` and the value of your CI key.

Navigate to your BitBucket Pipeline and add the following lines to the `bitbucket-pipelines.yaml` file:

```yaml
pipelines:
  default:
    - step:
        name: Test Localstack
        services:
          - docker
        script:
          ...
          - export LOCALSTACK_AUTH_TOKEN=$LOCALSTACK_AUTH_TOKEN
          ...
          - docker run -d --rm -p 4566:4566 -p 4510-4559:4510-4559 -e LOCALSTACK_AUTH_TOKEN=${LOCALSTACK_AUTH_TOKEN:?} -e DEBUG=1 -e LS_LOG=trace -e DOCKER_SOCK=tcp://${BITBUCKET_DOCKER_HOST_INTERNAL}:2375 -e DOCKER_HOST=tcp://${BITBUCKET_DOCKER_HOST_INTERNAL}:2375 --name localstack-main localstack/localstack-pro
          ...
```
## Current Limitations

### Mounting Volumes

BitBucket Pipelines does not support mounting volumes, so you cannot mount a volume to the LocalStack container. This limitation prevents you from mounting the Docker Socket to the LocalStack container, which is required to create compute resources, such as Lambda functions or ECS tasks.
