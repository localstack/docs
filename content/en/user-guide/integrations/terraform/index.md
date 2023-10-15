---
title: "Terraform"
weight: 5
description: >
  Use the Terraform Infrastructure as Code framework with LocalStack
---

## Introduction

[Terraform](https://terraform.io/) is an infrastructure as code (IaC) framework developed by HashiCorp. It enables users to define and provision infrastructure using a high-level configuration language. Terraform uses HashiCorp Configuration Language (HCL) as its configuration syntax. HCL is a domain-specific language designed for writing configurations that define infrastructure elements and their relationships.

LocalStack supports Terraform via the [AWS provider](https://registry.terraform.io/providers/hashicorp/aws/latest/docs) through [custom service endpoints](https://registry.terraform.io/providers/hashicorp/aws/latest/docs/guides/custom-service-endpoints#localstack). You can configure Terraform to use LocalStack in two ways:

-   Using the [`tflocal` wrapper script](https://github.com/localstack/terraform-local) to automatically configure the service endpoints for you.
-   Manually configure the service endpoints in your Terraform configuration with additional maintenance.

In this guide, we will demonstrate how you can create local AWS resources using Terraform and LocalStack, by using the `tflocal` wrapper script and a manual configuration example.

## `tflocal` wrapper script

`tflocal` is a small wrapper script to run Terraform against LocalStack. `tflocal` script uses the [Terraform Override mechanism](https://www.terraform.io/language/files/override) and creates a temporary file `localstack_providers_override.tf` to configure the endpoints for the AWS `provider` section. The endpoints for all services are configured to point to the LocalStack API (`http://localhost:4566` by default). It allows you to easily deploy your unmodified Terraform scripts against LocalStack.

### Create a Terraform configuration

Create a new file named `main.tf` and add a minimal S3 bucket configuration to it. The following contents should be added in the `main.tf` file:

```hcl
resource "aws_s3_bucket" "test-bucket" {
  bucket = "my-bucket"
}
```

### Install the `tflocal` wrapper script

To install the `tflocal` command, you can use `pip` (assuming you have a local Python installation):

{{< command >}}
$ pip install terraform-local
{{< / command >}}

After installation, you can use the `tflocal` command, which has the same interface as the `terraform` command line.

{{< command >}}
$ tflocal --help
<disable-copy>
Usage: terraform [global options] <subcommand> [args]
...
<disable-copy>
{{< / command >}}

### Deploy the Terraform configuration

Start your LocalStack container using your preferred method. Initialize Terraform using the following command:

{{< command >}}
$ tflocal init
{{< / command >}}

You can now provision the S3 bucket specified in the configuration:

{{< command >}}
$ tflocal apply
{{< / command >}}

### Configuration

| Environment Variable     | Description |
|--------------------------|-------------|
| `TF_CMD`                 | Terraform command to call (default: `terraform`) |
| `LOCALSTACK_HOSTNAME`    | Host name of the target LocalStack instance |
| `EDGE_PORT`              | Port number of the target LocalStack instance |
| `S3_HOSTNAME`            | Special hostname to be used to connect to LocalStack S3 (default: `s3.localhost.localstack.cloud`) |
| `USE_EXEC`               | Whether to use `os.exec` instead of `subprocess.Popen` (try using this in case of I/O issues) |
| `<SERVICE>_ENDPOINT`     | Setting a custom service endpoint, e.g., `COGNITO_IDP_ENDPOINT=http://example.com` |
| `AWS_DEFAULT_REGION`     | The AWS region to use (default: `us-east-1`, or determined from local credentials if `boto3` is installed) |
| `CUSTOMIZE_ACCESS_KEY`   | Enables you to override the static AWS Access Key ID. |
| `AWS_ACCESS_KEY_ID`      | AWS Access Key ID to use for multi-account setups (default: `test` -> account ID: `000000000000`) |

{{< alert title="Note" >}}
While using `CUSTOMIZE_ACCESS_KEY`, following cases are taking precedence over each other from top to bottom:
1.  If the `AWS_ACCESS_KEY_ID` environment variable is set.
2.  If `access_key` is configured in the Terraform AWS provider.
3.  If the `AWS_PROFILE` environment variable is set and properly configured.
4.  If the `AWS_DEFAULT_PROFILE` environment variable is set and configured.
5.  If credentials for the `default` profile are configured.
6.  If none of the above settings are present, it falls back to using the default `AWS_ACCESS_KEY_ID` mock value.
{{< /alert >}}

## Manual Configuration

Instead of using the `tflocal` script, you have the option to manually configure the local service endpoints and credentials. The following sections will provide detailed steps for this manual configuration.

### General Configuration

To begin, you need to define mock credentials for the AWS provider. Specify the following in your `main.tf` file:

```hcl
provider "aws" {

  access_key = "test"
  secret_key = "test"
  region     = "us-east-1"
}
```

### Request Management

Next, to prevent routing and authentication issues (which are unnecessary in this context), you should provide some general parameters:

```hcl
provider "aws" {

  access_key                  = "test"
  secret_key                  = "test"
  region                      = "us-east-1"


  # only required for non virtual hosted-style endpoint use case.
  # https://registry.terraform.io/providers/hashicorp/aws/latest/docs#s3_use_path_style
  s3_use_path_style           = true
  skip_credentials_validation = true
  skip_metadata_api_check     = true
  skip_requesting_account_id  = true
}
```

### Services

Furthermore, it's necessary to configure the individual services to use LocalStack. For S3, this configuration resembles the following snippet, where we've chosen to use the virtual hosted-style endpoint:

```hcl
  endpoints {
    s3             = "http://s3.localhost.localstack.cloud:4566"
  }
```

{{< alert title="Note">}}
If there are any difficulties resolving this DNS record, you can utilize `http://localhost:4566` as a fallback option in combination with setting `s3_use_path_style = true` in the provider. It's worth noting that the S3 service endpoint differs slightly from the other service endpoints due to AWS deprecating path-style based access for hosting buckets.
{{< /alert >}}

### Final Configuration

The final minimal configuration for deploying an S3 bucket via a `main.tf` file should resemble the following:

```hcl
provider "aws" {

  access_key                  = "mock_access_key"
  secret_key                  = "mock_secret_key"
  region                      = "us-east-1"

  s3_use_path_style           = true
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

Here's a configuration example with additional service endpoints. Please note that these provider configurations may not be necessary if you use the `tflocal` script (as described above). You can save the following configuration in a file named `provider.tf` and include it in your Terraform configuration.

```hcl
provider "aws" {
  access_key                  = "test"
  secret_key                  = "test"
  region                      = "us-east-1"
  s3_use_path_style           = false
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

## Examples

- [Serverless Container-based APIs with Amazon ECS & API Gateway](https://github.com/localstack/serverless-api-ecs-apigateway-sample)
- [Full-Stack application with AWS Lambda, DynamoDB & S3 for shipment validation](https://github.com/localstack/shipment-list-demo)
- [Search application with Lambda, Kinesis, Firehose, ElasticSearch, S3](https://github.com/localstack/sample-fuzzy-movie-search-lambda-kinesis-elasticsearch)
- [LocalStack Terraform Samples](https://github.com/localstack/localstack-terraform-samples)
