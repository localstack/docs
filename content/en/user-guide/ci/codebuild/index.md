---
title: "CodeBuild"
linkTitle: "CodeBuild"
weight: 5
description: Use LocalStack in CodeBuild
---

## Introduction

CodeBuild is a managed AWS service for the build and testing phases of software development. CodeBuild allows you to define your build project, set the source code location, and handles the building and testing, while supporting various programming languages, build tools, and runtime environments. LocalStack supports CodeBuild out of the box and can be easily integrated into your pipeline to run your tests against a cloud emulator.

## Getting started

This guide is designed for users new to CodeBuild and assumes basic knowledge of YAML and LocalStack tooling. In this guide, we will show you how to set up a CodeBuild project that uses LocalStack to run basic S3 tests against it.

### Configure your CodeBuild project

Navigate to the AWS Management Console and open the CodeBuild console at [https://console.aws.amazon.com/codesuite/codebuild/home](https://console.aws.amazon.com/codesuite/codebuild/home).

Click on **Create build project**. In the **Create build project** page, enter the following details:

- **Project name**: Enter a name for your build project.
- **Source**: Select the source code provider and repository details. For this example, we will use the the **No Source** option.
- **Operating system**: Select the operating system for your build environment. For this example, we will use **Ubuntu**.
- **Runtime**: Select the runtime for your build environment. For this example, we will use **Standard**.
- **Image**: Select the image for your build environment. For this example, we will use **aws/codebuild/standard:7.0**.
- **Service Role**: Select the service role for your build environment. For this example, we will use the **New service role** option.
- **Additional Configuration**: Click on it and select **Enable this flag if you want to build Docker images or want your builds to get elevated privileges** under the **Privileges** section.
- **Buildspec**: Select **Insert build commands** and add `uname -a` to the build commands for testing purposes.
- **Logs**: Select **CloudWatch** for the logs.

Click on **Create build project** to create your build project.

### Configure your buildspec file

On the project dashboard, click on **Edit** to open the dropdown and select **Buildspec**. On the **Edit Buildspec** page, enter the following build commands:

```yml
version: 0.2

phases:
  pre_build:
    commands:
      - pip3 install localstack awscli
      - docker pull public.ecr.aws/localstack/localstack:latest	
      - localstack start -d
      - localstack wait -t 30
  build:
    commands:
      - export AWS_ACCESS_KEY_ID="test"
      - export AWS_SECRET_ACCESS_KEY="test"
      - export AWS_DEFAULT_REGION="us-east-1"
      - docker ps
      - localstack logs
      - curl http://0.0.0.0:4566/_localstack/health | jq
      - aws s3 mb s3://test --endpoint-url=http://0.0.0.0:4566
      - aws s3 ls --endpoint-url=http://0.0.0.0:4566
```

Click on **Update buildspec** to save your buildspec file.

{{< alert title="Note">}}
In the above buildspec file, we are using the `public.ecr.aws/localstack/localstack:latest` image to start LocalStack, instead of the `localstack/localstack:latest` image. LocalStack mirrors the Docker Hub image to the public ECR repository. You can use the Docker Hub image as well, though you may run into the following error:
```bash
toomanyrequests: You have reached your pull rate limit. You may increase the limit by authenticating and upgrading: https://www.docker.com/increase-rate-limit
```
{{< /alert >}}

### Start your build

Click on **Start build** to start your build. After the build is complete, you can view the build logs and the build status.

```bash
[Container] 2024/02/07 09:19:25.791565 Running command aws s3 mb s3://test --endpoint-url=http://0.0.0.0:4566
make_bucket: test

[Container] 2024/02/07 09:19:26.849784 Running command aws s3 ls --endpoint-url=http://0.0.0.0:4566
2024-02-07 09:19:26 test

[Container] 2024/02/07 09:19:27.305446 Phase complete: BUILD State: SUCCEEDED
[Container] 2024/02/07 09:19:27.305465 Phase context status code:  Message: 
[Container] 2024/02/07 09:19:27.343546 Entering phase POST_BUILD
[Container] 2024/02/07 09:19:27.345126 Phase complete: POST_BUILD State: SUCCEEDED
[Container] 2024/02/07 09:19:27.345139 Phase context status code:  Message: 
```

## Configuring a CI key

To enable LocalStack Pro+, you need to add your LocalStack CI API key to the project's environment variables. The LocalStack container will automatically pick it up and activate the licensed features.

Go to the [CI Key Page](https://app.localstack.cloud/workspace/ci-keys) page and copy your CI key. To add the CI key to your CodeBuild project, follow these steps:

- Navigate to your project dashboard, click **Edit** to open the dropdown, and select **Environment**.
- Click on **Additional configuration** and navigate to the **Environment variables** section.
- Specify **Name** as `LOCALSTACK_API_KEY` and **Value** as your CI key. Specify **Type** as per your requirement.

Click on **Update environment** to save your environment variables. Navigate to the buildspec file and change the Docker image to `public.ecr.aws/localstack/localstack-pro:latest`:

```bash
...
phases:
  pre_build:
    commands:
      - pip3 install localstack awscli
      - docker pull public.ecr.aws/localstack/localstack-pro:latest	
...
```
