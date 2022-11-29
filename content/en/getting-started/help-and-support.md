---
title: "Help & Support"
linkTitle: "Help & Support"
weight: 7
description: >
  This page outlines how to get help and support while using LocalStack.
cascade:
  type: docs
---

We strive to make it as easy as possible for you to use LocalStack, and we are very grateful for any feedback. To report issues, we use [GitHub Issues](https://github.com/localstack/localstack/issues/new/choose) and [Discussion Pages](https://discuss.localstack.cloud/). For Community & Professional Support, we intend to use our [Slack Community](https://slack.localstack.cloud).

## Report an issue

Our LocalStack repository is open source and hosted on GitHub. You can request for [new features](https://github.com/localstack/localstack/issues/new?assignees=&labels=type%3A+feature%2Cstatus%3A+triage+needed&template=feature-request.yml&title=feature+request%3A+%3Ctitle%3E) or [report existing bugs](https://github.com/localstack/localstack/issues/new?assignees=&labels=type%3A+bug%2Cstatus%3A+triage+needed&template=bug-report.yml&title=bug%3A+%3Ctitle%3E). Mmake sure to follow the issue templates and provide as much information as possible. If you have discovered outdated documentation, please [submit an issue](https://github.com/localstack/docs/issues/new) on our open-source [docs repository](https://github.com/localstack/docs). We will take up your issues on priority and try to resolve them as soon as possible.

## Create a Discussion

We have a [Discussions Page](https://discuss.localstack.cloud/) where you can ask questions, share ideas, and discuss about LocalStack. Discussion Pages are used for general feature requests, best practice and usage related questions, and should serve as a comprehensive archive useful to the growing community over time. We also use Discussion Pages for [product-related announcements](https://discuss.localstack.cloud/c/announcement/5).

## Community support

We have a [Slack Community](https://slack.localstack.cloud) where you can get community support. Our Slack community comprises of LocalStack users, contributors, and maintainers. Please use `#community-support` channel to get help and support with LocalStack community version.

## Pro support

Our support engineers provide Pro support to LocalStack Pro users. Pro support entails service issues, LocalStack-specific configurations, and other technical issues that might concern with how LocalStack is expected to behave. Pro support does not include support for AWS services, or general troubleshooting of your application. We also don't intend to support on any product billing or account related questions. We encourage you to reach out to us on [info@localstack.cloud](mailto:info@localstack.cloud) for any such non-techincal queries.

To avail Pro support, please search **LocalStack Pro Support** application on our Slack community. Navigate to `Messages` and type your message to LocalStack Pro Support. To ensure we get back to you as soon as possible, please provide as much information as possible, including your LocalStack setup, a reproducible example, the steps we need to follow and any other relevant information to help us replicate the scenario. 

In many scenarios, we ask our customers to use Diagnosis endpoint to help us retrieve additional information. To activate it:

- Set the environment variable `LS_LOG=trace`
- Start LocalStack
- Run the affected task(s)
- Call the diagnostic endpoint `curl -s localhost:4566/_localstack/diagnose | gzip -cf > diagnose.json.gz`
- Send the output file to our Slack chat
