---
title: "Resource Browser"
tags: ["LocalStack Pro"]
weight: 100
description: >
    The Resource Browser allows you to view and manage your local AWS resources through the LocalStack Web Application.
---

The LocalStack Resource Browser allow you to view, manage, and deploy AWS resources locally while building & testing their cloud applications locally. It provides an internal, integrated experience, similar to the AWS Management Console, to manage the ephemeral resources locally in a LocalStack container on your local machine. The Resource Browser can be operated only if a LocalStack container is running on your local machine and the local endpoint URL, which can be configured in the [account settings](https://app.localstack.cloud/account/settings) of the web application, points to the URL under which LocalStack is accessible.

<img src="resource-browser.png" alt="LocalStack Web Application's Resource Browsers outlining various local AWS services" title="Resource Browser" width="900" />

{{< alert title="Warning" color="warning">}}
- If you encounter a `Network Failure` error message while accessing the Resource Browser, it is likely that the LocalStack container is not running or the local endpoint URL is not configured correctly. To resolve this issue, ensure that your LocalStack container is running or your [local endpoint URL is configured correctly](https://app.localstack.cloud/account/settings).
{{< /alert >}}

{{<alert title="Note">}}
- An AWS region dropdown menu in the dashboard is located on the top right of the navigation bar, beside the notifications icon. You can select your desired region to ensure that you can view your resources. If you cannot view resources that you have recently created, you should verify that you are checking the resources in the correct region.

- The Resource Browser provide an experience similar to the AWS Management Console. However, the Resource Browser is not a replacement for the AWS Management Console and only replicate some of the features of the AWS Management Console. We recommend using our [integrations](https://docs.localstack.cloud/user-guide/integrations/) to create your resources, with the Resource Browser being used for quick viewing and management of your resources.

- To view the running services in your LocalStack container, you can use the [System Status](https://app.localstack.cloud/status). This view provides a quick overview of the running services in your LocalStack container. To get a detailed telemetry of your API calls to your LocalStack containers, check out [Stack Insights](https://docs.localstack.cloud/user-guide/web-application/stack-insights/).
{{< /alert >}}

## Supported services

We currently support the following local AWS services in our Resource Browser:

- [API Gateway](https://app.localstack.cloud/resources/gateway/v1)
- [AppSync](https://app.localstack.cloud/resources/appsync)
- [Athena](https://app.localstack.cloud/resources/athena/databases)
- [Backup](https://app.localstack.cloud/resources/backup/plans)
- [CloudFormation](https://app.localstack.cloud/resources/cloudformation/stacks)
- [CloudTrail](https://app.localstack.cloud/resources/cloudtrail/events)
- [CloudWatch Logs](https://app.localstack.cloud/resources/cloudwatch/groups)
- [CloudWatch Metrics](https://app.localstack.cloud/resources/monitoring)
- [Cognito](https://app.localstack.cloud/resources/cognito)
- [DynamoDB](https://app.localstack.cloud/resources/dynamodb)
- [EC2](https://app.localstack.cloud/resources/ec2)
- [ECR](https://app.localstack.cloud/resources/ecr/repositories)
- [ECS](https://app.localstack.cloud/resources/ecs)
- [ElastiCache](https://app.localstack.cloud/resources/elasticache)
- [EventBridge](https://app.localstack.cloud/resources/eventbridge)
- [Glue](https://app.localstack.cloud/resources/glue)
- [IAM](https://app.localstack.cloud/resources/iam)
- [Kinesis](https://app.localstack.cloud/resources/kinesis)
- [KMS](https://app.localstack.cloud/resources/kms)
- [Lambda](https://app.localstack.cloud/resources/lambda/functions)
- [RDS](https://app.localstack.cloud/resources/rds/instances)
- [S3](https://app.localstack.cloud/resources/s3)
- [SES](https://app.localstack.cloud/resources/ses/v1/identities)
- [SQS](https://app.localstack.cloud/resources/sqs)
- [SNS](https://app.localstack.cloud/resources/sns)
- [Secrets Manager](https://app.localstack.cloud/resources/secretsmanager)
- [Step Functions](https://app.localstack.cloud/resources/stepfunctions)
- [Systems Manager](https://app.localstack.cloud/resources/ssm)
- [TimestreamDB](https://app.localstack.cloud/resources/timestream)
