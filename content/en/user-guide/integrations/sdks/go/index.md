---
title: "Go"
categories: []
description: >
  How to use the Go AWS SDK with LocalStack.
aliases:
  - /integrations/sdks/go/
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

{{< tabpane lang="golang" >}}
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
  awsEndpoint := "http://localhost:4566"
  awsRegion := "us-east-1"
  
  awsCfg, err := config.LoadDefaultConfig(context.TODO(),
    config.WithRegion(awsRegion),
  )
  if err != nil {
    log.Fatalf("Cannot load the AWS configs: %s", err)
  }

  // Create the resource client
  client := s3.NewFromConfig(awsCfg, func(o *s3.Options) {
    o.UsePathStyle = true
    o.BaseEndpoint = aws.String(awsEndpoint)
  })
  // ...
}{{< /tab >}}

{{< tab header="aws-go-sdk-v2 Credential Provider" lang="golang" >}}
package main

import (
	"context"
	"github.com/aws/aws-sdk-go-v2/aws"
	"github.com/aws/aws-sdk-go-v2/config"
)

const (
	AwsLocalEndpoint        = "http://localhost:4566"
	AwsLocalCredentialsName = "AwsLocalCredentials"
	AwsLocalDefaultRegion   = "us-east-1"
	AwsLocalAccountId       = "000000000000"
	AwsLocalAccessKey       = "test"         
	AwsLocalSecret          = "test"         
)

var (
	ErrorAwsLocalCredentialsEmpty = "awslocal credentials are empty"
)

// NewAwsLocalConfig returns a new [aws.Config] object configured to connect to LocalStack.
func NewAwsLocalConfig(ctx context.Context, accountId, endpoint, region, key, secret string, optFns ...func(*config.LoadOptions) error) aws.Config {
	opts := []func(*config.LoadOptions) error{
		config.WithRegion(region),
		config.WithCredentialsProvider(NewAwsLocalCredentialsProvider(key, secret, accountId)),
	}
	opts = append(opts, optFns...)

	cfg, err := config.LoadDefaultConfig(ctx, opts...)
	if err != nil {
		panic(err)
	}

	cfg.BaseEndpoint = aws.String(endpoint)
	return cfg
}

// NewDefaultAwsLocalConfig returns a new default [aws.Config] object configured to connect to the default LocalStack.
func NewDefaultAwsLocalConfig() aws.Config {
	cfg, err := config.LoadDefaultConfig(context.TODO(),
		config.WithRegion(AwsLocalDefaultRegion),
		config.WithCredentialsProvider(NewDefaultAwsLocalCredentialsProvider()))
	if err != nil {
		panic(err)
	}
	cfg.BaseEndpoint = aws.String(AwsLocalEndpoint)
	return cfg
}

// to ensure AwsLocalCredentialsProvider implements the [aws.CredentialsProvider] interface
var _ aws.CredentialsProvider = (*AwsLocalCredentialsProvider)(nil)

// A AwsLocalCredentialsProvider is a static credentials provider that returns the same credentials,
// designed for use with LocalStack
type AwsLocalCredentialsProvider struct {
	Value aws.Credentials
}

// NewDefaultAwsLocalCredentialsProvider returns an AwsLocalCredentialsProvider
// initialized with the default AwsLocal credentials.
func NewDefaultAwsLocalCredentialsProvider() AwsLocalCredentialsProvider {
	return NewAwsLocalCredentialsProvider(AwsLocalAccessKey, AwsLocalSecret, AwsLocalAccountId)
}

// NewAwsLocalCredentialsProvider return a StaticCredentialsProvider initialized with the AWS credentials passed in.
func NewAwsLocalCredentialsProvider(key, secret, accountId string) AwsLocalCredentialsProvider {
	return AwsLocalCredentialsProvider{
		Value: aws.Credentials{
			AccessKeyID:     key,
			SecretAccessKey: secret,
			AccountID:       accountId,
			SessionToken:    "",
			CanExpire:       false,
		},
	}
}

// Retrieve returns the credentials or error if the credentials are invalid.
func (s AwsLocalCredentialsProvider) Retrieve(_ context.Context) (aws.Credentials, error) {
	v := s.Value
	if v.AccessKeyID == "" || v.SecretAccessKey == "" {
		return aws.Credentials{
			Source: AwsLocalCredentialsName,
		}, &AwsLocalCredentialsEmptyError{}
	}

	if len(v.Source) == 0 {
		v.Source = AwsLocalCredentialsName
	}

	return v, nil
}

func (s AwsLocalCredentialsProvider) IsExpired() bool {
	return false
}

// AwsLocalCredentialsEmptyError is emitted when the AwsLocal credentials are empty.
type AwsLocalCredentialsEmptyError struct{}

func (*AwsLocalCredentialsEmptyError) Error() string {
	return ErrorAwsLocalCredentialsEmpty
}

func main() {
	// build an aws.Credential-compliant configuration
	awsCfg := NewDefaultAwsLocalConfig()

  // ...
}
{{< /tab >}}
{{< /tabpane >}}

## Resources

* [localstack-aws-sdk-examples for Go](https://github.com/localstack/localstack-aws-sdk-examples/tree/main/go)
* [AWS SDK for Go](https://aws.amazon.com/sdk-for-go/)
* [Official repository of the AWS SDK for Go (v1)](https://github.com/aws/aws-sdk-go)
* [Official repository of the AWS SDK for Go (v2)](https://github.com/aws/aws-sdk-go-v2)
