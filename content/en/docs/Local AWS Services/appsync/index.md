---
title: "AppSync"
linkTitle: "AppSync"
categories: ["LocalStack Pro"]
description: >
  AppSync
---

Basic support for AppSync is included in LocalStack Pro. The local AppSync API allows you to spin up local GraphQL APIs and directly expose your data sources (e.g., DynamoDB tables) to external clients.

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
```bash
curl -d '{"query":"query {getPosts{id{S}}}"}' http://localhost:4605/graphql/api123
```

For more details, please refer to the self-contained sample published in [this Github repository](https://github.com/localstack/localstack-pro-samples/tree/master/appsync-graphql-api).
