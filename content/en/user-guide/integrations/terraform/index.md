---
title: "Terraform"
tags: ["terraform", "infrastructure-as-code"]
weight: 5
description: >
  Use the Terraform Infrastructure as Code framework with LocalStack
aliases:
  - /integrations/terraform/
---

<img src="logo-terraform-main.svg" width="600px" alt="terraform logo">

## Overview

Terraform allows you to automate the management of AWS resources such as containers, lambda functions and so on by declaring them in the HashiCorp Configuration Language (HCL).
On this page we discuss how Terraform and LocalStack can be used together.
If you are adapting an existing configuration, you might be able to skip certain steps at your own discretion.

## Example

If you have not done so yet, [install Terraform](https://learn.hashicorp.com/tutorials/terraform/install-cli?in=terraform/aws-get-started).

Using Terraform with LocalStack requires little extra configuration.
Apart from some information Terraform expects there are basically only two things to take care of in the configuration.

Before we start changing the configuration, create and change into a new directory for this sample

{{< command >}}
$ mkdir terraform_quickstart && cd terraform_quickstart
{{< / command >}}

Inside this directory, create a file called `main.tf`. The following changes go into this file.

Now we are adding a minimal S3 bucket configuration to the `main.tf` file:
```hcl
resource "aws_s3_bucket" "test-bucket" {
  bucket = "my-bucket"
}

```

## Using the `tflocal` script

We provide `tflocal`, a thin wrapper script around the `terraform` command line client. `tflocal` takes care of automatically configuring the local service endpoints, which allows you to easily deploy your unmodified Terraform scripts against LocalStack.

You can install the `tflocal` command via `pip` (requires a local Python installation):
{{< command >}}
$ pip install terraform-local
{{< / command >}}

Once installed, the `tflocal` command should be available, with the same interface as the `terraform` command line:
{{< command >}}
$ tflocal --help
Usage: terraform [global options] <subcommand> [args]
...
{{< / command >}}

{{< alert >}}
**Note**: Alternatively, you can also manually configure the local endpoints in the `provider` section of your Terraform script - see further below.
{{< /alert >}}

### Deployment

After starting LocalStack you can now deploy the S3 bucket via `tflocal` and interact with the (still empty) S3 bucket via `awslocal`!

All you need to do is to initialize Terraform:

{{< command >}}
$ tflocal init
{{< / command >}}

... and then provision s3 bucket specified in the configuration:
{{< command >}}
$ tflocal apply
{{< / command >}}

## Manual Configuration

As an alternative to using the `tflocal` script, you may also manually configure the local service endpoints and credentials. We'll walk through the detailed steps in the following sections.

### General Configuration

First, we have to specify mock credentials for the AWS provider:

```hcl
provider "aws" {

  access_key = "test"
  secret_key = "test"
  region     = "us-east-1"
}
```

### Request Management

Second, we need to avoid issues with routing and authentication (as we do not need it).
Therefore we need to supply some general parameters:

```hcl
provider "aws" {

  access_key                  = "test"
  secret_key                  = "test"
  region                      = "us-east-1"


  # only required for non virtual hosted-style endpoint use case.
  # https://registry.terraform.io/providers/hashicorp/aws/latest/docs#s3_force_path_style
  s3_force_path_style         = true
  skip_credentials_validation = true
  skip_metadata_api_check     = true
  skip_requesting_account_id  = true
}
```

### Services

Additionally, we have to point the individual services to LocalStack.
In case of S3, this looks like the following snippet, in this case we opted to use the virtual hosted-style endpoint.

```hcl
  endpoints {
    s3             = "http://s3.localhost.localstack.cloud:4566"
  }
```

{{< alert >}}
**Note**: In case of issues resolving this DNS record, we can fallback to `http://localhost:4566` in combination with the provider setting `s3_force_path_style = true`. The S3 service endpoint is slightly
different from the other service endpoints, because AWS is deprecating path-style based access for hosting buckets.
{{< /alert >}}

### Final Configuration

The final (minimal) configuration to deploy an S3 bucket thus looks like this
```hcl
provider "aws" {

  access_key                  = "mock_access_key"
  secret_key                  = "mock_secret_key"
  region                      = "us-east-1"

  s3_force_path_style         = true
  skip_credentials_validation = true
  skip_metadata_api_check     = true
  skip_requesting_account_id  = true

  endpoints {
    s3             = "http://s3.localhost.localstack.cloud:4566"
  }
}

resource "aws_s3_bucket" "test-bucket" {
  bucket = "my-bucket"
}
```

### Endpoint Configuration

Below is a configuration example with additional service endpoints. 
Again, these provider configurations should no longer be required if you use the `tflocal` script (see above).

```hcl
provider "aws" {
  access_key                  = "test"
  secret_key                  = "test"
  region                      = "us-east-1"
  s3_force_path_style         = false
  skip_credentials_validation = true
  skip_metadata_api_check     = true
  skip_requesting_account_id  = true

  endpoints {
    apigateway     = "http://localhost:4566"
    apigatewayv2   = "http://localhost:4566"
    cloudformation = "http://localhost:4566"
    cloudwatch     = "http://localhost:4566"
    dynamodb       = "http://localhost:4566"
    ec2            = "http://localhost:4566"
    es             = "http://localhost:4566"
    elasticache    = "http://localhost:4566"
    firehose       = "http://localhost:4566"
    iam            = "http://localhost:4566"
    kinesis        = "http://localhost:4566"
    lambda         = "http://localhost:4566"
    rds            = "http://localhost:4566"
    redshift       = "http://localhost:4566"
    route53        = "http://localhost:4566"
    s3             = "http://s3.localhost.localstack.cloud:4566"
    secretsmanager = "http://localhost:4566"
    ses            = "http://localhost:4566"
    sns            = "http://localhost:4566"
    sqs            = "http://localhost:4566"
    ssm            = "http://localhost:4566"
    stepfunctions  = "http://localhost:4566"
    sts            = "http://localhost:4566"
  }
}
```

## Further Reading

For more examples, you can take a look at our [Terraform sample](https://github.com/localstack/localstack-pro-samples/tree/master/terraform-resources) or the [Terraform LocalStack section](https://registry.terraform.io/providers/hashicorp/aws/latest/docs/guides/custom-service-endpoints#localstack).

### Community Resources

* [LocalStack with Terraform and Docker for running AWS locally. 2021-07-04](https://dev.to/mrwormhole/localstack-with-terraform-and-docker-for-running-aws-locally-3a6d)
