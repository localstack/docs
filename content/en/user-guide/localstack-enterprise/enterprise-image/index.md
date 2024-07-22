---
title: "Enterprise Image"
linkTitle: "Enterprise Image"
weight: 1
description: Custom LocalStack Enterprise image for offline or air-gapped environments with preferred configurations and packages.
tags: ["Enterprise plan"]
---

## Introduction

LocalStack offers an Enterprise image that allows offline usage and includes a customer-specific configuration.
This offline functionality is enabled by:

- Pre-installed packages required for running specific services that are usually downloaded on demand (such as `opensearch` or `dynamodb-local`).
- A certificate keypair for `localhost.localstack.cloud` to resolve to the LocalStack container via our DNS server.
- An embedded decryption key in the image, eliminating the need to contact the license server to operate LocalStack.

## How to use the image?

- After the image is pushed to the customer-specific ECR repository, the customer can pull and push it to their internal Docker registry.
- Developers within the customer’s network can then pull the image from this registry.
- To use the image from the command line interface (CLI), set the `IMAGE_NAME` configuration to the name of the Enterprise image, typically using the command:
    {{< command >}}
    $ IMAGE_NAME=localstack-enterprise localstack start
    {{< / command >}}
