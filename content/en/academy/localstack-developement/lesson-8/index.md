---
title: "Cloud pods - Team Collaboration"
linkTitle: "Cloud pods - Team Collaboration"
weight: 8
description: >
  In this video we will discuss about Cloud pods, extending the discussion from module - 1. By default, LocalStack is an ephemeral environment, meaning that, once you terminate your LocalStack instance, all state will be discarded. Cloud Pods are a mechanism that allows you to take a snapshot of the current state of your LocalStack instance and easily share it with your team members. Furthermore we will pick a `QuickStart` guide to cloudpod and follow the on-screen tutorial to load a cloudpod in our environment using the web app. This cloudpod would 'load' the infrastructure and the deployed application onto our running localstack instance. The cloudpod contains the same application we deployed in this module.
length: 03:47
leadimage: cloud-pods.png
videoUrl: https://www.youtube.com/embed/ZJP2xfvwR_g?si=aG9TPQK7XtwlvFq5
type: lessons
url: "/academy/localstack-deployment/cloud-pods"
---


In this video, we will see how LocalStack can be used with infrastructure-as-code (IaC) and continuous integration (CI) tools to manage and automate AWS resources more efficiently. Manually deploying resources can be error-prone and time-consuming, thus we will be using one such LocalStack integration as a solution. 

- Using Infrastructure as Code tools such as terraform or pulumi, helps in managing configuration with added benefits such as version control, ease of editing, and reproducibility.
- LocalStack supports various integrations like Terraform and Pulumi, easing the automation of AWS resource deployment and management.
- Further we will demonstrate how LocalStack works seamlessly with CI platform, to incorporate local cloud emulation in CI pipelines. We can use localstack in these pipelines to run tests before pushing to production.

Towards the end we see a demo of how deploying PostgreSQL Aurora cluster on LocalStack using Terraform saves significant time and resources when deploying to using AWS directly. We've also mentioned some examples that you can refer to use localstack with Terraform and Pulumi.

Further reading:

- [LocalStack Integrations](https://docs.localstack.cloud/user-guide/integrations/)
- [LocalStack Pulumi Examples](https://github.com/localstack-samples/localstack-pulumi-samples)
- [LocalStack Terraform Examples](https://github.com/localstack-samples/localstack-terraform-samples)
- [LocalStack Continuous Integration](https://docs.localstack.cloud/user-guide/ci/)
- [LocalStack Screencasts](https://www.youtube.com/watch?v=JyQzr-i2E_k&list=PLTew28KOwGxMcBhN5_ds9ghlR-8QXEIJb)