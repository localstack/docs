---
title: "Creating infra with Terraform locally"
linkTitle: "Creating infra with Terraform locally"
weight: 4
description: >
  In this video we will be using LocalStack's terraform integration to automate the process of deploying and configuring the resources on localstack. For this we will be using `tflocal` - a small wrapper script to run Terraform against LocalStack. If you don’t want to use tflocal, you can use terraform, with small changes to the tf file, which we will talk about later in the video. 
length: 08:03
leadimage: infra-terraform.png
videoUrl: https://www.youtube.com/embed/lsF3kewOeBU?si=Pdjd0KDpnza6ifxJ
type: lessons
url: "/academy/localstack-deployment/infra-terraform/"
---

In this video we will use Terraform to deploy resources on localstack. These are AWS resources such as DynamoDB tables, API Gateway, VPC, etc.  that are requried by our application to function. We will deploy this using `tflocal`, small wrapper script to run Terraform against LocalStack.

- We will create `main.tf` file with some aws resources such as DynamoDb Table and apply the terraform on localstack.
- Further we will walk you through the whole terraform code and show the different configuration options for creating the infrastructure for our demo application.
- Once the terraform is applied, we will see some of the resources that are created as output such as API URLs, ECS cluster name, VPC ID etc.
- Towards the end we will check the deployment and that the resources have been created using the Resource Browser.

In the next video we will see the same deployment using AWS Cloudformation.

Further reading:

- [LocalStack Terraform Docs](https://docs.localstack.cloud/user-guide/integrations/)
- [LocalStack Tutroial using Terraform](https://docs.localstack.cloud/tutorials/s3-static-website-terraform/)
- [LocalStack Terraform Examples](https://github.com/localstack-samples/localstack-terraform-samples)
- [Sample Terraform ECS Apigateway ](https://github.com/localstack-samples/sample-terraform-ecs-apigateway)
- [Terraform Local](https://github.com/localstack/terraform-local)


