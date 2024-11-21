---
title: "CircleCI"
linkTitle: "CircleCI"
weight: 4
description: >
  Use LocalStack in CircleCI
---


## Introduction

[CircleCI](https://circleci.com) is a continuous integration and continuous delivery (CI/CD) platform which uses a configuration file (usually named `.circleci/config.yml`) to define the build, test, and deployment workflows.
LocalStack supports CircleCI out of the box and can be easily integrated into your pipeline to run your tests against a local cloud emulator.

## Snippets

### Start up LocalStack

#### Default

```yaml
version: '2.1'
orbs:
  localstack: localstack/platform@2.2
jobs:
  localstack-test:
    executor: localstack/default
    steps:
      - localstack/startup
      ...
workflows:
  localstack-test:
    jobs:
      - localstack-test

```

#### Async

```yaml
version: '2.1'
orbs:
  localstack: localstack/platform@2.2
jobs:
  localstack-test:
    executor: localstack/default
    steps:
      - localstack/start
      ...
      - localstack/wait
workflows:
  localstack-test:
    jobs:
      - localstack-test
```

### Configuration

To configure LocalStack use the `environment` key on the job level or a shell command, where the latter takes higher precedence.

Read more about the [configuration options](/references/configuration/) of LocalStack.

#### Job level

```yaml
...
jobs:
  localstack-test:
    executor: localstack/default
    environment:
      DEBUG: 1
    steps:
      - localstack/startup
...
```

#### Shell command

```yaml
...
jobs:
  localstack-test:
    executor: localstack/default
    steps:
      - run:
          name: Configure LocalStack
          command: echo 'export DEBUG=1' >> "$BASH_ENV"
...
```

### Configuring a CI key

To enable LocalStack Pro+, you need to add your LocalStack CI Auth Token to the project's environment variables.
The LocalStack container will automatically pick it up and activate the licensed features.

Go to the [CI Auth Token page](https://app.localstack.cloud/workspace/auth-tokens) and copy your CI Auth Token.
To add the CI Auth Token to your CircleCI project, follow these steps:

- Click on **Project Settings**.
- Select **Environment Variables** from the left side menu.
- Click **Add Environment Variable**.
- Name your environment variable `LOCALSTACK_AUTH_TOKEN`.
- Paste your CI Auth Token into the input field.

After the above steps, just start up LocalStack using our official orb as usual.

### Dump LocalStack logs

```yaml
...
jobs:
  localstack-test:
    executor: localstack/default
    steps:
...
      - run:
          name: Dump LocalStack logs
          command: localstack logs | tee localstack.log
      - store_artifacts:
          path: localstack.log
          name: localstack-logs
...
```

### Store LocalStack state

You can preserve your AWS infrastructure with LocalStack in various ways.
To be able to use any of the below samples, you must [set a valid CI key](#configuring-a-ci-key).

_Note: For best result we recommend to use a combination of the below techniques and you should familiarise yourself with CircleCI's data persistance approach, see their [official documentation](https://circleci.com/docs/persist-data/)._

#### Cloud Pods

Cloud Pods providing an easy solution to persist LocalStack's state, even between workflows or projects.

Find more information about [Cloud Pods](/user-guide/state-management/cloud-pods/).

##### Multiple projects

Update or create the Cloud Pod in it's own project (ie in a separate Infrastructure as Code repo), this would create a base Cloud Pod, which you can use in the future without any configuration or deployment.

_Note: If there is a previously created Cloud Pod which doesn't need updating this step can be skipped._

```yaml
orbs:
  localstack: localstack/platform@2.2
...
jobs:
  localstack-update-cloud-pod:
    executor: localstack/default
    steps:
      ...
      # LocalStack already running
      - run:
        name: Load state if exists
        command: localstack pod load <POD_NAME> || true # Not allowed to fail yet
      ...
      # Deploy infrastructure changes
      ...
      - localstack/cloud_pods:
          pod_name: <POD_NAME>


workflows:
  localstack-build:
    jobs:
      - localstack-update-cloud-pod
```

In a separate project use the previously created base Cloud Pod as below:

```yaml
orbs:
  localstack: localstack/platform@2.2
...
jobs:
  localstack-use-cloud-pod:
    executor: localstack/default
    steps:
      ...
      # LocalStack already running
      - localstack/cloud_pods:
          pod_name: <POD_NAME>
          pod_action: load
      ...
      # Run some tests

workflows:
  localstack-build:
    jobs:
      - localstack-use-cloud-pod
```

##### Same project

To use a dynamically updated Cloud Pod in multiple workflows but in the same project, you must eliminate the race conditions between the update workflow and the others.

Before you are able to use any stored artifacts in your pipeline, you must provide either a valid [project API token](https://circleci.com/docs/managing-api-tokens/#creating-a-project-api-token) or a [personal API token](https://circleci.com/docs/managing-api-tokens/#creating-a-personal-api-token) to CircleCI.

```yaml
orbs:
  localstack: localstack/platform@2.2
...
parameters:
  run_workflow_build:
    default: true
    type: boolean

  run_workflow_test1:
    default: false
    type: boolean

  run_workflow_test2:
    default: false
    type: boolean
...


jobs:
  localstack-update-state:
    executor: localstack/default
    steps:
      ...
      # LocalStack already running
      - localstack/cloud_pods:
          pod_name: <POD_NAME>
          pod_action: load
      ...
      # Deploy infrastructure
      ...
      - localstack/cloud_pods:
          pod_name: <POD_NAME>
          pod_action: save  # Optional as this is the default
      - run:
          name: Trigger other workflows
          # Replace placeholders with right values
          command: |
            curl --request POST \
              --url https://circleci.com/api/v2/project/<vcs-slug>/<org-name>/<repo-name>/pipeline \
              --header 'Circle-Token: $CIRCLECI_TOKEN' \
              --header 'content-type: application/json' \
              --data '{"parameters":{"run_workflow_build":false, "run_workflow_test1":true, "run_workflow_test2":true}}'


  localstack-use-state:
    executor: localstack/default
    steps:
      ...
      # LocalStack already running
      - run:
        name: Load state if exists
        command: localstack pod load <POD_NAME> || true
      ...


# Example workflows
workflows:
  localstack-build:
    when: << pipeline.parameters.run_workflow_build >>
    jobs:
      - localstack-update-state
  localstack-test1:
    when: << pipeline.parameters.run_workflow_test1 >>
    jobs:
      - localstack-use-state
      ...
  localstack-test2:
    when: << pipeline.parameters.run_workflow_test2 >>
    jobs:
      - localstack-use-state
      ...
```

#### Ephemeral Instance (Preview)

Find out more about [Ephemeral Instances](/user-guide/cloud-sandbox/).

##### Same job

```yaml
orbs:
  localstack: localstack/platform@2.2
...
jobs:
  do-work:
    executor: localstack/default
    steps:
      - localstack/ephemeral:
          auto_load_pod: <POD_NAME>  # Pod to load (optional)
          # Commands to run (optional)
          preview-cmd: |
            awslocal sqs create-queue --queue-name=test-queue
            awslocal s3 mb s3://test-bucket
      - run:
        name: Output the ephemeral instance address
        command: echo "$AWS_ENDPOINT_URL"
...
workflows:
  use-ephemeral-instance:
    jobs:
      - do-work
...
```

##### Multiple jobs

```yaml
...
jobs:
  setup-instance:
    executor: localstack/default
    steps:
      - localstack/ephemeral:
          ephemeral_action: start
          # Script to run (optional)
          preview-cmd: bin/deploy.sh
      - run:
        name: Persist AWS Endpoint URL
        command: echo "export AWS_ENDPOINT_URL=$endpointUrl" >> ls-env-vars
      - persist_to_workspace:
          root: .
          paths:
            - ls-env-vars

  run-test:
    executor: localstack/default
    steps:
      - attach_workspace:
          at: .
      - run:
        name: Set up LS env variables
        command: cat ./ls-env-vars >> $BASH_ENV
      - run:
        name: Output the ephemeral instance address
        command: echo "$AWS_ENDPOINT_URL"
...
    # Run any logic against the Ephemeral Instance,
    # then stop when not needed anymore
      - localstack/ephemeral:
          ephemeral_action: stop

...
workflows:
  use-ephemeral-instance:
    jobs:
      - setup-instance
      - run-test
...
```

#### Workspace

This strategy persist LocalStack's state between jobs for the current workflow.

```yaml
...
jobs:
  localstack-save-state:
    executor: localstack/default
    steps:
      ...
      # LocalStack already running and deployed infrastructure
      - run:
          name: Export state
          command: localstack state export ls-state.zip
      - persist_to_workspace:
        paths:
          - ls-state.zip
      # Store state as artifact for local debugging
      - store_artifact:
          key: ls-state
          paths: ls-state.zip
...
  localstack-load-state:
    executor: localstack/default
    steps:
      ...
      # LocalStack already running
      - attach_workspace:
          at: .
      - run:
          name: Import state
          command: |
            test -f ls-state.zip && localstack state import ls-state.zip
...
  workflows:
  localstack-build:
    jobs:
      - localstack-save-state
      - localstack-load-state
```

More information about Localstack's [state import/export](/user-guide/state-management/export-import-state).

#### Cache

To preserve state between workflow runs, you can take leverage of CircleCI's caching too.
This strategy will persist LocalStack's state for every workflow re-runs, but not for different workflows.

```yaml
...
jobs:
  localstack-update-state:
    executor: localstack/default
    steps:
      ...
      # LocalStack already running
      # Let's restore previous workflow run's LocalStack state
      - restore_cache:
          # Use latest "ls-state" prefixed cache
          key: ls-state-
      - run:
          name: Import state
          command: test -f ls-state.zip && localstack state import ls-state.zip
      ...
      # Infrastructure had been updated
      # Let's update cached LocalStack state
      - run:
          name: Export state
          command: localstack state export ls-state.zip
      - save_cache:
          key: ls-state-{{checksum ls-state.zip}}
          paths: ls-state.zip
  ...
  localstack-do-work:
    executor: localstack/default
    steps:
      # LocalStack already running
      - restore_cache:
          # Use latest "ls-state" prefixed cache
          key: ls-state-
      - run:
          name: Import state
          command: test -f ls-state.zip && localstack state import ls-state.zip
      ...


# Example workflows
workflows:
  localstack-build:
    jobs:
      - localstack-update-state
      - localstack-do-work
      ...
```

More information about [state management](/user-guide/state-management/export-import-state).
