---
title: "Quickstart"
tags: ["extensions"] 
weight: 3
description: >
  Get started with LocalStack extensions
---

In this quickstart guide, we will install and use the official [MailHog extensions](https://github.com/localstack/localstack-extensions/tree/main/mailhog).

## Install an extension

First, start up your LocalStack instance and navigate to our [Extension Manager App](https://app.localstack.cloud/inst/default/extensions/manage).
Then, click the "Install" button of the MailHog extension:

{{< figure src="install-extensions.png" >}}

You will be prompted to confirm that LocalStack will be restarted, and then the extension should become available.
In your LocalStack logs you should see the MailHog extension logging some output:

```
2023-10-11T19:10:54.708  INFO --- [  MainThread] l.extensions.platform      : loaded 1 extensions
2023-10-11T19:10:54.709  INFO --- [  MainThread] mailhog.extension          : starting mailhog server
2023-10-11T19:10:54.709  INFO --- [  MainThread] mailhog.extension          : configuring SMTP host to internal mailhog smtp: localhost:25
...
2023-10-11T19:10:55.023  INFO --- [  MainThread] mailhog.extension          : serving mailhog extension on host: http://mailhog.localhost.localstack.cloud:4566
2023-10-11T19:10:55.023  INFO --- [  MainThread] mailhog.extension          : serving mailhog extension on path: http://localhost:4566/mailhog/
```

## Use the extension

With MailHog, you can perform end-to-end testing of applications that send emails via SES.
Let's use the AWS CLI tool to send an email:

### Send an Email through SES

{{< command >}}
aws --endpoint-url=http://localhost:4566 \
    ses verify-email-identity --email-address user1@yourdomain.com
{{< /command >}}

{{< command >}}
aws --endpoint-url=http://localhost:4566 \
    ses send-email \
    --from user1@yourdomain.com \
    --message 'Body={Text={Data="Hello from LocalStack to MailHog"}},Subject={Data=Test Email}' \
    --destination 'ToAddresses=recipient1@example.com'
{{< /command >}}

### Open the extension's UI

Now, navigate in your browser to the MailHog UI in LocalStack: http://mailhog.localhost.localstack.cloud:4566/

You should see the email there:

{{< figure src="mailhog.png" >}}

## Next steps

* We have a range of official extensions, and a growing ecosystem of third-party extensions.
  Check them out in our [Extensions Library](https://app.localstack.cloud/extensions/library).
* There are different ways of managing extensions, and automating the installation of extensions when using LocalStack in CI.
  You can find out more in our [Managing Extensions]({{< ref "managing-extensions" >}}) guide.
* You can also build your own extensions!
  Check out our guide on [Developing Extensions]({{< ref "developing-extensions" >}}).
