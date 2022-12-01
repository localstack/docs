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

Our LocalStack repository is open source and hosted on GitHub. You can request for [new features](https://github.com/localstack/localstack/issues/new?assignees=&labels=type%3A+feature%2Cstatus%3A+triage+needed&template=feature-request.yml&title=feature+request%3A+%3Ctitle%3E) or [report existing bugs](https://github.com/localstack/localstack/issues/new?assignees=&labels=type%3A+bug%2Cstatus%3A+triage+needed&template=bug-report.yml&title=bug%3A+%3Ctitle%3E). Make sure to follow the issue templates and provide as much information as possible. If you have discovered outdated documentation, please [submit an issue](https://github.com/localstack/docs/issues/new) on our open-source [docs repository](https://github.com/localstack/docs).

## Create a Discussion

[LocalStack Discuss](https://discuss.localstack.cloud/) is a place where you can ask questions, share ideas, and discuss topics related to LocalStack. The Discussion pages are used to ask questions about best practices and how to use the LocalStack, general [feature requests](https://discuss.localstack.cloud/c/feature-requests/6), as well as keeping a record of these questions and answers for the larger community to use over time. You can find the latest product announcements on the [Announcements page](https://discuss.localstack.cloud/c/announcement/5).

## Community support

We have a [Slack Community](https://join.slack.com/t/localstack-community/shared_invite/zt-1d6ehd69s-g80yLgfrXNKsQU_nmgNafg) where you can get help from other members of the community. The LocalStack Slack community includes LocalStack users, contributors, and maintainers. If you need help with the community version of LocalStack, please use the `#community-support` [channel](https://localstack-community.slack.com/archives/CMAFN2KSP).

## Pro support

The LocalStack Support Team provides comprehensive support on the best effort basis, for all technical issues that may arise, including product issues, LocalStack-specific configurations, and other technical issues that might concern with how LocalStack is expected to behave. Pro support does not include support for AWS services, or general troubleshooting of your application. If you have questions about billing, account issues, or other questions that are not technical, please contact us at [info@localstack.cloud](mailto:info@localstack.cloud) or through our [contact form](https://localstack.cloud/pricing/).

To take advantage of Pro support, please search for the LocalStack Pro Support application on our Slack community. Navigate to 'Messages' and type your message to LocalStack Pro Support. We will do our best to respond to your request as quickly as possible if you could provide us with the information we require. This includes your LocalStack setup, a step-by-step example, and any other information you can provide to help us reproduce the issue. Kindly note that the communication between the support team and the customer is private and only visible to the support team and the customer.

In many scenarios, we ask our customers to use Diagnosis endpoint to help us retrieve additional information. To use LocalStack's Diagnosis endpoint:

- Set the environment variable `LS_LOG=trace`
- Start LocalStack
- Run the affected task(s)
- Call the diagnostic endpoint  `curl -s localhost:4566/_localstack/diagnose | gzip -cf > diagnose.json.gz`  (Endpoint URL depends on your configuration)
- Send the output file to our Slack chat
