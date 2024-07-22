---
title: "GitPod"
linkTitle: "GitPod"
description: >
  Use GitPod's fully automated, ephemeral workspaces to develop & test your cloud applications with LocalStack
---

<img src="gitpod_logo.png" width="600px" alt="GitPod logo">

## Overview

Gitpod is an open-source platform that enables remote software development via ephemeral workspaces.
It provides an automated setup with cloud-based, remote developer environments connected with a developer’s [editing experience of choice](https://www.gitpod.io/docs/references/ides-and-editors).
Gitpod allow users to codify their developer environment as code.
With projects codified, you can spin up a new workspace, start coding and throw away the workspace when they are done!

## LocalStack on GitPod

LocalStack allows you to set up a development environment with a cloud sandbox that can be used to test and develop cloud applications.
Using GitPod's environment you can run a LocalStack container inside the runtime that allows to instantiate your application on a code editor of your choice.
You can then conveniently deploy your cloud application assets into LocalStack's cloud sandbox, to then preview the results.

To configure LocalStack on GitPod, you would need to set up a `.gitpod.yml` on the root of your repository.
The file configures your workspace and the environment that you would like to use.
You can find more information on the [GitPod documentation](https://www.gitpod.io/docs/config-gitpod-file/).

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

If you are using GitHub, you can also use the [GitPod Prebuilds](https://www.gitpod.io/docs/prebuilds/) feature to automatically build your workspace.
This will allow you to start your workspace faster and with all the dependencies already installed.
Add the following to your `.gitpod.yml` file:

```yaml
github:
  prebuilds:
    # enable for the default branch
    master: true
    # enable for all branches in this repo
    branches: true
    # enable for pull requests coming from this repo
    pullRequests: true
    # enable for pull requests coming from forks
    pullRequestsFromForks: true
    # add a check to pull requests
    addCheck: true
    # add a "Review in Gitpod" button as a comment to pull requests
    addComment: false
    # add a "Review in Gitpod" button to the pull request's description
    addBadge: true
```

After adding the configuration, you can start your development & testing by creating [your workspace in GitPod](https://www.gitpod.io/docs/getting-started/#start-your-first-workspace).
Upon creation, you will be able to see the LocalStack container running in the background (you can use `localstack status` to check the status of the container).

For a simple demonstration, check out the [LocalStack GitPod demo](https://github.com/Gitpod-Samples/localstack-gitpod-demo) repository.
Check out our [in-depth walkthrough over the demo](https://localstack.cloud/blog/2022-09-26-localstack-x-gitpod-run-cloud-applications-with-localstack-and-gitpod/) on our blog!
