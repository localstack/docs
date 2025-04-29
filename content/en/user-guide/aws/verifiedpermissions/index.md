---
title: "Verified Permissions"
linkTitle: "Verified Permissions"
description: Get started with Verified Permissions on LocalStack
tags: ["Enterprise plan"]
---

## Introduction

Amazon Verified Permissions is a scalable, fine-grained permissions management and authorization service for custom applications.
Verified Permissions enables you to build secure applications faster by externalizing authorization and centralizing policy management and administration.
Verified Permissions uses the [Cedar policy language](https://docs.cedarpolicy.com/) to define fine-grained permissions to protect your application's resources.

Verified Permissions provides authorization by verifying whether a principal is allowed to perform an action on a resource in a given context in your application.

LocalStack allows you to use the Verified Permissions APIs in your local environment to test your authorization logic, with integrations with other AWS services like Cognito.
The supported APIs are available on our [API coverage page](https://docs.localstack.cloud/references/coverage/coverage_verifiedpermissions/), which provides information on the extent of Verified Permissions' integration with LocalStack.

{{< callout >}}
Verified Permissions is available as part of the LocalStack Enterprise plan.
If you'd like to try it out, please [contact us](https://www.localstack.cloud/demo) to request access.
{{< /callout >}}

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

First, create a JSON file containing the following policy named `static_policy.json`:

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

## Integration with Cognito

Verified Permissions allows you to use external identity provider (IdP) via Identity Sources.
Your application can use JSON web tokens (JWTs) generated by your IdP in authorization requests.
The user identity in the token is mapped to the principal ID of the request.

With ID tokens, Verified Permissions maps attribute claims to principal attributes.
With Access tokens, these claims are mapped to context.

### Create a Cognito UserPool
To create a user pool, you can use the [`CreateUserPool`](https://docs.aws.amazon.com/cognito-user-identity-pools/latest/APIReference/API_CreateUserPool.html) API call.
The following command creates a user pool named `avp-test`:

{{< command >}}
$ awslocal cognito-idp create-user-pool \
  --pool-name avp-test
{{< /command >}}

You can see an output similar to the following:

```json
{
    "UserPool": {
        "Id": "us-east-1_84e2d3fb5af24aba9827b82a6971b17f",
        "Name": "avp-test",
        "Arn": "arn:aws:cognito-idp:us-east-1:000000000000:userpool/us-east-1_84e2d3fb5af24aba9827b82a6971b17f",
        "LastModifiedDate": 1745357214.529315,
        "CreationDate": 1745357214.529319,
        "SchemaAttributes": ["...truncated"],
        "VerificationMessageTemplate": {
            "DefaultEmailOption": "CONFIRM_WITH_CODE"
        },
        "MfaConfiguration": "OFF",
        "EstimatedNumberOfUsers": 0,
        "EmailConfiguration": {
            "EmailSendingAccount": "COGNITO_DEFAULT"
        },
        "UserPoolTier": "ESSENTIALS",
        "...": "truncated"
    }
}
```

You will need the user pool's `Id` and `Arn` for further operations.

### Create a User Pool Client

You can proceed with adding a client to the pool we just created.
You will require the ID of the newly created client for the subsequent steps.
You can use the [`CreateUserPoolClient`](https://docs.aws.amazon.com/cognito-user-identity-pools/latest/APIReference/API_CreateUserPoolClient.html) for both client creation and extraction of the corresponding ID.
Run the following command, replacing the `--user-pool-id` with the one from the previous step:

{{< command >}}
$ awslocal cognito-idp create-user-pool-client \
  --user-pool-id us-east-1_84e2d3fb5af24aba9827b82a6971b17f \
  --client-name avp-client
{{< /command >}}

You can see an output similar to the following:

```json
{
    "UserPoolClient": {
        "UserPoolId": "us-east-1_84e2d3fb5af24aba9827b82a6971b17f",
        "ClientName": "avp-client",
        "ClientId": "xhixnryjv7fcc07s95xau9cjze",
        "LastModifiedDate": 1745357329.211135,
        "CreationDate": 1745357329.211147,
        "RefreshTokenValidity": 30,
        "TokenValidityUnits": {},
        "AllowedOAuthFlowsUserPoolClient": false,
        "EnableTokenRevocation": true,
        "EnablePropagateAdditionalUserContextData": false,
        "AuthSessionValidity": 3
    }
}
```

You will also need the user pool client's `ClientId` for further operations.

### Create a Cognito Group

To use a Verified Permissions policy that validate whether your user is part of a group, we can leverage Cognito Groups.

First, create a group named `AVPGroup`:
{{< command >}}
$ awslocal cognito-idp create-group \
  --user-pool-id us-east-1_84e2d3fb5af24aba9827b82a6971b17f \
  --group AVPGroup
{{< /command >}}

### Create a Cognito User

You can now create a user, which will be used when sending requests to Verified Permissions.
We will use `avp-user` for its username, and `avp@test.com` as its email address.

We can run the 4 following commands to create the user, add it to the Cognito Group then get the Identity Token and Access Token for the user.
You will need to replace the `--user-pool-id` from the User Pool `id` from the first step, and the `--client-id` with the User Pool Client `id` from the step above.

{{< command >}}
$ awslocal cognito-idp admin-create-user \
  --user-pool-id us-east-1_84e2d3fb5af24aba9827b82a6971b17f \
  --username avp-user \
  --user-attributes Name=email,Value="avp@test.com" Name=email_verified,Value=true
{{< /command >}}

{{< command >}}
$ awslocal cognito-idp admin-set-user-password \
  --user-pool-id us-east-1_84e2d3fb5af24aba9827b82a6971b17f \
  --username avp-user \
  --password Test123! \
  --permanent
{{< /command >}}

{{< command >}}
$ awslocal cognito-idp admin-add-user-to-group \
  --user-pool-id us-east-1_84e2d3fb5af24aba9827b82a6971b17f \
  --username avp-user \
  --group-name AVPGroup
{{< /command >}}

{{< command >}}
$ awslocal cognito-idp initiate-auth \
  --auth-flow USER_PASSWORD_AUTH \
  --client-id xhixnryjv7fcc07s95xau9cjze \
  --auth-parameters USERNAME=avp-user,PASSWORD=Test123!
{{< /command >}}

From the last command, you can see an output similar to the following:

```json
{
    "ChallengeParameters": {},
    "AuthenticationResult": {
        "AccessToken": "eyJhbGciOiJSUzI1NiIsImtpZCI6IjUyNmMzMjlkLWQ4OWUtNGM0NC1hN2VkLWQ3YTZkNzcwNzNmZCIsInR5cCI6IkpXVCJ9.eyJleHAiOjE3NDUzNTQxNDMsImlzcyI6Imh0dHA6Ly9sb2NhbGhvc3QubG9jYWxzdGFjay5jbG91ZDo0NTY2L3VzLWVhc3QtMV84NGUyZDNmYjVhZjI0YWJhOTgyN2I4MmE2OTcxYjE3ZiIsInN1YiI6IjNhYjllODE2LTgwYWMtNDdlYS1iZDVmLTllMjlmOTc2NzNjZSIsImF1dGhfdGltZSI6MTc0NTM1MDU0MywiaWF0IjoxNzQ1MzUwNTQzLCJldmVudF9pZCI6ImU4Yjg5Yzg2LTdkMGMtNDdhYS1hZTM3LWNjZjEwZDc4M2JiNiIsInRva2VuX3VzZSI6ImFjY2VzcyIsInVzZXJuYW1lIjoiYXZwLXVzZXIiLCJqdGkiOiJiZmE4MTM3YS0zOGFhLTQ1ZmYtYTY0Ni1kYTE3N2VlMTlkMTAiLCJjbGllbnRfaWQiOiJ4aGl4bnJ5anY3ZmNjMDdzOTV4YXU5Y2p6ZSIsImNvZ25pdG86Z3JvdXBzIjpbIkFWUEdyb3VwIl0sInNjb3BlIjoiYXdzLmNvZ25pdG8uc2lnbmluLnVzZXIuYWRtaW4ifQ.ZjoWd1uDunMPHUDcU6s8RuRzLRCB6dUKK_-VAoxXHC5K6Jf91Zie1hOiC_NCcW5yzre50RtsV458pNoHSF0nsehzgEz8Ockgc1tJ13UNBMDYRZXuSVoOsuTMYfizkxY3kOW4jDAaJthDJw12ja3RAUyr2Mdttka6PdzcbCOmX2Xf6MwL6CJbzb63zOg0Bl052rkYmSXvI2KvoSt0MijIvWfh-v6Hf7kWPjQxNODh5oWEbX3k-Bm519R3QBy4ZzCH5OrRbVjeUUX0SF5S1Ml_4JfROIqjK08c-NjzExBV1REHahaAJFzZlmoXkWTFxfLF80wXGYHGAR4AMm08LjZp7g",
        "ExpiresIn": 3600,
        "TokenType": "Bearer",
        "RefreshToken": "2d104b31",
        "IdToken": "eyJhbGciOiJSUzI1NiIsImtpZCI6IjUyNmMzMjlkLWQ4OWUtNGM0NC1hN2VkLWQ3YTZkNzcwNzNmZCIsInR5cCI6IkpXVCJ9.eyJleHAiOjE3NDUzNTQxNDMsImlzcyI6Imh0dHA6Ly9sb2NhbGhvc3QubG9jYWxzdGFjay5jbG91ZDo0NTY2L3VzLWVhc3QtMV84NGUyZDNmYjVhZjI0YWJhOTgyN2I4MmE2OTcxYjE3ZiIsInN1YiI6IjNhYjllODE2LTgwYWMtNDdlYS1iZDVmLTllMjlmOTc2NzNjZSIsImF1dGhfdGltZSI6MTc0NTM1MDU0MywiaWF0IjoxNzQ1MzUwNTQzLCJldmVudF9pZCI6ImU4Yjg5Yzg2LTdkMGMtNDdhYS1hZTM3LWNjZjEwZDc4M2JiNiIsInRva2VuX3VzZSI6ImlkIiwiY29nbml0bzp1c2VybmFtZSI6ImF2cC11c2VyIiwiZW1haWwiOiJhdnBAdGVzdC5jb20iLCJhdWQiOiJ4aGl4bnJ5anY3ZmNjMDdzOTV4YXU5Y2p6ZSIsImNvZ25pdG86Z3JvdXBzIjpbIkFWUEdyb3VwIl0sImVtYWlsX3ZlcmlmaWVkIjoidHJ1ZSIsImNvZ25pdG86dXNlcl9zdGF0dXMiOiJDT05GSVJNRUQifQ.C1tPAu7K7ZBfG5kZtoNRFiTPi3XUG4znTSFLiuSx72CUOe4SIVUkK3fIJ8pg2-CzlbUWKCczRwom2XzLjJkbmYPT3yd6sf3fuQldVS9HFBpYx42v3h23UUz_sccUPpXzuL1sNYzJmoJ_XyVpKBSdCtXYatKbV6o_beZmcQ6GFPTa5iNfAXeozEpjcWl-mHsd3nXVvTr5SrB8dofPfWGGEqYXYwCSBNnb5hXqON1-uwVe2JvyoRQCiqphtxVdjlRn1BYKfwlDm7EWU5-6CPWzqGfnKUrGaacdrYE6UUL5Q0AhA4MuULl0pwk6unzUHJ9SxKipWYdKd8nsx3k4qFSw8Q"
    }
}
```

You will need the `IdToken` for the Verified Permissions authorization request.

### Create a Policy Store

We can now create a new Policy Store:
{{< command >}}
$ awslocal verifiedpermissions create-policy-store \
  --validation-settings mode=OFF \
  --description "Policy Store with Cognito"
{{< /command >}}

The above command returns the following response:

```json
{
    "policyStoreId": "ESIPIqX1pUHDvwqekZno1G",
    "arn": "arn:aws:verifiedpermissions::000000000000:policy-store/ESIPIqX1pUHDvwqekZno1G",
    "createdDate": "2025-04-22T19:37:00.762622Z",
    "lastUpdatedDate": "2025-04-22T19:37:00.762622Z"
}
```

You will need the `policyStoreId` for the next commands.

### Create an Identity Source

You can now create an Identity Source, which is a representation of an external identity provider, Cognito in our case.
To create a Verified Permissions Identity Source, use the [`CreateIdentitySource`](https://docs.aws.amazon.com/verifiedpermissions/latest/apireference/API_CreateIdentitySource.html) API.

First, create a JSON file containing the following Identity Source configuration named `identity_source.json`.
Replace the `userPoolArn` with the User Pool `Arn` value from the previous step, and the `clientIds` value from the User Pool Client `Id`:

```json
{
    "cognitoUserPoolConfiguration": {
        "userPoolArn": "arn:aws:cognito-idp:us-east-1:000000000000:userpool/us-east-1_84e2d3fb5af24aba9827b82a6971b17f",
        "clientIds":["xhixnryjv7fcc07s95xau9cjze"],
        "groupConfiguration": {"groupEntityType": "UserGroup"}
    }
}
```

{{< command >}}
$ awslocal verifiedpermissions create-identity-source \
  --policy-store-id ESIPIqX1pUHDvwqekZno1G \
  --principal-entity-type "User" \
  --configuration file://identity_source.json
{{< /command >}}

### Create a Policy

You will now create a Policy that will take advantage of the configuration of your Identity Source, and will provide access to the resource if the principal is part of the group type that was defined in the IdentitySource configuration, and the group identity that was defined in Cognito.

First, create a JSON file containing the following policy named `policy_cognito.json`:

```json
{
    "static": {
        "description":  "Grant any User that is part of the UserGroup `` access to view the trip Album",
        "statement": "permit(principal in UserGroup::\"AVPGroup\", action == Action::\"create\", resource == Album::\"vacations\");"
    }
}
```

You can then run this command to create the policy:
{{< command >}}
$ awslocal verifiedpermissions create-policy \
    --definition file://policy_cognito.json \
    --policy-store-id ESIPIqX1pUHDvwqekZno1G
{{< /command >}}

You should see similiar output:

```json
{
    "policyStoreId": "ESIPIqX1pUHDvwqekZno1G",
    "policyId": "cF8X6thXBt5uCANQ8GAEK2",
    "policyType": "STATIC",
    "principal": {
        "entityType": "UserGroup",
        "entityId": "AVPGroup"
    },
    "resource": {
        "entityType": "Album",
        "entityId": "vacations"
    },
    "actions": [
        {
            "actionType": "Action",
            "actionId": "create"
        }
    ],
    "createdDate": "2025-04-22T19:39:54.542438Z",
    "lastUpdatedDate": "2025-04-22T19:39:54.542438Z",
    "effect": "Permit"
}
```

### Authorize a request with a Cognito Token

Finally, you can use everything that we created above to authorize your request.
By using your user's Identity Token, you can run an authorization request that will authenticate your principal, and automatically use the information that its type is of `UserGroup::`, and the value will be from the token attribute `cognito:groups`.

To authorize a request with a token using Verified Permissions, use the [`IsAuthorizedWithToken`](https://docs.aws.amazon.com/verifiedpermissions/latest/apireference/API_IsAuthorizedWithToken.html) API.

You can run the following command to verify that you can authorize the request:

{{< command >}}
$ awslocal verifiedpermissions is-authorized-with-token \
  --policy-store-id ESIPIqX1pUHDvwqekZno1G \
  --action actionType=Action,actionId=create \
  --resource entityType=Album,entityId=vacations \
  --identity-token eyJhbGciOiJSUzI1NiIsImtpZCI6IjUyNmMzMjlkLWQ4OWUtNGM0NC1hN2VkLWQ3YTZkNzcwNzNmZCIsInR5cCI6IkpXVCJ9.eyJleHAiOjE3NDUzNTQxNDMsImlzcyI6Imh0dHA6Ly9sb2NhbGhvc3QubG9jYWxzdGFjay5jbG91ZDo0NTY2L3VzLWVhc3QtMV84NGUyZDNmYjVhZjI0YWJhOTgyN2I4MmE2OTcxYjE3ZiIsInN1YiI6IjNhYjllODE2LTgwYWMtNDdlYS1iZDVmLTllMjlmOTc2NzNjZSIsImF1dGhfdGltZSI6MTc0NTM1MDU0MywiaWF0IjoxNzQ1MzUwNTQzLCJldmVudF9pZCI6ImU4Yjg5Yzg2LTdkMGMtNDdhYS1hZTM3LWNjZjEwZDc4M2JiNiIsInRva2VuX3VzZSI6ImlkIiwiY29nbml0bzp1c2VybmFtZSI6ImF2cC11c2VyIiwiZW1haWwiOiJhdnBAdGVzdC5jb20iLCJhdWQiOiJ4aGl4bnJ5anY3ZmNjMDdzOTV4YXU5Y2p6ZSIsImNvZ25pdG86Z3JvdXBzIjpbIkFWUEdyb3VwIl0sImVtYWlsX3ZlcmlmaWVkIjoidHJ1ZSIsImNvZ25pdG86dXNlcl9zdGF0dXMiOiJDT05GSVJNRUQifQ.C1tPAu7K7ZBfG5kZtoNRFiTPi3XUG4znTSFLiuSx72CUOe4SIVUkK3fIJ8pg2-CzlbUWKCczRwom2XzLjJkbmYPT3yd6sf3fuQldVS9HFBpYx42v3h23UUz_sccUPpXzuL1sNYzJmoJ_XyVpKBSdCtXYatKbV6o_beZmcQ6GFPTa5iNfAXeozEpjcWl-mHsd3nXVvTr5SrB8dofPfWGGEqYXYwCSBNnb5hXqON1-uwVe2JvyoRQCiqphtxVdjlRn1BYKfwlDm7EWU5-6CPWzqGfnKUrGaacdrYE6UUL5Q0AhA4MuULl0pwk6unzUHJ9SxKipWYdKd8nsx3k4qFSw8Q
{{< /command >}}

You should get the following output, indicating that your request was allowed:

```json
{
    "decision": "ALLOW",
    "determiningPolicies": [
        {
            "policyId": "cF8X6thXBt5uCANQ8GAEK2"
        }
    ],
    "errors": [],
    "principal": {
        "entityType": "User",
        "entityId": "us-east-1_84e2d3fb5af24aba9827b82a6971b17f|3ab9e816-80ac-47ea-bd5f-9e29f97673ce"
    }
}
```

Additionally, you can have more advanced and complex scenarios using Cognito attributes and claims to provide more context to your authorization request.
Your policy can also use those additionals attributes to provide more fine-grained authorization.

## Current limitations

LocalStack currently has a few limitations in its emulation capabilities:

- No Schema validation when creating a new schema using `PutSchema`, and no Policy validation using said schema when creating policies and template policies.
- Only Cognito is supported as an IdentitySource, external OIDC providers are not yet implemented.
- The validation around Identity Sources and JWT is not fully yet implemented: the identity source is not validated to have a valid `jwks.json` endpoint, and the issuer, signature and expiration of the incoming JWT are not validated.
