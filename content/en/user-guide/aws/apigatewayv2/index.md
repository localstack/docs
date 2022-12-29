---
title: "API Gateway V2"
linkTitle: "API Gateway V2"
categories: ["LocalStack Pro"]
description: >
  Get started with Amazon API Gateway V2 on LocalStack
aliases:
  - /aws/apigatewayv2/
---

The Pro version has support for API Gateway V2 (in addition to V1), which allows for creation of local HTTP as well as WebSocket APIs - for long-lived connections and bi-directional communication between the API and your clients.

## Accessing HTTP APIs via local domain name

For example, the following [Serverless](https://serverless.com/) configuration illustrates two Lambda functions (`serviceV1` and `serviceV2`) connected to an API Gateway v1 (`http` event) and an API Gateway v2 endpoint (`httpApi` event), respectively:
```yaml
...
plugins:
  - serverless-localstack
custom:
  localstack:
    stages: [local]
functions:
  serviceV1:
    handler: handler.handler
    events:
      - http:    # for API GW v1 integration
          method: POST
          path: /my/path1
  serviceV2:
    handler: handler.handler
    events:
      - httpApi: # for API GW v2 integration
          method: POST
          path: /my/path2
```

Once deployed, the API Gateway endpoints above can be accessed via the LocalStack edge port (`4566` by default).

There are two alternative URL formats for accessing the APIs (for both, v1 and v2 APIs). The recommended format is to use the following URL syntax with an `execute-api` hostname:

<pre><code>http://<b>&lt;apiId></b>.execute-api.localhost.localstack.cloud:4566/<b>&lt;stageId></b>/<b>&lt;path></b>
</code></pre>

Assuming the ID of the deployed HTTP/REST API is `0v1p6q6`, the invocation URL would be:
```
http://0v1p6q6.execute-api.localhost.localstack.cloud:4566/local/my/path2
```
The alternative format (sometimes used, e.g., in case of local DNS issues) is an endpoint with the predefined path marker `_user_request_`:

<pre><code>http://localhost:4566/restapis/<b>&lt;apiId></b>/<b>&lt;stageId></b>/_user_request_/<b>&lt;path></b>
</code></pre>

... which for the example above would result in:
```
http://localhost:4566/restapis/0v1p6q6/local/_user_request_/my/path1
```


{{< alert >}}
Please note that the URLs above include the name of the API Gateway stage (`local`) - adding the stage is required for API Gateway v1 APIs, but optional for API Gateway v2 APIs (in case they include the wildcard `$default` stage).
In other words, for v2 the URL `http://0v1p6q6.execute-api.localhost.localstack.cloud:4566/my/path1` should also work.
{{</ alert >}}

## WebSocket APIs

To illustrate the use of WebSockets, assume we define the following [Serverless](https://serverless.com/) configuration:
```yaml
...
plugins:
  - serverless-localstack
functions:
  actionHandler:
    handler: handler.handler
    events:
      - websocket:
          route: test-action
```

Upon deployment of the Serverless project, a new API Gateway V2 endpoint will be created in LocalStack. The [`awslocal`](https://github.com/localstack/awscli-local) CLI can be used to get the list of APIs, which should contain the WebSocket endpoint, e.g., `ws://localhost:4510` in the example below:

{{< command >}}
$ awslocal apigatewayv2 get-apis
{
    "Items": [{
        "ApiEndpoint": "ws://localhost:4510",
        "ApiId": "129ca37e",
        ...
    }]
}
{{< / command >}}

Assuming your project contains a simple Lambda `handler.js` like this:

```javascript
module.exports.handler = function(event, context, callback) {
  callback(null, event);
};
```

... then sending a message to the WebSocket at `ws://localhost:4510` will result in the same message getting returned as a response on the same WebSocket.


A backend service can push data to the connection using the [Amazon API Gateway Management API](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/apigatewaymanagementapi/index.html). In LocalStack, it looks like this (make sure to replace `<connectionId>` with your WebSocket connection ID):

{{< command >}}
$ awslocal apigatewaymanagementapi post-to-connection --connection-id '<connectionId>' --data '{"msg": "Hi"}'
{{< / command >}}

For a simple, self-contained example please refer to [this Github repository](https://github.com/localstack/localstack-pro-samples/tree/master/serverless-websockets).

### AWS API Gateway Custom ID via tags

To provide custom IDs for API Gateway REST API, you can specify `tags={"_custom_id_":"myid123"}` on creation of an API Gateway REST API, to assign it the custom ID `"myid123"` (can be useful to have a static API GW endpoint URL for testing).
  
Pre-define the IDs of newly created REST API by specifying a `_custom_id_` tag on it:

{{< command >}}
$ awslocal apigateway create-rest-api --name my-api --tags '{"_custom_id_":"myid123"}'
{
    "id": "myid123",
    ....
}

$ awslocal apigatewayv2 get-apis
{
    "Items": [{
        "ApiEndpoint": "ws://localhost:4510",
        "ApiId": "129ca37e",
        ...
    }]
}
{{< / command >}}

You can also configure the protocol type, the possible values being `HTTP` and `WEBSOCKET`: 

{{< command >}}
$ awslocal apigatewayv2 create-api --name=my-api --protocol-type=HTTP --tags="_custom_id_=my-api"                                                                                                                               
{
    "ApiEndpoint": "my-api.execute-api.localhost.localstack.cloud:4566",
    "ApiId": "my-api",
    "Name": "my-api",
    "ProtocolType": "HTTP",
    "Tags": {
        "_custom_id_": "my-api"
    }
}
{{< / command >}}

### AWS API Gateway Custom Domain Name

Custom domain names can be created for API Gateway REST APIs and API Gateway V2 APIs. The following example shows 
how to call a custom domain name for an API Gateway (v2), but the same applies to API Gateway REST APIs, using the `Host` header with the 
custom domain to route 
the 
request to the mapping target.

{{< command >}}
curl -H 'Host: test.example.com' http://localhost:4566/test
{{< / command >}}

For a simple, self-contained example please refer to [this Github repository](https://github.com/localstack/localstack-pro-samples/tree/master/apigw-custom-domain).
