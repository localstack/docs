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

Our support team is here to assist with:

- LocalStack issues troubleshooting
- Questions about features and functionality
- Help integrating LocalStack with your application
- Guidance on using LocalStack

However, technical support does not cover:

- Support for AWS services
- General troubleshooting of your application
- Billing, account-related issues, or non-technical questions

For operational support related to billing, account inquiries, or other non-technical matters, contact us at [support@localstack.cloud](mailto:support@localstack.cloud) or via our [contact form](https://localstack.cloud/contact/).

## Support Coverage

| Plan                | Support Level                                            |
|---------------------|----------------------------------------------------------|
| Community Edition    | [Basic Support](#basic-support)                          |
| Hobby Plan           | [Basic Support](#basic-support)                          |
| Trial Plan           | [Standard Support](#standard-support)                    |
| Starter Plan         | [Standard Support](#standard-support)                    |
| Teams Plan           | [Priority Support](#priority-support)                    |
| Enterprise Plan      | [Enterprise Support](#enterprise-support)                |

## Support features

| Features                     | Basic | Standard | Priority | Enterprise |
| ---------------------------- | ----- | -------- | -------- | ---------- |
| LocalStack documentation     | ✅    | ✅       | ✅       | ✅         |
| Community support            | ✅    | ✅       | ✅       | ✅         |
| Operational support          | ✅    | ✅       | ✅       | ✅         |
| 1v1 technical support        |       | ✅       | ✅       | ✅         |
| Screen sharing sessions      |       |          | ✅       | ✅         |
| Third-Party Tools            |       |          | ✅       | ✅         |
| Faster response times        |       |          | ✅       | ✅         |
| Real-time chat support\*     |       |          |          | ✅         |
| Support ticketing portal     |       |          |          | ✅         |
| SLAs                         |       |          |          | ✅         |
| Direct Slack connect channel |       |          |          | ✅         |
| Dedicated CSM and AM         |       |          |          | ✅         |

- Real time chat support is offered during our [Support Business Hours](#support-business-hours)

## Support channels

| Channels              | Basic | Standard | Priority | Enterprise |
| --------------------- | ----- | -------- | -------- | ---------- |
| Slack community       | ✅    | ✅       | ✅       | ✅         |
| GitHub Issues         | ✅    | ✅       | ✅       | ✅         |
| Support email         |       | ✅       | ✅       | ✅         |
| Slack support bot     |       | ✅       | ✅       | ✅         |
| Web Application chat          |       | ✅       | ✅       | ✅         |
| Ticketing portal      |       |          |          | ✅         |
| Slack connect channel |       |          |          | ✅         |

## Support plans

Find the details about different support services and what they entitle bellow.
Please refer to the [Support Features](#support-features) to see which features are included in each plan.

### Basic support

Basic Support is included for all LocalStack users, and provides access to our documentation, community support, account management support (operational support).

You can avail community support through the following channels:

- [LocalStack Discuss](https://discuss.localstack.cloud/)
- [LocalStack Slack Community](https://localstack.cloud/slack)
- [GitHub Issue](https://github.com/localstack/docs/issues/new)

Community support is provided on a best-effort basis and is not guaranteed.
We also encourage you to help others in the community by answering questions and sharing your experiences.

### Standard support

Standard support is available to all LocalStack users with an active Starter or Trial subscription.
With standard support, you get access to 1v1 support based on best effort basis.
With the best effort support, we do not provide fixed response times.
However, as we understand the importance of timely assistance, our support team always strives to respond to inquiries and requests within 24–48 hours during our [regular business hours](#support-business-hours).

#### Troubleshooting Guidelines

In case you encounter any issues with LocalStack, follow these troubleshooting guidelines:

- Review the documentation and FAQs for possible solutions.
- Check the system requirements to ensure compatibility.
- Verify the configuration settings against the documentation.
- Consult the error logs for any relevant error messages or warnings.
- Seek guidance from the community through the user forum.

{{< callout "note" >}}
In many scenarios, we ask our customers to use Diagnosis endpoint to help us retrieve additional information.

To use LocalStack's Diagnosis endpoint:

- Set the environment variable `LS_LOG=trace`
- Start LocalStack
- Run the affected task(s)
- Call the diagnostic endpoint `curl -s localhost:4566/_localstack/diagnose | gzip -cf > diagnose.json.gz` (Endpoint URL depends on your configuration)
- Send the output file to our Slack chat

Ensure that you avoid sending the diagnostic output to public channels or forums, as it may contain sensitive information.
{{< /callout >}}

#### Channels

You can avail standard support through the following channels:

- [LocalStack Slack Bot](https://localstack.cloud/slack)
- [LocalStack Web Application](https://app.localstack.cloud)

##### LocalStack Support Bot

To create a support ticket:

- Search for the **LocalStack Pro Support** in our [Slack Community](https://localstack.cloud/slack).
- Navigate to **Messages** and type your message to LocalStack Pro Support.

Sending a message to LocalStack Pro Support will create a support ticket, and our support team will respond to your request as quickly as possible.

##### LocalStack Web Application

To create a support ticket:

- Navigate to the [LocalStack Web Application](http://app.localstack.cloud).
- Click on the chat icon in the bottom right corner of the page.
- Select **Technical Question** from the menu.
- Fill in the required details and send your message.

### Priority support

Priority support is available for users with active Teams or Enterprise subscriptions, offering dedicated 1v1 assistance and faster response times:

- **First response time**: first response within 24h
- **Follow-up response time:** response to all follow-ups within 24h.

Please note that all responses are provided during our normal operating hours.
While we strive to respond within a 24-hour timeframe, we cannot guarantee that every response will meet this timeline.

Our support engineers may schedule live screen sharing sessions to directly observe and diagnose issues, ensuring faster and more effective resolutions.

### Enterprise support

To learn more about the support available to **Enterprise** plan users, refer to the [Enterprise Support]({{<ref "enterprise-support" >}}) page.

## Support Business Hours

Our support team operates in the CET timezone, Monday to Friday, from 8 AM to 4 PM, excluding the following holidays:

- January 1st,
- May 1st,
- August 15th,
- December 24th, 25th and 31st
