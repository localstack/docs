---
title: "Cognito"
linkTitle: "Cognito"
categories: ["LocalStack Pro"]
description: >
  Cognito
---
[AWS Cognito](https://aws.amazon.com/cognito/) enables you to manage authentication and access control for AWS-backed apps and resources.

LocalStack Pro contains basic support for authentication via Cognito. You can create Cognito user pools, sign up and confirm users, and use the `COGNITO_USER_POOLS` authorizer integration with API Gateway.
## Setup
{{< alert title="SMTP settings" >}}
For some Cognito features you will require an e-mail address and the corresponding SMTP settings. Check with your provider for details.
{{< /alert >}}
{{< alert title="sudo" >}}
When using Cognito, LocalStack may prompt you for your sudo password.
{{< /alert >}}

First, start up LocalStack. In addition to the normal setup, we need to pass the SMTP settings as environment variables:
```env
SMTP_HOST=<smtp-host-address>
SMTP_USER=<email-user-name>
SMTP_PASS=<email-password>
SMTP_EMAIL=<email-address>
```
If you only start a subset of the services by using the `SERVICES` environment variable, don't forget to add Cognito as well.

## Creating a User Pool

Just as with AWS, you can create a User Pool in LocalStack with the following command:
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

We will need the UserPool's `id` for further operations, so save it in a `pool_id` variable:
{{< command >}}
$ pool_id=<your-pool-id>
{{< /command >}}

Alternatively, you can also use a JSON processor like `[jq](https://stedolan.github.io/jq/)` to directly extract the necessary information when creating a pool in the first place:

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

In addition to the response, you should receive a new email.

As you can see, our user is still unconfirmed.
We can change this with the following instruction:
{{< command >}}
$ awslocal cognito-idp confirm-sign-up --client-id $client_id --username example_user --confirmation-code <received-confirmation-code>
{{< /command >}}

The verification code for the user is in the e-mail you received. Additionally, LocalStack prints out the verification code in the console logs.

The above command doesn't return an answer, you need to check the pool to see that the request was successful:
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

## Serverless and Cognito
You can also use Cognito and Localstack in conjunction with the [Serverless framework](https://www.serverless.com/).
Again, if you only start a subset of the services by using the `SERVICES` environment variable, don't forget to add `serverless` as well.
 (you need to include serverless in the LocalStack services).

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
For a more extensive example you can check our [sample repository](https://github.com/localstack/localstack-pro-samples/tree/master/cognito-jwt).
