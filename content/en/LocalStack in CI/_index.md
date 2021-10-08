---
title: "LocalStack in CI"
linkTitle: "LocalStack in CI"
weight: 20
description: >
  Using LocalStack in your Continuous Integration workflow
cascade:
  type: docs
---

LocalStack is key component of testing and delivering cloud-native applications in Continuous Integration/Delivery pipelines without complicated AWS testing and staging environments.

## Example workflow

The following image shows an example workflow.
The CI build is triggered through pushing code to the version control repository.
The CI runner starts LocalStack and executes the test suite.
The same Infrastructure-as-Code (IaC) configuration that sets up AWS in your production environment can be used to set up LocalStack in the CI environment.
LocalStack [Cloud Pods]({{< ref "cloud-pods" >}}) can be used to pre-seed state into the services (e.g., DynamoDB entries, or S3 files).
The tests then execute the application in the cloud environment emulated by LocalStack.
After a successful test run, the more expensive AWS CodeBuild pipeline for deploying your application can be executed.
The test reports created by your testing framework can be enriched with traces and analytics generated inside LocalStack.

{{< figure src="localstack-in-ci.svg" alt="An example CI/CD workflow using Localstack" width="70%">}}


## Running LocalStack in CI environments

It is easy to run LocalStack in your CI runners.
For some CI environments, for example Circle CI, we provide plugins that allow seamless integration of LocalStack in your workflow.
But LocalStack can work in any CI environment, and we have several examples in the sections below.
