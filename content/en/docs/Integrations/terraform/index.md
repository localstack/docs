---
title: "Terraform"
tags: ["terraform", "infrastructure-as-code"]
weight: 5
description: >
  Use the Terraform Infrastructure as Code framework with LocalStack
---

![Terraform logo](logo-terraform-main.svg)

## Overview
Terraform allows you to automate the management of AWS resources such as containers, lambda functions and so on by declaring them in the HashiCorp Configuration Language (HCL). On this page we are going to discuss how Terraform and LocalStack can be used together. If you are adapting an existing configuration, you might be able to skip certain steps at your own discretion.

## Quickstart
Using Terraform alongside LocalStack does not require a lot of configuration. Apart from some information Terraform expects there are basically only 2 things to take care of inside the AWS provider.

Before we start changing the configuration, create and change into a new directory for this sample
```
mkdir terraform_quickstart && cd terraform_quickstart
```
Inside this directory create a file called ```main.tf```. The following changes go into this file.

### General Configuration
First, we have to supply Terraform with some mock data for access and region, as these items are expected
```
provider "aws" {
  
  access_key                  = "mock_access_key"
  secret_key                  = "mock_secret_key"  
  region                      = "us-east-1"
}

```

### Request Management
Second, we need to avoid issues with routing and authentication (as we do not need it). Therefore we need to supply some general parameters

```
provider "aws" {
  
  access_key                  = "mock_access_key"
  secret_key                  = "mock_secret_key"  
  region                      = "us-east-1"
  
  s3_force_path_style         = true
  skip_credentials_validation = true
  skip_metadata_api_check     = true
  skip_requesting_account_id  = true
}
```

### Services
Third, we have to point the individual services to LocalStack. In case of S3, this looks like the following snippet

```
endpoints {
    s3             = "http://localhost:4566"
  }
```

Note that the localhost address is the same for all services.

### S3 Bucket
Now we are adding a minimal s3 bucket outside the provider
```
resource "aws_s3_bucket" "test-bucket" {
  bucket = "my-bucket"
}

```

### Final Configuration
The final (minimal) configuration to deploy an s3 bucket thus looks like this
```
provider "aws" {
  
  access_key                  = "mock_access_key"
  secret_key                  = "mock_secret_key"  
  region                      = "us-east-1"
  
  s3_force_path_style         = true
  skip_credentials_validation = true
  skip_metadata_api_check     = true
  skip_requesting_account_id  = true
  

  endpoints {
    s3             = "http://localhost:4566"
  }
}

resource "aws_s3_bucket" "test-bucket" {
  bucket = "my-bucket"
}
```
After starting LocalStack you can now deploy the s3 bucket via ```terraform```, and interact with the (still empty) s3 container via ```awslocal```!
All you need to do is to initialize Terraform
```
terraform init
```
and then deploy the bucket
```
terraform deploy
```


For a more detailled example, you can take a look at our [terraform sample]() in our repository.