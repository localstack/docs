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

- Use a GitLab CI image for the keyword image that best fits your use-case (`docker:20.10.16` or any other version).
- Add GitLab CI variables using the keyword variables to include `AWS_ACCESS_KEY_ID`, `AWS_SECRET_ACCESS_KEY`, and `AWS_DEFAULT_REGION`.
- Create a service using the keyword `services` and reference `docker:20.10.16-dind` to pull the latest Docker image and assign an alias for the container (`docker` in our case). Use the `command` option to disable TLS with `--tls=false`.
- Install LocalStack and/or AWS-related dependencies to define the commands that should be run before all builds.
- In the `before_script` section, add commands to set up the `LOCALSTACK_HOSTNAME` and `HOSTNAME_EXTERNAL` environment variables and append `localhost.localstack.cloud` to `/etc/hosts` using the IP address of the `docker` service.
- In the script section, pull the `localstack/localstack` Docker image, start LocalStack in detached mode, and run your LocalStack-related tests.

The following example Gitlab CI job config (`.gitlab-ci.yml`) executes these steps, creates a new S3 bucket, copies some content to the bucket, and checks the content of the bucket:

```yml
image: docker:20.10.16

stages:
  - test

test:
  stage: test
  variables:
    AWS_ACCESS_KEY_ID: test
    AWS_SECRET_ACCESS_KEY: test
    AWS_DEFAULT_REGION: us-east-1
    DOCKER_HOST: tcp://docker:2375
    DOCKER_TLS_CERTDIR: ""
    LOCALSTACK_HOSTNAME: localhost.localstack.cloud
    HOSTNAME_EXTERNAL: localhost.localstack.cloud

  services:
    - name: docker:20.10.16-dind
      alias: docker
      command: ["--tls=false"]

  before_script:
    - apk update
    - apk add gcc musl-dev linux-headers py3-pip python3 python3-dev
    - python3 -m pip install localstack awscli
  script:
    - docker pull localstack/localstack:latest
    - dind_ip="$(getent hosts docker | cut -d' ' -f1)"
    - echo "${dind_ip} localhost.localstack.cloud " >> /etc/hosts
    - DOCKER_HOST="tcp://${dind_ip}:2375" localstack start -d
    - aws --endpoint http://localhost.localstack.cloud:4566 s3 mb s3://test
    - echo "hello world" > /tmp/hello-world
    - aws --endpoint http://localhost.localstack.cloud:4566 s3 cp /tmp/hello-world s3://test/hello-world
    - aws --endpoint http://localhost.localstack.cloud:4566 s3 ls s3://test/
```

{{< alert title="Note">}}
While working with a Docker-in-Docker (`dind`) setup, the Docker runner requires `privileged` mode. You must always use `privileged = true` in your GitLab CI's `config.toml` file while setting up LocalStack in GitLab CI runners. For more information, see [GitLab CI Docker-in-Docker](https://docs.gitlab.com/ee/ci/docker/using_docker_build.html#use-docker-in-docker-executor) documentation.
{{< /alert >}}

## Configuring an API key

You can easily enable LocalStack Pro by using the `localstack/localstack-pro` image and adding your API key to the repository's environment variables. Go to your project's **Settings > CI/CD**  and expand the  **Variables**  section. Select the **Add Variable** button and fill in the necessary details. After you create a variable, you can use it in the `.gitlab-ci.yml` file.

However Variables set in the GitLab UI are not passed down to service containers. We need to assign them to variables in the UI, and then re-assign them in our `.gitlab-ci.yml`:

```yaml
...
test:
  stage: test
  variables:
    AWS_ACCESS_KEY_ID: test
    AWS_SECRET_ACCESS_KEY: test
    AWS_DEFAULT_REGION: us-east-1
    LOCALSTACK_API_KEY: $LOCALSTACK_API_KEY
  ...
  script:
    - docker pull localstack/localstack-pro:latest
    ...
    - DOCKER_HOST="tcp://${dind_ip}:2375" localstack start -d
...
```

You can check the logs of the LocalStack container to see if the activation was successful. If the API key activation fails, LocalStack container will exit with an error code.
