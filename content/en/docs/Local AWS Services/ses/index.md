---
title: "Simple Email Service (SES)"
linkTitle: "Simple Email Service (SES)"
categories: ["LocalStack Pro"]
description: >
  Simple Email Service (SES)
---

The Pro version ships with extended support Simple Email Service (SES), including a simple user interface to inspect email accounts and sent messages, as well as support for sending SES messages through an actual SMTP email server.

Please refer to the [Configuration section]({{< ref "#configuration" >}}) for instructions on how to configure the connection parameters of your SMTP server (`SMTP_HOST`/`SMTP_USER`/`SMTP_PASS`).

Once your SMTP server has been configured, you can use the SES user interface in the Web app to create a new email account (e.g., `user1@yourdomain.com`), and then send an email via the command line (or your SES client SDK):
{{< command >}}
$ awslocal ses send-email --from user1@yourdomain.com --message 'Body={Text={Data="Lorem ipsum dolor sit amet, consectetur adipiscing elit, ..."}},Subject={Data=Test Email}' --destination 'ToAddresses=recipient1@example.com'
{{< / command >}}

The [Web user interface](https://app.localstack.cloud) then allows you to interactively browse through the sent email messages, as illustrated in the screenshot below:

![SES Web Interface](sesInterface.png)
