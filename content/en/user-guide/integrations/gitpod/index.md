---
title: "Gitpod"
linkTitle: "Gitpod"
description: >
  Use Gitpod's fully automated, ephemeral workspaces to develop & test your cloud applications with LocalStack
---

<img src="gitpod_logo.png" width="600px" alt="Gitpod logo">

## Overview

Gitpod is an open-source platform that enables remote software development via ephemeral workspaces.
It provides an automated setup with cloud-based, remote developer environments connected with a developer’s [editing experience of choice](https://www.gitpod.io/docs/references/ides-and-editors).
Gitpod allow users to codify their developer environment as code.
With projects codified, you can spin up a new workspace, start coding and throw away the workspace when they are done!

## LocalStack on Gitpod

LocalStack allows you to set up a development environment with a cloud sandbox that can be used to test and develop cloud applications.
Using Gitpod's environment you can run a LocalStack container inside the runtime that allows to instantiate your application on a code editor of your choice.
You can then conveniently deploy your cloud application assets into LocalStack's cloud sandbox, to then preview the results.

To configure LocalStack on Gitpod, you would need to set up a `.gitpod.yml` on the root of your repository.
The file configures your workspace and the environment that you would like to use.
You can find more information on the [Gitpod documentation](https://www.gitpod.io/docs/config-gitpod-file/).

```yaml
tasks:
  - name: start-localstack
    env:
      AWS_ACCESS_KEY_ID: "test"
      AWS_SECRET_ACCESS_KEY: "test"
      AWS_DEFAULT_REGION: "us-east-1"
    init: |
      python -m pip install localstack
    command: |
      . ~/.bash_profile
      docker network create localstack
      localstack start
  - name: install-awslocal
    env:
      AWS_ACCESS_KEY_ID: "test"
      AWS_SECRET_ACCESS_KEY: "test"
      AWS_DEFAULT_REGION: "us-east-1"
    init: |
      cd /workspace
      curl "https://awscli.amazonaws.com/awscli-exe-linux-x86_64.zip" -o "awscliv2.zip"
      unzip awscliv2.zip
      sudo ./aws/install
      cd $THEIA_WORKSPACE_ROOT
      python -m pip install awscli-local
ports:
  - port: 4510-4559
    onOpen: ignore
  - port: 4566
    onOpen: ignore      
  - port: 53
    onOpen: ignore      
  - port: 443
    onOpen: ignore
```

Enabling [Gitpod Prebuilds](https://www.gitpod.io/docs/configure/repositories/prebuilds) helps save time by executing `init` tasks defined in the `.gitpod.yml` ahead of time, allowing your workspace to start faster and with all the dependencies already installed.

Upon creation, you will be able to see the LocalStack container running in the background (you can use `localstack status` to check the status of the container).

For a simple demonstration, check out the [LocalStack Gitpod demo](https://github.com/Gitpod-Samples/localstack-gitpod-demo) repository.
Check out our [in-depth walkthrough over the demo](https://localstack.cloud/blog/2022-09-26-localstack-x-gitpod-run-cloud-applications-with-localstack-and-gitpod/) on our blog!
