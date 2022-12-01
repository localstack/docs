---
title: "AWS Certificate Manager (ACM)"
linkTitle: "AWS Certificate Manager"
categories: ["LocalStack Community"]
description: >
  Get started with AWS Certificate Manager (ACM) on LocalStack
aliases:
  - /aws/acm/
---

AWS Certificate Manager (ACM) allows you to provision, manage, and deploy public and private SSL/TLS certificates to be used with other AWS services and internally connected resources. ACM allows you to secure multiple domain names and multiple names within a domain, create wildcard SSL certificates to protect an entire domain and its subdomains, and install public ACM certificates via services integrated with ACM.

LocalStack provides ACM support via the Community offering. You can use the ACM API to create, list, and delete certificates. The supported APIs are available over our [feature coverage page]({{< ref "feature-coverage" >}}).

## Getting started

In this getting started guide, you'll learn how to make a basic usage of ACM over LocalStack. This guide is intended for users who wish to get more acquainted with ACM, and assumes you have basic knowledge of the AWS CLI (and our [`awslocal`](https://github.com/localstack/awscli-local) wrapper script). First, start your LocalStack instance using your preferred method, then run the following commands:

1. Request a new public ACM certificate via the `request-certificate` command and specify the domain name for which you want to request a certificate for:
   {{< command >}}
   $ awslocal acm request-certificate \
        --domain-name www.example.com \
        --validation-method DNS \
        --idempotency-token 1234 \
        --options CertificateTransparencyLoggingPreference=DISABLED

    {
    "CertificateArn": "arn:aws:acm:<region>:000000000000:certificate/<certificate_ID>"
    }
   {{< /command >}}

2. You can list all the certificates in your account by running the following command:
   {{< command >}}
   $ awslocal acm list-certificates --max-items 10
   {{< /command >}}

3. You can view the certificate details via the `describe-certificate` command to display certificate details:
   {{< command >}}
   $ awslocal acm describe-certificate --certificate-arn arn:aws:acm:<region>:account:certificate/<certificate_ID>
   {{< /command >}}

4. You can use the `delete-certificate` command to delete a certificate:
   {{< command >}}
   $ awslocal acm delete-certificate --certificate-arn arn:aws:acm:<region>:account:certificate/<certificate_ID>
   {{< /command >}}

Navigate to the [official AWS ACM documentation](https://docs.aws.amazon.com/acm/latest/userguide/acm-overview.html) on all ACM operations and concepts.
