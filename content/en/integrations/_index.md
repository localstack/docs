---
title: "Integrations"
linkTitle: "Integrations"
weight: 10
description: >
  How to use your favorite cloud development tools with LocalStack.
cascade:
  type: docs
---

LocalStack supports a wide range of tools from the cloud development ecosystem.
This section of the documentation covers tools that are officially supported by LocalStack.

## The Cloud Development Ecosystem

Cloud development has many facets and a rich ecosystem of tools to cover them.
Whether you are using Infrastructure-as-Code (IaC) to manage your AWS infrastructure,
or are developing applications using AWS SDKs like boto, LocalStack allows you to run your workflow completely on your local machine.

{{< figure src="integrations-overview.png" width="70%" alt="Sample of supported tools" >}}

## Integrations

We strive to make the integration of LocalStack into your workflow as seamless as possible.
Sometimes it's as easy as calling one of our wrapper tools, like `awslocal`, a drop-in replacement for the `aws` CLI.
Other times there is a bit of configuration involved.

Here is a list of tools we support, and documentation on how to integrate LocalStack:
