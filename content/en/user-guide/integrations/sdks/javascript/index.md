---
title: "JavaScript"
categories: []
tags: ["sdk"]
description: >
  How to use the JavaScript AWS SDK with LocalStack.
aliases:
  - /integrations/sdks/javascript/
---

## Overview

The [AWS SDK for JavaScript](https://aws.amazon.com/sdk-for-javascript/), like other AWS SDKs, lets you set the endpoint when creating resource clients,
which is the preferred way of integrating the JavaScript SDK with LocalStack.

The JavaScript SDK has two major versions, each with their own way of specifying the LocalStack endpoint:

* [aws-sdk-js](https://github.com/aws/aws-sdk-js)
* [aws-sdk-js-v3](https://github.com/aws/aws-sdk-js-v3)

## Examples

Here is an example of how to create a Lambda client and an S3 client with the endpoint set to LocalStack.

{{< tabpane >}}
{{< tab header="aws-sdk-js" lang="javascript" >}}

WIP

{{< /tab >}}
{{< tab header="aws-sdk-js-v3" lang="javascript" >}}

WIP

/* By default, @aws-sdk/client-s3 will using virtual host addressing (http://<bucket-name>.s3.localhost.localstack.cloud:4566/<key-name>). To allow those requests to be directed to LocalStack, you need to set a specific endpoint. If this is not possible, you can set the special S3 configuration flag to use path addressing instead (http://s3.localhost.localstack.cloud:4566/<bucket-name>/<key-name>). 
*/

const client = new S3({
  region: "us-east-1",
  forcePathStyle: true,
  endpoint: "http://s3.localstack.localhost.cloud:4566"
});

{{< /tab >}}
{{< /tabpane >}}

{{< alert title="Note">}}
In case of issues resolving S3 DNS record, we can fallback to http://localhost:4566 in combination with the provider setting `forcePathStyle: true` (see the specific way of setting this parameter for each SDK above). The S3 service endpoint is slightly different from the other service endpoints, because AWS is deprecating path-style based access for hosting buckets.
{{< /alert >}}


## Resources

* [AWS SDK for Go](https://aws.amazon.com/sdk-for-javascript/)
* [Official repository of the AWS SDK for JavaScript (v2)](https://github.com/aws/aws-sdk-js)
* [Official repository of the AWS SDK for JavaScript (v3)](https://github.com/aws/aws-sdk-js-v3)
