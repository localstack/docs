---
title: "AWS CDK"
tags: ["cdk", "cloudformation", "infrastructure-as-code"]
categories: []
weight: 8
description: >
  Use the AWS CDK (Cloud Development Kit) with LocalStack
---

![AWS CDK](aws-cdk-logo.svg)
## Overview

The AWS Cloud Development Kit (CDK) is an IaC (Infrastructure-as-Code) tool using general-purpose programming languages such as TypeScript/JavaScript, Python, Java, and .NET to programmatically define your cloud architecture on AWS.

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

{{% alert title="Local node_modules" color="warning" %}}
Using `cdklocal` locally (e.g. within the `node_modules` of your repo instead of globally installed) does not work at the moment for some setups, so make sure you install both `aws-cdk` and `aws-cdk-local` with the `-G` flag.
{{% /alert %}}

### Usage

`cdklocal` can be used as a drop-in replacement of where you would otherwise use `cdk` when targeting the AWS Cloud.

{{< command >}}
$ cdklocal --help
{{< /command >}}
### Configuration


The following environment variables can be configured:

* `EDGE_PORT`: Port under which LocalStack edge service is accessible (default: `4566`)
* `LOCALSTACK_HOSTNAME`: Target host under which LocalStack edge service is accessible (default: `localhost`)
* `LAMBDA_MOUNT_CODE`: Whether to use local Lambda code mounting (via setting `__local__` S3 bucket name)


### Example

Make sure that LocalStack is installed and successfully started with the required services before running the example

{{< command >}}
$ curl http://localhost:4566/health
{{< /command >}}

The CDK command line ships with a sample app generator to run a quick test for getting started.

```bash
# create sample app
mkdir /tmp/test; cd /tmp/test
cdklocal init sample-app --language=javascript

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

## External resources

- [aws-cdk-local](https://github.com/localstack/aws-cdk-local)
- [AWS CDK API reference](https://docs.aws.amazon.com/cdk/api/latest/docs/aws-construct-library.html)
- [AWS CDK Developer Guide](https://docs.aws.amazon.com/cdk/latest/guide/home.html)

## Community resources

- https://blog.dennisokeeffe.com/blog/2021-08-07-using-the-aws-cdk-with-localstack-and-aws-cdk-local
- https://www.youtube.com/watch?v=3_sqr0G9zb0


