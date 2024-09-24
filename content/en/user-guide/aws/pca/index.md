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
We will follow the procedure to create and install a certificate for a single-level hierarchy CA hosted by ACM PCA.

### Create a CA

Start by creating a new Certificate Authority with ACM PCA using the [`CreateCertificateAuthority`](https://docs.aws.amazon.com/privateca/latest/APIReference/API_CreateCertificateAuthority.html) API.
This command sets up a new CA with specified configurations for key algorithm, signing algorithm, and subject information.

{{< command >}}
$ awslocal acm-pca create-certificate-authority \
     --certificate-authority-configuration '{
        "KeyAlgorithm":"RSA_2048",
        "SigningAlgorithm":"SHA256WITHRSA",
        "Subject":{
            "Country":"CH",
            "Organization":"LocalStack",
            "OrganizationalUnit":"Engineering",
            "CommonName":"test.localstack.cloud"
        }
     }' \
     --certificate-authority-type "ROOT"
<disable-copy>
{
    "CertificateAuthorityArn": "arn:aws:acm-pca:eu-central-1:000000000000:certificate-authority/0b20353f-ce7a-4de4-9b82-e06903a893ff"
}
</disable-copy>
{{< /command >}}

Note the `CertificateAuthorityArn` from the output as it will be needed for subsequent commands.

