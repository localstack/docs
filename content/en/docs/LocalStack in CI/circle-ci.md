---
title: "CircleCI"
date: 2021-09-27
tags: ["continuous-integration", "ci", "continuous-delivery", "testing"] 
weight: 4
description: >
  Use LocalStack in [Circle CI](https://circleci.com/)
---

LocalStack is an official partner of [Circle CI](https://circleci.com/) and can easily be integrated into your pipeline by using the [official CircleCI Orb](https://circleci.com/developer/orbs/orb/localstack/platform).\
The [Orb's documentation](https://circleci.com/developer/orbs/orb/localstack/platform) features examples, as well as a description of the available commands.

When using the official CircleCI Orb, using LocalStack in your pipeline is as easy as adding the Orb to your pipeline and executing the startup command.\
The following example starts localstack, creates a new S3 bucket, and prints a nice message in the end:
```yaml
version: 2.1
orbs:
  localstack: localstack/platform@1.0
jobs:
  run-integration-tests:
    executor: localstack/default
    steps:
      - localstack/startup
      - run:
          command: awslocal s3 mb s3://test-bucket
      - run:
          command: echo "Execute your tests here :)"
workflows:
  integration-test:
    jobs:
      - run-integration-tests
```

## Ran into trouble?

If you run into any issues or problems while integrating LocalStack with CircleCI, please [submit an issue](https://github.com/localstack/ci-plugin-circleci/issues).
