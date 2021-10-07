---
title: "Cognito"
linkTitle: "Cognito"
categories: ["LocalStack Pro"]
description: >
  Cognito
---
[AWS Cognito](https://aws.amazon.com/cognito/) enables you to manage authentication and access control for AWS-backed apps and resources.

LocalStack Pro contains basic support for authentication via Cognito. You can create Cognito user pools, sign up and confirm users, set up Lambda triggers, and use the `COGNITO_USER_POOLS` authorizer integration with API Gateway.

{{< alert title="SMTP settings" >}}
By default, Cognito does not send actual email messages. To enable this feature, you will require an e-mail address and the corresponding SMTP settings ([see below](#smtp-integration)).
{{< /alert >}}

## Creating a User Pool

Just as with AWS, you can create a user pool in LocalStack with the following command:
{{< command >}}
$ awslocal cognito-idp create-user-pool --pool-name test
{{< /command >}}

The response should look similar to this:

```json
"UserPool": {
        "Id": "us-east-1_fd924693e9b04f549f989283123a29c2",
        "Name": "test",
        "Policies": {
            "PasswordPolicy": {
                "MinimumLength": 8,
                "RequireUppercase": true,
                "RequireLowercase": true,
                "RequireNumbers": true,
                "RequireSymbols": true,
                "TemporaryPasswordValidityDays": 7
            }
        },
        "LastModifiedDate": "2021-10-06T11:57:21.883Z",
        "CreationDate": "2021-10-06T11:57:21.883Z",
        "SchemaAttributes": [],
        "VerificationMessageTemplate": {
            "DefaultEmailOption": "CONFIRM_WITH_CODE"
        },
        "EmailConfiguration": {
            "EmailSendingAccount": "COGNITO_DEFAULT"
        },
        "AdminCreateUserConfig": {
            "AllowAdminCreateUserOnly": false
        },
        "Arn": "arn:aws:cognito-idp:us-east-1:000000000000:userpool/us-east-1_fd924693e9b04f549f989283123a29c2"
}
```

We will need the user pool's `id` for further operations, so save it in a `pool_id` variable:
{{< command >}}
$ pool_id=<your-pool-id>
{{< /command >}}

Alternatively, you can also use a JSON processor like [`jq`](https://stedolan.github.io/jq/) to directly extract the necessary information when creating a pool in the first place:

{{< command >}}
$ pool_id=$(awslocal cognito-idp create-user-pool --pool-name test | jq -rc ".UserPool.Id")
{{< /command >}}

## Adding a Client

Now we add a client to our newly created pool. Again, we will also need the ID of the created client for the next step. The complete command for client creation with subsequent ID extraction is therefore:

{{< command >}}
$ client_id=$(awslocal cognito-idp create-user-pool-client --user-pool-id $pool_id --client-name test-client | jq -rc ".UserPoolClient.ClientId")
{{< /command >}}

## Signing up and confirming a user

With these steps already taken, we can now sign up a user:
{{< command >}}
$ awslocal cognito-idp sign-up --client-id $client_id --username example_user --password 12345678 --user-attributes Name=email,Value=<your.email@address.com>
{{< /command >}}

The response should look similar to this:
```json
{
    "UserConfirmed": false,
    "UserSub": "5fdbe1d5-7901-4fee-9d1d-518103789c94"
}
```

After the user is created, a confirmation code is generated. The code is printed in the LocalStack container logs (see below), and can optionally also be sent via email if you have [SMTP configured](#smtp-integration).

```
INFO:localstack_ext.services.cognito.cognito_idp_api: Confirmation code for Cognito user example_user: 125796
DEBUG:localstack_ext.bootstrap.email_utils: Sending confirmation code via email to "your.email@address.com"
```

We can confirm the user with the activation code, using the following command:
{{< command >}}
$ awslocal cognito-idp confirm-sign-up --client-id $client_id --username example_user --confirmation-code <received-confirmation-code>
{{< /command >}}

As the above command doesn't return an answer, we check the pool to see that the request was successful:
{{< command "hl_lines=21" >}}
$ awslocal cognito-idp list-users --user-pool-id $pool_id 
{
    "Users": [
        {
            "Username": "example_user",
            "Attributes": [
                {
                    "Name": "email",
                    "Value": "your.email@address.com"
                },
                {
                    "Name": "sub",
                    "Value": "5fdbe1d5-7901-4fee-9d1d-518103789c94"
                },
                {
                    "Name": "cognito:username",
                    "Value": "example_user"
                }
            ],
            "Enabled": true,
            "UserStatus": "CONFIRMED"
        }
    ]
}
{{< /command >}}

## Cognito Lambda Triggers

Cognito provides a number of lifecycle hooks in the form of Cognito Lambda triggers. These triggers can be used to react to various lifecycle events and customize the behavior of user signup, confirmation, migration, etc.

For example, to define a _user migration_ Lambda trigger, we can first create a Lambda function (say, named `"f1"`) capable of performing the migration, and then define the corresponding `--lambda-config` on the user pool creation:

{{<command >}}
awslocal cognito-idp create-user-pool --pool-name test2 --lambda-config '{"UserMigration":"arn:aws:lambda:us-east-1:000000000000:function:f1"}'
{{< /command >}}

Upon authentication of a non-registered user, Cognito will then automatically call the migration Lambda function and finally add the migrated user to the pool.

More details on Cognito Lambda triggers can be found in the [AWS documentation](https://docs.aws.amazon.com/cognito/latest/developerguide/cognito-user-identity-pools-working-with-aws-lambda-triggers.html).

## OAuth Flows via Cognito Login Form

You can also access the local [Cognito login form](https://docs.aws.amazon.com/cognito/latest/developerguide/login-endpoint.html) by entering the following URL in your browser:
```
http://localhost:4566/login?response_type=code&client_id=<client_id>&redirect_uri=<redirect_uri>
```
Please replace `<client_id>` with the ID of an existing user pool client ID (in this case, `example_user`), and `<redirect_uri>` with the redirect URI of your application (e.g., `http://example.com`).

The login form should look similar to the screenshot below:
{{< figure src="cognitoLogin.png" width="320" >}}

After successful login, the page will redirect to the specified redirect URI, with a path parameter `?code=<code>` appended, e.g., `http://example.com?code=test123`.
This authentication code can then be used to obtain a token via the Cognito OAuth2 TOKEN Endpoint documented [here](https://docs.aws.amazon.com/cognito/latest/developerguide/token-endpoint.html).

## SMTP Integration

In order to enable sending activation emails, configure the following SMTP settings as environment variables:
```env
SMTP_HOST=<smtp-host-address>
SMTP_USER=<email-user-name>
SMTP_PASS=<email-password>
SMTP_EMAIL=<email-address>
```

Please check with your email provider for details regarding the SMTP settings above.

## Serverless and Cognito

You can also use Cognito and Localstack in conjunction with the [Serverless framework](https://www.serverless.com/).

For example, take this snippet of a `serverless.yml` configuration:
```yaml
service: test

plugins:
  - serverless-deployment-bucket
  - serverless-pseudo-parameters
  - serverless-localstack

custom:
  localstack:
    stages: [local]

functions:
  http_request:
    handler: http.request
    events:
      - http:
          path: v1/request
          authorizer:
            arn: arn:aws:cognito-idp:us-east-1:#{AWS::AccountId}:userpool/ExampleUserPool

resources:
  Resources:
    UserPool:
      Type: AWS::Cognito::UserPool
      Properties:
        ...
```

The serverless configuration can then be deployed using `serverless deploy --stage local`.
The example contains a Lambda function `http_request` which is connected to an API Gateway endpoint.
Once deployed, the `v1/request` API Gateway endpoint will be secured against the Cognito user pool "`ExampleUserPool`".
You can then register users against that local pool, using the same API calls as for AWS.

In order to make requests against the secured API Gateway endpoint, use the local Cognito API to retrieve identity credentials which can be sent along as `Authentication` HTTP headers (where `test-1234567` is the name of the access key ID generated by Cognito):

```
Authentication: AWS4-HMAC-SHA256 Credential=test-1234567/20190821/us-east-1/cognito-idp/aws4_request ...
```

## Further reading

For a more detailed example, please check out our [sample repository](https://github.com/localstack/localstack-pro-samples/tree/master/cognito-jwt).
