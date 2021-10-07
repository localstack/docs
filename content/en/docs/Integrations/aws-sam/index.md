---
title: "AWS SAM"
tags: ["sam", "cloudformation", "infrastructure-as-code"]
categories: []
weight: 7
description: >
  Use the AWS SAM (Serverless Application Model) with LocalStack
---

![AWS SAM](aws-sam-logo.jpg)

## Overview

The AWS Serverless Application Model (SAM) is a framework on top of CloudFormation to quickly develop Cloud Applications with a focus on serverless services such as S3, Lambda, API Gateway, Step Functions and more.

## AWS SAM CLI for LocalStack

To deploy SAM applications on [LocalStack](https://github.com/localstack/localstack) you can use [samlocal](https://github.com/localstack/aws-sam-cli-local), a wrapper for the [AWS SAM CLI](https://github.com/aws/aws-sam-cli).

### Installation

Simply use `pip` to install `samlocal` as a Python library on your machine:

{{< command >}}
$ pip install aws-sam-cli-local
{{< / command >}}

### Usage

The `samlocal` command has the exact same usage as the underlying `sam` command. The main difference is that for commands like `samlocal deploy` the operations will be executed against the LocalStack endpoints (`http://localhost:4566` by default) instead of real AWS endpoints.

{{< command >}}
$ samlocal --help
{{< / command >}}

### Configuration

* `EDGE_PORT`: Port number under which the LocalStack edge service is available (default: `4566`)
* `LOCALSTACK_HOSTNAME`: Host under which the LocalStack edge service is available (default: `localhost`)
