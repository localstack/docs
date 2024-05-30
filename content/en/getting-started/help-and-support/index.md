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

We strive to make it as easy as possible for you to use LocalStack, and we are very grateful for any feedback. We provide different levels of support to help you with your queries and issues. The support you receive depends on the plan you are on.

| Plan | Support Level |
|------|---------------|
| Community Edition | [Community Support](#community-support) |
| Hobby Plan | [Community Support](#community-support) |
| Starter Plan | [Dedicated Support](#dedicated-support) |
| Teams Plan | [Dedicated Support](#dedicated-support) |
| Enterprise Plan | [Enterprise Support](#enterprise-support) |

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

Dedicated customer support is available to **Starter** & **Teams** plan users with an active subscription.

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

To create a support ticket:

- Search for the **LocalStack Pro Support** in our [Slack Community](https://localstack.cloud/slack).
- Navigate to **Messages** and type your message to LocalStack Pro Support.

Sending a message to LocalStack Pro Support will create a support ticket, and our support team will respond to your request as quickly as possible.

### LocalStack Web Application

To create a support ticket:

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

## Enterprise Support

A customer portal is a home behind a login where customers can view, open, and reply to their support tickets. Currently, the **customer portal** is only **available to Enterprise customers**.

You can find the customer portal here: [https://support.localstack.cloud/portal](https://support.localstack.cloud/portal)

<p>
{{< img src="customer-portal.png" alt="Customer portal for enterprise support" class="img-fluid shadow rounded" width="800px" >}}
</p>

### Signing up for Enterprise Support

If you are a member of an organization with an enterprise LocalStack subscription, you will receive an invitation to create an account and join the LocalStack Support Portal via email.

Follow the instructions in the email and set up your account by clicking on the **Sign up** button. You will be asked to create a password. Once you do so, you will be able to log in and start using the customer portal to create, view, and engage with tickets.

### Creating a Support Ticket

You can open a new ticket with LocalStack support by going to the **Create a Support Ticket** link. You will be redirected to a form where you will have to provide certain information to file a new support ticket.

<p> 
{{< img src="file-a-support-ticket.png" alt="Filing a support ticket" class="img-fluid shadow rounded" width="800px" >}} 
</p>

The form consists of two parts. One is basic information, which is mandatory to fill out, and additional information, which adds more context to your issue but is not mandatory. Once all the mandatory fields are filled out, you can create a new support ticket by clicking on the Submit button. Once the ticket is submitted, it will be reported to LocalStack support, who will get back to you on that query as soon as possible. A ticket will show up in the ticket list as soon as it’s submitted.

#### Basic Information

You need to fill out the following fields, which are mandatory to open a new ticket:

-   **Type** - Choose the type of your query from the following options:
    -   **Issue** - Select this when you are facing an issue using LocalStack.
    -   **General inquiry** - Select this when you have a general question regarding LocalStack.
    -   **Feature request** - Select this when you are looking for a feature that is not yet implemented in LocalStack.
-   **Ticket name** - Provide a descriptive name for the ticket that summarizes your inquiry.
-   **Description** - Provide a comprehensive description of your inquiry, explaining all the details that will help us understand your query.

#### Additional Information

-   **CI Issue?** - If the query is related to a CI issue, select the one that best fits your query from the dropdown.
-   **Operating system** - From the dropdown, select the operating system you are using.
-   **Affected Services** - From the dropdown, select the AWS service that is affected in your query.
-   **File upload** - Here you can provide any additional files that you believe would be helpful for LocalStack support (e.g., screenshots, log files, etc.).