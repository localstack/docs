---
title: "AppSync"
linkTitle: "AppSync"
categories: ["LocalStack Pro"]
description: >
  AppSync
aliases:
  - /aws/appsync/
---

Basic support for AppSync is included in LocalStack Pro. The local AppSync API allows you to spin up local GraphQL APIs and directly expose your data sources (e.g., DynamoDB tables) to external clients.

## Example AppSync API with DynamoDB data source

For example, you can create a DynamoDB table `"posts"` with a key attribute `id`, and define a GraphQL schema in a file `schema.graphql` like this:
```
schema {
    query: Query
}
type Query {
    getPosts: [Post!]!
}
type Post {
    id: DDBString!
}
type DDBString {
    S: String!
}
```
... and then use the AppSync API (or CloudFormation) to create the following entities:

1. a GraphQL API
2. a data source of type `AMAZON_DYNAMODB` that references the `"posts"` DynamoDB table
3. a request mapping template with a content like this:
```json
{
    "version" : "2017-02-28",
    "operation" : "Scan"
}
```
4. a response mapping template with a content like this:
```javascript
$util.toJson($context.result["Items"])
```

Once things have been wired up properly, and assuming the ID of your GraphQL API is `"api123"`, you should be able to run the following GraphQL query to retrieve all items from the `"posts"` DynamoDB table:
{{< command >}}
$ curl -d '{"query":"query {getPosts{id{S}}}"}' http://localhost:4605/graphql/api123
{{< / command >}}

For more details, please refer to the self-contained sample published in [this Github repository](https://github.com/localstack/localstack-pro-samples/tree/master/appsync-graphql-api).

## Custom GraphQL API IDs

It is possible to use a predefined ID when creating GraphQL APIs by setting the tag `_custom_id_`.
For example:

{{< command >}}
$ awslocal appsync create-graphql-api --name my-api --authentication-type API_KEY --tags _custom_id_=faceb00c
{
    "graphqlApi": {
        "name": "my-api",
        "apiId": "faceb00c",
        "authenticationType": "API_KEY",
        "arn": "arn:aws:appsync:us-east-1:000000000000:apis/my-api",
        "uris": {
            "GRAPHQL": "http://localhost:4566/graphql/faceb00c",
            "REALTIME": "ws://localhost:4510/graphql/faceb00c"
        },
        "tags": {
            "_custom_id_": "faceb00c"
        }
    }
}
{{< /command >}}

## GraphQL Resolvers

LocalStack currently provides support for the following [AppSync resolver types](https://docs.aws.amazon.com/appsync/latest/devguide/tutorials.html):

* `AMAZON_DYNAMODB` - for accessing DynamoDB tables
* `RELATIONAL_DATABASE` - for accessing RDS database tables
* `AWS_LAMBDA` - for retrieving data from Lambda function invocations
* `HTTP` - for calling HTTP endpoints to fetch data
* `NONE` - for pass-through resolver mapping templates that return the incoming payload

## GraphQL Endpoints 

There are three configurable strategies that govern how GraphQL API endpoints are created. The strategy can be configured via the `GRAPHQL_ENDPOINT_STRATEGY` environment variable.

| Value | Format | Description |
| - | - | - |
| `domain` | `<api-id>.appsync-api.localhost.localstack.cloud:4566` | This will be the default strategy in the future that uses the `localhost.localstack.cloud` domain to route to your localhost |
| `path` | `localhost:4566/appsync-api/<api-id>/graphql` | An alternative that can be useful if you cannot resolve LocalStack's localhost domain |
| `legacy` | `localhost:4566/graphql/<api-id>` | The old shape of the endpoint, which is currently the default but will be phased out|
