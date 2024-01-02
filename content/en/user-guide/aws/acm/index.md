---
title: "AWS Certificate Manager (ACM)"
linkTitle: "AWS Certificate Manager (ACM)"
description: Get started with AWS Certificate Manager (ACM) on LocalStack
---

## Introduction

[AWS Certificate Manager (ACM)](https://aws.amazon.com/certificate-manager/) is a service that enables you to create and manage SSL/TLS certificates that can be used to secure your applications and resources in AWS. You can use ACM to provision and deploy public or private certificates trusted by browsers and other clients.

ACM supports securing multiple domain names and subdomains and can create wildcard SSL certificates to protect an entire domain and its subdomains. You can also use ACM to import certificates from third-party certificate authorities or to generate private certificates for internal use.

LocalStack supports ACM via the Community offering, allowing you to use the ACM API to create, list, and delete certificates. The supported APIs are available on our [API coverage page](https://docs.localstack.cloud/references/coverage/coverage_acm/), which provides information on the extent of ACM's integration with LocalStack.

## Getting started

This guide is designed for users who are new to ACM and assumes basic knowledge of the AWS CLI and our [`awslocal`](https://github.com/localstack/awscli-local) wrapper script.

### Request a public certificate

Start your LocalStack container using your preferred method, then use the [RequestCertificate API](https://docs.aws.amazon.com/acm/latest/APIReference/API_RequestCertificate.html) to request a new public ACM certificate. Specify the domain name you want to request the certificate for, and any additional options you need. Here's an example command:

{{< command >}}
$ awslocal acm request-certificate \
   --domain-name www.example.com \
   --validation-method DNS \
   --idempotency-token 1234 \
   --options CertificateTransparencyLoggingPreference=DISABLED
{{< /command >}}

This command will return the Amazon Resource Name (ARN) of the new certificate, which you can use in other ACM commands.

```json
{
   "CertificateArn": "arn:aws:acm:<region>:000000000000:certificate/<certificate_ID>"
}
```

### List the certificates

Use the [`ListCertificates` API](https://docs.aws.amazon.com/acm/latest/APIReference/API_ListCertificates.html) to list all the certificates. This command returns a list of the ARNs of all the certificates that have been requested or imported into ACM. Here's an example command:

{{< command >}}
$ awslocal acm list-certificates --max-items 10
{{< /command >}}

### Describe the certificate

Use the [`DescribeCertificate` API](https://docs.aws.amazon.com/acm/latest/APIReference/API_DescribeCertificate.html) to view the details of a specific certificate. Provide the ARN of the certificate you want to view, and this command will return information about the certificate's status, domain name, and other attributes. Here's an example command:

{{< command >}}
$ awslocal acm describe-certificate --certificate-arn arn:aws:acm:<region>:account:certificate/<certificate_ID>
{{< /command >}}

### Delete the certificate

Finally you can use the [`DeleteCertificate` API](https://docs.aws.amazon.com/acm/latest/APIReference/API_DeleteCertificate.html) to delete a certificate from ACM, by passing the ARN of the certificate you want to delete. Here's an example command:

{{< command >}}
$ awslocal acm delete-certificate --certificate-arn arn:aws:acm:<region>:account:certificate/<certificate_ID>
{{< /command >}}

## ACM Private Certificate Authority

AWS Private Certificate Authority (ACM PCA) is a managed private Certificate Authority (CA) service that manages the lifecycle of your private certificates. 
ACM PCA extends ACM's certificate management capabilities to private certificates, enabling you to manage public and private certificates centrally.

LocalStack supports ACM PCA via the Pro/Team offering, allowing you to use the ACM PCA API to create, list, and delete private certificates. 
You can creating, describing, tagging, and listing tags for a CA using ACM PCA. 
The supported APIs are available on our [API coverage page](https://docs.localstack.cloud/references/coverage/coverage_acm-pca/), which provides information on the extent of ACM PCA's integration with LocalStack.

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

Tagging resources in AWS helps in managing and identifying them. Use the [`TagCertificateAuthority`](https://docs.aws.amazon.com/privateca/latest/APIReference/API_TagCertificateAuthority.html) API to tag the created Certificate Authority. 
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

## Examples

The following code snippets and sample applications provide practical examples of how to use ACM in LocalStack for various use cases:

- [API Gateway with Custom Domains](https://github.com/localstack/localstack-pro-samples/tree/master/apigw-custom-domain)
- [Generating an ACM certificate via Terraform](https://github.com/localstack/localstack-terraform-samples/tree/master/acm-route53)
