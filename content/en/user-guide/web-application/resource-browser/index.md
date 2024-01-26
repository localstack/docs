---
title: "Resource Browser"
tags: ["LocalStack Pro"]
weight: 100
description: >
    The Resource Browser allows you to view and manage your local AWS resources through the LocalStack Web Application.
---

The LocalStack Resource Browser allow you to view, manage, and deploy AWS resources locally while building & testing their cloud applications locally. It provides an internal, integrated experience, similar to the AWS Management Console, to manage the ephemeral resources locally in a LocalStack container on your local machine.

<img src="resource-browser.png" alt="LocalStack Web Application's Resource Browsers outlining various local AWS services" title="Resource Browser" width="900" />

{{< alert title="Warning" color="warning">}}
- If you encounter a `Network Failure` error message while accessing the Resource Browser, it is likely that the LocalStack container is not running or the instance is not reachable at the endpoint specified in the instance bookmark.
{{< /alert >}}

{{<alert title="Note">}}
- An AWS region dropdown menu in the dashboard is located on the top right of the page. You can select your desired region to ensure that you can view your resources. If you cannot view resources that you have recently created, you should verify that you are checking the resources in the correct region.

- The Resource Browser provide an experience similar to the AWS Management Console. However, the Resource Browser is not a replacement for the AWS Management Console and only replicate some of the features of the AWS Management Console. We recommend using our [integrations](https://docs.localstack.cloud/user-guide/integrations/) to create your resources, with the Resource Browser being used for quick viewing and management of your resources.

- To view the running services in your LocalStack container, you can use the [System Status](https://app.localstack.cloud/status). This view provides a quick overview of the running services in your LocalStack container. To get a detailed telemetry of your API calls to your LocalStack containers, check out [Stack Insights](https://docs.localstack.cloud/user-guide/web-application/stack-insights/).
{{< /alert >}}

## Supported services

We currently support the following local AWS services in our Resource Browser:

- [Application Auto Scaling](https://app.localstack.cloud/inst/default/resources/application-autoscaling)
- [API Gateway](https://app.localstack.cloud/inst/default/resources/apigateway/)
- [Athena](https://app.localstack.cloud/inst/default/resources/athena/databases)
- [AppSync](https://app.localstack.cloud/inst/default/resources/appsync)
- [Athena](https://app.localstack.cloud/inst/default/resources/athena/databases)
- [Backup](https://app.localstack.cloud/inst/default/resources/backup/plans)
- [CloudFormation](https://app.localstack.cloud/inst/default/resources/cloudformation/stacks)
- [CloudFront](https://app.localstack.cloud/inst/default/resources/cloudfront/distributions)
- [CloudTrail](https://app.localstack.cloud/inst/default/resources/cloudtrail/events)
- [CloudWatch Events](https://app.localstack.cloud/inst/default/resources/events)
- [CloudWatch Logs](https://app.localstack.cloud/inst/default/resources/cloudwatch/groups)
- [CloudWatch Metrics](https://app.localstack.cloud/inst/default/resources/monitoring)
- [Cognito](https://app.localstack.cloud/inst/default/resources/cognito-idp)
- [DynamoDB](https://app.localstack.cloud/inst/default/resources/dynamodb)
- [EC2](https://app.localstack.cloud/inst/default/resources/ec2)
- [ECR](https://app.localstack.cloud/inst/default/resources/ecr/repositories)
- [ECS](https://app.localstack.cloud/inst/default/resources/ecs)
- [ElastiCache](https://app.localstack.cloud/inst/default/resources/elasticache)
- [EventBridge](https://app.localstack.cloud/inst/default/resources/eventbridge)
- [Glue](https://app.localstack.cloud/inst/default/resources/glue)
- [IAM](https://app.localstack.cloud/inst/default/resources/iam)
- [Kafka](https://app.localstack.cloud/inst/default/resources/kafka)
- [Kinesis](https://app.localstack.cloud/inst/default/resources/kinesis)
- [KMS](https://app.localstack.cloud/inst/default/resources/kms)
- [Lambda](https://app.localstack.cloud/inst/default/resources/lambda/functions)
- [OpenSearch](https://app.localstack.cloud/inst/default/resources/opensearch/domains)
- [Route 53](https://app.localstack.cloud/inst/default/resources/route53)
- [RDS](https://app.localstack.cloud/inst/default/resources/rds)
- [Sagemaker](https://app.localstack.cloud/inst/default/resources/sagemaker/models)
- [S3](https://app.localstack.cloud/inst/default/resources/s3)
- [SES](https://app.localstack.cloud/inst/default/resources/ses/)
- [SQS](https://app.localstack.cloud/inst/default/resources/sqs)
- [SNS](https://app.localstack.cloud/inst/default/resources/sns)
- [Secrets Manager](https://app.localstack.cloud/inst/default/resources/secretsmanager)
- [Step Functions](https://app.localstack.cloud/inst/default/resources/stepfunctions)
- [Systems Manager](https://app.localstack.cloud/inst/default/resources/ssm)
- [TimestreamDB](https://app.localstack.cloud/inst/default/resources/timestream)
