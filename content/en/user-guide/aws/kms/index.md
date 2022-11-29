---
title: "Key Management Service (KMS)"
linkTitle: "Key Management Service (KMS)"
categories: ["LocalStack Community"]
description: >
  Get started with Amazon Key Management Service (KMS) on LocalStack
aliases:
  - /aws/kms/
---

Key Management Service (KMS) is mainly about
- Creation and management of cryptographic keys.
- Use of these keys to encrypt / decrypt data or to sign messages and to verify signatures for signed ones.

We advise to consult [the official AWS KMS documentation](https://docs.aws.amazon.com/kms/latest/APIReference/Welcome.html) on all KMS operations.

Keys in KMS roughly fall into the 3 categories:
- **Asymmetric encryption keys**: keys, that hold a pair of a private and a public key. Asymmetric keys can be used either for data encryption and decryption with [Encrypt](https://docs.aws.amazon.com/kms/latest/APIReference/API_Encrypt.html) / [Decrypt](https://docs.aws.amazon.com/kms/latest/APIReference/API_Decrypt.html) or for creation and verification of digital signatures for messages with [Sign](https://docs.aws.amazon.com/kms/latest/APIReference/API_Sign.html) / [Verify](https://docs.aws.amazon.com/kms/latest/APIReference/API_Verify.html) operations. AWS does not allow the same asymmetric key to be used for both pairs of operations - when you create such a key, you have to specify in its [KeyUsage](https://docs.aws.amazon.com/kms/latest/APIReference/API_CreateKey.html#KMS-CreateKey-request-KeyUsage) parameter, which pair of operations the key will support.
- **Symmetric encryption keys**: these keys consist of just one key. Symmetric keys **can not** be used to sign and to verify messages. They are only used to encrypt and to decrypt data.
- **Hash-Based Message Authentication Code (HMAC) keys**: a special case of symmetric keys that are only used in the creation and verification of message authentication codes (MACs) with [GenerateMac](https://docs.aws.amazon.com/kms/latest/APIReference/API_GenerateMac.html) / [VerifyMac](https://docs.aws.amazon.com/kms/latest/APIReference/API_VerifyMac.html) operations. You can read more about the use of HMAC keys [on the official AWS page](https://docs.aws.amazon.com/kms/latest/developerguide/hmac.html).

You can check [the official AWS reference page](https://docs.aws.amazon.com/kms/latest/developerguide/symm-asymm-compare.html) to see what other operations are supported for each type of keys. When you know what operations you require, this reference can help to figure out what key types are suitable for your goals.

## Tutorial

Let's create a simple symmetric encryption key and use it to encrypt / decrypt something.

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

The value of the `CiphertextBlob` field is a Base64-encoded result of the encryption of our plaintext. To decrypt this with KMS, we must first get rid of this Base64-encoding. So to our `Encrypt` operation we add the `output` parameter, requesting the output to be in the text form instead of the default JSON. We also supply the `query` parameter, so the output only contains the value of the specified `CiphertextBlob` field. Then we feed the result to the `base64` tool, asking it to remove the Base64 encoding, producing a binary output. We save that output to a file for future use. **Note:** Careful with the `CiphertextBlob` value for the `query` parameter - the AWS CLI doesn't check if the requested field is even if the output, so if you have a typo, the command will succeed, but the data sent to `base64` is going to be just a word `None`. It will lead to unexpected results later.

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

## Current differences between LocalStack KMS and AWS KMS

1. LocalStack KMS always performs symmetric key encryption - even if the requested key is an asymmetric one. LocalStack also has a format of encrypted data different from the one used in AWS. This would cause your decryption to fail if you create a key yourself outside LocalStack KMS, import it to KMS with the [ImportKeyMaterial](https://docs.aws.amazon.com/kms/latest/APIReference/API_ImportKeyMaterial.html) operation, encrypt something with LocalStack KMS and then try to decrypt it outside of LocalStack with your copy of the key. Less exotic setups should be fine. 
2. In AWS KMS, keys have many possible [states](https://docs.aws.amazon.com/kms/latest/developerguide/key-state.html). In LocalStack KMS, only `Enabled`, `Disabled` and `PendingDeletion` states exist.
3. LocalStack KMS supports [multi-region keys](https://docs.aws.amazon.com/kms/latest/developerguide/multi-region-keys-overview.html), but, unlike in AWS KMS, multi-region key replicas are not synchronized with their primary key. So if you create a replica of a multi-regional key and then update some settings for the primary key, the replica won't get automatically updated.
4. AWS KMS has [aliases](https://docs.aws.amazon.com/kms/latest/developerguide/kms-alias.html), that are created automatically for KMS keys used by services like, for example, S3. While LocalStack supports those pre-created aliases, they are getting created on the first attempt to access such an alias and are not visible before such an attempt.   