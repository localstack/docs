---
title: "Creating infrastructure with Terraform locally"
linkTitle: "Creating infrastructure with Terraform locally"
weight: 4
description: >
  In this video, we'll utilize LocalStack's Terraform integration to deploy and configure local AWS resources on LocalStack. We'll use `tflocal`, a wrapper CLI that enables you to run Terraform commands against LocalStack. Alternatively, if you prefer not to use `tflocal`, you can use `terraform` CLI directly with minor modifications to the Terraform configuration, a topic we'll cover later in the video.
length: 08:03
leadimage: infra-terraform.png
videoUrl: https://www.youtube.com/embed/lsF3kewOeBU?si=Pdjd0KDpnza6ifxJ
type: lessons
url: "/academy/localstack-deployment/infra-terraform/"
---

In this video, we'll utilize Terraform to deploy AWS resources locally through LocalStack. These resources, including DynamoDB tables, API Gateway, and VPC. We'll use `tflocal`, a wrapper CLI that serves as a wrapper on the `terraform` CLI to execute Terraform commands against LocalStack.

-   We'll create a `main.tf` file and then apply the Terraform configuration on LocalStack.
-   We'll demonstrate various configuration options for setting up the infrastructure for our application.
-   After applying Terraform, we'll inspect the output, showcasing deployed resources such as API URLs, ECS cluster name, and VPC ID.
-   Towards the end, we'll verify the deployment and resource creation using the Resource Browser.