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

LocalStack enables organizations to automate their application testing and integration process through continuous integration (CI).You can easily integrate LocalStack with your existing CI platform. LocalStack provide native plugins for CircleCI and a generic driver for any other CI platform you might use. This enables you to incorporate LocalStack’s local AWS cloud emulation in your CI pipelines, use advanced features like Cloud Pods and CI analytics, and run your test & integration suite before pushing to production.

In this video, we will use localstack CI Integration - Github action, it  makes it easy to automate all your software workflows. The objective of this video is to use Localstack Integration Github action to deploy infrastructure of our demo application on localstack and run a diagnostic test to verify the deployment. Thus ensuring that the code to be merged in the main repo would work on the actual AWS infra that will be deployed. 

- We will go through the `main.yml` in `.github` folder. This file runs the github action that deploys localstack on github runner, installs `awslocal`, `tflocal` and deploys the infrastructure resources there. 
- Then we use `awslocal` to verify the deployed resources and finally run a diagnostic test on localstack to confirm everything’s working fine.

Further reading:

- [LocalStack GitHub Action](https://docs.localstack.cloud/user-guide/ci/github-actions/)
- [LocalStack CI Analytics](https://docs.localstack.cloud/user-guide/ci/ci-analytics/)
- [CI Keys](https://docs.localstack.cloud/user-guide/ci/ci-keys/)
- [LocalStack Continuous Integration](https://docs.localstack.cloud/user-guide/ci/)