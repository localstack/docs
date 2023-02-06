---
title: "Simple Email Service (SES)"
linkTitle: "Simple Email Service (SES)"
categories: ["LocalStack Community", "LocalStack Pro"]
description: Get started with Amazon Simple Email Service (SES) on LocalStack
aliases:
  - /aws/ses/
---

## Community

LocalStack keeps track of all sent emails for retrospection.

The sent messages can be retrieved via a service API endpoint (GET `/_localstack/ses`) or from the filesystem.

Messages are also saved to the state directory (see [filesystem layout]({{< ref "filesystem" >}})).
The files are saved as JSON in the `ses/` subdirectory and organised by message ID.

## Pro

LocalStack Pro ships with extended support including a simple user interface to inspect email accounts and sent messages, as well as support for sending SES messages through an actual SMTP email server.

Please refer to the [Configuration]({{< ref "configuration#emails" >}}) guide for instructions on how to configure the connection parameters of your SMTP server (`SMTP_HOST`/`SMTP_USER`/`SMTP_PASS`).

Once the SMTP server has been configured, the SES user interface in the Web app can be used to create a new email account (e.g., `user1@yourdomain.com`).
Emails can be sent via the command line (or SES client SDK):
{{< command >}}
$ awslocal ses send-email \
    --from user1@yourdomain.com \
    --message 'Body={Text={Data="Lorem ipsum dolor sit amet, consectetur adipiscing elit, ..."}},Subject={Data=Test Email}' \
    --destination 'ToAddresses=recipient1@example.com'
{{< / command >}}

{{< alert title="Hint" color="info" >}}
If you receive a "Email address not verified message", simply call
```sh
awslocal ses verify-email-identity --email-address user1@yourdomain.com
```
{{< /alert >}}

The [Web user interface](https://app.localstack.cloud) can be used to view the sent email messages, as illustrated in the screenshot below:

![SES Web Interface](sesInterface.png)
