---
title: "AWS Service Feature Coverage"
linkTitle: "⭐ Feature Coverage"
weight: 1
description: >
  Overview of the implemented APIs and features provided by LocalStack
---

This page summarizes the implemented APIs and features provided by LocalStack, as well as their level of parity with the real cloud (e.g., AWS) or managed service provider.

## Coverage Levels / Support Tiers

LocalStack provides a variety of different features and cloud APIs (e.g., AWS), but the level of support and parity with the real system differs for the different services:

* **Tier 1 (⭐⭐⭐⭐)**: Feature fully supported by LocalStack maintainers; feature is guaranteed to pass all or the majority of tests
* **Tier 2 (⭐⭐⭐)**: Feature supports the majority of use cases (e.g., CRUD operations), but some advanced usages may not be fully supported
* **Tier 3 (⭐⭐)**: Feature may be lightly tested (or not), and so it should be considered unstable
* **Tier 4 (⭐)**: Feature is experimental, only partially supported or implemented
* **Tier 5 (-)**: Feature is not currently implemented, but on our roadmap

In the coverage tables below, the features are marked with their respective availability across different LocalStack versions:

* Community version (default, if not marked)
* Pro version (marked with "Pro")
* Enterprise version (marked with "Enterprise")

## AWS Feature Coverage

