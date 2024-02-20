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
- In the `script` section, append `localhost.localstack.cloud` to `/etc/hosts` using the IP address of the `docker` service.
- In the `script` section, pull the `localstack/localstack` Docker image, start LocalStack in detached mode, and run your LocalStack-related tests.

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

<details>
<summary>For LocalStack versions before 3.0.0</summary>
Under test>variables, add:<br>
LOCALSTACK_HOSTNAME: localhost.localstack.cloud<br>
HOSTNAME_EXTERNAL: localhost.localstack.cloud.
</details>

{{< alert title="Note">}}
While working with a Docker-in-Docker (`dind`) setup, the Docker runner requires `privileged` mode. You must always use `privileged = true` in your GitLab CI's `config.toml` file while setting up LocalStack in GitLab CI runners. For more information, see [GitLab CI Docker-in-Docker](https://docs.gitlab.com/ee/ci/docker/using_docker_build.html#use-docker-in-docker-executor) documentation.
{{< /alert >}}

## Configuring a CI key

You can easily enable LocalStack Pro by using the `localstack/localstack-pro` image and adding your CI key to the repository's environment variables. Go to your project's **Settings > CI/CD**  and expand the  **Variables**  section. Select the **Add Variable** button and fill in the necessary details. After you create a variable, you can use it in the `.gitlab-ci.yml` file.

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

You can check the logs of the LocalStack container to see if the activation was successful. If the CI key activation fails, LocalStack container will exit with an error code.

## Best practices and known issues

- Localstack must be able to reach a docker socket to provision containers for certain services, ie Lambda, EKS, ECS...etc
- the runner should be able to resolve the Localstack domain (by default _localhost.localstack.cloud_), see the sample pipelines for a possible solution
- we do NOT recommend to setup Localstack as a service for **Pro+ customers**, because the API key/auth token as a security best practice should be stored as CI secrets, however we've found with the current version of Gitlab, at the time of writing v16.10, is not expanding CI/CD variables for service containers eventhough the documentation states it as an option
- to be able to separate steps into their own jobs (something like deploy, test...etc) one must preserve Localstack's state, as Gitlab is not preserving job related containers/services during the pipelines
This can be done by **Pro+ customers** by using cloud pods, state exports in combination with CI artifacts/cache or ephemeral instances (beta).
**Free tier customers** must merge their steps into a single job as the above mentioned state preservation methods are not available for them.
- to start up Localstack images with docker tools are necessary, in our examples we use the official Alpine based dind images, however for many users might be easier to build their own images for convenience