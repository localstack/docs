---
title: "AWS Amplify"
linkTitle: "AWS Amplify"
categories: ["LocalStack Pro"]
tags:
- aws-amplify
- amplify
- amplifylocal
- amplify-plugin
- amplify-localstack
description: >
  Get started with AWS Amplify on LocalStack
aliases:
  - /aws/amplify/
---

## Introduction

AWS Amplify is a JavaScript-based development framework with libraries, UI components, and a standard CLI interface for building and deploying web and mobile applications. With Amplify, developers can build and host static websites, single-page applications, and full-stack serverless web applications using an abstraction layer over popular AWS services like DynamoDB, Cognito, AppSync, Lambda, S3, and more.

LocalStack supports AWS Amplify via a lightweight wrapper script called `amplifylocal` and an Amplify CLI Plugin. `amplifylocal` enables developers to use the Amplify JS library against LocalStack's emulated APIs, as a drop-in replacement for the standard `amplify` CLI command. The Amplify CLI plugin allows the `amplify` CLI tool to create resources directly on your local machine.

LocalStack supports Amplify via the Pro/Team offering, allowing you to use the Amplify APIs to build and test their Amplify applications locally. The supported APIs are available on our [API coverage page](https://docs.localstack.cloud/references/coverage/coverage_amplify/), which provides information on the extent of Amplify's integration with LocalStack.

## `amplifylocal` CLI

The `amplifylocal` CLI is a thin wrapper script for using the Amplify JS library against local AWS APIs provided by LocalStack.

### Installation

To install `amplifylocal`, simply install the [amplify-js-local](https://www.npmjs.com/package/amplify-js-local) package from the npm registry:

{{< command >}}
$ npm install -g amplify-js-local @aws-amplify/cli
{{< /command >}}

{{< alert title="Note">}}
Note that you also need to install the `@aws-amplify/cli` package manually to ensure decoupling of the two libraries and allow the use of arbitrary versions of `@aws-amplify/cli` under the covers.
{{< /alert >}}

You can check the version of the underlying `@aws-amplify/cli` installation used by `amplifylocal` by running:

{{< command >}}
$ amplifylocal --version
{{< /command >}}

This will return the version number of the installed `@aws-amplify/cli` package.

### Configuration

You can configure the following environment variables to customize LocalStack's behaviour:

- `EDGE_PORT`: The port under which LocalStack's edge service is accessible (default: `4566`).
- `LOCALSTACK_HOSTNAME`: The target host under which LocalStack's edge service is accessible (default: `localhost`).

## Getting Started

This guide provides step-by-step instructions on deploying a sample AWS Amplify application using the `amplifylocal` CLI on LocalStack. The guide assumes that you have already installed `amplifylocal`. Before you begin, ensure that you have started your LocalStack container using your preferred method.

Clone the [AWS Amplify sample application](https://github.com/aws-samples/aws-amplify-graphql), demonstrating how to use GraphQL to build an application that allows users to log in to the system, upload and download private photos.

{{< command >}}
$ git clone git@github.com:aws-samples/aws-amplify-graphql.git
{{< /command >}}

Navigate to the `aws-amplify-graphql` directory and install the dependencies.

{{< command >}}
$ cd aws-amplify-graphql
$ npm install
{{< /command >}}

Initialize the Amplify project. You will be prompted to enter a project name and select project configurations. Once you have entered your preferred configurations, you can initialize the project.

{{< command >}}
$ amplifylocal init
{{< /command >}}

Add the authentication service to the project.

{{< command >}}
$ amplifylocal add auth
{{< /command >}}

Add the API service to the project.

{{< command >}}
$ amplifylocal add api
{{< /command >}}

Deploy the application over the emulated AWS infrastructure created by LocalStack.

{{< command >}}
$ amplifylocal push
{{< /command >}}

Once the deployment is complete, you can inspect the created resources using the `awslocal` CLI. This will display a list of created resources including name, API ID, authentication type, ARN, and URIs.

{{< command >}}
$ awslocal appsync list-graphql-apis
{
    "graphqlApis": [
        {
            "name": "awsamplifygraphql-dev",
            "apiId": "1a6f1f11",
            "authenticationType": "API_KEY",
            "arn": "arn:aws:appsync:us-east-1:000000000000:apis/1a6f1f11",
            "uris": {
                "GRAPHQL": "http://localhost:4566/graphql/1a6f1f11",
                "REALTIME": "ws://localhost:4510/graphql/1a6f1f11"
            }
        },
    ...
{{< /command >}}

### Amplify JS Library

In addition to the `amplifylocal` CLI, you can use the Amplify JS library in your local Node.js programs or ES6 frontend code, such as React.js.

#### Node.js Program (Backend)

To use Amplify in your Node.js program, import and apply the patches as shown below:

```js
const amplifyLocal = require('amplify-js-local/lib/index');
amplifyLocal.applyPatches();
```

You can then use the regular Amplify commands, which should automatically use the local endpoints.

#### ES6 JavaScript Code

To use Amplify in your ES6 JavaScript code, first import Amplify and the `applyPatches` function as shown below:

```js
import Amplify from 'aws-amplify';
import applyPatches from 'amplify-js-local/lib/es6';

// apply patches
applyPatches();

// configure Amplify
Amplify.configure(...);
```

## Amplify LocalStack Plugin

Amplify LocalStack Plugin allows the `amplify` CLI tool to create resources on your local machine instead of AWS. It achieves this by redirecting any requests to AWS to a LocalStack container running locally on your machine.

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
