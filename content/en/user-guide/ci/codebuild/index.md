---
title: "CodeBuild"
linkTitle: "CodeBuild"
weight: 7
description: Use LocalStack in CodeBuild
---


## Introduction

[AWS CodeBuild](https://docs.aws.amazon.com/codebuild/latest/userguide/welcome.html) is a managed AWS service for the build and testing phases of software development.
CodeBuild allows you to define your build project, set the source code location, and handles the building and testing, while supporting various programming languages, build tools, and runtime environments.
LocalStack supports CodeBuild out of the box and can be easily integrated into your pipeline to run your tests against a cloud emulator.


## Snippets

CodeBuild has the capability to use LocalStack's GitHub Action.

### Start up LocalStack

#### Native Runner

```yml
version: 0.2
...
phases:
  pre_build:
    commands:
      - pip3 install localstack awscli
      - docker pull public.ecr.aws/localstack/localstack:latest	
      - localstack start -d
      - localstack wait -t 30
```

#### GitHub Actions Runner

```yml
version: 0.2

phases:
  pre_build:
    steps:
      - run: docker pull public.ecr.aws/localstack/localstack:latest
      - run: docker image tag public.ecr.aws/localstack/localstack-pro:latest localstack/localstack:latest
      - name: Start LocalStack
        uses: LocalStack/setup-localstack@v0.2.0
        with:
          image-tag: 'latest'
          install-awslocal: 'true'
```


### Configuration

Get know more about the LocalStack [config options](/references/configuration/).

#### Native Runner
```yml
version: 0.2

env:
  variables:
    DEBUG: 1
...
phases:
...
```

#### GitHub Actions Runner

```yml
version: 0.2

env:
  variables:
    DEBUG: 1
...

phases:
  pre_build:
    steps:
      ...
      - name: Start LocalStack
        uses: LocalStack/setup-localstack@v0.2.0
        with:
          image-tag: 'latest'
          configuration: LS_LOG=trace
...
```


### Configuring a CI key

To enable LocalStack Pro features, you need to add your LocalStack CI API key to the project's environment variables.
The LocalStack container will automatically pick it up and activate the licensed features.

Go to the [CI Key Page](https://app.localstack.cloud/workspace/ci-keys) page and copy your CI key.
To add the CI key to your CodeBuild project, follow these steps:

- Navigate to your project dashboard, click **Edit** to open the dropdown, and select **Environment**.
- Click on **Additional configuration** and navigate to the **Environment variables** section.
- Specify **Name** as `LOCALSTACK_API_KEY` and **Value** as your CI key.
Specify **Type** as per your requirement.

Click on **Update environment** to save your environment variables.
Navigate to the buildspec file and change the Docker image to `public.ecr.aws/localstack/localstack-pro:latest`:

#### Native Runner

```yaml
...
phases:
  pre_build:
    commands:
      - pip3 install localstack awscli
      - docker pull public.ecr.aws/localstack/localstack-pro:latest	
...
```

#### GitHub Actions Runner

```yml
...
phases:
  pre_build:
    steps:
      - run: docker pull public.ecr.aws/localstack/localstack-pro:latest
      - run: docker image tag public.ecr.aws/localstack/localstack-pro:latest localstack/localstack-pro:latest
      - name: Start LocalStack
        uses: LocalStack/setup-localstack@v0.2.0
        with:
          image-tag: 'latest'
          use-pro: 'true'
...
```


### Dump LocalStack logs
```yaml
...
artifacts:
  files:
    - localstack.log

phases:
  pre_build:
    commands:
      # Starts up LocalStack
    ...
  build:
    commands:
      # Run some commands which might fail
      ...
  post_build:
    commands:
      # Dump logs on build fail
      - '[ ${CODEBUILD_BUILD_SUCCEEDING:-0} -eq 0 ] (localstack logs | tee localstack.log) || true'
...
# Optionally store dumped logs as artifact
artifact:
  files:
    - localstack.log
```


### Store LocalStack state

#### Cloud Pods

Find more information about cloud pods [here](/user-guide/state-management/cloud-pods/).

##### Native Runner
```yml
...
phases:
  pre_build:
    commands:
      ...
      # LocalStack is up and running already
      - localstack pod load <POD_NAME> || true
      ...
      - localstack pod save <POD_NAME>
      ...
```

##### GitHub Actions Runner

```yml
...
phases:
  pre_build:
    steps:
      # LocalStack is up and running already
      - name: Load the Cloud Pod 
        continue-on-error: true  # Allow it to fail as pod does not exist at first run
        uses: LocalStack/setup-localstack@v0.2.0
        with:
          state-backend: cloud-pods
          name: <cloud-pod-name>
          action: load
          skip-startup: 'true'
      ...
      - name: Save the Cloud Pod 
        uses: LocalStack/setup-localstack@v0.2.0
        with:
          state-backend: cloud-pods
          state-name: <cloud-pod-name>
          state-action: save
      ...
```

#### Ephemeral Instances (Preview)
```yml
...
phases:
  pre_build:
    commands:
      ...
      - |
          response=$(curl -X POST -d '{"auto_load_pod": "false"}' \
            -H 'ls-api-key: $LOCALSTACK_API_KEY' \
            -H 'authorization: token $LOCALSTACK_API_KEY' \
            -H 'content-type: application/json' \
            https://api.localstack.cloud/v1/previews/my-localstack-state)
          
          if [ "$endpointUrl" = "null" ] || [ "$endpointUrl" = "" ]; then
            echo "Unable to create preview environment. API response: $response"
            exit 1
          fi
          echo "Created preview environment with endpoint URL: $endpointUrl"

          export AWS_ENDPOINT_URL=$endpointUrl
      ...
```

Find out more about [ephemeral instances](/user-guide/cloud-sandbox/).

#### Artifact

Find out more about [state management](/user-guide/state-management/export-import-state/).

```yml
...
phases:
  pre_build:
  # LocalStack is up and running already
  - (test -f ./ls-state-pod.zip && localstack state import ./ls-state-pod.zip) || true
  ...
  - localstack state export ./ls-state-pod.zip
...
artifact:
  files:
    - ls-state-pod.zip
```
Alternatively save as a secondary artifact:
```yml
...
artifact:
  ...
  secondary-artifacts:
    ls-state:
      files:
        - ls-state-pod.zip
    ...
```
To use previously stored artifacts as inputs, set them as a source in the project.

#### Cache

Additional information about [state export and import](/user-guide/state-management/export-import-state/).

##### Native Runner
```yml
...
phases:
  pre_build:
    commands:
    # LocalStack is up and running already
      - (test -f ./ls-state-pod.zip && localstack state import ./ls-state-pod.zip) || true
      ...
      - localstack state export ./ls-state-pod.zip
...
cache:
  paths:
    - 'ls-state-pod.zip'
```

##### GitHub Actions Runner
```yml
...
phases:
  pre_build:
    steps:
      - run: (test -f ./ls-state-pod.zip && localstack state import ./ls-state-pod.zip) || true
      ...
      - run: localstack state export ./ls-state-pod.zip
...
cache:
  paths:
    - 'ls-state-pod.zip'
```


## Current Limitations

- We recommend using the `public.ecr.aws/localstack/localstack:latest` image to start LocalStack, instead of the `localstack/localstack:latest` image. LocalStack mirrors the Docker Hub image to the public ECR repository.
  You can use the Docker Hub image as well, though you may run into the following error:
  ```bash
  toomanyrequests: You have reached your pull rate limit. You may increase the limit by authenticating and upgrading: https://www.docker.com/increase-rate-limit
  ```
  To resolve this use your Docker Hub account credentials to pull the image.
- LocalStack depends on the Docker socket to emulate your infrastructure.
  To enable it, update your project by ticking **Environment > Additional Configuration > Privileged > Enable this flag if you want to build Docker Images or want your builds to get elevated privileges**.
- AWS states in its [documentation](https://docs.aws.amazon.com/codebuild/latest/userguide/action-runner-buildspec.html#action-runner-limitations) GitHub Actions Runners are not available for **webhook triggered open Git repositories**.
- Be aware that you can only use either the _Native Runner_ or the _GitHub Actions Runner_ snippets in the same phase
For further information see the official CodeBuild [documentation](https://docs.aws.amazon.com/codebuild/latest/userguide/action-runner-buildspec.html).