| Service / Feature                                       | Coverage Level | Terraform Tests | Notes |
|---------------------------------------------------------|----------------|-----------------|-------|
| **ACM**                                                 |                |                 |       |
| Certificates                                            | ⭐⭐⭐         |                 |       |
| Tags                                                    | ⭐⭐⭐⭐       |                 |       |
| Account Configuration                                   | ⭐⭐           |                 |       |
| [**Amplify** (Pro)](../amplify)                         |                |                 |       |
| Apps                                                    | ⭐⭐⭐         |                 |       |
| Backend Environments                                    | ⭐⭐           |                 |       |
| Branches                                                | ⭐⭐           |                 |       |
| Deployments                                             | ⭐⭐⭐         |                 |       |
| Domain Associations                                     | \-             |                 |       |
| Jobs                                                    | ⭐⭐           |                 |       |
| Tags                                                    | ⭐⭐⭐⭐       |                 |       |
| Webhooks                                                | ⭐⭐           |                 |       |
| **API Gateway**                                         |                |                 |       |
| API Keys                                                | ⭐⭐⭐         |                 |       |
| Authorizers (Pro)                                       | ⭐⭐⭐⭐       |                 |       |
| Base Path Mappings                                      | ⭐⭐⭐⭐       |                 |       |
| Deployments                                             | ⭐⭐⭐⭐       |                 |       |
| Documentation Parts                                     | ⭐⭐⭐         |                 |       |
| Documentation Versions                                  | ⭐⭐⭐         |                 |       |
| Domain Names                                            | ⭐⭐⭐         |                 |       |
| Gateway / Integration / Method Responses                | ⭐⭐⭐⭐       |                 |       |
| Integrations                                            | ⭐⭐⭐⭐       |                 |       |
| Methods                                                 | ⭐⭐⭐⭐       |                 |       |
| Models                                                  | ⭐⭐⭐         |                 |       |
| Request Validators                                      | ⭐⭐           |                 |       |
| Resources                                               | ⭐⭐⭐⭐       |                 |       |
| REST APIs                                               | ⭐⭐⭐⭐       |                 |       |
| Stages                                                  | ⭐⭐⭐⭐       |                 |       |
| Tags                                                    | ⭐⭐⭐⭐       |                 |       |
| Usage Plans                                             | ⭐⭐⭐         |                 |       |
| Usage Plan Keys                                         | ⭐⭐⭐         |                 |       |
| VPC Links                                               | ⭐⭐⭐         |                 |       |
| [**API Gateway v2** (Pro)](../apigatewayv2)             |                |                 |       |
| APIs                                                    | ⭐⭐⭐⭐       |                 |       |
| API Mappings                                            | ⭐⭐⭐         |                 |       |
| Authorizers                                             | ⭐⭐⭐⭐       |                 |       |
| Deployments                                             | ⭐⭐⭐⭐       |                 |       |
| Domain Names                                            | ⭐⭐⭐         |                 |       |
| Import APIs from OpenAPI specs                          | ⭐⭐⭐         |                 |       |
| Integrations                                            | ⭐⭐⭐         |                 |       |
| Integration Responses                                   | ⭐⭐⭐         |                 |       |
| Models                                                  | ⭐⭐⭐         |                 |       |
| Routes                                                  | ⭐⭐⭐⭐       |                 |       |
| Route Responses                                         | ⭐⭐⭐         |                 |       |
| Stages                                                  | ⭐⭐⭐⭐       |                 |       |
| Tags                                                    | ⭐⭐⭐⭐       |                 |       |
| VPC Links                                               | ⭐⭐⭐         |                 |       |
| **AppConfig** (Pro)                                     |                |                 |       |
| Applications                                            | ⭐⭐⭐         |                 |       |
| Configuration Profiles                                  | ⭐⭐⭐⭐       |                 |       |
| Configurations                                          | ⭐⭐⭐         |                 |       |
| Deployment Strategies                                   | ⭐⭐⭐⭐       |                 |       |
| Deployments                                             | ⭐⭐⭐         |                 |       |
| Environments                                            | ⭐⭐⭐⭐       |                 |       |
| Hosted Configuration Versions                           | ⭐⭐⭐         |                 |       |
| Tags                                                    | ⭐⭐⭐⭐       |                 |       |
| **Application Autoscaling** (Pro)                       |                |                 |       |
| Scalable Targets                                        | ⭐⭐⭐         |                 |       |
| Scaling Activities                                      | ⭐⭐           |                 |       |
| Scaling Policies                                        | ⭐⭐           |                 |       |
| Scheduled Actions                                       | ⭐⭐           |                 |       |
| [**AppSync** (Pro)](../appsync)                         |                |                 |       |
| API Caches                                              | ⭐⭐⭐         |                 |       |
| API Keys                                                | ⭐⭐⭐         |                 |       |
| Data Sources                                            | ⭐⭐⭐         |                 |       |
| Functions                                               | ⭐⭐⭐         |                 |       |
| GraphQL APIs                                            | ⭐⭐⭐⭐       |                 |       |
| Resolvers                                               | ⭐⭐⭐⭐       |                 |       |
| Tags                                                    | ⭐⭐⭐⭐       |                 |       |
| Types                                                   | ⭐⭐⭐⭐       |                 |       |
| [**Athena** (Pro)](../athena)                           |                |                 |       |
| Data Catalogs                                           | ⭐⭐           |                 |       |
| Databases                                               | ⭐⭐           |                 |       |
| Named Queries                                           | \-             |                 |       |
| Prepared Statements                                     | ⭐⭐⭐         |                 |       |
| Query Executions                                        | ⭐⭐⭐         |                 |       |
| Table Metadata                                          | ⭐⭐           |                 |       |
| Tags                                                    | ⭐⭐⭐⭐       |                 |       |
| Work Groups                                             | \-             |                 |       |
| [**Backup** (Pro)](../backup)                           |                |                 |       |
| Backup Jobs                                             | ⭐⭐⭐         |                 |       |
| Backup Plans                                            | ⭐⭐⭐         |                 |       |
| Backup Selections                                       | ⭐⭐⭐         |                 |       |
| Backup Vaults                                           | ⭐⭐⭐         |                 |       |
| Backup Vault Access Policies                            | \-             |                 |       |
| Backup Vault Notifications                              | \-             |                 |       |
| Global Settings                                         | \-             |                 |       |
| Protected Resources                                     | \-             |                 |       |
| Recovery Points                                         | ⭐⭐⭐         |                 |       |
| Tags                                                    | \-             |                 |       |
| **Batch** (Pro)                                         |                |                 |       |
| Compute Environments                                    | ⭐⭐⭐         |                 |       |
| Job Queues                                              | ⭐⭐⭐         |                 |       |
| Job Definitions                                         | ⭐⭐⭐         |                 |       |
| Jobs                                                    | ⭐⭐⭐         |                 |       |
| Tags                                                    | ⭐⭐⭐⭐       |                 |       |
| **CloudFormation**                                      |                |                 |       |
| Change Sets                                             | ⭐⭐⭐⭐       |                 |       |
| Stacks                                                  | ⭐⭐⭐⭐       |                 |       |
| Stack Drifts                                            | \-             |                 |       |
| Stack Events                                            | ⭐⭐⭐⭐       |                 |       |
| Stack Instances                                         | ⭐⭐⭐⭐       |                 |       |
| Stack Policies                                          | ⭐⭐⭐         |                 |       |
| Stack Resources                                         | ⭐⭐⭐⭐       |                 |       |
| Stack Sets                                              | ⭐⭐⭐⭐       |                 |       |
| Publishers                                              | \-             |                 |       |
| Templates                                               | ⭐⭐⭐⭐       |                 |       |
| Type Activations                                        | ⭐⭐           |                 |       |
| [**CloudFront** (Pro)](../cloudfront)                   |                |                 |       |
| Cache Policies                                          | \-             |                 |       |
| Distributions                                           | ⭐⭐⭐         |                 |       |
| Field Level Encryption                                  | \-             |                 |       |
| Functions                                               | ⭐⭐⭐         |                 |       |
| Invalidations                                           | ⭐⭐⭐         |                 |       |
| Key Groups                                              | \-             |                 |       |
| Monitoring Subscriptions                                | \-             |                 |       |
| Origin Access Identities                                | ⭐⭐           |                 |       |
| Origin Request Policies                                 | ⭐⭐⭐         |                 |       |
| Public Keys                                             | \-             |                 |       |
| Realtime Log Configs                                    | \-             |                 |       |
| Streaming Distributions                                 | \-             |                 |       |
| Tags                                                    | ⭐⭐⭐⭐       |                 |       |
| **CloudTrail** (Pro)                                    |                |                 |       |
| Event Selectors                                         | ⭐⭐⭐         |                 |       |
| Insight Selectors                                       | \-             |                 |       |
| Tags                                                    | ⭐⭐⭐⭐       |                 |       |
| Trails                                                  | ⭐⭐⭐         |                 |       |
| Start/Stop Logging                                      | ⭐⭐⭐         |                 |       |
| **CloudWatch**                                          |                |                 |       |
| Alarms                                                  | ⭐⭐           |                 |       |
| Alarm Histories                                         | \-             |                 |       |
| Anomaly Detectors                                       | \-             |                 |       |
| Dashboards                                              | \-             |                 |       |
| Insight Rules                                           | \-             |                 |       |
| Metric Data                                             | ⭐⭐⭐⭐       |                 |       |
| Metric Statistics                                       | ⭐⭐⭐         |                 |       |
| Metric Streams                                          | \-             |                 |       |
| Tags                                                    | ⭐⭐⭐         |                 |       |
| **CloudWatch Logs**                                     |                |                 |       |
| Destinations                                            | ⭐⭐⭐⭐       |                 |       |
| Export Tasks                                            | ⭐⭐           |                 |       |
| Log Events                                              | ⭐⭐⭐⭐       |                 |       |
| Log Groups                                              | ⭐⭐⭐⭐       |                 |       |
| Log Streams                                             | ⭐⭐⭐⭐       |                 |       |
| Metric Filters                                          | ⭐⭐⭐         |                 |       |
| Queries                                                 | ⭐⭐⭐         |                 |       |
| Query Definitions                                       | ⭐⭐           |                 |       |
| Resource Policies                                       | ⭐⭐⭐⭐       |                 |       |
| Retention Policies                                      | ⭐⭐⭐         |                 |       |
| Subscription Filters                                    | ⭐⭐⭐         |                 |       |
| Tags                                                    | ⭐⭐⭐⭐       |                 |       |
| [**CodeCommit** (Pro)](../codecommit)                   |                |                 |       |
| Approval Rules                                          | \-             |                 |       |
| Blobs / Files / Folders                                 | ⭐⭐           |                 |       |
| Branches                                                | ⭐⭐           |                 |       |
| Comments                                                | \-             |                 |       |
| Commits                                                 | ⭐⭐           |                 |       |
| Merge Commits / Conflicts                               | \-             |                 |       |
| Pull Requests                                           | \-             |                 |       |
| Repositories                                            | ⭐⭐⭐         |                 |       |
| Tags                                                    | ⭐⭐⭐⭐       |                 |       |
| [**Cognito Identity** (Pro)](../cognito)                |                |                 |       |
| Developer Identities                                    | \-             |                 |       |
| Identities                                              | ⭐⭐⭐         |                 |       |
| Identity Pool Roles                                     | \-             |                 |       |
| Identity Pools                                          | ⭐⭐⭐⭐       |                 |       |
| OpenID Tokens                                           | \-             |                 |       |
| Tags                                                    | \-             |                 |       |
| [**Cognito Identity Provider (IdP)** (Pro)](../cognito) |                |                 |       |
| Admin APIs                                              | ⭐⭐⭐         |                 |       |
| Devices                                                 | ⭐⭐           |                 |       |
| Auth Flows                                              | ⭐⭐⭐         |                 |       |
| Groups                                                  | ⭐⭐⭐⭐       |                 |       |
| Lambda Triggers                                         | ⭐⭐⭐⭐       |                 |       |
| MFA Configs                                             | ⭐⭐⭐         |                 |       |
| Resource Servers                                        | \-             |                 |       |
| Risk Configurations                                     | \-             |                 |       |
| Identity Providers                                      | ⭐⭐⭐         |                 |       |
| User Import Jobs                                        | \-             |                 |       |
| User Pool Clients                                       | ⭐⭐⭐⭐       |                 |       |
| User Pool Domains                                       | ⭐⭐           |                 |       |
| User Pools                                              | ⭐⭐⭐⭐       |                 |       |
| Users                                                   | ⭐⭐⭐⭐       |                 |       |
| Tags                                                    | ⭐⭐⭐⭐       |                 |       |
| **DynamoDB**                                            |                |                 |       |
| Backups (Pro)                                           | ⭐⭐⭐⭐       |                 |       |
| Batch Operations                                        | ⭐⭐⭐⭐       |                 |       |
| Global Tables                                           | ⭐⭐⭐⭐       |                 |       |
| Items                                                   | ⭐⭐⭐⭐       |                 |       |
| Kinesis Streaming Destinations                          | \-             |                 |       |
| PartiQL Queries                                         | ⭐⭐⭐⭐       |                 |       |
| Query / Scan Operations                                 | ⭐⭐⭐⭐       |                 |       |
| Tables                                                  | ⭐⭐⭐⭐       |                 |       |
| Table Replica Autoscaling                               | \-             |                 |       |
| Tags                                                    | ⭐⭐⭐⭐       |                 |       |
| **DynamoDB Streams**                                    |                |                 |       |
| Records                                                 | ⭐⭐⭐⭐       |                 |       |
| Shard Iterators                                         | ⭐⭐⭐⭐       |                 |       |
| Streams                                                 | ⭐⭐⭐⭐       |                 |       |
| **EC2**                                                 |                |                 |       |
| Classic Links                                           | ⭐⭐⭐         |                 |       |
| Customer Gateways                                       | ⭐⭐⭐         |                 |       |
| DHCP Options                                            | ⭐⭐⭐         |                 |       |
| Allocate/Deallocate Elastic IPs                         | ⭐⭐⭐         |                 |       |
| Fleets                                                  | ⭐⭐           |                 |       |
| Flow Logs                                               | ⭐⭐⭐         |                 |       |
| Images                                                  | ⭐⭐           |                 |       |
| Internet Gateways                                       | ⭐⭐⭐         |                 |       |
| Local Gateway Routes                                    | ⭐⭐⭐         |                 |       |
| Key Pairs                                               | ⭐⭐⭐⭐       |                 |       |
| Launch Templates                                        | ⭐⭐⭐         |                 |       |
| NAT Gateways                                            | ⭐⭐⭐         |                 |       |
| Network ACLs                                            | ⭐⭐⭐         |                 |       |
| Network Interfaces                                      | ⭐⭐⭐         |                 |       |
| Reserved Instances                                      | ⭐⭐⭐         |                 |       |
| Route Tables / Routes                                   | ⭐⭐⭐         |                 |       |
| Scheduled Instances                                     | ⭐⭐⭐         |                 |       |
| Security Groups / Egress / Ingress                      | ⭐⭐⭐⭐       |                 |       |
| Snapshots                                               | ⭐⭐⭐         |                 |       |
| Spot Instances                                          | ⭐⭐⭐         |                 |       |
| Start Instances as VMs (Pro)                            | ⭐⭐           |                 |       |
| Subnets                                                 | ⭐⭐⭐         |                 |       |
| Tags                                                    | ⭐⭐⭐⭐       |                 |       |
| Traffic Mirrors                                         | ⭐⭐⭐         |                 |       |
| Transit Gateways                                        | ⭐⭐⭐         |                 |       |
| Volumes                                                 | ⭐⭐⭐         |                 |       |
| VPC Endpoint Connections                                | ⭐⭐⭐         |                 |       |
| VPC Peering Connections                                 | ⭐⭐⭐         |                 |       |
| VPCs                                                    | ⭐⭐⭐⭐       |                 |       |
| VPN Gateways / Connections                              | ⭐⭐⭐         |                 |       |
| [**ECR** (Pro)](../elastic-container-registry)          |                |                 |       |
| Images                                                  | ⭐⭐⭐         |                 |       |
| Image Scans                                             | \-             |                 |       |
| Lifecycle Policies                                      | ⭐⭐⭐⭐       |                 |       |
| Registries                                              | ⭐⭐⭐⭐       |                 |       |
| Registry Policies                                       | \-             |                 |       |
| Replication Configurations                              | \-             |                 |       |
| Repositories                                            | ⭐⭐⭐⭐       |                 |       |
| Repository Policies                                     | ⭐⭐⭐⭐       |                 |       |
| Tags                                                    | ⭐⭐⭐⭐       |                 |       |
| [**ECS** (Pro)](../elastic-container-service)           |                |                 |       |
| Account Settings                                        | \-             |                 |       |
| Attributes                                              | ⭐⭐⭐⭐       |                 |       |
| Capacity Providers                                      | \-             |                 |       |
| Clusters                                                | ⭐⭐⭐⭐       |                 |       |
| Container Instances                                     | ⭐⭐⭐⭐       |                 |       |
| Services                                                | ⭐⭐⭐⭐       |                 |       |
| Tags                                                    | ⭐⭐⭐⭐       |                 |       |
| Task Definitions                                        | ⭐⭐⭐⭐       |                 |       |
| Task Sets                                               | ⭐⭐⭐         |                 |       |
| Tasks                                                   | ⭐⭐⭐⭐       |                 |       |
| [**EKS** (Pro)](../elastic-kubernetes-service)          |                |                 |       |
| AddOns                                                  | \-             |                 |       |
| Clusters                                                | ⭐⭐⭐         |                 |       |
| Fargate Profiles                                        | ⭐⭐           |                 |       |
| Identity Provider Configs                               | \-             |                 |       |
| Node Groups                                             | \-             |                 |       |
| Tags                                                    | ⭐⭐⭐⭐       |                 |       |
| Updates                                                 | \-             |                 |       |
| [**ElastiCache** (Pro)](../elasticache)                 |                |                 |       |
| Cache Clusters (Memcached)                              | \-             |                 |       |
| Cache Parameter Groups                                  | ⭐⭐⭐⭐       |                 |       |
| Cache Security Groups                                   | ⭐⭐⭐⭐       |                 |       |
| Cache Subnet Groups                                     | ⭐⭐⭐⭐       |                 |       |
| Global Replication Groups                               | \-             |                 |       |
| Replication Groups                                      | ⭐⭐⭐⭐       |                 |       |
| Snapshots                                               | \-             |                 |       |
| Tags                                                    | ⭐⭐⭐⭐       |                 |       |
| Users / User Groups                                     | \-             |                 |       |
| **Elasticsearch Service**                               |                |                 |       |
| Cross-Cluster Search Connections                        | \-             |                 |       |
| Elasticsearch Domains                                   | ⭐⭐⭐⭐       |                 |       |
| Packages                                                | \-             |                 |       |
| Reserved Instances                                      | \-             |                 |       |
| Tags                                                    | ⭐⭐⭐⭐       |                 |       |
| **EMR** (Pro)                                           |                |                 |       |
| Clusters                                                | ⭐⭐⭐⭐       |                 |       |
| Instance Fleets                                         | ⭐⭐⭐         |                 |       |
| Job Flow Steps                                          | ⭐⭐⭐         |                 |       |
| Managed Scaling Policies                                | \-             |                 |       |
| Notebook Executions                                     | \-             |                 |       |
| Run Job Flows (Queries)                                 | ⭐⭐⭐         |                 |       |
| Security Configurations                                 | \-             |                 |       |
| Studios                                                 | \-             |                 |       |
| Tags                                                    | ⭐⭐⭐⭐       |                 |       |
| **EventBridge (CloudWatch Events)**                     |                |                 |       |
| API Destinations                                        | ⭐⭐⭐⭐       |                 |       |
| Archives                                                | \-             |                 |       |
| Connections                                             | \-             |                 |       |
| Event Buses                                             | ⭐⭐⭐⭐       |                 |       |
| Event Sources                                           | ⭐⭐⭐⭐       |                 |       |
| Partner Event Sources                                   | \-             |                 |       |
| Replays                                                 | \-             |                 |       |
| Rules                                                   | ⭐⭐⭐⭐       |                 |       |
| Tags                                                    | ⭐⭐⭐⭐       |                 |       |
| **Firehose**                                            |                |                 |       |
| Delivery Streams                                        | ⭐⭐⭐⭐       |                 |       |
| Destinations                                            | ⭐⭐⭐⭐       |                 |       |
| Records                                                 | ⭐⭐⭐⭐       |                 |       |
| Tags                                                    | ⭐⭐⭐⭐       |                 |       |
| [**Glue** (Pro)](../glue)                               |                |                 |       |
| Classifiers                                             | ⭐⭐⭐         |                 |       |
| Connections                                             | ⭐⭐⭐         |                 |       |
| Crawlers                                                | ⭐⭐⭐         |                 |       |
| Databases                                               | ⭐⭐⭐         |                 |       |
| Dev Endpoints                                           | \-             |                 |       |
| Jobs                                                    | ⭐⭐⭐         |                 |       |
| ML Transforms                                           | \-             |                 |       |
| Partitions                                              | ⭐⭐⭐         |                 |       |
| Registries                                              | ⭐⭐⭐         |                 |       |
| Schemas                                                 | ⭐⭐⭐         |                 |       |
| Scripts                                                 | \-             |                 |       |
| Security Configurations                                 | ⭐⭐⭐         |                 |       |
| Tables                                                  | ⭐⭐⭐         |                 |       |
| Triggers                                                | ⭐⭐⭐         |                 |       |
| Tags                                                    | ⭐⭐⭐         |                 |       |
| User Defined Functions                                  | \-             |                 |       |
| Workflows                                               | ⭐⭐⭐         |                 |       |
| [**IAM**](../iam)                                       |                |                 |       |
| Access Keys                                             | ⭐⭐⭐         |                 |       |
| Account Aliases                                         | ⭐⭐⭐         |                 |       |
| Credential Reports                                      | \-             |                 |       |
| Groups                                                  | ⭐⭐⭐⭐       |                 |       |
| Instance Profiles                                       | ⭐⭐⭐         |                 |       |
| Login Profiles                                          | ⭐⭐⭐         |                 |       |
| OIDC Providers                                          | \-             |                 |       |
| Policies                                                | ⭐⭐⭐⭐       |                 |       |
| Roles                                                   | ⭐⭐⭐⭐       |                 |       |
| SAML Providers                                          | \-             |                 |       |
| Server Certificates                                     | ⭐⭐⭐         |                 |       |
| Service Linked Roles                                    | ⭐⭐⭐         |                 |       |
| Users                                                   | ⭐⭐⭐⭐       |                 |       |
| Virtual MFA Devices                                     | ⭐⭐           |                 |       |
| [**IoT (IoT Analytics, IoT Data)** (Pro)](../iot)       |                |                 |       |
| Authorizers                                             | \-             |                 |       |
| Billing Groups                                          | \-             |                 |       |
| Certificates                                            | ⭐⭐           |                 |       |
| Channels                                                | ⭐⭐           |                 |       |
| Custom Metrics                                          | \-             |                 |       |
| Datasets                                                | ⭐⭐⭐         |                 |       |
| Dimensions                                              | \-             |                 |       |
| Domain Configurations                                   | \-             |                 |       |
| Jobs                                                    | ⭐⭐⭐         |                 |       |
| Jobs Executions                                         | ⭐⭐⭐         |                 |       |
| Jobs Templates                                          | \-             |                 |       |
| Mitigation Actions                                      | \-             |                 |       |
| Policies                                                | ⭐⭐⭐         |                 |       |
| Provisioning Claims / Templates                         | ⭐⭐           |                 |       |
| Role Aliases                                            | \-             |                 |       |
| Security Profiles                                       | \-             |                 |       |
| Shadows                                                 | ⭐⭐           |                 |       |
| Streams                                                 | \-             |                 |       |
| Tags                                                    | ⭐⭐⭐⭐       |                 |       |
| Thing Groups                                            | ⭐⭐⭐         |                 |       |
| Thing Types                                             | ⭐⭐⭐         |                 |       |
| Things                                                  | ⭐⭐⭐         |                 |       |
| Topic Rules                                             | ⭐⭐⭐         |                 |       |
| [**Kinesis**](../kinesis)                               |                |                 |       |
| Records                                                 | ⭐⭐⭐⭐       |                 |       |
| Split / Merge Shards                                    | ⭐⭐⭐⭐       |                 |       |
| Stream Consumers                                        | ⭐⭐⭐⭐       |                 |       |
| Stream Encryption                                       | \-             |                 |       |
| Streams                                                 | ⭐⭐⭐⭐       |                 |       |
| Subscribe to Shard                                      | ⭐⭐⭐⭐       |                 |       |
| Tags                                                    | ⭐⭐⭐⭐       |                 |       |
| **KMS**                                                 |                |                 |       |
| Aliases                                                 | ⭐⭐⭐⭐       |                 |       |
| Custom Key Stores                                       | ⭐⭐⭐         |                 |       |
| Encrypt / Decrypt / Sign Data                           | ⭐⭐⭐⭐       |                 |       |
| Grants                                                  | \-             |                 |       |
| Key Policies                                            | \-             |                 |       |
| Keys                                                    | ⭐⭐⭐⭐       |                 |       |
| Tags                                                    | ⭐⭐⭐⭐       |                 |       |
| **Lambda**                                              |                |                 |       |
| Aliases                                                 | ⭐⭐⭐⭐       |                 |       |
| Code Signing Configs                                    | ⭐⭐           |                 |       |
| Custom Images (Pro)                                     | ⭐⭐⭐⭐       |                 |       |
| Event Invoke Configs                                    | ⭐⭐⭐⭐       |                 |       |
| Event Source Mappings                                   | ⭐⭐⭐⭐       |                 |       |
| Function Concurrencies                                  | ⭐⭐⭐         |                 |       |
| Functions                                               | ⭐⭐⭐⭐       |                 |       |
| Invoke Functions                                        | ⭐⭐⭐⭐       |                 |       |
| [Layers (Pro)](../lambda-layers)                        | ⭐⭐⭐⭐       |                 |       |
| Permissions                                             | ⭐⭐⭐⭐       |                 |       |
| Tags                                                    | ⭐⭐⭐⭐       |                 |       |
| **Managed Streaming for Kafka (MSK)** (Pro)             |                |                 |       |
| Brokers                                                 | ⭐⭐           |                 |       |
| Cluster Operations                                      | ⭐⭐           |                 |       |
| Clusters                                                | ⭐⭐⭐⭐       |                 |       |
| Configurations                                          | ⭐⭐⭐⭐       |                 |       |
| Tags                                                    | ⭐⭐⭐⭐       |                 |       |
| **MediaStore** (Pro)                                    |                |                 |       |
| Access Logging                                          | \-             |                 |       |
| Container Policies                                      | \-             |                 |       |
| Containers                                              | ⭐⭐⭐         |                 |       |
| CORS Policies                                           | \-             |                 |       |
| Lifecycle Policies                                      | \-             |                 |       |
| Metric Policies                                         | \-             |                 |       |
| Tags                                                    | \-             |                 |       |
| [**Neptune DB** (Pro)](../neptune)                      |                |                 |       |
| DB Clusters                                             | ⭐⭐⭐⭐       |                 |       |
| DB Cluster Endpoints                                    | ⭐⭐⭐⭐       |                 |       |
| DB Cluster Parameter Groups                             | ⭐⭐⭐⭐       |                 |       |
| DB Cluster Snapshots                                    | \-             |                 |       |
| Engine Default Parameters                               | ⭐⭐           |                 |       |
| Event Subscriptions                                     | \-             |                 |       |
| Events                                                  | \-             |                 |       |
| Tags                                                    | \-             |                 |       |
| [**QLDB** (Pro)](../qldb)                               |                |                 |       |
| Blocks                                                  | ⭐⭐⭐         |                 |       |
| Digests                                                 | ⭐⭐⭐         |                 |       |
| Journal Kinesis Streams                                 | ⭐⭐⭐         |                 |       |
| Journal S3 Exports                                      | ⭐⭐⭐         |                 |       |
| Ledgers                                                 | ⭐⭐⭐⭐       |                 |       |
| Send Commands / Run Queries                             | ⭐⭐⭐⭐       |                 |       |
| Tags                                                    | ⭐⭐⭐⭐       |                 |       |
| [**RDS / Aurora Serverless** (Pro)](../rds)             |                |                 |       |
| DB/Cluster Parameter Groups                             | ⭐⭐⭐         |                 |       |
| DB/Cluster Snapshots                                    | ⭐⭐⭐         |                 |       |
| DB Clusters/Instances                                   | ⭐⭐⭐⭐       |                 |       |
| DB Proxies                                              | ⭐⭐           |                 |       |
| DB Security/Subnet Groups                               | ⭐⭐⭐         |                 |       |
| Event Subscriptions                                     | \-             |                 |       |
| Option Groups                                           | ⭐⭐⭐⭐       |                 |       |
| Postgres AWS Extension Functions                        | ⭐⭐⭐         |                 |       |
| Tags                                                    | ⭐⭐⭐⭐       |                 |       |
| **Redshift**                                            |                |                 |       |
| Authorize/Revoke Access                                 | \-             |                 |       |
| Cluster Parameter Groups                                | ⭐⭐⭐         |                 |       |
| Cluster Snapshots                                       | ⭐⭐⭐         |                 |       |
| Clusters/Instances                                      | ⭐⭐⭐⭐       |                 |       |
| Event Subscriptions                                     | \-             |                 |       |
| HSM Configurations                                      | \-             |                 |       |
| Partners                                                | \-             |                 |       |
| Security/Subnet Groups                                  | ⭐⭐⭐         |                 |       |
| Tags                                                    | ⭐⭐⭐⭐       |                 |       |
| Usage Limits                                            | ⭐⭐           |                 |       |
| [**Route53**](../route53)                               |                |                 |       |
| DNS Server Integration (Pro)                            | ⭐⭐⭐⭐       |                 |       |
| Geo Locations                                           | \-             |                 |       |
| Health Checks                                           | ⭐⭐           |                 |       |
| Hosted Zones                                            | ⭐⭐⭐⭐       |                 |       |
| Query Logging Configs                                   | \-             |                 |       |
| Resource Record Sets                                    | ⭐⭐⭐⭐       |                 |       |
| Reusable Delegation Sets                                | ⭐⭐⭐         |                 |       |
| Tags                                                    | ⭐⭐⭐⭐       |                 |       |
| Traffic Policies                                        | ⭐⭐⭐         |                 |       |
| [**S3**](../s3)                                         |                |                 |       |
| Bucket ACLs                                             | ⭐⭐⭐         |                 |       |
| Bucket CORS                                             | ⭐⭐⭐         |                 |       |
| Bucket Encryptions                                      | ⭐⭐⭐         |                 |       |
| Bucket Lifecycles                                       | ⭐⭐⭐         |                 |       |
| Bucket Loggings                                         | ⭐⭐⭐         |                 |       |
| Bucket Metrics Configurations                           | ⭐⭐⭐         |                 |       |
| Bucket Notifications                                    | ⭐⭐⭐         |                 |       |
| Bucket Ownership Controls                               | ⭐⭐⭐         |                 |       |
| Bucket Policies                                         | ⭐⭐⭐         |                 |       |
| Bucket Replications                                     | ⭐⭐⭐         |                 |       |
| Bucket Request Payments                                 | ⭐⭐⭐         |                 |       |
| Bucket Versionings                                      | ⭐⭐⭐         |                 |       |
| Bucket Websites                                         | ⭐⭐⭐         |                 |       |
| Buckets                                                 | ⭐⭐⭐⭐       |                 |       |
| Object Retentions                                       | ⭐⭐           |                 |       |
| Object Versions                                         | ⭐⭐⭐⭐       |                 |       |
| Objects                                                 | ⭐⭐⭐⭐       |                 |       |
| Tags                                                    | ⭐⭐⭐⭐       |                 |       |
| Upload/Download Files                                   | ⭐⭐⭐⭐       |                 |       |
| [**SageMaker** (Pro)](../sagemaker)                     |                |                 |       |
| Actions                                                 | ⭐⭐           |                 |       |
| Algorithms                                              | \-             |                 |       |
| App Image Configs                                       | ⭐⭐           |                 |       |
| Apps                                                    | ⭐⭐⭐         |                 |       |
| Artifacts                                               | ⭐⭐⭐         |                 |       |
| Associations                                            | \-             |                 |       |
| Auto ML Jobs                                            | \-             |                 |       |
| Code Repositories                                       | \-             |                 |       |
| Compilation Jobs                                        | \-             |                 |       |
| Contexts                                                | \-             |                 |       |
| Data Quality Job Definitions                            | \-             |                 |       |
| Device Fleets                                           | \-             |                 |       |
| Devices                                                 | \-             |                 |       |
| Domains                                                 | \-             |                 |       |
| Edge Packaging Jobs                                     | \-             |                 |       |
| Endpoints / Endpoint Configs                            | \-             |                 |       |
| Experiments                                             | \-             |                 |       |
| Feature Groups                                          | \-             |                 |       |
| Flow Definitions                                        | \-             |                 |       |
| Hyper Parameter Tuning Jobs                             | \-             |                 |       |
| Images / Image Versions                                 | \-             |                 |       |
| Labelling Jobs                                          | \-             |                 |       |
| Model Bias/Explainability Jobs                          | \-             |                 |       |
| Model Packages                                          | \-             |                 |       |
| Models                                                  | ⭐⭐           |                 |       |
| Monitoring Executions/Schedules                         | \-             |                 |       |
| Notebook Instances                                      | \-             |                 |       |
| Pipeline Executions                                     | \-             |                 |       |
| Pipelines                                               | \-             |                 |       |
| Projects                                                | \-             |                 |       |
| Tags                                                    | \-             |                 |       |
| Training Jobs                                           | \-             |                 |       |
| Transform Jobs                                          | \-             |                 |       |
| Trials                                                  | \-             |                 |       |
| User Profiles                                           | \-             |                 |       |
| Workforces / Workteams                                  | \-             |                 |       |
| **SecretsManager**                                      |                |                 |       |
| Resource Policies                                       | ⭐⭐⭐⭐       |                 |       |
| Secret Replications                                     | ⭐⭐           |                 |       |
| Secret Rotations                                        | ⭐⭐           |                 |       |
| Secrets                                                 | ⭐⭐⭐⭐       |                 |       |
| Tags                                                    | ⭐⭐⭐⭐       |                 |       |
| [**SES**](../ses)                                       |                |                 |       |
| Configuration Sets                                      | ⭐⭐⭐         |                 |       |
| Identities                                              | ⭐⭐           |                 |       |
| Identity Policies                                       | ⭐⭐           |                 |       |
| Quotas / Statistics                                     | ⭐⭐           |                 |       |
| Receipt Filters                                         | ⭐⭐⭐         |                 |       |
| Receipt Rules                                           | ⭐⭐⭐         |                 |       |
| Sending Emails via SMTP (Pro)                           | ⭐⭐⭐⭐       |                 |       |
| Templates                                               | ⭐⭐⭐⭐       |                 |       |
| **SNS**                                                 |                |                 |       |
| Platform Applications                                   | ⭐⭐⭐         |                 |       |
| Publish/Subscribe to Topics                             | ⭐⭐⭐⭐       |                 |       |
| SMS Attributes / Sandbox Accounts                       | ⭐⭐           |                 |       |
| Subscriptions                                           | ⭐⭐⭐⭐       |                 |       |
| Tags                                                    | ⭐⭐⭐⭐       |                 |       |
| Topics                                                  | ⭐⭐⭐⭐       |                 |       |
| [**SQS**](../sqs)                                       |                |                 |       |
| Message Visibility                                      | ⭐⭐⭐⭐       |                 |       |
| Messages                                                | ⭐⭐⭐⭐       |                 |       |
| Permission                                              | ⭐⭐⭐         |                 |       |
| Queues                                                  | ⭐⭐⭐⭐       |                 |       |
| Tags                                                    | ⭐⭐⭐⭐       |                 |       |
| **SSM**                                                 |                |                 |       |
| Associations                                            | ⭐⭐⭐         |                 |       |
| Calendar States                                         | ⭐⭐           |                 |       |
| Commands / Command Invocations                          | ⭐⭐⭐         |                 |       |
| Compliance Items                                        | ⭐⭐           |                 |       |
| Documents                                               | ⭐⭐⭐         |                 |       |
| Inventory Entries                                       | \-             |                 |       |
| Ops Metadata                                            | ⭐⭐           |                 |       |
| Parameters                                              | ⭐⭐⭐⭐       |                 |       |
| Resource Compliance Summaries                           | \-             |                 |       |
| Tags                                                    | ⭐⭐⭐⭐       |                 |       |
| **StepFunctions**                                       |                |                 |       |
| Activities                                              | ⭐⭐⭐⭐       |                 |       |
| Executions / Execution History                          | ⭐⭐⭐⭐       |                 |       |
| State Machines                                          | ⭐⭐⭐⭐       |                 |       |
| Tags                                                    | ⭐⭐⭐⭐       |                 |       |
| **STS**                                                 |                |                 |       |
| Assume Role (Pro)                                       | ⭐⭐⭐⭐       |                 |       |
| Get Access Key Info                                     | ⭐⭐⭐⭐       |                 |       |
| Get Caller Identity                                     | ⭐⭐⭐⭐       |                 |       |
| Session Tokens                                          | ⭐⭐⭐⭐       |                 |       |
| **Timestream** (Pro)                                    |                |                 |       |
| Databases                                               | ⭐⭐⭐         |                 |       |
| Run Query                                               | ⭐⭐⭐         |                 |       |
| Tables                                                  | ⭐⭐⭐         |                 |       |
| Tags                                                    | ⭐⭐⭐⭐       |                 |       |
| Write Records                                           | ⭐⭐⭐⭐       |                 |       |
| [**Transfer** (Pro)](../transfer)                       |                |                 |       |
| Accesses                                                | \-             |                 |       |
| Security Policies                                       | \-             |                 |       |
| Servers                                                 | ⭐⭐⭐         |                 |       |
| SSH Public Keys                                         | ⭐⭐⭐         |                 |       |
| Tags                                                    | \-             |                 |       |
| Users                                                   | ⭐⭐⭐         |                 |       |
| [**XRay** (Pro)](../xray-tracing)                       |                |                 |       |
| Encryption Configs                                      | \-             |                 |       |
| Groups                                                  | ⭐⭐           |                 |       |
| Insights                                                | \-             |                 |       |
| Sampling Rules                                          | ⭐⭐⭐         |                 |       |
| Service Graph                                           | \-             |                 |       |
| Tags                                                    | \-             |                 |       |
| Telemetry Records                                       | ⭐⭐⭐⭐       |                 |       |
| Trace Graph                                             | \-             |                 |       |
| Trace Segments / Summaries                              | ⭐⭐⭐         |                 |       |

## API Persistence Coverage (Pro)

The list below summarizes the APIs for which persistence has been implemented and (ideally) tested in the Pro version (list may not be exhaustive/complete). More details following soon.

- Amplify
- Athena
- Backup
- Cognito Identity
- Cognito Identity Provider
- DynamoDB
- EC2
- Elastic File System
- Kinesis
- QLDB
- S3
- Secrets Manager
- SNS
- SQS
- Route53
- RDS
- Appconfig
- Appsync
- Lambda
- CloudFormation
- CloudFront
- CodeCommit
- Cost Explorer
- Glue
- IoT
- Lake Formation
- Serverless Repo
- SES
- STS
