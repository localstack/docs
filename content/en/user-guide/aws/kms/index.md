---
title: "Key Management Service (KMS)"
linkTitle: "Key Management Service (KMS)"
categories: ["LocalStack Community"]
description: >
  Get started with Amazon Key Management Service (KMS) on LocalStack
aliases:
  - /aws/kms/
---

Key Management Service (KMS) is mainly about:
- Creation and management of cryptographic keys.
- Use of these keys to encrypt / decrypt data or to sign messages and to verify signatures for signed ones.

We advise to consult [the official AWS KMS documentation](https://docs.aws.amazon.com/kms/latest/APIReference/Welcome.html) on all KMS operations.

Keys in KMS roughly fall into the 3 categories:
- **Asymmetric encryption keys**: keys, that hold a pair of a private and a public key. Asymmetric keys can be used either for data encryption and decryption with [Encrypt](https://docs.aws.amazon.com/kms/latest/APIReference/API_Encrypt.html) / [Decrypt](https://docs.aws.amazon.com/kms/latest/APIReference/API_Decrypt.html) or for creation and verification of digital signatures for messages with [Sign](https://docs.aws.amazon.com/kms/latest/APIReference/API_Sign.html) / [Verify](https://docs.aws.amazon.com/kms/latest/APIReference/API_Verify.html) operations. AWS does not allow the same asymmetric key to be used for both pairs of operations - when you create such a key, you have to specify in its [KeyUsage](https://docs.aws.amazon.com/kms/latest/APIReference/API_CreateKey.html#KMS-CreateKey-request-KeyUsage) parameter, which pair of operations the key will support.
- **Symmetric encryption keys**: these keys consist of just one key. Symmetric keys **can not** be used to sign and to verify messages. They are only used to encrypt and to decrypt data.
- **Hash-Based Message Authentication Code (HMAC) keys**: a special case of symmetric keys that are only used in the creation and verification of message authentication codes (MACs) with [GenerateMac](https://docs.aws.amazon.com/kms/latest/APIReference/API_GenerateMac.html) / [VerifyMac](https://docs.aws.amazon.com/kms/latest/APIReference/API_VerifyMac.html) operations. You can read more about the use of HMAC keys [on the official AWS page](https://docs.aws.amazon.com/kms/latest/developerguide/hmac.html).

You can check [the official AWS reference page](https://docs.aws.amazon.com/kms/latest/developerguide/symm-asymm-compare.html) to see what other operations are supported for each type of keys. When you know what operations you require, this reference can help to figure out what key types are suitable for your goals.

## Tutorial

Let's first create a simple symmetric encryption key and use it to encrypt/ decrypt something.

A new key can be created in KMS with the following command:

{{< command >}}
$ awslocal kms create-key
{{</ command >}}

By default, this command creates a symmetric encryption key, so we do not even have to supply any additional arguments. In the output we want to pay attention to the ID of the newly created key, `010a4301-4205-4df8-ae52-4c2895d47326` in this case:

```sh
{
    "KeyMetadata": {
        "AWSAccountId": "000000000000",
        "KeyId": "010a4301-4205-4df8-ae52-4c2895d47326",
        "Arn": "arn:aws:kms:us-east-1:000000000000:key/010a4301-4205-4df8-ae52-4c2895d47326",
        "CreationDate": 1665432947.493433,
        "Enabled": true,
        "Description": "",
        "KeyUsage": "ENCRYPT_DECRYPT",
        "KeyState": "Enabled",
        "Origin": "AWS_KMS",
        "KeyManager": "CUSTOMER",
        "CustomerMasterKeySpec": "SYMMETRIC_DEFAULT",
        "KeySpec": "SYMMETRIC_DEFAULT",
        "EncryptionAlgorithms": [
            "SYMMETRIC_DEFAULT"
        ],
        "MultiRegion": false
    }
}
```

If we lose the ID, we can always list IDs and [Amazon Resource Identifiers](https://docs.aws.amazon.com/general/latest/gr/aws-arns-and-namespaces.html) (ARNs) of all the available keys this way:

{{< command >}}
$ awslocal kms list-keys
{{</ command >}}

If necessary, we can also check all the details about a key with a given key ID or ARN like this:

{{< command >}}
$ awslocal kms describe-key --key-id 010a4301-4205-4df8-ae52-4c2895d47326
{{</ command >}}

We can use the key now to encrypt something. Let's say, "*some important stuff*":

{{< command >}}
$ awslocal kms encrypt \
      --key-id 010a4301-4205-4df8-ae52-4c2895d47326 \
      --plaintext "some important stuff" \
      --output text \
      --query CiphertextBlob \
  | base64 --decode > my_encrypted_data
{{</ command >}}

Why do we require such a complicated command? The `Encrypt` Operation itself looks like this:

{{< command >}}
$ awslocal kms encrypt \
      --key-id 010a4301-4205-4df8-ae52-4c2895d47326 \
      --plaintext "some important stuff"
{{</ command >}}

Its output has the following look:

```sh
{
    "CiphertextBlob": "MDA4NDk4ZDYtMGU1ZS00NjU3LWEyZTQtMDliYTcwNDgyMmJkxw1eaLVUeUZA7bZzp+k7VAAAAAAAAAAAAAAAAAAAAAAetG9/5Znpw83/4xhwObc6Fc2B73y1ZvIigwahKopT0Q==",
    "KeyId": "arn:aws:kms:us-east-1:000000000000:key/010a4301-4205-4df8-ae52-4c2895d47326",
    "EncryptionAlgorithm": "SYMMETRIC_DEFAULT"
}
```

The value of the `CiphertextBlob` field is a Base64-encoded result of the encryption of our plaintext. To decrypt this with KMS, we must first get rid of this Base64-encoding. So to our `Encrypt` operation we add the `output` parameter, requesting the output to be in the text form instead of the default JSON. We also supply the `query` parameter, so the output only contains the value of the specified `CiphertextBlob` field. Then we feed the result to the `base64` tool, asking it to remove the Base64 encoding, producing a binary output. We save that output to a file for future use.

{{< alert title="Warning" color="warning">}}
Careful with the `CiphertextBlob` value for the `query` parameter - the AWS CLI doesn't check if the requested field is even if the output, so if you have a typo, the command will succeed, but the data sent to `base64` is going to be just a word `None`. It will lead to unexpected results later.
{{< /alert >}}

When we want to, we can decrypt our file using the same KMS key:

{{< command >}}
$ awslocal kms decrypt \
      --ciphertext-blob fileb://my_encrypted_data \
      --output text \
      --query Plaintext
  | base64 --decode
{{</ command >}}

Here we ask KMS to decrypt the contents of the binary file created during our previous `Encrypt` call. We do not have to specify the `key-id` while decrypting our file - when encrypting something with a symmetric key, AWS includes the key ID into the encrypted data, so can figure out itself which key to use for decryption. With asymmetric keys the `key-id` has to be specified, though.

As with the previous `Encrypt` call, we have to get rid of the Base64-encoding to actually get our data, so we use the `output` and `query` parameters along with the `base64` tool here as well. If everything went fine, the output is going to be our original text:

```sh
some important stuff
```
Let's now create a hash-based message authentication code(HMAC) key and use it to generate and verify mac for a specified message. In this example we will use key specification as `HMAC_256` and mac algorithm as `HMAC_SHA_256`.

An HMAC key can be created in KMS with the following command:

{{< command >}} $ awslocal kms create-key --key-spec HMAC_256 --key-usage GENERATE_VERIFY_MAC {{</ command >}}

Note that the `GENERATE_VERIFY_MAC` value for the `--key-usage` parameter is required even though it's the only valid value for HMAC KMS keys. The allowed values of `--key-spec` parameter can be checked in [official AWS documentation](https://docs.aws.amazon.com/kms/latest/developerguide/hmac.html#hmac-key-specs)

The create HMAC command gives the following output:
```sh
{
    "KeyMetadata": {
        "AWSAccountId": "000000000000",
        "KeyId": "922c14f0-f6e9-4d22-a56a-9619b78621f0",
        "Arn": "arn:aws:kms:us-east-1:000000000000:key/922c14f0-f6e9-4d22-a56a-9619b78621f0",
        "CreationDate": 1681215688.040106,
        "Enabled": true,
        "Description": "",
        "KeyUsage": "GENERATE_VERIFY_MAC",
        "KeyState": "Enabled",
        "Origin": "AWS_KMS",
        "KeyManager": "CUSTOMER",
        "CustomerMasterKeySpec": "HMAC_256",
        "KeySpec": "HMAC_256",
        "MultiRegion": false,
        "MacAlgorithms": [
            "HMAC_SHA_256"
        ]
    }
}
```

We can now use this key and a valid [MAC algorithm](https://docs.aws.amazon.com/kms/latest/developerguide/hmac.html#hmac-key-specs) to generate an HMAC for a message say "some important stuff". 

{{< command >}} $ awslocal kms generate-mac --message "some important stuff" --key-id 922c14f0-f6e9-4d22-a56a-9619b78621f0 --mac-algorithm HMAC_SHA_256 --query Mac --output text | base64 --decode > my_encrypted_data {{</ command >}}

The `GenerateMac` operation has the following output:
```sh
{
    "Mac": "Kl1cQNOgdYmwm3zXCOBfBa/mgq7bywA2HhQj4lHazUg=",
    "MacAlgorithm": "HMAC_SHA_256",
    "KeyId": "arn:aws:kms:us-east-1:000000000000:key/922c14f0-f6e9-4d22-a56a-9619b78621f0"
}
```

We now use `VerifyMac` which is done by computing an HMAC using the message, key, MAC algorithm and this is compared to the HMAC that you specify. . If the HMACs are identical, the verification succeeds; otherwise, it fails.

{{< command >}} $ awslocal kms verify-mac  --message "some important stuff" --key-id 922c14f0-f6e9-4d22-a56a-9619b78621f0 --mac-algorithm HMAC_SHA_256  --mac fileb://my_encrypted_data {{</ command >}}

Its ouput has the following look:

```sh
{
    "KeyId": "arn:aws:kms:us-east-1:000000000000:key/922c14f0-f6e9-4d22-a56a-9619b78621f0",
    "MacValid": true,
    "MacAlgorithm": "HMAC_SHA_256"
}
```

Let's now create an asymmetric KMS key for `Sign` and `Verify` operations. In this example we will use `RSA_2048` key pair for signing and verification, you can look at other specs in the [AWS reference page](https://docs.aws.amazon.com/kms/latest/developerguide/asymmetric-key-specs.html). Also, note that the `--key-usage` parameter is required even though `SIGN_VERIFY` is the only valid value for RSA KMS keys.

{{< command >}} $ awslocal kms create-key --key-spec RSA_2048 --key-usage SIGN_VERIFY {{</ command >}}

The output looks as follows:
```sh
{
    "KeyMetadata": {
        "AWSAccountId": "000000000000",
        "KeyId": "789ffd57-179b-493a-8415-b0b541b3ce7e",
        "Arn": "arn:aws:kms:us-east-1:000000000000:key/789ffd57-179b-493a-8415-b0b541b3ce7e",
        "CreationDate": 1681219769.125121,
        "Enabled": true,
        "Description": "",
        "KeyUsage": "SIGN_VERIFY",
        "KeyState": "Enabled",
        "Origin": "AWS_KMS",
        "KeyManager": "CUSTOMER",
        "CustomerMasterKeySpec": "RSA_2048",
        "KeySpec": "RSA_2048",
        "SigningAlgorithms": [
            "RSASSA_PKCS1_V1_5_SHA_256",
            "RSASSA_PKCS1_V1_5_SHA_384",
            "RSASSA_PKCS1_V1_5_SHA_512",
            "RSASSA_PSS_SHA_256",
            "RSASSA_PSS_SHA_384",
            "RSASSA_PSS_SHA_512"
        ],
        "MultiRegion": false
    }
}
```

Now let's create a digital signature for a message "some important stuff" using the KMS key created in the above command. 

{{< command >}} $ awslocal kms sign --key-id  789ffd57-179b-493a-8415-b0b541b3ce7e --message "some important stuff" --signing-algorithm "RSASSA_PSS_SHA_256" --query Signature --output text | base64 --decode > my_encrypted_data {{</ command >}}

The `Sign` operation has the following output:
```sh
{
    "KeyId": "789ffd57-179b-493a-8415-b0b541b3ce7e",
    "Signature": "pu2nLuRDhUJtLI8gkScv72gSUpWEneGa0DlX0I8vh80CH3UlRWNOoKZjXn5tY2nD9WtKCS+XLkdpJJdrQLcEzuqNA7b3snRMbNeW1T8uY7MrefLud2D8DWota1LckiI/piC7iashOCCMBVkRNRpv59MHEQRr1CWmCzbbHaRwp++dJ+LZ5jHR3ypTI3PU/yPVk0de5MRU3OmHywYukA9mJ11wpNzB/Vud6n9GdDDIkGywjctHOSZYuFvMwf4F4877nrL9xOxjol/tQOMCmwgmRtBn0hFZqjG4LccEiPElLG8w6Ax47KsFWa16QcaWDr4QfptOltVuG3fEYxTpa8+NcQ==",
    "SigningAlgorithm": "RSASSA_PSS_SHA_256"
}
```

Let's now verify the digital signature that was generated by the `Sign` operation. If the signature is verified, the value of the `SignatureValid` field in the response is `True` else if it fails with an `KMSInvalidSignatureException` exception.

{{< command >}} $ awslocal kms verify  --key-id 789ffd57-179b-493a-8415-b0b541b3ce7e --message "some important stuff" --signing-algorithm "RSASSA_PSS_SHA_256"  --signature fileb://my_encrypted_data {{</ command >}}

The `Verify` operaations has the following output:
```sh
{
    "KeyId": "789ffd57-179b-493a-8415-b0b541b3ce7e",
    "SignatureValid": true,
    "SigningAlgorithm": "RSASSA_PSS_SHA_256"
}
```

## Current differences between LocalStack KMS and AWS KMS

1. LocalStack KMS always performs symmetric key encryption - even if the requested key is an asymmetric one. LocalStack also has a format of encrypted data different from the one used in AWS. This would cause your decryption to fail if you create a key yourself outside LocalStack KMS, import it to KMS with the [ImportKeyMaterial](https://docs.aws.amazon.com/kms/latest/APIReference/API_ImportKeyMaterial.html) operation, encrypt something with LocalStack KMS and then try to decrypt it outside of LocalStack with your copy of the key. Less exotic setups should be fine. 
2. In AWS KMS, keys have many possible [states](https://docs.aws.amazon.com/kms/latest/developerguide/key-state.html). In LocalStack KMS, only `Enabled`, `Disabled`, `Creating`, `PendingImport` and `PendingDeletion` states exist.
3. LocalStack KMS supports [multi-region keys](https://docs.aws.amazon.com/kms/latest/developerguide/multi-region-keys-overview.html), but, unlike in AWS KMS, multi-region key replicas are not synchronized with their primary key. So if you create a replica of a multi-regional key and then update some settings for the primary key, the replica won't get automatically updated.
4. AWS KMS has [aliases](https://docs.aws.amazon.com/kms/latest/developerguide/kms-alias.html), that are created automatically for KMS keys used by services like, for example, S3. While LocalStack supports those pre-created aliases, they are getting created on the first attempt to access such an alias and are not visible before such an attempt.   
