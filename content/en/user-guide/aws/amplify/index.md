---
title: "Amplify"
linkTitle: "Amplify"
categories: ["LocalStack Pro"]
description: >
  Get started with AWS Amplify on LocalStack
aliases:
  - /aws/amplify/
---

AWS Amplify is a JavaScript-based development framework that comprises libraries, UI components, and a standard CLI interface to build and deploy Web and Mobile applications. Amplify allows developers to build, deploy, and host static websites, single-page applications, and full-stack serverless web applications. Amplify is an abstraction over some popular AWS Services like DyanmoDB, Cognito, AppSync, Lambda, S3, and more.

LocalStack supports AWS Amplify via a thin wrapper script called `amplifylocal` for using the Amplify JS library against local APIs. The `amplifylocal` script is a drop-in replacement for the `amplify` CLI command and can configure and deploy AWS Amplify projects against LocalStack.

## Installation

The `amplifylocal` command line is published as an [npm library](https://www.npmjs.com/package/amplify-js-local):

{{< command >}}
$ npm install -g amplify-js-local @aws-amplify/cli
{{< /command >}}

{{< alert title="Note">}}
The dependency `@aws-amplify/cli` needs to be installed manually to decouple the two libraries, and allow using arbitrary versions of `@aws-amplify/cli` under the covers.
{{< /alert >}}

The version reported by `amplifylocal` represents the version of the underlying `@aws-amplify/cli` installation:

{{< command >}}
$ amplifylocal --version
4.41.0
{{< /command >}}

## Configurations

The following environment variables can be configured:

* `EDGE_PORT`: Port under which LocalStack edge service is accessible (default: `4566`)
* `LOCALSTACK_HOSTNAME`: Target host under which LocalStack edge service is accessible (default: `localhost`)

## Getting Started

In this getting started guide, you'll learn how to deploy a sample AWS Amplify application via CLI on LocalStack. This guide is intended for users who wish to get more acquainted with Amplify, and assumes you have installed `amplifylocal`. To get started, start your LocalStack instance using your preferred method:

1. Clone the [AWS Amplify sample application](https://github.com/aws-samples/aws-amplify-graphql) that demonstrates how to use GraphQL to build an application that a user can login to the system, then upload and download photos which are private to them.
   {{< command >}}
   $ git clone git@github.com:aws-samples/aws-amplify-graphql.git
   {{< /command >}}

2. Navigate to the `aws-amplify-graphql` directory and install the dependencies.
   {{< command >}}
   $ cd aws-amplify-graphql
   $ npm install
   {{< /command >}}

3. Initialize the Amplify project.
   {{< command >}}
   $ amplifylocal init

   ? Enter a name for the project awsamplifygraphql
   The following configuration will be applied:

   Project information
   | Name: awsamplifygraphql
   | Environment: dev
   | Default editor: Visual Studio Code
   | App type: javascript
   | Javascript framework: react
   | Source Directory Path: src
   | Distribution Directory Path: build
   | Build Command: npm run-script build
   | Start Command: npm run-script start

   ? Initialize the project with the above configuration? Yes
   Using default provider  awscloudformation
   {{< /command >}}

4. Add the authentication service to the project.
   {{< command >}}
   $ amplifylocal add auth
   {{< /command >}}

5. Add the API service to the project.
   {{< command >}}
   $ amplifylocal add api
   {{< /command >}}

6. Deploy the application over the mock AWS infrastructure created by LocalStack.
   {{< command >}}
   $ amplifylocal push
   {{< /command >}}

After the deployment is complete, you can inspect the created resources via the `awslocal` CLI:

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

## Using the Amplify JS Library

In addition to using the CLI, you should also be able to use the library in your local Node.js program or ES6 frontend code (e.g., React.js).

### Node.js Program (Backend)

{{< command >}}
// import and apply patches
const amplifyLocal = require('amplify-js-local/lib/index');
amplifyLocal.applyPatches();

// use regular amplify commands below (should automatically use the local endpoints)
...
{{< /command >}}

### ES6 JavaScript Code

{{< command >}}
import Amplify from 'aws-amplify';
import applyPatches from 'amplify-js-local/lib/es6';

// apply patches
applyPatches();

// configure Amplify
Amplify.configure(...);
{{< /command >}}
