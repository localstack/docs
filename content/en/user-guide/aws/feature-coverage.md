---
title: "AWS Service Feature Coverage"
linkTitle: "⭐ Feature Coverage"
weight: 1
description: >
  Overview of the implemented AWS APIs and their level of parity with the AWS cloud
aliases:
  - /localstack/coverage/
  - /aws/feature-coverage/
---


## Coverage Levels

LocalStack provides emulation services for different AWS APIs (e.g., Lambda, SQS, SNS, ...), but the level of support with the real system differs and is categorized using the following system:

|          |                                                         |
|----------|------------------------------------------------------------------------------------------------------------------------|
| ⭐⭐⭐⭐⭐ | Feature fully supported by LocalStack maintainers; feature is guaranteed to pass all or the majority of tests         | 
| ⭐⭐⭐⭐   | Feature partially supported by LocalStack maintainers         |               
| ⭐⭐⭐    | Feature supports basic functionalities (e.g., CRUD operations)          |                
| ⭐⭐      | Feature should be considered unstable          |                 
| ⭐       | Feature is experimental and regressions should be expected         | 
| **-**    | Feature is not yet implemented        | 


## Emulation Levels

* CRUD: The service accepts requests and returns proper (potentially static) responses. No additional business logic besides storing entities.
* Emulated: The service imitates the functionality, including synchronous and asynchronous business logic operating on service entities.

## AWS Feature Coverage

In the coverage table below, the features are marked with their respective availability across different LocalStack versions:

* Community version (default, if not marked)
* Pro version (marked with **Pro**)

