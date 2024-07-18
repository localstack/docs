---
title: "Continuous Integration"
linkTitle: "Continuous Integration"
weight: 3
description: >
  Run LocalStack in your CI environment to test your application against a high-fidelity cloud emulator
cascade:
  type: docs
slug: ci
---

LocalStack enables organizations to automate their application testing and integration process through DevOps practices, such as continuous integration (CI).
To meet your organizational needs, LocalStack lets you move away from complicated AWS testing and staging environments by enabling a key component of testing and delivering cloud-native applications.

You can easily integrate LocalStack with your existing CI platform.
We provide native plugins for CircleCI and a generic driver for any other CI platform you might use.
This enables you to incorporate LocalStack's local AWS cloud emulation in your CI pipelines, use advanced features like Cloud Pods and CI analytics, and run your test & integration suite before pushing to production.

## Hypothetical CI workflow

Let's assume that your team has an automated CI workflow into which you want to integrate end-to-end cloud testing with LocalStack.
As an example, consider the following pipeline, which represents part of a simple CI workflow:

{{< figure src="localstack-in-ci.svg" alt="An example CI/CD workflow using LocalStack" width="90%">}}

The CI build is triggered by pushing code to a version control repository, like GitHub.
The CI runner starts LocalStack and executes the test suite.
You can also use the same Infrastructure-as-Code (IaC) configuration that you use to set up AWS in your production environment to set up LocalStack in the CI environment.
You can also pre-seed state into the local AWS services (e.g., DynamoDB entries or S3 files) provided by LocalStack in your CI environment via [Cloud Pods]({{< ref "user-guide/state-management/cloud-pods" >}}).

After a successful test run, you can execute the more expensive AWS CodeBuild pipeline for deploying your application.
You can enrich the test reports created by your testing framework with traces and analytics generated inside LocalStack.

## CI integrations

The steps required for the integration differ slightly depending on your preferred CI platform.
Please refer to the relevant sections of the [CI keys settings page](https://app.localstack.cloud/workspace/ci-keys) in the [LocalStack Web app](https://app.localstack.cloud).

## CI images

LocalStack Docker images can be used in your CI environment by adding a CI Key.
The images are available on [Docker Hub](https://hub.docker.com/r/localstack/localstack/tags), and comprehensive documentation is available on our [Docker images](https://docs.localstack.cloud/references/docker-images/) documentation.
Community users can use the `localstack/localstack` image, while licensed users can use the `localstack/localstack-pro` image.
For Big Data jobs that require services such as EMR, Athena, and Glue, we provide a mono-container that uses the `localstack/localstack-pro:2.0.2-bigdata` image, which bakes in the required dependencies, such as Hadoop, Hive, Presto, into the LocalStack image.
