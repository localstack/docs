---
title: "Terraform"
linkTitle: "Terraform"
description: >
  Use the Terraform Infrastructure as Code framework with LocalStack
aliases:
  - /user-guide/integrations/cdk-for-terraform/
---

## Introduction

[Terraform](https://terraform.io/) is an Infrastructure-as-Code (IaC) framework developed by HashiCorp. It enables users to define and provision infrastructure using a high-level configuration language. Terraform uses HashiCorp Configuration Language (HCL) as its configuration syntax. HCL is a domain-specific language designed for writing configurations that define infrastructure elements and their relationships.

LocalStack supports Terraform via the [AWS provider](https://registry.terraform.io/providers/hashicorp/aws/latest/docs) through [custom service endpoints](https://registry.terraform.io/providers/hashicorp/aws/latest/docs/guides/custom-service-endpoints#localstack). You can configure Terraform to use LocalStack in two ways:

-   Using the [`tflocal` wrapper script](https://github.com/localstack/terraform-local) to automatically configure the service endpoints for you.
-   Manually configuring the service endpoints in your Terraform configuration with additional maintenance.

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

| Environment Variable     | Default value                    | Description |
| ------------------------ | -------------------------------- | ----------- |
| `TF_CMD`                 | `terraform`                        | Terraform command to call |
| `AWS_ENDPOINT_URL`       | -                                | Hostname and port of the target LocalStack instance |
| `LOCALSTACK_HOSTNAME`    | `localhost`                        | **(Deprecated)** Host name of the target LocalStack instance |
| `EDGE_PORT`              | `4566`                             | **(Deprecated)** Port number of the target LocalStack instance |
| `S3_HOSTNAME`            | `s3.localhost.localstack.cloud`    | Special hostname to be used to connect to LocalStack S3 |
| `USE_EXEC`               | -                                | Whether to use `os.exec` instead of `subprocess.Popen` (try using this in case of I/O issues) |
| `<SERVICE>_ENDPOINT`     | -                                | Setting a custom service endpoint, e.g., `COGNITO_IDP_ENDPOINT=http://example.com` |
| `AWS_DEFAULT_REGION`     | `us-east-1`                        | The AWS region to use (determined from local credentials if `boto3` is installed) |
| `CUSTOMIZE_ACCESS_KEY`   | -                                | Enables you to override the static AWS Access Key ID |
| `AWS_ACCESS_KEY_ID`      | `test` (`accountId`: 000000000000)   | AWS Access Key ID to use for multi-account setups |

{{< callout >}}
While using `CUSTOMIZE_ACCESS_KEY`, following cases are taking precedence over each other from top to bottom:
1.  If the `AWS_ACCESS_KEY_ID` environment variable is set.
2.  If `access_key` is configured in the Terraform AWS provider.
3.  If the `AWS_PROFILE` environment variable is set and properly configured.
4.  If the `AWS_DEFAULT_PROFILE` environment variable is set and configured.
5.  If credentials for the `default` profile are configured.
6.  If none of the above settings are present, it falls back to using the default `AWS_ACCESS_KEY_ID` mock value.
{{< /callout >}}

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

{{< callout >}}
If there are any difficulties resolving this DNS record, you can utilize `http://localhost:4566` as a fallback option in combination with setting `s3_use_path_style = true` in the provider. It's worth noting that the S3 service endpoint differs slightly from the other service endpoints due to AWS deprecating path-style based access for hosting buckets.
{{< /callout  >}}

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

{{< callout >}}
To heuristically detect whether your Terraform configuration should be deployed against LocalStack, you can use the following snippet:

```hcl
data "aws_caller_identity" "current" {}
output "is_localstack" {
  value = data.aws_caller_identity.current.id == "000000000000"
}
```

It will detect whether the AWS account ID is `000000000000`, which is the default value for LocalStack. If you use a different account ID within LocalStack, you can customize the snippet accordingly.
{{< /callout >}}

## CDK for Terraform

Cloud Development Kit for Terraform (CDKTF) allows you to use general-purpose programming languages, such as TypeScript, Python, Java, and more, to create infrastructure declaratively. It allows you to create, update, and delete AWS infrastructure by leveraging a Terraform backend without manually configuring Terraform using HCL and [AWS Cloud Development Kit](https://aws.amazon.com/cdk/) to translate your code into infrastructure configuration files for Terraform. CDKTF supports every Terraform provider and module available on the [Terraform Registry](https://registry.terraform.io/).

### Configuration

To configure your existing CDKTF configuration to work with LocalStack, manually configure the local service endpoints and credentials. It includes:

- General configuration to specify mock credentials for the AWS provider (`region`, `access_key`, `secret_key`).
- Request Management to avoid issues with routing and authentication, if needed.
- Service configuration to point the individual services to LocalStack.

Here is a configuration example to use with Python & TypeScript CDKTF configurations: 

{{< tabpane >}}
{{< tab header="localstack_config.py" lang="py" >}}
AWS_CONFIG = {
    "region": "us-east-1",
    "endpoints": [
        {
            "apigateway": "http://localhost:4566",
            "apigatewayv2": "http://localhost:4566",
            "cloudformation": "http://localhost:4566",
            "cloudwatch": "http://localhost:4566",
            "dynamodb": "http://localhost:4566",
            "ec2": "http://localhost:4566",
            "es": "http://localhost:4566",
            "elasticache": "http://localhost:4566",
            "firehose": "http://localhost:4566",
            "iam": "http://localhost:4566",
            "kinesis": "http://localhost:4566",
            "lambda": "http://localhost:4566",
            "rds": "http://localhost:4566",
            "redshift": "http://localhost:4566",
            "route53": "http://localhost:4566",
            "s3": "http://s3.localhost.localstack.cloud:4566",
            "secretsmanager": "http://localhost:4566",
            "ses": "http://localhost:4566",
            "sns": "http://localhost:4566",
            "sqs": "http://localhost:4566",
            "ssm": "http://localhost:4566",
            "stepfunctions": "http://localhost:4566",
            "sts": "http://localhost:4566",
        }
    ],
} 
{{< /tab >}}
{{< tab header="localstack-config.ts" lang="ts" >}}
export const AWS_CONFIG = {
  region: "us-east-1",
  endpoints: [
    {
      apigateway: "http://localhost:4566",
      apigatewayv2: "http://localhost:4566",
      cloudformation: "http://localhost:4566",
      cloudwatch: "http://localhost:4566",
      dynamodb: "http://localhost:4566",
      ec2: "http://localhost:4566",
      es: "http://localhost:4566",
      elasticache: "http://localhost:4566",
      firehose: "http://localhost:4566",
      iam: "http://localhost:4566",
      kinesis: "http://localhost:4566",
      lambda: "http://localhost:4566",
      rds: "http://localhost:4566",
      redshift: "http://localhost:4566",
      route53: "http://localhost:4566",
      s3: "http://s3.localhost.localstack.cloud:4566",
      secretsmanager: "http://localhost:4566",
      ses: "http://localhost:4566",
      sns: "http://localhost:4566",
      sqs: "http://localhost:4566",
      ssm: "http://localhost:4566",
      stepfunctions: "http://localhost:4566",
      sts: "http://localhost:4566",
    },
  ],
}; 
{{< /tab >}}
{{< /tabpane >}}

You can further import the above configuration in your project's code, and use it to configure the AWS provider:

{{< tabpane >}}
{{< tab header="main.py" lang="py" >}}
...
from localstack_config import AWS_CONFIG
...
AwsProvider(self, "Aws", **AWS_CONFIG)
...
{{< /tab >}}
{{< tab header="main.ts" lang="ts" >}}
...
import { AWS_CONFIG } from "./localstack-config";
...
new AwsProvider(this, "aws", AWS_CONFIG);
...
{{< /tab >}}
{{< /tabpane >}}

### Getting started

To get started with CDKTF on LocalStack, we will set up a simple stack to create some AWS resources. We will then deploy the stack to LocalStack, and verify that the resources have been created successfully. Before we start, make sure you have the following prerequisites:

* LocalStack
* [`cdktf`](https://www.npmjs.com/package/cdktf)

For Python:

* [`python`](https://www.python.org/downloads/)
* [`pipenv`](https://pipenv.pypa.io/en/latest/installation.html#installing-pipenv)

For TypeScript:

* [`tsc`](https://www.npmjs.com/package/typescript)

Create a new directory named `cdktf-localstack` and initialize a new CDKTF project using the following command:

{{< tabpane >}}
{{< tab header="Python" lang="py" >}}
$ cdktf init
...
? Do you want to continue with Terraform Cloud remote state management? No
? What template do you want to use? python

Initializing a project using the python template.
? Project Name sample-app
? Project Description A simple getting started project for cdktf.
? Do you want to start from an existing Terraform project? No
? Do you want to send crash reports to the CDKTF team? Refer to https://developer.hashicorp.com/terraform/cdktf/create-and-deploy/configuration-file#enable-crash-reporting-for-the-cli for more information no
Note: You can always add providers using 'cdktf provider add' later on
? What providers do you want to use? aws
...
{{< /tab >}}
{{< tab header="TypeScript" lang="ts" >}}
$ cdktf init
...
? Do you want to continue with Terraform Cloud remote state management? No
? What template do you want to use? typescript

Initializing a project using the typescript template.
? Project Name sample-app
? Project Description A simple getting started project for cdktf.
? Do you want to start from an existing Terraform project? No
? Do you want to send crash reports to the CDKTF team? Refer to https://developer.hashicorp.com/terraform/cdktf/create-and-deploy/configuration-file#enable-crash-reporting-for-the-cli for more information no
Note: You can always add providers using 'cdktf provider add' later on
? What providers do you want to use? aws
...
{{< /tab >}}
{{< /tabpane >}}

(Optional) If necessary, we can install the AWS provider separately for CDKTF, by running the following command:

{{< tabpane >}}
{{< tab header="Python" lang="py" >}}
 $ pipenv install cdktf-cdktf-provider-aws
{{< /tab >}}
{{< tab header="TypeScript" lang="ts" >}}
$ npm install @cdktf/provider-aws
{{< /tab >}}
{{< /tabpane >}}

Add the following code to import the AWS provider and create a new S3 bucket in the relevant file:

{{< tabpane >}}
{{< tab header="main.py" lang="py" >}}
#!/usr/bin/env python
from constructs import Construct
from cdktf import App, TerraformStack
from cdktf_cdktf_provider_aws.provider import AwsProvider
from cdktf_cdktf_provider_aws.s3_bucket import S3Bucket


class MyStack(TerraformStack):
    def __init__(self, scope: Construct, id: str):
        super().__init__(scope, id)

        AwsProvider(self, "aws",
            region="us-east-1",
            s3_use_path_style=True,
            endpoints=[
                {
                    "s3": "http://localhost:4566",
                    "sts": "http://localhost:4566",
                }
            ]
        )

        S3Bucket(self, "bucket")

app = App()
MyStack(app, "cdktf-example-python")

app.synth()
{{< /tab >}}
{{< tab header="main.ts" lang="ts" >}}
import { Construct } from "constructs";
import { App, TerraformStack } from "cdktf";
import { AwsProvider } from "@cdktf/provider-aws/lib/provider";
import {S3Bucket} from "@cdktf/provider-aws/lib/s3-bucket";

class MyStack extends TerraformStack {
  constructor(scope: Construct, id: string) {
    super(scope, id);

    new AwsProvider(this, "aws",{
      region: "us-east-1",
      s3UsePathStyle: true,
      endpoints: [
          {
            s3: "http://localhost:4566",
            sts: "http://localhost:4566"
          },
      ],
    });

    new S3Bucket(this, "bucket", {});
  }
}

const app = new App();
new MyStack(app, "example");
app.synth();
{{< /tab >}}
{{< /tabpane >}}

Run the following command to compile and deploy the CDKTF stack to LocalStack:

{{< command >}}
$ cdktf synth && cdktf deploy
{{< /command >}}

You should see the following output:

```sh
example  Initializing the backend...
example  
         Successfully configured the backend "local"! Terraform will automatically
         use this backend unless the backend configuration changes.
...
example  aws_s3_bucket.bucket (bucket): Creating...
example  aws_s3_bucket.bucket (bucket): Creation complete after 5s [id=terraform-20230418074657926600000001]
example  
         Apply complete! Resources: 1 added, 0 changed, 0 destroyed.
```

Verify that the S3 bucket has been created successfully by running the following command:

{{< command >}}
$ awslocal s3 ls
{{< /command >}}

Your CDKTF stack is now successfully deployed to LocalStack. You can now start using CDKTF to create and manage your AWS resources on LocalStack.

## OpenTofu

OpenTofu is an open-source fork of Terraform acting as a drop-in replacement for Terraform, as it's compatible with Terraform versions 1.5.x and most of 1.6.x. You can use OpenTofu with LocalStack to create and manage your AWS resources with your pre-existing Terraform configurations. You can use the `TF_CMD` environment variable with `tflocal` to specify the `tofu` binary to call, or setup a manual configuration to point the individual services to LocalStack.

{{< command >}}
$ TF_CMD=tofu tflocal --help
<disable-copy>
Usage: tofu [global options] <subcommand> [args]

The available commands for execution are listed below.
The primary workflow commands are given first, followed by
less common or more advanced commands.
...
</disable-copy>
{{< /command >}}

## Terragrunt

Terragrunt is an open-source wrapper for Terraform that provides extra tools for keeping your configurations DRY, working with multiple Terraform modules, and managing remote state. You can use Terragrunt with LocalStack to create and manage your AWS resources with your pre-existing Terraform configurations.

### Configuration

A sample `terragrunt.hcl` configuration file to use with LocalStack is shown below:

```hcl
generate "provider" {
  path = "provider.tf"
  if_exists = "overwrite_terragrunt"
  contents = <<EOF
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
    dynamodb       = "http://localhost:4566"
    iam            = "http://localhost:4566"
    kinesis        = "http://localhost:4566"
    lambda         = "http://localhost:4566"
    s3             = "http://s3.localhost.localstack.cloud:4566"
    ses            = "http://localhost:4566"
    sns            = "http://localhost:4566"
    sqs            = "http://localhost:4566"
    sts            = "http://localhost:4566"
  }
}
EOF
}
```

You can add more service endpoints to the above configuration as needed, and point them to LocalStack (`http://localhost:4566`).

## Examples

- [Serverless Container-based APIs with Amazon ECS & API Gateway](https://github.com/localstack/serverless-api-ecs-apigateway-sample)
- [Full-Stack application with AWS Lambda, DynamoDB & S3 for shipment validation](https://github.com/localstack/shipment-list-demo)
- [Search application with Lambda, Kinesis, Firehose, ElasticSearch, S3](https://github.com/localstack/sample-fuzzy-movie-search-lambda-kinesis-elasticsearch)
- [LocalStack Terraform Samples](https://github.com/localstack/localstack-terraform-samples)
