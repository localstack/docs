---
title: "Setup GitHub Action workflow that starts up LocalStack and deploys the infrastructure"
linkTitle: "Setup GitHub Action workflow that starts up LocalStack and deploys the infrastructure"
weight: 7
description: >
  In this video, we will employ LocalStack's GitHub Actions integration to deploy our application's infrastructure on LocalStack. Additionally, we will perform a diagnostic test to validate the deployment, ensuring that the infrastructure is set up correctly. This will enable you to conduct cloud integration tests for your application and infrastructure.
length: 03:22
leadimage: github-action.png
videoUrl: https://www.youtube.com/embed/XNh8aSaT9v0?si=do2ZMVfb6F6Tmzby
type: lessons
url: "/academy/localstack-deployment/github-action-ls"
---

LocalStack allows organizations to automate their application testing and integration process using continuous integration (CI). You can seamlessly integrate LocalStack with your current CI platform. LocalStack offers native plugin for [CircleCI](https://circleci.com/developer/orbs/orb/localstack/platform) & [GitHub Actions](https://github.com/marketplace/actions/setup-localstack), and a universal driver for other CI platforms. This integration enables you to include LocalStack's local AWS cloud emulation in your CI pipelines, leverage advanced features such as Cloud Pods and CI analytics, and execute your test and integration suite before deploying to production.

Here's a breakdown of the steps we'll take:

- We'll look the `main.yml` file located in the `.github` directory. This file sets up LocalStack on the GitHub Action runner.
- We install `awslocal` and `tflocal` to deploy the local infrastructure on LocalStack's cloud emulator running in the CI pipeline.
- Following this deployment, we utilize `awslocal` to validate the deployed resources and conduct a diagnostic test on LocalStack to ensure everything is functioning correctly.

Further reading:

- [Configuring CI Keys in LocalStack](https://docs.localstack.cloud/user-guide/ci/ci-keys/)
- [LocalStack CI Analytics](https://docs.localstack.cloud/user-guide/ci/ci-analytics/)
- [GitHub Actions & Infrastructure Testing with LocalStack](https://hashnode.localstack.cloud/github-actions-infrastructure-testing-with-localstack)
- [Github Actions & End-to-End Testing with Testcontainers & LocalStack](https://hashnode.localstack.cloud/github-actions-end-to-end-testing-with-testcontainers-localstack)
