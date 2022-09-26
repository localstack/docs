---
title: "LocalStack Concepts"
weight: 6
description: >
  Get a condensed overview of the most important architectural concepts of LocalStack.
---

When you first start working on LocalStack, you will most likely start working on AWS providers, either fixing bugs or adding features. In that case, you probably care mostly about Services, and, depending on the service and how it interacts with the Gateway, also **custom request handlers** and edge **routes**.

If you are adding new service providers, then you’ll want to know how Plugins work, and how to expose a service provider as a service plugin. This guide will give you a comprehensive overview about various core architectural concepts of LocalStack.

## AWS Server Framework (ASF)

AWS is essentially a Remote Procedure Call (RPC) system, and ASF is our server-side implementation of that system. The principal components of which are:

-   Service specifications
-   Stub generation
-   Remote objects (service implementations)
-   Marshalling
-   Skeleton

## Service specifications

AWS developed a specification language, [Smithy](https://awslabs.github.io/smithy/), which they use internally to define their APIs in a declarative way. They use these specs to generate client SDKs and client documentation. All these specifications are available, among other repositories, in the [botocore repository](https://github.com/boto/botocore/tree/develop/botocore/data). Botocore are the internals of the AWS Python SDK, which allows ASF to interpret and operate on the service specifications. Take a look at an example, [the `Invoke` operation of the `lambda` API](https://github.com/boto/botocore/blob/474e7a23d0fd178790579638cec9123d7e92d10b/botocore/data/lambda/2015-03-31/service-2.json#L564-L573):

```json 
	"Invoke":{
    "name":"Invoke",
    "http":{
      "method":"POST",
      "requestUri":"/2015-03-31/functions/{FunctionName}/invocations"
    },
    "input":{"shape":"InvocationRequest"},
    "output":{"shape":"InvocationResponse"},
    "errors":[
      {"shape":"ServiceException"},
    ...
```

## Scaffold - Generating AWS API stubs

We use these specifications to generate server-side API stubs using our scaffold script. The stubs comprise Python representations of _Shapes_ (type definitions), and an `<Service>Api` class that contains all the operations as function definitions. Notice the `@handler` decorator, which binds the function to the particular AWS operation. This is how we know where to dispatch the request to.

<img src="asf-code-generation.png" width="600px" alt="Generating AWS API stubs via ASF">

You can try it using this command in the LocalStack repository:

{{< command >}}
$ python -m localstack.aws.scaffold generate <service> --save [--doc]
{{< /command >}}

## Service providers

A service provider is an implementation of an AWS service API. Service providers are the remote object in the RPC terminology. You will find the modern ASF provider implementations in `localstack/services/<service>/provider.py`.

## Marshalling

A server-side protocol implementation requires a marshaller (a parser for incoming requests, and a serializer for outgoing responses).

- Our [protocol parser](https://github.com/localstack/localstack/blob/master/localstack/aws/protocol/parser.py) translates AWS HTTP requests into objects that can be used to call the respective function of the service provider.
- Our [protocol serializer](https://github.com/localstack/localstack/blob/master/localstack/aws/protocol/serializer.py) translates response objects coming from service provider functions into HTTP responses.

