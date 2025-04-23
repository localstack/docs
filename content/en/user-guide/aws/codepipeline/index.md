---
title: CodePipeline
linkTitle: CodePipeline
description: >
  Get started with CodePipeline on LocalStack
tags: ["Pro image"]
---

## Introduction

CodePipeline is a continuous integration/continuous delivery (CI/CD) service offered by AWS.
CodePipeline can be used to create automated pipelines that handle the build, test and deployment of software.

With LocalStack, you can create, manage and execute pipelines.
CodePipeline on LocalStack support a variety of actions that integrate with S3, CodeBuild and CodeConnections.

## Getting Started



## Actions

CodePipeline on LocalStack supports the following actions:

### S3 Source

The [S3 Source](https://docs.aws.amazon.com/codepipeline/latest/userguide/action-reference-S3.html) action is used to specify an S3 bucket object as input to the pipeline.

### S3 Deploy

The [S3 Deploy](https://docs.aws.amazon.com/codepipeline/latest/userguide/action-reference-S3Deploy.html) action is used to upload artifacts to a given S3 bucket as the output of the pipeline.

### CodeConnections Source

The [CodeConnections Source](https://docs.aws.amazon.com/codepipeline/latest/userguide/action-reference-CodestarConnectionSource.html) action is used to specify a VCS repo as the input to the pipeline.

Currently LocalStack supports integration with [GitHub](https://github.com/).
Please set the environment configuration option `CODEPIPELINE_GH_TOKEN` with the GitHub Personal Access Token to be able to fetch private repositories.

### CodeBuild Source and Test

The [CodeBuild Source and Test](https://docs.aws.amazon.com/codepipeline/latest/userguide/action-reference-CodeBuild.html) action can be used to start a CodeBuild container and run the given buildspec.

## Limitations

- [V2 pipeline types](https://docs.aws.amazon.com/codepipeline/latest/userguide/pipeline-types-planning.html) are not supported.
- [Rollbacks and stage retries](https://docs.aws.amazon.com/codepipeline/latest/userguide/pipelines-stages.html) are not available.
- [Triggers](https://docs.aws.amazon.com/codepipeline/latest/userguide/pipelines-triggers.html) are not implemented.
  Pipelines are executed only when [CreatePipeline](https://docs.aws.amazon.com/codepipeline/latest/APIReference/API_CreatePipeline.html) and [StartPipelineExecution](https://docs.aws.amazon.com/codepipeline/latest/APIReference/API_StartPipelineExecution.html) are invoked.
