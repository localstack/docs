---
title: "Pricing Coverage"
linkTitle: "Pricing Coverage"
weight: 14
description: >
    This page lists the pricing coverage for the various features provided by the LocalStack platform.
cascade:
  type: docs
---

## AWS services

| Service                                     | Community image | Pro image |
| ------------------------------------------- | --------------- | --------- |
| Account Management                          |                 | ✅        |
| Amplify                                     |                 | ✅        |
| API Gateway                                 | ✅              | ✅        |
| AppConfig                                   |                 | ✅        |
| Application Auto Scaling                    |                 | ✅        |
| AppSync                                     |                 | ✅        |
| Athena                                      |                 | ✅        |
| Backup                                      |                 | ✅        |
| Batch                                       |                 | ✅        |
| Certificate Manager (ACM)                   | ✅              | ✅        |
| CloudFormation                              | ✅              | ✅        |
| CloudFront                                  |                 | ✅        |
| CloudTrail                                  |                 | ✅        |
| CloudWatch                                  | ✅              | ✅        |
| CloudWatch Logs                             | ✅              | ✅        |
| CodeCommit                                  |                 | ✅        |
| Cognito                                     |                 | ✅        |
| Config                                      | ✅              | ✅        |
| Cost Explorer                               |                 | ✅        |
| Database Migration Service (DMS)            |                 | ✅        |
| DocumentDB (DocDB)                          |                 | ✅        |
| DynamoDB                                    | ✅              | ✅        |
| Elastic Beanstalk                           |                 | ✅        |
| Elastic Compute Cloud (EC2)                 | ✅              | ✅        |
| Elastic Container Registry (ECR)            |                 | ✅        |
| Elastic Container Service (ECS)             |                 | ✅        |
| Elastic File System (EFS)                   |                 | ✅        |
| Elastic Kubernetes Service (EKS)            |                 | ✅        |
| Elastic Load Balancing (ELB)                |                 | ✅        |
| Elastic MapReduce (EMR)                     |                 | ✅        |
| Elastic Transcoder                          |                 | ✅        |
| ElastiCache                                 |                 | ✅        |
| Elasticsearch Service                       |                 | ✅        |
| Elemental MediaStore                        |                 | ✅        |
| EventBridge                                 | ✅              | ✅        |
| EventBridge Pipes                           |                 | ✅        |
| Fault Injection Simulator (FIS)             |                 | ✅        |
| Glacier                                     |                 | ✅        |
| Glue                                        |                 | ✅        |
| Identity and Access Management (IAM)        | ✅              | ✅        |
| Identity Store                              |                 | ✅        |
| IoT                                         |                 | ✅        |
| Key Management Service (KMS)                | ✅              | ✅        |
| Kinesis                                     | ✅              | ✅        |
| Kinesis Data Analytics                      |                 | ✅        |
| Kinesis Data Firehose                       | ✅              | ✅        |
| Lambda                                      | ✅              | ✅        |
| Managed Blockchain (AMB)                    |                 | ✅        |
| Managed Streaming for Kafka (MSK)           |                 | ✅        |
| Managed Workflows for Apache Airflow (MWAA) |                 | ✅        |
| MemoryDB for Redis                          |                 | ✅        |
| MQ                                          |                 | ✅        |
| Neptune                                     |                 | ✅        |
| OpenSearch Service                          | ✅              | ✅        |
| Organizations                               |                 | ✅        |
| Pinpoint                                    |                 | ✅        |
| Private Certificate Authority (ACM PCA)     |                 | ✅        |
| Quantum Ledger Database (QLDB)              |                 | ✅        |
| Redshift                                    |                 | ✅        |
| Relational Database Service (RDS)           |                 | ✅        |
| Resource Access Manager (RAM)               |                 | ✅        |
| Resource Groups                             | ✅              | ✅        |
| Route 53                                    | ✅              | ✅        |
| Route 53 Resolver                           | ✅              | ✅        |
| SageMaker                                   |                 | ✅        |
| Secrets Manager                             | ✅              | ✅        |
| Security Token Service (STS)                | ✅              | ✅        |
| Serverless Application Repository           |                 | ✅        |
| Service Discovery                           |                 | ✅        |
| Simple Email Service (SES)                  | ✅              | ✅        |
| Simple Notification Service (SNS)           | ✅              | ✅        |
| Simple Queue Service (SQS)                  | ✅              | ✅        |
| Simple Storage Service (S3)                 | ✅              | ✅        |
| Simple Workflow Service (SWF)               | ✅              | ✅        |
| Step Functions                              | ✅              | ✅        |
| Support                                     | ✅              | ✅        |
| Systems Manager (SSM)                       | ✅              | ✅        |
| Textract                                    |                 | ✅        |
| Timestream                                  |                 | ✅        |
| Transcribe                                  | ✅              | ✅        |
| Transfer                                    |                 | ✅        |
| Web Application Firewall (WAF)              |                 | ✅        |
| X-Ray                                       |                 | ✅        |

### Notes:

- Lambda Layers are not available in the community image.
- CloudWatch Logs filter patterns are not available in the community image.
- API Gateway v2 and SES v2 are not available in the community image.
- Running EC2 instances with Docker or a libvirt backend is not available in the community image.
- CloudFormation in the community image only supports services included in the community image.

## LocalStack features
| Features                       | Community | Starter | Teams | Enterprise |
| ------------------------------ | --------- | ------- | ----- | ---------- |
| Chaos Engineering              |           |         |       | ✅         |
| CI Analytics \*                |           |         |       | ✅         |
| Cloud Pods storage             |           |         | ✅    | ✅         |
| Desktop Application            | ✅        | ✅      | ✅    | ✅         |
| Ephemeral Instances \*         |           |         | ✅    | ✅         |
| Extensions                     |           | ✅      | ✅    | ✅         |
| IAM Enforcement                |           | ✅      | ✅    | ✅         |
| IAM Policy Stream              |           | ✅      | ✅    | ✅         |
| LocalStack on Kubernetes       |           |         |       | ✅         |
| Offline image                  |           |         |       | ✅         |
| Persistence                    |           | ✅      | ✅    | ✅         |
| Resource Browsers              | ✅        | ✅      | ✅    | ✅         |
| SSO Support                    |           |         |       | ✅         |
| Stack Insights                 |           |         | ✅    | ✅         |
| State Import/Export            |           | ✅      | ✅    | ✅         |
| Transparent Endpoint Injection |           | ✅      | ✅    | ✅         |

### Notes

- Resource Browsers for community users are limited to the services available in the community version.
- Features marked with `*` are available in a private preview. Request access to use them.

## LocalStack services

| Support Channels                                                                 | Community | Starter | Teams | Enterprise |
| -------------------------------------------------------------------------------- | --------- | ------- | ----- | ---------- |
| Community Support by other LocalStack users in our LocalStack Community Channels | ✅        | ✅      | ✅    | ✅         |
| Best effort support by LocalStack engineers through LocalStack Community Slack   |           | ✅      | ✅    | ✅         |
| Prioritized best effort support by LocalStack engineers through Community Slack  |           |         | ✅    | ✅         |
| Enterprise Support via Ticketing System                                          |           |         |       | ✅         |
| Highest prioritization and SLAs                                                  |           |         |       | ✅         |
| Dedicated Technical Account Manager and Customer Success Point of Contact        |           |         |       | ✅         |
| Prioritization of critical feature requests in the LocalStack Product Roadmap    |           |         |       | ✅         |
