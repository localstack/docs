---
title: "Credentials"
linkTitle: "Credentials"
weight: 50
description: >
  Credentials for accessing LocalStack AWS API
---

Like AWS, LocalStack requires access key IDs to be set in all operations.
The choice of access key ID will affect [multi-account namespacing]({{< ref "multi-account-setups" >}}).
Values of secret access keys are currently ignored by LocalStack.

Access key IDs can be one of following patterns:

## Accounts IDs

You can specify a 12-digit number which will be taken by LocalStack as the account ID.
For example, `112233445566`.

## Structured access key ID

You can specify a structured key like `LSIAQAAAAAAVNCBMPNSG` (which translates to account ID `000000000042`).
This must be at least 20 characters in length and must be decodable to an account ID.

By default, LocalStack will only accept access keys that start with the `LSIA...` or `LKIA...` prefix.
If keys with `ASIA...`/`AKIA...` prefix are provided, these are rejected and the fallback account ID `000000000000` is used.
This is a safeguard to prevent misuse of production AWS access key IDs.
To disable this safeguard, set the `PARITY_AWS_ACCESS_KEY_ID` configuration variable.

{{< callout "warning" >}}
Disabling the access key safeguard and using production access key IDs may cause accidental connections to AWS.
We strongly recommend leaving it on.
{{< /callout >}}

Please refer to the [IAM docs]({{< ref "user-guide/aws/iam" >}}) to learn how to create access keys in LocalStack.

## Alphanumeric string

You can also specify an arbitrary alphanumeric access key ID like `test` or `foobar123`.
In all such cases, the account ID will be evaluated to `000000000000`.
