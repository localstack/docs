---
title: "Sample"
linkTitle: "Sample"
weight: 5
description: >
  Localstack Sample Project in Github Actions
aliases:
  - /ci/github-actions/samples
tags: ["continuous-integration", "ci", "continuous-delivery", "testing","github-actions","sample"]
---

This page containes our Quickstart project's test pipeline implemented in Github actions.

# Serverless image resizer s3 lambda
This is an app to resize images uploaded to S3 in a serverless way.
Find code in repo [here](https://github.com/localstack-samples/sample-serverless-image-resizer-s3-lambda).

## Integration testing
A build matrix for Ubuntu and MacOS to run integration tests triggered by various ways.
In case of failure the pipeline dumps the logs of Localstack and preserves them as artifacts for further investigations.

```
name: Run Integration Tests

on:
  push:
    paths-ignore:
      - 'README.md'
    branches:
      - main
  pull_request:
    branches:
      - main
  schedule:
    # “At 00:00 on Sunday.”
    - cron: "0 0 * * 0"
  workflow_dispatch:

jobs:
  run-it-tests-job:
    strategy:
      matrix:
        os: [macos-latest, ubuntu-latest]
    runs-on: ${{ matrix.os }}
    steps:
      - name: Checkout
        uses: actions/checkout@v2

      - name: Set up Python 3.9
        id: setup-python
        uses: actions/setup-python@v2
        with:
          python-version: 3.9

      - name: Docker setup (macos only)
        id: setup-docker-mac
        if: ${{ runner.os == 'macOS' }}
        run: |
          brew install docker
          colima start

      - name: Set up Project
        run: |
          pip install -r requirements-dev.txt

      - name: Start LocalStack
        uses: LocalStack/setup-localstack@main
        with:
          image-tag: 'latest'
          use-pro: 'true'
          configuration: LS_LOG=trace
          install-awslocal: 'true'
        env:
          LOCALSTACK_API_KEY: ${{ secrets.LOCALSTACK_API_KEY }}

      - name: Deploy infrastructure
        run: |
          bin/deploy.sh

      - name: Run Tests
        env:
          AWS_DEFAULT_REGION: us-east-1
          AWS_REGION: us-east-1
          AWS_ACCESS_KEY_ID: test
          AWS_SECRET_ACCESS_KEY: test
        run: |
          pytest tests

      - name: Show localstack logs
        if: always()
        run: |
          localstack logs

      - name: Send a Slack notification
        if: failure() || github.event_name != 'pull_request'
        uses: ravsamhq/notify-slack-action@v2
        with:
          status: ${{ job.status }}
          token: ${{ secrets.GITHUB_TOKEN }}
          notification_title: "{workflow} has {status_message}"
          message_format: "{emoji} *{workflow}* {status_message} in <{repo_url}|{repo}>"
          footer: "Linked Repo <{repo_url}|{repo}> | <{run_url}|View Workflow run>"
          notify_when: "failure"
        env:
          SLACK_WEBHOOK_URL: ${{ secrets.SLACK_WEBHOOK_URL }}

      - name: Generate a Diagnostic Report
        if: failure()
        run: |
          curl -s localhost:4566/_localstack/diagnose | gzip -cf > diagnose.json.gz

      - name: Upload the Diagnostic Report
        if: failure()
        uses: actions/upload-artifact@v3
        with:
          name: diagnose.json.gz
          path: ./diagnose.json.gz
```

## Cloud pod testing
Cloud pods providing a quick and easy way to test newly written tests against existing infrastructure or deployed code.
This can be stored locally, like we did below, or remotely in our Web Application.
Find more information on them [here](/user-guide/state-management/cloud-pods/).

### Create pods
Preserves infrastructure and deployed code for different versions.

```
on:
  workflow_dispatch:
    inputs:
      release-tag:
        type: string
        required: true
        description: This will be the version of the release, but will also be used as 'tag' for the localstack docker image
  push:
    paths-ignore:
      - 'README.md'
    branches:
      - main
            
permissions:
  contents: write

name: Create Release
jobs:
  release:
    name: Create Release for Cloud Pod
    runs-on: ubuntu-latest
    steps:
      - name: Checkout
        uses: actions/checkout@v2

      - name: Set up Python 3.9
        id: setup-python
        uses: actions/setup-python@v2
        with:
          python-version: 3.9

      - name: Set up Project
        run: |
          pip install -r requirements-dev.txt

      - name: Start LocalStack
        uses: LocalStack/setup-localstack@main
        with:
          image-tag: ${{ inputs.release-tag || 'latest'}}
          use-pro: 'true'
          install-awslocal: 'true'
        env:
          LOCALSTACK_API_KEY: ${{ secrets.LOCALSTACK_API_KEY }}

      - name: Deploy infrastructure
        run: |
          bin/deploy.sh

      - name: Run Tests
        env:
          AWS_DEFAULT_REGION: us-east-1
          AWS_REGION: us-east-1
          AWS_ACCESS_KEY_ID: test
          AWS_SECRET_ACCESS_KEY: test
        run: |
          pytest tests
      
      - name: Save the Cloud Pod 
        env:
          LOCALSTACK_API_KEY: ${{ secrets.LOCALSTACK_API_KEY }}
        run: | 
          localstack state export release-pod.zip

      - name: Prepare Release Notes
        run: |
          echo "This release includes the Cloud Pod of the sample created with LocalStack Version \`${{ inputs.release-tag || 'latest'}}\`." > Release.txt
          echo "You can download the \`release-pod.zip\` and inject it manually by running \`localstack state import release-pod.zip\`, or use the Cloud Pods Launchpad." >> Release.txt
          echo "### Cloud Pods Launchpad" >> Release.txt
          echo "You can click the Launchpad to inject the the pod into your running LocalStack instance using the WebUI:" >> Release.txt
          echo "[![LocalStack Pods Launchpad](https://localstack.cloud/gh/launch-pod-badge.svg)](https://app.localstack.cloud/launchpad?url=https://github.com/$GITHUB_REPOSITORY/releases/download/${{ inputs.release-tag || 'latest'}}/release-pod.zip)" >> Release.txt

      - name: Create Release
        id: create_release
        uses: softprops/action-gh-release@v1
        with:
          tag_name: "${{ inputs.release-tag || 'latest'}}"
          name: "Cloud Pod for LocalStack Version '${{ inputs.release-tag || 'latest'}}'"
          body_path: ./Release.txt
          files: |
              ./release-pod.zip
```

### Test pods
To test the saved Cloud Pods we take all the existing releases and loading back the related cloud pods saved in the previous workflow into Localstack to check their validity against our integration tests.

```
name: Test Released Cloud Pods

on:
  schedule:
    # “At 00:00 on Saturday.”
    - cron: "0 0 * * 6"
  workflow_dispatch:

permissions:
  contents: write

jobs:
  get-releases:
    name: Retrieve Released Cloud Pods
    runs-on: ubuntu-latest
    outputs:
      matrix: ${{ steps.set-matrix.outputs.matrix }}
    steps:
    - id: set-matrix
      env:
        GITHUB_TOKEN: ${{ secrets.GITHUB_TOKEN }}
      run: |
        output=$(gh api repos/$GITHUB_REPOSITORY/releases | jq -r '[.[] | select(.tag_name|startswith("v")|not) | .tag_name]')
        output=$(echo $output | tr '\n' ' ')
        echo "matrix=$output" >> $GITHUB_OUTPUT
  
  test-pod-release:
    needs: get-releases
    runs-on: ubuntu-latest
    strategy:
      fail-fast: false
      matrix: 
        tag: ${{ fromJson(needs.get-releases.outputs.matrix) }}
    steps:
      # checkout to run the tests later on
      - name: Checkout
        uses: actions/checkout@v3

      - name: Retrieve Pod
        env:
          GITHUB_TOKEN: ${{ secrets.GITHUB_TOKEN }}
        run: |
          # TODO the download url seems to follow the pattern $GITHUB_REPOSITORY/releases/download/{TAG}/{ASSET_NAME}
          # alternatively we can query the asset-id, and browser_download_url, but it seems like an overhead
          # asset_id=$(gh api repos/$GITHUB_REPOSITORY/releases/tags/latest | jq -r '.assets[]' | jq --arg DB $DB -c 'select(.name=="release-pod-\( $DB ).zip") | .id)
          # download_url=$(gh api repos/$GITHUB_REPOSITORY/releases/assets/$asset_id | jq -r ".browser_download_url")
          download_url="https://github.com/$GITHUB_REPOSITORY/releases/download/${{ matrix.tag }}/release-pod.zip"
          curl -L $download_url --output release-pod.zip
          ls -la

      - name: Setup Python
        uses: actions/setup-python@v4
        with:
          python-version: '3.9'

      - name: Start LocalStack
        uses: LocalStack/setup-localstack@main
        with:
          image-tag: ${{ matrix.tag }}
          use-pro: 'true'
          install-awslocal: 'true'
        env:
          DEBUG: 1
          POD_LOAD_CLI_TIMEOUT: 300
          LOCALSTACK_API_KEY: ${{ secrets.LOCALSTACK_API_KEY }}

      - name: Inject Pod
        env:
          LOCALSTACK_API_KEY: ${{ secrets.LOCALSTACK_API_KEY }}
        run: |
          localstack state import release-pod.zip

      - name: Run Tests
        env:
          AWS_DEFAULT_REGION: us-east-1
          AWS_REGION: us-east-1
          AWS_ACCESS_KEY_ID: test
          AWS_SECRET_ACCESS_KEY: test
        run: |
          pip install -r requirements-dev.txt
          pytest tests

      - name: Show Logs
        if: failure()
        run: |
          localstack logs

      - name: Send a Slack notification
        if: failure() || github.event_name != 'pull_request'
        uses: ravsamhq/notify-slack-action@v2
        with:
          status: ${{ job.status }}
          token: ${{ secrets.GITHUB_TOKEN }}
          notification_title: "{workflow} has {status_message}"
          message_format: "{emoji} *{workflow}* {status_message} in <{repo_url}|{repo}>"
          footer: "Linked Repo <{repo_url}|{repo}> | <{run_url}|View Workflow run>"
          notify_when: "failure"
        env:
          SLACK_WEBHOOK_URL: ${{ secrets.SLACK_WEBHOOK_URL }}

      - name: Prevent Workflows from getting Stale
        if: always()
        uses: gautamkrishnar/keepalive-workflow@v1
        with:
          # this message should prevent automatic triggering of workflows
          # see https://docs.github.com/en/actions/managing-workflow-runs/skipping-workflow-runs
          commit_message: "[skip ci] Automated commit by Keepalive Workflow to keep the repository active"
```

## Preview application
Application Preview allows you to generate an preview environment from GitHub Pull Request (PR) builds.
To communicate with the ephemeral instance use it's address as an AWS endpoint URL from your local environment.
For more information please read the related section [here](https://docs.localstack.cloud/user-guide/cloud-sandbox/application-previews/).

### Create preview
The pipeline creates a preview environment by deploying the application for every pull requests.
```
name: Create PR Preview

on:
  pull_request:
    types: [opened, synchronize, reopened]

jobs:
  test:
    runs-on: ubuntu-latest
    timeout-minutes: 15
    permissions:
      pull-requests: write
    steps:
      - name: Checkout
        uses: actions/checkout@v4

      - name: Set up Python 3.9
        id: setup-python
        uses: actions/setup-python@v2
        with:
          python-version: 3.9

      - name: Install dependencies
        run: |
          pip install awscli-local

      - name: Deploy Preview
        uses: LocalStack/setup-localstack/preview@main
        env:
          AWS_DEFAULT_REGION: us-east-1
          AWS_REGION: us-east-1
          AWS_ACCESS_KEY_ID: test
          AWS_SECRET_ACCESS_KEY: test
        with:
          github-token: ${{ secrets.GITHUB_TOKEN }}
          localstack-api-key: ${{ secrets.LOCALSTACK_API_KEY }}
          preview-cmd: |
            # Add your custom deployment commands here. 
            # Below is an example for the Image resizer application.
            bin/deploy.sh  
```

### Attach preview URL
It attaches the Preview URL to the pull request.
```
name: Finalize PR Preview

on:
  workflow_run:
    workflows: ["Create PR Preview"]
    types:
      - completed

jobs:
  test:
    runs-on: ubuntu-latest
    permissions:
      pull-requests: write
    steps:
      - name: Finalize PR comment
        uses: LocalStack/setup-localstack/finish@main
        with:
          github-token: ${{ secrets.GITHUB_TOKEN }}
          include-preview: true
```