---
title: "Credentials"
linkTitle: "Credentials"
categories: ["LocalStack"]
tags: ["access-key-id", "secret-access-key", "account-id"]
weight: 5
description: >
  Credentials for accessing LocalStack services
---

Like AWS, LocalStack requires access key IDs to be set in all operations.
The choice of access key ID will affect [multi-account namespacing]({{< ref "multi-account-setups" >}}).
Values of secret access keys are currently ignored by LocalStack.

Access key IDs can be one of following patterns:

### Accounts IDs

You can specify a 12-digit number which will be taken by LocalStack as the account ID.
For example, `112233445566`.

### Structured access key ID

You can specify a structured key like `LSIAQAAAAAAVNCBMPNSG` (which translates to account ID `000000000042`).
This must be atleast 20 characters in length and must be decodable to an account ID.

{{< alert title="Note">}}
In the future LocalStack will support IAM service which will issue proper access key IDs.
{{< /alert >}}

By default, LocalStack will only accept access keys that start with the `LSIA...` or `LKIA...` prefix.
This is a safeguard to prevent misuse of production AWS access key IDs, which start with `ASIA...`/`AKIA...` prefix.
To disable this safeguard, set the `PARITY_AWS_ACCESS_KEY_ID` configuration variable.

{{< alert title="Warning" color="warning" >}}
Disabling the access key safeguard and using production access key IDs may cause accidental connections to AWS.
We strongly recommend leaving it on.
{{< /alert >}}

### Random alphanumeric string

You can also specify an arbitrary alphanumeric access key ID like `test` or `foobar123`.
In all such cases, the account ID will be evalutated to `000000000000`.