To retrieve the detailed information about the created Certificate Authority, use the [`DescribeCertificateAuthority`](https://docs.aws.amazon.com/privateca/latest/APIReference/API_DescribeCertificateAuthority.html) API.
This command returns the detailed information about the CA, including the CA's ARN, status, and configuration.

{{< command >}}
$ awslocal acm-pca describe-certificate-authority \
    --certificate-authority-arn arn:aws:acm-pca:eu-central-1:000000000000:certificate-authority/0b20353f-ce7a-4de4-9b82-e06903a893ff
<disable-copy>
{
    "CertificateAuthority": {
        "Arn": "arn:aws:acm-pca:eu-central-1:000000000000:certificate-authority/0b20353f-ce7a-4de4-9b82-e06903a893ff",
        "OwnerAccount": "000000000000",
        "CreatedAt": "2024-08-08T10:45:58.065504+05:30",
        "Type": "ROOT",
        "Status": "PENDING_CERTIFICATE",
        "CertificateAuthorityConfiguration": {
            "KeyAlgorithm": "RSA_2048",
            "SigningAlgorithm": "SHA256WITHRSA",
            "Subject": {
                "Country": "CH",
                "Organization": "LocalStack",
                "OrganizationalUnit": "Engineering",
                "CommonName": "test.localstack.cloud"
            }
        },
        "RevocationConfiguration": {
            "CrlConfiguration": {
                "Enabled": false
            }
        },
        "KeyStorageSecurityStandard": "FIPS_140_2_LEVEL_3_OR_HIGHER",
        "UsageMode": "SHORT_LIVED_CERTIFICATE"
    }
}
</disable-copy>
{{< /command >}}

Note the `PENDING_CERTIFICATE` status.
In the following steps, we will create and attach a certificate for this CA.

### Issue CA Certificate

Use the [`GetCertificateAuthorityCsr`](https://docs.aws.amazon.com/privateca/latest/APIReference/API_GetCertificateAuthorityCsr.html) operation to obtain the Certificate Signing Request (CSR) for the CA.

{{< command >}}
$ awslocal acm-pca get-certificate-authority-csr \
    --certificate-authority-arn arn:aws:acm-pca:eu-central-1:000000000000:certificate-authority/0b20353f-ce7a-4de4-9b82-e06903a893ff \
    --output text | tee ca.csr
{{< /command >}}

Next, issue the certificate for the CA using this CSR.

{{< command >}}
$ awslocal acm-pca issue-certificate \
    --csr fileb://ca.csr \
    --signing-algorithm SHA256WITHRSA \
    --template-arn arn:aws:acm-pca:::template/RootCACertificate/V1 \
    --validity Value=10,Type=YEARS \
    --certificate-authority-arn arn:aws:acm-pca:eu-central-1:000000000000:certificate-authority/0b20353f-ce7a-4de4-9b82-e06903a893ff
<disable-copy>
{
    "CertificateArn": "arn:aws:acm-pca:eu-central-1:000000000000:certificate-authority/0b20353f-ce7a-4de4-9b82-e06903a893ff/certificate/17ef7bbf3cc6471ba3ef0707119b8392"
}
</disable-copy>
{{< /command >}}

The CA certificate is now created and its ARN is indicated by the `CertficiateArn` parameter.

### Import CA Certificate

Finally, we retrieve the signed certificate with [`GetCertificate`](https://docs.aws.amazon.com/privateca/latest/APIReference/API_GetCertificate.html) and import it using [`ImportCertificateAuthorityCertificate`](https://docs.aws.amazon.com/privateca/latest/APIReference/API_ImportCertificateAuthorityCertificate.html).

{{< command >}}
$ awslocal acm-pca get-certificate \
    --certificate-authority-arn arn:aws:acm-pca:eu-central-1:000000000000:certificate-authority/0b20353f-ce7a-4de4-9b82-e06903a893ff \
    --certificate-arn arn:aws:acm-pca:eu-central-1:000000000000:certificate-authority/0b20353f-ce7a-4de4-9b82-e06903a893ff/certificate/17ef7bbf3cc6471ba3ef0707119b8392 \
    --output text | tee cert.pem
{{< /command >}}

{{< command >}}
$ awslocal acm-pca import-certificate-authority-certificate \
     --certificate-authority-arn arn:aws:acm-pca:eu-central-1:000000000000:certificate-authority/0b20353f-ce7a-4de4-9b82-e06903a893ff \
     --certificate fileb://cert.pem
{{< /command >}}

The CA is now ready for use.
You can verify this by checking its status:

{{< command >}}
$ awslocal acm-pca describe-certificate-authority \
    --certificate-authority-arn arn:aws:acm-pca:eu-central-1:000000000000:certificate-authority/0b20353f-ce7a-4de4-9b82-e06903a893ff \
    --query CertificateAuthority.Status \
    --output text
<disable-copy>
ACTIVE
</disable-copy>
{{< /command >}}

The CA certificate can be retrieved at a later point using [`GetCertificateAuthorityCertificate`](https://docs.aws.amazon.com/privateca/latest/APIReference/API_GetCertificateAuthorityCertificate.html).
In general, this operation returns both the certificate and the certificate chain.
In this case however, only the certificate will be returned, because we used a single-level CA hierarchy and the certificate chain is null.
For production setups, you must use a [multi-level CA hierarchy](https://docs.aws.amazon.com/privateca/latest/userguide/ca-hierarchy.html) for best security.

### Issue End-entity Certificates

With the private CA set up, you can now issue end-entity certificates.

Using [OpenSSL](https://openssl-library.org/), create a CSR and the private key:

{{< command >}}
$ openssl req -out local-csr.pem -new -newkey rsa:2048 -nodes -keyout local-pkey.pem
{{< /command >}}

You may inspect the CSR using the following command.
It should resemble the illustrated output.

{{< command >}}
$ openssl req -in local-csr.pem -text -noout
<disable-copy>
Certificate Request:
    Data:
        Version: 1 (0x0)
        Subject: C = IN, ST = GA, O = EvilCorp, OU = Engineering, CN = evilcorp.com
        Subject Public Key Info:
            Public Key Algorithm: rsaEncryption
                Public-Key: (2048 bit)
                Modulus:
                    00:a3:1d:5d:50:00:5c:4e:5d:79:a8:9a:d4:10:f4:
                    ...
                Exponent: 65537 (0x10001)
        Attributes:
            (none)
            Requested Extensions:
    Signature Algorithm: sha256WithRSAEncryption
    Signature Value:
        3e:23:12:26:45:af:39:35:5d:d7:b4:40:fb:1a:08:c7:16:c3:
        ...
</disable-copy>
{{< /command >}}

Next, using [`IssueCertificate`](https://docs.aws.amazon.com/privateca/latest/APIReference/API_IssueCertificate.html) you can generate the end-entity certificate.
Note that there is no [certificate template](https://docs.aws.amazon.com/privateca/latest/userguide/UsingTemplates.html) specified which causes the end-entity certificate to be issued by default.

{{< command >}}
$ awslocal acm-pca issue-certificate \
      --certificate-authority-arn arn:aws:acm-pca:eu-central-1:000000000000:certificate-authority/0b20353f-ce7a-4de4-9b82-e06903a893ff \
      --csr fileb://local-csr.pem \
      --signing-algorithm "SHA256WITHRSA" \
      --validity Value=365,Type="DAYS"
<disable-copy>
{
    "CertificateArn": "arn:aws:acm-pca:eu-central-1:000000000000:certificate-authority/0b20353f-ce7a-4de4-9b82-e06903a893ff/certificate/079d0a13daf943f6802d365dd83658c7"
}
</disable-copy>
{{< /command >}}

### Verify Certificates

Using OpenSSL, you can verify that the end-entity certificate was indeed signed by the CA.
In the following command, `local-cert.pem` refers to the end-entity certificate and `cert.pem` refers to the CA certificate.

{{< command >}}
$ openssl verify -CAfile cert.pem local-cert.pem
local-cert.pem: OK
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
