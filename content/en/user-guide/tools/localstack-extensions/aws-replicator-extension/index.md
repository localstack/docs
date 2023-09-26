---
title: "AWS Replicator"
linkTitle: "AWS Replicator"
weight: 1
description: A LocalStack extension that replicates AWS resources into your LocalStack container
---

AWS Replicator Extension is a LocalStack extension that allows you to replicate AWS resources into your LocalStack instance.

{{<alert title="Note">}}
This Extension is experimental and still under active development. Report any issues or feature requests on our [GitHub repository](https://github.com/localstack/localstack-extensions).
{{</alert>}}

## Installation

To install the CLI extension, use the following `pip` command:

{{< command >}}
$ pip install "git+https://github.com/localstack/localstack-extensions/#egg=localstack-extension-aws-replicator&subdirectory=aws-replicator"
{{< / command >}}

To install the Extension itself (server component running inside LocalStack), use the following `extensions` command:

{{< command >}}
$ localstack extensions install "git+https://github.com/localstack/localstack-extensions/#egg=localstack-extension-aws-replicator&subdirectory=aws-replicator"
{{< / command >}}

## Usage

This extension currently offers two modes of operation:

- AWS connection proxy
- Resource replicator CLI

### AWS Connection Proxy

The AWS connection proxy can be used to forward certain API calls in LocalStack to real AWS, in order to enable seamless transition between local and remote resources.

For example, in order to forward all API calls for DynamoDB/S3/Cognito to real AWS, the proxy can be started via the CLI as follows:

{{< command >}}
# configure terminal session to allow access to a real cloud account
$ export AWS_ACCESS_KEY_ID=... AWS_SECRET_ACCESS_KEY=...
# start proxy via the CLI
$ localstack aws proxy -s dynamodb,s3,cognito-idp
{{< / command >}}

{{< alert title="Warning" color="warning">}}
Be careful when using the proxy. Ensure to never give access to production accounts or any critical/sensitive data!
{{< /alert >}}

### Resource Replicator CLI

Resource Replicator CLI can be used to replicate the state, e.g., an SQS queue and the messages contained in it, from AWS into your LocalStack instance.

To use the resource replicator, make sure that you have access to AWS configured in your terminal. The extension will only talk to AWS in read-only mode, and will **not** make any changes to your real AWS account.

The following command can be used to replicate SQS queues (including their messages) into your LocalStack instance:

{{< command >}}
$ localstack aws replicate -s sqs
{{< / command >}}

Once the command has completed, you should be able to list and interact with the queue that was replicated into your local account:

{{< command >}}
$ awslocal sqs list-queues
...
$ awslocal sqs receive-message --queue-url ...
...
{{< / command >}}
