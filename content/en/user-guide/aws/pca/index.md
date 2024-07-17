---
title: "Private Certificate Authority (ACM PCA)"
linkTitle: "Private Certificate Authority (ACM PCA)"
description: Get started with Private Certificate Authority (ACM PCA) on LocalStack
tags: ["Pro image"]
---

## Introduction

AWS Private Certificate Authority (ACM PCA) is a managed private Certificate Authority (CA) service that manages the lifecycle of your private certificates.
ACM PCA extends ACM's certificate management capabilities to private certificates, enabling you to manage public and private certificates centrally.

LocalStack allows you to use the ACM PCA APIs to create, list, and delete private certificates.
You can creating, describing, tagging, and listing tags for a CA using ACM PCA.
The supported APIs are available on our [API coverage page](https://docs.localstack.cloud/references/coverage/coverage_acm-pca/), which provides information on the extent of ACM PCA's integration with LocalStack.

## Getting started

This guide is designed for users who are new to ACM PCA and assumes basic knowledge of the AWS CLI and our [`awslocal`](https://github.com/localstack/awscli-local) wrapper script.

### Create a Certificate Authority (CA)

Start by creating a new Certificate Authority with ACM PCA using the [`CreateCertificateAuthority`](https://docs.aws.amazon.com/privateca/latest/APIReference/API_CreateCertificateAuthority.html) API.
This command sets up a new CA with specified configurations for key algorithm, signing algorithm, and subject information.

{{< command >}}
$ awslocal acm-pca create-certificate-authority \
     --certificate-authority-configuration '{
        "KeyAlgorithm":"RSA_2048",
        "SigningAlgorithm":"SHA256WITHRSA",
        "Subject":{
            "Country":"US",
            "Organization":"Example Corp",
            "OrganizationalUnit":"Sales",
            "State":"WA",
            "Locality":"Seattle",
            "CommonName":"www.example.com"
        }
     }' \
     --revocation-configuration '{
        "OcspConfiguration":{
            "Enabled":true
        }
     }' \
     --certificate-authority-type "ROOT" \
     --tags  Key=Name,Value=MyPCA
<disable-copy>
{
    "CertificateAuthorityArn": "arn:aws:acm-pca:us-east-1:000000000000:certificate-authority/f38ee966-bc23-40f8-8143-e981aee73600"
}
</disable-copy>
{{< /command >}}

Note the `CertificateAuthorityArn` from the output as it will be needed for subsequent commands.

### Describe the Certificate Authority

To retrieve the detailed information about the created Certificate Authority, use the [`DescribeCertificateAuthority`](https://docs.aws.amazon.com/privateca/latest/APIReference/API_DescribeCertificateAuthority.html) API.
This command returns the detailed information about the CA, including the CA's ARN, status, and configuration.

{{< command >}}
$ awslocal acm-pca describe-certificate-authority \
    --certificate-authority-arn arn:aws:acm-pca:us-east-1:000000000000:certificate-authority/f38ee966-bc23-40f8-8143-e981aee73600
<disable-copy>
{
    "CertificateAuthority": {
        "Arn": "arn:aws:acm-pca:us-east-1:000000000000:certificate-authority/f38ee966-bc23-40f8-8143-e981aee73600",
        "OwnerAccount": "000000000000",
        "CreatedAt": "2023-12-23T20:52:20.917796+05:30",
        "Type": "ROOT",
        "Status": "PENDING_CERTIFICATE",
        "CertificateAuthorityConfiguration": {
            "KeyAlgorithm": "RSA_2048",
            "SigningAlgorithm": "SHA256WITHRSA",
            "Subject": {
                "Country": "US",
                "Organization": "Example Corp",
                "OrganizationalUnit": "Sales",
                "State": "WA",
                "CommonName": "www.example.com",
                "Locality": "Seattle"
            }
        },
        "RevocationConfiguration": {
            "OcspConfiguration": {
                "Enabled": true
            }
        },
        "KeyStorageSecurityStandard": "FIPS_140_2_LEVEL_3_OR_HIGHER",
        "UsageMode": "SHORT_LIVED_CERTIFICATE"
    }
}
</disable-copy>
{{< /command >}}

### Tag the Certificate Authority

Tagging resources in AWS helps in managing and identifying them.
Use the [`TagCertificateAuthority`](https://docs.aws.amazon.com/privateca/latest/APIReference/API_TagCertificateAuthority.html) API to tag the created Certificate Authority.
This command adds the specified tags to the specified CA.

{{< command >}}
$ awslocal acm-pca tag-certificate-authority \
    --certificate-authority-arn arn:aws:acm-pca:us-east-1:000000000000:certificate-authority/f38ee966-bc23-40f8-8143-e981aee73600 \
    --tags Key=Admin,Value=Alice
{{< /command >}}

After tagging your Certificate Authority, you may want to view these tags.
You can use the [`ListTags`](https://docs.aws.amazon.com/privateca/latest/APIReference/API_ListTags.html) API to list all the tags associated with the specified CA.

{{< command >}}
$ awslocal acm-pca list-tags \
    --certificate-authority-arn arn:aws:acm-pca:us-east-1:000000000000:certificate-authority/f38ee966-bc23-40f8-8143-e981aee73600 \
    --max-results 10
<disable-copy>
{
    "Tags": [
        {
            "Key": "Name",
            "Value": "MyPCA"
        },
        {
            "Key": "Admin",
            "Value": "Alice"
        }
    ]
}
</disable-copy>
{{< /command >}}
