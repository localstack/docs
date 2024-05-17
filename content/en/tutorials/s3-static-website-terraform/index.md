---
title: "Host a static website locally using Simple Storage Service (S3) and Terraform with LocalStack"
linkTitle: "Host a static website locally using Simple Storage Service (S3) and Terraform with LocalStack"
weight: 4
description: >
  Host a static website using a Simple Storage Service (S3) bucket to serve static content by provisioning the infrastructure using Terraform in LocalStack. Learn how to configure S3 buckets locally for testing and integration, and make use of LocalStack's S3 API & `tflocal` CLI to provision infrastructure locally.
type: tutorials
teaser: ""
services:
- s3
platform:
- html
deployment:
- terraform
tags:
- S3
- Terraform
- S3-Website
- Static-Website
- tflocal CLI
pro: false
leadimage: "s3-static-website-terraform-featured-image.png"
---

[AWS Simple Storage Service (S3)](https://aws.amazon.com/s3/) is a proprietary object storage solution that can store an unlimited number of objects for many use cases. S3 is a highly scalable, durable and reliable service that we can use for various use cases: hosting a static site, handling big data analytics, managing application logs, storing web assets and much more!

With S3, you have unlimited storage with your data stored in buckets. A bucket refers to a directory, while an object is just another term for a file. Every object (file) stores the name of the file (key), the contents (value), a version ID and the associated metadata. You can also use S3 to host a static website, to serve static content. It might include HTML, CSS, JavaScript, images, and other assets that make up your website.

LocalStack supports the S3 API, which means you can use the same API calls to interact with S3 in LocalStack as you would with AWS. Using LocalStack, you can create and manage S3 buckets and objects locally, use AWS SDKs and third-party integrations to work with S3, and test your applications without making any significant alterations. LocalStack also supports the creation of S3 buckets with static website hosting enabled.

In this tutorial, we will deploy a static website using an S3 bucket over a locally emulated AWS infrastructure on LocalStack. We will use Terraform to automate the creation & management of AWS resources by declaring them in the HashiCorp Configuration Language (HCL). We will also learn about `tflocal`, a CLI wrapper created by LocalStack, that allows you to run Terraform locally against LocalStack.

## Prerequisites

For this tutorial, you will need:

- [LocalStack Community](https://github.com/localstack/localstack)
- [Terraform](https://www.terraform.io/downloads.html)
- [awslocal](https://github.com/localstack/awscli-local)

## Creating a static website

We will create a simple static website using plain HTML to get started. To create a static website deployed over S3, we need to create an index document and a custom error document. We will name our index document `index.html` and our error document `error.html`. Optionally, you can create a folder called `assets` to store images and other assets.

Let's create a directory named `s3-static-website-localstack` where we'll store our static website files. If you don't have an `index.html` file, you can use the following code to create one:

```html
<!DOCTYPE html>
<html lang="en">
  <head>
    <meta http-equiv="Content-Type" content="text/html" />
    <meta  charset="utf-8"  />
    <title>Static Website</title>
  </head>
  <body>
    <p>Static Website deployed locally over S3 using LocalStack</p>
  </body>
</html>
```

S3 will serve this file when a user visits the root URL of your static website, serving as the default page. In a similar fashion, you can configure a custom error document that contains a user-friendly error message. Let's create a file named `error.html` and add the following code:

```html
<!DOCTYPE html>
<html lang="en">
  <head>
    <meta charset="utf-8">
    <title>404</title>
  </head>
  <body>
    <p>Something is amiss.</p>
  </body>
</html>
```

S3 will return the above file content only for HTTP 4XX error codes. Some browsers might choose to display their custom error message if a user tries to access a resource that does not exist. In this case, browsers might ignore the above error document. With the initial setup complete, we can now move on to creating a static website using S3 via `awslocal`, LocalStack's wrapper for the AWS CLI.

## Hosting a static website using S3

To create a static website using S3, we need to create a bucket, enable static website hosting, and upload the files to the bucket. We will use the `awslocal` CLI for these operations. Navigate to the root directory of the project and create a bucket named `testwebsite` using LocalStack's S3 API:

{{< command >}}
$ awslocal s3api create-bucket --bucket testwebsite
{{< / command >}}

With the bucket created, we can now attach a policy to it to allow public access and its contents. Let's create a file named `bucket_policy.json` in the root directory and add the following code:

```json
{
    "Version": "2012-10-17",
    "Statement": [
        {
            "Sid": "PublicReadGetObject",
            "Effect": "Allow",
            "Principal": "*",
            "Action": "s3:GetObject",
            "Resource": "arn:aws:s3:::testwebsite/*"
        }
    ]
}
```

Let's now attach the policy to the bucket:

{{< command >}}
$ awslocal s3api put-bucket-policy --bucket testwebsite --policy file://bucket_policy.json
{{< / command >}}

With the policy attached, we can now sync the contents of our root directory to the bucket:

{{< command >}}
$ awslocal s3 sync ./ s3://testwebsite
{{< / command >}}

We'll now enable static website hosting on the bucket and configure the index and error documents:

{{< command >}}
$ awslocal s3 website s3://testwebsite/ --index-document index.html --error-document error.html
{{< / command >}}

If you are deploying a static website using S3 on real AWS cloud, your S3 website endpoint will follow one of these two formats:

- `http://<BUCKET_NAME>.s3-website-<REGION>.amazonaws.com`
- `http://<BUCKET_NAME>.s3-website.<REGION>.amazonaws.com`

In LocalStack, the S3 website endpoint follows the following format: `http://<BUCKET_NAME>.s3-website.localhost.localstack.cloud:4566`. You can navigate to [`http://testwebsite.s3-website.localhost.localstack.cloud:4566/`](http://testwebsite.s3-website.localhost.localstack.cloud:4566/) to view your static website.

## Orchestrating infrastructure using Terraform

You can automate the above process by orchestrating your AWS infrastructure using Terraform. Terraform is an infrastructure as code (IaC) tool that allows you to create, manage, and version your infrastructure. Terraform uses a declarative configuration language called HashiCorp Configuration Language (HCL) to describe your infrastructure.

Before that, we would need to manually configure the local service endpoints and credentials for Terraform to integrate with LocalStack. We will use the [AWS Provider for Terraform](https://registry.terraform.io/providers/hashicorp/aws/latest/docs) to interact with the many resources supported by AWS in LocalStack. Create a new file named `provider.tf` and specify mock credentials for the AWS provider:

```hcl
provider "aws" {
  region                      = "us-east-1"
  access_key                  = "fake"
  secret_key                  = "fake"
}
```

We would also need to avoid issues with routing and authentication (as we do not need it). Therefore we need to supply some general parameters. Additionally, we have to point the individual services to LocalStack. We can do this by specifying the `endpoints` parameter for each service, that we intend to use. Our `provider.tf` file should look like this:

```hcl
provider "aws" {
  access_key                  = "test"
  secret_key                  = "test"
  region                      = "us-east-1"

  # only required for non virtual hosted-style endpoint use case.
  # https://registry.terraform.io/providers/hashicorp/aws/latest/docs#s3_force_path_style
  s3_use_path_style           = false
  skip_credentials_validation = true
  skip_metadata_api_check     = true
  skip_requesting_account_id  = true

  endpoints {
    s3             = "http://s3.localhost.localstack.cloud:4566"
  }
}
```

{{< callout "note" >}}
We use `localhost.localstack.cloud` as the recommended endpoint for the S3 to enable host-based bucket endpoints. Users can rely on the `localhost.localstack.cloud` domain to be publicly resolvable. We also publish an SSL certificate which is automatically used inside LocalStack to enable HTTPS endpoints with valid certificates. For most of the other services, it is fine to use `localhost:4566`.
{{< /callout >}}

With the provider configured, we can now configure the variables for our S3 bucket. Create a new file named `variables.tf` and add the following code:

```hcl
variable "bucket_name" {
  description = "Name of the s3 bucket. Must be unique."
  type        = string
}

variable "tags" {
  description = "Tags to set on the bucket."
  type        = map(string)
  default     = {}
}
```

We take a user input for the bucket name and tags. Next, we will define the output variables for our Terraform configuration. Create a new file named `outputs.tf` and add the following code:

```hcl
output "arn" {
  description = "ARN of the bucket"
  value       = aws_s3_bucket.s3_bucket.arn
}

output "name" {
  description = "Name (id) of the bucket"
  value       = aws_s3_bucket.s3_bucket.id
}

output "domain" {
  description = "Domain name of the bucket"
  value       = aws_s3_bucket_website_configuration.s3_bucket.website_domain
}

output "website_endpoint" {
  value = aws_s3_bucket_website_configuration.s3_bucket.website_endpoint
}
```

The output variables are the ARN, name, domain name, and website endpoint of the bucket. With all the configuration files in place, we can now create the S3 bucket. Create a new file named `main.tf` and create the S3 bucket using the following code:

```hcl
resource "aws_s3_bucket" "s3_bucket" {
  bucket = var.bucket_name
  tags   = var.tags
}
```

To configure the static website hosting, we will use the `aws_s3_bucket_website_configuration` resource. Add the following code to the `main.tf` file:

```hcl
resource "aws_s3_bucket_website_configuration" "s3_bucket" {
  bucket = aws_s3_bucket.s3_bucket.id

  index_document {
    suffix = "index.html"
  }

  error_document {
    key = "error.html"
  }

}
```

To set the bucket policy, we will use the `aws_s3_bucket_policy` resource. Add the following code to the `main.tf` file:

```hcl
resource "aws_s3_bucket_acl" "s3_bucket" {
  bucket = aws_s3_bucket.s3_bucket.id
  acl    = "public-read"
}

resource "aws_s3_bucket_policy" "s3_bucket" {
  bucket = aws_s3_bucket.s3_bucket.id

  policy = jsonencode({
    Version = "2012-10-17"
    Statement = [
      {
        Sid       = "PublicReadGetObject"
        Effect    = "Allow"
        Principal = "*"
        Action    = "s3:GetObject"
        Resource = [
          aws_s3_bucket.s3_bucket.arn,
          "${aws_s3_bucket.s3_bucket.arn}/*",
        ]
      },
    ]
  })
}
```

In the above code, we are setting the ACL of the bucket to `public-read` and setting the bucket policy to allow public access to the bucket. Pick up an appropriate policy based on your use case. Let's use the `aws_s3_object` resource to upload the files to the bucket. Add the following code to the `main.tf` file:

```hcl
resource "aws_s3_object" "object_www" {
  depends_on   = [aws_s3_bucket.s3_bucket]
  for_each     = fileset("${path.root}", "*.html")
  bucket       = var.bucket_name
  key          = basename(each.value)
  source       = each.value
  etag         = filemd5("${each.value}")
  content_type = "text/html"
  acl          = "public-read"
}
```

The above code uploads all our html files to the bucket. We are also setting the ACL of the files to `public-read`. Optionally, if you have static assets like images, CSS, and JavaScript files, you can upload them to the bucket using the same `aws_s3_bucket_object` resource by adding the following code to the `main.tf` file:

```hcl
resource "aws_s3_object" "object_assets" {
  depends_on = [aws_s3_bucket.s3_bucket]
  for_each   = fileset(path.module, "assets/*")
  bucket     = var.bucket_name
  key        = each.value
  source     = "${each.value}"
  etag       = filemd5("${each.value}")
  acl        = "public-read"
}
```

With all the configuration files in place, we can now initialize the Terraform configuration. Run the following command to initialize the Terraform configuration:

{{< command >}}
$ terraform init

...
Terraform has been successfully initialized!
...
{{< / command >}}

We can create an execution plan based on our Terraform configuration for the AWS resources. Run the following command to create an execution plan:

{{< command >}}
$ terraform plan
{{< / command >}}

Finally, we can apply the Terraform configuration to create the AWS resources. Run the following command to apply the Terraform configuration:

{{< command >}}
$ terraform apply

var.bucket_name
  Name of the s3 bucket. Must be unique.

  Enter a value: testbucket
...
arn = "arn:aws:s3:::testbucket"
domain = "s3-website-us-east-1.amazonaws.com"
name = "testbucket"
website_endpoint = "testbucket.s3-website-us-east-1.amazonaws.com"
{{< / command >}}

In the above command, we specified `testbucket` as the bucket name. You can specify any bucket name since LocalStack is ephemeral, and stopping your LocalStack container will delete all the created resources. The above command output includes the ARN, name, domain name, and website endpoint of the bucket. You can see the `website_endpoint` configured to use AWS S3 Website Endpoint. You can now access the website using the bucket name in the following format: `http://<BUCKET_NAME>.s3-website.localhost.localstack.cloud:4566`. Since the endpoint is configured to use `localhost.localstack.cloud`, no real AWS resources have been created.

You can optionally use the `tflocal` CLI as a drop-in replacement for the official Terraform CLI. `tflocal` uses the Terraform Override mechanism to create a temporary `localstack_providers_override.tf` file, which is deleted after the infrastructure is created. It mitigates the need to create the `provider.tf` file manually. You can use `tflocal` to create the infrastructure by running the following commands:

{{< command >}}
$ tflocal init
$ tflocal plan
$ tflocal apply
{{< / command >}}

## Conclusion

In this tutorial, we have seen how to use LocalStack to create an S3 bucket and configure it to serve a static website. We have also seen how you can use Terraform to provision AWS infrastructure in an emulated local environment using LocalStack. You can use the [LocalStack App](https://app.localstack.cloud) to view the created buckets and files on the LocalStack Resource dashboard for S3 and upload more files or perform other operations on the bucket. Using LocalStack, you can perform various operations using emulated S3 buckets and other AWS services without creating any real AWS resources.

The code for this tutorial can be found in our [LocalStack Terraform samples over GitHub](https://github.com/localstack/localstack-terraform-samples/tree/master/s3-static-website).
Please make sure to adjust the paths for the html files in `main.tf`.
Further documentation for S3 is available on our [S3 documentation]({{<ref "user-guide/aws/s3" >}}).
