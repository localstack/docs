---
title: "Creating infra with Terraform locally"
linkTitle: "Creating infra with Terraform locally"
weight: 4
description: >
  In this video we will be using LocalStack's terraform integration to automate the process of deploying and configuring the resources on localstack. For this we will be using `tflocal` - a small wrapper script to run Terraform against LocalStack. If you don’t want to use tflocal, you can use terraform, with small changes to the tf file, which we will talk about later in the video. 
length: 03:43
leadimage: getting-started.png
videoUrl: https://www.youtube.com/embed/CzX4mfiS058
type: lessons
url: "/academy/localstack-101/getting-started/"
---

There are several LocalStack installation methods to kickstart your cloud development journey. 
Discover multiple pathways to initiate your LocalStack experience:

You'll understand the diverse approaches to LocalStack installation:

1. Quickstart with LocalStack CLI:
- Install `awscli-local` and `localstack` via `pip install`. On macOS you can use `brew install`.
- Start LocalStack using `localstack start`.
- Create a bucket and list buckets using `awslocal s3 mb s3://test` and `awslocal s3 ls`.
1. Alternative - Docker: Dive into an alternate installation method using Docker: pull the image and run it, it's that easy.
2. Docker Compose: Explore yet another approach via Docker Compose.

Further reading:

- [Getting Started with LocalStack](https://docs.localstack.cloud/overview/)
- [Better Understanding the Concepts of Image, Container, and Quickly Getting Started with Docker](https://docs.docker.com/get-started/)
- [What is AWS CLI](https://aws.amazon.com/cli/)
- [What is AWS CLI local](https://docs.localstack.cloud/user-guide/integrations/aws-cli/)
- [Pip Documentation](https://pypi.org/project/pip/)
- [Docker Compose Docs](https://docs.docker.com/get-started/08_using_compose/)



