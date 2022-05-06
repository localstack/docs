---
title: "Simple Email Service (SES)"
linkTitle: "Simple Email Service (SES)"
categories: ["LocalStack Community", "LocalStack Pro"]
description: Amazon Simple Email Service (Amazon SES)
---

## Community

LocalStack keeps track of all sent emails for retrospection.

The sent messages can be retrieved via a service API endpoint (GET `/_localstack/ses`) or from the filesystem.

Messages are also saved to the data directory (`DATA_DIR`, see [Configuration]({{< ref "configuration#configuration" >}})).
If data directory is not available, the temporary directory (`TMPDIR`) is used.
The files are saved as JSON in the `ses/` subdirectory and organised by message ID.

## Pro

LocalStack Pro ships with extended support including a simple user interface to inspect email accounts and sent messages, as well as support for sending SES messages through an actual SMTP email server.

Please refer to the [Configuration]({{< ref "configuration#simple-email-service" >}}) guide for instructions on how to configure the connection parameters of your SMTP server (`SMTP_HOST`/`SMTP_USER`/`SMTP_PASS`).

Once the SMTP server has been configured, the SES user interface in the Web app can be used to create a new email account (e.g., `user1@yourdomain.com`).
Emails can be sent via the command line (or SES client SDK):
{{< command >}}
$ awslocal ses send-email \
    --from user1@yourdomain.com \
    --message 'Body={Text={Data="Lorem ipsum dolor sit amet, consectetur adipiscing elit, ..."}},Subject={Data=Test Email}' \
    --destination 'ToAddresses=recipient1@example.com'
{{< / command >}}

The [Web user interface](https://app.localstack.cloud) can be used to view the sent email messages, as illustrated in the screenshot below:

![SES Web Interface](sesInterface.png)
