---
title: "GitHub Actions"
tags: ["continuous-integration", "ci", "continuous-delivery", "testing"] 
weight: 5
description: >
  Use LocalStack in [GitHub Actions](https://github.com/features/actions)
---

This guide shows you how to start LocalStack in a Github Actions job.

## Setting up your Github Actions job

In order to start LocalStack, we recommend to start it in a separate [build step][1], to separate its log output / status from the rest of your job.

We recommend taking the following steps:
- Install the LocalStack CLI (and maybe also `awslocal`).
- Make sure your LocalStack docker image is up-to-date by pulling the latest version.
- Use the LocalStack CLI to start LocalStack. Make sure to use the `-d` flag to start the LocalStack docker container in detached mode.
- Wait for the container to report that it is up and running.

An official GitHub action for this also planned, to make the configuration easier and less verbose.

The following example can be integrated into your GitHub workflow.
As an example, it will use awslocal to create bucket and list it afterwards.

```yaml
name: localstack-action-example
on: push
jobs:
  example-job:
    runs-on: ubuntu-latest
    steps:
      - name: Start LocalStack
        env:
          LOCALSTACK_API_KEY: ${{ secrets.LOCALSTACK_API_KEY }}
        run: |
          # install LocalStack cli and awslocal
          pip install localstack awscli-local[ver1]
          # Make sure to pull the latest version of the image
          docker pull localstack/localstack
          # Start LocalStack in the background
          localstack start -d
          # Wait 30 seconds for the LocalStack container to become ready before timing out
          echo "Waiting for LocalStack startup..."
          localstack wait -t 30
          echo "Startup complete"
      - name: Run some Tests against LocalStack
        run: |
          awslocal s3 mb s3://test
          awslocal s3 ls
          echo "Test Execution complete!"
```

If you want to add further configuration for LocalStack, you can use the `env` section of your build step to set the configuration variables as described [here][2].

## Activating LocalStack Pro

If you want to use LocalStack Pro in your GitHub Actions job, you should use a [Github Encrypted Secret][3] to store your API key securely.
In the above example, you can see us setting the `LOCALSTACK_API_KEY` environment variable to the value of the secret `LOCALSTACK_API_KEY`.

You can set your secret at an environment, repository or organization level, for more information see [here][3].
In the simplest case, you just set it at the repository level.
For this, you go, in your repository, to Settings => Secrets and press "New Repository Secret".

There, you create the secret for your API key like in the following image, replacing `foobar` with your API key.

![Adding the LocalStack API key as secret in GitHub](github-create-secret.png)

## Troubleshooting / FAQ

### Installations fails with `AttributeError: module 'lib' has no attribute 'X509_V_FLAG_CB_ISSUER_CHECK'`

The issue is caused by a conflict of the pre-installed version of `pyOpenSSL` with newer versions of `cryptography`.
Please manually upgrade by running `pip install --upgrade pyopenssl` before installing localstack to solve this issue.

[See here for more information](https://github.com/localstack/localstack/pull/6831#issuecomment-1241974114)

[1]: https://docs.github.com/en/actions/learn-github-actions/understanding-github-actions#steps "GitHub Action Build Steps"
[2]: https://docs.github.com/en/actions/using-workflows/workflow-syntax-for-github-actions#jobsjob_idstepsenv "GitHub Action Steps - Environment variables"
[3]: https://docs.github.com/en/actions/security-guides/encrypted-secrets "GitHub Encrypted Secrets"