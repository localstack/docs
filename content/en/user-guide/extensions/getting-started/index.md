---
title: "Getting started"
linkTitle: "Getting started"
weight: 1
description: >
  Get started with LocalStack extensions by installing and using the official MailHog extension.
tags: ["Base"]
---

## Introduction

MailHog is an open source email testing tool for developers.
It provides a simple SMTP server and web interface that allows developers to easily catch and inspect emails sent from their application during development.
In this guide, you will install and use the [official MailHog extension for LocalStack](https://github.com/localstack/localstack-extensions/tree/main/mailhog) and send an email through SES, while inspecting it in MailHog.

## Prerequisites

- [LocalStack Account](https://app.localstack.cloud/)
- [AWS CLI](https://docs.aws.amazon.com/cli/latest/userguide/cli-chap-welcome.html)

## Installation

To get started, start your LocalStack instance with your `LOCALSTACK_AUTH_TOKEN`.
Access our [Extension Manager](https://app.localstack.cloud/inst/default/extensions/manage), and click the **Install** button for the MailHog extension.

{{< figure src="install-extensions.png" alt="Extensions Manager" width="800">}}

You'll receive a confirmation prompt indicating that LocalStack container will restart, after which the extension will become accessible.
Check your LocalStack logs for MailHog extension output, where you should see relevant logging information:

```bash
2023-10-11T19:10:54.708  INFO --- [  MainThread] l.extensions.platform      : loaded 1 extensions
2023-10-11T19:10:54.709  INFO --- [  MainThread] mailhog.extension          : starting mailhog server
2023-10-11T19:10:54.709  INFO --- [  MainThread] mailhog.extension          : configuring SMTP host to internal mailhog smtp: localhost:25
...
2023-10-11T19:10:55.023  INFO --- [  MainThread] mailhog.extension          : serving mailhog extension on host: http://mailhog.localhost.localstack.cloud:4566
2023-10-11T19:10:55.023  INFO --- [  MainThread] mailhog.extension          : serving mailhog extension on path: http://localhost:4566/mailhog/
```

## Usage

MailHog enables you to conduct end-to-end testing of applications that utilize SES (Simple Email Service) for sending emails.
To test this, let's use the AWS CLI to send an email.

### Send an Email

You can use the [`VerifyEmailIdentity`](https://docs.aws.amazon.com/cli/latest/reference/ses/verify-email-identity.html) API to verify an email address with SES.
This is a required step before you can send emails from SES.
Run the following command to verify an email address:

{{< command >}}
$ aws --endpoint-url=http://localhost:4566 \
    ses verify-email-identity --email-address user1@yourdomain.com
{{< /command >}}

You can further send an email using the [`SendEmail`](https://docs.aws.amazon.com/cli/latest/reference/ses/send-email.html) API.
Run the following command to send an email:

{{< command >}}
$ aws --endpoint-url=http://localhost:4566 \
    ses send-email \
    --from user1@yourdomain.com \
    --message 'Body={Text={Data="Hello from LocalStack to MailHog"}},Subject={Data=Test Email}' \
    --destination 'ToAddresses=recipient1@example.com'
{{< /command >}}

### Navigate to Extension UI

Navigate in your browser to the [MailHog UI in LocalStack](http://mailhog.localhost.localstack.cloud:4566/).
You should see the email you sent in the MailHog UI.

{{< figure src="mailhog.png" alt="Mailhog UI" width="800">}}

## Next steps

- Explore our collection of official extensions, along with a growing ecosystem of third-party extensions, in our [Extensions Library](https://app.localstack.cloud/extensions/library).
- Learn about the various methods for extension management and automating their installation when using LocalStack in a CI environment.
  Get detailed insights from our [Managing Extensions]({{< ref "managing-extensions" >}}) guide.
- Want to create your own extensions?
  Dive into our guide on [Developing Extensions]({{< ref "developing-extensions" >}}) for step-by-step instructions.
