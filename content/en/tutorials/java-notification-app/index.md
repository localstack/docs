---
title: "Building a Java Notification app using AWS Java SDK, Simple Email Service (SES), and CloudFormation"
linkTitle: "Building a Java Notification app using AWS Java SDK, Simple Email Service (SES), and CloudFormation"
weight: 3
description: >
  Build a Java Spring Boot application to configure Simple Email Service (SMS) to send messages using AWS Java SDK. Learn how to configure Simple Queue Service (SQS) & Simple Notification Service (SNS) by using a local CloudFormation infrastructure mocked by LocalStack.
cascade:
  type: docs
---

AWS Java SDK provides a set of libraries that enables Java developers to work with Amazon Web Services and build applications that work with various AWS services, like Simple Email Service (SES), Simple Queue Service (SQS), Simple Notification Service (SNS), and more. Simple Email Service (SES) is a cloud-based email-sending service that enables developers to integrate email functionality into their applications running on AWS. SES allows developers to work without an on-prem Simple Mail Transfer Protocol (SMTP) system and send bulk emails to many recipients.

[LocalStack Pro](https://app.localstack.cloud/) supports SES along with a simple user interface to inspect email accounts and sent messages. LocalStack also supports sending SES messages through an actual SMTP email server. We will use Simple Queue Service (SQS) and Simple Notification Service (SNS) to process the emails. We would further employ a CloudFormation stack to configure the infrastructure and configure SNS & SQS subscriptions. AWS Java SDK would be employed to receive these SQS messages and to send these messages through SES further.

In this tutorial, we will build a Java Spring Boot application to provision a locally emulated infrastructure over LocalStack using CloudFormation, and configure SES, SQS, and SNS to send notifications through Java AWS SDK. We will further use [MailHog](https://github.com/mailhog/MailHog), a local SMTP server, to inspect the emails sent through SES via an intuitive user interface.