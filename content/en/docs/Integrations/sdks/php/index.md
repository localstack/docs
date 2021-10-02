---
title: "PHP"
categories: []
tags: ["sdk"]
description: >
  How to use the PHP AWS SDK with LocalStack.
---

## Overview

The [AWS SDK for PHP](https://aws.amazon.com/sdk-for-php/), like other AWS SDKs, let you set the endpoint when creating resource clients,
which is the preferred way of integrating the PHP SDK with LocalStack.

## Example

Here is an example of how to create an `S3Client` with the endpoint set to LocalStack.

```php
use Aws\S3\S3Client;
use Aws\Exception\AwsException;

// Configuring S3 Client
$s3 = new Aws\S3\S3Client([
    'version' => '2006-03-01',
    'region' => 'us-east-1',
    // Enable 'use_path_style_endpoint' => true, if bucket name is non dns complient
    'use_path_style_endpoint' => true,
    'endpoint' => 'http://s3.localhost.localstack.cloud:4566',
]);
```

A full example can be found [in our samples repository](https://github.com/localstack/localstack-aws-sdk-examples/tree/main/php).


## Resources

* [localstack-aws-sdk-examples for PHP](https://github.com/localstack/localstack-aws-sdk-examples/tree/main/php)
* [AWS SDK for PHP](https://aws.amazon.com/sdk-for-php/)
* [Official repository of the AWS SDK for PHP](https://github.com/aws/aws-sdk-php)
