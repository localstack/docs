---
title: "AWS CDK"
linkTitle: "AWS CDK"
description: >
  Use the AWS CDK (Cloud Development Kit) with LocalStack
---

![AWS CDK](aws-cdk-logo.svg)
## Overview

The AWS Cloud Development Kit (CDK) is an Infrastructure-as-Code (IaC) tool using general-purpose programming languages such as TypeScript/JavaScript, Python, Java, and .NET to programmatically define your cloud architecture on AWS.

## AWS CDK CLI for LocalStack

`cdklocal` is a thin wrapper script for using the [AWS CDK](https://github.com/aws/aws-cdk) library against local APIs provided by [LocalStack](https://github.com/localstack/localstack).

### Installation

The `cdklocal` command line is published as an [npm library](https://www.npmjs.com/package/aws-cdk-local):

```bash
# Install globally
npm install -g aws-cdk-local aws-cdk

# Verify it installed correctly
cdklocal --version
# e.g. 1.65.5
```

{{< callout >}}
Using `cdklocal` locally (e.g. within the `node_modules` of your repo instead of globally installed) does not work at the moment for some setups, so make sure you install both `aws-cdk` and `aws-cdk-local` with the `-G` flag.
{{< /callout >}}

### Usage

`cdklocal` can be used as a drop-in replacement of where you would otherwise use `cdk` when targeting the AWS Cloud.

{{< command >}}
$ cdklocal --help
{{< /command >}}

### Configuration

The following environment variables can be configured:

* `AWS_ENDPOINT_URL`: The endpoint URL (i.e., protocol, host, and port) to connect to LocalStack (default: `http://localhost:4566`)
* `LAMBDA_MOUNT_CODE`: Whether to use local Lambda code mounting (via setting `hot-reload` S3 bucket name)


### Example

Make sure that LocalStack is installed and successfully started with the required services before running the example

{{< command >}}
$ curl http://localhost:4566/_localstack/health
{{< /command >}}

The CDK command line ships with a sample app generator to run a quick test for getting started.

```bash
# create sample app
mkdir /tmp/test; cd /tmp/test
cdklocal init sample-app --language=javascript

# bootstrap localstack environment
cdklocal bootstrap

# deploy the sample app
cdklocal deploy
> Do you wish to deploy these changes (y/n)? y
```

Once the deployment is done, you can inspect the created resources via the [`awslocal`](https://github.com/localstack/awscli-local) command line

{{< command >}}
$ awslocal sns list-topics
 {
     "Topics": [
         {
             "TopicArn": "arn:aws:sns:us-east-1:000000000000:TestStack-TestTopic339EC197-79F43WWCCS4Z"
         }
     ]
}
{{< /command >}}

## Current Limitations

### Updating CDK stacks

Updating CDK stacks may result in deployment failures and inconsistent state within LocalStack. It is advisable to prioritize re-creating (deleting and re-deploying) over updating stacks. Our focus for this year will be on resolving issues related to the `UPDATE` support, and continuous improvements can be anticipated in this area throughout 2024.

### Stacks with validated certificates

By default, stacks with validated certificates may not be deployed using the `local` lambda executor.
This originates from the way how CDK ensures the certificate is ready - it creates a single-file lambda function with a single dependency on `aws-sdk` which is usually preinstalled and available globally in lambda runtime.
When this lambda is executed locally from the `/tmp` folder, the package can not be discovered by Node due to the way how Node package resolution works.

## Other resources

- [Hot-reloading Lambda functions with CDK]({{< ref "user-guide/lambda-tools/hot-reloading#aws-cloud-development-kit-cdk-configuration" >}})

## External resources

- [aws-cdk-local](https://github.com/localstack/aws-cdk-local)
- [AWS CDK API reference](https://docs.aws.amazon.com/cdk/api/latest/docs/aws-construct-library.html)
- [AWS CDK Developer Guide](https://docs.aws.amazon.com/cdk/latest/guide/home.html)

## Community resources

- https://blog.dennisokeeffe.com/blog/2021-08-07-using-the-aws-cdk-with-localstack-and-aws-cdk-local
- https://www.youtube.com/watch?v=3_sqr0G9zb0
