---
title: "Verified Permissions"
linkTitle: "Verified Permissions"
description: Get started with Verified Permissions on LocalStack
tags: ["Ultimate"]
---

## Introduction

Amazon Verified Permissions is a scalable service for managing fine-grained permissions and authorization in custom applications.  
It helps secure applications by moving authorization logic outside the app and managing policies in one place, using the [Cedar policy language](https://docs.cedarpolicy.com/) to define access rules.  
It checks if a principal can take an action on a resource in a specific context in your application.

LocalStack allows you to use the Verified Permissions APIs in your local environment to test your authorization logic, with integrations with other AWS services like Cognito.
The supported APIs are available on our [API coverage page](https://docs.localstack.cloud/references/coverage/coverage_verifiedpermissions/), which provides information on the extent of Verified Permissions' integration with LocalStack.

## Getting started

This guide is designed for users new to Verified Permissions and assumes basic knowledge of the AWS CLI and our [`awslocal`](https://github.com/localstack/awscli-local) wrapper script.

Start your LocalStack container using your preferred method.
We will demonstrate how to create a Verified Permissions Policy Store, add a policy to it, and authorize a request with the AWS CLI.

### Create a Policy Store

To create a Verified Permissions Policy Store, use the [`CreatePolicyStore`](https://docs.aws.amazon.com/verifiedpermissions/latest/apireference/API_CreatePolicyStore.html) API.
Run the following command to create a Policy Store with Schema validation settings set to `OFF`:

{{< command >}}
$ awslocal verifiedpermissions create-policy-store \
  --validation-settings mode=OFF \
  --description "A local Policy Store"
{{< /command >}}

The above command returns the following response:

```json
{
    "policyStoreId": "q5PCScu9qo4aswMVc0owNN",
    "arn": "arn:aws:verifiedpermissions::000000000000:policy-store/q5PCScu9qo4aswMVc0owNN",
    "createdDate": "2025-04-22T19:24:11.175557Z",
    "lastUpdatedDate": "2025-04-22T19:24:11.175557Z"
}
```

You can list all the Verified Permissions policy stores using the [`ListPolicyStores`](https://docs.aws.amazon.com/verifiedpermissions/latest/apireference/API_ListPolicyStores.html) API.
Run the following command to list all the Verified Permissions policy stores:

{{< command >}}
$ awslocal verifiedpermissions list-policy-stores
{{< /command >}}

### Create a Policy

To create a Verified Permissions Policy, use the [`CreatePolicy`](https://docs.aws.amazon.com/verifiedpermissions/latest/apireference/API_CreatePolicy.html) API.

Create a JSON file named `static_policy.json` with the following content:

```json
{
    "static": {
        "description":  "Grant the User alice access to view the trip Album",
        "statement": "permit(principal == User::\"alice\", action == Action::\"view\", resource == Album::\"trip\");"
    }
}
```

You can then run this command to create the policy:
{{< command >}}
$ awslocal verifiedpermissions create-policy \
    --definition file://static_policy.json \
    --policy-store-id q5PCScu9qo4aswMVc0owNN
{{< /command >}}

Replace the policy store ID with the ID of the policy store you created previously.

You should see the following output:

```json
{
    "policyStoreId": "q5PCScu9qo4aswMVc0owNN",
    "policyId": "MfsIseJDeZsr5WUm3tB4FX",
    "policyType": "STATIC",
    "principal": {
        "entityType": "User",
        "entityId": "alice"
    },
    "resource": {
        "entityType": "Album",
        "entityId": "trip"
    },
    "actions": [
        {
            "actionType": "Action",
            "actionId": "view"
        }
    ],
    "createdDate": "2025-04-22T19:25:25.161652Z",
    "lastUpdatedDate": "2025-04-22T19:25:25.161652Z",
    "effect": "Permit"
}
```

### Authorize a request

We can now make use of the Policy Store and the Policy to start authorizing requests.
To authorize a request using Verified Permissions, use the [`IsAuthorized`](https://docs.aws.amazon.com/verifiedpermissions/latest/apireference/API_IsAuthorized.html) API.

{{< command >}}
$ awslocal verifiedpermissions is-authorized \
  --policy-store-id q5PCScu9qo4aswMVc0owNN \
  --principal entityType=User,entityId=alice \
  --action actionType=Action,actionId=view \
  --resource entityType=Album,entityId=trip
{{< /command >}}

You should get the following output, indicating that your request was allowed:

```json
{
    "decision": "ALLOW",
    "determiningPolicies": [
        {
            "policyId": "MfsIseJDeZsr5WUm3tB4FX"
        }
    ],
    "errors": []
}
```

## Current limitations

- No Schema validation when creating a new schema using `PutSchema`, and no Policy validation using said schema when creating policies and template policies.
- Only Cognito is supported as an `IdentitySource`, external OIDC providers are not yet implemented.
- The validation around Identity Sources and JWT is not fully yet implemented: the identity source is not validated to have a valid `jwks.json` endpoint, and the issuer, signature and expiration of the incoming JWT are not validated.
