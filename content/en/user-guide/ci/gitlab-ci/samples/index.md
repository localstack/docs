---
title: "Sample"
linkTitle: "Sample"
weight: 5
description: >
  Localstack Sample Project in Gitlab CI
aliases:
  - /ci/gitlab-ci/samples
tags: ["continuous-integration", "ci", "continuous-delivery", "testing","gitlab-ci","sample"]
---

This page containes our Quickstart project's test pipeline implemented in Gitlab CI.

# Serverless image resizer s3 lambda
This is an app to resize images uploaded to S3 in a serverless way.
Find code in repo [here](https://gitlab.com/Lakkeger/sample-serverless-image-resizer-s3-lambda).

## Main pipeline
Run integration tests by taking leverage of Localstack's cloud pods feature.

Cloud pods providing a quick and easy way to break the pipeline into multiple steps and load the same state every time without going through the hassle of deploying the infrastructure again.
This can be stored locally, like we did below, or remotely in our Web Application.
Find more information on them [here](/user-guide/state-management/cloud-pods/).

In case of failure the pipeline dumps the logs of Localstack and preserves them as artifacts for further investigations.

```
image: docker:20.10.16-dind

stages:
  - deploy
  - test

variables:
  AWS_ACCESS_KEY_ID: test
  AWS_SECRET_ACCESS_KEY: test
  AWS_DEFAULT_REGION: us-east-1
  AWS_REGION: us-east-1
  AWS_ENDPOINT_URL: http://localhost.localstack.cloud:4566
  PIP_CACHE_DIR: $CI_PROJECT_DIR/.cache/pip
  DOCKER_HOST: tcp://docker:2375
  DOCKER_TLS_CERTDIR: ""
  CI_DEBUG_TRACE: "true"
  LS_LOG: trace

services:
  - name: docker:20.10.16-dind
    alias: docker
    command: ["--tls=false"]

default:
  before_script: &default_before_scripts
    - apk update
    - apk add --no-cache gcc musl-dev linux-headers bash zip jq tee
    - apk add --no-cache --repository=http://dl-cdn.alpinelinux.org/alpine/v3.15/main python3~3.9
    - apk add --no-cache --repository=http://dl-cdn.alpinelinux.org/alpine/v3.15/community py3-psutil~5.8
    - python3 -m ensurepip
    - python3 -m pip install --no-cache --upgrade pip setuptools
    - mkdir -p $PIP_CACHE_DIR
    - python3 -m pip install localstack awscli awscli-local
    - docker pull localstack/localstack-pro:latest
    - dind_ip="$(getent hosts docker | cut -d' ' -f1)"
    - echo "${dind_ip} localhost.localstack.cloud " >> /etc/hosts
    - localstack start -d
    - localstack wait -t 30
    - (test -f ./ls-state-pod.zip && localstack state import ./ls-state-pod.zip) || true
  cache:
    paths:
      - $CI_PROJECT_DIR/.cache/pip
  artifacts:
    paths:
      - $CI_PROJECT_DIR/ls-state-pod.zip
    expire_in: 1 days

deploy:
  stage: deploy
  script:
    - ./bin/deploy.sh
    - localstack state export ./ls-state-pod.zip

test:
  stage: test
  before_script:
    - *default_before_scripts
    - python3 -m pip install -r requirements-dev.txt
  script:
    - python3 -m pytest tests
  after_script:
    - docker ps | tee docker_ps.log
    - docker inspect localstack-main | tee docker_inspect.log
    - curl ${AWS_ENDPOINT_URL}:4566/_localstack/diagnose | tee ls_diagnose.log
    - localstack logs | tee ls_runlogs.log
  artifacts:
    when: on_failure
    name: logs
    paths:
      - *.log
    expire_in: 30 days
```