| Service / Feature                                                  | Coverage Level    | Emulation Level | Notes |
|--------------------------------------------------------------------|-------------------|-----------------|-------|
| **ACM**                                                            | [🔍]({{< ref "references/coverage#acm" >}})      |                 |       |
| Certificates                                                       | ⭐⭐⭐              | CRUD            |       |
| Tags                                                               | ⭐⭐⭐⭐            | CRUD            |       |
| Account Configuration                                              | ⭐⭐                | CRUD            |       |
| [**Amplify** (Pro)]({{< ref "amplify" >}})                         | [🔍]({{< ref "references/coverage#amplify" >}})  |                 |       |
| Apps                                                               | ⭐⭐⭐⭐             | Emulated        |       |
| Backend Environments                                               | ⭐⭐⭐               | CRUD            |       |
| Branches                                                           | ⭐⭐⭐              | CRUD            |       |
| Deployments                                                        | \-                 |                 |       |
| Domain Associations                                                | \-                 |                 |       |
| Jobs                                                               | \-                 |                 |       |
| Tags                                                               | ⭐⭐⭐⭐             | CRUD            |       |
| Webhooks                                                           | ⭐⭐⭐               | Emulated       |       |
| **API Gateway**                                                    | [🔍]({{< ref "references/coverage#apigateway" >}}) |                 |       |
| API Keys                                                           | ⭐⭐⭐              | CRUD                |       |
| Authorizers (Pro)                                                  | ⭐⭐⭐⭐            | Emulated                |       |
| Base Path Mappings                                                 | ⭐⭐⭐⭐            | Emulated                |       |
| Deployments                                                        | ⭐⭐⭐⭐            | CRUD                |       |
| Documentation Parts                                                | ⭐⭐⭐              | CRUD                |       |
| Documentation Versions                                             | ⭐⭐⭐              | CRUD                |       |
| Domain Names                                                       | ⭐⭐⭐              | CRUD                |       |
| Gateway / Integration / Method Responses                           | ⭐⭐⭐⭐            | Emulated                |       |
| Integrations                                                       | ⭐⭐⭐⭐            | Emulated                |       |
| Methods                                                            | ⭐⭐⭐⭐            | Emulated                |       |
| Models                                                             | ⭐⭐⭐              | CRUD                |       |
| Request Validators                                                 | ⭐⭐                | Emulated                |       |
| Resources                                                          | ⭐⭐⭐⭐            | Emulated                |       |
| REST APIs                                                          | ⭐⭐⭐⭐            | Emulated                |       |
| Stages                                                             | ⭐⭐⭐⭐            | Emulated                |       |
| Tags                                                               | ⭐⭐⭐⭐            | CRUD                |       |
| Usage Plans                                                        | ⭐⭐⭐              | CRUD                |       |
| Usage Plan Keys                                                    | ⭐⭐⭐              | CRUD                |       |
| VPC Links                                                          | ⭐⭐⭐              | CRUD                |       |
| [**API Gateway v2** (Pro)]({{< ref "apigatewayv2" >}})             | [🔍]({{< ref "references/coverage#apigatewayv2" >}})     |                 |       |
| APIs                                                               | ⭐⭐⭐⭐            | Emulated                |       |
| API Mappings                                                       | ⭐⭐⭐              | Emulated                |       |
| Authorizers                                                        | ⭐⭐⭐⭐            | Emulated                |       |
| Deployments                                                        | ⭐⭐⭐⭐            | CRUD                |       |
| Domain Names                                                       | ⭐⭐⭐              | CRUD                |       |
| Import APIs from OpenAPI specs                                     | ⭐⭐⭐              | Emulated                |       |
| Integrations                                                       | ⭐⭐⭐              | Emulated                |       |
| Integration Responses                                              | ⭐⭐⭐              | Emulated                |       |
| Models                                                             | ⭐⭐⭐              | CRUD                |       |
| Routes                                                             | ⭐⭐⭐⭐            | Emulated                |       |
| Route Responses                                                    | ⭐⭐⭐              | Emulated                |       |
| Stages                                                             | ⭐⭐⭐⭐            | CRUD                |       |
| Tags                                                               | ⭐⭐⭐⭐            | CRUD                |       |
| VPC Links                                                          | ⭐⭐⭐              | CRUD                |       |
| **API Gateway Management API** (Pro)                               | [🔍]({{< ref "references/coverage#apigatewaymanagementapi" >}}) |                 |       |
| Connections                                                         | ⭐⭐⭐            | Emulated                |       |
| **AppConfig** (Pro)                                                | [🔍]({{< ref "references/coverage#appconfig" >}})               |                 |       |
| Applications                                                       | ⭐⭐⭐           | CRUD            |       |
| Configuration Profiles                                             | ⭐⭐⭐⭐         | CRUD            |       |
| Configurations                                                     | ⭐⭐⭐           | CRUD            |       |
| Deployment Strategies                                              | ⭐⭐⭐⭐         | CRUD            |       |
| Deployments                                                        | ⭐⭐⭐           | Emulated        |       |
| Environments                                                       | ⭐⭐⭐⭐          | CRUD           |       |
| Hosted Configuration Versions                                      | ⭐⭐⭐           | CRUD            |       |
| Tags                                                               | ⭐⭐⭐⭐         | CRUD             |       |
| **Application Autoscaling** (Pro)                                  | [🔍]({{< ref "references/coverage#application-autoscaling" >}})     |                 |       |
| Scalable Targets                                                   | ⭐⭐⭐           | CRUD           |       |
| Scaling Activities                                                 | \-              |                |       |
| Scaling Policies                                                   | ⭐⭐⭐           | CRUD            |       |
| Scheduled Actions                                                  | ⭐⭐⭐           | CRUD             |       |
| [**AppSync** (Pro)]({{< ref "appsync" >}})                         | [🔍]({{< ref "references/coverage#appsync" >}})                |                 |       |
| API Caches                                                         | ⭐⭐⭐⭐         | Emulated        |       |
| API Keys                                                           | ⭐⭐⭐⭐         | Emulated         |       |
| Data Sources                                                       | ⭐⭐⭐          | Emulated         |       |
| Functions                                                          | ⭐⭐⭐          | Emulated         |       |
| GraphQL APIs                                                       | ⭐⭐⭐⭐         | Emulated        |       |
| Resolvers                                                          | ⭐⭐⭐⭐         | Emulated        |       |
| Tags                                                               | ⭐⭐⭐⭐         | CRUD            |       |
| Types                                                              | ⭐⭐⭐⭐         | Emulated        |       |
| [**Athena** (Pro)]({{< ref "athena" >}})                           | [🔍]({{< ref "references/coverage#athena" >}}) |                 |       |
| Data Catalogs                                                      | ⭐⭐           | CRUD            |       |
| Databases                                                          | ⭐⭐           | Emulated        |       |
| Named Queries                                                      | \-             |                 |       |
| Prepared Statements                                                | \-             |                 |       |
| Query Executions                                                   | ⭐⭐⭐         | Emulated        |       |
| Table Metadata                                                     | \-             |                 |       |
| Tags                                                               | ⭐⭐⭐         | CRUD            |       |
| Work Groups                                                        | \-             |                 |       |
| **Autoscaling** (Pro)                                              | [🔍]({{< ref "references/coverage#autoscaling" >}}) |                 |       |
| Metric Collection                                                  | ⭐⭐⭐         | CRUD            |       |
| Autoscaling Groups                                                 | ⭐⭐           | CRUD            |       |
| Loadbalancer                                                       | ⭐⭐⭐         | CRUD            |       |
| [**Backup** (Pro)]({{< ref "backup" >}})                           | [🔍]({{< ref "references/coverage#backup" >}}) |                 |       |
| Backup Jobs                                                        | ⭐⭐⭐⭐       | Emulated        |       |
| Backup Plans                                                       | ⭐⭐⭐         | Emulated        |       |
| Backup Selections                                                  | ⭐⭐⭐         | Emulated        |       |
| Backup Vaults                                                      | ⭐⭐⭐         | Emulated        |       |
| Backup Vault Access Policies                                       | \-             |                 |       |
| Backup Vault Notifications                                         | \-             |                 |       |
| Global Settings                                                    | \-             |                 |       |
| Protected Resources                                                | \-             |                 |       |
| Recovery Points                                                    | ⭐⭐⭐          | Emulated        |       |
| Tags                                                               | \-             |                 |       |
| **Batch** (Pro)                                                    | [🔍]({{< ref "references/coverage#batch" >}}) |                 |       |
| Compute Environments                                               | ⭐⭐⭐         | CRUD            |       |
| Job Queues                                                         | ⭐⭐⭐         | CRUD            |       |
| Job Definitions                                                    | ⭐⭐⭐         | CRUD            |       |
| Jobs                                                               | ⭐⭐⭐         | Emulated        |       |
| **CE (Cost Explorer API)** (Pro)                                   | [🔍]({{< ref "references/coverage#ce" >}}) |                 |       |
| Anomaly Monitoring                                                 | ⭐⭐⭐         | CRUD            |       |
| Anomaly Subscription                                               | ⭐⭐⭐         | CRUD            |       |
| Cost Category                                                      | ⭐⭐           | CRUD            |       |
| Cost Usage/Forecast                                                | \-             |                 |       |
| Savings Plan                                                       | \-             |                 |       |
| [**CloudFormation**]({{< ref "cloudformation" >}})                 | [🔍]({{< ref "references/coverage#cloudformation" >}}) |                 |       |
| Change Sets                                                        | ⭐⭐⭐⭐       | Emulated        |       |
| Stacks                                                             | ⭐⭐⭐⭐       | Emulated        |       |
| Stack Drifts                                                       | \-             | \-               |       |
| Stack Events                                                       | ⭐⭐⭐         | Emulated        |       |
| Stack Instances                                                    | ⭐⭐⭐⭐       | Emulated         |       |
| Stack Policies                                                     | ⭐⭐⭐         | CRUD             |       |
| Stack Resources                                                    | ⭐⭐⭐⭐       | Emulated        |       |
| Stack Sets                                                         | ⭐⭐⭐         | CRUD         |       |
| Publishers                                                         | \-             | \-                |       |
| Templates                                                          | ⭐⭐⭐⭐       | Emulated                |       |
| Type Activations                                                   | ⭐⭐           | \-                |       |
| [**CloudFront** (Pro)]({{< ref "cloudfront" >}})                   | [🔍]({{< ref "references/coverage#cloudfront" >}}) |                 |       |
| Cache Policies                                                     | \-             |                 |       |
| Distributions                                                      | ⭐⭐⭐⭐        | Emulated        |       |
| Field Level Encryption                                             | \-             |                 |       |
| Functions                                                          | ⭐⭐⭐         | CRUD             |       |
| Invalidations                                                      | ⭐⭐⭐         | CRUD             |       |
| Key Groups                                                         | \-             |                 |       |
| Monitoring Subscriptions                                           | \-             |                 |       |
| Origin Access Identities                                           | ⭐⭐⭐          | CRUD            |       |
| Origin Request Policies                                            | ⭐⭐⭐          | CRUD            |       |
| Public Keys                                                        | \-             |                 |       |
| Realtime Log Configs                                               | \-             |                 |       |
| Streaming Distributions                                            | \-             |                 |       |
| Tags                                                               | ⭐⭐⭐⭐       |  CRUD            |       |
| **CloudTrail** (Pro)                                               | [🔍]({{< ref "references/coverage#cloudtrail" >}}) |                 |       |
| Event Selectors                                                    | ⭐⭐⭐⭐        | Emulated          |       |
| Insight Selectors                                                  | \-             |                 |       |
| Tags                                                               | ⭐⭐⭐⭐       | CRUD             |       |
| Trails                                                             | ⭐⭐⭐⭐        | Emulated         |       |
| Start/Stop Logging                                                 | ⭐⭐⭐⭐        | Emulated         |       |
| [**CloudWatch**]({{< ref "cloudwatch" >}})                         | [🔍]({{< ref "references/coverage#cloudwatch" >}}) |                 |       |
| Alarms                                                             | ⭐⭐⭐⭐        | Emulated       |       |
| Alarm Histories                                                    | \-             |                 |       |
| Anomaly Detectors                                                  | \-             |                 |       |
| Dashboards                                                         | \-             |                 |       |
| Insight Rules                                                      | \-             |                 |       |
| Metric Data                                                        | ⭐⭐⭐⭐         | CRUD         |       |
| Metric Statistics                                                  | ⭐⭐⭐⭐          | CRUD             |       |
| Metric Streams                                                     | \-             |                 |       |
| Tags                                                               | ⭐⭐⭐⭐         | CRUD            |       |
| [**CodeCommit** (Pro)]({{< ref "codecommit" >}})                   | [🔍]({{< ref "references/coverage#codecommit" >}})                |                 |       |
| Approval Rules                                                     | \-             |                 |       |
| Blobs / Files / Folders                                            | ⭐⭐⭐           | Emulated       |       |
| Branches                                                           | ⭐⭐⭐           | Emulated        |       |
| Comments                                                           | \-             |                 |       |
| Commits                                                            | ⭐⭐⭐           | Emulated       |       |
| Merge Commits / Conflicts                                          | \-             |                 |       |
| Pull Requests                                                      | \-             |                 |       |
| Repositories                                                       | ⭐⭐⭐⭐         | Emulated        |       |
| Tags                                                               | ⭐⭐⭐⭐         | CRUD            |       |
| [**Cognito Identity** (Pro)]({{< ref "cognito" >}})                | [🔍]({{< ref "references/coverage#cognito-identity" >}}) |                 |       |
| Developer Identities                                               | \-             |                 |       |
| Identities                                                         | ⭐⭐⭐         | Emulated         |       |
| Identity Pool Roles                                                | \-             |                 |       |
| Identity Pools                                                     | ⭐⭐⭐⭐       | Emulated         |       |
| OpenID Tokens                                                      | \-             |                 |       |
| Tags                                                               | \-             |                 |       |
| [**Cognito Identity Provider (IdP)** (Pro)]({{< ref "cognito" >}}) | [🔍]({{< ref "references/coverage#cognito-idp" >}}) |                 |       |
| Admin APIs                                                         | ⭐⭐⭐         | Emulated        | Triggers can involve Lambda     |
| Devices                                                            | ⭐⭐           | CRUD            |       |
| Auth Flows                                                         | ⭐⭐⭐         | Emulated        |       |
| Groups                                                             | ⭐⭐⭐⭐       | CRUD            |       |
| Lambda Triggers                                                    | ⭐⭐⭐⭐       | Emulated        |       |
| MFA Configs                                                        | ⭐⭐⭐         | CRUD            |       |
| Resource Servers                                                   | \-             |                 |       |
| Risk Configurations                                                | \-             |                 |       |
| Identity Providers                                                 | ⭐⭐⭐         | CRUD            |       |
| User Import Jobs                                                   | \-             |                 |       |
| User Pool Clients                                                  | ⭐⭐⭐⭐       | CRUD            |       |
| User Pool Domains                                                  | ⭐⭐           | CRUD            |       |
| User Pools                                                         | ⭐⭐⭐⭐       | CRUD            |       |
| Users                                                              | ⭐⭐⭐⭐       | CRUD            |       |
| Tags                                                               | ⭐⭐⭐⭐       | CRUD            |       |
| **Config**                                                         | [🔍]({{< ref "references/coverage#config" >}}) |                 |       |
| Config Rules                                                       | ⭐⭐⭐         | CRUD            |       |
| Conformance                                                        | ⭐⭐         | CRUD            |       |
| Remediation                                                        | \-             |                 |       |
| **DocumentDB** (Pro)                                               | [🔍]({{< ref "references/coverage#docdb" >}}) |                 |       |
| DB/Cluster Parameter Groups                                        | ⭐⭐⭐         | CRUD            |       |
| DB/Cluster Snapshots                                               | ⭐⭐           | Emulated        |       |
| DB Clusters/Instances                                              | ⭐⭐⭐⭐       | Emulated         |       |
| DB Subnet Groups                                                   | ⭐⭐⭐         | Emulated         |       |
| Event Subscriptions                                                | \-           |                 |       |
| Tags                                                               | ⭐⭐⭐⭐       | CRUD            |       |
| **DynamoDB**                                                       | [🔍]({{< ref "references/coverage#dynamodb" >}}) |                 |       |
| Backups (Pro)                                                      | ⭐⭐⭐⭐       | Emulated        |       |
| Batch Operations                                                   | ⭐⭐⭐⭐       | Emulated        |       |
| Global Tables                                                      | ⭐⭐⭐⭐       | CRUD            | version 2019.11.21 not supported yet |
| Items                                                              | ⭐⭐⭐⭐       | Emulated        |       |
| Kinesis Streaming Destinations                                     | ⭐⭐⭐         | Emulated        |       |
| PartiQL Queries                                                    | ⭐⭐⭐⭐       | Emulated        |       |
| Query / Scan Operations                                            | ⭐⭐⭐⭐       | Emulated        |       |
| Tables                                                             | ⭐⭐⭐⭐       | Emulated        |       |
| Table Replica Autoscaling                                          | \-             |                 |       |
| Tags                                                               | ⭐⭐⭐⭐       | CRUD            |       |
| **DynamoDB Streams**                                               | [🔍]({{< ref "references/coverage#dynamodbstreams" >}}) |                 |       |
| Records                                                            | ⭐⭐⭐⭐       | Emulated        |       |
| Shard Iterators                                                    | ⭐⭐⭐⭐       | Emulated        |       |
| Streams                                                            | ⭐⭐⭐⭐       | Emulated        |       |
| [**EC2**]({{< ref "elastic-compute-cloud" >}})                      | [🔍]({{< ref "references/coverage#ec2" >}})  |                 |       |
| Classic Links                                                      | \-             |                 |       |
| Customer Gateways                                                  | ⭐             | CRUD            |       |
| DHCP Options                                                       | ⭐⭐           | CRUD            |       |
| Allocate/Deallocate Elastic IPs                                    | ⭐⭐⭐         | CRUD            |       |
| Fleets                                                             | ⭐⭐           | CRUD            |       |
| Flow Logs                                                          | ⭐⭐⭐         | CRUD            |       |
| Images                                                             | ⭐⭐           | CRUD            | (Pro) Include Docker images |
| Internet Gateways                                                  | ⭐⭐⭐         | CRUD            |       |
| Local Gateway Routes                                               | ⭐⭐⭐         | CRUD            |       |
| Key Pairs                                                          | ⭐⭐⭐⭐       | CRUD            |       |
| Launch Templates                                                   | ⭐⭐⭐         | CRUD            |       |
| NAT Gateways                                                       | ⭐⭐⭐         | CRUD            |       |
| Network ACLs                                                       | ⭐⭐⭐         | CRUD            |       |
| Network Interfaces                                                 | ⭐⭐⭐         | CRUD            |       |
| Reserved Instances                                                 | ⭐⭐⭐         | CRUD            |       |
| Route Tables / Routes                                              | ⭐⭐⭐         | CRUD            |       |
| Scheduled Instances                                                | ⭐⭐⭐         | CRUD            |       |
| Security Groups / Egress / Ingress                                 | ⭐⭐⭐⭐       | CRUD            |       |
| Snapshots                                                          | ⭐⭐⭐         | CRUD            |       |
| Spot Instances                                                     | ⭐⭐⭐         | CRUD            |       |
| Instances                                                          | ⭐⭐           | Emulated        | (Pro) As Docker containers |
| Subnets                                                            | ⭐⭐⭐         | CRUD            |       |
| Tags                                                               | ⭐⭐⭐⭐       | CRUD            |       |
| Traffic Mirrors                                                    | \-             |                 |       |
| Transit Gateways                                                   | ⭐⭐           | CRUD            |       |
| Volumes                                                            | ⭐⭐⭐         | CRUD            |       |
| VPC Endpoint Connections                                           | ⭐⭐⭐         | CRUD            |       |
| VPC Peering Connections                                            | ⭐⭐⭐         | CRUD            |       |
| VPCs                                                               | ⭐⭐⭐⭐       | CRUD            |       |
| VPN Gateways / Connections                                         | ⭐⭐⭐         | CRUD            |       |
| [**ECR** (Pro)]({{< ref "elastic-container-registry" >}})          | [🔍]({{< ref "references/coverage#ecr" >}}) |                 |       |
| Images                                                             | ⭐⭐⭐         |    Emulated     |       |
| Image Scans                                                        | \-             |                 |       |
| Lifecycle Policies                                                 | ⭐⭐⭐⭐       |      CRUD       |       |
| Registries                                                         | ⭐⭐⭐⭐       |    Emulated     |       |
| Registry Policies                                                  | \-             |                 |       |
| Replication Configurations                                         | \-             |                 |       |
| Repositories                                                       | ⭐⭐⭐⭐       |    Emulated     |       |
| Repository Policies                                                | ⭐⭐⭐⭐       |      CRUD       |       |
| Tags                                                               | ⭐⭐⭐⭐       |      CRUD       |       |
| [**ECS** (Pro)]({{< ref "elastic-container-service" >}})           | [🔍]({{< ref "references/coverage#ecs" >}}) |                 |       |
| Account Settings                                                   | \-             |                 |       |
| Attributes                                                         | ⭐⭐⭐⭐       |      CRUD       |       |
| Capacity Providers                                                 | \-             |                 |       |
| Clusters                                                           | ⭐⭐⭐⭐       |    Emulated     |       |
| Container Instances                                                | ⭐⭐⭐⭐       |    Emulated     |       |
| Services                                                           | ⭐⭐⭐⭐       |    Emulated     |       |
| Tags                                                               | ⭐⭐⭐⭐       |      CRUD       |       |
| Task Definitions                                                   | ⭐⭐⭐⭐       |    Emulated     |       |
| Task Sets                                                          | ⭐⭐⭐         |      CRUD       |       |
| Tasks                                                              | ⭐⭐⭐⭐       |    Emulated     |       |
| **EFS** (Pro)                                                      | [🔍]({{< ref "references/coverage#efs" >}}) |                 |       |
| File System                                                        | ⭐⭐⭐⭐       | Emulated        |        |
| Backup Policy                                                      | \-             |                 |       |
| [**EKS** (Pro)]({{< ref "elastic-kubernetes-service" >}})          | [🔍]({{< ref "references/coverage#eks" >}}) |                 |       |
| AddOns                                                             | \-             |                 |       |
| Clusters                                                           | ⭐⭐⭐         | Emulated        |       |
| Fargate Profiles                                                   | ⭐⭐           | CRUD            |       |
| Identity Provider Configs                                          | \-             |                 |       |
| Node Groups                                                        | \-             |                 |       |
| Tags                                                               | ⭐⭐⭐⭐       | CRUD            |       |
| Updates                                                            | \-             |                 |       |
| [**ElastiCache** (Pro)]({{< ref "elasticache" >}})                 | [🔍]({{< ref "references/coverage#elasticache" >}}) |       |
| Cache Clusters (Memcached)                                         | \-             |                 |       |
| Cache Clusters (Redis)                                             | ⭐⭐⭐         | Emulated       |       |
| Cache Parameter Groups                                             | ⭐⭐⭐⭐       | Emulated       |       |
| Cache Security Groups                                              | ⭐⭐⭐⭐       | CRUD           |       |
| Cache Subnet Groups                                                | ⭐⭐⭐⭐       | CRUD           |       |
| Global Replication Groups                                          | \-             |                 |       |
| Replication Groups                                                 | ⭐⭐⭐⭐       | Emulated       |       |
| Snapshots                                                          | \-             |                 |       |
| Tags                                                               | ⭐⭐⭐⭐       | CRUD           |       |
| Users / User Groups                                                | \-             |                 |       |
| **Elastic Beanstalk** (Pro)                                        | [🔍]({{< ref "references/coverage#elasticbeanstalk" >}}) |                 |       |
| Application Deployment                                             | ⭐⭐⭐         | CRUD            |       |
| Environment                                                        | ⭐⭐           | CRUD            |       |
| **ELB (Elastic Load Balancing)** (Pro)                             | [🔍]({{< ref "references/coverage#elb" >}}) |                 |       |
| Listeners                                                          | ⭐⭐⭐         | CRUD            |       |
| Load balancers                                                     | ⭐⭐⭐         | Emulated        | Application load balancers with IP address or Lambda targets only |
| Rules                                                              | ⭐⭐⭐         | CRUD            |       |
| Target groups                                                      | ⭐⭐⭐         | CRUD            |       |
| Listener certificates                                              | ⭐⭐⭐         | CRUD            |       |
| [**ELBv2 (Elastic Load Balancing v2)**]({{< ref "elastic-load-balancing" >}}) (Pro) | [🔍]({{< ref "references/coverage#elbv2" >}}) |                 |       |
| Listeners                                                          | ⭐⭐⭐         | CRUD            |       |
| Load balancers                                                     | ⭐⭐⭐         | CRUD            |       |
| Rules                                                              | ⭐⭐⭐         | CRUD            |       |
| Target groups                                                      | ⭐⭐⭐         | CRUD            |       |
| Listener certificates                                              | ⭐⭐⭐         | CRUD            |       |
| [**EMR**]({{< ref "elastic-mapreduce" >}}) (Pro)                   | [🔍]({{< ref "references/coverage#emr" >}}) |                 |       |
| Clusters                                                           | ⭐⭐⭐⭐       | Emulated        |       |
| Instance Fleets                                                    | ⭐⭐⭐         | CRUD            |       |
| Job Flow Steps                                                     | ⭐⭐⭐         | Emulated        |       |
| Managed Scaling Policies                                           | \-             |                 |       |
| Notebook Executions                                                | \-             |                 |       |
| Run Job Flows (Queries)                                            | ⭐⭐⭐         | Emulated         |       |
| Security Configurations                                            | \-             |                 |       |
| Studios                                                            | \-             |                 |       |
| Tags                                                               | ⭐⭐⭐⭐       | CRUD             |       |
| [**ES (Elasticsearch Service)**]({{< ref "elasticsearch" >}})      | [🔍]({{< ref "references/coverage#es" >}}) |                 |       |
| Cross-Cluster Search Connections                                   | \-             |                 |       |
| Elasticsearch Domains                                              | ⭐⭐⭐⭐       | Emulated        |       |
| Packages                                                           | \-             |                 |       |
| Reserved Instances                                                 | \-             |                 |       |
| Tags                                                               | ⭐⭐⭐⭐       | CRUD            |       |
| **EventBridge (Events)**                                           | [🔍]({{< ref "references/coverage#events" >}}) |                 |       |
| API Destinations                                                   | ⭐⭐⭐⭐       | Emulated                |       |
| Archives                                                           | \-             |                 |       |
| Connections                                                        | \-             |                 |       |
| Event Buses                                                        | ⭐⭐⭐⭐       | Emulated                |       |
| Event Sources                                                      | ⭐⭐⭐⭐       | Emulated                |       |
| Partner Event Sources                                              | \-             |                 |       |
| Replays                                                            | \-             |                 |       |
| Rules                                                              | ⭐⭐⭐⭐       | Emulated                |       |
| Tags                                                               | ⭐⭐⭐⭐       | CRUD                |       |
| **Firehose**                                                       | [🔍]({{< ref "references/coverage#firehose" >}}) |                 |       |
| Delivery Streams                                                   | ⭐⭐⭐⭐       | Emulated        |       |
| Destinations                                                       | ⭐⭐⭐⭐       | Emulated        |       |
| Records                                                            | ⭐⭐⭐⭐       | Emulated        |       |
| Tags                                                               | ⭐⭐⭐⭐       | CRUD            |       |
| Stream Encryption                                                  | \-           |                  |       |
| **Glacier** (Pro)                                                  | [🔍]({{< ref "references/coverage#glacier" >}}) |                 |       |
| Archive                                                            | ⭐⭐⭐⭐       | Emulated        |       |
| Vault                                                              | ⭐⭐⭐⭐       | Emulated        |       |
| Job                                                                | ⭐⭐⭐⭐       | Emulated        |       |
| Tags                                                               | ⭐⭐⭐⭐       | CRUD            |       |
| [**Glue** (Pro)]({{< ref "glue" >}})                               | [🔍]({{< ref "references/coverage#glue" >}}) |                 |       |
| Classifiers                                                        | ⭐⭐⭐         | CRUD            |       |
| Connections                                                        | ⭐⭐⭐         | CRUD            |       |
| Crawlers                                                           | ⭐⭐⭐         | Emulated        |       |
| Databases                                                          | ⭐⭐⭐         | Emulated        |       |
| Dev Endpoints                                                      | \-             |                 |       |
| Jobs                                                               | ⭐⭐⭐         | Emulated        |       |
| ML Transforms                                                      | \-             |                 |       |
| Partitions                                                         | ⭐⭐⭐         | Emulated        |       |
| Registries                                                         | ⭐⭐⭐⭐       | Emulated        |       |
| Schemas                                                            | ⭐⭐⭐⭐       | Emulated        |       |
| Scripts                                                            | \-             |                 |       |
| Security Configurations                                            | ⭐⭐⭐         | CRUD            |       |
| Tables                                                             | ⭐⭐⭐         | Emulated        |       |
| Triggers                                                           | ⭐⭐⭐         | CRUD            |       |
| Tags                                                               | ⭐⭐⭐         | CRUD            |       |
| User Defined Functions                                             | \-             |                 |       |
| Workflows                                                          | ⭐⭐⭐         | CRUD            |       |
| [**IAM**]({{< ref "iam" >}})                                       | [🔍]({{< ref "references/coverage#iam" >}}) |                 |       |
| Access Keys                                                        | ⭐⭐⭐         |    Emulated     |       |
| Account Aliases                                                    | ⭐⭐⭐         |      CRUD       |       |
| Credential Reports                                                 | \-             |                 |       |
| Groups                                                             | ⭐⭐⭐⭐       |    Emulated     |       |
| Instance Profiles                                                  | ⭐⭐⭐         |      CRUD       |       |
| Login Profiles                                                     | ⭐⭐⭐         |      CRUD       |       |
| OIDC Providers                                                     | \-             |                 |       |
| Policies                                                           | ⭐⭐⭐⭐       |    Emulated     |       |
| Roles                                                              | ⭐⭐⭐⭐       |    Emulated     |       |
| SAML Providers                                                     | \-             |                 |       |
| Server Certificates                                                | ⭐⭐⭐         |      CRUD       |       |
| Service Linked Roles                                               | ⭐⭐⭐         |      CRUD       |       |
| Users                                                              | ⭐⭐⭐⭐       |    Emulated     |       |
| Virtual MFA Devices                                                | ⭐⭐           |      CRUD       |       |
| [**IoT (Analytics, Data, Wireless)** (Pro)]({{< ref "iot" >}})     | [🔍]({{< ref "references/coverage#iot" >}}) |                 |       |
| Authorizers                                                        | \-             |                 |       |
| Billing Groups                                                     | \-             |                 |       |
| Certificates                                                       | ⭐⭐           | CRUD            |       |
| Channels                                                           | ⭐⭐           | CRUD            |       |
| Custom Metrics                                                     | \-             |                 |       |
| Datasets                                                           | ⭐⭐⭐         | CRUD            |       |
| Dimensions                                                         | \-             |                 |       |
| Domain Configurations                                              | \-             |                 |       |
| Jobs                                                               | ⭐⭐⭐         | CRUD            |       |
| Jobs Executions                                                    | ⭐⭐⭐         | CRUD            |       |
| Jobs Templates                                                     | \-             |                 |       |
| Mitigation Actions                                                 | \-             |                 |       |
| Policies                                                           | ⭐⭐⭐         | CRUD            |       |
| Provisioning Claims / Templates                                    | ⭐⭐           | CRUD            |       |
| Role Aliases                                                       | \-             |                 |       |
| Security Profiles                                                  | \-             | CRUD            |       |
| Shadows                                                            | ⭐⭐           | CRUD            |       |
| Streams                                                            | \-             |                 |       |
| Tags                                                               | ⭐⭐⭐⭐       | CRUD            |       |
| Thing Groups                                                       | ⭐⭐⭐         | CRUD            |       |
| Thing Types                                                        | ⭐⭐⭐         | CRUD            |       |
| Things                                                             | ⭐⭐⭐         | CRUD            |       |
| Topic Rules                                                        | ⭐⭐⭐         | CRUD            |       |
| [**Kafka (MSK - Managed Streaming for Kafka)**]({{< ref "managed-streaming-for-kafka" >}}) (Pro) | [🔍]({{< ref "references/coverage#kafka" >}}) |                 |       |
| Brokers                                                            | ⭐⭐           | Emulated        |       |
| Cluster Operations                                                 | ⭐⭐           | Emulated        |       |
| Clusters                                                           | ⭐⭐⭐⭐       | Emulated        | Single node clusters |
| Configurations                                                     | ⭐⭐⭐⭐       | CRUD            |       |
| Tags                                                               | ⭐⭐⭐⭐       | CRUD            |       |
| [**Kinesis**]({{< ref "kinesis" >}})                               | [🔍]({{< ref "references/coverage#kinesis" >}}) |                 |       |
| Records                                                            | ⭐⭐⭐⭐       | Emulated                |       |
| Split / Merge Shards                                               | ⭐⭐⭐⭐       | Emulated                |       |
| Stream Consumers                                                   | ⭐⭐⭐⭐       | Emulated                |       |
| Stream Encryption                                                  | \-             |                 |       |
| Streams                                                            | ⭐⭐⭐⭐       | Emulated                |       |
| Subscribe to Shard                                                 | ⭐⭐⭐⭐       | Emulated                |       |
| Tags                                                               | ⭐⭐⭐⭐       | CRUD            |       |
| **Kinesis Analytics** (Pro)                                        | [🔍]({{< ref "references/coverage#kinesisanalytics" >}})  |                 |       |
| Applications                                                       | ⭐⭐⭐         | Emulated            |       |
| Tags                                                               | ⭐⭐⭐⭐       | CRUD            |       |
| **Kinesis Analytics v2** (Pro)                                     | [🔍]({{< ref "references/coverage#kinesisanalyticsv2" >}}) |                 |       |
| Applications                                                       | ⭐⭐⭐         | Emulated            |       |
| Tags                                                               | ⭐⭐⭐⭐       | CRUD            |       |
| **KMS**                                                            | [🔍]({{< ref "references/coverage#kms" >}}) |                 |       |
| Aliases                                                            | ⭐⭐⭐⭐       | CRUD             |       |
| Custom Key Stores                                                  | ⭐⭐⭐         | Emulated         |       |
| Encrypt / Decrypt / Sign Data                                      | ⭐⭐⭐⭐       | Emulated         |       |
| Grants                                                             | \-             |                 |       |
| Key Policies                                                       | \-             |                 |       |
| Keys                                                               | ⭐⭐⭐⭐       | Emulated         |       |
| Tags                                                               | ⭐⭐⭐⭐       | CRUD             |       |
| **Lake Formation** (Pro)                                           | [🔍]({{< ref "references/coverage#lakeformation" >}}) |                 |       |
| Transactions                                                       | \-             |                 |       |
| Permissions                                                        | ⭐⭐             | CRUD                |       |
| Resources                                                          | ⭐⭐             | CRUD                |       |
| [**Lambda**]({{< ref "lambda" >}})                                 | [🔍]({{< ref "references/coverage#lambda" >}}) |                 |       |
| Aliases                                                            | ⭐⭐⭐⭐       | CRUD            |       |
| Code Signing Configs                                               | ⭐⭐           | CRUD            |       |
| Custom Images (Pro)                                                | ⭐⭐⭐⭐       | Emulated        |       |
| Event Invoke Configs (Destinations)                                | ⭐⭐⭐⭐       | Emulated        |       |
| Event Source Mappings                                              | ⭐⭐⭐⭐       | Emulated        |       |
| Function Concurrencies                                             | ⭐⭐⭐         | CRUD            |       |
| Function URLs                                                      | ⭐⭐⭐⭐       | Emulated        |       |
| Functions                                                          | ⭐⭐⭐⭐       | Emulated        |       |
| Invoke Functions                                                   | ⭐⭐⭐⭐       | Emulated        |       |
| [Layers (Pro)]({{< ref "lambda#lambda-layers" >}})                 | ⭐⭐⭐⭐       | Emulated        |       |
| Permissions                                                        | ⭐⭐⭐⭐       | CRUD            |       |
| Tags                                                               | ⭐⭐⭐⭐       | CRUD            |       |
| [**Logs**]({{< ref "logs" >}})                                     | [🔍]({{< ref "references/coverage#logs" >}}) |                 |       |
| Destinations                                                       | ⭐⭐⭐⭐       | Emulated       |       |
| Export Tasks                                                       | ⭐⭐          | CRUD            |       |
| Log Events                                                         | ⭐⭐⭐⭐       | Emulated        |       |
| Log Groups                                                         | ⭐⭐⭐⭐       | CRUD                |       |
| Log Streams                                                        | ⭐⭐⭐⭐       | CRUD                |       |
| Metric Filters                                                     | ⭐⭐⭐         | CRUD                |       |
| Queries                                                            | ⭐⭐          | CRUD                |       |
| Resource Policies                                                  | ⭐⭐⭐        | CRUD               |       |
| Retention Policies                                                 | ⭐⭐⭐         | CRUD                |       |
| Subscription Filters                                               | ⭐⭐⭐         | Emulated        |       |
| Tags                                                               | ⭐⭐⭐⭐       | CRUD               |       |
| **MediaStore** (Pro)                                               | [🔍]({{< ref "references/coverage#mediastore" >}}) |                 |       |
| Access Logging                                                     | \-             |                 |       |
| Container Policies                                                 | \-             |                 |       |
| Containers                                                         | ⭐⭐⭐         | CRUD                |       |
| CORS Policies                                                      | \-             |                 |       |
| Lifecycle Policies                                                 | \-             |                 |       |
| Metric Policies                                                    | \-             |                 |       |
| Tags                                                               | \-             |                 |       |
| **MediaStore Data** (Pro)                                          | [🔍]({{< ref "references/coverage#mediastore-data" >}}) |                 |       |
| Objects                                                            | ⭐⭐⭐         | CRUD            |       |
| **MWAA (Managed Workflows for Apache Airflow)** (Pro)              | [🔍]({{< ref "references/coverage#mwaa" >}}) |                 |       |
| CLI Tokens                                                         | -              |                 |       |
| Environments                                                       | ⭐⭐⭐          | Emulated       |       |
| S3 integration (DAG bucket/paths)                                  | ⭐⭐⭐          | Emulated       |       |
| Tags                                                               | ⭐⭐⭐⭐        | CRUD           |       |
| Web Login                                                          | ⭐⭐⭐          | Emulated       |       |
| [**Neptune DB** (Pro)]({{< ref "neptune" >}})                      | [🔍]({{< ref "references/coverage#neptune" >}}) |                 |       |
| DB Clusters                                                        | ⭐⭐⭐⭐       | Emulated        |       |
| DB Cluster Endpoints                                               | ⭐⭐⭐⭐       | Emulated        |       |
| DB Cluster Parameter Groups                                        | ⭐⭐⭐        | CRUD             |       |
| DB Cluster Snapshots                                               | ⭐⭐          | Emulated         |       |
| Event Subscriptions                                                | ⭐⭐          | CRUD             |       |
| Events                                                             | \-             |                 |       |
| Global Clusters                                                    | \-             |                 |       |
| PendingMaintenanceAction                                           | \-             |                 |       |
| Tags                                                               | ⭐⭐⭐⭐       | CRUD                |       |
| [**OpenSearch Service**]({{< ref "opensearch" >}})                 | [🔍]({{< ref "references/coverage#opensearch" >}}) |                 |       |
| Cross-Cluster Search Connections                                   | \-             |                 |       |
| OpenSearch Domains                                                 | ⭐⭐⭐⭐       | Emulated        |       |
| Packages                                                           | \-             |                 |       |
| Reserved Instances                                                 | \-             |                 |       |
| Tags                                                               | ⭐⭐⭐⭐       | CRUD            |       |
| **Organizations** (Pro)                                            | [🔍]({{< ref "references/coverage#organizations" >}}) |                 |       |
| Accounts                                                           | ⭐⭐⭐          | CRUD            |        |
| Handshakes                                                         |  \-            |                 |        |
| Organization                                                       | ⭐⭐           | CRUD            |        |
| Organizational Units                                               | ⭐⭐           | CRUD            |        |
| Policies                                                           | ⭐⭐⭐         | CRUD            |        |
| Tags                                                               | ⭐⭐⭐⭐       | CRUD            |        |
| [**QLDB** (Pro)]({{< ref "qldb" >}})                               | [🔍]({{< ref "references/coverage#qldb" >}}) |                 |       |
| Blocks                                                             | ⭐⭐⭐         | Emulated                 |       |
| Digests                                                            | ⭐⭐⭐         | CRUD                |       |
| Journal Kinesis Streams                                            | ⭐⭐⭐         | CRUD                |       |
| Journal S3 Exports                                                 | ⭐⭐⭐         | CRUD                |       |
| Ledgers                                                            | ⭐⭐⭐⭐       | Emulated        |       |
| Send Commands / Run Queries                                        | ⭐⭐⭐⭐       | Emulated        |       |
| Tags                                                               | ⭐⭐⭐⭐       | CRUD            |       |
| **QLDB Sessions** (Pro)                                            | [🔍]({{< ref "references/coverage#qldb-session" >}}) |             |
| Send Command                                                       | ⭐⭐⭐⭐       | Emulated
| [**RDS / Aurora Serverless** (Pro)]({{< ref "rds" >}})             | [🔍]({{< ref "references/coverage#rds" >}}) |                 |       |
| DB/Cluster Parameter Groups                                        | ⭐⭐⭐         | CRUD            |       |
| DB/Cluster Snapshots                                               | ⭐⭐⭐         | Emulated        |       |
| DB Clusters/Instances                                              | ⭐⭐⭐⭐       | Emulated        |       |
| DB Proxies                                                         | ⭐⭐           | Emulated       |       |
| DB Security/Subnet Groups                                          | ⭐⭐⭐         | Emulated        |       |
| Event Subscriptions                                                | ⭐⭐           | CRUD            |       |
| Option Groups                                                      | ⭐⭐⭐⭐       | CRUD            |       |
| Postgres AWS Extension Functions                                   | ⭐⭐⭐         | Emulated        |       |
| Tags                                                               | ⭐⭐⭐⭐       | CRUD            |       |
| **RDS Data** (Pro)                                                 | [🔍]({{< ref "references/coverage#rds-data" >}}) |                 |       |
| Execute sql/statements                                             | ⭐⭐⭐         | Emulated               |       |
| Transactions                                                       | ⭐⭐           | Emulated                |       |
| Batch Execution                                                    | \-             |                 |       |
| **Redshift**  (Pro)                                                | [🔍]({{< ref "references/coverage#redshift" >}}) |                 |       |
| Authorize/Revoke Access                                            | \-             |                 |       |
| Cluster Parameter Groups                                           | ⭐⭐⭐         | Emulated         |       |
| Cluster Snapshots                                                  | ⭐⭐          | CRUD             |       |
| Clusters/Instances                                                 | ⭐⭐⭐⭐       | Emulated                |       |
| Event Subscriptions                                                | \-             |                 |       |
| HSM Configurations                                                 | \-             |                 |       |
| Partners                                                           | \-             |                 |       |
| Security/Subnet Groups                                             | ⭐⭐⭐         | CRUD             |       |
| Tags                                                               | ⭐⭐⭐⭐       | CRUD            |       |
| Usage Limits                                                       | \-           |                 |       |
| **Redshift Data** (Pro)                                            | [🔍]({{< ref "references/coverage#redshift-data" >}}) |                 |       |
| Statements                                                         | ⭐⭐⭐         | Emulated          |       |
| Describe Table                                                     | ⭐⭐⭐         | Emulated         |       |
| Batch Execution                                                    | \-             |                 |       |
| **Resource Groups**                                                | [🔍]({{< ref "references/coverage#resource-groups" >}}) |                 |       |
| Resources                                                          | ⭐⭐⭐         | CRUD                |       |
| Groups                                                             | ⭐⭐⭐         | CRUD                |       |
| Group Configurations                                               | ⭐⭐⭐         | CRUD                |       |
| Tags                                                               | ⭐⭐           | CRUD                |       |
| **Resource Groups Tagging API**                                    | [🔍]({{< ref "references/coverage#resourcegroupstaggingapi" >}})  |                 |       |
| Reports                                                            | \-             |                 |       |
| Tags                                                               | ⭐⭐           | CRUD                |       |
| [**Route53**]({{< ref "route53" >}})                               | [🔍]({{< ref "references/coverage#route53" >}}) |                 |       |
| DNS Server Integration (Pro)                                       | ⭐⭐⭐⭐       | Emulated       |       |
| Geo Locations                                                      | \-             |                |       |
| Health Checks                                                      | ⭐⭐           | CRUD           |       |
| Hosted Zones                                                       | ⭐⭐⭐⭐       | CRUD           |       |
| Query Logging Configs                                              | \-             |                |       |
| Resource Record Sets                                               | ⭐⭐⭐⭐       | CRUD           |       |
| Reusable Delegation Sets                                           | ⭐⭐⭐         | CRUD           |       |
| Tags                                                               | ⭐⭐⭐⭐       | CRUD           |       |
| Traffic Policies                                                   | ⭐⭐⭐         | CRUD           |       |
| **Route53 Resolver**                                               | [🔍]({{< ref "references/coverage#route53resolver" >}}) |                |       |
| [**S3**]({{< ref "s3" >}})                                         | [🔍]({{< ref "references/coverage#s3" >}}) |                 |       |
| Bucket ACLs                                                        | ⭐⭐⭐         | Emulated       |       |
| Bucket CORS                                                        | ⭐⭐⭐         | Emulated       |       |
| Bucket Encryptions                                                 | ⭐⭐⭐         | Emulated       |       |
| Bucket Lifecycles                                                  | ⭐⭐⭐         | Emulated       |       |
| Bucket Loggings                                                    | ⭐⭐⭐         | Emulated       |       |
| Bucket Metrics Configurations                                      | ⭐⭐⭐         | Emulated       |       |
| Bucket Notifications                                               | ⭐⭐⭐         | Emulated       | Supported notification targets: SQS, SNS, Lambda; Supported notification events: ObjectCreated, ObjectRemoved, ObjectTagging     |
| Bucket Ownership Controls                                          | ⭐⭐⭐         | Emulated       |       |
| Bucket Policies                                                    | ⭐⭐⭐         | Emulated       |       |
| Bucket Replications                                                | ⭐⭐⭐         | Emulated       |       |
| Bucket Request Payments                                            | ⭐⭐⭐         | Emulated       |       |
| Bucket Versionings                                                 | ⭐⭐⭐         | Emulated       |       |
| Bucket Websites                                                    | ⭐⭐⭐         | Emulated       |       |
| Buckets                                                            | ⭐⭐⭐⭐       | Emulated       |       |
| Object Retentions                                                  | ⭐⭐           | Emulated       |       |
| Object Versions                                                    | ⭐⭐⭐⭐       | Emulated       |       |
| Objects                                                            | ⭐⭐⭐⭐       | Emulated       |       |
| Presigned URLs                                                     | ⭐⭐⭐⭐       | Emulated       |       |
| Tags                                                               | ⭐⭐⭐⭐       | Emulated       |       |
| Upload/Download Files                                              | ⭐⭐⭐⭐       | Emulated       |       |
| **S3 Control**                                                     | [🔍]({{< ref "references/coverage#s3control" >}}) |                 |       |
| Access Point Policies                                              | ⭐⭐           | CRUD            |       |
| Access Points                                                      | ⭐⭐           | CRUD            |       |
| Jobs                                                               | \-             |                 |       |
| Lifecycle configurations                                           | \-             |                 |       |
| Multi-region Access Points                                         | \-             |                 |       |
| Public Access Blocks                                               | ⭐⭐           | CRUD            |       |
| Storage Lens                                                       | \-             |                 |       |
| [**SageMaker** (Pro)]({{< ref "sagemaker" >}})                     | [🔍]({{< ref "references/coverage#sagemaker" >}}) |                 |       |
| Actions                                                            | \-             |                 |       |
| Algorithms                                                         | \-             |                 |       |
| App Image Configs                                                  | \-             |                 |       |
| Apps                                                               | \-             |                 |       |
| Artifacts                                                          | \-             |                 |       |
| Associations                                                       | \-             |                 |       |
| Auto ML Jobs                                                       | \-             |                 |       |
| Code Repositories                                                  | \-             |                 |       |
| Compilation Jobs                                                   | \-             |                 |       |
| Contexts                                                           | \-             |                 |       |
| Data Quality Job Definitions                                       | \-             |                 |       |
| Device Fleets                                                      | \-             |                 |       |
| Devices                                                            | \-             |                 |       |
| Domains                                                            | \-             |                 |       |
| Edge Packaging Jobs                                                | \-             |                 |       |
| Endpoints / Endpoint Configs                                       | ⭐⭐           | CRUD            |       |
| Experiments                                                        | \-             |                 |       |
| Feature Groups                                                     | \-             |                 |       |
| Flow Definitions                                                   | \-             |                 |       |
| Hyper Parameter Tuning Jobs                                        | \-             |                 |       |
| Images / Image Versions                                            | \-             |                 |       |
| Labelling Jobs                                                     | \-             |                 |       |
| Model Bias/Explainability Jobs                                     | \-             |                 |       |
| Model Packages                                                     | \-             |                 |       |
| Models                                                             | ⭐⭐           | CRUD            |       |
| Monitoring Executions/Schedules                                    | \-             |                 |       |
| Notebook Instances                                                 | ⭐⭐           | CRUD            |       |
| Pipeline Executions                                                | \-             |                 |       |
| Pipelines                                                          | \-             |                 |       |
| Projects                                                           | \-             |                 |       |
| Tags                                                               | \-             |                 |       |
| Training Jobs                                                      | ⭐⭐           | Emulated        |       |
| Transform Jobs                                                     | \-             |                 |       |
| Trials                                                             | ⭐⭐           | CRUD            |       |
| User Profiles                                                      | \-             |                 |       |
| Workforces / Workteams                                             | \-             |                 |       |
| **SecretsManager**                                                 | [🔍]({{< ref "references/coverage#secretsmanager" >}}) |                 |       |
| Resource Policies                                                  | ⭐⭐⭐⭐       | CRUD                 |       |
| Secret Replications                                                | ⭐⭐           | CRUD                |       |
| Secret Rotations                                                   | ⭐⭐           | CRUD                |       |
| Secrets                                                            | ⭐⭐⭐⭐       | CRUD                |       |
| Tags                                                               | ⭐⭐⭐⭐       | CRUD                |       |
| **Serverless Repo** (Pro)                                          | [🔍]({{< ref "references/coverage#serverlessrepo" >}}) |                 |       |
| Applications                                                       | ⭐⭐⭐         | CRUD                |       |
| Application Policies                                               | \-             |                |       |
| CloudFormation templates                                           | ⭐⭐⭐         | Emulated                |       |
| **Service Discovery (CloudMap)** (Pro)                             | [🔍]({{< ref "references/coverage#servicediscovery" >}}) |                 |       |
| Namespaces                                                         | ⭐⭐⭐         | CRUD                |       |
| [**SES**]({{< ref "ses" >}})                                       | [🔍]({{< ref "references/coverage#ses" >}}) |                 |       |
| Configuration Sets                                                 | ⭐⭐⭐         | CRUD               |       |
| Identities                                                         | ⭐⭐           | CRUD               |       |
| Identity Policies                                                  | ⭐⭐           | CRUD               |       |
| Quotas / Statistics                                                | ⭐⭐           | CRUD               |       |
| Receipt Filters                                                    | ⭐⭐⭐         | CRUD               |       |
| Receipt Rules                                                      | ⭐⭐⭐         | CRUD               |       |
| Sending Emails via SMTP (Pro)                                      | ⭐⭐⭐⭐       | Emulated           |       |
| Templates                                                          | ⭐⭐⭐⭐       | CRUD               |       |
| **SESv2 (Pro)**                                                   | [🔍]({{< ref "references/coverage#sesv2" >}}) |                 |       |
| Identities                                                         | ⭐⭐           | CRUD               |       |
| Sending Emails via SMTP                                            | ⭐⭐⭐⭐       | Emulated           |       |
| Templates                                                          | ⭐⭐⭐⭐       | CRUD               |       |
| **SNS**                                                            | [🔍]({{< ref "references/coverage#sns" >}}) |                 |       |
| Platform Applications                                              | ⭐⭐⭐         |  CRUD               |       |
| Publish/Subscribe to Topics                                        | ⭐⭐⭐⭐       |  Emulated               |       |
| SMS Attributes / Sandbox Accounts                                  | ⭐⭐           |  CRUD               |       |
| Subscriptions                                                      | ⭐⭐⭐⭐       |   Emulated             |       |
| Tags                                                               | ⭐⭐⭐⭐       |   CRUD              |       |
| Topics                                                             | ⭐⭐⭐⭐       |   CRUD              |       |
| [**SQS**]({{< ref "sqs" >}})                                       | [🔍]({{< ref "references/coverage#sqs" >}}) |                 |       |
| FIFO Queues                                                        | ⭐⭐⭐⭐       | Emulated        |       |
| Message Deduplication                                              | ⭐⭐⭐⭐       | Emulated        |       |
| Message Visibility                                                 | ⭐⭐⭐⭐⭐     | Emulated        |       |
| Messages                                                           | ⭐⭐⭐⭐⭐     | Emulated        |       |
| Permission                                                         | ⭐⭐⭐         | CRUD            |       |
| Query API                                                          | ⭐⭐⭐⭐       | Emulated        |       |
| Standard Queues                                                    | ⭐⭐⭐⭐       | Emulated        |       |
| Tags                                                               | ⭐⭐⭐⭐       | CRUD            |       |
| [**SSM**]({{< ref "systems-manager" >}})                           | [🔍]({{< ref "references/coverage#ssm" >}}) |                 |       |
| Associations                                                       | ⭐⭐⭐         | CRUD                |       |
| Calendar States                                                    | ⭐⭐           | CRUD                |       |
| Commands / Command Invocations                                     | ⭐⭐⭐         | CRUD                |       |
| Compliance Items                                                   | ⭐⭐           | CRUD                |       |
| Documents                                                          | ⭐⭐⭐         | CRUD                |       |
| Inventory Entries                                                  | \-             |                 |       |
| Ops Metadata                                                       | ⭐⭐           | CRUD                |       |
| Parameters                                                         | ⭐⭐⭐⭐       | CRUD                |       |
| Resource Compliance Summaries                                      | \-             |                 |       |
| Tags                                                               | ⭐⭐⭐⭐       | CRUD                |       |
| **StepFunctions**                                                  | [🔍]({{< ref "references/coverage#stepfunctions" >}}) |                 |       |
| Activities                                                         | ⭐⭐⭐⭐       | Emulated                |       |
| Executions / Execution History                                     | ⭐⭐⭐⭐       | Emulated                |       |
| State Machines                                                     | ⭐⭐⭐⭐       | Emulated                |       |
| Tags                                                               | ⭐⭐⭐⭐       | Emulated                |       |
| **STS**                                                            | [🔍]({{< ref "references/coverage#sts" >}})  |                 |       |
| Assume Role (Pro)                                                  | ⭐⭐⭐⭐       | Emulated                |       |
| Get Access Key Info                                                | \-             |                 |       |
| Get Caller Identity                                                | ⭐⭐⭐⭐       | Emulated                |       |
| Session Tokens                                                     | ⭐⭐⭐⭐       | CRUD                |       |
| **Support**                                                        | [🔍]({{< ref "references/coverage#support" >}}) |                 |       |
| Cases                                                              | ⭐⭐⭐         | CRUD                |       |
| TrustedAdvisorChecks                                               | ⭐⭐           | CRUD                |       |
| Attachments                                                        | \-             |                 |       |
| **SWF**                                                            | [🔍]({{< ref "references/coverage#swf" >}}) |                 |       |
| Domain                                                             | ⭐⭐⭐         | CRUD                |       |
| Activity                                                           | ⭐⭐⭐         | CRUD                |       |
| Workflows                                                          | ⭐⭐⭐         | CRUD                |       |
| Domains                                                            | ⭐⭐⭐         | CRUD                |       |
| [**Timestream (query, write)**]({{< ref "timestream" >}}) (Pro)    | [🔍]({{< ref "references/coverage#timestream-query" >}}) |                 |       |
| Databases                                                          | ⭐⭐⭐         | Emulated                |       |
| Run Query                                                          | ⭐⭐⭐         | Emulated                |       |
| Tables                                                             | ⭐⭐⭐         | Emulated                |       |
| Tags                                                               | ⭐⭐⭐         | CRUD               |       |
| Write Records                                                      | ⭐⭐⭐         | Emulated                |       |
| [**Transfer** (Pro)]({{< ref "transfer" >}})                       | [🔍]({{< ref "references/coverage#transfer" >}}) |                 |       |
| Accesses                                                           | \-             |                 |       |
| Security Policies                                                  | \-             |                 |       |
| Servers                                                            | ⭐⭐⭐         | Emulated                |       |
| SSH Public Keys                                                    | ⭐⭐⭐         | CRUD                |       |
| Tags                                                               | \-             |                 |       |
| Users                                                              | ⭐⭐⭐         | Emulated                |       |
| [**XRay** (Pro)]({{< ref "xray-tracing" >}})                       | [🔍]({{< ref "references/coverage#xray" >}}) |                 |       |
| Encryption Configs                                                 | \-             |                 |       |
| Groups                                                             | \-           |                 |       |
| Insights                                                           | \-             |                 |       |
| Sampling Rules                                                     | ⭐⭐⭐         | CRUD                |       |
| Service Graph                                                      | \-             |                 |       |
| Tags                                                               | \-             |                 |       |
| Telemetry Records                                                  | ⭐⭐⭐⭐       | Emulated                |       |
| Trace Graph                                                        | \-             |                 |       |
| Trace Segments / Summaries                                         | ⭐⭐⭐         | CRUD                |       |

