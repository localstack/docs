---
title: "GitLab CI"
tags: ["continuous-integration", "ci", "continuous-delivery", "testing"] 
weight: 7
description: >
  Use LocalStack in [GitLab CI](https://docs.gitlab.com/ee/ci/)
aliases:
  - /ci/gitlab-ci/
---

This guide shows you how to start LocalStack in a GitLab CI pipeline.

## Setting up your GitLab CI job

To start LocalStack, we recommend starting it using Services. Services can be configured using the `services` keyword and run LocalStack with network access to help you connect with LocalStack using the `aws` command-line interface. Every time a GitLab CI job is triggered, it checks which ports are exposed from the LocalStack container by default and starts a special container that waits for these ports to be accessible.

We recommend taking the following steps:

- Use a GitLab CI image for the keyword `image` that best fits your use-case (`python:3.10`, `node:16` or anything specific).
- Add GitLab CI variables using the keyword `variables` to include `AWS_ACCESS_KEY_ID`, `AWS_SECRET_ACCESS_KEY`, and `AWS_DEFAULT_REGION`.
- Create a service using the keyword `services` and reference `localstack/localstack` to pull the latest Docker image and assign an `alias` for the container (`localstack` in our case).
- Install LocalStack and/or AWS-related dependencies to define the commands that should be run before all builds.
- Run your LocalStack-related tests in the main job. 

The following example Gitlab CI job config (`.gitlab-ci.yml`) executes these steps, creates a new S3 bucket, copies some content to the bucket, and check the available buckets:

```yml
image: python:3.10

stages:
  - test

test:
  stage: test
  variables:
    AWS_ACCESS_KEY_ID: dummy
    AWS_SECRET_ACCESS_KEY: dummy
    AWS_DEFAULT_REGION: eu-central-1
  services:
    - name: localstack/localstack
      alias: localstack
  before_script:
    - LOCALSTACK_URL=http://localstack:4566
    - pip install awscli
  script:
    - aws s3 mb s3://test --endpoint-url ${LOCALSTACK_URL}
    - echo "hello world" > /tmp/hello-world
    - aws s3 cp /tmp/hello-world s3://test/hello-world --endpoint-url ${LOCALSTACK_URL}
    - aws s3 ls s3://test/ --endpoint-url ${LOCALSTACK_URL}
```

## Configuring an API key

You can easily enable LocalStack Pro by by using the `localstack/localstack-pro` image and adding your API key to the repository's environment variables. Go to your project's **Settings > CI/CD**  and expand the  **Variables**  section. Select the **Add Variable** button and fill in the necessary details. After you create a variable, you can use it in the `.gitlab-ci.yml` file.

However Variables set in the GitLab UI are not passed down to service containers. We need to assign them to variables in the UI, and then re-assign them in our `.gitlab-ci.yml`:

```yaml
test:
  stage: test
  variables:
    AWS_ACCESS_KEY_ID: dummy
    AWS_SECRET_ACCESS_KEY: dummy
    AWS_DEFAULT_REGION: eu-central-1
    LOCALSTACK_API_KEY: $LOCALSTACK_API_KEY
  services:
    - name: localstack/localstack-pro
      alias: localstack
      variables:
        LOCALSTACK_API_KEY=${LOCALSTACK_API_KEY}
```
