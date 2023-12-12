---
title: "Amplify"
linkTitle: "Amplify"
description: >
  Get started with Amplify on LocalStack
---

## Introduction

Amplify is a JavaScript-based development framework with libraries, UI components, and a standard CLI interface for building and deploying web and mobile applications. With Amplify, developers can build and host static websites, single-page applications, and full-stack serverless web applications using an abstraction layer over popular AWS services like DynamoDB, Cognito, AppSync, Lambda, S3, and more.

LocalStack supports Amplify via the Pro/Team offering, allowing you to use the Amplify APIs to build and test their Amplify applications locally. The supported APIs are available on our [API coverage page](https://docs.localstack.cloud/references/coverage/coverage_amplify/), which provides information on the extent of Amplify's integration with LocalStack.

{{< alert title="Note" >}}
The `amplifylocal` CLI and the Amplify JS library have been deprecated and are no longer supported. We recommend using the Amplify CLI with the Amplify LocalStack Plugin instead.
{{< /alert >}}

## Amplify LocalStack Plugin

[Amplify LocalStack Plugin](https://github.com/localstack/amplify-localstack) allows the `amplify` CLI tool to create resources on your local machine instead of AWS. It achieves this by redirecting any requests to AWS to a LocalStack container running locally on your machine.

### Installation

To install the Amplify LocalStack Plugin, install the [amplify-localstack](https://www.npmjs.com/package/amplify-localstack) package from the npm registry and add the plugin to your Amplify setup:

{{< command >}}
$ npm install -g amplify-localstack
$ amplify plugin add amplify-localstack
{{< /command >}}

### Configuration

You can configure the following environment variables to customize LocalStack's behaviour:

- `EDGE_PORT`: The port number under which the LocalStack edge service is accessible. The default value is `4566`.
- `LOCALSTACK_HOSTNAME`: It specifies the target host under which the LocalStack edge service is accessible. The default value is `localhost.localstack.cloud`.
- `LOCALSTACK_ENDPOINT`: It allows you to set a custom endpoint directly. If set, it overrides the values set for `EDGE_PORT` and `LOCALSTACK_HOSTNAME`. The default value is `https://localhost.localstack.cloud:4566`.

### Usage

After installing the plugin, you can deploy your resources to LocalStack using the `amplify init` or `amplify push` commands. The console will prompt you to select whether to deploy to LocalStack or AWS.

You can also add the parameter `--use-localstack true` to your commands to avoid being prompted and automatically use LocalStack. Here is an example:

{{< command >}}
$ amplify init --use-localstack true
$ amplify add api
$ amplify push --use-localstack true
{{< /command >}}
