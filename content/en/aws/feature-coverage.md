---
title: "AWS Service Feature Coverage"
linkTitle: "⭐ Feature Coverage"
weight: 1
description: >
  Overview of the implemented AWS APIs and their level of parity with the AWS cloud
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
| **ACM**                                                            | [🔍]({{< ref "../localstack/metric-coverage/#acm" >}})      |                 |       |
| Certificates                                                       | ⭐⭐⭐              | CRUD            |       |
| Tags                                                               | ⭐⭐⭐⭐            | CRUD            |       |
| Account Configuration                                              | ⭐⭐                | CRUD            |       |
| [**Amplify** (Pro)]({{< ref "amplify" >}})                         | [🔍]({{< ref "../localstack/metric-coverage/#amplify" >}})  |                 |       |
| Apps                                                               | ⭐⭐⭐⭐             | Emulated        |       |
| Backend Environments                                               | ⭐⭐⭐               | CRUD            |       |
| Branches                                                           | ⭐⭐⭐              | CRUD            |       |
| Deployments                                                        | \-                 |                 |       |
| Domain Associations                                                | \-                 |                 |       |
| Jobs                                                               | \-                 |                 |       |
| Tags                                                               | ⭐⭐⭐⭐             | CRUD            |       |
| Webhooks                                                           | ⭐⭐⭐               | Emulated       |       |
| **API Gateway**                                                    | [🔍]({{< ref "../localstack/metric-coverage/#apigateway" >}}) |                 |       |
| API Keys                                                           | ⭐⭐⭐              |                 |       |
| Authorizers (Pro)                                                  | ⭐⭐⭐⭐             |                 |       |
| Base Path Mappings                                                 | ⭐⭐⭐⭐             |                 |       |
| Deployments                                                        | ⭐⭐⭐⭐            |                 |       |
| Documentation Parts                                                | ⭐⭐⭐              |                 |       |
| Documentation Versions                                             | ⭐⭐⭐              |                 |       |
| Domain Names                                                       | ⭐⭐⭐              |                 |       |
| Gateway / Integration / Method Responses                           | ⭐⭐⭐⭐             |                 |       |
| Integrations                                                       | ⭐⭐⭐⭐             |                 |       |
| Methods                                                            | ⭐⭐⭐⭐             |                 |       |
| Models                                                             | ⭐⭐⭐              |                 |       |
| Request Validators                                                 | ⭐⭐                |                 |       |
| Resources                                                          | ⭐⭐⭐⭐             |                 |       |
| REST APIs                                                          | ⭐⭐⭐⭐             |                 |       |
| Stages                                                             | ⭐⭐⭐⭐             |                 |       |
| Tags                                                               | ⭐⭐⭐⭐             |                 |       |
| Usage Plans                                                        | ⭐⭐⭐               |                 |       |
| Usage Plan Keys                                                    | ⭐⭐⭐               |                 |       |
| VPC Links                                                          | ⭐⭐⭐               |                 |       |
| [**API Gateway v2** (Pro)]({{< ref "apigatewayv2" >}})             | [🔍]({{< ref "../localstack/metric-coverage/#apigatewayv2" >}})     |                 |       |
| APIs                                                               | ⭐⭐⭐⭐              |                 |       |
| API Mappings                                                       | ⭐⭐⭐                |                 |       |
| Authorizers                                                        | ⭐⭐⭐⭐              |                 |       |
| Deployments                                                        | ⭐⭐⭐⭐              |                 |       |
| Domain Names                                                       | ⭐⭐⭐               |                 |       |
| Import APIs from OpenAPI specs                                     | ⭐⭐⭐               |                 |       |
| Integrations                                                       | ⭐⭐⭐               |                 |       |
| Integration Responses                                              | ⭐⭐⭐               |                 |       |
| Models                                                             | ⭐⭐⭐               |                 |       |
| Routes                                                             | ⭐⭐⭐⭐              |                 |       |
| Route Responses                                                    | ⭐⭐⭐               |                 |       |
| Stages                                                             | ⭐⭐⭐⭐              |                 |       |
| Tags                                                               | ⭐⭐⭐⭐              |                 |       |
| VPC Links                                                          | ⭐⭐⭐               |                 |       |
| **API Gateway Management API** (Pro)                               | [🔍]({{< ref "../localstack/metric-coverage/#apigatewaymanagementapi" >}}) |                 |       |
| **AppConfig** (Pro)                                                | [🔍]({{< ref "../localstack/metric-coverage/#appconfig" >}})               |                 |       |
| Applications                                                       | ⭐⭐⭐           |                 |       |
| Configuration Profiles                                             | ⭐⭐⭐⭐         |                 |       |
| Configurations                                                     | ⭐⭐⭐           |                 |       |
| Deployment Strategies                                              | ⭐⭐⭐⭐         |                 |       |
| Deployments                                                        | ⭐⭐⭐           |                 |       |
| Environments                                                       | ⭐⭐⭐⭐          |                 |       |
| Hosted Configuration Versions                                      | ⭐⭐⭐           |                 |       |
| Tags                                                               | ⭐⭐⭐⭐         |                 |       |
| **Application Autoscaling** (Pro)                                  | [🔍]({{< ref "../localstack/metric-coverage/#application-autoscaling" >}})     |                 |       |
| Scalable Targets                                                   | ⭐⭐⭐           | CRUD           |       |
| Scaling Activities                                                 | \-              |                |       |
| Scaling Policies                                                   | ⭐⭐⭐           | CRUD            |       |
| Scheduled Actions                                                  | ⭐⭐⭐           | CRUD             |       |
| [**AppSync** (Pro)]({{< ref "appsync" >}})                         | [🔍]({{< ref "../localstack/metric-coverage/#appsync" >}})                |                 |       |
| API Caches                                                         | ⭐⭐⭐          |                 |       |
| API Keys                                                           | ⭐⭐⭐          |                 |       |
| Data Sources                                                       | ⭐⭐⭐          |                 |       |
| Functions                                                          | ⭐⭐⭐          |                 |       |
| GraphQL APIs                                                       | ⭐⭐⭐⭐         |                 |       |
| Resolvers                                                          | ⭐⭐⭐⭐         |                 |       |
| Tags                                                               | ⭐⭐⭐⭐         |                 |       |
| Types                                                              | ⭐⭐⭐⭐         |                 |       |
| [**Athena** (Pro)]({{< ref "athena" >}})                           | [🔍]({{< ref "../localstack/metric-coverage/#athena" >}}) |                 |       |
| Data Catalogs                                                      | ⭐⭐           | CRUD            |       |
| Databases                                                          | ⭐⭐           | Emulated        |       |
| Named Queries                                                      | \-             |                 |       |
| Prepared Statements                                                | \-             |                 |       |
| Query Executions                                                   | ⭐⭐⭐         | Emulated        |       |
| Table Metadata                                                     | \-             |                 |       |
| Tags                                                               | ⭐⭐⭐         | CRUD            |       |
| Work Groups                                                        | \-             |                 |       |
| **Autoscaling** (Pro)                                              | [🔍]({{< ref "../localstack/metric-coverage/#autoscaling" >}}) |                 |       |
| Metric Collection                                                  | ⭐⭐⭐         | CRUD            |       |
| Autoscaling Groups                                                 | ⭐⭐           | CRUD            |       |
| Loadbalancer                                                       | ⭐⭐⭐         | CRUD            |       |
| [**Backup** (Pro)]({{< ref "backup" >}})                           | [🔍]({{< ref "../localstack/metric-coverage/#backup" >}}) |                 |       |
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
| **Batch** (Pro)                                                    | [🔍]({{< ref "../localstack/metric-coverage/#batch" >}}) |                 |       |
| Compute Environments                                               | ⭐⭐⭐         | CRUD            |       |
| Job Queues                                                         | ⭐⭐⭐         | CRUD            |       |
| Job Definitions                                                    | ⭐⭐⭐         | CRUD            |       |
| Jobs                                                               | ⭐⭐⭐         | Emulated        |       |
| **CE (Cost Explorer API)** (Pro)                                   | [🔍]({{< ref "../localstack/metric-coverage/#ce" >}}) |                 |       |
| Anomaly Monitoring                                                 | ⭐⭐⭐         | CRUD            |       |
| Anomaly Subscription                                               | ⭐⭐⭐         | CRUD            |       |
| Cost Category                                                      | ⭐⭐           | CRUD            |       |
| Cost Usage/Forecast                                                | \-             |                 |       |
| Savings Plan                                                       | \-             |                 |       |
| [**CloudFormation**]({{< ref "cloudformation" >}})                 | [🔍]({{< ref "../localstack/metric-coverage/#cloudformation" >}}) |                 |       |
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
| [**CloudFront** (Pro)]({{< ref "cloudfront" >}})                   | [🔍]({{< ref "../localstack/metric-coverage/#cloudfront" >}}) |                 |       |
| Cache Policies                                                     | \-             |                 |       |
| Distributions                                                      | ⭐⭐⭐         |                 |       |
| Field Level Encryption                                             | \-             |                 |       |
| Functions                                                          | ⭐⭐⭐         |                 |       |
| Invalidations                                                      | ⭐⭐⭐         |                 |       |
| Key Groups                                                         | \-             |                 |       |
| Monitoring Subscriptions                                           | \-             |                 |       |
| Origin Access Identities                                           | ⭐⭐           |                 |       |
| Origin Request Policies                                            | ⭐⭐⭐         |                 |       |
| Public Keys                                                        | \-             |                 |       |
| Realtime Log Configs                                               | \-             |                 |       |
| Streaming Distributions                                            | \-             |                 |       |
| Tags                                                               | ⭐⭐⭐⭐       |                 |       |
| **CloudTrail** (Pro)                                               | [🔍]({{< ref "../localstack/metric-coverage/#cloudtrail" >}}) |                 |       |
| Event Selectors                                                    | ⭐⭐⭐         |                 |       |
| Insight Selectors                                                  | \-             |                 |       |
| Tags                                                               | ⭐⭐⭐⭐       |                 |       |
| Trails                                                             | ⭐⭐⭐         |                 |       |
| Start/Stop Logging                                                 | ⭐⭐⭐         |                 |       |
| [**CloudWatch**]({{< ref "cloudwatch" >}})                         | [🔍]({{< ref "../localstack/metric-coverage/#cloudwatch" >}}) |                 |       |
| Alarms                                                             | ⭐⭐⭐⭐        | Emulated       |       |
| Alarm Histories                                                    | \-             |                 |       |
| Anomaly Detectors                                                  | \-             |                 |       |
| Dashboards                                                         | \-             |                 |       |
| Insight Rules                                                      | \-             |                 |       |
| Metric Data                                                        | ⭐⭐⭐⭐         | CRUD         |       |
| Metric Statistics                                                  | ⭐⭐⭐⭐          | CRUD             |       |
| Metric Streams                                                     | \-             |                 |       |
| Tags                                                               | ⭐⭐⭐⭐         | CRUD            |       |
| [**CodeCommit** (Pro)]({{< ref "codecommit" >}})                   | [🔍]({{< ref "../localstack/metric-coverage/#codecommit" >}})                |                 |       |
| Approval Rules                                                     | \-             |                 |       |
| Blobs / Files / Folders                                            | ⭐⭐           |                 |       |
| Branches                                                           | ⭐⭐           |                 |       |
| Comments                                                           | \-             |                 |       |
| Commits                                                            | ⭐⭐           |                 |       |
| Merge Commits / Conflicts                                          | \-             |                 |       |
| Pull Requests                                                      | \-             |                 |       |
| Repositories                                                       | ⭐⭐⭐         |                 |       |
| Tags                                                               | ⭐⭐⭐⭐       |                 |       |
| [**Cognito Identity** (Pro)]({{< ref "cognito" >}})                | [🔍]({{< ref "../localstack/metric-coverage/#cognito-identity" >}}) |                 |       |
| Developer Identities                                               | \-             |                 |       |
| Identities                                                         | ⭐⭐⭐         |                 |       |
| Identity Pool Roles                                                | \-             |                 |       |
| Identity Pools                                                     | ⭐⭐⭐⭐       |                 |       |
| OpenID Tokens                                                      | \-             |                 |       |
| Tags                                                               | \-             |                 |       |
| [**Cognito Identity Provider (IdP)** (Pro)]({{< ref "cognito" >}}) | [🔍]({{< ref "../localstack/metric-coverage/#cognito-idp" >}}) |                 |       |
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
| **Config**                                                         | [🔍]({{< ref "../localstack/metric-coverage/#config" >}}) |                 |       |
| **DocumentDB** (Pro)                                               | [🔍]({{< ref "../localstack/metric-coverage/#docdb" >}}) |                 |       |
| DB/Cluster Parameter Groups                                        | ⭐⭐⭐         |                 |       |
| DB/Cluster Snapshots                                               | ⭐            |                 |       |
| DB Clusters/Instances                                              | ⭐⭐⭐⭐       |                 |       |
| DB Subnet Groups                                                   | ⭐⭐          |                 |       |
| Event Subscriptions                                                | \-           |                 |       |
| Tags                                                               | ⭐⭐⭐⭐       |                 |       |
| **DynamoDB**                                                       | [🔍]({{< ref "../localstack/metric-coverage/#dynamodb" >}}) |                 |       |
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
| **DynamoDB Streams**                                               | [🔍]({{< ref "../localstack/metric-coverage/#dynamodbstreams" >}}) |                 |       |
| Records                                                            | ⭐⭐⭐⭐       |                 |       |
| Shard Iterators                                                    | ⭐⭐⭐⭐       |                 |       |
| Streams                                                            | ⭐⭐⭐⭐       |                 |       |
| [**EC2**]({{< ref "elastic-compute-cloud" >}})                      | [🔍]({{< ref "../localstack/metric-coverage/#ec2" >}})  |                 |       |
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
| [**ECR** (Pro)]({{< ref "elastic-container-registry" >}})          | [🔍]({{< ref "../localstack/metric-coverage/#ecr" >}}) |                 |       |
| Images                                                             | ⭐⭐⭐         |    Emulated     |       |
| Image Scans                                                        | \-             |                 |       |
| Lifecycle Policies                                                 | ⭐⭐⭐⭐       |      CRUD       |       |
| Registries                                                         | ⭐⭐⭐⭐       |    Emulated     |       |
| Registry Policies                                                  | \-             |                 |       |
| Replication Configurations                                         | \-             |                 |       |
| Repositories                                                       | ⭐⭐⭐⭐       |    Emulated     |       |
| Repository Policies                                                | ⭐⭐⭐⭐       |      CRUD       |       |
| Tags                                                               | ⭐⭐⭐⭐       |      CRUD       |       |
| [**ECS** (Pro)]({{< ref "elastic-container-service" >}})           | [🔍]({{< ref "../localstack/metric-coverage/#ecs" >}}) |                 |       |
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
| **EFS** (Pro)                                                      | [🔍]({{< ref "../localstack/metric-coverage/#efs" >}}) |                 |       |
| [**EKS** (Pro)]({{< ref "elastic-kubernetes-service" >}})          | [🔍]({{< ref "../localstack/metric-coverage/#eks" >}}) |                 |       |
| AddOns                                                             | \-             |                 |       |
| Clusters                                                           | ⭐⭐⭐         | Emulated        |       |
| Fargate Profiles                                                   | ⭐⭐           | CRUD            |       |
| Identity Provider Configs                                          | \-             |                 |       |
| Node Groups                                                        | \-             |                 |       |
| Tags                                                               | ⭐⭐⭐⭐       | CRUD            |       |
| Updates                                                            | \-             |                 |       |
| [**ElastiCache** (Pro)]({{< ref "elasticache" >}})                 | [🔍]({{< ref "../localstack/metric-coverage/#elasticache" >}}) |       |
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
| **Elastic Beanstalk** (Pro)                                        | [🔍]({{< ref "../localstack/metric-coverage/#elasticbeanstalk" >}}) |                 |       |
| **ELB (Elastic Load Balancing)** (Pro)                             | [🔍]({{< ref "../localstack/metric-coverage/#elb" >}}) |                 |       |
| Listeners                                                          | ⭐⭐⭐         | CRUD            |       |
| Load balancers                                                     | ⭐⭐⭐         | Emulated        | Application load balancers with IP address or Lambda targets only |
| Rules                                                              | ⭐⭐⭐         | CRUD            |       |
| Target groups                                                      | ⭐⭐⭐         | CRUD            |       |
| Listener certificates                                              | ⭐⭐⭐         | CRUD            |       |
| [**ELBv2 (Elastic Load Balancing v2)**]({{< ref "elastic-load-balancing" >}}) (Pro) | [🔍]({{< ref "../localstack/metric-coverage/#elbv2" >}}) |                 |       |
| Listeners                                                          | ⭐⭐⭐         | CRUD            |       |
| Load balancers                                                     | ⭐⭐⭐         | CRUD            |       |
| Rules                                                              | ⭐⭐⭐         | CRUD            |       |
| Target groups                                                      | ⭐⭐⭐         | CRUD            |       |
| Listener certificates                                              | ⭐⭐⭐         | CRUD            |       |
| [**EMR**]({{< ref "elastic-mapreduce" >}}) (Pro)                   | [🔍]({{< ref "../localstack/metric-coverage/#emr" >}}) |                 |       |
| Clusters                                                           | ⭐⭐⭐⭐       |                 |       |
| Instance Fleets                                                    | ⭐⭐⭐         |                 |       |
| Job Flow Steps                                                     | ⭐⭐⭐         |                 |       |
| Managed Scaling Policies                                           | \-             |                 |       |
| Notebook Executions                                                | \-             |                 |       |
| Run Job Flows (Queries)                                            | ⭐⭐⭐         |                 |       |
| Security Configurations                                            | \-             |                 |       |
| Studios                                                            | \-             |                 |       |
| Tags                                                               | ⭐⭐⭐⭐       |                 |       |
| [**ES (Elasticsearch Service)**]({{< ref "elasticsearch" >}})      | [🔍]({{< ref "../localstack/metric-coverage/#es" >}}) |                 |       |
| Cross-Cluster Search Connections                                   | \-             |                 |       |
| Elasticsearch Domains                                              | ⭐⭐⭐⭐       | Emulated        |       |
| Packages                                                           | \-             |                 |       |
| Reserved Instances                                                 | \-             |                 |       |
| Tags                                                               | ⭐⭐⭐⭐       | CRUD            |       |
| **EventBridge (Events)**                                           | [🔍]({{< ref "../localstack/metric-coverage/#events" >}}) |                 |       |
| API Destinations                                                   | ⭐⭐⭐⭐       | Emulated                |       |
| Archives                                                           | \-             |                 |       |
| Connections                                                        | \-             |                 |       |
| Event Buses                                                        | ⭐⭐⭐⭐       | Emulated                |       |
| Event Sources                                                      | ⭐⭐⭐⭐       | Emulated                |       |
| Partner Event Sources                                              | \-             |                 |       |
| Replays                                                            | \-             |                 |       |
| Rules                                                              | ⭐⭐⭐⭐       | Emulated                |       |
| Tags                                                               | ⭐⭐⭐⭐       | CRUD                |       |
| **Firehose**                                                       | [🔍]({{< ref "../localstack/metric-coverage/#firehose" >}}) |                 |       |
| Delivery Streams                                                   | ⭐⭐⭐⭐       |                 |       |
| Destinations                                                       | ⭐⭐⭐⭐       |                 |       |
| Records                                                            | ⭐⭐⭐⭐       |                 |       |
| Tags                                                               | ⭐⭐⭐⭐       |                 |       |
| **Glacier** (Pro)                                                  | [🔍]({{< ref "../localstack/metric-coverage/#glacier" >}}) |                 |       |
| [**Glue** (Pro)]({{< ref "glue" >}})                               | [🔍]({{< ref "../localstack/metric-coverage/#glue" >}}) |                 |       |
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
| [**IAM**]({{< ref "iam" >}})                                       | [🔍]({{< ref "../localstack/metric-coverage/#iam" >}}) |                 |       |
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
| [**IoT (Analytics, Data, Wireless)** (Pro)]({{< ref "iot" >}})     | [🔍]({{< ref "../localstack/metric-coverage/#iot" >}}) |                 |       |
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
| [**Kafka (MSK - Managed Streaming for Kafka)**]({{< ref "managed-streaming-for-kafka" >}}) (Pro) | [🔍]({{< ref "../localstack/metric-coverage/#kafka" >}}) |                 |       |
| Brokers                                                            | ⭐⭐           | Emulated        |       |
| Cluster Operations                                                 | ⭐⭐           | Emulated        |       |
| Clusters                                                           | ⭐⭐⭐⭐       | Emulated        | Single node clusters |
| Configurations                                                     | ⭐⭐⭐⭐       | CRUD            |       |
| Tags                                                               | ⭐⭐⭐⭐       | CRUD            |       |
| [**Kinesis**]({{< ref "kinesis" >}})                               | [🔍]({{< ref "../localstack/metric-coverage/#kinesis" >}}) |                 |       |
| Records                                                            | ⭐⭐⭐⭐       | Emulated                |       |
| Split / Merge Shards                                               | ⭐⭐⭐⭐       | Emulated                |       |
| Stream Consumers                                                   | ⭐⭐⭐⭐       | Emulated                |       |
| Stream Encryption                                                  | \-             |                 |       |
| Streams                                                            | ⭐⭐⭐⭐       | Emulated                |       |
| Subscribe to Shard                                                 | ⭐⭐⭐⭐       | Emulated                |       |
| Tags                                                               | ⭐⭐⭐⭐       | CRUD            |       |
| **Kinesis Analytics** (Pro)                                        | [🔍]({{< ref "../localstack/metric-coverage/#kinesisanalytics" >}})  |                 |       |
| **Kinesis Analytics v2** (Pro)                                     | [🔍]({{< ref "../localstack/metric-coverage/#kinesisanalyticsv2" >}}) |                 |       |
| **KMS**                                                            | [🔍]({{< ref "../localstack/metric-coverage/#kms" >}}) |                 |       |
| Aliases                                                            | ⭐⭐⭐⭐       |                 |       |
| Custom Key Stores                                                  | ⭐⭐⭐         |                 |       |
| Encrypt / Decrypt / Sign Data                                      | ⭐⭐⭐⭐       |                 |       |
| Grants                                                             | \-             |                 |       |
| Key Policies                                                       | \-             |                 |       |
| Keys                                                               | ⭐⭐⭐⭐       |                 |       |
| Tags                                                               | ⭐⭐⭐⭐       |                 |       |
| **Lake Formation** (Pro)                                           | [🔍]({{< ref "../localstack/metric-coverage/#lakeformation" >}}) |                 |       |
| [**Lambda**]({{< ref "lambda" >}})                                 | [🔍]({{< ref "../localstack/metric-coverage/#lambda" >}}) |                 |       |
| Aliases                                                            | ⭐⭐⭐⭐       | CRUD            |       |
| Code Signing Configs                                               | ⭐⭐           | CRUD            |       |
| Custom Images (Pro)                                                | ⭐⭐⭐⭐       | Emulated        |       |
| Event Invoke Configs (Destinations)                                | ⭐⭐⭐⭐       | Emulated        |       |
| Event Source Mappings                                              | ⭐⭐⭐⭐       | Emulated        |       |
| Function Concurrencies                                             | ⭐⭐⭐         | CRUD            |       |
| Functions                                                          | ⭐⭐⭐⭐       | Emulated        |       |
| Invoke Functions                                                   | ⭐⭐⭐⭐       | Emulated        |       |
| [Layers (Pro)]({{< ref "lambda#lambda-layers" >}})                 | ⭐⭐⭐⭐       | Emulated        |       |
| Permissions                                                        | ⭐⭐⭐⭐       | CRUD            |       |
| Tags                                                               | ⭐⭐⭐⭐       | CRUD            |       |
| **Logs**                                                           | [🔍]({{< ref "../localstack/metric-coverage/#logs" >}}) |                 |       |
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
| **MediaStore** (Pro)                                               | [🔍]({{< ref "../localstack/metric-coverage/#mediastore" >}}) |                 |       |
| Access Logging                                                     | \-             |                 |       |
| Container Policies                                                 | \-             |                 |       |
| Containers                                                         | ⭐⭐⭐         |                 |       |
| CORS Policies                                                      | \-             |                 |       |
| Lifecycle Policies                                                 | \-             |                 |       |
| Metric Policies                                                    | \-             |                 |       |
| Tags                                                               | \-             |                 |       |
| **MediaStore Data** (Pro)                                          | [🔍]({{< ref "../localstack/metric-coverage/#mediastore-data" >}}) |                 |       |
| **MWAA (Managed Workflows for Apache Airflow)** (Pro)              | [🔍]({{< ref "../localstack/metric-coverage/#mwaa" >}}) |                 |       |
| CLI Tokens                                                         | -              |                 |       |
| Environments                                                       | ⭐⭐⭐          |                 |       |
| S3 integration (DAG bucket/paths)                                  | ⭐⭐⭐          |                 |       |
| Tags                                                               | ⭐⭐⭐⭐        |                 |       |
| Web Login                                                          | ⭐⭐⭐          |                 |       |
| [**Neptune DB** (Pro)]({{< ref "neptune" >}})                      | [🔍]({{< ref "../localstack/metric-coverage/#neptune" >}}) |                 |       |
| DB Clusters                                                        | ⭐⭐⭐⭐       |                 |       |
| DB Cluster Endpoints                                               | ⭐⭐⭐⭐       |                 |       |
| DB Cluster Parameter Groups                                        | ⭐⭐⭐⭐       |                 |       |
| DB Cluster Snapshots                                               | \-             |                 |       |
| Engine Default Parameters                                          | ⭐⭐           |                 |       |
| Event Subscriptions                                                | \-             |                 |       |
| Events                                                             | \-             |                 |       |
| Tags                                                               | \-             |                 |       |
| [**OpenSearch Service**]({{< ref "opensearch" >}})                 | [🔍]({{< ref "../localstack/metric-coverage/#opensearch" >}}) |                 |       |
| Cross-Cluster Search Connections                                   | \-             |                 |       |
| OpenSearch Domains                                                 | ⭐⭐⭐⭐       | Emulated        |       |
| Packages                                                           | \-             |                 |       |
| Reserved Instances                                                 | \-             |                 |       |
| Tags                                                               | ⭐⭐⭐⭐       | CRUD            |       |
| **Organizations** (Pro)                                            | [🔍]({{< ref "../localstack/metric-coverage/#organizations" >}}) |                 |       |
| [**QLDB** (Pro)]({{< ref "qldb" >}})                               | [🔍]({{< ref "../localstack/metric-coverage/#qldb" >}}) |                 |       |
| Blocks                                                             | ⭐⭐⭐         |                 |       |
| Digests                                                            | ⭐⭐⭐         |                 |       |
| Journal Kinesis Streams                                            | ⭐⭐⭐         |                 |       |
| Journal S3 Exports                                                 | ⭐⭐⭐         |                 |       |
| Ledgers                                                            | ⭐⭐⭐⭐       |                 |       |
| Send Commands / Run Queries                                        | ⭐⭐⭐⭐       |                 |       |
| Tags                                                               | ⭐⭐⭐⭐       |                 |       |
| **QLDB Sessions** (Pro)                                            | [🔍]({{< ref "../localstack/metric-coverage/#qldb-session" >}}) |                 |       |
| [**RDS / Aurora Serverless** (Pro)]({{< ref "rds" >}})             | [🔍]({{< ref "../localstack/metric-coverage/#rds" >}}) |                 |       |
| DB/Cluster Parameter Groups                                        | ⭐⭐⭐         | CRUD            |       |
| DB/Cluster Snapshots                                               | ⭐⭐⭐         | Emulated        |       |
| DB Clusters/Instances                                              | ⭐⭐⭐⭐       | Emulated        |       |
| DB Proxies                                                         | ⭐⭐           | Emulated       |       |
| DB Security/Subnet Groups                                          | ⭐⭐⭐         | Emulated        |       |
| Event Subscriptions                                                | \-             |                 |       |
| Option Groups                                                      | ⭐⭐⭐⭐       | CRUD            |       |
| Postgres AWS Extension Functions                                   | ⭐⭐⭐         | Emulated        |       |
| Tags                                                               | ⭐⭐⭐⭐       | CRUD            |       |
| **RDS Data** (Pro)                                                 | [🔍]({{< ref "../localstack/metric-coverage/#rds-data" >}}) |                 |       |
| Execute sql/statements                                             | ⭐⭐⭐         | Emulated               |       |
| Transactions                                                       | ⭐⭐           | Emulated                |       |
| Batch Execution                                                    | \-             |                 |       |
| **Redshift**                                                       | [🔍]({{< ref "../localstack/metric-coverage/#redshift" >}}) |                 |       |
| Authorize/Revoke Access                                            | \-             |                 |       |
| Cluster Parameter Groups                                           | ⭐⭐⭐         |                 |       |
| Cluster Snapshots                                                  | ⭐⭐⭐         |                 |       |
| Clusters/Instances                                                 | ⭐⭐⭐⭐       |                 |       |
| Event Subscriptions                                                | \-             |                 |       |
| HSM Configurations                                                 | \-             |                 |       |
| Partners                                                           | \-             |                 |       |
| Security/Subnet Groups                                             | ⭐⭐⭐         |                 |       |
| Tags                                                               | ⭐⭐⭐⭐       |                 |       |
| Usage Limits                                                       | ⭐⭐           |                 |       |
| **Redshift Data** (Pro)                                            | [🔍]({{< ref "../localstack/metric-coverage/#redshift-data" >}}) |                 |       |
| **Resource Groups**                                                | [🔍]({{< ref "../localstack/metric-coverage/#resource-groups" >}}) |                 |       |
| **Resource Groups Tagging API**                                    | [🔍]({{< ref "../localstack/metric-coverage/#resourcegroupstaggingapi" >}})  |                 |       |
| [**Route53**]({{< ref "route53" >}})                               | [🔍]({{< ref "../localstack/metric-coverage/#route53" >}}) |                 |       |
| DNS Server Integration (Pro)                                       | ⭐⭐⭐⭐       |                 |       |
| Geo Locations                                                      | \-             |                 |       |
| Health Checks                                                      | ⭐⭐           |                 |       |
| Hosted Zones                                                       | ⭐⭐⭐⭐       |                 |       |
| Query Logging Configs                                              | \-             |                 |       |
| Resource Record Sets                                               | ⭐⭐⭐⭐       |                 |       |
| Reusable Delegation Sets                                           | ⭐⭐⭐         |                 |       |
| Tags                                                               | ⭐⭐⭐⭐       |                 |       |
| Traffic Policies                                                   | ⭐⭐⭐         |                 |       |
| **Route53 Resolver**                                               | [🔍]({{< ref "../localstack/metric-coverage/#route53resolver" >}}) |                |       |
| [**S3**]({{< ref "s3" >}})                                         | [🔍]({{< ref "../localstack/metric-coverage/#s3" >}}) |                 |       |
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
| **S3 Control**                                                     | [🔍]({{< ref "../localstack/metric-coverage/#s3control" >}}) |                 |       |
| Access Point Policies                                              | ⭐⭐           | CRUD            |       |
| Access Points                                                      | ⭐⭐           | CRUD            |       |
| Jobs                                                               | \-             |                 |       |
| Lifecycle configurations                                           | \-             |                 |       |
| Multi-region Access Points                                         | \-             |                 |       |
| Public Access Blocks                                               | ⭐⭐           | CRUD            |       |
| Storage Lens                                                       | \-             |                 |       |
| [**SageMaker** (Pro)]({{< ref "sagemaker" >}})                     | [🔍]({{< ref "../localstack/metric-coverage/#sagemaker" >}}) |                 |       |
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
| **SecretsManager**                                                 | [🔍]({{< ref "../localstack/metric-coverage/#secretsmanager" >}}) |                 |       |
| Resource Policies                                                  | ⭐⭐⭐⭐       | CRUD                 |       |
| Secret Replications                                                | ⭐⭐           | CRUD                |       |
| Secret Rotations                                                   | ⭐⭐           | CRUD                |       |
| Secrets                                                            | ⭐⭐⭐⭐       | CRUD                |       |
| Tags                                                               | ⭐⭐⭐⭐       | CRUD                |       |
| **Serverless Repo** (Pro)                                          | [🔍]({{< ref "../localstack/metric-coverage/#serverlessrepo" >}}) |                 |       |
| **Service Discovery (CloudMap)** (Pro)                             | [🔍]({{< ref "../localstack/metric-coverage/#servicediscovery" >}}) |                 |       |
| Namespaces                                                         | ⭐⭐⭐         | CRUD                |       |
| [**SES**]({{< ref "ses" >}})                                       | [🔍]({{< ref "../localstack/metric-coverage/#ses" >}}) |                 |       |
| Configuration Sets                                                 | ⭐⭐⭐         | CRUD               |       |
| Identities                                                         | ⭐⭐           | CRUD               |       |
| Identity Policies                                                  | ⭐⭐           | CRUD               |       |
| Quotas / Statistics                                                | ⭐⭐           | CRUD               |       |
| Receipt Filters                                                    | ⭐⭐⭐         | CRUD               |       |
| Receipt Rules                                                      | ⭐⭐⭐         | CRUD               |       |
| Sending Emails via SMTP (Pro)                                      | ⭐⭐⭐⭐       | Emulated           |       |
| Templates                                                          | ⭐⭐⭐⭐       | CRUD               |       |
| **SESv2 (Pro)**                                                   | [🔍]({{< ref "../localstack/metric-coverage/#sesv2" >}}) |                 |       |
| Identities                                                         | ⭐⭐           | CRUD               |       |
| Sending Emails via SMTP                                            | ⭐⭐⭐⭐       | Emulated           |       |
| Templates                                                          | ⭐⭐⭐⭐       | CRUD               |       |
| **SNS**                                                            | [🔍]({{< ref "../localstack/metric-coverage/#sns" >}}) |                 |       |
| Platform Applications                                              | ⭐⭐⭐         |  CRUD               |       |
| Publish/Subscribe to Topics                                        | ⭐⭐⭐⭐       |  Emulated               |       |
| SMS Attributes / Sandbox Accounts                                  | ⭐⭐           |  CRUD               |       |
| Subscriptions                                                      | ⭐⭐⭐⭐       |   Emulated             |       |
| Tags                                                               | ⭐⭐⭐⭐       |   CRUD              |       |
| Topics                                                             | ⭐⭐⭐⭐       |   CRUD              |       |
| [**SQS**]({{< ref "sqs" >}})                                       | [🔍]({{< ref "../localstack/metric-coverage/#sqs" >}}) |                 |       |
| FIFO Queues                                                        | ⭐⭐⭐⭐       | Emulated        |       |
| Message Deduplication                                              | ⭐⭐⭐⭐       | Emulated        |       |
| Message Visibility                                                 | ⭐⭐⭐⭐⭐     | Emulated        |       |
| Messages                                                           | ⭐⭐⭐⭐⭐     | Emulated        |       |
| Permission                                                         | ⭐⭐⭐         | CRUD            |       |
| Query API                                                          | ⭐⭐⭐⭐       | Emulated        |       |
| Standard Queues                                                    | ⭐⭐⭐⭐       | Emulated        |       |
| Tags                                                               | ⭐⭐⭐⭐       | CRUD            |       |
| [**SSM**]({{< ref "systems-manager" >}})                           | [🔍]({{< ref "../localstack/metric-coverage/#ssm" >}}) |                 |       |
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
| **StepFunctions**                                                  | [🔍]({{< ref "../localstack/metric-coverage/#stepfunctions" >}}) |                 |       |
| Activities                                                         | ⭐⭐⭐⭐       | Emulated                |       |
| Executions / Execution History                                     | ⭐⭐⭐⭐       | Emulated                |       |
| State Machines                                                     | ⭐⭐⭐⭐       | Emulated                |       |
| Tags                                                               | ⭐⭐⭐⭐       | Emulated                |       |
| **STS**                                                            | [🔍]({{< ref "../localstack/metric-coverage/#sts" >}})  |                 |       |
| Assume Role (Pro)                                                  | ⭐⭐⭐⭐       |                 |       |
| Get Access Key Info                                                | ⭐⭐⭐⭐       |                 |       |
| Get Caller Identity                                                | ⭐⭐⭐⭐       |                 |       |
| Session Tokens                                                     | ⭐⭐⭐⭐       |                 |       |
| **Support**                                                        | [🔍]({{< ref "../localstack/metric-coverage/#support" >}}) |                 |       |
| **SWF**                                                            | [🔍]({{< ref "../localstack/metric-coverage/#swf" >}}) |                 |       |
| [**Timestream (query, write)**]({{< ref "timestream" >}}) (Pro)    | [🔍]({{< ref "../localstack/metric-coverage/#timestream-query" >}}) |                 |       |
| Databases                                                          | ⭐⭐⭐         |                 |       |
| Run Query                                                          | ⭐⭐⭐         |                 |       |
| Tables                                                             | ⭐⭐⭐         |                 |       |
| Tags                                                               | ⭐⭐⭐⭐       |                 |       |
| Write Records                                                      | ⭐⭐⭐⭐       |                 |       |
| [**Transfer** (Pro)]({{< ref "transfer" >}})                       | [🔍]({{< ref "../localstack/metric-coverage/#transfer" >}}) |                 |       |
| Accesses                                                           | \-             |                 |       |
| Security Policies                                                  | \-             |                 |       |
| Servers                                                            | ⭐⭐⭐         |                 |       |
| SSH Public Keys                                                    | ⭐⭐⭐         |                 |       |
| Tags                                                               | \-             |                 |       |
| Users                                                              | ⭐⭐⭐         |                 |       |
| [**XRay** (Pro)]({{< ref "xray-tracing" >}})                       | [🔍]({{< ref "../localstack/metric-coverage/#xray" >}}) |                 |       |
| Encryption Configs                                                 | \-             |                 |       |
| Groups                                                             | ⭐⭐           |                 |       |
| Insights                                                           | \-             |                 |       |
| Sampling Rules                                                     | ⭐⭐⭐         |                 |       |
| Service Graph                                                      | \-             |                 |       |
| Tags                                                               | \-             |                 |       |
| Telemetry Records                                                  | ⭐⭐⭐⭐       |                 |       |
| Trace Graph                                                        | \-             |                 |       |
| Trace Segments / Summaries                                         | ⭐⭐⭐         |                 |       |

