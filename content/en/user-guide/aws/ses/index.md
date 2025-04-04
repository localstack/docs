---
title: "Simple Email Service (SES)"
linkTitle: "Simple Email Service (SES)"
description: Get started with Amazon Simple Email Service (SES) on LocalStack
tags: ["Pro image"]
persistence: supported

---

## Introduction

Simple Email Service (SES) is an emailing service that can be integrated with other cloud-based services.
It provides API to facilitate email templating, sending bulk emails and more.

SESv1 is available in LocalStack Community image, while SESv2 and SMTP integration is available in LocalStack Pro.
The supported APIs are available on the API coverage page for [SESv1](https://docs.localstack.cloud/references/coverage/coverage_ses/) and [SESv2](https://docs.localstack.cloud/references/coverage/coverage_sesv2/).

## Getting Started

This is an introductory guide to get started with SES.
Basic knowledge of the AWS CLI and LocalStack [`awslocal`](https://github.com/localstack/awscli-local) command is assumed.

Start LocalStack using your preferred method.

To be able to send emails, we need to create a verified identity.
A verified identity appears as part of the 'From' field in the sent email.

A singular email identity can be added using the `VerifyEmailIdentity` operation.

{{< command >}}
$ awslocal ses verify-email-identity --email hello@example.com

$ awslocal ses list-identities
{
    "Identities": [
        "hello@example.com"
    ]
}
{{< /command >}}

{{< callout >}}
On AWS, verifying email identities or domain identities require additional steps like changing DNS configuration or clicking verification links respectively.
In LocalStack, identities are automatically verified.
{{< /callout >}}

Next, emails can be sent using the `SendEmail` operation.

{{< command >}}
$ awslocal ses send-email \
        --from "hello@example.com"   \
        --message 'Body={Text={Data="This is the email body"}},Subject={Data="This is the email subject"}'   \
        --destination 'ToAddresses=jeff@aws.com'
{
    "MessageId": "labpqxukegeaftfh-ymaouvvy-ribr-qeoy-izfp-kxaxbfcfsgbh-wpewvd"
}
{{< /command >}}

{{< callout >}}
In LocalStack Community, all operations are mocked and no real emails are sent.
In LocalStack Pro, it is possible to send real emails via an SMTP server.
{{< /callout >}}

## Retrieve Sent Emails

LocalStack keeps track of all sent emails for retrospection.
Sent messages can be retrieved in following ways:
- **API endpoint:** LocalStack provides a service endpoint (`/_aws/ses`) which can be used to return in-memory saved messages.
    A `GET` call returns all messages.
    Query parameters `id` and `email` can be used to filter by message ID and message source respectively.
    {{< command >}}
$ curl --silent localhost.localstack.cloud:4566/_aws/ses?email=hello@example.com | jq .
{
  "messages": [
    {
      "Id": "dqxhhgoutkmylpbc-ffuqlkjs-ljld-fckp-hcph-wcsrkmxhhldk-pvadjc",
      "Region": "eu-central-1",
      "Destination": {
        "ToAddresses": [
          "jeff@aws.com"
        ]
      },
      "Source": "hello@example.com",
      "Subject": "This is the email subject",
      "Body": {
        "text_part": "This is the email body",
        "html_part": null
      },
      "Timestamp": "2023-09-11T08:37:13"
    }
  ]
}
    {{< /command >}}
    A `DELETE` call clears all messages from the memory.
    The query parameter `id` can be used to delete only a specific message.
    {{< command >}}
    $ curl -X DELETE localhost.localstack.cloud:4566/_aws/ses?id=dqxhhgoutkmylpbc-ffuqlkjs-ljld-fckp-hcph-wcsrkmxhhldk-pvadjc
    {{< /command >}}
- **Filesystem:** All messages are saved to the state directory (see [filesystem layout]({{< ref "filesystem" >}})).
    The files are saved as JSON in the `ses/` subdirectory and named by the message ID.

## SMTP Integration

LocalStack Pro supports sending emails via an SMTP server.
To enable this, set the connections parameters and access credentials for the server in the configuration.
Refer to the [Configuration]({{< ref "configuration#emails" >}}) guide for details.

{{< callout "tip" >}}
If you do not have access to a live SMTP server, you can use tools like [MailDev](https://github.com/maildev/maildev) or [smtp4dev](https://github.com/rnwood/smtp4dev).
These run as Docker containers on your local machine.
Make sure they run in the same Docker network as the LocalStack container.
{{< /callout >}}

## Resource Browser

LocalStack Web Application provides a resource browser for managing email identities and introspecing sent emails.

<img src="ses-resource-browser.png" alt="SES Resource Browser" title="SESE Resource Browser" width="900"/>
<br/>
<br/>

The Resource Browser allows you to perform following actions:
- **Create Email Identity**: Create an email identity by clicking **Create Identity** and specifying the email address.
- **View Sent Emails**: View all sent emails from an email identity by clicking the email address.
  You can the view the details of a sent email by selecting them from the list.
- **Send Emails**: On selecting an email identity, click **Send Message** and specify destination fields (To, CC and BCC addresses) and the body (Plaintext, HTML) to send an email.

## Current Limitations

- It is currently not possible to [receive emails via SES](https://docs.aws.amazon.com/ses/latest/dg/receiving-email.html) in LocalStack.
- All operations related to Receipt Rules are mocked.
