---
title: "JavaScript"
categories: []
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

{{< tabpane lang="javascript" >}}
{{< tab header="aws-sdk-js" lang="javascript" >}}

const AWS = require('aws-sdk');

// Configure the AWS SDK to use the LocalStack endpoint and credentials
const lambda = new AWS.Lambda({
  endpoint: 'http://localhost:4566',
  accessKeyId: 'test',
  secretAccessKey: 'test',
  region: 'us-east-1',
});

// List the Lambda functions using the LocalStack endpoint
lambda.listFunctions({}, (err, data) => {
  if (err) {
    console.error(err);
  } else {
    console.log(data);
  }
});

// Now, we create an S3 client, which has a special endpoint
// You can read the S3 documentation to learn more about the different endpoints.
const s3 = new AWS.S3({
  endpoint: 'http://s3.localhost.localstack.cloud:4566',
  s3ForcePathStyle: true,  // If you want to use virtual host addressing of buckets, you can remove `s3ForcePathStyle: true`. 
  accessKeyId: 'test',
  secretAccessKey: 'test',
  region: 'us-east-1',
});

// If your region is `us-east-1`, you will need to override the globalEndpoint of the client
// due to an issue in the SDK with `createBucket`.
// you will need to set it to the hostname of your endpoint specified right above
// If your region is different than `us-east-1`, you can skip that line
s3.api.globalEndpoint = 's3.localhost.localstack.cloud';

// Call an S3 API using the LocalStack endpoint
s3.listBuckets((err, data) => {
  if (err) {
    console.error(err);
  } else {
    console.log(data);
  }
});
{{< /tab >}}
{{< tab header="aws-sdk-js-v3" lang="javascript" >}}
const { LambdaClient, ListFunctionsCommand } = require('@aws-sdk/client-lambda');
const { S3Client, ListBucketsCommand } = require('@aws-sdk/client-s3');

// Configure the AWS SDK to use the LocalStack endpoint and credentials
const lambda = new LambdaClient({
  endpoint: 'http://localhost:4566',
  region: 'us-east-1',
  credentials: {
    accessKeyId: 'test',
    secretAccessKey: 'test',
  },
});

// Call a Lambda API using the LocalStack endpoint
lambda.send(new ListFunctionsCommand({}))
  .then((data) => console.log(data))
  .catch((error) => console.error(error));


// By default, @aws-sdk/client-s3 will using virtual host addressing:
// -> http://<bucket-name>.s3.localhost.localstack.cloud:4566/<key-name>
// To allow those requests to be directed to LocalStack, you need to set a specific endpoint.
// If this is not possible, you can set the special S3 configuration flag to use path
// addressing instead: 
// -> http://s3.localhost.localstack.cloud:4566/<bucket-name>/<key-name>
// You can read the S3 documentation to learn more about the different endpoints. 

const s3 = new S3Client({
  region: 'us-east-1',
  forcePathStyle: true, // If you want to use virtual host addressing of buckets, you can remove `forcePathStyle: true`. 
  endpoint: 'http://s3.localhost.localstack.cloud:4566',
  credentials: {
    accessKeyId: 'test',
    secretAccessKey: 'test',
  },
});

// Call an S3 API using the LocalStack endpoint
s3.send(new ListBucketsCommand({}))
  .then((data) => console.log(data))
  .catch((error) => console.error(error));
  

{{< /tab >}}
{{< /tabpane >}}

{{< callout >}}
In case of issues resolving S3 DNS record, we can fallback to `http://localhost:4566` in combination with the provider setting `forcePathStyle: true` (see the specific way of setting this parameter for each SDK above). The S3 service endpoint is slightly different from the other service endpoints, because AWS is deprecating path-style based access for hosting buckets. See [S3 documentation]({{< ref "user-guide/aws/s3" >}}) about endpoints.
{{< /callout >}}


## Resources

* [AWS SDK for JavaScript](https://aws.amazon.com/sdk-for-javascript/)
* [Official repository of the AWS SDK for JavaScript (v2)](https://github.com/aws/aws-sdk-js)
* [Official repository of the AWS SDK for JavaScript (v3)](https://github.com/aws/aws-sdk-js-v3)
