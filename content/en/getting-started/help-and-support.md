---
title: "Help & Support"
linkTitle: "Help & Support"
weight: 60
description: >
  This page outlines how to get help and support while using LocalStack.
cascade:
  type: docs
---

## Introduction

We strive to make it as easy as possible for you to use LocalStack, and we are very grateful for any feedback.

## Community Support

LocalStack's Community support is available to all users of the LocalStack Community Edition & Hobby Plan users. You can avail community support through the following channels:

- [LocalStack Discuss](https://discuss.localstack.cloud/)
- [LocalStack Slack Community](https://localstack.cloud/slack)
- [GitHub Issue](https://github.com/localstack/docs/issues/new)

Community support is provided on a best-effort basis and is not guaranteed. We also encourage you to help others in the community by answering questions and sharing your experiences.

### LocalStack Discuss

LocalStack Discuss allows our community users to ask questions, share ideas, and discuss topics related to LocalStack. To create a new topic on Discuss, follow these steps:

- Create a new account on [LocalStack Discuss](https://discuss.localstack.cloud/) by clicking the **Sign Up** button.
- Once you have created an account, you can create a new topic by clicking the **New Topic** button.
- Choose the appropriate category for your topic and provide a title and description.
- Click the **Create Topic** button to submit your topic.

LocalStack Discuss is public, allowing us to keep a record of these questions and answers for the larger community to use over time. However, you should avoid sharing any sensitive information on the platform (such as Auth Tokens, private configuration, etc.).

### LocalStack Slack Community

LocalStack Slack Community includes LocalStack users, contributors, and maintainers. If you need help with the community version of LocalStack, please use the `#help` channel. You can sign up for the [LocalStack Slack Community](https://localstack.cloud/slack) by creating an account.

However, the messages on Slack are not accessible after three months, so it is not the best place to ask questions that may be useful to others in the future. For that, we recommend using LocalStack Discuss.

### GitHub Issue

You can use GitHub Issue to:

- [Request new features](https://github.com/localstack/localstack/issues/new?assignees=&labels=type%3A+feature%2Cstatus%3A+triage+needed&template=feature-request.yml&title=feature+request%3A+%3Ctitle%3E)
- [Report existing bugs](https://github.com/localstack/localstack/issues/new?assignees=&labels=type%3A+bug%2Cstatus%3A+triage+needed&template=bug-report.yml&title=bug%3A+%3Ctitle%3E)

Make sure to follow the issue templates and provide as much information as possible. If you have encountered outdated documentation, please report it on our [documentation GitHub page](https://github.com/localstack/docs).

## Dedicated support

Dedicated customer support is available to all the LocalStack users with an active subscription.

The support team is available to help you with:

- Troubleshooting LocalStack issues
- Answering questions about LocalStack features and functionality
- Providing guidance on how to use LocalStack
- Providing guidance on how to integrate LocalStack with your application

However, dedicated support does not include:

- Support for AWS services
- General troubleshooting of your application
- Billing, account issues, or other questions that are not technical

If you have questions about billing, account issues, or other questions that are not technical, please contact us at [support@localstack.cloud](mailto:support@localstack.cloud) or through our [contact form](https://localstack.cloud/contact/).

You can avail dedicated support through the following channels:

- [LocalStack Slack Bot](https://localstack.cloud/slack)
- [LocalStack Web Application](https://app.localstack.cloud)

### LocalStack Slack Bot

LocalStack Slack Bot is available to all licensed users. To create a support ticket:

- Search for the **LocalStack Pro Support** in our [Slack Community](https://localstack.cloud/slack).
- Navigate to **Messages** and type your message to LocalStack Pro Support.

Sending a message to LocalStack Pro Support will create a support ticket, and our support team will respond to your request as quickly as possible.

### LocalStack Web Application

LocalStack Web Application is available to all licensed users. To create a support ticket:

- Navigate to the [LocalStack Web Application](http://app.localstack.cloud).
- Click on the chat icon in the bottom right corner of the page.
- Select **Technical Question** from the menu.
- Fill in the required details and send your message.

You can optionally choose to continue the conversation via email or via the Web Application.

{{< callout "note" >}}
In many scenarios, we ask our customers to use Diagnosis endpoint to help us retrieve additional information. To use LocalStack's Diagnosis endpoint:

- Set the environment variable `LS_LOG=trace`
- Start LocalStack
- Run the affected task(s)
- Call the diagnostic endpoint  `curl -s localhost:4566/_localstack/diagnose | gzip -cf > diagnose.json.gz` (Endpoint URL depends on your configuration)
- Send the output file to our Slack chat

Ensure that you avoid sending the diagnostic output to public channels or forums, as it may contain sensitive information.
{{< /callout >}}
