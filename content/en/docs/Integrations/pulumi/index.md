---
title: "Pulumi"
tags: ["pulumi", "infrastructure-as-code"]
categories: []
date: 2021-09-29
weight: 10
description: >
  Use the Pulumi Infrastructure as Code framework with LocalStack
---

![Pulumi logo](pulumi-logo.svg)

## Overview

Pulumi's infrastructure-as-code SDK helps you create, deploy, and manage AWS containers, serverless functions, and infrastructure using familiar programming languages.
The endpoints configuration environment of Pulumi allows us to easily point Pulumi to LocalStack.
This guide follows the instructions from Pulumi's [Get Started with Pulumi and AWS](https://www.pulumi.com/docs/get-started/aws/) guide, with additional explanation of how to make it work with LocalStack.


## Quickstart

### Create a new Pulumi stack

First, run the following commands and follow the instructions in the CLI create a new project.

```
mkdir quickstart && cd quickstart
pulumi new aws-typescript
```

We use the default configuration values:

```
This command will walk you through creating a new Pulumi project.

Enter a value or leave blank to accept the (default), and press <ENTER>.
Press ^C at any time to quit.

project name: (quickstart) 
project description: (A minimal AWS TypeScript Pulumi program) 
Created project 'quickstart'

Please enter your desired stack name.
To create a stack in an organization, use the format <org-name>/<stack-name> (e.g. `acmecorp/dev`).
stack name: (dev) 
Created stack 'dev'

aws:region: The AWS region to deploy into: (us-east-1) 
Saved config

Installing dependencies...
```

This will create the following directory structure.

```language
 % tree -L 1
.
├── index.ts
├── node_modules
├── package.json
├── package-lock.json
├── Pulumi.dev.yaml
├── Pulumi.yaml
└── tsconfig.json
```

Now edit your stack configuration `Pulumi.dev.yaml` as follows:

```yaml
config:
  aws:accessKey: test
  aws:endpoints:
  - acm: http://localhost:4566
    amplify: http://localhost:4566
    apigateway: http://localhost:4566
    applicationautoscaling: http://localhost:4566
    appsync: http://localhost:4566
    athena: http://localhost:4566
    autoscaling: http://localhost:4566
    batch: http://localhost:4566
    cloudformation: http://localhost:4566
    cloudfront: http://localhost:4566
    cloudsearch: http://localhost:4566
    cloudtrail: http://localhost:4566
    cloudwatch: http://localhost:4566
    cloudwatchevents: http://localhost:4566
    cloudwatchlogs: http://localhost:4566
    codecommit: http://localhost:4566
    cognitoidentity: http://localhost:4566
    cognitoidp: http://localhost:4566
    docdb: http://localhost:4566
    dynamodb: http://localhost:4566
    ec2: http://localhost:4566
    ecr: http://localhost:4566
    ecs: http://localhost:4566
    eks: http://localhost:4566
    elasticache: http://localhost:4566
    elasticbeanstalk: http://localhost:4566
    elb: http://localhost:4566
    emr: http://localhost:4566
    es: http://localhost:4566
    firehose: http://localhost:4566
    glacier: http://localhost:4566
    glue: http://localhost:4566
    iam: http://localhost:4566
    iot: http://localhost:4566
    kafka: http://localhost:4566
    kinesis: http://localhost:4566
    kinesisanalytics: http://localhost:4566
    kms: http://localhost:4566
    lambda: http://localhost:4566
    mediastore: http://localhost:4566
    neptune: http://localhost:4566
    organizations: http://localhost:4566
    qldb: http://localhost:4566
    rds: http://localhost:4566
    redshift: http://localhost:4566
    route53: http://localhost:4566
    s3: http://localhost:4566
    sagemaker: http://localhost:4566
    secretsmanager: http://localhost:4566
    servicediscovery: http://localhost:4566
    ses: http://localhost:4566
    sns: http://localhost:4566
    sqs: http://localhost:4566
    ssm: http://localhost:4566
    stepfunctions: http://localhost:4566
    sts: http://localhost:4566
    swf: http://localhost:4566
    transfer: http://localhost:4566
    xray: http://localhost:4566
  aws:s3ForcePathStyle: 'true'
  aws:secretKey: test
  aws:skipCredentialsValidation: 'true'
  aws:skipRequestingAccountId: 'true'
```



### Deploy the stack to LocalStack

Make sure your LocalStack is running.
For the example stack the only required service is S3.
After updating the stack configuration, and starting localstack, you can run:

```bash
pulumi up
```

once the stack update was performed, you can run:

```bash
awslocal s3 ls
```

Where you should see something like

```
2021-09-30 11:50:59 my-bucket-6c21027
```

## Pulumilocal

`pulumilocal` is a wrapper script and drop-in replacement for the `pulumi` CLI, that also provides commands to better interface Pulumi with LocalStack.
You can find the source code repository here: https://github.com/localstack/pulumi-local

### Install

`pulumilocal` requires that you already have the `pulumi` command in your path.
Then, simply run

```bash
pip install pulumi-local
```

then,

```
pulumi version
pulumilocal version
```

should output the same value.

### Use

Instead of manually editing a stack configuration as explained earlier, you can run

```bash
pulumilocal init
```

which will create a `Pulumi.localstack.yaml` stack configuration, and initialize an additional stack named `localstack`.

You can now run

```bash
pulumilocal up
```

to start the localstack stack.


### Configuration

You can configure the integration between pulumi-local and LocalStack by adding these environment variables before running `pulumilocal`:

| Variable              | Default value | Description |
| --------------------- | ------------- | ------------|
| `PULUMI_CMD`          | pulumi        | The Pulumi command that is being delegated to |
| `PULUMI_STACK_NAME`   | localstack    | The Pulumi stack name used for looking up the stack file (`Pulumi.<stack>.yaml`) |
| `LOCALSTACK_HOSTNAME` | localhost     | The name of the host LocalStack is reachable at |
| `EDGE_PORT`           | 4566          | The port LocalStack is reachable at |
| `USE_SSL`             | 0             | A truthy (`1`, `true`) string that indicates whether to use SSL when connecting to LocalStack |


## Community resources

### Articles

* [Pulumi and LocalStack -- beyond the basics. 2021-08-26](https://delitescere.medium.com/pulumi-and-localstack-beyond-the-basics-d993f3b94d17)
* [How to deploy Localstack with Pulumi. 2020-09-22](https://overflowed.dev/blog/how-to-deploy-localstack-with-pulumi)


