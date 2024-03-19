---
title: "Drone CI"
weight: 7
description: >
  Use LocalStack in [Drone CI](https://drone.io/)
---

This guide shows you how to start LocalStack in a Drone CI pipeline.

## Setting up your Drone CI pipeline

There are a few restrictions in Drone CI Pipelines that make it hard to customize the behavior of Docker. For example, mounting the host machine Docker socket is considered insecure, and hence alleviated privileges are required to run commands like `localstack wait`. Learn more about configuring Docker for Drone CI pipelines over [their official documentation](https://docs.drone.io/pipeline/docker/overview/).

A possible alternative to mounting the Docker socket (`/var/run/docker.sock`) into the container to communicate with the Docker daemon on the host is to expose port `2375` and make it reachable in the main LocalStack container. However, it requires changes to the typical Docker-Compose setup.

## Example

We can integrate the following example into your Drone CI workflow. As an example, it will pull the LocalStack Docker image and check if the LocalStack service is up and running:

```yml
kind: pipeline
type: docker
name: localstack

trigger:
  branch:
  - main

services:
- name: localstack
  image: localstack/localstack

steps:
- name: localstack wait
  image: alpine/curl:3.14
  commands:
  - until curl -s http://localstack:4566/_localstack/health; do echo -n . && sleep 1; done
```

## Configuring a CI key

You can easily enable LocalStack Pro by by using the `localstack/localstack-pro` image and adding your API key to Drone Repository secrets. You can manage them from your repository settings screen. Navigate to your Repository secrets on your Drone repository and add the LocalStack CI key as `localstack_ci_key`. Here is an example:

```yml
services:
- name: localstack
  image: localstack/localstack-pro
  environment:
    LOCALSTACK_API_KEY:
      from_secret: localstack_ci_key
```
