---
title: "LocalStack Integrations - Infrastructure-as-Code and CI tools "
linkTitle: "LocalStack Integrations - Infrastructure-as-Code and CI tools "
weight: 3
description: >
  In the last video where we manually deployed some AWS resources, we realized that there were a lot of resources that needed to be deployed and doing it manually can be really hard and prone to errors. We mostly interacted with LocalStack through the CLI. However, large systems are hardly built this way. To the rescue comes LocalStack’s integrations. LocalStack supports a wide range of integrations from the cloud development ecosystem. One such integration is terraform, which is an Infrastructure as Code ( IaC ) tool, which we are going to use to setup the whole AWS infrastructure, that we discussed in the previous video. 
  
  We will also see how using Localstack's CircleCI integration, you can easily integrate it to your CI pipelines, to emulate AWS cloud in your pipelines.
length: 03:09
leadimage: ls-integrations.png
videoUrl: https://www.youtube.com/embed/YV0Zs6UNI9I?si=dD8VzemepxA1Pzkg
type: lessons
url: "/academy/localstack-deployment/ls-integrations/"
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