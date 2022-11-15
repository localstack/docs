---
title: "LocalStack in CI"
linkTitle: "LocalStack in CI"
weight: 3
description: >
  Using LocalStack in your Continuous Integration (CI) workflows
cascade:
  type: docs
slug: ci
---

LocalStack enables organizations to automate their application testing and integration process through DevOps practices, such as continuous integration (CI). To meet your organizational needs, LocalStack lets you move away from complicated AWS testing and staging environments by enabling a key component of testing and delivering cloud-native applications. 

You can easily integrate LocalStack with your existing CI platform. We provide native plugins for CircleCI and a generic driver for any other CI platform you might use. This enables you to incorporate LocalStack's local AWS cloud emulation in your CI pipelines, use advanced features like Cloud Pods and CI analytics, and run your test & integration suite before pushing to production. 

## Hypothetical CI workflow

Let's assume that your team has an automated CI workflow into which you want to integrate end-to-end cloud testing with LocalStack. As an example, consider the following pipeline, which represents part of a simple CI workflow:

{{< figure src="localstack-in-ci.svg" alt="An example CI/CD workflow using LocalStack" width="90%">}}

The CI build is triggered by pushing code to a version control repository, like GitHub. The CI runner starts LocalStack and executes the test suite. You can also use the same Infrastructure-as-Code (IaC) configuration that you use to set up AWS in your production environment to set up LocalStack in the CI environment. You can also pre-seed state into the local AWS services (e.g., DynamoDB entries or S3 files) provided by LocalStack in your CI environment via [Cloud Pods](https://docs.localstack.cloud/tools/cloud-pods/). 

After a successful test run, you can execute the more expensive AWS CodeBuild pipeline for deploying your application. You can enrich the test reports created by your testing framework with traces and analytics generated inside LocalStack.

## CI Credits

A _CI key_ is a special type of API key that allows you to use LocalStack in your CI environment. Each key activation, i.e., each single startup of the LocalStack container in your CI environment, consumes one build credit. LocalStack Pro offers a CI key with a limited number of build credits to help you start experimenting with larger CI settings. LocalStack Team is focused on using LocalStack on individual user machines, across teams, and in larger CI settings to help teams collaborate and use LocalStack extensively in CI.

The Pro subscription is mainly intended for use on individual user machines. We recommend our Team plan if you intend to use LocalStack extensively for team collaboration and in CI environments. For the CI environment, each subscription (both Pro and Team) comes with one extra CI key (included in the subscription at no extra charge), which allows you to use LocalStack in your CI environment. The CI key has a certain number of credits, depending on the number of individual user seats and the plan you have purchased.

## CI integrations

The steps required for the integration differ slightly depending on your preferred CI platform. Please refer to the relevant sections below for detailed instructions on the integration process. To follow the instructions, you can first retrieve the CI key from the Account settings page in the [LocalStack Web app](https://app.localstack.cloud).
