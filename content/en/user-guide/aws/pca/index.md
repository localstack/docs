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
We will follow the procedure to create and install a certificate for a root CA hosted by ACM PCA.

### Create a Certificate Authority

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
            "CommonName":"localhost.localstack.cloud"
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
                "CommonName": "localhost.localstack.cloud"
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

### Issue the CA certificate

Use the [`GetCertificateAuthorityCsr`](https://docs.aws.amazon.com/privateca/latest/APIReference/API_GetCertificateAuthorityCsr.html) operation to obtain the Certificate Signing Request (CSR) for the CA.

{{< command >}}
$ awslocal acm-pca get-certificate-authority-csr \
    --certificate-authority-arn arn:aws:acm-pca:eu-central-1:000000000000:certificate-authority/0b20353f-ce7a-4de4-9b82-e06903a893ff \
    --output text | tee ca.csr
<disable-copy>
-----BEGIN CERTIFICATE REQUEST-----
MIICuTCCAaECAQAwdDELMAkGA1UEBhMCVVMxEzARBgNVBAgMCkNhbGlmb3JuaWEx
FjAUBgNVBAcMDVNhbiBGcmFuY2lzY28xEzARBgNVBAoMCk15IENvbXBhbnkxIzAh
BgNVBAMMGmxvY2FsaG9zdC5sb2NhbHN0YWNrLmNsb3VkMIIBIjANBgkqhkiG9w0B
AQEFAAOCAQ8AMIIBCgKCAQEAs+VYfE/ntonEBz5nZVdAjyoiLo7DVlMEekUY72Jc
sj6olkrQlRhPlfLPvOTppqO63HuQ1AR/oftFTkjt+nCvIO/HFEBiY7Q8626/ryWr
sJBRmU+9oVTTZs9oI3S2v7GzywGtb7/J3m9l8QSxYYO7wwT0h3elUzsMD+GOATor
/DYFgyh1tc5lzyyyHUvpzJdTIDj0twwvPC/pE9zGy27PSj++R/1xtOgndShNE8PB
wmqu3B+3sHLV9+kLW8OHUJ08jplspVa4tE/RaT4kQ+/sSh5bjj27oZnRVtCi1t20
kkiFfcj69L1BLi6xZ9H2ETzbYeX6wctzwFCZrI/+4K5wTQIDAQABoAAwDQYJKoZI
hvcNAQELBQADggEBABugIdtTYtvwBwjkvE4YEv+N56sw+aARFx9lrHVDYpXBjG8e
UtstJ+LIBXkXRVJiHcvQ2I9TljZ1ECVqOKiL/0T6sjDgcMGYeVzqRBYW1KBzESpE
sTGep7SvUyXi1KMpnQ0CoQNR/z/KDuvt+cK3Ja2BslfOXc7AFr/M8fVeY7K+BR1F
/psR5PUz7yw6aUj6wTLnk45ezT3TXilypDvNbMIIFrIrGLe79Xz7KGCE1+cVJugr
D0/wZWgLMLGxAWUgrWXdSwJtS5aJW4qyuc/nGHVjxVk7L9C5SxKn2ueofTOnfUbv
m5kIFqBTYkB68FGebWpI4c7QISc5OhiiFEAC3tc=
-----END CERTIFICATE REQUEST-----
</disable-copy>
{{< /command >}}

We then sign the CSR with the CA using:

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

The signed CA certificate created with the ARN `CertficiateArn`.

### Import CA Certificate

Finally, we retrieve the signed certificate with [`GetCertificate`](https://docs.aws.amazon.com/privateca/latest/APIReference/API_GetCertificate.html) and import it using [`ImportCertificateAuthorityCertificate`](https://docs.aws.amazon.com/privateca/latest/APIReference/API_ImportCertificateAuthorityCertificate.html).

{{< command >}}
$ awslocal acm-pca get-certificate \
    --certificate-authority-arn arn:aws:acm-pca:eu-central-1:000000000000:certificate-authority/0b20353f-ce7a-4de4-9b82-e06903a893ff \
    --certificate-arn arn:aws:acm-pca:eu-central-1:000000000000:certificate-authority/0b20353f-ce7a-4de4-9b82-e06903a893ff/certificate/17ef7bbf3cc6471ba3ef0707119b8392 \
    --output text | tee cert.pem
<disable-copy>
-----BEGIN CERTIFICATE-----
MIIDQDCCAiigAwIBAgIUWsM4iHOoFE71RottADZQ36ePNJYwDQYJKoZIhvcNAQEN
BQAwQDELMAkGA1UEBhMCVVMxDzANBgNVBAoMBkFtYXpvbjEVMBMGA1UECwwMU2Vy
dmVyIENBIDFCMQkwBwYDVQQDDAAwHhcNMjQwODA4MDUyMzUxWhcNMjUwODA4MDUy
MzUxWjB0MQswCQYDVQQGEwJVUzETMBEGA1UECAwKQ2FsaWZvcm5pYTEWMBQGA1UE
BwwNU2FuIEZyYW5jaXNjbzETMBEGA1UECgwKTXkgQ29tcGFueTEjMCEGA1UEAwwa
bG9jYWxob3N0LmxvY2Fsc3RhY2suY2xvdWQwggEiMA0GCSqGSIb3DQEBAQUAA4IB
DwAwggEKAoIBAQCz5Vh8T+e2icQHPmdlV0CPKiIujsNWUwR6RRjvYlyyPqiWStCV
GE+V8s+85Ommo7rce5DUBH+h+0VOSO36cK8g78cUQGJjtDzrbr+vJauwkFGZT72h
VNNmz2gjdLa/sbPLAa1vv8neb2XxBLFhg7vDBPSHd6VTOwwP4Y4BOiv8NgWDKHW1
zmXPLLIdS+nMl1MgOPS3DC88L+kT3MbLbs9KP75H/XG06Cd1KE0Tw8HCaq7cH7ew
ctX36Qtbw4dQnTyOmWylVri0T9FpPiRD7+xKHluOPbuhmdFW0KLW3bSSSIV9yPr0
vUEuLrFn0fYRPNth5frBy3PAUJmsj/7grnBNAgMBAAEwDQYJKoZIhvcNAQENBQAD
ggEBAC3oGUW6brHXHZlEqUr4KA7tuINh8CysXTThMfJ3qlO4yJdtj3JI/AeFBpvu
9tBnf+lmbjzs5cWAEXKlZSj24V4npzuxIiMHLgMW38FCiy2th2KyTPxjtynP8wjz
THy4kvBEpmtDtRAyAgMtAqs3svuGgFUTXlK77GZLgQ48wqnV3hHF9PTndJevqy9j
C2jmoHNKMmO7pWYo6kfUGdFCzjy0X1E5SACZYw0xru1w5XM3y2usO7LSnVzJVK6n
+3rkCfYR1NtYzyRiqMCTxnXKy4BiRpHQaSFQqRmc/2S1SZQY8mYqWPQmTp2o48zp
as9oTVimnCEZrCqykUkc8kmELr0=
-----END CERTIFICATE-----
</disable-copy>
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

The CA certificate can also be retrieved at a later point using [`GetCertificateAuthorityCertificate`](https://docs.aws.amazon.com/privateca/latest/APIReference/API_GetCertificateAuthorityCertificate.html).

### Issuing End-entity Certificates

With the private CA set up, you can now issue private end-entity certificates.

<!-- TODO -->

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
