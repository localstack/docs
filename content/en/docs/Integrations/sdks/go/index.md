---
title: "Go"
categories: []
tags: ["sdk"]
description: >
  How to use the Go AWS SDK with LocalStack.
---

## Overview

The [AWS SDK for Go](https://aws.amazon.com/sdk-for-go/), like other AWS SDKs, lets you set the endpoint when creating resource clients,
which is the preferred way of integrating the Go SDK with LocalStack.

The Go SDK has two major versions, each with their own way of specifying the LocalStack endpoint:

* [aws-sdk-go](https://github.com/aws/aws-sdk-go)
* [aws-sdk-go-v2](https://github.com/aws/aws-sdk-go-v2)

## Examples

Here is an example of how to create an S3 Client from a Session with the endpoint set to LocalStack.
Full examples for both SDK versions can be found [in our samples repository](https://github.com/localstack/localstack-aws-sdk-examples/tree/main/go).

{{< tabpane >}}
{{< tab header="aws-go-sdk" lang="golang" >}}
package main

import (
    "github.com/aws/aws-sdk-go/aws"
    "github.com/aws/aws-sdk-go/aws/session"
    "github.com/aws/aws-sdk-go/service/s3"
    "github.com/aws/aws-sdk-go/aws/credentials"
)

func main() {
  // Initialize a session
  sess, _ := session.NewSession(&aws.Config{
    Region:           aws.String("us-east-1"),
    Credentials:      credentials.NewStaticCredentials("test", "test", ""),
    S3ForcePathStyle: aws.Bool(true),
    Endpoint:         aws.String("http://localhost:4566"),
  })

  // Create S3 service client
  client := s3.New(sess)

  // ...
}{{< /tab >}}

{{< tab header="aws-go-sdk-v2" lang="golang" >}}
package main

import (
  "context"
  "log"

  "github.com/aws/aws-sdk-go-v2/aws"
  "github.com/aws/aws-sdk-go-v2/config"
  "github.com/aws/aws-sdk-go-v2/service/s3"
)

func main() {
  awsEndpoint = "http://localhost:4566"
  awsRegion = "us-east-1"

  customResolver := aws.EndpointResolverFunc(func(service, region string) (aws.Endpoint, error) {
    if awsEndpoint != "" {
      return aws.Endpoint{
        PartitionID:   "aws",
        URL:           awsEndpoint,
        SigningRegion: awsRegion,
      }, nil
    }

    // returning EndpointNotFoundError will allow the service to fallback to its default resolution
    return aws.Endpoint{}, &aws.EndpointNotFoundError{}
  })

  awsCfg, err := config.LoadDefaultConfig(context.TODO(),
    config.WithRegion(awsRegion),
    config.WithEndpointResolver(customResolver),
  )
  if err != nil {
    log.Fatalf("Cannot load the AWS configs: %s", err)
  }

  // Create the resource client
  client = s3.NewFromConfig(awsCfg, func(o *s3.Options) {
    o.UsePathStyle = true
  })
  // ...
}{{< /tab >}}
{{< /tabpane >}}



## Resources

* [localstack-aws-sdk-examples for Go](https://github.com/localstack/localstack-aws-sdk-examples/tree/main/go)
* [AWS SDK for Go](https://aws.amazon.com/sdk-for-go/)
* [Official repository of the AWS SDK for Go (v1)](https://github.com/aws/aws-sdk-go)
* [Official repository of the AWS SDK for Go (v2)](https://github.com/aws/aws-sdk-go-v2)
