---
title: "Pulumi"
tags: ["pulumi", "infrastructure-as-code"]
categories: ["Stub"]
date: 2021-09-29
weight: 10
description: >
  Use the Pulumi Infrastructure as Code framework with LocalStack
---

## Overview


## Pulumilocal

`pulumilocal` is a wrapper script around the `pulumi` CLI that interfaces Pulumi with LocalStack.
You can find the source code repository here: https://github.com/localstack/pulumi-local


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


