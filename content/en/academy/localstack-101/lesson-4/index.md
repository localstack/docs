---
title: "Getting started"
linkTitle: "Getting started"
weight: 4
description: >
  Discover multiple ways to dive into LocalStack's world of cloud development. Learn the easiest
  method using the LocalStack CLI, or alternatively, you can pull the Docker image, run it and start using AWS services. 
  Explore Docker and Docker Compose alternatives, plus discover advanced options like Docker Extension and Helm.
length: 07:01
leadimage: thumbnail.jpg
videoUrl: https://www.youtube.com/embed/SYCeM-Q6nRs
type: lessons
url: "/academy/localstack-101/getting-started/"
---

There are several LocalStack installation methods to kickstart your cloud development journey. 
Discover multiple pathways to initiate your LocalStack experience:

You'll understand the diverse approaches to LocalStack installation:

1. Quickstart with LocalStack CLI:
- Install `awscli-local` and `localstack` via `pip`, or, more recently, you can just use `brew` on macOS.
- Commence LocalStack using `localstack start [-d]`.
- Create a bucket and list buckets using `awslocal s3 mb s3://test` and `awslocal s3 ls`.
2. Alternative - Docker: Dive into an alternate installation method using Docker: pull the image and run it, it's that easy.
3. Docker Compose: Explore yet another approach via Docker Compose.

Further reading:

- [Getting Started with LocalStack](https://docs.localstack.cloud/overview/)
- [Better Understanding the Concepts of Image, Container, and Quickly Getting Started with Docker](https://docs.docker.com/get-started/)
- [What is AWS CLI](https://aws.amazon.com/cli/)
- [What is AWS CLI local](https://docs.localstack.cloud/user-guide/integrations/aws-cli/)
- [Pip Documentation](https://pypi.org/project/pip/)
- [Docker Compose Docs](https://docs.docker.com/get-started/08_using_compose/)



