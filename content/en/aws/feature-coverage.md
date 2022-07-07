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
| **-**    | Feature is not implemented yet        | 


## Emulation Levels

* CRUD: The service accepts requests and returns proper (potentially static) responses. No additional business logic besides storing entities.
* EMULATED: The service imitates the functionality, including synchronous and asynchronous business logic operating on service entities. 


## AWS Feature Coverage

In the coverage table below, the features are marked with their respective availability across different LocalStack versions:

* Community version (default, if not marked)
* Pro version (marked with **Pro**)

| Service / Feature                                                  | Coverage Level    | Emulation Level | Notes |
|--------------------------------------------------------------------|-------------------|-----------------|-------|
| **ACM**                                                            | [🔍]({{< ref "../localstack/metric-coverage/#acm" >}})      |                 |       |
| Certificates                                                       | ⭐⭐⭐              |                 |       |
| Tags                                                               | ⭐⭐⭐⭐            |                 |       |
| Account Configuration                                              | ⭐⭐                |                 |       |
| [**Amplify** (Pro)]({{< ref "amplify" >}})                         | [🔍]({{< ref "../localstack/metric-coverage/#amplify" >}})  |                 |       |
| Apps                                                               | ⭐⭐⭐              |                 |       |
| Backend Environments                                               | ⭐⭐                |                 |       |
| Branches                                                           | ⭐⭐                |                 |       |
| Deployments                                                        | ⭐⭐⭐              |                 |       |
| Domain Associations                                                | \-                 |                 |       |
| Jobs                                                               | ⭐⭐                |                 |       |
| Tags                                                               | ⭐⭐⭐⭐             |                 |       |
| Webhooks                                                           | ⭐⭐                |                 |       |
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
| Scalable Targets                                                   | ⭐⭐⭐           |                 |       |
| Scaling Activities                                                 | ⭐⭐             |                 |       |
| Scaling Policies                                                   | ⭐⭐             |                 |       |
| Scheduled Actions                                                  | ⭐⭐             |                 |       |
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
| Data Catalogs                                                      | ⭐⭐           |                 |       |
| Databases                                                          | ⭐⭐           |                 |       |
| Named Queries                                                      | \-             |                 |       |
| Prepared Statements                                                | ⭐⭐⭐         |                 |       |
| Query Executions                                                   | ⭐⭐⭐         |                 |       |
| Table Metadata                                                     | ⭐⭐           |                 |       |
| Tags                                                               | ⭐⭐⭐⭐       |                 |       |
| Work Groups                                                        | \-             |                 |       |
| **Autoscaling** (Pro)                                              | [🔍]({{< ref "../localstack/metric-coverage/#autoscaling" >}}) |                 |       |
| [**Backup** (Pro)]({{< ref "backup" >}})                           | [🔍]({{< ref "../localstack/metric-coverage/#backup" >}}) |                 |       |
| Backup Jobs                                                        | ⭐⭐⭐         |                 |       |
| Backup Plans                                                       | ⭐⭐⭐         |                 |       |
| Backup Selections                                                  | ⭐⭐⭐         |                 |       |
| Backup Vaults                                                      | ⭐⭐⭐         |                 |       |
| Backup Vault Access Policies                                       | \-             |                 |       |
| Backup Vault Notifications                                         | \-             |                 |       |
| Global Settings                                                    | \-             |                 |       |
| Protected Resources                                                | \-             |                 |       |
| Recovery Points                                                    | ⭐⭐⭐         |                 |       |
| Tags                                                               | \-             |                 |       |
| **Batch** (Pro)                                                    | [🔍]({{< ref "../localstack/metric-coverage/#batch" >}}) |                 |       |
| Compute Environments                                               | ⭐⭐⭐         |                 |       |
| Job Queues                                                         | ⭐⭐⭐         |                 |       |
| Job Definitions                                                    | ⭐⭐⭐         |                 |       |
| Jobs                                                               | ⭐⭐⭐         |                 |       |
| Tags                                                               | ⭐⭐⭐⭐       |                 |       |
| **CE (Cost Explorer API)** (Pro)                                   | [🔍]({{< ref "../localstack/metric-coverage/#ce" >}}) |                 |       |
| [**CloudFormation**]({{< ref "cloudformation" >}})                 | [🔍]({{< ref "../localstack/metric-coverage/#cloudformation" >}}) |                 |       |
| Change Sets                                                        | ⭐⭐⭐⭐       |                 |       |
| Stacks                                                             | ⭐⭐⭐⭐       |                 |       |
| Stack Drifts                                                       | \-             |                 |       |
| Stack Events                                                       | ⭐⭐⭐⭐       |                 |       |
| Stack Instances                                                    | ⭐⭐⭐⭐       |                 |       |
| Stack Policies                                                     | ⭐⭐⭐         |                 |       |
| Stack Resources                                                    | ⭐⭐⭐⭐       |                 |       |
| Stack Sets                                                         | ⭐⭐⭐⭐       |                 |       |
| Publishers                                                         | \-             |                 |       |
| Templates                                                          | ⭐⭐⭐⭐       |                 |       |
| Type Activations                                                   | ⭐⭐           |                 |       |
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
| Alarms                                                             | ⭐⭐⭐⭐        | EMULATED       |       |
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
| Admin APIs                                                         | ⭐⭐⭐         |                 |       |
| Devices                                                            | ⭐⭐           |                 |       |
| Auth Flows                                                         | ⭐⭐⭐         |                 |       |
| Groups                                                             | ⭐⭐⭐⭐       |                 |       |
| Lambda Triggers                                                    | ⭐⭐⭐⭐       |                 |       |
| MFA Configs                                                        | ⭐⭐⭐         |                 |       |
| Resource Servers                                                   | \-             |                 |       |
| Risk Configurations                                                | \-             |                 |       |
| Identity Providers                                                 | ⭐⭐⭐         |                 |       |
| User Import Jobs                                                   | \-             |                 |       |
| User Pool Clients                                                  | ⭐⭐⭐⭐       |                 |       |
| User Pool Domains                                                  | ⭐⭐           |                 |       |
| User Pools                                                         | ⭐⭐⭐⭐       |                 |       |
| Users                                                              | ⭐⭐⭐⭐       |                 |       |
| Tags                                                               | ⭐⭐⭐⭐       |                 |       |
| **Config**                                                         | [🔍]({{< ref "../localstack/metric-coverage/#config" >}}) |                 |       |
| **DocumentDB** (Pro)                                               | [🔍]({{< ref "../localstack/metric-coverage/#docdb" >}}) |                 |       |
| DB/Cluster Parameter Groups                                        | ⭐⭐⭐         |                 |       |
| DB/Cluster Snapshots                                               | ⭐            |                 |       |
| DB Clusters/Instances                                              | ⭐⭐⭐⭐       |                 |       |
| DB Subnet Groups                                                   | ⭐⭐          |                 |       |
| Event Subscriptions                                                | \-           |                 |       |
| Tags                                                               | ⭐⭐⭐⭐       |                 |       |
| **DynamoDB**                                                       | [🔍]({{< ref "../localstack/metric-coverage/#dynamodb" >}}) |                 |       |
| Backups (Pro)                                                      | ⭐⭐⭐⭐       |                 |       |
| Batch Operations                                                   | ⭐⭐⭐⭐       |                 |       |
| Global Tables                                                      | ⭐⭐⭐⭐       |                 |       |
| Items                                                              | ⭐⭐⭐⭐       |                 |       |
| Kinesis Streaming Destinations                                     | \-             |                 |       |
| PartiQL Queries                                                    | ⭐⭐⭐⭐       |                 |       |
| Query / Scan Operations                                            | ⭐⭐⭐⭐       |                 |       |
| Tables                                                             | ⭐⭐⭐⭐       |                 |       |
| Table Replica Autoscaling                                          | \-             |                 |       |
| Tags                                                               | ⭐⭐⭐⭐       |                 |       |
| **DynamoDB Streams**                                               | [🔍]({{< ref "../localstack/metric-coverage/#dynamodbstreams" >}}) |                 |       |
| Records                                                            | ⭐⭐⭐⭐       |                 |       |
| Shard Iterators                                                    | ⭐⭐⭐⭐       |                 |       |
| Streams                                                            | ⭐⭐⭐⭐       |                 |       |
| [**EC2**]({{< ref "elastic-compute-cloud" >}})                      | [🔍]({{< ref "../localstack/metric-coverage/#ec2" >}})  |                 |       |
| Classic Links                                                      | ⭐⭐⭐         |                 |       |
| Customer Gateways                                                  | ⭐⭐⭐         |                 |       |
| DHCP Options                                                       | ⭐⭐⭐         |                 |       |
| Allocate/Deallocate Elastic IPs                                    | ⭐⭐⭐         |                 |       |
| Fleets                                                             | ⭐⭐           |                 |       |
| Flow Logs                                                          | ⭐⭐⭐         |                 |       |
| Images                                                             | ⭐⭐           |                 |       |
| Internet Gateways                                                  | ⭐⭐⭐         |                 |       |
| Local Gateway Routes                                               | ⭐⭐⭐         |                 |       |
| Key Pairs                                                          | ⭐⭐⭐⭐       |                 |       |
| Launch Templates                                                   | ⭐⭐⭐         |                 |       |
| NAT Gateways                                                       | ⭐⭐⭐         |                 |       |
| Network ACLs                                                       | ⭐⭐⭐         |                 |       |
| Network Interfaces                                                 | ⭐⭐⭐         |                 |       |
| Reserved Instances                                                 | ⭐⭐⭐         |                 |       |
| Route Tables / Routes                                              | ⭐⭐⭐         |                 |       |
| Scheduled Instances                                                | ⭐⭐⭐         |                 |       |
| Security Groups / Egress / Ingress                                 | ⭐⭐⭐⭐       |                 |       |
| Snapshots                                                          | ⭐⭐⭐         |                 |       |
| Spot Instances                                                     | ⭐⭐⭐         |                 |       |
| Start Instances as VMs (Pro)                                       | ⭐⭐           |                 |       |
| Subnets                                                            | ⭐⭐⭐         |                 |       |
| Tags                                                               | ⭐⭐⭐⭐       |                 |       |
| Traffic Mirrors                                                    | ⭐⭐⭐         |                 |       |
| Transit Gateways                                                   | ⭐⭐⭐         |                 |       |
| Volumes                                                            | ⭐⭐⭐         |                 |       |
| VPC Endpoint Connections                                           | ⭐⭐⭐         |                 |       |
| VPC Peering Connections                                            | ⭐⭐⭐         |                 |       |
| VPCs                                                               | ⭐⭐⭐⭐       |                 |       |
| VPN Gateways / Connections                                         | ⭐⭐⭐         |                 |       |
| [**ECR** (Pro)]({{< ref "elastic-container-registry" >}})          | [🔍]({{< ref "../localstack/metric-coverage/#ecr" >}}) |                 |       |
| Images                                                             | ⭐⭐⭐         |                 |       |
| Image Scans                                                        | \-             |                 |       |
| Lifecycle Policies                                                 | ⭐⭐⭐⭐       |                 |       |
| Registries                                                         | ⭐⭐⭐⭐       |                 |       |
| Registry Policies                                                  | \-             |                 |       |
| Replication Configurations                                         | \-             |                 |       |
| Repositories                                                       | ⭐⭐⭐⭐       |                 |       |
| Repository Policies                                                | ⭐⭐⭐⭐       |                 |       |
| Tags                                                               | ⭐⭐⭐⭐       |                 |       |
| [**ECS** (Pro)]({{< ref "elastic-container-service" >}})           | [🔍]({{< ref "../localstack/metric-coverage/#ecs" >}}) |                 |       |
| Account Settings                                                   | \-             |                 |       |
| Attributes                                                         | ⭐⭐⭐⭐       |                 |       |
| Capacity Providers                                                 | \-             |                 |       |
| Clusters                                                           | ⭐⭐⭐⭐       |                 |       |
| Container Instances                                                | ⭐⭐⭐⭐       |                 |       |
| Services                                                           | ⭐⭐⭐⭐       |                 |       |
| Tags                                                               | ⭐⭐⭐⭐       |                 |       |
| Task Definitions                                                   | ⭐⭐⭐⭐       |                 |       |
| Task Sets                                                          | ⭐⭐⭐         |                 |       |
| Tasks                                                              | ⭐⭐⭐⭐       |                 |       |
| **EFS** (Pro)                                                      | [🔍]({{< ref "../localstack/metric-coverage/#efs" >}}) |                 |       |
| [**EKS** (Pro)]({{< ref "elastic-kubernetes-service" >}})          | [🔍]({{< ref "../localstack/metric-coverage/#eks" >}}) |                 |       |
| AddOns                                                             | \-             |                 |       |
| Clusters                                                           | ⭐⭐⭐         |                 |       |
| Fargate Profiles                                                   | ⭐⭐           |                 |       |
| Identity Provider Configs                                          | \-             |                 |       |
| Node Groups                                                        | \-             |                 |       |
| Tags                                                               | ⭐⭐⭐⭐       |                 |       |
| Updates                                                            | \-             |                 |       |
| [**ElastiCache** (Pro)]({{< ref "elasticache" >}})                 | [🔍]({{< ref "../localstack/metric-coverage/#elasticache" >}}) |       |
| Cache Clusters (Memcached)                                         | \-             |                 |       |
| Cache Parameter Groups                                             | ⭐⭐⭐⭐       |                 |       |
| Cache Security Groups                                              | ⭐⭐⭐⭐       |                 |       |
| Cache Subnet Groups                                                | ⭐⭐⭐⭐       |                 |       |
| Global Replication Groups                                          | \-             |                 |       |
| Replication Groups                                                 | ⭐⭐⭐⭐       |                 |       |
| Snapshots                                                          | \-             |                 |       |
| Tags                                                               | ⭐⭐⭐⭐       |                 |       |
| Users / User Groups                                                | \-             |                 |       |
| **Elastic Beanstalk** (Pro)                                        | [🔍]({{< ref "../localstack/metric-coverage/#elasticbeanstalk" >}}) |                 |       |
| **ELB (Elastic Load Balancing)** (Pro)                             | [🔍]({{< ref "../localstack/metric-coverage/#elb" >}}) |                 |       |
| [**ELBv2 (Elastic Load Balancing v2)**]({{< ref "elastic-load-balancing" >}}) (Pro) | [🔍]({{< ref "../localstack/metric-coverage/#elbv2" >}}) |                 |       |
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
| Elasticsearch Domains                                              | ⭐⭐⭐⭐       |                 |       |
| Packages                                                           | \-             |                 |       |
| Reserved Instances                                                 | \-             |                 |       |
| Tags                                                               | ⭐⭐⭐⭐       |                 |       |
| **EventBridge (Events)**                                           | [🔍]({{< ref "../localstack/metric-coverage/#events" >}}) |                 |       |
| API Destinations                                                   | ⭐⭐⭐⭐       |                 |       |
| Archives                                                           | \-             |                 |       |
| Connections                                                        | \-             |                 |       |
| Event Buses                                                        | ⭐⭐⭐⭐       |                 |       |
| Event Sources                                                      | ⭐⭐⭐⭐       |                 |       |
| Partner Event Sources                                              | \-             |                 |       |
| Replays                                                            | \-             |                 |       |
| Rules                                                              | ⭐⭐⭐⭐       |                 |       |
| Tags                                                               | ⭐⭐⭐⭐       |                 |       |
| **Firehose**                                                       | [🔍]({{< ref "../localstack/metric-coverage/#firehose" >}}) |                 |       |
| Delivery Streams                                                   | ⭐⭐⭐⭐       |                 |       |
| Destinations                                                       | ⭐⭐⭐⭐       |                 |       |
| Records                                                            | ⭐⭐⭐⭐       |                 |       |
| Tags                                                               | ⭐⭐⭐⭐       |                 |       |
| **Glacier** (Pro)                                                  | [🔍]({{< ref "../localstack/metric-coverage/#glacier" >}}) |                 |       |
| [**Glue** (Pro)]({{< ref "glue" >}})                               | [🔍]({{< ref "../localstack/metric-coverage/#glue" >}}) |                 |       |
| Classifiers                                                        | ⭐⭐⭐         |                 |       |
| Connections                                                        | ⭐⭐⭐         |                 |       |
| Crawlers                                                           | ⭐⭐⭐         |                 |       |
| Databases                                                          | ⭐⭐⭐         |                 |       |
| Dev Endpoints                                                      | \-             |                 |       |
| Jobs                                                               | ⭐⭐⭐         |                 |       |
| ML Transforms                                                      | \-             |                 |       |
| Partitions                                                         | ⭐⭐⭐         |                 |       |
| Registries                                                         | ⭐⭐⭐         |                 |       |
| Schemas                                                            | ⭐⭐⭐         |                 |       |
| Scripts                                                            | \-             |                 |       |
| Security Configurations                                            | ⭐⭐⭐         |                 |       |
| Tables                                                             | ⭐⭐⭐         |                 |       |
| Triggers                                                           | ⭐⭐⭐         |                 |       |
| Tags                                                               | ⭐⭐⭐         |                 |       |
| User Defined Functions                                             | \-             |                 |       |
| Workflows                                                          | ⭐⭐⭐         |                 |       |
| [**IAM**]({{< ref "iam" >}})                                       | [🔍]({{< ref "../localstack/metric-coverage/#iam" >}}) |                 |       |
| Access Keys                                                        | ⭐⭐⭐         |                 |       |
| Account Aliases                                                    | ⭐⭐⭐         |                 |       |
| Credential Reports                                                 | \-             |                 |       |
| Groups                                                             | ⭐⭐⭐⭐       |                 |       |
| Instance Profiles                                                  | ⭐⭐⭐         |                 |       |
| Login Profiles                                                     | ⭐⭐⭐         |                 |       |
| OIDC Providers                                                     | \-             |                 |       |
| Policies                                                           | ⭐⭐⭐⭐       |                 |       |
| Roles                                                              | ⭐⭐⭐⭐       |                 |       |
| SAML Providers                                                     | \-             |                 |       |
| Server Certificates                                                | ⭐⭐⭐         |                 |       |
| Service Linked Roles                                               | ⭐⭐⭐         |                 |       |
| Users                                                              | ⭐⭐⭐⭐       |                 |       |
| Virtual MFA Devices                                                | ⭐⭐           |                 |       |
| [**IoT (Analytics, Data, Wireless)** (Pro)]({{< ref "iot" >}})     | [🔍]({{< ref "../localstack/metric-coverage/#iot" >}}) |                 |       |
| Authorizers                                                        | \-             |                 |       |
| Billing Groups                                                     | \-             |                 |       |
| Certificates                                                       | ⭐⭐           |                 |       |
| Channels                                                           | ⭐⭐           |                 |       |
| Custom Metrics                                                     | \-             |                 |       |
| Datasets                                                           | ⭐⭐⭐         |                 |       |
| Dimensions                                                         | \-             |                 |       |
| Domain Configurations                                              | \-             |                 |       |
| Jobs                                                               | ⭐⭐⭐         |                 |       |
| Jobs Executions                                                    | ⭐⭐⭐         |                 |       |
| Jobs Templates                                                     | \-             |                 |       |
| Mitigation Actions                                                 | \-             |                 |       |
| Policies                                                           | ⭐⭐⭐         |                 |       |
| Provisioning Claims / Templates                                    | ⭐⭐           |                 |       |
| Role Aliases                                                       | \-             |                 |       |
| Security Profiles                                                  | \-             |                 |       |
| Shadows                                                            | ⭐⭐           |                 |       |
| Streams                                                            | \-             |                 |       |
| Tags                                                               | ⭐⭐⭐⭐       |                 |       |
| Thing Groups                                                       | ⭐⭐⭐         |                 |       |
| Thing Types                                                        | ⭐⭐⭐         |                 |       |
| Things                                                             | ⭐⭐⭐         |                 |       |
| Topic Rules                                                        | ⭐⭐⭐         |                 |       |
| [**Kafka (MSK - Managed Streaming for Kafka)**]({{< ref "managed-streaming-for-kafka" >}}) (Pro) | [🔍]({{< ref "../localstack/metric-coverage/#kafka" >}}) |                 |       |
| Brokers                                                            | ⭐⭐           |                 |       |
| Cluster Operations                                                 | ⭐⭐           |                 |       |
| Clusters                                                           | ⭐⭐⭐⭐       |                 |       |
| Configurations                                                     | ⭐⭐⭐⭐       |                 |       |
| Tags                                                               | ⭐⭐⭐⭐       |                 |       |
| [**Kinesis**]({{< ref "kinesis" >}})                               | [🔍]({{< ref "../localstack/metric-coverage/#kinesis" >}}) |                 |       |
| Records                                                            | ⭐⭐⭐⭐       |                 |       |
| Split / Merge Shards                                               | ⭐⭐⭐⭐       |                 |       |
| Stream Consumers                                                   | ⭐⭐⭐⭐       |                 |       |
| Stream Encryption                                                  | \-             |                 |       |
| Streams                                                            | ⭐⭐⭐⭐       |                 |       |
| Subscribe to Shard                                                 | ⭐⭐⭐⭐       |                 |       |
| Tags                                                               | ⭐⭐⭐⭐       |                 |       |
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
| Aliases                                                            | ⭐⭐⭐⭐       |                 |       |
| Code Signing Configs                                               | ⭐⭐           |                 |       |
| Custom Images (Pro)                                                | ⭐⭐⭐⭐       | EMULATED        |       |
| Event Invoke Configs (Destinations)                                | ⭐⭐⭐⭐       |                 |       |
| Event Source Mappings                                              | ⭐⭐⭐⭐       |                 |       |
| Function Concurrencies                                             | ⭐⭐⭐         |                 |       |
| Functions                                                          | ⭐⭐⭐⭐       |                 |       |
| Invoke Functions                                                   | ⭐⭐⭐⭐       |                 |       |
| [Layers (Pro)]({{< ref "lambda#lambda-layers" >}})                 | ⭐⭐⭐⭐       |                 |       |
| Permissions                                                        | ⭐⭐⭐⭐       |                 |       |
| Tags                                                               | ⭐⭐⭐⭐       |                 |       |
| **Logs**                                                           | [🔍]({{< ref "../localstack/metric-coverage/#logs" >}}) |                 |       |
| Destinations                                                       | ⭐⭐⭐⭐       | EMULATED       |       |
| Export Tasks                                                       | ⭐⭐          | CRUD            |       |
| Log Events                                                         | ⭐⭐⭐⭐       | EMULATED        |       |
| Log Groups                                                         | ⭐⭐⭐⭐       | CRUD                |       |
| Log Streams                                                        | ⭐⭐⭐⭐       | CRUD                |       |
| Metric Filters                                                     | ⭐⭐⭐         | CRUD                |       |
| Queries                                                            | ⭐⭐          | CRUD                |       |
| Resource Policies                                                  | ⭐⭐⭐        | CRUD               |       |
| Retention Policies                                                 | ⭐⭐⭐         | CRUD                |       |
| Subscription Filters                                               | ⭐⭐⭐         | EMULATED        |       |
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
| OpenSearch Domains                                                 | ⭐⭐⭐⭐       |                 |       |
| Packages                                                           | \-             |                 |       |
| Reserved Instances                                                 | \-             |                 |       |
| Tags                                                               | ⭐⭐⭐⭐       |                 |       |
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
| DB/Cluster Snapshots                                               | ⭐⭐⭐         | EMULATED        |       |
| DB Clusters/Instances                                              | ⭐⭐⭐⭐       | EMULATED        |       |
| DB Proxies                                                         | ⭐⭐           | EMULATED       |       |
| DB Security/Subnet Groups                                          | ⭐⭐⭐         | EMULATED        |       |
| Event Subscriptions                                                | \-             |                 |       |
| Option Groups                                                      | ⭐⭐⭐⭐       | CRUD            |       |
| Postgres AWS Extension Functions                                   | ⭐⭐⭐         | EMULATED        |       |
| Tags                                                               | ⭐⭐⭐⭐       | CRUD            |       |
| **RDS Data** (Pro)                                                 | [🔍]({{< ref "../localstack/metric-coverage/#rds-data" >}}) |                 |       |
| Execute sql/statements                                             | ⭐⭐⭐         | EMULATED               |       |
| Transactions                                                       | ⭐⭐           | EMULATED                |       |
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
| Bucket ACLs                                                        | ⭐⭐⭐         |                 |       |
| Bucket CORS                                                        | ⭐⭐⭐         |                 |       |
| Bucket Encryptions                                                 | ⭐⭐⭐         |                 |       |
| Bucket Lifecycles                                                  | ⭐⭐⭐         |                 |       |
| Bucket Loggings                                                    | ⭐⭐⭐         |                 |       |
| Bucket Metrics Configurations                                      | ⭐⭐⭐         |                 |       |
| Bucket Notifications                                               | ⭐⭐⭐         |                 |       |
| Bucket Ownership Controls                                          | ⭐⭐⭐         |                 |       |
| Bucket Policies                                                    | ⭐⭐⭐         |                 |       |
| Bucket Replications                                                | ⭐⭐⭐         |                 |       |
| Bucket Request Payments                                            | ⭐⭐⭐         |                 |       |
| Bucket Versionings                                                 | ⭐⭐⭐         |                 |       |
| Bucket Websites                                                    | ⭐⭐⭐         |                 |       |
| Buckets                                                            | ⭐⭐⭐⭐       |                 |       |
| Object Retentions                                                  | ⭐⭐           |                 |       |
| Object Versions                                                    | ⭐⭐⭐⭐       |                 |       |
| Objects                                                            | ⭐⭐⭐⭐       |                 |       |
| Tags                                                               | ⭐⭐⭐⭐       |                 |       |
| Upload/Download Files                                              | ⭐⭐⭐⭐       |                 |       |
| **S3 Control**                                                     | [🔍]({{< ref "../localstack/metric-coverage/#s3control" >}}) |                 |       |
| [**SageMaker** (Pro)]({{< ref "sagemaker" >}})                     | [🔍]({{< ref "../localstack/metric-coverage/#sagemaker" >}}) |                 |       |
| Actions                                                            | ⭐⭐           |                 |       |
| Algorithms                                                         | \-             |                 |       |
| App Image Configs                                                  | ⭐⭐           |                 |       |
| Apps                                                               | ⭐⭐⭐         |                 |       |
| Artifacts                                                          | ⭐⭐⭐         |                 |       |
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
| Endpoints / Endpoint Configs                                       | \-             |                 |       |
| Experiments                                                        | \-             |                 |       |
| Feature Groups                                                     | \-             |                 |       |
| Flow Definitions                                                   | \-             |                 |       |
| Hyper Parameter Tuning Jobs                                        | \-             |                 |       |
| Images / Image Versions                                            | \-             |                 |       |
| Labelling Jobs                                                     | \-             |                 |       |
| Model Bias/Explainability Jobs                                     | \-             |                 |       |
| Model Packages                                                     | \-             |                 |       |
| Models                                                             | ⭐⭐           |                 |       |
| Monitoring Executions/Schedules                                    | \-             |                 |       |
| Notebook Instances                                                 | \-             |                 |       |
| Pipeline Executions                                                | \-             |                 |       |
| Pipelines                                                          | \-             |                 |       |
| Projects                                                           | \-             |                 |       |
| Tags                                                               | \-             |                 |       |
| Training Jobs                                                      | \-             |                 |       |
| Transform Jobs                                                     | \-             |                 |       |
| Trials                                                             | \-             |                 |       |
| User Profiles                                                      | \-             |                 |       |
| Workforces / Workteams                                             | \-             |                 |       |
| **SecretsManager**                                                 | [🔍]({{< ref "../localstack/metric-coverage/#secretsmanager" >}}) |                 |       |
| Resource Policies                                                  | ⭐⭐⭐⭐       |                 |       |
| Secret Replications                                                | ⭐⭐           |                 |       |
| Secret Rotations                                                   | ⭐⭐           |                 |       |
| Secrets                                                            | ⭐⭐⭐⭐       |                 |       |
| Tags                                                               | ⭐⭐⭐⭐       |                 |       |
| **Serverless Repo** (Pro)                                          | [🔍]({{< ref "../localstack/metric-coverage/#serverlessrepo" >}}) |                 |       |
| **Service Discovery** (Pro)                                        | [🔍]({{< ref "../localstack/metric-coverage/#servicediscovery" >}}) |                 |       |
| [**SES**]({{< ref "ses" >}})                                       | [🔍]({{< ref "../localstack/metric-coverage/#ses" >}}) |                 |       |
| Configuration Sets                                                 | ⭐⭐⭐         |                 |       |
| Identities                                                         | ⭐⭐           |                 |       |
| Identity Policies                                                  | ⭐⭐           |                 |       |
| Quotas / Statistics                                                | ⭐⭐           |                 |       |
| Receipt Filters                                                    | ⭐⭐⭐         |                 |       |
| Receipt Rules                                                      | ⭐⭐⭐         |                 |       |
| Sending Emails via SMTP (Pro)                                      | ⭐⭐⭐⭐       |                 |       |
| Templates                                                          | ⭐⭐⭐⭐       |                 |       |
| **SES v2**                                                         | [🔍]({{< ref "../localstack/metric-coverage/#sesv2" >}}) |                 |       |
| **SNS**                                                            | [🔍]({{< ref "../localstack/metric-coverage/#sns" >}}) |                 |       |
| Platform Applications                                              | ⭐⭐⭐         |                 |       |
| Publish/Subscribe to Topics                                        | ⭐⭐⭐⭐       |                 |       |
| SMS Attributes / Sandbox Accounts                                  | ⭐⭐           |                 |       |
| Subscriptions                                                      | ⭐⭐⭐⭐       |                 |       |
| Tags                                                               | ⭐⭐⭐⭐       |                 |       |
| Topics                                                             | ⭐⭐⭐⭐       |                 |       |
| [**SQS**]({{< ref "sqs" >}})                                       | [🔍]({{< ref "../localstack/metric-coverage/#sqs" >}}) |                 |       |
| Message Visibility                                                 | ⭐⭐⭐⭐       |                 |       |
| Messages                                                           | ⭐⭐⭐⭐       |                 |       |
| Permission                                                         | ⭐⭐⭐         |                 |       |
| Queues                                                             | ⭐⭐⭐⭐       |                 |       |
| Tags                                                               | ⭐⭐⭐⭐       |                 |       |
| [**SSM**]({{< ref "systems-manager" >}})                           | [🔍]({{< ref "../localstack/metric-coverage/#ssm" >}}) |                 |       |
| Associations                                                       | ⭐⭐⭐         |                 |       |
| Calendar States                                                    | ⭐⭐           |                 |       |
| Commands / Command Invocations                                     | ⭐⭐⭐         |                 |       |
| Compliance Items                                                   | ⭐⭐           |                 |       |
| Documents                                                          | ⭐⭐⭐         |                 |       |
| Inventory Entries                                                  | \-             |                 |       |
| Ops Metadata                                                       | ⭐⭐           |                 |       |
| Parameters                                                         | ⭐⭐⭐⭐       |                 |       |
| Resource Compliance Summaries                                      | \-             |                 |       |
| Tags                                                               | ⭐⭐⭐⭐       |                 |       |
| **StepFunctions**                                                  | [🔍]({{< ref "../localstack/metric-coverage/#stepfunctions" >}}) |                 |       |
| Activities                                                         | ⭐⭐⭐⭐       |                 |       |
| Executions / Execution History                                     | ⭐⭐⭐⭐       |                 |       |
| State Machines                                                     | ⭐⭐⭐⭐       |                 |       |
| Tags                                                               | ⭐⭐⭐⭐       |                 |       |
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

## API Persistence Coverage (Pro)

The list below summarizes the APIs for which persistence has been implemented and (ideally) tested in the Pro version (list may not be exhaustive/complete). More details following soon.

- Amplify
- Appconfig
- Appsync
- Athena
- Backup
- Cognito Identity
- Cognito Identity Provider
- CloudFormation
- CloudFront
- CodeCommit
- Cost Explorer
- DynamoDB
- EC2
- Elastic File System
- Glue
- IoT
- Kinesis
- Lake Formation
- Lambda
- KMS
- QLDB
- Route53
- RDS
- S3
- Secrets Manager
- Serverless Repo
- SES
- SNS
- SQS
- Stepfunctions
- STS
