---
title: "GitLab CI"
weight: 6
description: >
  Use LocalStack in [GitLab CI](https://docs.gitlab.com/ee/ci/)
---

This page contains easily customisable snippets to show you how to manage LocalStack in a GitLab CI pipeline.

## Snippets

### Start up Localstack
{{< callout "tip" >}}
While working with a Docker-in-Docker (`dind`) setup, the Docker runner requires `privileged` mode.
You must always use `privileged = true` in your GitLab CI's `config.toml` file while setting up LocalStack in GitLab CI runners.
For more information, see [GitLab CI Docker-in-Docker](https://docs.gitlab.com/ee/ci/docker/using_docker_build.html#use-docker-in-docker-executor) documentation.
{{< /callout >}}

<details>
<summary>For LocalStack versions before 3.0.0</summary>
Under test>variables, add:<br>
LOCALSTACK_HOSTNAME: localhost.localstack.cloud<br>
HOSTNAME_EXTERNAL: localhost.localstack.cloud.
</details>

#### Service
```yaml
...
variables:
  DOCKER_SOCK: tcp://docker:2375
  DOCKER_HOST: tcp://docker:2375
  DOCKER_TLS_CERTDIR: ""
...
services:
  - name: localstack/localstack:latest
    alias: localstack
  - name: docker:dind
    alias: docker
    command: ["--tls=false"]
...
```

#### Container
```yaml
image: docker:latest

stages:
  - job

job:
  stage: job
  variables:
    ...
    DOCKER_HOST: tcp://docker:2375
    DOCKER_TLS_CERTDIR: ""
    AWS_ENDPOINT_URL: "http://localhost.localstack.cloud:4566"
    ...

  services:
    - name: docker:dind
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
```

### Configure a CI key
You can easily enable LocalStack Pro by using the `localstack/localstack-pro` image and adding your CI key to the repository's environment variables.
Go to your project's **Settings > CI/CD**  and expand the  **Variables**  section.
Select the **Add Variable** button and fill in the necessary details.
After you create a variable, you can use it in the `.gitlab-ci.yml` file.

However Variables set in the GitLab UI are not passed down to service containers.
We need to assign them to variables in the UI, and then re-assign them in our `.gitlab-ci.yml`

```yaml
...
variables:
  LOCALSTACK_API_KEY: $LOCALSTACK_API_KEY
...
services:
  - name: localstack/localstack-pro:latest
    alias: localstack
...
```
You can check the logs of the LocalStack container to see if the activation was successful.
If the CI key activation fails, LocalStack container will exit with an error code.

### Dump Localstack logs
```yaml
...
job:
  variables:
    LOCALSTACK_HOST: <LS_HOST>:<LS_PORT>
  script:
  - localstack logs | tee localstack.log
... 
```
In case of the service setup `LOCALSTACK_HOST` will be `localstack:4566`.

### Store Localstack state

You can preserve your AWS infrastructure with Localstack in various ways.

#### Artifact
```yaml
...
job:
  before_script:
    - (test -f ./ls-state-pod.zip && localstack state import ./ls-state-pod.zip) || true
  script:
  ...
    - localstack state export ./ls-state-pod.zip
  ...
  artifacts:
    paths:
      - $CI_PROJECT_DIR/ls-state-pod.zip
...
```
More info about Localstack's state export and import [here](/user-guide/state-management/export-import-state/).

#### Cache
```yaml
...
job:
  before_script:
    - (test -f ./ls-state-pod.zip && localstack state import ./ls-state-pod.zip) || true
  script:
  ...
    - localstack state export ./ls-state-pod.zip
  ...
  cache:
    key:
      untracked: true
      files:
        - $CI_PROJECT_DIR/ls-state-pod.zip
    paths:
      - $CI_PROJECT_DIR/ls-state-pod.zip
...
```
Additional information about state export and import [here](/user-guide/state-management/export-import-state/).

#### Cloud Pod
```yaml
...
job:
  before_script:
    - localstack pod load <POD_NAME> || true
  script:
  ...
    - localstack pod save <POD_NAME>
...
```
Find more information about cloud pods [here](/user-guide/state-management/cloud-pods/).

#### Ephemeral Instance (Preview)

```yaml
...
variables:
  LOCALSTACK_API_KEY: $LOCALSTACK_API_KEY
...
setup-job:
  stage: build
  before_script:
    - |
      response=$(curl -X POST -d '{"auto_load_pod": "false"}' \
        -H 'ls-api-key: $LOCALSTACK_API_KEY' \
        -H 'authorization: token $LOCALSTACK_API_KEY' \
        -H 'content-type: application/json' \
        https://api.localstack.cloud/v1/previews/my-gitlab-state)
      
      if [ "$endpointUrl" = "null" ] || [ "$endpointUrl" = "" ]; then
        echo "Unable to create preview environment. API response: $response"
        exit 1
      fi
      echo "Created preview environment with endpoint URL: $endpointUrl"

      echo "export AWS_ENDPOINT_URL=$endpointUrl"
      echo "$AWS_ENDPOINT_URL" >> ls-endpoint.env
  ...
  artifacts:
    reports:
      dotenv: ls-endpoint.env

test-job:
  stage: test
  script:
    - echo "$AWS_ENDPOINT_URL"  # Output is the address of the ephemeral instance
...
```

Find out more about ephemeral instances [here](/user-guide/cloud-sandbox/).

## Current Limitations

- Localstack must be able to reach a docker socket to provision containers for certain services, ie Lambda, EKS, ECS...etc
- the runner must be able to resolve the Localstack domain (by default _localhost.localstack.cloud_), see the sample pipelines for a possible solution
- to be able to separate steps into their own jobs one must preserve Localstack's state, since Gitlab is not preserving job related containers/services during the pipelines
- to start up Localstack in Gitlab CI Docker tools are necessary
- when Localstack run as a container, it's not accessible during the `after_script` phase
