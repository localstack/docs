---
title: "Architect"
tags: ["architect", "infrastructure-as-code"]
weight: 5
description: >
  Use the Architect Infrastructure as Code framework with LocalStack
aliases:
  - /integrations/architect/
---

<img src="architect_logo.png" width="600px" alt="architect logo">

## Overview

Architect enables you to quickly build large serverless apps without worrying about the underlying infrastructure.
On this page we discuss how Architect and LocalStack can be used together.
If you are adapting an existing configuration, you might be able to skip certain steps at your own discretion.

## Example

### Setup
To use Architect in conjunction with LocalStack, simply install the `arclocal` command (sources can be found [here](https://github.com/localstack/architect-local)).
{{< command >}}
$ npm install -g architect-local @architect/architect aws-sdk
{{< /command >}}

The `arclocal` command has the same usage as the `arc` command, so you can start right away.

Create a test directory

{{< command >}}
$ mkdir architect_quickstart && cd architect_quickstart
{{< / command >}}

then create an architect project

{{< command >}}
$ arclocal init
{{< / command >}}

### Deployment

Now you need to start LocalStack. After LocalStack has started you can deploy your Architect setup via:
{{< command >}}
$ arclocal deploy
{{< / command >}}

## Further reading

For more architect examples, you can take a look at the [official architect docs](https://arc.codes).
