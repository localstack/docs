---
title: "Host a static website locally using Simple Storage Service (S3) and Terraform with LocalStack"
linkTitle: "Host a static website locally using Simple Storage Service (S3) and Terraform with LocalStack"
weight: 4
description: >
  Host a static website using a Simple Storage Service (S3) bucket to serve static content by provisioning the infrastructure using Terraform in LocalStack. Learn how to configure S3 buckets locally for testing and integration, and make use of LocalStack's S3 API & `tflocal` CLI to provision infrastructure locally.
cascade:
  type: docs
---

[AWS Simple Storage Service (S3)](https://aws.amazon.com/s3/) is a proprietary object storage solution that can store an unlimited number of objects for many use cases. S3 is a highly scalable, durable and reliable service that we can use for various use-cases: hosting a static site, handling big data analytics, managing application logs, storing web assets and much more!

With S3, you have unlimited storage with your data stored in buckets. A bucket refers to a directory, while an object is just another term for a file. Every object (file) stores the name of the file (key), the contents (value), a version ID and the associated metadata. You can also use S3 to host a static website, to serve static content. It might include HTML, CSS, JavaScript, images, and other assets that make up your website.

LocalStack Community supports the S3 API, which means you can use the same API calls to interact with S3 in LocalStack as you would with AWS. Using LocalStack, you can create and manage S3 buckets and objects locally, use AWS SDKs and third-party integrations to work with S3, and test your applications without making any significant alterations. LocalStack also supports creation of S3 buckets with static website hosting enabled.

In this tutorial, we will deploy a static website using a S3 bucket over a locally emulated AWS infrastructure on LocalStack. We will use Terraform, to automate the creation & management of AWS resources by declaring them in the HashiCorp Configuration Language (HCL). We will also learn about `tflocal`, a CLI wrapper created by LocalStack, that allows you to run Terraform locally against LocalStack.
