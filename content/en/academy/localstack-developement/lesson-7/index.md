---
title: "Setup GitHub Action workflow that starts up LocalStack and deploys the infrastructure"
linkTitle: "Setup GitHub Action workflow that starts up LocalStack and deploys the infrastructure"
weight: 7
description: >
  GitHub Actions makes it easy to automate all your software workflows, with CI/CD. Build, test, and deploy your code right from GitHub. The objective of this video is to use localstack along with all the infra built, for testing the code. Thus ensuring that the code to be merged in the main repo would work on the actual AWS infra that is deployed.
length: 03:22
leadimage: github-action.png
videoUrl: https://www.youtube.com/embed/XNh8aSaT9v0?si=do2ZMVfb6F6Tmzby
type: lessons
url: "/academy/localstack-deployment/github-action-ls"
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