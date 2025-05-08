---
title: "LocalStack for AWS: Tiers, Licensing, and Access"
linkTitle: "Licensing & Tiers"
weight: 80
description: >
  Service availability and licensing details across LocalStack for AWS tiers.
---

This document outlines the features, emulated AWS services, and enhancements included in each LocalStack for AWS tier.
It also clarifies how licensing works across workspaces and users.

As of **May 8, 2025**, LocalStack for AWS is offered in four tiers:

- Free
- Base
- Ultimate
- Enterprise (custom offering available via Sales only)

If you purchased a LocalStack license **before May 8, 2025**, [click here to learn about your available features and legacy entitlements]](#legacy-plans).

### Licensing & Access Rules

Each **workspace** can only be assigned a single pricing tier.
You cannot mix and match (e.g., Base and Ultimate) within the same workspace.

Licenses must be assigned to individual users.
This generates an authentication token that enables access to the emulator and any enhancements included in the tier.

Not sure which tier fits your use case?
Explore our [pricing page](https://www.localstack.cloud/pricing).

For unique licensing needs across teams or environments, please contact Sales.

### Usage Allocation Per Workspace

All paid tiers include a fixed allocation of:

- CI credits (monthly pool)
- Ephemeral Instance minutes (monthly pool)
- Cloud Pod storage (per contract, shared across all users)

We will soon support self-service purchasing of additional credits, minutes, and storage.
Until then, please reach out to Sales if you need to expand your usage.

### Service Coverage Clarification

The table below shows which AWS services are available in each pricing tier.
It does not indicate the level of API coverage or feature availability.

To learn more about how a service behaves in LocalStack, refer to that individual service page or contact Support.

| AWS Services | Free | Base | Ultimate |
| -------- | ------- | ------- | ------- |
| Analytics |  |  |  |
| [](https://docs.localstack.cloud/user-guide/aws/es/)[Amazon ElasticSearch](https://docs.localstack.cloud/user-guide/aws/es/) | ✅ | ✅ | ✅ |
| [](https://docs.localstack.cloud/references/coverage/coverage_kinesis/)[Amazon Kinesis Streams](https://docs.localstack.cloud/references/coverage/coverage_kinesis/) | ✅ | ✅ | ✅ |
| [](https://docs.localstack.cloud/references/coverage/coverage_firehose/)[Amazon Kinesis Data Firehose](https://docs.localstack.cloud/references/coverage/coverage_firehose/) | ✅ | ✅ | ✅ |
| [](https://docs.localstack.cloud/references/coverage/coverage_opensearch/)[Amazon OpenSearch](https://docs.localstack.cloud/references/coverage/coverage_opensearch/) | ✅ | ✅ | ✅ |
| [](https://docs.localstack.cloud/references/coverage/coverage_redshift/)[Amazon Redshift](https://docs.localstack.cloud/references/coverage/coverage_redshift/) | ✅ | ✅ | ✅ |
| [](https://docs.localstack.cloud/references/coverage/coverage_athena/)[Amazon Athena](https://docs.localstack.cloud/references/coverage/coverage_athena/) | ❌ | ❌ | ✅ |
| [](https://docs.localstack.cloud/references/coverage/coverage_emr/)[Amazon EMR](https://docs.localstack.cloud/references/coverage/coverage_emr/) | ❌ | ❌ | ✅ |
| [](https://docs.localstack.cloud/references/coverage/coverage_emr-serverless/)[Amazon EMR Serverless](https://docs.localstack.cloud/references/coverage/coverage_emr-serverless/) | ❌ | ❌ | ✅ |
| [](https://docs.localstack.cloud/references/coverage/coverage_glue/)[AWS Glue](https://docs.localstack.cloud/references/coverage/coverage_glue/) | ❌ | ❌ | ✅ |
| [](https://docs.localstack.cloud/references/coverage/coverage_redshift-data/)[Amazon Redshift Data API](https://docs.localstack.cloud/references/coverage/coverage_redshift-data/) | ❌ | ❌ | ✅ |
| [](https://docs.localstack.cloud/references/coverage/coverage_lakeformation/)[AWS Lake Formation](https://docs.localstack.cloud/references/coverage/coverage_lakeformation/) | ❌ | ❌ | ✅ |
| [](https://docs.localstack.cloud/user-guide/aws/msk/)[Amazon Managed Streaming for Apache Kafka](https://docs.localstack.cloud/user-guide/aws/msk/) | ❌ | ❌ | ✅ |
| [](https://docs.localstack.cloud/user-guide/aws/kinesisanalytics/)[Amazon Kinesis Data Analytics](https://docs.localstack.cloud/user-guide/aws/kinesisanalytics/) | ❌ | ❌ | ✅ |
| [](https://docs.localstack.cloud/user-guide/aws/kinesisanalyticsv2/)[Amazon Managed Service for Apache Flink](https://docs.localstack.cloud/user-guide/aws/kinesisanalyticsv2/) | ❌ | ❌ | ✅ |
| Application Integration |  |  |  |
| [](https://docs.localstack.cloud/user-guide/aws/swf/)[Amazon Simple Workflow Service (SWF)](https://docs.localstack.cloud/user-guide/aws/swf/) | ✅ | ✅ | ✅ |
| [](https://docs.localstack.cloud/user-guide/aws/sns/)[Amazon Simple Notification Service (SNS)](https://docs.localstack.cloud/user-guide/aws/sns/) | ✅ | ✅ | ✅ |
| [](https://docs.localstack.cloud/user-guide/aws/sqs/)[Amazon Simple Queue Service (SQS)](https://docs.localstack.cloud/user-guide/aws/sqs/) | ✅ | ✅ | ✅ |
| [](https://docs.localstack.cloud/user-guide/aws/stepfunctions/)[AWS Step Functions](https://docs.localstack.cloud/user-guide/aws/stepfunctions/) | ✅ | ✅ | ✅ |
| [](https://docs.localstack.cloud/user-guide/aws/events/)[Amazon EventBridge](https://docs.localstack.cloud/user-guide/aws/events/) | ✅ | ✅ | ✅ |
| [](https://docs.localstack.cloud/user-guide/aws/scheduler/)[Amazon EventBridge Scheduler](https://docs.localstack.cloud/user-guide/aws/scheduler/) | ✅ | ✅ | ✅ |
| [](https://docs.localstack.cloud/user-guide/aws/mq/)[Amazon MQ](https://docs.localstack.cloud/user-guide/aws/mq/) | ❌ | ✅ | ✅ |
| [](https://docs.localstack.cloud/user-guide/aws/pipes/)[Amazon EventBridge Pipes](https://docs.localstack.cloud/user-guide/aws/pipes/) | ❌ | ❌ | ✅ |
| [](https://docs.localstack.cloud/user-guide/aws/mwaa/)[Amazon Managed Workflows for Apache Airflow](https://docs.localstack.cloud/user-guide/aws/mwaa/) | ❌ | ❌ | ✅ |
| BlockChain |  |  |  |
| [](https://docs.localstack.cloud/user-guide/aws/managedblockchain/)[Amazon Managed Blockchain](https://docs.localstack.cloud/user-guide/aws/managedblockchain/) | ❌ | ❌ | ✅ |
| Business Applications |  |  |  |
| [](https://docs.localstack.cloud/user-guide/aws/ses/)[Amazon Simple Email Service (SES)](https://docs.localstack.cloud/user-guide/aws/ses/) | ✅ | ✅ | ✅ |
| [](https://docs.localstack.cloud/user-guide/aws/ses/)[Amazon Simple Email Service API V2 (SES)](https://docs.localstack.cloud/user-guide/aws/ses/) | ❌ | ✅ | ✅ |
| [](https://docs.localstack.cloud/user-guide/aws/pinpoint/)[Amazon Pinpoint](https://docs.localstack.cloud/user-guide/aws/pinpoint/) | ❌ | ❌ | ✅ |
| Cloud Financial Management |  |  |  |
| [](https://docs.localstack.cloud/user-guide/aws/ce/)[AWS Cost Explorer](https://docs.localstack.cloud/user-guide/aws/ce/) | ❌ | ❌ | ✅ |
| Compute |  |  |  |
| [](https://docs.localstack.cloud/user-guide/aws/ec2/)[Amazon Elastic Compute Cloud (EC2)](https://docs.localstack.cloud/user-guide/aws/ec2/) | ✅ | ✅ | ✅ |
| [](https://docs.localstack.cloud/user-guide/aws/lambda/)[AWS Lambda](https://docs.localstack.cloud/user-guide/aws/lambda/) | ✅ | ✅ | ✅ |
| [](https://docs.localstack.cloud/user-guide/aws/batch/)[AWS Batch](https://docs.localstack.cloud/user-guide/aws/batch/) | ❌ | ❌ | ✅ |
| [](https://docs.localstack.cloud/user-guide/aws/elasticbeanstalk/)[AWS Elastic Beanstalk](https://docs.localstack.cloud/user-guide/aws/elasticbeanstalk/) | ❌ | ❌ | ✅ |
| [](https://docs.localstack.cloud/user-guide/aws/serverlessrepo/)[AWS Serverless Application Repository](https://docs.localstack.cloud/user-guide/aws/serverlessrepo/) | ❌ | ❌ | ✅ |
| Containers |  |  |  |
| [](https://docs.localstack.cloud/user-guide/aws/ecr/)[Amazon Elastic Container Registry (ECR)](https://docs.localstack.cloud/user-guide/aws/ecr/) | ❌ | ✅ | ✅ |
| [](https://docs.localstack.cloud/user-guide/aws/ecr/)[Amazon Elastic Container Service (ECS)](https://docs.localstack.cloud/user-guide/aws/ecr/) | ❌ | ✅ | ✅ |
| [](https://docs.localstack.cloud/user-guide/aws/eks/)[Amazon Elastic Kubernetes Service (EKS)](https://docs.localstack.cloud/user-guide/aws/eks/) | ❌ | ❌ | ✅ |
| Customer Enablement |  |  |  |
| [](https://docs.localstack.cloud/user-guide/aws/support/)[AWS Support API](https://docs.localstack.cloud/user-guide/aws/support/) | ✅ | ✅ | ✅ |
| DataBases |  |  |  |
| [](https://docs.localstack.cloud/user-guide/aws/dynamodb/)[Amazon DynamoDB](https://docs.localstack.cloud/user-guide/aws/dynamodb/) | ✅ | ✅ | ✅ |
| [](https://docs.localstack.cloud/user-guide/aws/dynamodbstreams/)[Amazon DynamoDB Streams](https://docs.localstack.cloud/user-guide/aws/dynamodbstreams/) | ✅ | ✅ | ✅ |
| [](https://docs.localstack.cloud/user-guide/aws/elasticache/)[Amazon ElastiCache](https://docs.localstack.cloud/user-guide/aws/elasticache/) | ❌ | ✅ | ✅ |
| [](https://docs.localstack.cloud/user-guide/aws/rds/)[Amazon Relational Database Service (RDS)](https://docs.localstack.cloud/user-guide/aws/rds/) | ❌ | ✅ | ✅ |
| [](https://docs.localstack.cloud/references/coverage/coverage_rds-data/)[Amazon RDS Data API](https://docs.localstack.cloud/references/coverage/coverage_rds-data/) | ❌ | ✅ | ✅ |
| [](https://docs.localstack.cloud/user-guide/aws/docdb/)[Amazon DocumentDB](https://docs.localstack.cloud/user-guide/aws/docdb/) | ❌ | ❌ | ✅ |
| [](https://docs.localstack.cloud/user-guide/aws/memorydb/)[Amazon MemoryDB](https://docs.localstack.cloud/user-guide/aws/memorydb/) | ❌ | ❌ | ✅ |
| [](https://docs.localstack.cloud/user-guide/aws/neptune/)[Amazon Neptune](https://docs.localstack.cloud/user-guide/aws/neptune/) | ❌ | ❌ | ✅ |
| [](https://docs.localstack.cloud/user-guide/aws/timestream/)[Amazon Timestream](https://docs.localstack.cloud/user-guide/aws/timestream/) | ❌ | ❌ | ✅ |
| [](https://docs.localstack.cloud/user-guide/aws/qldb/)[Amazon Quantum Ledger Database (QLDB)](https://docs.localstack.cloud/user-guide/aws/qldb/) | ❌ | ❌ | ✅ |
| Developer Tools |  |  |  |
| [](https://docs.localstack.cloud/references/coverage/coverage_codecommit/)[AWS CodeCommit](https://docs.localstack.cloud/references/coverage/coverage_codecommit/) | ❌ | ✅ | ✅ |
| AWS CodeBuild | ❌ | ✅ | ✅ |
| AWS CodeConnections | ❌ | ✅ | ✅ |
| [](https://docs.localstack.cloud/user-guide/aws/fis/)[AWS Fault Injection Service](https://docs.localstack.cloud/user-guide/aws/fis/) | ❌ | ❌ | ✅ |
| AWS CodeDeploy | ❌ | ❌ | ✅ |
| AWS CodePipeline | ❌ | ❌ | ✅ |
| [](https://docs.localstack.cloud/user-guide/aws/xray/)[AWS X-Ray](https://docs.localstack.cloud/user-guide/aws/xray/) | ❌ | ❌ | ✅ |
| Frontend Web & Mobile Services |  |  |  |
| [](https://docs.localstack.cloud/user-guide/aws/amplify/)[AWS Amplify](https://docs.localstack.cloud/user-guide/aws/amplify/) | ❌ | ❌ | ✅ |
| [](https://docs.localstack.cloud/user-guide/aws/appsync/)[AWS AppSync](https://docs.localstack.cloud/user-guide/aws/appsync/) | ❌ | ❌ | ✅ |
| IoT |  |  |  |
| [](https://docs.localstack.cloud/user-guide/aws/iot/)[AWS IoT](https://docs.localstack.cloud/user-guide/aws/iot/) | ❌ | ✅ | ✅ |
| [](https://docs.localstack.cloud/user-guide/aws/iotwireless/)[AWS IoT Wireless](https://docs.localstack.cloud/user-guide/aws/iotwireless/) | ❌ | ❌ | ✅ |
| [](https://docs.localstack.cloud/user-guide/aws/iotanalytics/)[AWS IoT Analytics](https://docs.localstack.cloud/user-guide/aws/iotanalytics/) | ❌ | ❌ | ✅ |
| [](https://docs.localstack.cloud/user-guide/aws/iotdata/)[AWS IoT Data](https://docs.localstack.cloud/user-guide/aws/iotdata/) | ❌ | ❌ | ✅ |
| Management & Governance |  |  |  |
| [](https://docs.localstack.cloud/user-guide/aws/cloudformation/)[AWS CloudFormation](https://docs.localstack.cloud/user-guide/aws/cloudformation/) | ✅ | ✅ | ✅ |
| [](https://docs.localstack.cloud/user-guide/aws/cloudwatch/)[Amazon CloudWatch Metrics](https://docs.localstack.cloud/user-guide/aws/cloudwatch/) | ✅ | ✅ | ✅ |
| [](https://docs.localstack.cloud/user-guide/aws/logs/)[Amazon CloudWatch Logs](https://docs.localstack.cloud/user-guide/aws/logs/) | ✅ | ✅ | ✅ |
| [](https://docs.localstack.cloud/user-guide/aws/resource_groups/)[AWS Resource Groups](https://docs.localstack.cloud/user-guide/aws/resource_groups/) | ✅ | ✅ | ✅ |
| [](https://docs.localstack.cloud/references/coverage/coverage_ssm/)[AWS Systems Manager Parameter Store](https://docs.localstack.cloud/references/coverage/coverage_ssm/) | ✅ | ✅ | ✅ |
| [](https://docs.localstack.cloud/references/coverage/coverage_cloudcontrol/)[AWS Cloud Control](https://docs.localstack.cloud/references/coverage/coverage_cloudcontrol/) | ❌ | ✅ | ✅ |
| [](https://docs.localstack.cloud/references/coverage/coverage_application-autoscaling/)[AWS Application Auto Scaling](https://docs.localstack.cloud/references/coverage/coverage_application-autoscaling/) | ❌ | ✅ | ✅ |
| [](https://docs.localstack.cloud/references/coverage/coverage_autoscaling/)[Amazon EC2 Auto Scaling](https://docs.localstack.cloud/references/coverage/coverage_autoscaling/) | ❌ | ✅ | ✅ |
| [](https://docs.localstack.cloud/references/coverage/coverage_config/)[AWS Config](https://docs.localstack.cloud/references/coverage/coverage_config/) | ✅ | ✅ | ✅ |
| [](https://docs.localstack.cloud/references/coverage/coverage_appconfig/)[AWS AppConfig](https://docs.localstack.cloud/references/coverage/coverage_appconfig/) | ❌ | ✅ | ✅ |
| [](https://docs.localstack.cloud/references/coverage/coverage_cloudtrail/)[AWS CloudTrail](https://docs.localstack.cloud/references/coverage/coverage_cloudtrail/) | ❌ | ❌ | ✅ |
| [](https://docs.localstack.cloud/references/coverage/coverage_account/)[AWS Account Management](https://docs.localstack.cloud/references/coverage/coverage_account/) | ❌ | ❌ | ✅ |
| [](https://docs.localstack.cloud/references/coverage/coverage_organizations/)[AWS Organizations](https://docs.localstack.cloud/references/coverage/coverage_organizations/) | ❌ | ❌ | ✅ |
| Media |  |  |  |
| [](https://docs.localstack.cloud/references/coverage/coverage_elastictranscoder/)[Amazon Elastic Transcoder](https://docs.localstack.cloud/references/coverage/coverage_elastictranscoder/) | ❌ | ✅ | ✅ |
| [](https://docs.localstack.cloud/references/coverage/coverage_mediaconvert/)[AWS Elemental MediaConvert](https://docs.localstack.cloud/references/coverage/coverage_mediaconvert/) | ❌ | ❌ | ✅ |
| [](https://docs.localstack.cloud/references/coverage/coverage_mediastore/)[AWS Elemental MediaStore](https://docs.localstack.cloud/references/coverage/coverage_mediastore/) | ❌ | ❌ | ✅ |
| [](https://docs.localstack.cloud/references/coverage/coverage_mediastore-data/)[AWS Elemental MediaStore Data Plane](https://docs.localstack.cloud/references/coverage/coverage_mediastore-data/) | ❌ | ❌ | ✅ |
| Migration & Transfer |  |  |  |
| [](https://docs.localstack.cloud/references/coverage/coverage_transfer/)[AWS Transfer Family](https://docs.localstack.cloud/references/coverage/coverage_transfer/) | ❌ | ❌ | ✅ |
| [](https://docs.localstack.cloud/references/coverage/coverage_dms/)[AWS Database Migration Service](https://docs.localstack.cloud/references/coverage/coverage_dms/) | ❌ | ❌ | ✅ |
| Machine Learning |  |  |  |
| [](https://docs.localstack.cloud/references/coverage/coverage_transcribe/)[Amazon Transcribe](https://docs.localstack.cloud/references/coverage/coverage_transcribe/) | ✅ | ✅ | ✅ |
| [](https://docs.localstack.cloud/references/coverage/coverage_textract/)[Amazon Textract](https://docs.localstack.cloud/references/coverage/coverage_textract/) | ❌ | ❌ | ✅ |
| [](https://docs.localstack.cloud/references/coverage/coverage_sagemaker/)[Amazon SageMaker AI](https://docs.localstack.cloud/references/coverage/coverage_sagemaker/) | ❌ | ❌ | ✅ |
| [](https://docs.localstack.cloud/references/coverage/coverage_sagemaker-runtime/)[Amazon SageMaker Runtime](https://docs.localstack.cloud/references/coverage/coverage_sagemaker-runtime/) | ❌ | ❌ | ✅ |
| [](https://docs.localstack.cloud/references/coverage/coverage_bedrock/)[Amazon Bedrock](https://docs.localstack.cloud/references/coverage/coverage_bedrock/) | ❌ | ❌ | ✅ |
| [](https://docs.localstack.cloud/references/coverage/coverage_bedrock-runtime/)[Amazon Bedrock Runtime](https://docs.localstack.cloud/references/coverage/coverage_bedrock-runtime/) | ❌ | ❌ | ✅ |
| Networking & Content Delivery |  |  |  |
| [](https://docs.localstack.cloud/references/coverage/coverage_route53/)[Amazon Route 53](https://docs.localstack.cloud/references/coverage/coverage_route53/) | ✅ | ✅ | ✅ |
| [](https://docs.localstack.cloud/user-guide/aws/route53resolver/)[Amazon Route 53 Resolver](https://docs.localstack.cloud/user-guide/aws/route53resolver/) | ✅ | ✅ | ✅ |
| [](https://docs.localstack.cloud/references/coverage/coverage_apigateway/)[Amazon API Gateway REST API](https://docs.localstack.cloud/references/coverage/coverage_apigateway/) | ✅ | ✅ | ✅ |
| [](https://docs.localstack.cloud/references/coverage/coverage_apigatewayv2/)[Amazon API Gateway HTTP and WebSocket API](https://docs.localstack.cloud/references/coverage/coverage_apigatewayv2/) | ❌ | ✅ | ✅ |
| [](https://docs.localstack.cloud/references/coverage/coverage_apigatewaymanagementapi/)[Amazon API Gateway Management API](https://docs.localstack.cloud/references/coverage/coverage_apigatewaymanagementapi/) | ❌ | ✅ | ✅ |
| [](https://docs.localstack.cloud/references/coverage/coverage_elb/)[Elastic Load Balancing](https://docs.localstack.cloud/references/coverage/coverage_elb/) | ❌ | ✅ | ✅ |
| [](https://docs.localstack.cloud/references/coverage/coverage_elbv2/)[Elastic Load Balancing v2 (Application, Network)](https://docs.localstack.cloud/references/coverage/coverage_elbv2/) | ❌ | ✅ | ✅ |
| [](https://docs.localstack.cloud/references/coverage/coverage_cloudfront/)[Amazon CloudFront](https://docs.localstack.cloud/references/coverage/coverage_cloudfront/) | ❌ | ✅ | ✅ |
| [](https://docs.localstack.cloud/references/coverage/coverage_servicediscovery/)[AWS Cloud Map](https://docs.localstack.cloud/references/coverage/coverage_servicediscovery/) | ❌ | ❌ | ✅ |
| Security, Identity & Compliance |  |  |  |
| [](https://docs.localstack.cloud/references/coverage/coverage_kms/)[AWS Key Management Service (KMS)](https://docs.localstack.cloud/references/coverage/coverage_kms/) | ✅ | ✅ | ✅ |
| [](https://docs.localstack.cloud/references/coverage/coverage_secretsmanager/)[AWS Secrets Manager](https://docs.localstack.cloud/references/coverage/coverage_secretsmanager/) | ✅ | ✅ | ✅ |
| [](https://docs.localstack.cloud/references/coverage/coverage_sts/)[AWS Security Token Service](https://docs.localstack.cloud/references/coverage/coverage_sts/) | ✅ | ✅ | ✅ |
| [](https://docs.localstack.cloud/references/coverage/coverage_acm/)[AWS Certificate Manager](https://docs.localstack.cloud/references/coverage/coverage_acm/) | ✅ | ✅ | ✅ |
| [](https://docs.localstack.cloud/references/coverage/coverage_cognito-identity/)[Amazon Cognito Identity Pools](https://docs.localstack.cloud/references/coverage/coverage_cognito-identity/) | ❌ | ✅ | ✅ |
| [](https://docs.localstack.cloud/references/coverage/coverage_cognito-idp/)[Amazon Cognito User Pools](https://docs.localstack.cloud/references/coverage/coverage_cognito-idp/) | ❌ | ✅ | ✅ |
| [](https://docs.localstack.cloud/references/coverage/coverage_acm-pca/)[AWS Private Certificate Authority](https://docs.localstack.cloud/references/coverage/coverage_acm-pca/) | ❌ |  | ✅ |
| [](https://docs.localstack.cloud/references/coverage/coverage_wafv2/)[AWS Web Application Firewall (WAF)](https://docs.localstack.cloud/references/coverage/coverage_wafv2/) | ❌ | ❌ | ✅ |
| [](https://docs.localstack.cloud/references/coverage/coverage_iam/)[AWS Identity and Access Management (IAM)](https://docs.localstack.cloud/references/coverage/coverage_iam/) | ✅ | ✅ | ✅ |
| [](https://docs.localstack.cloud/references/coverage/coverage_identitystore/)[AWS IAM Identity Store API](https://docs.localstack.cloud/references/coverage/coverage_identitystore/) | ❌ | ❌ | ✅ |
| [](https://docs.localstack.cloud/references/coverage/coverage_sso-admin/)[AWS IAM Identity Center](https://docs.localstack.cloud/references/coverage/coverage_sso-admin/) | ❌ | ❌ | ✅ |
| [](https://docs.localstack.cloud/references/coverage/coverage_ram/)[AWS Resource Access Manager (RAM)](https://docs.localstack.cloud/references/coverage/coverage_ram/) | ❌ | ❌ | ✅ |
| [](https://docs.localstack.cloud/references/coverage/coverage_shield/)[AWS Shield](https://docs.localstack.cloud/references/coverage/coverage_shield/) | ❌ | ❌ | ✅ |
| Storage |  |  |  |
| [](https://docs.localstack.cloud/references/coverage/coverage_s3/)[Amazon S3](https://docs.localstack.cloud/references/coverage/coverage_s3/) | ✅ | ✅ | ✅ |
| [](https://docs.localstack.cloud/references/coverage/coverage_s3control/)[Amazon S3 Control](https://docs.localstack.cloud/references/coverage/coverage_s3control/) | ✅ | ✅ | ✅ |
| [](https://docs.localstack.cloud/references/coverage/coverage_glacier/)[Amazon S3 Glacier](https://docs.localstack.cloud/references/coverage/coverage_glacier/) | ❌ | ❌ | ✅ |
| [](https://docs.localstack.cloud/user-guide/aws/backup/)[AWS Backup](https://docs.localstack.cloud/user-guide/aws/backup/) | ❌ | ❌ | ✅ |
| [](https://docs.localstack.cloud/references/coverage/coverage_efs/)[Amazon EFS](https://docs.localstack.cloud/references/coverage/coverage_efs/) | ❌ | ❌ | ✅ |
| Emulator Enhancements |  |  |  |
| CI Credits | ❌ | ✅ 300 credits monthly per workspace | ✅ 1000 credits monthly per workspace |
| Stack Insights | ❌ | ✅ For all supported services | ✅ For all supported services |
| Local state persistence | ❌ | ✅ | ✅ |
| Cloud-based state persistence via Cloud pods | ❌ | ✅ 300 MB, lifetime per workspace | ✅ 3 GB, lifetime per workspace |
| Cloud Sandbox previews & ephemeral instances | ❌ | ✅ 100 minutes monthly per workspace | ✅ 500 minutes monthly per workspace |
| AWS Replicator | ❌ | ❌ | ✅ |
| IAM Policy Enforcement | ❌ | ✅ | ✅ |
| IAM Policy Streams | ❌ | ❌ | ✅ |
| Emulator Compliance Pack | ❌ | ❌ | ❌ |
| User Security Pack | ❌ | ❌ | ❌ |
| [Chaos Engineering](https://docs.localstack.cloud/user-guide/chaos-engineering/) | ❌ | ❌ | ✅ Add-on |
| [Kubernetes Executor](https://docs.localstack.cloud/user-guide/localstack-enterprise/kubernetes-executor/) | ❌ | ❌ | ✅ Add-on |
|  |  |  |  |
| [Support](https://docs.localstack.cloud/getting-started/help-and-support/) | Basic | Standard | Priority |

## Legacy Plans

As of **May 8, 2025**, the following plans are no longer available for new purchases.
If you're an existing customer on one of these tiers, your subscription remains active and unchanged.
You’ll continue receiving all regular version updates and will not experience any downgrade or loss of access.
If you have questions or concerns, please contact Support.

### Subscription Continuity

You may continue purchasing new licenses under your current legacy plan for the duration of your active subscription.
However, if your subscription lapses, we may not be able to restore access to these legacy plans.

### Legacy Plan Usage Allocations

**Starter:**

- 100 CI credits for the first 3 licenses
- +20 CI credits per additional license
- 240 CI credits maximum

**Teams:**

- 1000 CI credits for the first 3 licenses
- +200 CI credits per additional license
- 2400 CI credits maximum
- Includes workspace-wide Ephemeral Instance minutes and Cloud Pod storage

**Enterprise:**

- Unlimited CI credits
- Includes workspace-wide Ephemeral Instance minutes and Cloud Pod storage
- Detailed values for CI credits, minutes, and storage are shown in the table below

For any subscription or access-related questions, please reach out to Support.

| AWS Services | Legacy Plan: Starter | Legacy Plan: Teams | Legacy Plan: Enterprise sold before May 8th, 2025 |
| -------- | ------- | ------- | ------- |
| Analytics |  |  |  |
| [](https://docs.localstack.cloud/user-guide/aws/es/)[Amazon ElasticSearch](https://docs.localstack.cloud/user-guide/aws/es/) | ✅ | ✅ | ✅ |
| [](https://docs.localstack.cloud/references/coverage/coverage_kinesis/)[Amazon Kinesis Streams](https://docs.localstack.cloud/references/coverage/coverage_kinesis/) | ✅ | ✅ | ✅ |
| [](https://docs.localstack.cloud/references/coverage/coverage_firehose/)[Amazon Kinesis Data Firehose](https://docs.localstack.cloud/references/coverage/coverage_firehose/) | ✅ | ✅ | ✅ |
| [](https://docs.localstack.cloud/references/coverage/coverage_opensearch/)[Amazon OpenSearch](https://docs.localstack.cloud/references/coverage/coverage_opensearch/) | ✅ | ✅ | ✅ |
| [](https://docs.localstack.cloud/references/coverage/coverage_redshift/)[Amazon Redshift](https://docs.localstack.cloud/references/coverage/coverage_redshift/) | ✅ | ✅ | ✅ |
| [](https://docs.localstack.cloud/references/coverage/coverage_athena/)[Amazon Athena](https://docs.localstack.cloud/references/coverage/coverage_athena/) | ✅ | ✅ | ✅ |
| [](https://docs.localstack.cloud/references/coverage/coverage_emr/)[Amazon EMR](https://docs.localstack.cloud/references/coverage/coverage_emr/) | ✅ | ✅ | ✅ |
| [](https://docs.localstack.cloud/references/coverage/coverage_emr-serverless/)[Amazon EMR Serverless](https://docs.localstack.cloud/references/coverage/coverage_emr-serverless/) | ✅ | ✅ | ✅ |
| [](https://docs.localstack.cloud/references/coverage/coverage_glue/)[AWS Glue](https://docs.localstack.cloud/references/coverage/coverage_glue/) | ✅ | ✅ | ✅ |
| [](https://docs.localstack.cloud/references/coverage/coverage_redshift-data/)[Amazon Redshift Data API](https://docs.localstack.cloud/references/coverage/coverage_redshift-data/) | ✅ | ✅ | ✅ |
| [](https://docs.localstack.cloud/references/coverage/coverage_lakeformation/)[AWS Lake Formation](https://docs.localstack.cloud/references/coverage/coverage_lakeformation/) | ✅ | ✅ | ✅ |
| [](https://docs.localstack.cloud/user-guide/aws/msk/)[Amazon Managed Streaming for Apache Kafka](https://docs.localstack.cloud/user-guide/aws/msk/) | ✅ | ✅ | ✅ |
| [](https://docs.localstack.cloud/user-guide/aws/kinesisanalytics/)[Amazon Kinesis Data Analytics](https://docs.localstack.cloud/user-guide/aws/kinesisanalytics/) | ✅ | ✅ | ✅ |
| [](https://docs.localstack.cloud/user-guide/aws/kinesisanalyticsv2/)[Amazon Managed Service for Apache Flink](https://docs.localstack.cloud/user-guide/aws/kinesisanalyticsv2/) | ✅ | ✅ | ✅ |
| Application Integration |  |  |  |
| [](https://docs.localstack.cloud/user-guide/aws/swf/)[Amazon Simple Workflow Service (SWF)](https://docs.localstack.cloud/user-guide/aws/swf/) | ✅ | ✅ | ✅ |
| [](https://docs.localstack.cloud/user-guide/aws/sns/)[Amazon Simple Notification Service (SNS)](https://docs.localstack.cloud/user-guide/aws/sns/) | ✅ | ✅ | ✅ |
| [](https://docs.localstack.cloud/user-guide/aws/sqs/)[Amazon Simple Queue Service (SQS)](https://docs.localstack.cloud/user-guide/aws/sqs/) | ✅ | ✅ | ✅ |
| [](https://docs.localstack.cloud/user-guide/aws/stepfunctions/)[AWS Step Functions](https://docs.localstack.cloud/user-guide/aws/stepfunctions/) | ✅ | ✅ | ✅ |
| [](https://docs.localstack.cloud/user-guide/aws/events/)[Amazon EventBridge](https://docs.localstack.cloud/user-guide/aws/events/) | ✅ | ✅ | ✅ |
| [](https://docs.localstack.cloud/user-guide/aws/scheduler/)[Amazon EventBridge Scheduler](https://docs.localstack.cloud/user-guide/aws/scheduler/) | ✅ | ✅ | ✅ |
| [](https://docs.localstack.cloud/user-guide/aws/mq/)[Amazon MQ](https://docs.localstack.cloud/user-guide/aws/mq/) | ✅ | ✅ | ✅ |
| [](https://docs.localstack.cloud/user-guide/aws/pipes/)[Amazon EventBridge Pipes](https://docs.localstack.cloud/user-guide/aws/pipes/) | ✅ | ✅ | ✅ |
| [](https://docs.localstack.cloud/user-guide/aws/mwaa/)[Amazon Managed Workflows for Apache Airflow](https://docs.localstack.cloud/user-guide/aws/mwaa/) | ✅ | ✅ | ✅ |
| BlockChain |  |  |  |
| [](https://docs.localstack.cloud/user-guide/aws/managedblockchain/)[Amazon Managed Blockchain](https://docs.localstack.cloud/user-guide/aws/managedblockchain/) | ✅ | ✅ | ✅ |
| Business Applications |  |  |  |
| [](https://docs.localstack.cloud/user-guide/aws/ses/)[Amazon Simple Email Service (SES)](https://docs.localstack.cloud/user-guide/aws/ses/) | ✅ | ✅ | ✅ |
| [](https://docs.localstack.cloud/user-guide/aws/ses/)[Amazon Simple Email Service API V2 (SES)](https://docs.localstack.cloud/user-guide/aws/ses/) | ✅ | ✅ | ✅ |
| [](https://docs.localstack.cloud/user-guide/aws/pinpoint/)[Amazon Pinpoint](https://docs.localstack.cloud/user-guide/aws/pinpoint/) | ✅ | ✅ | ✅ |
| Cloud Financial Management |  |  |  |
| [](https://docs.localstack.cloud/user-guide/aws/ce/)[AWS Cost Explorer](https://docs.localstack.cloud/user-guide/aws/ce/) | ✅ | ✅ | ✅ |
| Compute |  |  |  |
| [](https://docs.localstack.cloud/user-guide/aws/ec2/)[Amazon Elastic Compute Cloud (EC2)](https://docs.localstack.cloud/user-guide/aws/ec2/) | ✅ | ✅ | ✅ |
| [](https://docs.localstack.cloud/user-guide/aws/lambda/)[AWS Lambda](https://docs.localstack.cloud/user-guide/aws/lambda/) | ✅ | ✅ | ✅ |
| [](https://docs.localstack.cloud/user-guide/aws/batch/)[AWS Batch](https://docs.localstack.cloud/user-guide/aws/batch/) | ✅ | ✅ | ✅ |
| [](https://docs.localstack.cloud/user-guide/aws/elasticbeanstalk/)[AWS Elastic Beanstalk](https://docs.localstack.cloud/user-guide/aws/elasticbeanstalk/) | ✅ | ✅ | ✅ |
| [](https://docs.localstack.cloud/user-guide/aws/serverlessrepo/)[AWS Serverless Application Repository](https://docs.localstack.cloud/user-guide/aws/serverlessrepo/) | ✅ | ✅ | ✅ |
| Containers |  |  |  |
| [](https://docs.localstack.cloud/user-guide/aws/ecr/)[Amazon Elastic Container Registry (ECR)](https://docs.localstack.cloud/user-guide/aws/ecr/) | ✅ | ✅ | ✅ |
| [](https://docs.localstack.cloud/user-guide/aws/ecr/)[Amazon Elastic Container Service (ECS)](https://docs.localstack.cloud/user-guide/aws/ecr/) | ✅ | ✅ | ✅ |
| [](https://docs.localstack.cloud/user-guide/aws/eks/)[Amazon Elastic Kubernetes Service (EKS)](https://docs.localstack.cloud/user-guide/aws/eks/) | ✅ | ✅ | ✅ |
| Customer Enablement |  |  |  |
| [](https://docs.localstack.cloud/user-guide/aws/support/)[AWS Support API](https://docs.localstack.cloud/user-guide/aws/support/) | ✅ | ✅ | ✅ |
| DataBases |  |  |  |
| [](https://docs.localstack.cloud/user-guide/aws/dynamodb/)[Amazon DynamoDB](https://docs.localstack.cloud/user-guide/aws/dynamodb/) | ✅ | ✅ | ✅ |
| [](https://docs.localstack.cloud/user-guide/aws/dynamodbstreams/)[Amazon DynamoDB Streams](https://docs.localstack.cloud/user-guide/aws/dynamodbstreams/) | ✅ | ✅ | ✅ |
| [](https://docs.localstack.cloud/user-guide/aws/elasticache/)[Amazon ElastiCache](https://docs.localstack.cloud/user-guide/aws/elasticache/) | ✅ | ✅ | ✅ |
| [](https://docs.localstack.cloud/user-guide/aws/rds/)[Amazon Relational Database Service (RDS)](https://docs.localstack.cloud/user-guide/aws/rds/) | ✅ | ✅ | ✅ |
| [](https://docs.localstack.cloud/references/coverage/coverage_rds-data/)[Amazon RDS Data API](https://docs.localstack.cloud/references/coverage/coverage_rds-data/) | ✅ | ✅ | ✅ |
| [](https://docs.localstack.cloud/user-guide/aws/docdb/)[Amazon DocumentDB](https://docs.localstack.cloud/user-guide/aws/docdb/) | ✅ | ✅ | ✅ |
| [](https://docs.localstack.cloud/user-guide/aws/memorydb/)[Amazon MemoryDB](https://docs.localstack.cloud/user-guide/aws/memorydb/) | ✅ | ✅ | ✅ |
| [](https://docs.localstack.cloud/user-guide/aws/neptune/)[Amazon Neptune](https://docs.localstack.cloud/user-guide/aws/neptune/) | ✅ | ✅ | ✅ |
| [](https://docs.localstack.cloud/user-guide/aws/timestream/)[Amazon Timestream](https://docs.localstack.cloud/user-guide/aws/timestream/) | ✅ | ✅ | ✅ |
| [](https://docs.localstack.cloud/user-guide/aws/qldb/)[Amazon Quantum Ledger Database (QLDB)](https://docs.localstack.cloud/user-guide/aws/qldb/) | ✅ | ✅ | ✅ |
| Developer Tools |  |  |  |
| [](https://docs.localstack.cloud/references/coverage/coverage_codecommit/)[AWS CodeCommit](https://docs.localstack.cloud/references/coverage/coverage_codecommit/) | ✅ | ✅ | ✅ |
| AWS CodeBuild | ✅ | ✅ | ✅ |
| AWS CodeConnections | ✅ | ✅ | ✅ |
| [](https://docs.localstack.cloud/user-guide/aws/fis/)[AWS Fault Injection Service](https://docs.localstack.cloud/user-guide/aws/fis/) | ❌ | ❌ | ✅ |
| AWS CodeDeploy | ✅ | ✅ | ✅ |
| AWS CodePipeline | ✅ | ✅ | ✅ |
| [](https://docs.localstack.cloud/user-guide/aws/xray/)[AWS X-Ray](https://docs.localstack.cloud/user-guide/aws/xray/) | ✅ | ✅ | ✅ |
| Frontend Web & Mobile Services |  |  |  |
| [](https://docs.localstack.cloud/user-guide/aws/amplify/)[AWS Amplify](https://docs.localstack.cloud/user-guide/aws/amplify/) | ✅ | ✅ | ✅ |
| [](https://docs.localstack.cloud/user-guide/aws/appsync/)[AWS AppSync](https://docs.localstack.cloud/user-guide/aws/appsync/) | ✅ | ✅ | ✅ |
| IoT |  |  |  |
| [](https://docs.localstack.cloud/user-guide/aws/iot/)[AWS IoT](https://docs.localstack.cloud/user-guide/aws/iot/) | ✅ | ✅ | ✅ |
| [](https://docs.localstack.cloud/user-guide/aws/iotwireless/)[AWS IoT Wireless](https://docs.localstack.cloud/user-guide/aws/iotwireless/) | ✅ | ✅ | ✅ |
| [](https://docs.localstack.cloud/user-guide/aws/iotanalytics/)[AWS IoT Analytics](https://docs.localstack.cloud/user-guide/aws/iotanalytics/) | ✅ | ✅ | ✅ |
| [](https://docs.localstack.cloud/user-guide/aws/iotdata/)[AWS IoT Data](https://docs.localstack.cloud/user-guide/aws/iotdata/) | ✅ | ✅ | ✅ |
| Management & Governance |  |  |  |
| [](https://docs.localstack.cloud/user-guide/aws/cloudformation/)[AWS CloudFormation](https://docs.localstack.cloud/user-guide/aws/cloudformation/) | ✅ | ✅ | ✅ |
| [](https://docs.localstack.cloud/user-guide/aws/cloudwatch/)[Amazon CloudWatch Metrics](https://docs.localstack.cloud/user-guide/aws/cloudwatch/) | ✅ | ✅ | ✅ |
| [](https://docs.localstack.cloud/user-guide/aws/logs/)[Amazon CloudWatch Logs](https://docs.localstack.cloud/user-guide/aws/logs/) | ✅ | ✅ | ✅ |
| [](https://docs.localstack.cloud/user-guide/aws/resource_groups/)[AWS Resource Groups](https://docs.localstack.cloud/user-guide/aws/resource_groups/) | ✅ | ✅ | ✅ |
| [](https://docs.localstack.cloud/references/coverage/coverage_ssm/)[AWS Systems Manager Parameter Store](https://docs.localstack.cloud/references/coverage/coverage_ssm/) | ✅ | ✅ | ✅ |
| [](https://docs.localstack.cloud/references/coverage/coverage_cloudcontrol/)[AWS Cloud Control](https://docs.localstack.cloud/references/coverage/coverage_cloudcontrol/) | ✅ | ✅ | ✅ |
| [](https://docs.localstack.cloud/references/coverage/coverage_application-autoscaling/)[AWS Application Auto Scaling](https://docs.localstack.cloud/references/coverage/coverage_application-autoscaling/) | ✅ | ✅ | ✅ |
| [](https://docs.localstack.cloud/references/coverage/coverage_autoscaling/)[Amazon EC2 Auto Scaling](https://docs.localstack.cloud/references/coverage/coverage_autoscaling/) | ✅ | ✅ | ✅ |
| [](https://docs.localstack.cloud/references/coverage/coverage_config/)[AWS Config](https://docs.localstack.cloud/references/coverage/coverage_config/) | ✅ | ✅ | ✅ |
| [](https://docs.localstack.cloud/references/coverage/coverage_appconfig/)[AWS AppConfig](https://docs.localstack.cloud/references/coverage/coverage_appconfig/) | ✅ | ✅ | ✅ |
| [](https://docs.localstack.cloud/references/coverage/coverage_cloudtrail/)[AWS CloudTrail](https://docs.localstack.cloud/references/coverage/coverage_cloudtrail/) | ✅ | ✅ | ✅ |
| [](https://docs.localstack.cloud/references/coverage/coverage_account/)[AWS Account Management](https://docs.localstack.cloud/references/coverage/coverage_account/) | ✅ | ✅ | ✅ |
| [](https://docs.localstack.cloud/references/coverage/coverage_organizations/)[AWS Organizations](https://docs.localstack.cloud/references/coverage/coverage_organizations/) | ✅ | ✅ | ✅ |
| Media |  |  |  |
| [](https://docs.localstack.cloud/references/coverage/coverage_elastictranscoder/)[Amazon Elastic Transcoder](https://docs.localstack.cloud/references/coverage/coverage_elastictranscoder/) | ✅ | ✅ | ✅ |
| [](https://docs.localstack.cloud/references/coverage/coverage_mediaconvert/)[AWS Elemental MediaConvert](https://docs.localstack.cloud/references/coverage/coverage_mediaconvert/) | ✅ | ✅ | ✅ |
| [](https://docs.localstack.cloud/references/coverage/coverage_mediastore/)[AWS Elemental MediaStore](https://docs.localstack.cloud/references/coverage/coverage_mediastore/) | ✅ | ✅ | ✅ |
| [](https://docs.localstack.cloud/references/coverage/coverage_mediastore-data/)[AWS Elemental MediaStore Data Plane](https://docs.localstack.cloud/references/coverage/coverage_mediastore-data/) | ✅ | ✅ | ✅ |
| Migration & Transfer |  |  |  |
| [](https://docs.localstack.cloud/references/coverage/coverage_transfer/)[AWS Transfer Family](https://docs.localstack.cloud/references/coverage/coverage_transfer/) | ✅ | ✅ | ✅ |
| [](https://docs.localstack.cloud/references/coverage/coverage_dms/)[AWS Database Migration Service](https://docs.localstack.cloud/references/coverage/coverage_dms/) | ✅ | ✅ | ✅ |
| Machine Learning |  |  |  |
| [](https://docs.localstack.cloud/references/coverage/coverage_transcribe/)[Amazon Transcribe](https://docs.localstack.cloud/references/coverage/coverage_transcribe/) | ✅ | ✅ | ✅ |
| [](https://docs.localstack.cloud/references/coverage/coverage_textract/)[Amazon Textract](https://docs.localstack.cloud/references/coverage/coverage_textract/) | ✅ | ✅ | ✅ |
| [](https://docs.localstack.cloud/references/coverage/coverage_sagemaker/)[Amazon SageMaker AI](https://docs.localstack.cloud/references/coverage/coverage_sagemaker/) | ✅ | ✅ | ✅ |
| [](https://docs.localstack.cloud/references/coverage/coverage_sagemaker-runtime/)[Amazon SageMaker Runtime](https://docs.localstack.cloud/references/coverage/coverage_sagemaker-runtime/) | ✅ | ✅ | ✅ |
| [](https://docs.localstack.cloud/references/coverage/coverage_bedrock/)[Amazon Bedrock](https://docs.localstack.cloud/references/coverage/coverage_bedrock/) | ❌ | ❌ | ✅ |
| [](https://docs.localstack.cloud/references/coverage/coverage_bedrock-runtime/)[Amazon Bedrock Runtime](https://docs.localstack.cloud/references/coverage/coverage_bedrock-runtime/) | ❌ | ❌ | ✅ |
| Networking & Content Delivery |  |  |  |
| [](https://docs.localstack.cloud/references/coverage/coverage_route53/)[Amazon Route 53](https://docs.localstack.cloud/references/coverage/coverage_route53/) | ✅ | ✅ | ✅ |
| [](https://docs.localstack.cloud/user-guide/aws/route53resolver/)[Amazon Route 53 Resolver](https://docs.localstack.cloud/user-guide/aws/route53resolver/) | ✅ | ✅ | ✅ |
| [](https://docs.localstack.cloud/references/coverage/coverage_apigateway/)[Amazon API Gateway REST API](https://docs.localstack.cloud/references/coverage/coverage_apigateway/) | ✅ | ✅ | ✅ |
| [](https://docs.localstack.cloud/references/coverage/coverage_apigatewayv2/)[Amazon API Gateway HTTP and WebSocket API](https://docs.localstack.cloud/references/coverage/coverage_apigatewayv2/) | ✅ | ✅ | ✅ |
| [](https://docs.localstack.cloud/references/coverage/coverage_apigatewaymanagementapi/)[Amazon API Gateway Management API](https://docs.localstack.cloud/references/coverage/coverage_apigatewaymanagementapi/) | ✅ | ✅ | ✅ |
| [](https://docs.localstack.cloud/references/coverage/coverage_elb/)[Elastic Load Balancing](https://docs.localstack.cloud/references/coverage/coverage_elb/) | ✅ | ✅ | ✅ |
| [](https://docs.localstack.cloud/references/coverage/coverage_elbv2/)[Elastic Load Balancing v2 (Application, Network)](https://docs.localstack.cloud/references/coverage/coverage_elbv2/) | ✅ | ✅ | ✅ |
| [](https://docs.localstack.cloud/references/coverage/coverage_cloudfront/)[Amazon CloudFront](https://docs.localstack.cloud/references/coverage/coverage_cloudfront/) | ✅ | ✅ | ✅ |
| [](https://docs.localstack.cloud/references/coverage/coverage_servicediscovery/)[AWS Cloud Map](https://docs.localstack.cloud/references/coverage/coverage_servicediscovery/) | ✅ | ✅ | ✅ |
| Security, Identity & Compliance |  |  |  |
| [](https://docs.localstack.cloud/references/coverage/coverage_kms/)[AWS Key Management Service (KMS)](https://docs.localstack.cloud/references/coverage/coverage_kms/) | ✅ | ✅ | ✅ |
| [](https://docs.localstack.cloud/references/coverage/coverage_secretsmanager/)[AWS Secrets Manager](https://docs.localstack.cloud/references/coverage/coverage_secretsmanager/) | ✅ | ✅ | ✅ |
| [](https://docs.localstack.cloud/references/coverage/coverage_sts/)[AWS Security Token Service](https://docs.localstack.cloud/references/coverage/coverage_sts/) | ✅ | ✅ | ✅ |
| [](https://docs.localstack.cloud/references/coverage/coverage_acm/)[AWS Certificate Manager](https://docs.localstack.cloud/references/coverage/coverage_acm/) | ✅ | ✅ | ✅ |
| [](https://docs.localstack.cloud/references/coverage/coverage_cognito-identity/)[Amazon Cognito Identity Pools](https://docs.localstack.cloud/references/coverage/coverage_cognito-identity/) | ✅ | ✅ | ✅ |
| [](https://docs.localstack.cloud/references/coverage/coverage_cognito-idp/)[Amazon Cognito User Pools](https://docs.localstack.cloud/references/coverage/coverage_cognito-idp/) | ✅ | ✅ | ✅ |
| [](https://docs.localstack.cloud/references/coverage/coverage_acm-pca/)[AWS Private Certificate Authority](https://docs.localstack.cloud/references/coverage/coverage_acm-pca/) | ✅ | ✅ | ✅ |
| [](https://docs.localstack.cloud/references/coverage/coverage_wafv2/)[AWS Web Application Firewall (WAF)](https://docs.localstack.cloud/references/coverage/coverage_wafv2/) | ✅ | ✅ | ✅ |
| [](https://docs.localstack.cloud/references/coverage/coverage_iam/)[AWS Identity and Access Management (IAM)](https://docs.localstack.cloud/references/coverage/coverage_iam/) | ✅ | ✅ | ✅ |
| [](https://docs.localstack.cloud/references/coverage/coverage_identitystore/)[AWS IAM Identity Store API](https://docs.localstack.cloud/references/coverage/coverage_identitystore/) | ✅ | ✅ | ✅ |
| [](https://docs.localstack.cloud/references/coverage/coverage_sso-admin/)[AWS IAM Identity Center](https://docs.localstack.cloud/references/coverage/coverage_sso-admin/) | ✅ | ✅ | ✅ |
| [](https://docs.localstack.cloud/references/coverage/coverage_ram/)[AWS Resource Access Manager (RAM)](https://docs.localstack.cloud/references/coverage/coverage_ram/) | ✅ | ✅ | ✅ |
| [](https://docs.localstack.cloud/references/coverage/coverage_shield/)[AWS Shield](https://docs.localstack.cloud/references/coverage/coverage_shield/) | ✅ | ✅ | ✅ |
| Storage |  |  |  |
| [](https://docs.localstack.cloud/references/coverage/coverage_s3/)[Amazon S3](https://docs.localstack.cloud/references/coverage/coverage_s3/) | ✅ | ✅ | ✅ |
| [](https://docs.localstack.cloud/references/coverage/coverage_s3control/)[Amazon S3 Control](https://docs.localstack.cloud/references/coverage/coverage_s3control/) | ✅ | ✅ | ✅ |
| [](https://docs.localstack.cloud/references/coverage/coverage_glacier/)[Amazon S3 Glacier](https://docs.localstack.cloud/references/coverage/coverage_glacier/) | ✅ | ✅ | ✅ |
| [](https://docs.localstack.cloud/user-guide/aws/backup/)[AWS Backup](https://docs.localstack.cloud/user-guide/aws/backup/) | ✅ | ✅ | ✅ |
| [](https://docs.localstack.cloud/references/coverage/coverage_efs/)[Amazon EFS](https://docs.localstack.cloud/references/coverage/coverage_efs/) | ✅ | ✅ | ✅ |
| Emulator Enhancements |  |  |  |
| CI Credits | ✅ Up to 240 credits monthly per workspace | ✅ Up to 2400 credits monthly per workspace | Unlimited |
| Stack Insights | ✅ For all supported services | ✅ For all supported services | ✅ For all supported services |
| Local state persistence | ✅ | ✅ | ✅ |
| Cloud-based state persistence via Cloud pods | ✅ 500 MB, lifetime per license | ✅ 1 GB, lifetime per license | ✅ 5 GB lifetime, per license |
| Application previews via Ephemeral Instances | ❌ | ✅ 1000 minutes monthly per workspace | ✅ 3000 minutes monthly per workspace |
| AWS Replicator | ❌ | ✅ | ✅ |
| IAM Policy Enforcement | ❌ | ❌ | ✅ |
| IAM Policy Streams | ❌ | ❌ | ✅ |
| Emulator Compliance Pack | ❌ | ❌ | ✅ |
| User Security Pack | ❌ | ❌ | ✅ |
| [Chaos Engineering](https://docs.localstack.cloud/user-guide/chaos-engineering/) | ❌ | ❌ | ✅ |
| [Kubernetes Pack](https://docs.localstack.cloud/user-guide/localstack-enterprise/kubernetes-executor/) | ❌ | ❌ | ✅ |
|  |  |  |  |
| [Support](https://docs.localstack.cloud/getting-started/help-and-support/) | Standard | Priority | Enterprise |
