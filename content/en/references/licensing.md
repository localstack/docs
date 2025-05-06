---
title: LocalStack for AWS Licenses"
linkTitle: "LocalStack for AWS Licenses"
weight: 200
description: >
  Details on the packaging and service support across LocalStack tiers.
---

**This document outlines the emulated services and enhancements provided under each LocalStack for AWS tier and their respective licenses.** It is intended to clarify the available features and functionality purchased, and ensure compliance with licensing terms.

As of May 8th, 2025 there are four tiers available for purchase for **LocalStack for AWS**; Free, Base, Ultimate, and Enterprise. Please note, Enterprise licensing is custom serviced to qualified customer needs and only available via sales, therefore it is not further detailed below.

[Purchased before May 8th, 2025 - click here to learn more.](#legacy-plans)

More information on the intended audience of each tier may be found on our [pricing page](https://www.localstack.cloud/pricing). 

In order to access the functionality of an available tier, a license for that tier must be purchased and assigned to a user. This assigns an authentication token to the user that enables access to the emulator and its enhancements. At this time, self-servicing customers may only purchase licenses to one tier per workspace, meaning a single workspace may not have both Base and Ultimate licenses. For more information or questions on flexibility of licensing tied to your unique needs, please contact sales. 

Each workspace is allotted a monthly amount of CI credits and Ephemeral Instance minutes to use across all licensed users, and a set amount of Cloud Pod storage to be leveraged across the entire workspace for the lifetime of the contract. To provide flexibility, we will be enabling self-servicing purchasing of additional credits, minutes, and storage in the coming weeks. If you have immediate needs to expand usage, please contact sales for assistance. 

{{< callout "note" >}}
If you purchased LocalStack before May 8th, 2025 and had an active subscription before then, you may access information on your available features and functionality here.
{{</ callout >}}

Please note, this table is only representative of whether an emulated AWS service is accessible in a given tier, NOT the level of coverage. To learn more about the coverage of each service, please visit that service’s detailed tech document that is linked in the table below, or reach out to support. 

|  | Free | Base | Ultimate |
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
| Application previews via Ephemeral Instances | ❌ | ✅ 100 minutes monthly per workspace | ✅ 500 minutes monthly per workspace |
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

As of May 8th, 2025, we are no longer offering these following tiers and licenses to new customers. If you are an existing customer on these tiers, your subscription is unaffected by this change. We are not making changes to your subscription nor regressing your LocalStack for AWS experience in any way, and you will continue to benefit from our regular version releases. If you have any concerns or questions, please reach out to support. 

You may continue to purchase new licenses tied to your tier throughout the duration of your subscription. Please note, that a lapse in an active subscription may result in our inability to grant you access to these legacy plans again. 

Each workspace is allotted a maximum monthly amount of CI credits tied to the number of users on the account. For users on Starter, we provide a base of 100 credits for the first three licenses and an additional 20 credits for each additional license up to 240 total credits. In Teams, we provide a base of 1000 credits for the first three licenses and an additional 200 credits for each additional license up to 2400 total credits. There are unlimited CI credits in Enterprise. Additionally, in Teams and Enterprise, there is a monthly set amount of Ephemeral Instance minutes for the entire workspace as detailed in the table below, along with there is a set amount of Cloud Pod storage for each license. 

For any questions, please reach out to support. 

|  | Legacy Plan: Starter | Legacy Plan: Teams | Legacy Plan: Enterprise sold before May 8th, 2025 |
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
| Application previews via Ephemeral Instances | ❌ | ✅ 1000 minutes monrhtly per workspace | ✅ 3000 minutes monrhtly per workspace |
| AWS Replicator | ❌ | ✅ | ✅ |
| IAM Policy Enforcement | ❌ | ❌ | ✅ |
| IAM Policy Streams | ❌ | ❌ | ✅ |
| Emulator Compliance Pack | ❌ | ❌ | ✅ |
| User Security Pack | ❌ | ❌ | ✅ |
| [Chaos Engineering](https://docs.localstack.cloud/user-guide/chaos-engineering/) | ❌ | ❌ | ✅ |
| [Kubernetes Executor](https://docs.localstack.cloud/user-guide/localstack-enterprise/kubernetes-executor/) | ❌ | ❌ | ✅ |
|  |  |  |  |
| [Support](https://docs.localstack.cloud/getting-started/help-and-support/) | Standard | Priority | Enterprise |