---
title: "Pinpoint"
linkTitle: "Pinpoint"
description: Get started with Pinpoint on LocalStack
tags: ["Ultimate"]
persistence: supported

---

{{< callout "warning" >}}
Amazon Pinpoint will be [retired on 30 October 2026](https://docs.aws.amazon.com/pinpoint/latest/userguide/migrate.html).
It will be removed from LocalStack soon after this date.
{{< /callout >}}

## Introduction

Pinpoint is a customer engagement service to facilitate communication across multiple channels, including email, SMS, and push notifications.
Pinpoint allows developers to create and manage customer segments based on various attributes, such as user behavior and demographics, while integrating with other AWS services to send targeted messages to customers.

LocalStack allows you to mock the Pinpoint APIs in your local environment.
The supported APIs are available on our [API coverage page](https://docs.localstack.cloud/references/coverage/coverage_pinpoint/), which provides information on the extent of Pinpoint's integration with LocalStack.

## Getting started

This guide is designed for users new to Pinpoint and assumes basic knowledge of the AWS CLI and our [`awslocal`](https://github.com/localstack/awscli-local) wrapper script.

Start your LocalStack container using your preferred method.
We will demonstrate how to create a Pinpoint application, retrieve all applications, and list tags for the resource.

### Create an application

Create a Pinpoint application using the [`CreateApp`](https://docs.aws.amazon.com/pinpoint/latest/apireference/apps-application-id.html) API.
Execute the following command:

{{< command >}}
$ awslocal pinpoint create-app \
    --create-application-request Name=ExampleCorp,tags={"Stack"="Test"}
{{< /command >}}

The following output would be retrieved:

```bash
{
    "ApplicationResponse": {
        "Arn": "arn:aws:mobiletargeting:us-east-1:000000000000:apps/4487a55ac6fb4a2699a1b90727c978e7",
        "Id": "4487a55ac6fb4a2699a1b90727c978e7",
        "Name": "ExampleCorp",
        "CreationDate": 1706609789.906863
    }
}
```

### List applications

You can list all applications using the [`GetApps`](https://docs.aws.amazon.com/pinpoint/latest/apireference/apps.html) API.
Execute the following command:

{{< command >}}
$ awslocal pinpoint get-apps
{{< /command >}}

The following output would be retrieved:

```bash
{
    "ApplicationsResponse": {
        "Item": [
            {
                "Arn": "arn:aws:mobiletargeting:us-east-1:000000000000:apps/4487a55ac6fb4a2699a1b90727c978e7",
                "Id": "4487a55ac6fb4a2699a1b90727c978e7",
                "Name": "ExampleCorp",
                "CreationDate": 1706609789.906863
            }
        ]
    }
}
```

### List tags for the application

You can list all tags for the application using the [`GetApp`](https://docs.aws.amazon.com/pinpoint/latest/apireference/apps-application-id.html) API.
Execute the following command:

{{< command >}}
$ awslocal pinpoint list-tags-for-resource \
    --resource-arn arn:aws:mobiletargeting:us-east-1:000000000000:apps/4487a55ac6fb4a2699a1b90727c978e7
{{< /command >}}

Replace the `resource-arn` with the ARN of the application you created earlier.
The following output would be retrieved:

```bash
{
    "TagsModel": {
        "tags": {
            "Stack": "Test"
        }
    }
}
```

### OTP verification

The operations [`SendOTPMessage`](https://docs.aws.amazon.com/pinpoint/latest/apireference/apps-application-id-otp.html#SendOTPMessage) and [`VerifyOTPMessage`](https://docs.aws.amazon.com/pinpoint/latest/apireference/apps-application-id-verify-otp.html#VerifyOTPMessage) are used for one-time password (OTP) verification.

On production AWS, `SendOTPMessage` sends an SMS text message with the OTP code.
The OTP can then be verified against the reference ID using `VerifyOTPMessage`

LocalStack however can not send real SMS text messages.
Instead it provides alternative ways to retrieve the actual OTP code as illustrated below.

Begin by making a OTP request:

{{< command >}}
$ awslocal pinpoint send-otp-message \
  --application-id fff5a801e01643c18a13a763e22a8fbf \
  --send-otp-message-request-parameters '{
      "BrandName": "LocalStack Community",
      "Channel": "SMS",
      "DestinationIdentity": "+1224364860",
      "ReferenceId": "liftoffcampaign",
      "OriginationIdentity": "+1123581321",
      "CodeLength": 6,
      "AllowedAttempts": 3,
      "ValidityPeriod": 2
    }'
<disable-copy>
{
    "MessageResponse": {
        "ApplicationId": "fff5a801e01643c18a13a763e22a8fbf"
    }
}
</disable-copy>
{{< /command >}}

You can use the debug endpoint `/_aws/pinpoint/<application_id>/<reference_id>` to retrieve the OTP message details:

{{< command >}}
$ curl http://localhost:4566/_aws/pinpoint/fff5a801e01643c18a13a763e22a8fbf/liftoffcampaign | jq .
{
  "AllowedAttempts": 3,
  "BrandName": "LocalStack Community",
  "CodeLength": 6,
  "DestinationIdentity": "+1224364860",
  "OriginationIdentity": "+1123581321",
  "ReferenceId": "liftoffcampaign",
  "ValidityPeriod": 2,
  "Attempts": 0,
  "ApplicationId": "fff5a801e01643c18a13a763e22a8fbf",
  "CreatedTimestamp": "2024-10-17T05:38:24.070Z",
  "Code": "655745"
}
{{< /command >}}

The OTP code is also printed in an `INFO` level message in the LocalStack log output:

```text
2024-10-17T11:08:24.044 INFO : OTP for application ID fff5a801e01643c18a13a763e22a8fbf reference ID liftoffcampaign: 655745
```

Finally, the OTP code can be verified using:

{{< command >}}
$ awslocal pinpoint verify-otp-message \
  --application-id fff5a801e01643c18a13a763e22a8fbf \
  --verify-otp-message-request-parameters '{
      "ReferenceId": "liftoffcampaign",
      "DestinationIdentity": "+1224364860",
      "Otp": "655745"
  }'
<disable-copy>
{
    "VerificationResponse": {
        "Valid": true
    }
}
</disable-copy>
{{< /command >}}

When validating OTP codes, LocalStack checks for the number of allowed attempts and the validity period.
Unlike AWS, there is no lower limit for validity period.
