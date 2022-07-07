---
title: "LocalStack Metric Coverage"
linkTitle: "LocalStack Metric Coverage"
weight: 100
description: >
  Overview of the implemented AWS APIs and integration test coverage in LocalStack
---



## acm ##

API returns a response for 73.3% of the operations.

| Operation                              | Implemented | Tested |
|----------------------------------------|-------------|--------|
| AddTagsToCertificate                   | ✅         | ❌    |
| DeleteCertificate                      | ✅         | ✅    |
| DescribeCertificate                    | ✅         | ✅    |
| ExportCertificate                      | ✅         | ❌    |
| GetAccountConfiguration                | ❌         | ❌    |
| GetCertificate                         | ✅         | ❌    |
| ImportCertificate                      | ✅         | ✅    |
| ListCertificates                       | ✅         | ✅    |
| ListTagsForCertificate                 | ✅         | ✅    |
| PutAccountConfiguration                | ❌         | ❌    |
| RemoveTagsFromCertificate              | ✅         | ❌    |
| RenewCertificate                       | ❌         | ❌    |
| RequestCertificate                     | ✅         | ✅    |
| ResendValidationEmail                  | ✅         | ❌    |
| UpdateCertificateOptions               | ❌         | ❌    |



## amplify ##

API returns a response for 51.4% of the operations.

| Operation                              | Implemented | Tested |
|----------------------------------------|-------------|--------|
| CreateApp                              | ✅         | ✅    |
| CreateBackendEnvironment               | ✅         | ✅    |
| CreateBranch                           | ✅         | ✅    |
| CreateDeployment                       | ❌         | ❌    |
| CreateDomainAssociation                | ❌         | ❌    |
| CreateWebhook                          | ✅         | ✅    |
| DeleteApp                              | ✅         | ✅    |
| DeleteBackendEnvironment               | ✅         | ✅    |
| DeleteBranch                           | ✅         | ✅    |
| DeleteDomainAssociation                | ❌         | ❌    |
| DeleteJob                              | ❌         | ❌    |
| DeleteWebhook                          | ✅         | ✅    |
| GenerateAccessLogs                     | ❌         | ❌    |
| GetApp                                 | ✅         | ✅    |
| GetArtifactUrl                         | ❌         | ❌    |
| GetBackendEnvironment                  | ✅         | ✅    |
| GetBranch                              | ✅         | ✅    |
| GetDomainAssociation                   | ❌         | ❌    |
| GetJob                                 | ❌         | ❌    |
| GetWebhook                             | ✅         | ✅    |
| ListApps                               | ✅         | ✅    |
| ListArtifacts                          | ❌         | ❌    |
| ListBackendEnvironments                | ❌         | ❌    |
| ListBranches                           | ✅         | ✅    |
| ListDomainAssociations                 | ❌         | ❌    |
| ListJobs                               | ❌         | ❌    |
| ListTagsForResource                    | ✅         | ✅    |
| ListWebhooks                           | ❌         | ❌    |
| StartDeployment                        | ❌         | ❌    |
| StartJob                               | ❌         | ❌    |
| StopJob                                | ❌         | ❌    |
| TagResource                            | ✅         | ✅    |
| UntagResource                          | ✅         | ✅    |
| UpdateApp                              | ✅         | ✅    |
| UpdateBranch                           | ❌         | ❌    |
| UpdateDomainAssociation                | ❌         | ❌    |
| UpdateWebhook                          | ✅         | ✅    |



## apigateway ##

API returns a response for 88.3% of the operations.

| Operation                              | Implemented | Tested |
|----------------------------------------|-------------|--------|
| CreateApiKey                           | ✅         | ✅    |
| CreateAuthorizer                       | ✅         | ✅    |
| CreateBasePathMapping                  | ✅         | ✅    |
| CreateDeployment                       | ✅         | ✅    |
| CreateDocumentationPart                | ✅         | ❌    |
| CreateDocumentationVersion             | ❌         | ❌    |
| CreateDomainName                       | ✅         | ✅    |
| CreateModel                            | ✅         | ✅    |
| CreateRequestValidator                 | ✅         | ✅    |
| CreateResource                         | ✅         | ✅    |
| CreateRestApi                          | ✅         | ✅    |
| CreateStage                            | ✅         | ✅    |
| CreateUsagePlan                        | ✅         | ✅    |
| CreateUsagePlanKey                     | ✅         | ✅    |
| CreateVpcLink                          | ✅         | ❌    |
| DeleteApiKey                           | ✅         | ✅    |
| DeleteAuthorizer                       | ✅         | ✅    |
| DeleteBasePathMapping                  | ✅         | ✅    |
| DeleteClientCertificate                | ✅         | ❌    |
| DeleteDeployment                       | ✅         | ❌    |
| DeleteDocumentationPart                | ✅         | ❌    |
| DeleteDocumentationVersion             | ❌         | ❌    |
| DeleteDomainName                       | ✅         | ✅    |
| DeleteGatewayResponse                  | ✅         | ❌    |
| DeleteIntegration                      | ✅         | ✅    |
| DeleteIntegrationResponse              | ✅         | ✅    |
| DeleteMethod                           | ✅         | ✅    |
| DeleteMethodResponse                   | ✅         | ✅    |
| DeleteModel                            | ✅         | ❌    |
| DeleteRequestValidator                 | ✅         | ✅    |
| DeleteResource                         | ✅         | ✅    |
| DeleteRestApi                          | ✅         | ✅    |
| DeleteStage                            | ✅         | ✅    |
| DeleteUsagePlan                        | ✅         | ❌    |
| DeleteUsagePlanKey                     | ✅         | ❌    |
| DeleteVpcLink                          | ✅         | ❌    |
| FlushStageAuthorizersCache             | ❌         | ❌    |
| FlushStageCache                        | ❌         | ❌    |
| GenerateClientCertificate              | ✅         | ❌    |
| GetAccount                             | ✅         | ✅    |
| GetApiKey                              | ✅         | ❌    |
| GetApiKeys                             | ✅         | ✅    |
| GetAuthorizer                          | ✅         | ✅    |
| GetAuthorizers                         | ✅         | ✅    |
| GetBasePathMapping                     | ✅         | ✅    |
| GetBasePathMappings                    | ✅         | ✅    |
| GetClientCertificate                   | ✅         | ❌    |
| GetClientCertificates                  | ✅         | ❌    |
| GetDeployment                          | ✅         | ✅    |
| GetDeployments                         | ✅         | ✅    |
| GetDocumentationPart                   | ✅         | ❌    |
| GetDocumentationParts                  | ✅         | ❌    |
| GetDocumentationVersion                | ❌         | ❌    |
| GetDocumentationVersions               | ❌         | ❌    |
| GetDomainName                          | ✅         | ✅    |
| GetDomainNames                         | ✅         | ✅    |
| GetExport                              | ✅         | ✅    |
| GetGatewayResponse                     | ✅         | ❌    |
| GetGatewayResponses                    | ✅         | ❌    |
| GetIntegration                         | ✅         | ✅    |
| GetIntegrationResponse                 | ✅         | ✅    |
| GetMethod                              | ✅         | ✅    |
| GetMethodResponse                      | ✅         | ✅    |
| GetModel                               | ✅         | ✅    |
| GetModelTemplate                       | ❌         | ❌    |
| GetModels                              | ✅         | ✅    |
| GetRequestValidator                    | ✅         | ✅    |
| GetRequestValidators                   | ✅         | ✅    |
| GetResource                            | ✅         | ✅    |
| GetResources                           | ✅         | ✅    |
| GetRestApi                             | ✅         | ✅    |
| GetRestApis                            | ✅         | ✅    |
| GetSdk                                 | ❌         | ❌    |
| GetSdkType                             | ❌         | ❌    |
| GetSdkTypes                            | ❌         | ❌    |
| GetStage                               | ✅         | ✅    |
| GetStages                              | ✅         | ❌    |
| GetTags                                | ✅         | ✅    |
| GetUsage                               | ❌         | ❌    |
| GetUsagePlan                           | ✅         | ❌    |
| GetUsagePlanKey                        | ✅         | ❌    |
| GetUsagePlanKeys                       | ✅         | ✅    |
| GetUsagePlans                          | ✅         | ✅    |
| GetVpcLink                             | ✅         | ❌    |
| GetVpcLinks                            | ✅         | ❌    |
| ImportApiKeys                          | ✅         | ❌    |
| ImportDocumentationParts               | ❌         | ❌    |
| ImportRestApi                          | ✅         | ✅    |
| PutGatewayResponse                     | ✅         | ❌    |
| PutIntegration                         | ✅         | ✅    |
| PutIntegrationResponse                 | ✅         | ✅    |
| PutMethod                              | ✅         | ✅    |
| PutMethodResponse                      | ✅         | ✅    |
| PutRestApi                             | ✅         | ✅    |
| TagResource                            | ✅         | ✅    |
| TestInvokeAuthorizer                   | ✅         | ❌    |
| TestInvokeMethod                       | ✅         | ✅    |
| UntagResource                          | ✅         | ❌    |
| UpdateAccount                          | ✅         | ✅    |
| UpdateApiKey                           | ✅         | ❌    |
| UpdateAuthorizer                       | ✅         | ✅    |
| UpdateBasePathMapping                  | ✅         | ✅    |
| UpdateClientCertificate                | ✅         | ❌    |
| UpdateDeployment                       | ✅         | ❌    |
| UpdateDocumentationPart                | ✅         | ❌    |
| UpdateDocumentationVersion             | ❌         | ❌    |
| UpdateDomainName                       | ✅         | ❌    |
| UpdateGatewayResponse                  | ✅         | ❌    |
| UpdateIntegration                      | ✅         | ❌    |
| UpdateIntegrationResponse              | ✅         | ❌    |
| UpdateMethod                           | ✅         | ✅    |
| UpdateMethodResponse                   | ✅         | ❌    |
| UpdateModel                            | ✅         | ❌    |
| UpdateRequestValidator                 | ✅         | ✅    |
| UpdateResource                         | ✅         | ✅    |
| UpdateRestApi                          | ✅         | ✅    |
| UpdateStage                            | ✅         | ❌    |
| UpdateUsage                            | ❌         | ❌    |
| UpdateUsagePlan                        | ✅         | ❌    |
| UpdateVpcLink                          | ✅         | ❌    |



## apigatewaymanagementapi ##

API returns a response for 100.0% of the operations.

| Operation                              | Implemented | Tested |
|----------------------------------------|-------------|--------|
| DeleteConnection                       | ✅         | ❌    |
| GetConnection                          | ✅         | ❌    |
| PostToConnection                       | ✅         | ✅    |



## apigatewayv2 ##

API returns a response for 91.7% of the operations.

| Operation                              | Implemented | Tested |
|----------------------------------------|-------------|--------|
| CreateApi                              | ✅         | ✅    |
| CreateApiMapping                       | ✅         | ✅    |
| CreateAuthorizer                       | ✅         | ✅    |
| CreateDeployment                       | ✅         | ✅    |
| CreateDomainName                       | ✅         | ✅    |
| CreateIntegration                      | ✅         | ✅    |
| CreateIntegrationResponse              | ✅         | ✅    |
| CreateModel                            | ✅         | ✅    |
| CreateRoute                            | ✅         | ✅    |
| CreateRouteResponse                    | ✅         | ✅    |
| CreateStage                            | ✅         | ✅    |
| CreateVpcLink                          | ✅         | ✅    |
| DeleteAccessLogSettings                | ❌         | ❌    |
| DeleteApi                              | ✅         | ✅    |
| DeleteApiMapping                       | ✅         | ❌    |
| DeleteAuthorizer                       | ✅         | ✅    |
| DeleteCorsConfiguration                | ✅         | ❌    |
| DeleteDeployment                       | ✅         | ✅    |
| DeleteDomainName                       | ✅         | ✅    |
| DeleteIntegration                      | ✅         | ✅    |
| DeleteIntegrationResponse              | ✅         | ✅    |
| DeleteModel                            | ✅         | ❌    |
| DeleteRoute                            | ✅         | ✅    |
| DeleteRouteRequestParameter            | ❌         | ❌    |
| DeleteRouteResponse                    | ✅         | ✅    |
| DeleteRouteSettings                    | ❌         | ❌    |
| DeleteStage                            | ✅         | ✅    |
| DeleteVpcLink                          | ✅         | ✅    |
| ExportApi                              | ❌         | ❌    |
| GetApi                                 | ✅         | ✅    |
| GetApiMapping                          | ✅         | ❌    |
| GetApiMappings                         | ✅         | ❌    |
| GetApis                                | ✅         | ✅    |
| GetAuthorizer                          | ✅         | ✅    |
| GetAuthorizers                         | ✅         | ✅    |
| GetDeployment                          | ✅         | ✅    |
| GetDeployments                         | ✅         | ✅    |
| GetDomainName                          | ✅         | ✅    |
| GetDomainNames                         | ✅         | ✅    |
| GetIntegration                         | ✅         | ✅    |
| GetIntegrationResponse                 | ✅         | ✅    |
| GetIntegrationResponses                | ✅         | ✅    |
| GetIntegrations                        | ✅         | ✅    |
| GetModel                               | ✅         | ❌    |
| GetModelTemplate                       | ❌         | ❌    |
| GetModels                              | ✅         | ✅    |
| GetRoute                               | ✅         | ✅    |
| GetRouteResponse                       | ✅         | ✅    |
| GetRouteResponses                      | ✅         | ✅    |
| GetRoutes                              | ✅         | ✅    |
| GetStage                               | ✅         | ✅    |
| GetStages                              | ✅         | ❌    |
| GetTags                                | ✅         | ❌    |
| GetVpcLink                             | ✅         | ❌    |
| GetVpcLinks                            | ✅         | ✅    |
| ImportApi                              | ✅         | ✅    |
| ReimportApi                            | ✅         | ✅    |
| ResetAuthorizersCache                  | ❌         | ❌    |
| TagResource                            | ✅         | ❌    |
| UntagResource                          | ✅         | ❌    |
| UpdateApi                              | ✅         | ❌    |
| UpdateApiMapping                       | ✅         | ❌    |
| UpdateAuthorizer                       | ✅         | ❌    |
| UpdateDeployment                       | ✅         | ❌    |
| UpdateDomainName                       | ✅         | ❌    |
| UpdateIntegration                      | ✅         | ✅    |
| UpdateIntegrationResponse              | ✅         | ✅    |
| UpdateModel                            | ✅         | ❌    |
| UpdateRoute                            | ✅         | ✅    |
| UpdateRouteResponse                    | ✅         | ✅    |
| UpdateStage                            | ✅         | ✅    |
| UpdateVpcLink                          | ✅         | ❌    |



## appconfig ##

API returns a response for 100.0% of the operations.

| Operation                              | Implemented | Tested |
|----------------------------------------|-------------|--------|
| CreateApplication                      | ✅         | ✅    |
| CreateConfigurationProfile             | ✅         | ✅    |
| CreateDeploymentStrategy               | ✅         | ✅    |
| CreateEnvironment                      | ✅         | ✅    |
| CreateHostedConfigurationVersion       | ✅         | ✅    |
| DeleteApplication                      | ✅         | ✅    |
| DeleteConfigurationProfile             | ✅         | ✅    |
| DeleteDeploymentStrategy               | ✅         | ✅    |
| DeleteEnvironment                      | ✅         | ✅    |
| DeleteHostedConfigurationVersion       | ✅         | ✅    |
| GetApplication                         | ✅         | ✅    |
| GetConfiguration                       | ✅         | ✅    |
| GetConfigurationProfile                | ✅         | ✅    |
| GetDeployment                          | ✅         | ❌    |
| GetDeploymentStrategy                  | ✅         | ✅    |
| GetEnvironment                         | ✅         | ✅    |
| GetHostedConfigurationVersion          | ✅         | ✅    |
| ListApplications                       | ✅         | ✅    |
| ListConfigurationProfiles              | ✅         | ✅    |
| ListDeploymentStrategies               | ✅         | ✅    |
| ListDeployments                        | ✅         | ✅    |
| ListEnvironments                       | ✅         | ✅    |
| ListHostedConfigurationVersions        | ✅         | ✅    |
| ListTagsForResource                    | ✅         | ❌    |
| StartDeployment                        | ✅         | ✅    |
| StopDeployment                         | ✅         | ❌    |
| TagResource                            | ✅         | ❌    |
| UntagResource                          | ✅         | ❌    |
| UpdateApplication                      | ✅         | ✅    |
| UpdateConfigurationProfile             | ✅         | ✅    |
| UpdateDeploymentStrategy               | ✅         | ✅    |
| UpdateEnvironment                      | ✅         | ✅    |
| ValidateConfiguration                  | ✅         | ✅    |



## application-autoscaling ##

API returns a response for 90.0% of the operations.

| Operation                              | Implemented | Tested |
|----------------------------------------|-------------|--------|
| DeleteScalingPolicy                    | ✅         | ✅    |
| DeleteScheduledAction                  | ✅         | ❌    |
| DeregisterScalableTarget               | ✅         | ✅    |
| DescribeScalableTargets                | ✅         | ✅    |
| DescribeScalingActivities              | ❌         | ❌    |
| DescribeScalingPolicies                | ✅         | ✅    |
| DescribeScheduledActions               | ✅         | ❌    |
| PutScalingPolicy                       | ✅         | ✅    |
| PutScheduledAction                     | ✅         | ❌    |
| RegisterScalableTarget                 | ✅         | ✅    |



## appsync ##

API returns a response for 93.9% of the operations.

| Operation                              | Implemented | Tested |
|----------------------------------------|-------------|--------|
| AssociateApi                           | ❌         | ❌    |
| CreateApiCache                         | ✅         | ✅    |
| CreateApiKey                           | ✅         | ✅    |
| CreateDataSource                       | ✅         | ✅    |
| CreateDomainName                       | ✅         | ❌    |
| CreateFunction                         | ✅         | ✅    |
| CreateGraphqlApi                       | ✅         | ✅    |
| CreateResolver                         | ✅         | ✅    |
| CreateType                             | ✅         | ❌    |
| DeleteApiCache                         | ✅         | ❌    |
| DeleteApiKey                           | ✅         | ❌    |
| DeleteDataSource                       | ✅         | ❌    |
| DeleteDomainName                       | ✅         | ❌    |
| DeleteFunction                         | ✅         | ❌    |
| DeleteGraphqlApi                       | ✅         | ✅    |
| DeleteResolver                         | ✅         | ✅    |
| DeleteType                             | ✅         | ❌    |
| DisassociateApi                        | ❌         | ❌    |
| FlushApiCache                          | ✅         | ❌    |
| GetApiAssociation                      | ❌         | ❌    |
| GetApiCache                            | ✅         | ❌    |
| GetDataSource                          | ✅         | ❌    |
| GetDomainName                          | ✅         | ❌    |
| GetFunction                            | ✅         | ✅    |
| GetGraphqlApi                          | ✅         | ✅    |
| GetIntrospectionSchema                 | ✅         | ✅    |
| GetResolver                            | ✅         | ✅    |
| GetSchemaCreationStatus                | ✅         | ✅    |
| GetType                                | ✅         | ❌    |
| ListApiKeys                            | ✅         | ✅    |
| ListDataSources                        | ✅         | ✅    |
| ListDomainNames                        | ✅         | ❌    |
| ListFunctions                          | ✅         | ✅    |
| ListGraphqlApis                        | ✅         | ✅    |
| ListResolvers                          | ✅         | ✅    |
| ListResolversByFunction                | ✅         | ❌    |
| ListTagsForResource                    | ✅         | ✅    |
| ListTypes                              | ✅         | ❌    |
| StartSchemaCreation                    | ✅         | ✅    |
| TagResource                            | ✅         | ✅    |
| UntagResource                          | ✅         | ❌    |
| UpdateApiCache                         | ✅         | ✅    |
| UpdateApiKey                           | ✅         | ✅    |
| UpdateDataSource                       | ✅         | ❌    |
| UpdateDomainName                       | ✅         | ❌    |
| UpdateFunction                         | ✅         | ❌    |
| UpdateGraphqlApi                       | ✅         | ❌    |
| UpdateResolver                         | ✅         | ✅    |
| UpdateType                             | ✅         | ❌    |



## athena ##

API returns a response for 61.1% of the operations.

| Operation                              | Implemented | Tested |
|----------------------------------------|-------------|--------|
| BatchGetNamedQuery                     | ❌         | ❌    |
| BatchGetPreparedStatement              | ✅         | ❌    |
| BatchGetQueryExecution                 | ❌         | ❌    |
| CreateDataCatalog                      | ✅         | ✅    |
| CreateNamedQuery                       | ✅         | ✅    |
| CreatePreparedStatement                | ❌         | ❌    |
| CreateWorkGroup                        | ✅         | ✅    |
| DeleteDataCatalog                      | ✅         | ✅    |
| DeleteNamedQuery                       | ✅         | ✅    |
| DeletePreparedStatement                | ❌         | ❌    |
| DeleteWorkGroup                        | ✅         | ✅    |
| GetDataCatalog                         | ✅         | ✅    |
| GetDatabase                            | ✅         | ❌    |
| GetNamedQuery                          | ✅         | ❌    |
| GetPreparedStatement                   | ❌         | ❌    |
| GetQueryExecution                      | ✅         | ❌    |
| GetQueryResults                        | ✅         | ❌    |
| GetTableMetadata                       | ❌         | ❌    |
| GetWorkGroup                           | ✅         | ✅    |
| ListDataCatalogs                       | ✅         | ✅    |
| ListDatabases                          | ✅         | ❌    |
| ListEngineVersions                     | ❌         | ❌    |
| ListNamedQueries                       | ✅         | ✅    |
| ListPreparedStatements                 | ❌         | ❌    |
| ListQueryExecutions                    | ✅         | ❌    |
| ListTableMetadata                      | ❌         | ❌    |
| ListTagsForResource                    | ✅         | ✅    |
| ListWorkGroups                         | ✅         | ✅    |
| StartQueryExecution                    | ✅         | ❌    |
| StopQueryExecution                     | ❌         | ❌    |
| TagResource                            | ✅         | ✅    |
| UntagResource                          | ✅         | ✅    |
| UpdateDataCatalog                      | ❌         | ❌    |
| UpdateNamedQuery                       | ❌         | ❌    |
| UpdatePreparedStatement                | ❌         | ❌    |
| UpdateWorkGroup                        | ❌         | ❌    |



## autoscaling ##

API returns a response for 60.7% of the operations.

| Operation                              | Implemented | Tested |
|----------------------------------------|-------------|--------|
| AttachInstances                        | ✅         | ❌    |
| AttachLoadBalancerTargetGroups         | ✅         | ❌    |
| AttachLoadBalancers                    | ✅         | ❌    |
| BatchDeleteScheduledAction             | ❌         | ❌    |
| BatchPutScheduledUpdateGroupAction     | ❌         | ❌    |
| CancelInstanceRefresh                  | ❌         | ❌    |
| CompleteLifecycleAction                | ❌         | ❌    |
| CreateAutoScalingGroup                 | ✅         | ❌    |
| CreateLaunchConfiguration              | ✅         | ❌    |
| CreateOrUpdateTags                     | ✅         | ❌    |
| DeleteAutoScalingGroup                 | ✅         | ❌    |
| DeleteLaunchConfiguration              | ✅         | ❌    |
| DeleteLifecycleHook                    | ✅         | ❌    |
| DeleteNotificationConfiguration        | ❌         | ❌    |
| DeletePolicy                           | ✅         | ❌    |
| DeleteScheduledAction                  | ❌         | ❌    |
| DeleteTags                             | ✅         | ❌    |
| DeleteWarmPool                         | ❌         | ❌    |
| DescribeAccountLimits                  | ❌         | ❌    |
| DescribeAdjustmentTypes                | ❌         | ❌    |
| DescribeAutoScalingGroups              | ✅         | ❌    |
| DescribeAutoScalingInstances           | ✅         | ❌    |
| DescribeAutoScalingNotificationTypes   | ❌         | ❌    |
| DescribeInstanceRefreshes              | ❌         | ❌    |
| DescribeLaunchConfigurations           | ✅         | ❌    |
| DescribeLifecycleHookTypes             | ❌         | ❌    |
| DescribeLifecycleHooks                 | ✅         | ❌    |
| DescribeLoadBalancerTargetGroups       | ✅         | ❌    |
| DescribeLoadBalancers                  | ✅         | ❌    |
| DescribeMetricCollectionTypes          | ✅         | ✅    |
| DescribeNotificationConfigurations     | ❌         | ❌    |
| DescribePolicies                       | ✅         | ❌    |
| DescribeScalingActivities              | ❌         | ❌    |
| DescribeScalingProcessTypes            | ❌         | ❌    |
| DescribeScheduledActions               | ❌         | ❌    |
| DescribeTags                           | ✅         | ❌    |
| DescribeTerminationPolicyTypes         | ❌         | ❌    |
| DescribeWarmPool                       | ❌         | ❌    |
| DetachInstances                        | ✅         | ❌    |
| DetachLoadBalancerTargetGroups         | ✅         | ❌    |
| DetachLoadBalancers                    | ✅         | ❌    |
| DisableMetricsCollection               | ✅         | ✅    |
| EnableMetricsCollection                | ✅         | ✅    |
| EnterStandby                           | ✅         | ❌    |
| ExecutePolicy                          | ✅         | ❌    |
| ExitStandby                            | ✅         | ❌    |
| GetPredictiveScalingForecast           | ❌         | ❌    |
| PutLifecycleHook                       | ✅         | ❌    |
| PutNotificationConfiguration           | ❌         | ❌    |
| PutScalingPolicy                       | ✅         | ❌    |
| PutScheduledUpdateGroupAction          | ❌         | ❌    |
| PutWarmPool                            | ❌         | ❌    |
| RecordLifecycleActionHeartbeat         | ❌         | ❌    |
| ResumeProcesses                        | ✅         | ❌    |
| SetDesiredCapacity                     | ✅         | ❌    |
| SetInstanceHealth                      | ✅         | ❌    |
| SetInstanceProtection                  | ✅         | ❌    |
| StartInstanceRefresh                   | ❌         | ❌    |
| SuspendProcesses                       | ✅         | ❌    |
| TerminateInstanceInAutoScalingGroup    | ✅         | ❌    |
| UpdateAutoScalingGroup                 | ✅         | ❌    |



## backup ##

API returns a response for 31.8% of the operations.

| Operation                              | Implemented | Tested |
|----------------------------------------|-------------|--------|
| CreateBackupPlan                       | ✅         | ✅    |
| CreateBackupSelection                  | ✅         | ✅    |
| CreateBackupVault                      | ✅         | ✅    |
| CreateFramework                        | ❌         | ❌    |
| CreateReportPlan                       | ❌         | ❌    |
| DeleteBackupPlan                       | ✅         | ✅    |
| DeleteBackupSelection                  | ✅         | ✅    |
| DeleteBackupVault                      | ✅         | ✅    |
| DeleteBackupVaultAccessPolicy          | ❌         | ❌    |
| DeleteBackupVaultLockConfiguration     | ❌         | ❌    |
| DeleteBackupVaultNotifications         | ❌         | ❌    |
| DeleteFramework                        | ❌         | ❌    |
| DeleteRecoveryPoint                    | ❌         | ❌    |
| DeleteReportPlan                       | ❌         | ❌    |
| DescribeBackupJob                      | ❌         | ❌    |
| DescribeBackupVault                    | ✅         | ✅    |
| DescribeCopyJob                        | ❌         | ❌    |
| DescribeFramework                      | ❌         | ❌    |
| DescribeGlobalSettings                 | ❌         | ❌    |
| DescribeProtectedResource              | ❌         | ❌    |
| DescribeRecoveryPoint                  | ❌         | ❌    |
| DescribeRegionSettings                 | ❌         | ❌    |
| DescribeReportJob                      | ❌         | ❌    |
| DescribeReportPlan                     | ❌         | ❌    |
| DescribeRestoreJob                     | ✅         | ✅    |
| DisassociateRecoveryPoint              | ❌         | ❌    |
| ExportBackupPlanTemplate               | ❌         | ❌    |
| GetBackupPlan                          | ✅         | ✅    |
| GetBackupPlanFromJSON                  | ❌         | ❌    |
| GetBackupPlanFromTemplate              | ❌         | ❌    |
| GetBackupSelection                     | ✅         | ✅    |
| GetBackupVaultAccessPolicy             | ❌         | ❌    |
| GetBackupVaultNotifications            | ❌         | ❌    |
| GetRecoveryPointRestoreMetadata        | ❌         | ❌    |
| GetSupportedResourceTypes              | ❌         | ❌    |
| ListBackupJobs                         | ✅         | ❌    |
| ListBackupPlanTemplates                | ❌         | ❌    |
| ListBackupPlanVersions                 | ❌         | ❌    |
| ListBackupPlans                        | ✅         | ✅    |
| ListBackupSelections                   | ✅         | ✅    |
| ListBackupVaults                       | ✅         | ✅    |
| ListCopyJobs                           | ✅         | ❌    |
| ListFrameworks                         | ❌         | ❌    |
| ListProtectedResources                 | ❌         | ❌    |
| ListRecoveryPointsByBackupVault        | ✅         | ✅    |
| ListRecoveryPointsByResource           | ✅         | ✅    |
| ListReportJobs                         | ✅         | ❌    |
| ListReportPlans                        | ❌         | ❌    |
| ListRestoreJobs                        | ✅         | ❌    |
| ListTags                               | ❌         | ❌    |
| PutBackupVaultAccessPolicy             | ❌         | ❌    |
| PutBackupVaultLockConfiguration        | ❌         | ❌    |
| PutBackupVaultNotifications            | ❌         | ❌    |
| StartBackupJob                         | ❌         | ❌    |
| StartCopyJob                           | ❌         | ❌    |
| StartReportJob                         | ❌         | ❌    |
| StartRestoreJob                        | ✅         | ✅    |
| StopBackupJob                          | ❌         | ❌    |
| TagResource                            | ❌         | ❌    |
| UntagResource                          | ❌         | ❌    |
| UpdateBackupPlan                       | ✅         | ✅    |
| UpdateFramework                        | ❌         | ❌    |
| UpdateGlobalSettings                   | ❌         | ❌    |
| UpdateRecoveryPointLifecycle           | ❌         | ❌    |
| UpdateRegionSettings                   | ❌         | ❌    |
| UpdateReportPlan                       | ❌         | ❌    |



## batch ##

API returns a response for 100.0% of the operations.

| Operation                              | Implemented | Tested |
|----------------------------------------|-------------|--------|
| CancelJob                              | ✅         | ❌    |
| CreateComputeEnvironment               | ✅         | ✅    |
| CreateJobQueue                         | ✅         | ✅    |
| CreateSchedulingPolicy                 | ✅         | ❌    |
| DeleteComputeEnvironment               | ✅         | ❌    |
| DeleteJobQueue                         | ✅         | ✅    |
| DeleteSchedulingPolicy                 | ✅         | ❌    |
| DeregisterJobDefinition                | ✅         | ✅    |
| DescribeComputeEnvironments            | ✅         | ❌    |
| DescribeJobDefinitions                 | ✅         | ✅    |
| DescribeJobQueues                      | ✅         | ❌    |
| DescribeJobs                           | ✅         | ✅    |
| DescribeSchedulingPolicies             | ✅         | ❌    |
| ListJobs                               | ✅         | ❌    |
| ListSchedulingPolicies                 | ✅         | ❌    |
| ListTagsForResource                    | ✅         | ❌    |
| RegisterJobDefinition                  | ✅         | ✅    |
| SubmitJob                              | ✅         | ✅    |
| TagResource                            | ✅         | ❌    |
| TerminateJob                           | ✅         | ❌    |
| UntagResource                          | ✅         | ❌    |
| UpdateComputeEnvironment               | ✅         | ❌    |
| UpdateJobQueue                         | ✅         | ❌    |
| UpdateSchedulingPolicy                 | ✅         | ❌    |



## ce ##

API returns a response for 34.3% of the operations.

| Operation                              | Implemented | Tested |
|----------------------------------------|-------------|--------|
| CreateAnomalyMonitor                   | ✅         | ✅    |
| CreateAnomalySubscription              | ✅         | ✅    |
| CreateCostCategoryDefinition           | ✅         | ✅    |
| DeleteAnomalyMonitor                   | ✅         | ✅    |
| DeleteAnomalySubscription              | ✅         | ✅    |
| DeleteCostCategoryDefinition           | ✅         | ✅    |
| DescribeCostCategoryDefinition         | ✅         | ✅    |
| GetAnomalies                           | ❌         | ❌    |
| GetAnomalyMonitors                     | ✅         | ✅    |
| GetAnomalySubscriptions                | ✅         | ✅    |
| GetCostAndUsage                        | ❌         | ❌    |
| GetCostAndUsageWithResources           | ❌         | ❌    |
| GetCostCategories                      | ❌         | ❌    |
| GetCostForecast                        | ❌         | ❌    |
| GetDimensionValues                     | ❌         | ❌    |
| GetReservationCoverage                 | ❌         | ❌    |
| GetReservationPurchaseRecommendation   | ❌         | ❌    |
| GetReservationUtilization              | ❌         | ❌    |
| GetRightsizingRecommendation           | ❌         | ❌    |
| GetSavingsPlansCoverage                | ❌         | ❌    |
| GetSavingsPlansPurchaseRecommendation  | ❌         | ❌    |
| GetSavingsPlansUtilization             | ❌         | ❌    |
| GetSavingsPlansUtilizationDetails      | ❌         | ❌    |
| GetTags                                | ❌         | ❌    |
| GetUsageForecast                       | ❌         | ❌    |
| ListCostAllocationTags                 | ❌         | ❌    |
| ListCostCategoryDefinitions            | ❌         | ❌    |
| ListTagsForResource                    | ❌         | ❌    |
| ProvideAnomalyFeedback                 | ❌         | ❌    |
| TagResource                            | ❌         | ❌    |
| UntagResource                          | ❌         | ❌    |
| UpdateAnomalyMonitor                   | ✅         | ✅    |
| UpdateAnomalySubscription              | ✅         | ✅    |
| UpdateCostAllocationTagsStatus         | ❌         | ❌    |
| UpdateCostCategoryDefinition           | ✅         | ✅    |



## cloudformation ##

API returns a response for 40.9% of the operations.

| Operation                              | Implemented | Tested |
|----------------------------------------|-------------|--------|
| ActivateType                           | ❌         | ❌    |
| BatchDescribeTypeConfigurations        | ❌         | ❌    |
| CancelUpdateStack                      | ❌         | ❌    |
| ContinueUpdateRollback                 | ❌         | ❌    |
| CreateChangeSet                        | ✅         | ✅    |
| CreateStack                            | ✅         | ✅    |
| CreateStackInstances                   | ✅         | ❌    |
| CreateStackSet                         | ✅         | ❌    |
| DeactivateType                         | ❌         | ❌    |
| DeleteChangeSet                        | ✅         | ✅    |
| DeleteStack                            | ✅         | ✅    |
| DeleteStackInstances                   | ❌         | ❌    |
| DeleteStackSet                         | ✅         | ❌    |
| DeregisterType                         | ❌         | ❌    |
| DescribeAccountLimits                  | ❌         | ❌    |
| DescribeChangeSet                      | ✅         | ✅    |
| DescribeChangeSetHooks                 | ❌         | ❌    |
| DescribePublisher                      | ❌         | ❌    |
| DescribeStackDriftDetectionStatus      | ❌         | ❌    |
| DescribeStackEvents                    | ✅         | ✅    |
| DescribeStackInstance                  | ❌         | ❌    |
| DescribeStackResource                  | ✅         | ✅    |
| DescribeStackResourceDrifts            | ❌         | ❌    |
| DescribeStackResources                 | ✅         | ✅    |
| DescribeStackSet                       | ✅         | ❌    |
| DescribeStackSetOperation              | ✅         | ❌    |
| DescribeStacks                         | ✅         | ✅    |
| DescribeType                           | ❌         | ❌    |
| DescribeTypeRegistration               | ❌         | ❌    |
| DetectStackDrift                       | ❌         | ❌    |
| DetectStackResourceDrift               | ❌         | ❌    |
| DetectStackSetDrift                    | ❌         | ❌    |
| EstimateTemplateCost                   | ❌         | ❌    |
| ExecuteChangeSet                       | ✅         | ✅    |
| GetStackPolicy                         | ❌         | ❌    |
| GetTemplate                            | ✅         | ✅    |
| GetTemplateSummary                     | ✅         | ✅    |
| ImportStacksToStackSet                 | ❌         | ❌    |
| ListChangeSets                         | ✅         | ❌    |
| ListExports                            | ✅         | ✅    |
| ListImports                            | ✅         | ❌    |
| ListStackInstances                     | ✅         | ❌    |
| ListStackResources                     | ✅         | ✅    |
| ListStackSetOperationResults           | ❌         | ❌    |
| ListStackSetOperations                 | ❌         | ❌    |
| ListStackSets                          | ✅         | ❌    |
| ListStacks                             | ✅         | ✅    |
| ListTypeRegistrations                  | ❌         | ❌    |
| ListTypeVersions                       | ❌         | ❌    |
| ListTypes                              | ❌         | ❌    |
| PublishType                            | ❌         | ❌    |
| RecordHandlerProgress                  | ❌         | ❌    |
| RegisterPublisher                      | ❌         | ❌    |
| RegisterType                           | ❌         | ❌    |
| RollbackStack                          | ❌         | ❌    |
| SetStackPolicy                         | ❌         | ❌    |
| SetTypeConfiguration                   | ❌         | ❌    |
| SetTypeDefaultVersion                  | ❌         | ❌    |
| SignalResource                         | ❌         | ❌    |
| StopStackSetOperation                  | ❌         | ❌    |
| TestType                               | ❌         | ❌    |
| UpdateStack                            | ✅         | ✅    |
| UpdateStackInstances                   | ❌         | ❌    |
| UpdateStackSet                         | ✅         | ❌    |
| UpdateTerminationProtection            | ❌         | ❌    |
| ValidateTemplate                       | ✅         | ✅    |



## cloudfront ##

API returns a response for 28.3% of the operations.

| Operation                              | Implemented | Tested |
|----------------------------------------|-------------|--------|
| AssociateAlias                         | ❌         | ❌    |
| CreateCachePolicy                      | ❌         | ❌    |
| CreateCloudFrontOriginAccessIdentity   | ✅         | ✅    |
| CreateDistribution                     | ✅         | ✅    |
| CreateDistributionWithTags             | ✅         | ✅    |
| CreateFieldLevelEncryptionConfig       | ❌         | ❌    |
| CreateFieldLevelEncryptionProfile      | ❌         | ❌    |
| CreateFunction                         | ✅         | ✅    |
| CreateInvalidation                     | ✅         | ✅    |
| CreateKeyGroup                         | ❌         | ❌    |
| CreateMonitoringSubscription           | ❌         | ❌    |
| CreateOriginRequestPolicy              | ✅         | ✅    |
| CreatePublicKey                        | ❌         | ❌    |
| CreateRealtimeLogConfig                | ❌         | ❌    |
| CreateResponseHeadersPolicy            | ❌         | ❌    |
| CreateStreamingDistribution            | ❌         | ❌    |
| CreateStreamingDistributionWithTags    | ❌         | ❌    |
| DeleteCachePolicy                      | ❌         | ❌    |
| DeleteCloudFrontOriginAccessIdentity   | ✅         | ✅    |
| DeleteDistribution                     | ✅         | ✅    |
| DeleteFieldLevelEncryptionConfig       | ❌         | ❌    |
| DeleteFieldLevelEncryptionProfile      | ❌         | ❌    |
| DeleteFunction                         | ✅         | ✅    |
| DeleteKeyGroup                         | ❌         | ❌    |
| DeleteMonitoringSubscription           | ❌         | ❌    |
| DeleteOriginRequestPolicy              | ✅         | ✅    |
| DeletePublicKey                        | ❌         | ❌    |
| DeleteRealtimeLogConfig                | ❌         | ❌    |
| DeleteResponseHeadersPolicy            | ❌         | ❌    |
| DeleteStreamingDistribution            | ❌         | ❌    |
| DescribeFunction                       | ❌         | ❌    |
| GetCachePolicy                         | ❌         | ❌    |
| GetCachePolicyConfig                   | ❌         | ❌    |
| GetCloudFrontOriginAccessIdentity      | ✅         | ✅    |
| GetCloudFrontOriginAccessIdentityConfig| ❌         | ❌    |
| GetDistribution                        | ✅         | ❌    |
| GetDistributionConfig                  | ❌         | ❌    |
| GetFieldLevelEncryption                | ❌         | ❌    |
| GetFieldLevelEncryptionConfig          | ❌         | ❌    |
| GetFieldLevelEncryptionProfile         | ❌         | ❌    |
| GetFieldLevelEncryptionProfileConfig   | ❌         | ❌    |
| GetFunction                            | ✅         | ✅    |
| GetInvalidation                        | ✅         | ✅    |
| GetKeyGroup                            | ❌         | ❌    |
| GetKeyGroupConfig                      | ❌         | ❌    |
| GetMonitoringSubscription              | ❌         | ❌    |
| GetOriginRequestPolicy                 | ✅         | ✅    |
| GetOriginRequestPolicyConfig           | ❌         | ❌    |
| GetPublicKey                           | ❌         | ❌    |
| GetPublicKeyConfig                     | ❌         | ❌    |
| GetRealtimeLogConfig                   | ❌         | ❌    |
| GetResponseHeadersPolicy               | ❌         | ❌    |
| GetResponseHeadersPolicyConfig         | ❌         | ❌    |
| GetStreamingDistribution               | ❌         | ❌    |
| GetStreamingDistributionConfig         | ❌         | ❌    |
| ListCachePolicies                      | ❌         | ❌    |
| ListCloudFrontOriginAccessIdentities   | ✅         | ✅    |
| ListConflictingAliases                 | ❌         | ❌    |
| ListDistributions                      | ✅         | ✅    |
| ListDistributionsByCachePolicyId       | ❌         | ❌    |
| ListDistributionsByKeyGroup            | ❌         | ❌    |
| ListDistributionsByOriginRequestPolicyId| ❌         | ❌    |
| ListDistributionsByRealtimeLogConfig   | ❌         | ❌    |
| ListDistributionsByResponseHeadersPolicyId| ❌         | ❌    |
| ListDistributionsByWebACLId            | ❌         | ❌    |
| ListFieldLevelEncryptionConfigs        | ❌         | ❌    |
| ListFieldLevelEncryptionProfiles       | ❌         | ❌    |
| ListFunctions                          | ✅         | ✅    |
| ListInvalidations                      | ✅         | ✅    |
| ListKeyGroups                          | ❌         | ❌    |
| ListOriginRequestPolicies              | ✅         | ✅    |
| ListPublicKeys                         | ❌         | ❌    |
| ListRealtimeLogConfigs                 | ❌         | ❌    |
| ListResponseHeadersPolicies            | ❌         | ❌    |
| ListStreamingDistributions             | ❌         | ❌    |
| ListTagsForResource                    | ✅         | ✅    |
| PublishFunction                        | ❌         | ❌    |
| TagResource                            | ✅         | ❌    |
| TestFunction                           | ❌         | ❌    |
| UntagResource                          | ✅         | ✅    |
| UpdateCachePolicy                      | ❌         | ❌    |
| UpdateCloudFrontOriginAccessIdentity   | ❌         | ❌    |
| UpdateDistribution                     | ✅         | ❌    |
| UpdateFieldLevelEncryptionConfig       | ❌         | ❌    |
| UpdateFieldLevelEncryptionProfile      | ❌         | ❌    |
| UpdateFunction                         | ✅         | ✅    |
| UpdateKeyGroup                         | ❌         | ❌    |
| UpdateOriginRequestPolicy              | ✅         | ✅    |
| UpdatePublicKey                        | ❌         | ❌    |
| UpdateRealtimeLogConfig                | ❌         | ❌    |
| UpdateResponseHeadersPolicy            | ❌         | ❌    |
| UpdateStreamingDistribution            | ❌         | ❌    |



## cloudtrail ##

API returns a response for 58.6% of the operations.

| Operation                              | Implemented | Tested |
|----------------------------------------|-------------|--------|
| AddTags                                | ✅         | ❌    |
| CancelQuery                            | ❌         | ❌    |
| CreateEventDataStore                   | ❌         | ❌    |
| CreateTrail                            | ✅         | ✅    |
| DeleteEventDataStore                   | ❌         | ❌    |
| DeleteTrail                            | ✅         | ✅    |
| DescribeQuery                          | ❌         | ❌    |
| DescribeTrails                         | ✅         | ✅    |
| GetEventDataStore                      | ❌         | ❌    |
| GetEventSelectors                      | ✅         | ❌    |
| GetInsightSelectors                    | ✅         | ❌    |
| GetQueryResults                        | ❌         | ❌    |
| GetTrail                               | ✅         | ✅    |
| GetTrailStatus                         | ✅         | ✅    |
| ListEventDataStores                    | ❌         | ❌    |
| ListPublicKeys                         | ❌         | ❌    |
| ListQueries                            | ❌         | ❌    |
| ListTags                               | ✅         | ✅    |
| ListTrails                             | ✅         | ✅    |
| LookupEvents                           | ✅         | ✅    |
| PutEventSelectors                      | ✅         | ✅    |
| PutInsightSelectors                    | ✅         | ❌    |
| RemoveTags                             | ✅         | ❌    |
| RestoreEventDataStore                  | ❌         | ❌    |
| StartLogging                           | ✅         | ✅    |
| StartQuery                             | ❌         | ❌    |
| StopLogging                            | ✅         | ✅    |
| UpdateEventDataStore                   | ❌         | ❌    |
| UpdateTrail                            | ✅         | ✅    |



## cloudwatch ##

API returns a response for 47.2% of the operations.

| Operation                              | Implemented | Tested |
|----------------------------------------|-------------|--------|
| DeleteAlarms                           | ✅         | ✅    |
| DeleteAnomalyDetector                  | ❌         | ❌    |
| DeleteDashboards                       | ✅         | ❌    |
| DeleteInsightRules                     | ❌         | ❌    |
| DeleteMetricStream                     | ❌         | ❌    |
| DescribeAlarmHistory                   | ❌         | ❌    |
| DescribeAlarms                         | ✅         | ✅    |
| DescribeAlarmsForMetric                | ✅         | ❌    |
| DescribeAnomalyDetectors               | ❌         | ❌    |
| DescribeInsightRules                   | ❌         | ❌    |
| DisableAlarmActions                    | ❌         | ❌    |
| DisableInsightRules                    | ❌         | ❌    |
| EnableAlarmActions                     | ❌         | ❌    |
| EnableInsightRules                     | ❌         | ❌    |
| GetDashboard                           | ✅         | ❌    |
| GetInsightRuleReport                   | ❌         | ❌    |
| GetMetricData                          | ✅         | ✅    |
| GetMetricStatistics                    | ✅         | ✅    |
| GetMetricStream                        | ❌         | ❌    |
| GetMetricWidgetImage                   | ❌         | ❌    |
| ListDashboards                         | ✅         | ❌    |
| ListMetricStreams                      | ❌         | ❌    |
| ListMetrics                            | ✅         | ✅    |
| ListTagsForResource                    | ✅         | ✅    |
| PutAnomalyDetector                     | ❌         | ❌    |
| PutCompositeAlarm                      | ✅         | ✅    |
| PutDashboard                           | ✅         | ❌    |
| PutInsightRule                         | ❌         | ❌    |
| PutMetricAlarm                         | ✅         | ✅    |
| PutMetricData                          | ✅         | ✅    |
| PutMetricStream                        | ❌         | ❌    |
| SetAlarmState                          | ✅         | ✅    |
| StartMetricStreams                     | ❌         | ❌    |
| StopMetricStreams                      | ❌         | ❌    |
| TagResource                            | ✅         | ✅    |
| UntagResource                          | ✅         | ✅    |



## codecommit ##

API returns a response for 18.2% of the operations.

| Operation                              | Implemented | Tested |
|----------------------------------------|-------------|--------|
| AssociateApprovalRuleTemplateWithRepository| ❌         | ❌    |
| BatchAssociateApprovalRuleTemplateWithRepositories| ❌         | ❌    |
| BatchDescribeMergeConflicts            | ❌         | ❌    |
| BatchDisassociateApprovalRuleTemplateFromRepositories| ❌         | ❌    |
| BatchGetCommits                        | ❌         | ❌    |
| BatchGetRepositories                   | ❌         | ❌    |
| CreateApprovalRuleTemplate             | ❌         | ❌    |
| CreateBranch                           | ✅         | ✅    |
| CreateCommit                           | ✅         | ✅    |
| CreatePullRequest                      | ✅         | ✅    |
| CreatePullRequestApprovalRule          | ❌         | ❌    |
| CreateRepository                       | ✅         | ✅    |
| CreateUnreferencedMergeCommit          | ❌         | ❌    |
| DeleteApprovalRuleTemplate             | ❌         | ❌    |
| DeleteBranch                           | ✅         | ✅    |
| DeleteCommentContent                   | ❌         | ❌    |
| DeleteFile                             | ❌         | ❌    |
| DeletePullRequestApprovalRule          | ❌         | ❌    |
| DeleteRepository                       | ✅         | ✅    |
| DescribeMergeConflicts                 | ❌         | ❌    |
| DescribePullRequestEvents              | ❌         | ❌    |
| DisassociateApprovalRuleTemplateFromRepository| ❌         | ❌    |
| EvaluatePullRequestApprovalRules       | ❌         | ❌    |
| GetApprovalRuleTemplate                | ❌         | ❌    |
| GetBlob                                | ❌         | ❌    |
| GetBranch                              | ✅         | ✅    |
| GetComment                             | ❌         | ❌    |
| GetCommentReactions                    | ❌         | ❌    |
| GetCommentsForComparedCommit           | ❌         | ❌    |
| GetCommentsForPullRequest              | ❌         | ❌    |
| GetCommit                              | ❌         | ❌    |
| GetDifferences                         | ❌         | ❌    |
| GetFile                                | ✅         | ✅    |
| GetFolder                              | ✅         | ✅    |
| GetMergeCommit                         | ❌         | ❌    |
| GetMergeConflicts                      | ❌         | ❌    |
| GetMergeOptions                        | ❌         | ❌    |
| GetPullRequest                         | ❌         | ❌    |
| GetPullRequestApprovalStates           | ❌         | ❌    |
| GetPullRequestOverrideState            | ❌         | ❌    |
| GetRepository                          | ✅         | ✅    |
| GetRepositoryTriggers                  | ❌         | ❌    |
| ListApprovalRuleTemplates              | ❌         | ❌    |
| ListAssociatedApprovalRuleTemplatesForRepository| ❌         | ❌    |
| ListBranches                           | ❌         | ❌    |
| ListPullRequests                       | ✅         | ✅    |
| ListRepositories                       | ✅         | ❌    |
| ListRepositoriesForApprovalRuleTemplate| ❌         | ❌    |
| ListTagsForResource                    | ✅         | ❌    |
| MergeBranchesByFastForward             | ❌         | ❌    |
| MergeBranchesBySquash                  | ❌         | ❌    |
| MergeBranchesByThreeWay                | ❌         | ❌    |
| MergePullRequestByFastForward          | ❌         | ❌    |
| MergePullRequestBySquash               | ❌         | ❌    |
| MergePullRequestByThreeWay             | ❌         | ❌    |
| OverridePullRequestApprovalRules       | ❌         | ❌    |
| PostCommentForComparedCommit           | ❌         | ❌    |
| PostCommentForPullRequest              | ❌         | ❌    |
| PostCommentReply                       | ❌         | ❌    |
| PutCommentReaction                     | ❌         | ❌    |
| PutFile                                | ❌         | ❌    |
| PutRepositoryTriggers                  | ❌         | ❌    |
| TagResource                            | ✅         | ❌    |
| TestRepositoryTriggers                 | ❌         | ❌    |
| UntagResource                          | ❌         | ❌    |
| UpdateApprovalRuleTemplateContent      | ❌         | ❌    |
| UpdateApprovalRuleTemplateDescription  | ❌         | ❌    |
| UpdateApprovalRuleTemplateName         | ❌         | ❌    |
| UpdateComment                          | ❌         | ❌    |
| UpdateDefaultBranch                    | ❌         | ❌    |
| UpdatePullRequestApprovalRuleContent   | ❌         | ❌    |
| UpdatePullRequestApprovalState         | ❌         | ❌    |
| UpdatePullRequestDescription           | ❌         | ❌    |
| UpdatePullRequestStatus                | ❌         | ❌    |
| UpdatePullRequestTitle                 | ❌         | ❌    |
| UpdateRepositoryDescription            | ❌         | ❌    |
| UpdateRepositoryName                   | ❌         | ❌    |



## cognito-identity ##

API returns a response for 52.2% of the operations.

| Operation                              | Implemented | Tested |
|----------------------------------------|-------------|--------|
| CreateIdentityPool                     | ✅         | ✅    |
| DeleteIdentities                       | ❌         | ❌    |
| DeleteIdentityPool                     | ✅         | ✅    |
| DescribeIdentity                       | ❌         | ❌    |
| DescribeIdentityPool                   | ✅         | ❌    |
| GetCredentialsForIdentity              | ✅         | ✅    |
| GetId                                  | ✅         | ✅    |
| GetIdentityPoolRoles                   | ✅         | ✅    |
| GetOpenIdToken                         | ✅         | ❌    |
| GetOpenIdTokenForDeveloperIdentity     | ✅         | ❌    |
| GetPrincipalTagAttributeMap            | ❌         | ❌    |
| ListIdentities                         | ✅         | ❌    |
| ListIdentityPools                      | ✅         | ✅    |
| ListTagsForResource                    | ❌         | ❌    |
| LookupDeveloperIdentity                | ❌         | ❌    |
| MergeDeveloperIdentities               | ❌         | ❌    |
| SetIdentityPoolRoles                   | ✅         | ✅    |
| SetPrincipalTagAttributeMap            | ❌         | ❌    |
| TagResource                            | ❌         | ❌    |
| UnlinkDeveloperIdentity                | ❌         | ❌    |
| UnlinkIdentity                         | ❌         | ❌    |
| UntagResource                          | ❌         | ❌    |
| UpdateIdentityPool                     | ✅         | ❌    |



## cognito-idp ##

API returns a response for 63.4% of the operations.

| Operation                              | Implemented | Tested |
|----------------------------------------|-------------|--------|
| AddCustomAttributes                    | ✅         | ❌    |
| AdminAddUserToGroup                    | ✅         | ✅    |
| AdminConfirmSignUp                     | ✅         | ✅    |
| AdminCreateUser                        | ✅         | ✅    |
| AdminDeleteUser                        | ✅         | ✅    |
| AdminDeleteUserAttributes              | ✅         | ✅    |
| AdminDisableProviderForUser            | ❌         | ❌    |
| AdminDisableUser                       | ✅         | ✅    |
| AdminEnableUser                        | ✅         | ❌    |
| AdminForgetDevice                      | ❌         | ❌    |
| AdminGetDevice                         | ❌         | ❌    |
| AdminGetUser                           | ✅         | ✅    |
| AdminInitiateAuth                      | ✅         | ✅    |
| AdminLinkProviderForUser               | ❌         | ❌    |
| AdminListDevices                       | ❌         | ❌    |
| AdminListGroupsForUser                 | ✅         | ✅    |
| AdminListUserAuthEvents                | ❌         | ❌    |
| AdminRemoveUserFromGroup               | ✅         | ❌    |
| AdminResetUserPassword                 | ✅         | ❌    |
| AdminRespondToAuthChallenge            | ✅         | ✅    |
| AdminSetUserMFAPreference              | ✅         | ✅    |
| AdminSetUserPassword                   | ✅         | ✅    |
| AdminSetUserSettings                   | ❌         | ❌    |
| AdminUpdateAuthEventFeedback           | ❌         | ❌    |
| AdminUpdateDeviceStatus                | ❌         | ❌    |
| AdminUpdateUserAttributes              | ✅         | ✅    |
| AdminUserGlobalSignOut                 | ✅         | ✅    |
| AssociateSoftwareToken                 | ❌         | ❌    |
| ChangePassword                         | ✅         | ✅    |
| ConfirmDevice                          | ✅         | ❌    |
| ConfirmForgotPassword                  | ✅         | ✅    |
| ConfirmSignUp                          | ✅         | ❌    |
| CreateGroup                            | ✅         | ✅    |
| CreateIdentityProvider                 | ✅         | ✅    |
| CreateResourceServer                   | ✅         | ✅    |
| CreateUserImportJob                    | ❌         | ❌    |
| CreateUserPool                         | ✅         | ✅    |
| CreateUserPoolClient                   | ✅         | ✅    |
| CreateUserPoolDomain                   | ✅         | ❌    |
| DeleteGroup                            | ✅         | ✅    |
| DeleteIdentityProvider                 | ✅         | ✅    |
| DeleteResourceServer                   | ✅         | ✅    |
| DeleteUser                             | ❌         | ❌    |
| DeleteUserAttributes                   | ✅         | ✅    |
| DeleteUserPool                         | ✅         | ✅    |
| DeleteUserPoolClient                   | ✅         | ✅    |
| DeleteUserPoolDomain                   | ✅         | ❌    |
| DescribeIdentityProvider               | ✅         | ✅    |
| DescribeResourceServer                 | ✅         | ✅    |
| DescribeRiskConfiguration              | ❌         | ❌    |
| DescribeUserImportJob                  | ❌         | ❌    |
| DescribeUserPool                       | ✅         | ✅    |
| DescribeUserPoolClient                 | ✅         | ✅    |
| DescribeUserPoolDomain                 | ✅         | ❌    |
| ForgetDevice                           | ❌         | ❌    |
| ForgotPassword                         | ✅         | ✅    |
| GetCSVHeader                           | ❌         | ❌    |
| GetDevice                              | ❌         | ❌    |
| GetGroup                               | ✅         | ❌    |
| GetIdentityProviderByIdentifier        | ❌         | ❌    |
| GetSigningCertificate                  | ✅         | ✅    |
| GetUICustomization                     | ❌         | ❌    |
| GetUser                                | ✅         | ✅    |
| GetUserAttributeVerificationCode       | ❌         | ❌    |
| GetUserPoolMfaConfig                   | ✅         | ✅    |
| GlobalSignOut                          | ✅         | ✅    |
| InitiateAuth                           | ✅         | ✅    |
| ListDevices                            | ❌         | ❌    |
| ListGroups                             | ✅         | ✅    |
| ListIdentityProviders                  | ✅         | ✅    |
| ListResourceServers                    | ✅         | ✅    |
| ListTagsForResource                    | ❌         | ❌    |
| ListUserImportJobs                     | ❌         | ❌    |
| ListUserPoolClients                    | ✅         | ✅    |
| ListUserPools                          | ✅         | ✅    |
| ListUsers                              | ✅         | ✅    |
| ListUsersInGroup                       | ✅         | ✅    |
| ResendConfirmationCode                 | ❌         | ❌    |
| RespondToAuthChallenge                 | ✅         | ✅    |
| RevokeToken                            | ❌         | ❌    |
| SetRiskConfiguration                   | ❌         | ❌    |
| SetUICustomization                     | ❌         | ❌    |
| SetUserMFAPreference                   | ✅         | ✅    |
| SetUserPoolMfaConfig                   | ✅         | ✅    |
| SetUserSettings                        | ❌         | ❌    |
| SignUp                                 | ✅         | ✅    |
| StartUserImportJob                     | ❌         | ❌    |
| StopUserImportJob                      | ❌         | ❌    |
| TagResource                            | ❌         | ❌    |
| UntagResource                          | ❌         | ❌    |
| UpdateAuthEventFeedback                | ❌         | ❌    |
| UpdateDeviceStatus                     | ❌         | ❌    |
| UpdateGroup                            | ✅         | ❌    |
| UpdateIdentityProvider                 | ✅         | ✅    |
| UpdateResourceServer                   | ✅         | ❌    |
| UpdateUserAttributes                   | ✅         | ❌    |
| UpdateUserPool                         | ✅         | ✅    |
| UpdateUserPoolClient                   | ✅         | ❌    |
| UpdateUserPoolDomain                   | ❌         | ❌    |
| VerifySoftwareToken                    | ❌         | ❌    |
| VerifyUserAttribute                    | ❌         | ❌    |



## config ##

API returns a response for 36.4% of the operations.

| Operation                              | Implemented | Tested |
|----------------------------------------|-------------|--------|
| BatchGetAggregateResourceConfig        | ✅         | ❌    |
| BatchGetResourceConfig                 | ✅         | ❌    |
| DeleteAggregationAuthorization         | ✅         | ❌    |
| DeleteConfigRule                       | ✅         | ❌    |
| DeleteConfigurationAggregator          | ✅         | ❌    |
| DeleteConfigurationRecorder            | ✅         | ✅    |
| DeleteConformancePack                  | ❌         | ❌    |
| DeleteDeliveryChannel                  | ✅         | ✅    |
| DeleteEvaluationResults                | ❌         | ❌    |
| DeleteOrganizationConfigRule           | ❌         | ❌    |
| DeleteOrganizationConformancePack      | ✅         | ❌    |
| DeletePendingAggregationRequest        | ❌         | ❌    |
| DeleteRemediationConfiguration         | ❌         | ❌    |
| DeleteRemediationExceptions            | ❌         | ❌    |
| DeleteResourceConfig                   | ❌         | ❌    |
| DeleteRetentionConfiguration           | ❌         | ❌    |
| DeleteStoredQuery                      | ❌         | ❌    |
| DeliverConfigSnapshot                  | ❌         | ❌    |
| DescribeAggregateComplianceByConfigRules| ❌         | ❌    |
| DescribeAggregateComplianceByConformancePacks| ❌         | ❌    |
| DescribeAggregationAuthorizations      | ✅         | ❌    |
| DescribeComplianceByConfigRule         | ❌         | ❌    |
| DescribeComplianceByResource           | ❌         | ❌    |
| DescribeConfigRuleEvaluationStatus     | ❌         | ❌    |
| DescribeConfigRules                    | ✅         | ❌    |
| DescribeConfigurationAggregatorSourcesStatus| ❌         | ❌    |
| DescribeConfigurationAggregators       | ✅         | ❌    |
| DescribeConfigurationRecorderStatus    | ✅         | ❌    |
| DescribeConfigurationRecorders         | ✅         | ✅    |
| DescribeConformancePackCompliance      | ❌         | ❌    |
| DescribeConformancePackStatus          | ❌         | ❌    |
| DescribeConformancePacks               | ❌         | ❌    |
| DescribeDeliveryChannelStatus          | ❌         | ❌    |
| DescribeDeliveryChannels               | ✅         | ✅    |
| DescribeOrganizationConfigRuleStatuses | ❌         | ❌    |
| DescribeOrganizationConfigRules        | ❌         | ❌    |
| DescribeOrganizationConformancePackStatuses| ✅         | ❌    |
| DescribeOrganizationConformancePacks   | ✅         | ❌    |
| DescribePendingAggregationRequests     | ❌         | ❌    |
| DescribeRemediationConfigurations      | ❌         | ❌    |
| DescribeRemediationExceptions          | ❌         | ❌    |
| DescribeRemediationExecutionStatus     | ❌         | ❌    |
| DescribeRetentionConfigurations        | ❌         | ❌    |
| GetAggregateComplianceDetailsByConfigRule| ❌         | ❌    |
| GetAggregateConfigRuleComplianceSummary| ❌         | ❌    |
| GetAggregateConformancePackComplianceSummary| ❌         | ❌    |
| GetAggregateDiscoveredResourceCounts   | ❌         | ❌    |
| GetAggregateResourceConfig             | ❌         | ❌    |
| GetComplianceDetailsByConfigRule       | ❌         | ❌    |
| GetComplianceDetailsByResource         | ❌         | ❌    |
| GetComplianceSummaryByConfigRule       | ❌         | ❌    |
| GetComplianceSummaryByResourceType     | ❌         | ❌    |
| GetConformancePackComplianceDetails    | ❌         | ❌    |
| GetConformancePackComplianceSummary    | ❌         | ❌    |
| GetCustomRulePolicy                    | ❌         | ❌    |
| GetDiscoveredResourceCounts            | ❌         | ❌    |
| GetOrganizationConfigRuleDetailedStatus| ❌         | ❌    |
| GetOrganizationConformancePackDetailedStatus| ✅         | ❌    |
| GetOrganizationCustomRulePolicy        | ❌         | ❌    |
| GetResourceConfigHistory               | ✅         | ❌    |
| GetStoredQuery                         | ❌         | ❌    |
| ListAggregateDiscoveredResources       | ✅         | ❌    |
| ListDiscoveredResources                | ✅         | ❌    |
| ListStoredQueries                      | ❌         | ❌    |
| ListTagsForResource                    | ✅         | ❌    |
| PutAggregationAuthorization            | ✅         | ❌    |
| PutConfigRule                          | ✅         | ❌    |
| PutConfigurationAggregator             | ✅         | ❌    |
| PutConfigurationRecorder               | ✅         | ✅    |
| PutConformancePack                     | ❌         | ❌    |
| PutDeliveryChannel                     | ✅         | ✅    |
| PutEvaluations                         | ✅         | ❌    |
| PutExternalEvaluation                  | ❌         | ❌    |
| PutOrganizationConfigRule              | ❌         | ❌    |
| PutOrganizationConformancePack         | ✅         | ❌    |
| PutRemediationConfigurations           | ❌         | ❌    |
| PutRemediationExceptions               | ❌         | ❌    |
| PutResourceConfig                      | ❌         | ❌    |
| PutRetentionConfiguration              | ❌         | ❌    |
| PutStoredQuery                         | ❌         | ❌    |
| SelectAggregateResourceConfig          | ❌         | ❌    |
| SelectResourceConfig                   | ❌         | ❌    |
| StartConfigRulesEvaluation             | ❌         | ❌    |
| StartConfigurationRecorder             | ✅         | ❌    |
| StartRemediationExecution              | ❌         | ❌    |
| StopConfigurationRecorder              | ✅         | ❌    |
| TagResource                            | ✅         | ❌    |
| UntagResource                          | ✅         | ❌    |



## docdb ##

API returns a response for 66.0% of the operations.

| Operation                              | Implemented | Tested |
|----------------------------------------|-------------|--------|
| AddSourceIdentifierToSubscription      | ❌         | ❌    |
| AddTagsToResource                      | ✅         | ❌    |
| ApplyPendingMaintenanceAction          | ❌         | ❌    |
| CopyDBClusterParameterGroup            | ❌         | ❌    |
| CopyDBClusterSnapshot                  | ✅         | ❌    |
| CreateDBCluster                        | ✅         | ❌    |
| CreateDBClusterParameterGroup          | ✅         | ❌    |
| CreateDBClusterSnapshot                | ✅         | ❌    |
| CreateDBInstance                       | ✅         | ❌    |
| CreateDBSubnetGroup                    | ✅         | ❌    |
| CreateEventSubscription                | ✅         | ❌    |
| CreateGlobalCluster                    | ❌         | ❌    |
| DeleteDBCluster                        | ✅         | ❌    |
| DeleteDBClusterParameterGroup          | ✅         | ❌    |
| DeleteDBClusterSnapshot                | ✅         | ❌    |
| DeleteDBInstance                       | ✅         | ❌    |
| DeleteDBSubnetGroup                    | ✅         | ❌    |
| DeleteEventSubscription                | ✅         | ❌    |
| DeleteGlobalCluster                    | ❌         | ❌    |
| DescribeCertificates                   | ✅         | ❌    |
| DescribeDBClusterParameterGroups       | ✅         | ❌    |
| DescribeDBClusterParameters            | ✅         | ❌    |
| DescribeDBClusterSnapshotAttributes    | ❌         | ❌    |
| DescribeDBClusterSnapshots             | ✅         | ❌    |
| DescribeDBClusters                     | ✅         | ❌    |
| DescribeDBEngineVersions               | ✅         | ❌    |
| DescribeDBInstances                    | ✅         | ❌    |
| DescribeDBSubnetGroups                 | ✅         | ❌    |
| DescribeEngineDefaultClusterParameters | ❌         | ❌    |
| DescribeEventCategories                | ❌         | ❌    |
| DescribeEventSubscriptions             | ✅         | ❌    |
| DescribeEvents                         | ❌         | ❌    |
| DescribeGlobalClusters                 | ✅         | ❌    |
| DescribeOrderableDBInstanceOptions     | ❌         | ❌    |
| DescribePendingMaintenanceActions      | ❌         | ❌    |
| FailoverDBCluster                      | ❌         | ❌    |
| ListTagsForResource                    | ✅         | ❌    |
| ModifyDBCluster                        | ✅         | ❌    |
| ModifyDBClusterParameterGroup          | ✅         | ❌    |
| ModifyDBClusterSnapshotAttribute       | ❌         | ❌    |
| ModifyDBInstance                       | ✅         | ❌    |
| ModifyDBSubnetGroup                    | ✅         | ❌    |
| ModifyEventSubscription                | ❌         | ❌    |
| ModifyGlobalCluster                    | ❌         | ❌    |
| RebootDBInstance                       | ✅         | ❌    |
| RemoveFromGlobalCluster                | ❌         | ❌    |
| RemoveSourceIdentifierFromSubscription | ❌         | ❌    |
| RemoveTagsFromResource                 | ✅         | ❌    |
| ResetDBClusterParameterGroup           | ✅         | ❌    |
| RestoreDBClusterFromSnapshot           | ✅         | ❌    |
| RestoreDBClusterToPointInTime          | ❌         | ❌    |
| StartDBCluster                         | ✅         | ❌    |
| StopDBCluster                          | ✅         | ❌    |



## dynamodb ##

API returns a response for 70.0% of the operations.

| Operation                              | Implemented | Tested |
|----------------------------------------|-------------|--------|
| BatchExecuteStatement                  | ✅         | ✅    |
| BatchGetItem                           | ✅         | ✅    |
| BatchWriteItem                         | ✅         | ✅    |
| CreateBackup                           | ✅         | ✅    |
| CreateGlobalTable                      | ✅         | ✅    |
| CreateTable                            | ✅         | ✅    |
| DeleteBackup                           | ✅         | ✅    |
| DeleteItem                             | ✅         | ✅    |
| DeleteTable                            | ✅         | ✅    |
| DescribeBackup                         | ❌         | ❌    |
| DescribeContinuousBackups              | ❌         | ✅    |
| DescribeContributorInsights            | ❌         | ❌    |
| DescribeEndpoints                      | ❌         | ❌    |
| DescribeExport                         | ❌         | ❌    |
| DescribeGlobalTable                    | ✅         | ✅    |
| DescribeGlobalTableSettings            | ❌         | ❌    |
| DescribeKinesisStreamingDestination    | ✅         | ✅    |
| DescribeLimits                         | ✅         | ❌    |
| DescribeTable                          | ✅         | ✅    |
| DescribeTableReplicaAutoScaling        | ❌         | ❌    |
| DescribeTimeToLive                     | ✅         | ✅    |
| DisableKinesisStreamingDestination     | ✅         | ✅    |
| EnableKinesisStreamingDestination      | ✅         | ✅    |
| ExecuteStatement                       | ✅         | ✅    |
| ExecuteTransaction                     | ✅         | ✅    |
| ExportTableToPointInTime               | ❌         | ❌    |
| GetItem                                | ✅         | ✅    |
| ListBackups                            | ✅         | ❌    |
| ListContributorInsights                | ❌         | ❌    |
| ListExports                            | ❌         | ❌    |
| ListGlobalTables                       | ✅         | ❌    |
| ListTables                             | ✅         | ✅    |
| ListTagsOfResource                     | ✅         | ✅    |
| PutItem                                | ✅         | ✅    |
| Query                                  | ✅         | ✅    |
| RestoreTableFromBackup                 | ✅         | ✅    |
| RestoreTableToPointInTime              | ❌         | ❌    |
| Scan                                   | ✅         | ✅    |
| TagResource                            | ✅         | ✅    |
| TransactGetItems                       | ✅         | ✅    |
| TransactWriteItems                     | ✅         | ✅    |
| UntagResource                          | ✅         | ✅    |
| UpdateContinuousBackups                | ❌         | ❌    |
| UpdateContributorInsights              | ❌         | ❌    |
| UpdateGlobalTable                      | ✅         | ✅    |
| UpdateGlobalTableSettings              | ❌         | ❌    |
| UpdateItem                             | ✅         | ✅    |
| UpdateTable                            | ✅         | ✅    |
| UpdateTableReplicaAutoScaling          | ❌         | ❌    |
| UpdateTimeToLive                       | ✅         | ✅    |



## dynamodbstreams ##

API returns a response for 100.0% of the operations.

| Operation                              | Implemented | Tested |
|----------------------------------------|-------------|--------|
| DescribeStream                         | ✅         | ✅    |
| GetRecords                             | ✅         | ✅    |
| GetShardIterator                       | ✅         | ✅    |
| ListStreams                            | ✅         | ✅    |



## ec2 ##

API returns a response for 42.1% of the operations.

| Operation                              | Implemented | Tested |
|----------------------------------------|-------------|--------|
| AcceptReservedInstancesExchangeQuote   | ❌         | ❌    |
| AcceptTransitGatewayMulticastDomainAssociations| ❌         | ❌    |
| AcceptTransitGatewayPeeringAttachment  | ✅         | ❌    |
| AcceptTransitGatewayVpcAttachment      | ❌         | ❌    |
| AcceptVpcEndpointConnections           | ❌         | ❌    |
| AcceptVpcPeeringConnection             | ✅         | ✅    |
| AdvertiseByoipCidr                     | ❌         | ❌    |
| AllocateAddress                        | ✅         | ✅    |
| AllocateHosts                          | ❌         | ❌    |
| AllocateIpamPoolCidr                   | ❌         | ❌    |
| ApplySecurityGroupsToClientVpnTargetNetwork| ❌         | ❌    |
| AssignIpv6Addresses                    | ✅         | ❌    |
| AssignPrivateIpAddresses               | ✅         | ❌    |
| AssociateAddress                       | ✅         | ❌    |
| AssociateClientVpnTargetNetwork        | ❌         | ❌    |
| AssociateDhcpOptions                   | ✅         | ❌    |
| AssociateEnclaveCertificateIamRole     | ❌         | ❌    |
| AssociateIamInstanceProfile            | ✅         | ❌    |
| AssociateInstanceEventWindow           | ❌         | ❌    |
| AssociateRouteTable                    | ✅         | ✅    |
| AssociateSubnetCidrBlock               | ✅         | ❌    |
| AssociateTransitGatewayMulticastDomain | ❌         | ❌    |
| AssociateTransitGatewayRouteTable      | ✅         | ❌    |
| AssociateTrunkInterface                | ❌         | ❌    |
| AssociateVpcCidrBlock                  | ✅         | ❌    |
| AttachClassicLinkVpc                   | ❌         | ❌    |
| AttachInternetGateway                  | ✅         | ✅    |
| AttachNetworkInterface                 | ✅         | ❌    |
| AttachVolume                           | ✅         | ❌    |
| AttachVpnGateway                       | ✅         | ✅    |
| AuthorizeClientVpnIngress              | ❌         | ❌    |
| AuthorizeSecurityGroupEgress           | ✅         | ✅    |
| AuthorizeSecurityGroupIngress          | ✅         | ✅    |
| BundleInstance                         | ❌         | ❌    |
| CancelBundleTask                       | ❌         | ❌    |
| CancelCapacityReservation              | ❌         | ❌    |
| CancelCapacityReservationFleets        | ❌         | ❌    |
| CancelConversionTask                   | ❌         | ❌    |
| CancelExportTask                       | ❌         | ❌    |
| CancelImportTask                       | ❌         | ❌    |
| CancelReservedInstancesListing         | ❌         | ❌    |
| CancelSpotFleetRequests                | ✅         | ❌    |
| CancelSpotInstanceRequests             | ✅         | ❌    |
| ConfirmProductInstance                 | ❌         | ❌    |
| CopyFpgaImage                          | ❌         | ❌    |
| CopyImage                              | ✅         | ❌    |
| CopySnapshot                           | ✅         | ❌    |
| CreateCapacityReservation              | ❌         | ❌    |
| CreateCapacityReservationFleet         | ❌         | ❌    |
| CreateCarrierGateway                   | ✅         | ❌    |
| CreateClientVpnEndpoint                | ❌         | ❌    |
| CreateClientVpnRoute                   | ❌         | ❌    |
| CreateCustomerGateway                  | ✅         | ❌    |
| CreateDefaultSubnet                    | ❌         | ❌    |
| CreateDefaultVpc                       | ❌         | ❌    |
| CreateDhcpOptions                      | ✅         | ❌    |
| CreateEgressOnlyInternetGateway        | ✅         | ❌    |
| CreateFleet                            | ❌         | ❌    |
| CreateFlowLogs                         | ✅         | ❌    |
| CreateFpgaImage                        | ❌         | ❌    |
| CreateImage                            | ✅         | ✅    |
| CreateInstanceEventWindow              | ❌         | ❌    |
| CreateInstanceExportTask               | ❌         | ❌    |
| CreateInternetGateway                  | ✅         | ✅    |
| CreateIpam                             | ❌         | ❌    |
| CreateIpamPool                         | ❌         | ❌    |
| CreateIpamScope                        | ❌         | ❌    |
| CreateKeyPair                          | ✅         | ✅    |
| CreateLaunchTemplate                   | ✅         | ❌    |
| CreateLaunchTemplateVersion            | ✅         | ❌    |
| CreateLocalGatewayRoute                | ❌         | ❌    |
| CreateLocalGatewayRouteTableVpcAssociation| ❌         | ❌    |
| CreateManagedPrefixList                | ✅         | ❌    |
| CreateNatGateway                       | ✅         | ✅    |
| CreateNetworkAcl                       | ✅         | ❌    |
| CreateNetworkAclEntry                  | ✅         | ❌    |
| CreateNetworkInsightsAccessScope       | ❌         | ❌    |
| CreateNetworkInsightsPath              | ❌         | ❌    |
| CreateNetworkInterface                 | ✅         | ❌    |
| CreateNetworkInterfacePermission       | ❌         | ❌    |
| CreatePlacementGroup                   | ✅         | ❌    |
| CreatePublicIpv4Pool                   | ❌         | ❌    |
| CreateReplaceRootVolumeTask            | ❌         | ❌    |
| CreateReservedInstancesListing         | ❌         | ❌    |
| CreateRestoreImageTask                 | ❌         | ❌    |
| CreateRoute                            | ✅         | ✅    |
| CreateRouteTable                       | ✅         | ✅    |
| CreateSecurityGroup                    | ✅         | ✅    |
| CreateSnapshot                         | ✅         | ❌    |
| CreateSnapshots                        | ✅         | ❌    |
| CreateSpotDatafeedSubscription         | ✅         | ❌    |
| CreateStoreImageTask                   | ❌         | ❌    |
| CreateSubnet                           | ✅         | ✅    |
| CreateSubnetCidrReservation            | ❌         | ❌    |
| CreateTags                             | ✅         | ✅    |
| CreateTrafficMirrorFilter              | ❌         | ❌    |
| CreateTrafficMirrorFilterRule          | ❌         | ❌    |
| CreateTrafficMirrorSession             | ❌         | ❌    |
| CreateTrafficMirrorTarget              | ❌         | ❌    |
| CreateTransitGateway                   | ✅         | ❌    |
| CreateTransitGatewayConnect            | ❌         | ❌    |
| CreateTransitGatewayConnectPeer        | ❌         | ❌    |
| CreateTransitGatewayMulticastDomain    | ❌         | ❌    |
| CreateTransitGatewayPeeringAttachment  | ✅         | ❌    |
| CreateTransitGatewayPrefixListReference| ❌         | ❌    |
| CreateTransitGatewayRoute              | ✅         | ❌    |
| CreateTransitGatewayRouteTable         | ✅         | ❌    |
| CreateTransitGatewayVpcAttachment      | ✅         | ❌    |
| CreateVolume                           | ✅         | ❌    |
| CreateVpc                              | ✅         | ✅    |
| CreateVpcEndpoint                      | ✅         | ✅    |
| CreateVpcEndpointConnectionNotification| ❌         | ❌    |
| CreateVpcEndpointServiceConfiguration  | ✅         | ❌    |
| CreateVpcPeeringConnection             | ✅         | ✅    |
| CreateVpnConnection                    | ✅         | ❌    |
| CreateVpnConnectionRoute               | ❌         | ❌    |
| CreateVpnGateway                       | ✅         | ✅    |
| DeleteCarrierGateway                   | ✅         | ❌    |
| DeleteClientVpnEndpoint                | ❌         | ❌    |
| DeleteClientVpnRoute                   | ❌         | ❌    |
| DeleteCustomerGateway                  | ✅         | ❌    |
| DeleteDhcpOptions                      | ✅         | ❌    |
| DeleteEgressOnlyInternetGateway        | ✅         | ❌    |
| DeleteFleets                           | ❌         | ❌    |
| DeleteFlowLogs                         | ✅         | ❌    |
| DeleteFpgaImage                        | ❌         | ❌    |
| DeleteInstanceEventWindow              | ❌         | ❌    |
| DeleteInternetGateway                  | ✅         | ❌    |
| DeleteIpam                             | ❌         | ❌    |
| DeleteIpamPool                         | ❌         | ❌    |
| DeleteIpamScope                        | ❌         | ❌    |
| DeleteKeyPair                          | ✅         | ❌    |
| DeleteLaunchTemplate                   | ✅         | ❌    |
| DeleteLaunchTemplateVersions           | ❌         | ❌    |
| DeleteLocalGatewayRoute                | ❌         | ❌    |
| DeleteLocalGatewayRouteTableVpcAssociation| ❌         | ❌    |
| DeleteManagedPrefixList                | ✅         | ❌    |
| DeleteNatGateway                       | ✅         | ✅    |
| DeleteNetworkAcl                       | ✅         | ❌    |
| DeleteNetworkAclEntry                  | ✅         | ❌    |
| DeleteNetworkInsightsAccessScope       | ❌         | ❌    |
| DeleteNetworkInsightsAccessScopeAnalysis| ❌         | ❌    |
| DeleteNetworkInsightsAnalysis          | ❌         | ❌    |
| DeleteNetworkInsightsPath              | ❌         | ❌    |
| DeleteNetworkInterface                 | ✅         | ❌    |
| DeleteNetworkInterfacePermission       | ❌         | ❌    |
| DeletePlacementGroup                   | ✅         | ❌    |
| DeletePublicIpv4Pool                   | ❌         | ❌    |
| DeleteQueuedReservedInstances          | ❌         | ❌    |
| DeleteRoute                            | ✅         | ✅    |
| DeleteRouteTable                       | ✅         | ✅    |
| DeleteSecurityGroup                    | ✅         | ✅    |
| DeleteSnapshot                         | ✅         | ❌    |
| DeleteSpotDatafeedSubscription         | ✅         | ❌    |
| DeleteSubnet                           | ✅         | ✅    |
| DeleteSubnetCidrReservation            | ❌         | ❌    |
| DeleteTags                             | ✅         | ❌    |
| DeleteTrafficMirrorFilter              | ❌         | ❌    |
| DeleteTrafficMirrorFilterRule          | ❌         | ❌    |
| DeleteTrafficMirrorSession             | ❌         | ❌    |
| DeleteTrafficMirrorTarget              | ❌         | ❌    |
| DeleteTransitGateway                   | ✅         | ❌    |
| DeleteTransitGatewayConnect            | ❌         | ❌    |
| DeleteTransitGatewayConnectPeer        | ❌         | ❌    |
| DeleteTransitGatewayMulticastDomain    | ❌         | ❌    |
| DeleteTransitGatewayPeeringAttachment  | ✅         | ❌    |
| DeleteTransitGatewayPrefixListReference| ❌         | ❌    |
| DeleteTransitGatewayRoute              | ✅         | ❌    |
| DeleteTransitGatewayRouteTable         | ✅         | ❌    |
| DeleteTransitGatewayVpcAttachment      | ✅         | ❌    |
| DeleteVolume                           | ✅         | ❌    |
| DeleteVpc                              | ✅         | ✅    |
| DeleteVpcEndpointConnectionNotifications| ❌         | ❌    |
| DeleteVpcEndpointServiceConfigurations | ✅         | ❌    |
| DeleteVpcEndpoints                     | ✅         | ✅    |
| DeleteVpcPeeringConnection             | ✅         | ✅    |
| DeleteVpnConnection                    | ✅         | ❌    |
| DeleteVpnConnectionRoute               | ❌         | ❌    |
| DeleteVpnGateway                       | ✅         | ✅    |
| DeprovisionByoipCidr                   | ❌         | ❌    |
| DeprovisionIpamPoolCidr                | ❌         | ❌    |
| DeprovisionPublicIpv4PoolCidr          | ❌         | ❌    |
| DeregisterImage                        | ✅         | ❌    |
| DeregisterInstanceEventNotificationAttributes| ❌         | ❌    |
| DeregisterTransitGatewayMulticastGroupMembers| ❌         | ❌    |
| DeregisterTransitGatewayMulticastGroupSources| ❌         | ❌    |
| DescribeAccountAttributes              | ✅         | ✅    |
| DescribeAddresses                      | ✅         | ❌    |
| DescribeAddressesAttribute             | ❌         | ❌    |
| DescribeAggregateIdFormat              | ❌         | ❌    |
| DescribeAvailabilityZones              | ✅         | ❌    |
| DescribeBundleTasks                    | ❌         | ❌    |
| DescribeByoipCidrs                     | ❌         | ❌    |
| DescribeCapacityReservationFleets      | ❌         | ❌    |
| DescribeCapacityReservations           | ❌         | ❌    |
| DescribeCarrierGateways                | ✅         | ❌    |
| DescribeClassicLinkInstances           | ❌         | ❌    |
| DescribeClientVpnAuthorizationRules    | ❌         | ❌    |
| DescribeClientVpnConnections           | ❌         | ❌    |
| DescribeClientVpnEndpoints             | ❌         | ❌    |
| DescribeClientVpnRoutes                | ❌         | ❌    |
| DescribeClientVpnTargetNetworks        | ❌         | ❌    |
| DescribeCoipPools                      | ❌         | ❌    |
| DescribeConversionTasks                | ❌         | ❌    |
| DescribeCustomerGateways               | ✅         | ❌    |
| DescribeDhcpOptions                    | ✅         | ❌    |
| DescribeEgressOnlyInternetGateways     | ✅         | ❌    |
| DescribeElasticGpus                    | ❌         | ❌    |
| DescribeExportImageTasks               | ❌         | ❌    |
| DescribeExportTasks                    | ❌         | ❌    |
| DescribeFastLaunchImages               | ❌         | ❌    |
| DescribeFastSnapshotRestores           | ❌         | ❌    |
| DescribeFleetHistory                   | ❌         | ❌    |
| DescribeFleetInstances                 | ❌         | ❌    |
| DescribeFleets                         | ❌         | ❌    |
| DescribeFlowLogs                       | ✅         | ❌    |
| DescribeFpgaImageAttribute             | ❌         | ❌    |
| DescribeFpgaImages                     | ❌         | ❌    |
| DescribeHostReservationOfferings       | ❌         | ❌    |
| DescribeHostReservations               | ❌         | ❌    |
| DescribeHosts                          | ❌         | ❌    |
| DescribeIamInstanceProfileAssociations | ✅         | ❌    |
| DescribeIdFormat                       | ❌         | ❌    |
| DescribeIdentityIdFormat               | ❌         | ❌    |
| DescribeImageAttribute                 | ✅         | ❌    |
| DescribeImages                         | ✅         | ✅    |
| DescribeImportImageTasks               | ❌         | ❌    |
| DescribeImportSnapshotTasks            | ❌         | ❌    |
| DescribeInstanceAttribute              | ✅         | ❌    |
| DescribeInstanceCreditSpecifications   | ✅         | ❌    |
| DescribeInstanceEventNotificationAttributes| ❌         | ❌    |
| DescribeInstanceEventWindows           | ❌         | ❌    |
| DescribeInstanceStatus                 | ✅         | ❌    |
| DescribeInstanceTypeOfferings          | ✅         | ❌    |
| DescribeInstanceTypes                  | ✅         | ❌    |
| DescribeInstances                      | ✅         | ✅    |
| DescribeInternetGateways               | ✅         | ✅    |
| DescribeIpamPools                      | ❌         | ❌    |
| DescribeIpamScopes                     | ❌         | ❌    |
| DescribeIpams                          | ❌         | ❌    |
| DescribeIpv6Pools                      | ❌         | ❌    |
| DescribeKeyPairs                       | ✅         | ❌    |
| DescribeLaunchTemplateVersions         | ✅         | ❌    |
| DescribeLaunchTemplates                | ✅         | ❌    |
| DescribeLocalGatewayRouteTableVirtualInterfaceGroupAssociations| ❌         | ❌    |
| DescribeLocalGatewayRouteTableVpcAssociations| ❌         | ❌    |
| DescribeLocalGatewayRouteTables        | ❌         | ❌    |
| DescribeLocalGatewayVirtualInterfaceGroups| ❌         | ❌    |
| DescribeLocalGatewayVirtualInterfaces  | ❌         | ❌    |
| DescribeLocalGateways                  | ❌         | ❌    |
| DescribeManagedPrefixLists             | ✅         | ❌    |
| DescribeMovingAddresses                | ❌         | ❌    |
| DescribeNatGateways                    | ✅         | ✅    |
| DescribeNetworkAcls                    | ✅         | ✅    |
| DescribeNetworkInsightsAccessScopeAnalyses| ❌         | ❌    |
| DescribeNetworkInsightsAccessScopes    | ❌         | ❌    |
| DescribeNetworkInsightsAnalyses        | ❌         | ❌    |
| DescribeNetworkInsightsPaths           | ❌         | ❌    |
| DescribeNetworkInterfaceAttribute      | ✅         | ❌    |
| DescribeNetworkInterfacePermissions    | ❌         | ❌    |
| DescribeNetworkInterfaces              | ✅         | ✅    |
| DescribePlacementGroups                | ❌         | ❌    |
| DescribePrefixLists                    | ✅         | ❌    |
| DescribePrincipalIdFormat              | ❌         | ❌    |
| DescribePublicIpv4Pools                | ❌         | ❌    |
| DescribeRegions                        | ✅         | ❌    |
| DescribeReplaceRootVolumeTasks         | ❌         | ❌    |
| DescribeReservedInstances              | ✅         | ✅    |
| DescribeReservedInstancesListings      | ❌         | ❌    |
| DescribeReservedInstancesModifications | ❌         | ❌    |
| DescribeReservedInstancesOfferings     | ✅         | ✅    |
| DescribeRouteTables                    | ✅         | ✅    |
| DescribeScheduledInstanceAvailability  | ❌         | ❌    |
| DescribeScheduledInstances             | ❌         | ❌    |
| DescribeSecurityGroupReferences        | ❌         | ❌    |
| DescribeSecurityGroupRules             | ❌         | ❌    |
| DescribeSecurityGroups                 | ✅         | ✅    |
| DescribeSnapshotAttribute              | ✅         | ❌    |
| DescribeSnapshotTierStatus             | ❌         | ❌    |
| DescribeSnapshots                      | ✅         | ❌    |
| DescribeSpotDatafeedSubscription       | ❌         | ❌    |
| DescribeSpotFleetInstances             | ✅         | ❌    |
| DescribeSpotFleetRequestHistory        | ❌         | ❌    |
| DescribeSpotFleetRequests              | ✅         | ❌    |
| DescribeSpotInstanceRequests           | ✅         | ❌    |
| DescribeSpotPriceHistory               | ✅         | ❌    |
| DescribeStaleSecurityGroups            | ❌         | ❌    |
| DescribeStoreImageTasks                | ❌         | ❌    |
| DescribeSubnets                        | ✅         | ✅    |
| DescribeTags                           | ✅         | ❌    |
| DescribeTrafficMirrorFilters           | ❌         | ❌    |
| DescribeTrafficMirrorSessions          | ❌         | ❌    |
| DescribeTrafficMirrorTargets           | ❌         | ❌    |
| DescribeTransitGatewayAttachments      | ✅         | ❌    |
| DescribeTransitGatewayConnectPeers     | ❌         | ❌    |
| DescribeTransitGatewayConnects         | ❌         | ❌    |
| DescribeTransitGatewayMulticastDomains | ❌         | ❌    |
| DescribeTransitGatewayPeeringAttachments| ✅         | ❌    |
| DescribeTransitGatewayRouteTables      | ✅         | ❌    |
| DescribeTransitGatewayVpcAttachments   | ✅         | ❌    |
| DescribeTransitGateways                | ✅         | ❌    |
| DescribeTrunkInterfaceAssociations     | ❌         | ❌    |
| DescribeVolumeAttribute                | ❌         | ❌    |
| DescribeVolumeStatus                   | ❌         | ❌    |
| DescribeVolumes                        | ✅         | ❌    |
| DescribeVolumesModifications           | ❌         | ❌    |
| DescribeVpcAttribute                   | ✅         | ✅    |
| DescribeVpcClassicLink                 | ✅         | ✅    |
| DescribeVpcClassicLinkDnsSupport       | ✅         | ✅    |
| DescribeVpcEndpointConnectionNotifications| ❌         | ❌    |
| DescribeVpcEndpointConnections         | ❌         | ❌    |
| DescribeVpcEndpointServiceConfigurations| ✅         | ❌    |
| DescribeVpcEndpointServicePermissions  | ✅         | ❌    |
| DescribeVpcEndpointServices            | ✅         | ✅    |
| DescribeVpcEndpoints                   | ✅         | ✅    |
| DescribeVpcPeeringConnections          | ✅         | ✅    |
| DescribeVpcs                           | ✅         | ✅    |
| DescribeVpnConnections                 | ✅         | ❌    |
| DescribeVpnGateways                    | ✅         | ✅    |
| DetachClassicLinkVpc                   | ❌         | ❌    |
| DetachInternetGateway                  | ✅         | ❌    |
| DetachNetworkInterface                 | ✅         | ❌    |
| DetachVolume                           | ✅         | ❌    |
| DetachVpnGateway                       | ✅         | ✅    |
| DisableEbsEncryptionByDefault          | ✅         | ❌    |
| DisableFastLaunch                      | ❌         | ❌    |
| DisableFastSnapshotRestores            | ❌         | ❌    |
| DisableImageDeprecation                | ❌         | ❌    |
| DisableIpamOrganizationAdminAccount    | ❌         | ❌    |
| DisableSerialConsoleAccess             | ❌         | ❌    |
| DisableTransitGatewayRouteTablePropagation| ✅         | ❌    |
| DisableVgwRoutePropagation             | ❌         | ❌    |
| DisableVpcClassicLink                  | ✅         | ❌    |
| DisableVpcClassicLinkDnsSupport        | ✅         | ❌    |
| DisassociateAddress                    | ✅         | ❌    |
| DisassociateClientVpnTargetNetwork     | ❌         | ❌    |
| DisassociateEnclaveCertificateIamRole  | ❌         | ❌    |
| DisassociateIamInstanceProfile         | ✅         | ❌    |
| DisassociateInstanceEventWindow        | ❌         | ❌    |
| DisassociateRouteTable                 | ✅         | ✅    |
| DisassociateSubnetCidrBlock            | ✅         | ❌    |
| DisassociateTransitGatewayMulticastDomain| ❌         | ❌    |
| DisassociateTransitGatewayRouteTable   | ✅         | ❌    |
| DisassociateTrunkInterface             | ❌         | ❌    |
| DisassociateVpcCidrBlock               | ✅         | ❌    |
| EnableEbsEncryptionByDefault           | ✅         | ❌    |
| EnableFastLaunch                       | ❌         | ❌    |
| EnableFastSnapshotRestores             | ❌         | ❌    |
| EnableImageDeprecation                 | ❌         | ❌    |
| EnableIpamOrganizationAdminAccount     | ❌         | ❌    |
| EnableSerialConsoleAccess              | ❌         | ❌    |
| EnableTransitGatewayRouteTablePropagation| ✅         | ❌    |
| EnableVgwRoutePropagation              | ❌         | ❌    |
| EnableVolumeIO                         | ✅         | ❌    |
| EnableVpcClassicLink                   | ✅         | ❌    |
| EnableVpcClassicLinkDnsSupport         | ✅         | ❌    |
| ExportClientVpnClientCertificateRevocationList| ❌         | ❌    |
| ExportClientVpnClientConfiguration     | ❌         | ❌    |
| ExportImage                            | ❌         | ❌    |
| ExportTransitGatewayRoutes             | ❌         | ❌    |
| GetAssociatedEnclaveCertificateIamRoles| ❌         | ❌    |
| GetAssociatedIpv6PoolCidrs             | ❌         | ❌    |
| GetCapacityReservationUsage            | ❌         | ❌    |
| GetCoipPoolUsage                       | ❌         | ❌    |
| GetConsoleOutput                       | ✅         | ❌    |
| GetConsoleScreenshot                   | ❌         | ❌    |
| GetDefaultCreditSpecification          | ❌         | ❌    |
| GetEbsDefaultKmsKeyId                  | ❌         | ❌    |
| GetEbsEncryptionByDefault              | ✅         | ❌    |
| GetFlowLogsIntegrationTemplate         | ❌         | ❌    |
| GetGroupsForCapacityReservation        | ❌         | ❌    |
| GetHostReservationPurchasePreview      | ❌         | ❌    |
| GetInstanceTypesFromInstanceRequirements| ❌         | ❌    |
| GetInstanceUefiData                    | ❌         | ❌    |
| GetIpamAddressHistory                  | ❌         | ❌    |
| GetIpamPoolAllocations                 | ❌         | ❌    |
| GetIpamPoolCidrs                       | ❌         | ❌    |
| GetIpamResourceCidrs                   | ❌         | ❌    |
| GetLaunchTemplateData                  | ❌         | ❌    |
| GetManagedPrefixListAssociations       | ❌         | ❌    |
| GetManagedPrefixListEntries            | ✅         | ❌    |
| GetNetworkInsightsAccessScopeAnalysisFindings| ❌         | ❌    |
| GetNetworkInsightsAccessScopeContent   | ❌         | ❌    |
| GetPasswordData                        | ❌         | ❌    |
| GetReservedInstancesExchangeQuote      | ❌         | ❌    |
| GetSerialConsoleAccessStatus           | ❌         | ❌    |
| GetSpotPlacementScores                 | ❌         | ❌    |
| GetSubnetCidrReservations              | ❌         | ❌    |
| GetTransitGatewayAttachmentPropagations| ❌         | ❌    |
| GetTransitGatewayMulticastDomainAssociations| ❌         | ❌    |
| GetTransitGatewayPrefixListReferences  | ❌         | ❌    |
| GetTransitGatewayRouteTableAssociations| ✅         | ❌    |
| GetTransitGatewayRouteTablePropagations| ✅         | ❌    |
| GetVpnConnectionDeviceSampleConfiguration| ❌         | ❌    |
| GetVpnConnectionDeviceTypes            | ❌         | ❌    |
| ImportClientVpnClientCertificateRevocationList| ❌         | ❌    |
| ImportImage                            | ❌         | ❌    |
| ImportInstance                         | ❌         | ❌    |
| ImportKeyPair                          | ✅         | ✅    |
| ImportSnapshot                         | ❌         | ❌    |
| ImportVolume                           | ✅         | ❌    |
| ListImagesInRecycleBin                 | ❌         | ❌    |
| ListSnapshotsInRecycleBin              | ❌         | ❌    |
| ModifyAddressAttribute                 | ❌         | ❌    |
| ModifyAvailabilityZoneGroup            | ❌         | ❌    |
| ModifyCapacityReservation              | ❌         | ❌    |
| ModifyCapacityReservationFleet         | ❌         | ❌    |
| ModifyClientVpnEndpoint                | ❌         | ❌    |
| ModifyDefaultCreditSpecification       | ❌         | ❌    |
| ModifyEbsDefaultKmsKeyId               | ❌         | ❌    |
| ModifyFleet                            | ❌         | ❌    |
| ModifyFpgaImageAttribute               | ❌         | ❌    |
| ModifyHosts                            | ❌         | ❌    |
| ModifyIdFormat                         | ❌         | ❌    |
| ModifyIdentityIdFormat                 | ❌         | ❌    |
| ModifyImageAttribute                   | ✅         | ❌    |
| ModifyInstanceAttribute                | ✅         | ❌    |
| ModifyInstanceCapacityReservationAttributes| ❌         | ❌    |
| ModifyInstanceCreditSpecification      | ❌         | ❌    |
| ModifyInstanceEventStartTime           | ❌         | ❌    |
| ModifyInstanceEventWindow              | ❌         | ❌    |
| ModifyInstanceMaintenanceOptions       | ❌         | ❌    |
| ModifyInstanceMetadataOptions          | ❌         | ❌    |
| ModifyInstancePlacement                | ❌         | ❌    |
| ModifyIpam                             | ❌         | ❌    |
| ModifyIpamPool                         | ❌         | ❌    |
| ModifyIpamResourceCidr                 | ❌         | ❌    |
| ModifyIpamScope                        | ❌         | ❌    |
| ModifyLaunchTemplate                   | ❌         | ❌    |
| ModifyManagedPrefixList                | ✅         | ❌    |
| ModifyNetworkInterfaceAttribute        | ✅         | ❌    |
| ModifyPrivateDnsNameOptions            | ❌         | ❌    |
| ModifyReservedInstances                | ❌         | ❌    |
| ModifySecurityGroupRules               | ❌         | ❌    |
| ModifySnapshotAttribute                | ✅         | ❌    |
| ModifySnapshotTier                     | ❌         | ❌    |
| ModifySpotFleetRequest                 | ✅         | ❌    |
| ModifySubnetAttribute                  | ✅         | ✅    |
| ModifyTrafficMirrorFilterNetworkServices| ❌         | ❌    |
| ModifyTrafficMirrorFilterRule          | ❌         | ❌    |
| ModifyTrafficMirrorSession             | ❌         | ❌    |
| ModifyTransitGateway                   | ✅         | ❌    |
| ModifyTransitGatewayPrefixListReference| ❌         | ❌    |
| ModifyTransitGatewayVpcAttachment      | ✅         | ❌    |
| ModifyVolume                           | ❌         | ❌    |
| ModifyVolumeAttribute                  | ✅         | ❌    |
| ModifyVpcAttribute                     | ✅         | ❌    |
| ModifyVpcEndpoint                      | ✅         | ❌    |
| ModifyVpcEndpointConnectionNotification| ❌         | ❌    |
| ModifyVpcEndpointServiceConfiguration  | ✅         | ❌    |
| ModifyVpcEndpointServicePayerResponsibility| ❌         | ❌    |
| ModifyVpcEndpointServicePermissions    | ✅         | ❌    |
| ModifyVpcPeeringConnectionOptions      | ✅         | ❌    |
| ModifyVpcTenancy                       | ✅         | ❌    |
| ModifyVpnConnection                    | ❌         | ❌    |
| ModifyVpnConnectionOptions             | ❌         | ❌    |
| ModifyVpnTunnelCertificate             | ❌         | ❌    |
| ModifyVpnTunnelOptions                 | ❌         | ❌    |
| MonitorInstances                       | ✅         | ❌    |
| MoveAddressToVpc                       | ❌         | ❌    |
| MoveByoipCidrToIpam                    | ❌         | ❌    |
| ProvisionByoipCidr                     | ❌         | ❌    |
| ProvisionIpamPoolCidr                  | ❌         | ❌    |
| ProvisionPublicIpv4PoolCidr            | ❌         | ❌    |
| PurchaseHostReservation                | ❌         | ❌    |
| PurchaseReservedInstancesOffering      | ✅         | ✅    |
| PurchaseScheduledInstances             | ❌         | ❌    |
| RebootInstances                        | ✅         | ❌    |
| RegisterImage                          | ✅         | ❌    |
| RegisterInstanceEventNotificationAttributes| ❌         | ❌    |
| RegisterTransitGatewayMulticastGroupMembers| ❌         | ❌    |
| RegisterTransitGatewayMulticastGroupSources| ❌         | ❌    |
| RejectTransitGatewayMulticastDomainAssociations| ❌         | ❌    |
| RejectTransitGatewayPeeringAttachment  | ✅         | ❌    |
| RejectTransitGatewayVpcAttachment      | ❌         | ❌    |
| RejectVpcEndpointConnections           | ❌         | ❌    |
| RejectVpcPeeringConnection             | ✅         | ❌    |
| ReleaseAddress                         | ✅         | ✅    |
| ReleaseHosts                           | ❌         | ❌    |
| ReleaseIpamPoolAllocation              | ❌         | ❌    |
| ReplaceIamInstanceProfileAssociation   | ✅         | ❌    |
| ReplaceNetworkAclAssociation           | ✅         | ❌    |
| ReplaceNetworkAclEntry                 | ✅         | ❌    |
| ReplaceRoute                           | ✅         | ❌    |
| ReplaceRouteTableAssociation           | ✅         | ❌    |
| ReplaceTransitGatewayRoute             | ❌         | ❌    |
| ReportInstanceStatus                   | ❌         | ❌    |
| RequestSpotFleet                       | ✅         | ❌    |
| RequestSpotInstances                   | ✅         | ❌    |
| ResetAddressAttribute                  | ❌         | ❌    |
| ResetEbsDefaultKmsKeyId                | ❌         | ❌    |
| ResetFpgaImageAttribute                | ❌         | ❌    |
| ResetImageAttribute                    | ✅         | ❌    |
| ResetInstanceAttribute                 | ❌         | ❌    |
| ResetNetworkInterfaceAttribute         | ✅         | ❌    |
| ResetSnapshotAttribute                 | ✅         | ❌    |
| RestoreAddressToClassic                | ❌         | ❌    |
| RestoreImageFromRecycleBin             | ❌         | ❌    |
| RestoreManagedPrefixListVersion        | ❌         | ❌    |
| RestoreSnapshotFromRecycleBin          | ❌         | ❌    |
| RestoreSnapshotTier                    | ❌         | ❌    |
| RevokeClientVpnIngress                 | ❌         | ❌    |
| RevokeSecurityGroupEgress              | ✅         | ✅    |
| RevokeSecurityGroupIngress             | ✅         | ❌    |
| RunInstances                           | ✅         | ✅    |
| RunScheduledInstances                  | ❌         | ❌    |
| SearchLocalGatewayRoutes               | ❌         | ❌    |
| SearchTransitGatewayMulticastGroups    | ❌         | ❌    |
| SearchTransitGatewayRoutes             | ✅         | ❌    |
| SendDiagnosticInterrupt                | ❌         | ❌    |
| StartInstances                         | ✅         | ✅    |
| StartNetworkInsightsAccessScopeAnalysis| ❌         | ❌    |
| StartNetworkInsightsAnalysis           | ❌         | ❌    |
| StartVpcEndpointServicePrivateDnsVerification| ❌         | ❌    |
| StopInstances                          | ✅         | ✅    |
| TerminateClientVpnConnections          | ❌         | ❌    |
| TerminateInstances                     | ✅         | ✅    |
| UnassignIpv6Addresses                  | ✅         | ❌    |
| UnassignPrivateIpAddresses             | ✅         | ❌    |
| UnmonitorInstances                     | ✅         | ❌    |
| UpdateSecurityGroupRuleDescriptionsEgress| ✅         | ❌    |
| UpdateSecurityGroupRuleDescriptionsIngress| ✅         | ❌    |
| WithdrawByoipCidr                      | ❌         | ❌    |



## ecr ##

API returns a response for 70.7% of the operations.

| Operation                              | Implemented | Tested |
|----------------------------------------|-------------|--------|
| BatchCheckLayerAvailability            | ❌         | ❌    |
| BatchDeleteImage                       | ✅         | ✅    |
| BatchGetImage                          | ✅         | ✅    |
| BatchGetRepositoryScanningConfiguration| ❌         | ❌    |
| CompleteLayerUpload                    | ❌         | ❌    |
| CreatePullThroughCacheRule             | ❌         | ❌    |
| CreateRepository                       | ✅         | ✅    |
| DeleteLifecyclePolicy                  | ✅         | ✅    |
| DeletePullThroughCacheRule             | ❌         | ❌    |
| DeleteRegistryPolicy                   | ✅         | ❌    |
| DeleteRepository                       | ✅         | ✅    |
| DeleteRepositoryPolicy                 | ✅         | ❌    |
| DescribeImageReplicationStatus         | ❌         | ❌    |
| DescribeImageScanFindings              | ✅         | ❌    |
| DescribeImages                         | ✅         | ✅    |
| DescribePullThroughCacheRules          | ❌         | ❌    |
| DescribeRegistry                       | ✅         | ❌    |
| DescribeRepositories                   | ✅         | ✅    |
| GetAuthorizationToken                  | ✅         | ✅    |
| GetDownloadUrlForLayer                 | ❌         | ❌    |
| GetLifecyclePolicy                     | ✅         | ✅    |
| GetLifecyclePolicyPreview              | ✅         | ❌    |
| GetRegistryPolicy                      | ✅         | ❌    |
| GetRegistryScanningConfiguration       | ❌         | ❌    |
| GetRepositoryPolicy                    | ✅         | ❌    |
| InitiateLayerUpload                    | ❌         | ❌    |
| ListImages                             | ✅         | ✅    |
| ListTagsForResource                    | ✅         | ✅    |
| PutImage                               | ✅         | ❌    |
| PutImageScanningConfiguration          | ✅         | ❌    |
| PutImageTagMutability                  | ✅         | ✅    |
| PutLifecyclePolicy                     | ✅         | ✅    |
| PutRegistryPolicy                      | ✅         | ❌    |
| PutRegistryScanningConfiguration       | ❌         | ❌    |
| PutReplicationConfiguration            | ✅         | ❌    |
| SetRepositoryPolicy                    | ✅         | ❌    |
| StartImageScan                         | ✅         | ❌    |
| StartLifecyclePolicyPreview            | ✅         | ❌    |
| TagResource                            | ✅         | ✅    |
| UntagResource                          | ✅         | ✅    |
| UploadLayerPart                        | ❌         | ❌    |



## ecs ##

API returns a response for 84.6% of the operations.

| Operation                              | Implemented | Tested |
|----------------------------------------|-------------|--------|
| CreateCapacityProvider                 | ✅         | ❌    |
| CreateCluster                          | ✅         | ✅    |
| CreateService                          | ✅         | ✅    |
| CreateTaskSet                          | ✅         | ✅    |
| DeleteAccountSetting                   | ✅         | ❌    |
| DeleteAttributes                       | ✅         | ❌    |
| DeleteCapacityProvider                 | ✅         | ❌    |
| DeleteCluster                          | ✅         | ✅    |
| DeleteService                          | ✅         | ✅    |
| DeleteTaskSet                          | ✅         | ❌    |
| DeregisterContainerInstance            | ✅         | ❌    |
| DeregisterTaskDefinition               | ✅         | ✅    |
| DescribeCapacityProviders              | ✅         | ❌    |
| DescribeClusters                       | ✅         | ✅    |
| DescribeContainerInstances             | ✅         | ❌    |
| DescribeServices                       | ✅         | ✅    |
| DescribeTaskDefinition                 | ✅         | ✅    |
| DescribeTaskSets                       | ✅         | ❌    |
| DescribeTasks                          | ✅         | ✅    |
| DiscoverPollEndpoint                   | ✅         | ❌    |
| ExecuteCommand                         | ❌         | ❌    |
| ListAccountSettings                    | ✅         | ❌    |
| ListAttributes                         | ✅         | ❌    |
| ListClusters                           | ✅         | ✅    |
| ListContainerInstances                 | ✅         | ❌    |
| ListServices                           | ✅         | ❌    |
| ListTagsForResource                    | ✅         | ❌    |
| ListTaskDefinitionFamilies             | ✅         | ❌    |
| ListTaskDefinitions                    | ✅         | ✅    |
| ListTasks                              | ✅         | ✅    |
| PutAccountSetting                      | ✅         | ❌    |
| PutAccountSettingDefault               | ❌         | ❌    |
| PutAttributes                          | ✅         | ❌    |
| PutClusterCapacityProviders            | ✅         | ✅    |
| RegisterContainerInstance              | ✅         | ❌    |
| RegisterTaskDefinition                 | ✅         | ✅    |
| RunTask                                | ✅         | ✅    |
| StartTask                              | ✅         | ❌    |
| StopTask                               | ✅         | ✅    |
| SubmitAttachmentStateChanges           | ❌         | ❌    |
| SubmitContainerStateChange             | ❌         | ❌    |
| SubmitTaskStateChange                  | ❌         | ❌    |
| TagResource                            | ✅         | ❌    |
| UntagResource                          | ✅         | ❌    |
| UpdateCapacityProvider                 | ❌         | ❌    |
| UpdateCluster                          | ✅         | ✅    |
| UpdateClusterSettings                  | ❌         | ❌    |
| UpdateContainerAgent                   | ❌         | ❌    |
| UpdateContainerInstancesState          | ✅         | ❌    |
| UpdateService                          | ✅         | ❌    |
| UpdateServicePrimaryTaskSet            | ✅         | ❌    |
| UpdateTaskSet                          | ✅         | ❌    |



## efs ##

API returns a response for 10.0% of the operations.

| Operation                              | Implemented | Tested |
|----------------------------------------|-------------|--------|
| CreateAccessPoint                      | ❌         | ❌    |
| CreateFileSystem                       | ✅         | ✅    |
| CreateMountTarget                      | ❌         | ❌    |
| CreateReplicationConfiguration         | ❌         | ❌    |
| CreateTags                             | ❌         | ❌    |
| DeleteAccessPoint                      | ❌         | ❌    |
| DeleteFileSystem                       | ✅         | ✅    |
| DeleteFileSystemPolicy                 | ❌         | ❌    |
| DeleteMountTarget                      | ❌         | ❌    |
| DeleteReplicationConfiguration         | ❌         | ❌    |
| DeleteTags                             | ❌         | ❌    |
| DescribeAccessPoints                   | ❌         | ❌    |
| DescribeAccountPreferences             | ❌         | ❌    |
| DescribeBackupPolicy                   | ❌         | ❌    |
| DescribeFileSystemPolicy               | ❌         | ❌    |
| DescribeFileSystems                    | ✅         | ✅    |
| DescribeLifecycleConfiguration         | ❌         | ❌    |
| DescribeMountTargetSecurityGroups      | ❌         | ❌    |
| DescribeMountTargets                   | ❌         | ❌    |
| DescribeReplicationConfigurations      | ❌         | ❌    |
| DescribeTags                           | ❌         | ❌    |
| ListTagsForResource                    | ❌         | ❌    |
| ModifyMountTargetSecurityGroups        | ❌         | ❌    |
| PutAccountPreferences                  | ❌         | ❌    |
| PutBackupPolicy                        | ❌         | ❌    |
| PutFileSystemPolicy                    | ❌         | ❌    |
| PutLifecycleConfiguration              | ❌         | ❌    |
| TagResource                            | ❌         | ❌    |
| UntagResource                          | ❌         | ❌    |
| UpdateFileSystem                       | ❌         | ❌    |



## eks ##

API returns a response for 44.1% of the operations.

| Operation                              | Implemented | Tested |
|----------------------------------------|-------------|--------|
| AssociateEncryptionConfig              | ❌         | ❌    |
| AssociateIdentityProviderConfig        | ❌         | ❌    |
| CreateAddon                            | ❌         | ❌    |
| CreateCluster                          | ✅         | ✅    |
| CreateFargateProfile                   | ✅         | ❌    |
| CreateNodegroup                        | ✅         | ❌    |
| DeleteAddon                            | ❌         | ❌    |
| DeleteCluster                          | ✅         | ✅    |
| DeleteFargateProfile                   | ✅         | ❌    |
| DeleteNodegroup                        | ✅         | ❌    |
| DeregisterCluster                      | ❌         | ❌    |
| DescribeAddon                          | ❌         | ❌    |
| DescribeAddonVersions                  | ❌         | ❌    |
| DescribeCluster                        | ✅         | ✅    |
| DescribeFargateProfile                 | ✅         | ❌    |
| DescribeIdentityProviderConfig         | ❌         | ❌    |
| DescribeNodegroup                      | ✅         | ❌    |
| DescribeUpdate                         | ❌         | ❌    |
| DisassociateIdentityProviderConfig     | ❌         | ❌    |
| ListAddons                             | ❌         | ❌    |
| ListClusters                           | ✅         | ❌    |
| ListFargateProfiles                    | ✅         | ❌    |
| ListIdentityProviderConfigs            | ❌         | ❌    |
| ListNodegroups                         | ✅         | ❌    |
| ListTagsForResource                    | ❌         | ❌    |
| ListUpdates                            | ❌         | ❌    |
| RegisterCluster                        | ❌         | ❌    |
| TagResource                            | ❌         | ❌    |
| UntagResource                          | ❌         | ❌    |
| UpdateAddon                            | ❌         | ❌    |
| UpdateClusterConfig                    | ✅         | ❌    |
| UpdateClusterVersion                   | ❌         | ❌    |
| UpdateNodegroupConfig                  | ✅         | ❌    |
| UpdateNodegroupVersion                 | ✅         | ❌    |



## elasticache ##

API returns a response for 35.4% of the operations.

| Operation                              | Implemented | Tested |
|----------------------------------------|-------------|--------|
| AddTagsToResource                      | ✅         | ❌    |
| AuthorizeCacheSecurityGroupIngress     | ❌         | ❌    |
| BatchApplyUpdateAction                 | ❌         | ❌    |
| BatchStopUpdateAction                  | ❌         | ❌    |
| CompleteMigration                      | ❌         | ❌    |
| CopySnapshot                           | ❌         | ❌    |
| CreateCacheCluster                     | ✅         | ✅    |
| CreateCacheParameterGroup              | ✅         | ✅    |
| CreateCacheSecurityGroup               | ✅         | ✅    |
| CreateCacheSubnetGroup                 | ✅         | ✅    |
| CreateGlobalReplicationGroup           | ❌         | ❌    |
| CreateReplicationGroup                 | ✅         | ✅    |
| CreateSnapshot                         | ❌         | ❌    |
| CreateUser                             | ❌         | ❌    |
| CreateUserGroup                        | ❌         | ❌    |
| DecreaseNodeGroupsInGlobalReplicationGroup| ❌         | ❌    |
| DecreaseReplicaCount                   | ❌         | ❌    |
| DeleteCacheCluster                     | ✅         | ✅    |
| DeleteCacheParameterGroup              | ✅         | ✅    |
| DeleteCacheSecurityGroup               | ✅         | ✅    |
| DeleteCacheSubnetGroup                 | ✅         | ✅    |
| DeleteGlobalReplicationGroup           | ❌         | ❌    |
| DeleteReplicationGroup                 | ✅         | ✅    |
| DeleteSnapshot                         | ❌         | ❌    |
| DeleteUser                             | ❌         | ❌    |
| DeleteUserGroup                        | ❌         | ❌    |
| DescribeCacheClusters                  | ✅         | ✅    |
| DescribeCacheEngineVersions            | ❌         | ❌    |
| DescribeCacheParameterGroups           | ✅         | ✅    |
| DescribeCacheParameters                | ✅         | ✅    |
| DescribeCacheSecurityGroups            | ✅         | ✅    |
| DescribeCacheSubnetGroups              | ✅         | ✅    |
| DescribeEngineDefaultParameters        | ❌         | ❌    |
| DescribeEvents                         | ❌         | ❌    |
| DescribeGlobalReplicationGroups        | ❌         | ❌    |
| DescribeReplicationGroups              | ✅         | ✅    |
| DescribeReservedCacheNodes             | ❌         | ❌    |
| DescribeReservedCacheNodesOfferings    | ❌         | ❌    |
| DescribeServiceUpdates                 | ❌         | ❌    |
| DescribeSnapshots                      | ❌         | ❌    |
| DescribeUpdateActions                  | ❌         | ❌    |
| DescribeUserGroups                     | ❌         | ❌    |
| DescribeUsers                          | ❌         | ❌    |
| DisassociateGlobalReplicationGroup     | ❌         | ❌    |
| FailoverGlobalReplicationGroup         | ❌         | ❌    |
| IncreaseNodeGroupsInGlobalReplicationGroup| ❌         | ❌    |
| IncreaseReplicaCount                   | ❌         | ❌    |
| ListAllowedNodeTypeModifications       | ❌         | ❌    |
| ListTagsForResource                    | ✅         | ❌    |
| ModifyCacheCluster                     | ✅         | ✅    |
| ModifyCacheParameterGroup              | ✅         | ✅    |
| ModifyCacheSubnetGroup                 | ✅         | ✅    |
| ModifyGlobalReplicationGroup           | ❌         | ❌    |
| ModifyReplicationGroup                 | ✅         | ✅    |
| ModifyReplicationGroupShardConfiguration| ❌         | ❌    |
| ModifyUser                             | ❌         | ❌    |
| ModifyUserGroup                        | ❌         | ❌    |
| PurchaseReservedCacheNodesOffering     | ❌         | ❌    |
| RebalanceSlotsInGlobalReplicationGroup | ❌         | ❌    |
| RebootCacheCluster                     | ❌         | ❌    |
| RemoveTagsFromResource                 | ✅         | ❌    |
| ResetCacheParameterGroup               | ❌         | ❌    |
| RevokeCacheSecurityGroupIngress        | ❌         | ❌    |
| StartMigration                         | ❌         | ❌    |
| TestFailover                           | ❌         | ❌    |



## elasticbeanstalk ##

API returns a response for 25.5% of the operations.

| Operation                              | Implemented | Tested |
|----------------------------------------|-------------|--------|
| AbortEnvironmentUpdate                 | ❌         | ❌    |
| ApplyEnvironmentManagedAction          | ❌         | ❌    |
| AssociateEnvironmentOperationsRole     | ❌         | ❌    |
| CheckDNSAvailability                   | ❌         | ❌    |
| ComposeEnvironments                    | ❌         | ❌    |
| CreateApplication                      | ✅         | ✅    |
| CreateApplicationVersion               | ✅         | ✅    |
| CreateConfigurationTemplate            | ❌         | ❌    |
| CreateEnvironment                      | ✅         | ✅    |
| CreatePlatformVersion                  | ❌         | ❌    |
| CreateStorageLocation                  | ❌         | ❌    |
| DeleteApplication                      | ✅         | ✅    |
| DeleteApplicationVersion               | ✅         | ✅    |
| DeleteConfigurationTemplate            | ❌         | ❌    |
| DeleteEnvironmentConfiguration         | ✅         | ✅    |
| DeletePlatformVersion                  | ❌         | ❌    |
| DescribeAccountAttributes              | ❌         | ❌    |
| DescribeApplicationVersions            | ✅         | ✅    |
| DescribeApplications                   | ✅         | ✅    |
| DescribeConfigurationOptions           | ❌         | ❌    |
| DescribeConfigurationSettings          | ❌         | ❌    |
| DescribeEnvironmentHealth              | ❌         | ❌    |
| DescribeEnvironmentManagedActionHistory| ❌         | ❌    |
| DescribeEnvironmentManagedActions      | ❌         | ❌    |
| DescribeEnvironmentResources           | ❌         | ❌    |
| DescribeEnvironments                   | ✅         | ✅    |
| DescribeEvents                         | ❌         | ❌    |
| DescribeInstancesHealth                | ❌         | ❌    |
| DescribePlatformVersion                | ❌         | ❌    |
| DisassociateEnvironmentOperationsRole  | ❌         | ❌    |
| ListAvailableSolutionStacks            | ❌         | ❌    |
| ListPlatformBranches                   | ❌         | ❌    |
| ListPlatformVersions                   | ❌         | ❌    |
| ListTagsForResource                    | ❌         | ❌    |
| RebuildEnvironment                     | ❌         | ❌    |
| RequestEnvironmentInfo                 | ❌         | ❌    |
| RestartAppServer                       | ❌         | ❌    |
| RetrieveEnvironmentInfo                | ❌         | ❌    |
| SwapEnvironmentCNAMEs                  | ❌         | ❌    |
| TerminateEnvironment                   | ❌         | ❌    |
| UpdateApplication                      | ✅         | ✅    |
| UpdateApplicationResourceLifecycle     | ❌         | ❌    |
| UpdateApplicationVersion               | ✅         | ✅    |
| UpdateConfigurationTemplate            | ❌         | ❌    |
| UpdateEnvironment                      | ✅         | ✅    |
| UpdateTagsForResource                  | ❌         | ❌    |
| ValidateConfigurationSettings          | ❌         | ❌    |



## elb ##

API returns a response for 93.1% of the operations.

| Operation                              | Implemented | Tested |
|----------------------------------------|-------------|--------|
| AddTags                                | ✅         | ❌    |
| ApplySecurityGroupsToLoadBalancer      | ✅         | ❌    |
| AttachLoadBalancerToSubnets            | ✅         | ❌    |
| ConfigureHealthCheck                   | ✅         | ❌    |
| CreateAppCookieStickinessPolicy        | ✅         | ❌    |
| CreateLBCookieStickinessPolicy         | ✅         | ❌    |
| CreateLoadBalancer                     | ✅         | ❌    |
| CreateLoadBalancerListeners            | ✅         | ❌    |
| CreateLoadBalancerPolicy               | ✅         | ❌    |
| DeleteLoadBalancer                     | ✅         | ❌    |
| DeleteLoadBalancerListeners            | ✅         | ❌    |
| DeleteLoadBalancerPolicy               | ✅         | ❌    |
| DeregisterInstancesFromLoadBalancer    | ✅         | ❌    |
| DescribeAccountLimits                  | ❌         | ❌    |
| DescribeInstanceHealth                 | ✅         | ❌    |
| DescribeLoadBalancerAttributes         | ✅         | ❌    |
| DescribeLoadBalancerPolicies           | ✅         | ❌    |
| DescribeLoadBalancerPolicyTypes        | ❌         | ❌    |
| DescribeLoadBalancers                  | ✅         | ❌    |
| DescribeTags                           | ✅         | ❌    |
| DetachLoadBalancerFromSubnets          | ✅         | ❌    |
| DisableAvailabilityZonesForLoadBalancer| ✅         | ❌    |
| EnableAvailabilityZonesForLoadBalancer | ✅         | ❌    |
| ModifyLoadBalancerAttributes           | ✅         | ❌    |
| RegisterInstancesWithLoadBalancer      | ✅         | ❌    |
| RemoveTags                             | ✅         | ❌    |
| SetLoadBalancerListenerSSLCertificate  | ✅         | ❌    |
| SetLoadBalancerPoliciesForBackendServer| ✅         | ❌    |
| SetLoadBalancerPoliciesOfListener      | ✅         | ❌    |



## elbv2 ##

API returns a response for 100.0% of the operations.

| Operation                              | Implemented | Tested |
|----------------------------------------|-------------|--------|
| AddListenerCertificates                | ✅         | ❌    |
| AddTags                                | ✅         | ❌    |
| CreateListener                         | ✅         | ✅    |
| CreateLoadBalancer                     | ✅         | ✅    |
| CreateRule                             | ✅         | ✅    |
| CreateTargetGroup                      | ✅         | ✅    |
| DeleteListener                         | ✅         | ❌    |
| DeleteLoadBalancer                     | ✅         | ❌    |
| DeleteRule                             | ✅         | ❌    |
| DeleteTargetGroup                      | ✅         | ❌    |
| DeregisterTargets                      | ✅         | ❌    |
| DescribeAccountLimits                  | ✅         | ❌    |
| DescribeListenerCertificates           | ✅         | ❌    |
| DescribeListeners                      | ✅         | ✅    |
| DescribeLoadBalancerAttributes         | ✅         | ❌    |
| DescribeLoadBalancers                  | ✅         | ✅    |
| DescribeRules                          | ✅         | ✅    |
| DescribeSSLPolicies                    | ✅         | ❌    |
| DescribeTags                           | ✅         | ❌    |
| DescribeTargetGroupAttributes          | ✅         | ❌    |
| DescribeTargetGroups                   | ✅         | ✅    |
| DescribeTargetHealth                   | ✅         | ❌    |
| ModifyListener                         | ✅         | ❌    |
| ModifyLoadBalancerAttributes           | ✅         | ✅    |
| ModifyRule                             | ✅         | ❌    |
| ModifyTargetGroup                      | ✅         | ❌    |
| ModifyTargetGroupAttributes            | ✅         | ❌    |
| RegisterTargets                        | ✅         | ✅    |
| RemoveListenerCertificates             | ✅         | ❌    |
| RemoveTags                             | ✅         | ❌    |
| SetIpAddressType                       | ✅         | ❌    |
| SetRulePriorities                      | ✅         | ❌    |
| SetSecurityGroups                      | ✅         | ❌    |
| SetSubnets                             | ✅         | ❌    |



## emr ##

API returns a response for 57.7% of the operations.

| Operation                              | Implemented | Tested |
|----------------------------------------|-------------|--------|
| AddInstanceFleet                       | ✅         | ✅    |
| AddInstanceGroups                      | ✅         | ❌    |
| AddJobFlowSteps                        | ✅         | ❌    |
| AddTags                                | ✅         | ❌    |
| CancelSteps                            | ❌         | ❌    |
| CreateSecurityConfiguration            | ✅         | ❌    |
| CreateStudio                           | ❌         | ❌    |
| CreateStudioSessionMapping             | ❌         | ❌    |
| DeleteSecurityConfiguration            | ✅         | ❌    |
| DeleteStudio                           | ❌         | ❌    |
| DeleteStudioSessionMapping             | ❌         | ❌    |
| DescribeCluster                        | ✅         | ✅    |
| DescribeJobFlows                       | ✅         | ❌    |
| DescribeNotebookExecution              | ❌         | ❌    |
| DescribeReleaseLabel                   | ❌         | ❌    |
| DescribeSecurityConfiguration          | ✅         | ❌    |
| DescribeStep                           | ✅         | ❌    |
| DescribeStudio                         | ❌         | ❌    |
| GetAutoTerminationPolicy               | ✅         | ✅    |
| GetBlockPublicAccessConfiguration      | ✅         | ❌    |
| GetManagedScalingPolicy                | ❌         | ❌    |
| GetStudioSessionMapping                | ❌         | ❌    |
| ListBootstrapActions                   | ✅         | ✅    |
| ListClusters                           | ✅         | ✅    |
| ListInstanceFleets                     | ✅         | ✅    |
| ListInstanceGroups                     | ✅         | ✅    |
| ListInstances                          | ✅         | ❌    |
| ListNotebookExecutions                 | ❌         | ❌    |
| ListReleaseLabels                      | ❌         | ❌    |
| ListSecurityConfigurations             | ❌         | ❌    |
| ListSteps                              | ✅         | ✅    |
| ListStudioSessionMappings              | ❌         | ❌    |
| ListStudios                            | ❌         | ❌    |
| ModifyCluster                          | ✅         | ❌    |
| ModifyInstanceFleet                    | ✅         | ✅    |
| ModifyInstanceGroups                   | ✅         | ❌    |
| PutAutoScalingPolicy                   | ✅         | ❌    |
| PutAutoTerminationPolicy               | ✅         | ✅    |
| PutBlockPublicAccessConfiguration      | ❌         | ❌    |
| PutManagedScalingPolicy                | ❌         | ❌    |
| RemoveAutoScalingPolicy                | ✅         | ❌    |
| RemoveAutoTerminationPolicy            | ✅         | ✅    |
| RemoveManagedScalingPolicy             | ❌         | ❌    |
| RemoveTags                             | ✅         | ❌    |
| RunJobFlow                             | ✅         | ✅    |
| SetTerminationProtection               | ✅         | ❌    |
| SetVisibleToAllUsers                   | ✅         | ❌    |
| StartNotebookExecution                 | ❌         | ❌    |
| StopNotebookExecution                  | ❌         | ❌    |
| TerminateJobFlows                      | ✅         | ✅    |
| UpdateStudio                           | ❌         | ❌    |
| UpdateStudioSessionMapping             | ❌         | ❌    |



## es ##

API returns a response for 29.3% of the operations.

| Operation                              | Implemented | Tested |
|----------------------------------------|-------------|--------|
| AcceptInboundCrossClusterSearchConnection| ❌         | ❌    |
| AddTags                                | ✅         | ✅    |
| AssociatePackage                       | ❌         | ❌    |
| CancelElasticsearchServiceSoftwareUpdate| ❌         | ❌    |
| CreateElasticsearchDomain              | ✅         | ✅    |
| CreateOutboundCrossClusterSearchConnection| ❌         | ❌    |
| CreatePackage                          | ❌         | ❌    |
| DeleteElasticsearchDomain              | ✅         | ✅    |
| DeleteElasticsearchServiceRole         | ❌         | ❌    |
| DeleteInboundCrossClusterSearchConnection| ❌         | ❌    |
| DeleteOutboundCrossClusterSearchConnection| ❌         | ❌    |
| DeletePackage                          | ❌         | ❌    |
| DescribeDomainAutoTunes                | ❌         | ❌    |
| DescribeDomainChangeProgress           | ❌         | ❌    |
| DescribeElasticsearchDomain            | ✅         | ✅    |
| DescribeElasticsearchDomainConfig      | ✅         | ✅    |
| DescribeElasticsearchDomains           | ✅         | ✅    |
| DescribeElasticsearchInstanceTypeLimits| ❌         | ❌    |
| DescribeInboundCrossClusterSearchConnections| ❌         | ❌    |
| DescribeOutboundCrossClusterSearchConnections| ❌         | ❌    |
| DescribePackages                       | ❌         | ❌    |
| DescribeReservedElasticsearchInstanceOfferings| ❌         | ❌    |
| DescribeReservedElasticsearchInstances | ❌         | ❌    |
| DissociatePackage                      | ❌         | ❌    |
| GetCompatibleElasticsearchVersions     | ✅         | ✅    |
| GetPackageVersionHistory               | ❌         | ❌    |
| GetUpgradeHistory                      | ❌         | ❌    |
| GetUpgradeStatus                       | ❌         | ❌    |
| ListDomainNames                        | ✅         | ✅    |
| ListDomainsForPackage                  | ❌         | ❌    |
| ListElasticsearchInstanceTypes         | ❌         | ❌    |
| ListElasticsearchVersions              | ✅         | ✅    |
| ListPackagesForDomain                  | ❌         | ❌    |
| ListTags                               | ✅         | ✅    |
| PurchaseReservedElasticsearchInstanceOffering| ❌         | ❌    |
| RejectInboundCrossClusterSearchConnection| ❌         | ❌    |
| RemoveTags                             | ✅         | ❌    |
| StartElasticsearchServiceSoftwareUpdate| ❌         | ❌    |
| UpdateElasticsearchDomainConfig        | ✅         | ✅    |
| UpdatePackage                          | ❌         | ❌    |
| UpgradeElasticsearchDomain             | ❌         | ❌    |



## events ##

API returns a response for 71.4% of the operations.

| Operation                              | Implemented | Tested |
|----------------------------------------|-------------|--------|
| ActivateEventSource                    | ❌         | ❌    |
| CancelReplay                           | ✅         | ❌    |
| CreateApiDestination                   | ✅         | ✅    |
| CreateArchive                          | ✅         | ❌    |
| CreateConnection                       | ✅         | ✅    |
| CreateEndpoint                         | ❌         | ❌    |
| CreateEventBus                         | ✅         | ✅    |
| CreatePartnerEventSource               | ❌         | ❌    |
| DeactivateEventSource                  | ❌         | ❌    |
| DeauthorizeConnection                  | ❌         | ❌    |
| DeleteApiDestination                   | ✅         | ✅    |
| DeleteArchive                          | ✅         | ❌    |
| DeleteConnection                       | ✅         | ✅    |
| DeleteEndpoint                         | ❌         | ❌    |
| DeleteEventBus                         | ✅         | ✅    |
| DeletePartnerEventSource               | ❌         | ❌    |
| DeleteRule                             | ✅         | ✅    |
| DescribeApiDestination                 | ✅         | ✅    |
| DescribeArchive                        | ✅         | ❌    |
| DescribeConnection                     | ✅         | ✅    |
| DescribeEndpoint                       | ❌         | ❌    |
| DescribeEventBus                       | ✅         | ✅    |
| DescribeEventSource                    | ❌         | ❌    |
| DescribePartnerEventSource             | ❌         | ❌    |
| DescribeReplay                         | ✅         | ❌    |
| DescribeRule                           | ✅         | ✅    |
| DisableRule                            | ✅         | ✅    |
| EnableRule                             | ✅         | ❌    |
| ListApiDestinations                    | ✅         | ❌    |
| ListArchives                           | ✅         | ❌    |
| ListConnections                        | ✅         | ✅    |
| ListEndpoints                          | ❌         | ❌    |
| ListEventBuses                         | ✅         | ✅    |
| ListEventSources                       | ❌         | ❌    |
| ListPartnerEventSourceAccounts         | ❌         | ❌    |
| ListPartnerEventSources                | ❌         | ❌    |
| ListReplays                            | ✅         | ❌    |
| ListRuleNamesByTarget                  | ✅         | ❌    |
| ListRules                              | ✅         | ✅    |
| ListTagsForResource                    | ✅         | ✅    |
| ListTargetsByRule                      | ✅         | ✅    |
| PutEvents                              | ✅         | ✅    |
| PutPartnerEvents                       | ❌         | ❌    |
| PutPermission                          | ✅         | ✅    |
| PutRule                                | ✅         | ✅    |
| PutTargets                             | ✅         | ✅    |
| RemovePermission                       | ✅         | ✅    |
| RemoveTargets                          | ✅         | ✅    |
| StartReplay                            | ✅         | ❌    |
| TagResource                            | ✅         | ✅    |
| TestEventPattern                       | ✅         | ❌    |
| UntagResource                          | ✅         | ✅    |
| UpdateApiDestination                   | ✅         | ❌    |
| UpdateArchive                          | ✅         | ❌    |
| UpdateConnection                       | ✅         | ❌    |
| UpdateEndpoint                         | ❌         | ❌    |



## firehose ##

API returns a response for 83.3% of the operations.

| Operation                              | Implemented | Tested |
|----------------------------------------|-------------|--------|
| CreateDeliveryStream                   | ✅         | ✅    |
| DeleteDeliveryStream                   | ✅         | ✅    |
| DescribeDeliveryStream                 | ✅         | ✅    |
| ListDeliveryStreams                    | ✅         | ✅    |
| ListTagsForDeliveryStream              | ✅         | ✅    |
| PutRecord                              | ✅         | ✅    |
| PutRecordBatch                         | ✅         | ❌    |
| StartDeliveryStreamEncryption          | ❌         | ❌    |
| StopDeliveryStreamEncryption           | ❌         | ❌    |
| TagDeliveryStream                      | ✅         | ❌    |
| UntagDeliveryStream                    | ✅         | ❌    |
| UpdateDestination                      | ✅         | ✅    |



## glacier ##

API returns a response for 100.0% of the operations.

| Operation                              | Implemented | Tested |
|----------------------------------------|-------------|--------|
| AbortMultipartUpload                   | ✅         | ❌    |
| AbortVaultLock                         | ✅         | ❌    |
| AddTagsToVault                         | ✅         | ✅    |
| CompleteMultipartUpload                | ✅         | ❌    |
| CompleteVaultLock                      | ✅         | ❌    |
| CreateVault                            | ✅         | ✅    |
| DeleteArchive                          | ✅         | ❌    |
| DeleteVault                            | ✅         | ✅    |
| DeleteVaultAccessPolicy                | ✅         | ❌    |
| DeleteVaultNotifications               | ✅         | ❌    |
| DescribeJob                            | ✅         | ❌    |
| DescribeVault                          | ✅         | ✅    |
| GetDataRetrievalPolicy                 | ✅         | ❌    |
| GetJobOutput                           | ✅         | ✅    |
| GetVaultAccessPolicy                   | ✅         | ✅    |
| GetVaultLock                           | ✅         | ❌    |
| GetVaultNotifications                  | ✅         | ✅    |
| InitiateJob                            | ✅         | ✅    |
| InitiateMultipartUpload                | ✅         | ❌    |
| InitiateVaultLock                      | ✅         | ❌    |
| ListJobs                               | ✅         | ❌    |
| ListMultipartUploads                   | ✅         | ❌    |
| ListParts                              | ✅         | ❌    |
| ListProvisionedCapacity                | ✅         | ❌    |
| ListTagsForVault                       | ✅         | ✅    |
| ListVaults                             | ✅         | ✅    |
| PurchaseProvisionedCapacity            | ✅         | ❌    |
| RemoveTagsFromVault                    | ✅         | ❌    |
| SetDataRetrievalPolicy                 | ✅         | ❌    |
| SetVaultAccessPolicy                   | ✅         | ❌    |
| SetVaultNotifications                  | ✅         | ❌    |
| UploadArchive                          | ✅         | ✅    |
| UploadMultipartPart                    | ✅         | ❌    |



## glue ##

API returns a response for 51.1% of the operations.

| Operation                              | Implemented | Tested |
|----------------------------------------|-------------|--------|
| BatchCreatePartition                   | ✅         | ❌    |
| BatchDeleteConnection                  | ❌         | ❌    |
| BatchDeletePartition                   | ✅         | ❌    |
| BatchDeleteTable                       | ✅         | ❌    |
| BatchDeleteTableVersion                | ❌         | ❌    |
| BatchGetBlueprints                     | ❌         | ❌    |
| BatchGetCrawlers                       | ❌         | ❌    |
| BatchGetCustomEntityTypes              | ❌         | ❌    |
| BatchGetDevEndpoints                   | ❌         | ❌    |
| BatchGetJobs                           | ❌         | ❌    |
| BatchGetPartition                      | ✅         | ❌    |
| BatchGetTriggers                       | ❌         | ❌    |
| BatchGetWorkflows                      | ❌         | ❌    |
| BatchStopJobRun                        | ❌         | ❌    |
| BatchUpdatePartition                   | ✅         | ❌    |
| CancelMLTaskRun                        | ❌         | ❌    |
| CancelStatement                        | ❌         | ❌    |
| CheckSchemaVersionValidity             | ✅         | ❌    |
| CreateBlueprint                        | ❌         | ❌    |
| CreateClassifier                       | ✅         | ✅    |
| CreateConnection                       | ✅         | ✅    |
| CreateCrawler                          | ✅         | ✅    |
| CreateCustomEntityType                 | ❌         | ❌    |
| CreateDatabase                         | ✅         | ✅    |
| CreateDevEndpoint                      | ❌         | ❌    |
| CreateJob                              | ✅         | ✅    |
| CreateMLTransform                      | ❌         | ❌    |
| CreatePartition                        | ✅         | ✅    |
| CreatePartitionIndex                   | ✅         | ✅    |
| CreateRegistry                         | ✅         | ✅    |
| CreateSchema                           | ✅         | ✅    |
| CreateScript                           | ❌         | ❌    |
| CreateSecurityConfiguration            | ✅         | ✅    |
| CreateSession                          | ❌         | ❌    |
| CreateTable                            | ✅         | ✅    |
| CreateTrigger                          | ✅         | ✅    |
| CreateUserDefinedFunction              | ❌         | ❌    |
| CreateWorkflow                         | ✅         | ✅    |
| DeleteBlueprint                        | ❌         | ❌    |
| DeleteClassifier                       | ✅         | ✅    |
| DeleteColumnStatisticsForPartition     | ❌         | ❌    |
| DeleteColumnStatisticsForTable         | ❌         | ❌    |
| DeleteConnection                       | ✅         | ✅    |
| DeleteCrawler                          | ✅         | ✅    |
| DeleteCustomEntityType                 | ❌         | ❌    |
| DeleteDatabase                         | ✅         | ✅    |
| DeleteDevEndpoint                      | ❌         | ❌    |
| DeleteJob                              | ✅         | ✅    |
| DeleteMLTransform                      | ❌         | ❌    |
| DeletePartition                        | ✅         | ✅    |
| DeletePartitionIndex                   | ✅         | ✅    |
| DeleteRegistry                         | ✅         | ✅    |
| DeleteResourcePolicy                   | ✅         | ✅    |
| DeleteSchema                           | ✅         | ✅    |
| DeleteSchemaVersions                   | ✅         | ✅    |
| DeleteSecurityConfiguration            | ✅         | ✅    |
| DeleteSession                          | ❌         | ❌    |
| DeleteTable                            | ✅         | ✅    |
| DeleteTableVersion                     | ❌         | ❌    |
| DeleteTrigger                          | ✅         | ✅    |
| DeleteUserDefinedFunction              | ❌         | ❌    |
| DeleteWorkflow                         | ✅         | ✅    |
| GetBlueprint                           | ❌         | ❌    |
| GetBlueprintRun                        | ❌         | ❌    |
| GetBlueprintRuns                       | ❌         | ❌    |
| GetCatalogImportStatus                 | ✅         | ❌    |
| GetClassifier                          | ✅         | ✅    |
| GetClassifiers                         | ✅         | ✅    |
| GetColumnStatisticsForPartition        | ❌         | ❌    |
| GetColumnStatisticsForTable            | ❌         | ❌    |
| GetConnection                          | ✅         | ✅    |
| GetConnections                         | ✅         | ✅    |
| GetCrawler                             | ✅         | ✅    |
| GetCrawlerMetrics                      | ❌         | ❌    |
| GetCrawlers                            | ✅         | ✅    |
| GetCustomEntityType                    | ❌         | ❌    |
| GetDataCatalogEncryptionSettings       | ❌         | ❌    |
| GetDatabase                            | ✅         | ✅    |
| GetDatabases                           | ✅         | ✅    |
| GetDataflowGraph                       | ❌         | ❌    |
| GetDevEndpoint                         | ❌         | ❌    |
| GetDevEndpoints                        | ❌         | ❌    |
| GetJob                                 | ✅         | ✅    |
| GetJobBookmark                         | ❌         | ❌    |
| GetJobRun                              | ✅         | ✅    |
| GetJobRuns                             | ✅         | ✅    |
| GetJobs                                | ✅         | ✅    |
| GetMLTaskRun                           | ❌         | ❌    |
| GetMLTaskRuns                          | ❌         | ❌    |
| GetMLTransform                         | ❌         | ❌    |
| GetMLTransforms                        | ❌         | ❌    |
| GetMapping                             | ❌         | ❌    |
| GetPartition                           | ✅         | ✅    |
| GetPartitionIndexes                    | ✅         | ✅    |
| GetPartitions                          | ✅         | ✅    |
| GetPlan                                | ❌         | ❌    |
| GetRegistry                            | ✅         | ✅    |
| GetResourcePolicies                    | ❌         | ❌    |
| GetResourcePolicy                      | ✅         | ✅    |
| GetSchema                              | ✅         | ✅    |
| GetSchemaByDefinition                  | ✅         | ❌    |
| GetSchemaVersion                       | ✅         | ✅    |
| GetSchemaVersionsDiff                  | ✅         | ❌    |
| GetSecurityConfiguration               | ✅         | ✅    |
| GetSecurityConfigurations              | ✅         | ✅    |
| GetSession                             | ❌         | ❌    |
| GetStatement                           | ❌         | ❌    |
| GetTable                               | ✅         | ✅    |
| GetTableVersion                        | ✅         | ❌    |
| GetTableVersions                       | ✅         | ❌    |
| GetTables                              | ✅         | ✅    |
| GetTags                                | ✅         | ❌    |
| GetTrigger                             | ✅         | ✅    |
| GetTriggers                            | ❌         | ❌    |
| GetUnfilteredPartitionMetadata         | ❌         | ❌    |
| GetUnfilteredPartitionsMetadata        | ❌         | ❌    |
| GetUnfilteredTableMetadata             | ❌         | ❌    |
| GetUserDefinedFunction                 | ❌         | ❌    |
| GetUserDefinedFunctions                | ❌         | ❌    |
| GetWorkflow                            | ✅         | ✅    |
| GetWorkflowRun                         | ❌         | ❌    |
| GetWorkflowRunProperties               | ❌         | ❌    |
| GetWorkflowRuns                        | ❌         | ❌    |
| ImportCatalogToGlue                    | ✅         | ❌    |
| ListBlueprints                         | ❌         | ❌    |
| ListCrawlers                           | ❌         | ❌    |
| ListCrawls                             | ❌         | ❌    |
| ListCustomEntityTypes                  | ❌         | ❌    |
| ListDevEndpoints                       | ❌         | ❌    |
| ListJobs                               | ✅         | ✅    |
| ListMLTransforms                       | ❌         | ❌    |
| ListRegistries                         | ✅         | ✅    |
| ListSchemaVersions                     | ✅         | ✅    |
| ListSchemas                            | ✅         | ✅    |
| ListSessions                           | ❌         | ❌    |
| ListStatements                         | ❌         | ❌    |
| ListTriggers                           | ❌         | ❌    |
| ListWorkflows                          | ✅         | ✅    |
| PutDataCatalogEncryptionSettings       | ❌         | ❌    |
| PutResourcePolicy                      | ✅         | ✅    |
| PutSchemaVersionMetadata               | ✅         | ✅    |
| PutWorkflowRunProperties               | ❌         | ❌    |
| QuerySchemaVersionMetadata             | ✅         | ✅    |
| RegisterSchemaVersion                  | ✅         | ✅    |
| RemoveSchemaVersionMetadata            | ✅         | ✅    |
| ResetJobBookmark                       | ❌         | ❌    |
| ResumeWorkflowRun                      | ❌         | ❌    |
| RunStatement                           | ❌         | ❌    |
| SearchTables                           | ❌         | ❌    |
| StartBlueprintRun                      | ❌         | ❌    |
| StartCrawler                           | ✅         | ✅    |
| StartCrawlerSchedule                   | ❌         | ❌    |
| StartExportLabelsTaskRun               | ❌         | ❌    |
| StartImportLabelsTaskRun               | ❌         | ❌    |
| StartJobRun                            | ✅         | ✅    |
| StartMLEvaluationTaskRun               | ❌         | ❌    |
| StartMLLabelingSetGenerationTaskRun    | ❌         | ❌    |
| StartTrigger                           | ✅         | ❌    |
| StartWorkflowRun                       | ❌         | ❌    |
| StopCrawler                            | ✅         | ❌    |
| StopCrawlerSchedule                    | ❌         | ❌    |
| StopSession                            | ❌         | ❌    |
| StopTrigger                            | ✅         | ❌    |
| StopWorkflowRun                        | ❌         | ❌    |
| TagResource                            | ✅         | ❌    |
| UntagResource                          | ✅         | ❌    |
| UpdateBlueprint                        | ❌         | ❌    |
| UpdateClassifier                       | ✅         | ❌    |
| UpdateColumnStatisticsForPartition     | ❌         | ❌    |
| UpdateColumnStatisticsForTable         | ❌         | ❌    |
| UpdateConnection                       | ✅         | ❌    |
| UpdateCrawler                          | ✅         | ✅    |
| UpdateCrawlerSchedule                  | ❌         | ❌    |
| UpdateDatabase                         | ✅         | ✅    |
| UpdateDevEndpoint                      | ❌         | ❌    |
| UpdateJob                              | ✅         | ✅    |
| UpdateMLTransform                      | ❌         | ❌    |
| UpdatePartition                        | ✅         | ✅    |
| UpdateRegistry                         | ✅         | ✅    |
| UpdateSchema                           | ✅         | ✅    |
| UpdateTable                            | ✅         | ✅    |
| UpdateTrigger                          | ✅         | ✅    |
| UpdateUserDefinedFunction              | ❌         | ❌    |
| UpdateWorkflow                         | ✅         | ❌    |



## iam ##

API returns a response for 80.4% of the operations.

| Operation                              | Implemented | Tested |
|----------------------------------------|-------------|--------|
| AddClientIDToOpenIDConnectProvider     | ❌         | ❌    |
| AddRoleToInstanceProfile               | ✅         | ✅    |
| AddUserToGroup                         | ✅         | ❌    |
| AttachGroupPolicy                      | ✅         | ✅    |
| AttachRolePolicy                       | ✅         | ✅    |
| AttachUserPolicy                       | ✅         | ✅    |
| ChangePassword                         | ❌         | ❌    |
| CreateAccessKey                        | ✅         | ✅    |
| CreateAccountAlias                     | ✅         | ❌    |
| CreateGroup                            | ✅         | ✅    |
| CreateInstanceProfile                  | ✅         | ✅    |
| CreateLoginProfile                     | ✅         | ❌    |
| CreateOpenIDConnectProvider            | ✅         | ❌    |
| CreatePolicy                           | ✅         | ✅    |
| CreatePolicyVersion                    | ✅         | ❌    |
| CreateRole                             | ✅         | ✅    |
| CreateSAMLProvider                     | ✅         | ❌    |
| CreateServiceLinkedRole                | ✅         | ✅    |
| CreateServiceSpecificCredential        | ❌         | ❌    |
| CreateUser                             | ✅         | ✅    |
| CreateVirtualMFADevice                 | ✅         | ❌    |
| DeactivateMFADevice                    | ✅         | ❌    |
| DeleteAccessKey                        | ✅         | ❌    |
| DeleteAccountAlias                     | ✅         | ❌    |
| DeleteAccountPasswordPolicy            | ✅         | ❌    |
| DeleteGroup                            | ✅         | ✅    |
| DeleteGroupPolicy                      | ✅         | ✅    |
| DeleteInstanceProfile                  | ✅         | ✅    |
| DeleteLoginProfile                     | ✅         | ❌    |
| DeleteOpenIDConnectProvider            | ✅         | ❌    |
| DeletePolicy                           | ✅         | ✅    |
| DeletePolicyVersion                    | ✅         | ❌    |
| DeleteRole                             | ✅         | ✅    |
| DeleteRolePermissionsBoundary          | ✅         | ❌    |
| DeleteRolePolicy                       | ✅         | ✅    |
| DeleteSAMLProvider                     | ✅         | ❌    |
| DeleteSSHPublicKey                     | ✅         | ❌    |
| DeleteServerCertificate                | ✅         | ❌    |
| DeleteServiceLinkedRole                | ✅         | ✅    |
| DeleteServiceSpecificCredential        | ❌         | ❌    |
| DeleteSigningCertificate               | ✅         | ❌    |
| DeleteUser                             | ✅         | ✅    |
| DeleteUserPermissionsBoundary          | ❌         | ❌    |
| DeleteUserPolicy                       | ✅         | ✅    |
| DeleteVirtualMFADevice                 | ✅         | ❌    |
| DetachGroupPolicy                      | ✅         | ✅    |
| DetachRolePolicy                       | ✅         | ✅    |
| DetachUserPolicy                       | ✅         | ✅    |
| EnableMFADevice                        | ✅         | ❌    |
| GenerateCredentialReport               | ✅         | ❌    |
| GenerateOrganizationsAccessReport      | ❌         | ❌    |
| GenerateServiceLastAccessedDetails     | ❌         | ❌    |
| GetAccessKeyLastUsed                   | ✅         | ❌    |
| GetAccountAuthorizationDetails         | ✅         | ✅    |
| GetAccountPasswordPolicy               | ✅         | ❌    |
| GetAccountSummary                      | ✅         | ❌    |
| GetContextKeysForCustomPolicy          | ❌         | ❌    |
| GetContextKeysForPrincipalPolicy       | ❌         | ❌    |
| GetCredentialReport                    | ✅         | ❌    |
| GetGroup                               | ✅         | ✅    |
| GetGroupPolicy                         | ✅         | ✅    |
| GetInstanceProfile                     | ✅         | ✅    |
| GetLoginProfile                        | ✅         | ❌    |
| GetOpenIDConnectProvider               | ✅         | ❌    |
| GetOrganizationsAccessReport           | ❌         | ❌    |
| GetPolicy                              | ✅         | ✅    |
| GetPolicyVersion                       | ✅         | ✅    |
| GetRole                                | ✅         | ✅    |
| GetRolePolicy                          | ✅         | ✅    |
| GetSAMLProvider                        | ✅         | ❌    |
| GetSSHPublicKey                        | ✅         | ❌    |
| GetServerCertificate                   | ✅         | ❌    |
| GetServiceLastAccessedDetails          | ❌         | ❌    |
| GetServiceLastAccessedDetailsWithEntities| ❌         | ❌    |
| GetServiceLinkedRoleDeletionStatus     | ✅         | ❌    |
| GetUser                                | ✅         | ✅    |
| GetUserPolicy                          | ✅         | ✅    |
| ListAccessKeys                         | ✅         | ❌    |
| ListAccountAliases                     | ✅         | ❌    |
| ListAttachedGroupPolicies              | ✅         | ✅    |
| ListAttachedRolePolicies               | ✅         | ✅    |
| ListAttachedUserPolicies               | ✅         | ✅    |
| ListEntitiesForPolicy                  | ✅         | ❌    |
| ListGroupPolicies                      | ✅         | ✅    |
| ListGroups                             | ✅         | ❌    |
| ListGroupsForUser                      | ✅         | ❌    |
| ListInstanceProfileTags                | ✅         | ✅    |
| ListInstanceProfiles                   | ✅         | ✅    |
| ListInstanceProfilesForRole            | ✅         | ✅    |
| ListMFADeviceTags                      | ❌         | ❌    |
| ListMFADevices                         | ✅         | ❌    |
| ListOpenIDConnectProviderTags          | ✅         | ❌    |
| ListOpenIDConnectProviders             | ✅         | ❌    |
| ListPolicies                           | ✅         | ✅    |
| ListPoliciesGrantingServiceAccess      | ❌         | ❌    |
| ListPolicyTags                         | ✅         | ❌    |
| ListPolicyVersions                     | ✅         | ✅    |
| ListRolePolicies                       | ✅         | ✅    |
| ListRoleTags                           | ✅         | ❌    |
| ListRoles                              | ✅         | ✅    |
| ListSAMLProviderTags                   | ❌         | ❌    |
| ListSAMLProviders                      | ✅         | ❌    |
| ListSSHPublicKeys                      | ✅         | ❌    |
| ListServerCertificateTags              | ❌         | ❌    |
| ListServerCertificates                 | ✅         | ❌    |
| ListServiceSpecificCredentials         | ❌         | ❌    |
| ListSigningCertificates                | ✅         | ❌    |
| ListUserPolicies                       | ✅         | ✅    |
| ListUserTags                           | ✅         | ❌    |
| ListUsers                              | ✅         | ❌    |
| ListVirtualMFADevices                  | ✅         | ❌    |
| PutGroupPolicy                         | ✅         | ✅    |
| PutRolePermissionsBoundary             | ✅         | ❌    |
| PutRolePolicy                          | ✅         | ✅    |
| PutUserPermissionsBoundary             | ❌         | ❌    |
| PutUserPolicy                          | ✅         | ✅    |
| RemoveClientIDFromOpenIDConnectProvider| ❌         | ❌    |
| RemoveRoleFromInstanceProfile          | ✅         | ✅    |
| RemoveUserFromGroup                    | ✅         | ❌    |
| ResetServiceSpecificCredential         | ❌         | ❌    |
| ResyncMFADevice                        | ❌         | ❌    |
| SetDefaultPolicyVersion                | ✅         | ❌    |
| SetSecurityTokenServicePreferences     | ❌         | ❌    |
| SimulateCustomPolicy                   | ❌         | ❌    |
| SimulatePrincipalPolicy                | ✅         | ✅    |
| TagInstanceProfile                     | ✅         | ✅    |
| TagMFADevice                           | ❌         | ❌    |
| TagOpenIDConnectProvider               | ✅         | ❌    |
| TagPolicy                              | ✅         | ❌    |
| TagRole                                | ✅         | ❌    |
| TagSAMLProvider                        | ❌         | ❌    |
| TagServerCertificate                   | ❌         | ❌    |
| TagUser                                | ✅         | ❌    |
| UntagInstanceProfile                   | ✅         | ✅    |
| UntagMFADevice                         | ❌         | ❌    |
| UntagOpenIDConnectProvider             | ✅         | ❌    |
| UntagPolicy                            | ✅         | ❌    |
| UntagRole                              | ✅         | ❌    |
| UntagSAMLProvider                      | ❌         | ❌    |
| UntagServerCertificate                 | ❌         | ❌    |
| UntagUser                              | ✅         | ❌    |
| UpdateAccessKey                        | ✅         | ❌    |
| UpdateAccountPasswordPolicy            | ✅         | ❌    |
| UpdateAssumeRolePolicy                 | ✅         | ❌    |
| UpdateGroup                            | ✅         | ❌    |
| UpdateLoginProfile                     | ✅         | ❌    |
| UpdateOpenIDConnectProviderThumbprint  | ✅         | ❌    |
| UpdateRole                             | ✅         | ✅    |
| UpdateRoleDescription                  | ✅         | ❌    |
| UpdateSAMLProvider                     | ✅         | ❌    |
| UpdateSSHPublicKey                     | ✅         | ❌    |
| UpdateServerCertificate                | ❌         | ❌    |
| UpdateServiceSpecificCredential        | ❌         | ❌    |
| UpdateSigningCertificate               | ✅         | ❌    |
| UpdateUser                             | ✅         | ❌    |
| UploadSSHPublicKey                     | ✅         | ❌    |
| UploadServerCertificate                | ✅         | ❌    |
| UploadSigningCertificate               | ✅         | ❌    |



## iot ##

API returns a response for 39.7% of the operations.

| Operation                              | Implemented | Tested |
|----------------------------------------|-------------|--------|
| AcceptCertificateTransfer              | ❌         | ❌    |
| AddThingToBillingGroup                 | ❌         | ❌    |
| AddThingToThingGroup                   | ✅         | ✅    |
| AssociateTargetsWithJob                | ❌         | ❌    |
| AttachPolicy                           | ✅         | ✅    |
| AttachPrincipalPolicy                  | ✅         | ❌    |
| AttachSecurityProfile                  | ❌         | ❌    |
| AttachThingPrincipal                   | ✅         | ✅    |
| CancelAuditMitigationActionsTask       | ❌         | ❌    |
| CancelAuditTask                        | ❌         | ❌    |
| CancelCertificateTransfer              | ❌         | ❌    |
| CancelDetectMitigationActionsTask      | ❌         | ❌    |
| CancelJob                              | ✅         | ❌    |
| CancelJobExecution                     | ✅         | ❌    |
| ClearDefaultAuthorizer                 | ❌         | ❌    |
| ConfirmTopicRuleDestination            | ❌         | ❌    |
| CreateAuditSuppression                 | ❌         | ❌    |
| CreateAuthorizer                       | ❌         | ❌    |
| CreateBillingGroup                     | ❌         | ❌    |
| CreateCertificateFromCsr               | ✅         | ❌    |
| CreateCustomMetric                     | ❌         | ❌    |
| CreateDimension                        | ❌         | ❌    |
| CreateDomainConfiguration              | ✅         | ❌    |
| CreateDynamicThingGroup                | ✅         | ✅    |
| CreateFleetMetric                      | ❌         | ❌    |
| CreateJob                              | ✅         | ✅    |
| CreateJobTemplate                      | ❌         | ❌    |
| CreateKeysAndCertificate               | ✅         | ❌    |
| CreateMitigationAction                 | ❌         | ❌    |
| CreateOTAUpdate                        | ❌         | ❌    |
| CreatePolicy                           | ✅         | ✅    |
| CreatePolicyVersion                    | ✅         | ❌    |
| CreateProvisioningClaim                | ❌         | ❌    |
| CreateProvisioningTemplate             | ❌         | ❌    |
| CreateProvisioningTemplateVersion      | ❌         | ❌    |
| CreateRoleAlias                        | ❌         | ❌    |
| CreateScheduledAudit                   | ❌         | ❌    |
| CreateSecurityProfile                  | ❌         | ❌    |
| CreateStream                           | ❌         | ❌    |
| CreateThing                            | ✅         | ✅    |
| CreateThingGroup                       | ✅         | ✅    |
| CreateThingType                        | ✅         | ❌    |
| CreateTopicRule                        | ✅         | ✅    |
| CreateTopicRuleDestination             | ✅         | ✅    |
| DeleteAccountAuditConfiguration        | ❌         | ❌    |
| DeleteAuditSuppression                 | ❌         | ❌    |
| DeleteAuthorizer                       | ❌         | ❌    |
| DeleteBillingGroup                     | ❌         | ❌    |
| DeleteCACertificate                    | ✅         | ❌    |
| DeleteCertificate                      | ✅         | ❌    |
| DeleteCustomMetric                     | ❌         | ❌    |
| DeleteDimension                        | ❌         | ❌    |
| DeleteDomainConfiguration              | ✅         | ❌    |
| DeleteDynamicThingGroup                | ✅         | ✅    |
| DeleteFleetMetric                      | ❌         | ❌    |
| DeleteJob                              | ✅         | ✅    |
| DeleteJobExecution                     | ✅         | ❌    |
| DeleteJobTemplate                      | ❌         | ❌    |
| DeleteMitigationAction                 | ❌         | ❌    |
| DeleteOTAUpdate                        | ❌         | ❌    |
| DeletePolicy                           | ✅         | ✅    |
| DeletePolicyVersion                    | ✅         | ❌    |
| DeleteProvisioningTemplate             | ❌         | ❌    |
| DeleteProvisioningTemplateVersion      | ❌         | ❌    |
| DeleteRegistrationCode                 | ❌         | ❌    |
| DeleteRoleAlias                        | ❌         | ❌    |
| DeleteScheduledAudit                   | ❌         | ❌    |
| DeleteSecurityProfile                  | ❌         | ❌    |
| DeleteStream                           | ❌         | ❌    |
| DeleteThing                            | ✅         | ✅    |
| DeleteThingGroup                       | ✅         | ✅    |
| DeleteThingType                        | ✅         | ❌    |
| DeleteTopicRule                        | ✅         | ✅    |
| DeleteTopicRuleDestination             | ✅         | ❌    |
| DeleteV2LoggingLevel                   | ❌         | ❌    |
| DeprecateThingType                     | ✅         | ❌    |
| DescribeAccountAuditConfiguration      | ❌         | ❌    |
| DescribeAuditFinding                   | ❌         | ❌    |
| DescribeAuditMitigationActionsTask     | ❌         | ❌    |
| DescribeAuditSuppression               | ❌         | ❌    |
| DescribeAuditTask                      | ❌         | ❌    |
| DescribeAuthorizer                     | ❌         | ❌    |
| DescribeBillingGroup                   | ❌         | ❌    |
| DescribeCACertificate                  | ✅         | ❌    |
| DescribeCertificate                    | ✅         | ❌    |
| DescribeCustomMetric                   | ❌         | ❌    |
| DescribeDefaultAuthorizer              | ❌         | ❌    |
| DescribeDetectMitigationActionsTask    | ❌         | ❌    |
| DescribeDimension                      | ❌         | ❌    |
| DescribeDomainConfiguration            | ✅         | ❌    |
| DescribeEndpoint                       | ✅         | ✅    |
| DescribeEventConfigurations            | ❌         | ❌    |
| DescribeFleetMetric                    | ❌         | ❌    |
| DescribeIndex                          | ❌         | ❌    |
| DescribeJob                            | ✅         | ✅    |
| DescribeJobExecution                   | ✅         | ✅    |
| DescribeJobTemplate                    | ❌         | ❌    |
| DescribeManagedJobTemplate             | ❌         | ❌    |
| DescribeMitigationAction               | ❌         | ❌    |
| DescribeProvisioningTemplate           | ❌         | ❌    |
| DescribeProvisioningTemplateVersion    | ❌         | ❌    |
| DescribeRoleAlias                      | ❌         | ❌    |
| DescribeScheduledAudit                 | ❌         | ❌    |
| DescribeSecurityProfile                | ❌         | ❌    |
| DescribeStream                         | ❌         | ❌    |
| DescribeThing                          | ✅         | ✅    |
| DescribeThingGroup                     | ✅         | ✅    |
| DescribeThingRegistrationTask          | ❌         | ❌    |
| DescribeThingType                      | ✅         | ❌    |
| DetachPolicy                           | ✅         | ❌    |
| DetachPrincipalPolicy                  | ✅         | ❌    |
| DetachSecurityProfile                  | ❌         | ❌    |
| DetachThingPrincipal                   | ✅         | ✅    |
| DisableTopicRule                       | ✅         | ❌    |
| EnableTopicRule                        | ✅         | ❌    |
| GetBehaviorModelTrainingSummaries      | ❌         | ❌    |
| GetBucketsAggregation                  | ❌         | ❌    |
| GetCardinality                         | ❌         | ❌    |
| GetEffectivePolicies                   | ❌         | ❌    |
| GetIndexingConfiguration               | ❌         | ❌    |
| GetJobDocument                         | ✅         | ❌    |
| GetLoggingOptions                      | ❌         | ❌    |
| GetOTAUpdate                           | ❌         | ❌    |
| GetPercentiles                         | ❌         | ❌    |
| GetPolicy                              | ✅         | ✅    |
| GetPolicyVersion                       | ✅         | ❌    |
| GetRegistrationCode                    | ✅         | ❌    |
| GetStatistics                          | ❌         | ❌    |
| GetTopicRule                           | ✅         | ✅    |
| GetTopicRuleDestination                | ✅         | ❌    |
| GetV2LoggingOptions                    | ❌         | ❌    |
| ListActiveViolations                   | ❌         | ❌    |
| ListAttachedPolicies                   | ✅         | ❌    |
| ListAuditFindings                      | ❌         | ❌    |
| ListAuditMitigationActionsExecutions   | ❌         | ❌    |
| ListAuditMitigationActionsTasks        | ✅         | ❌    |
| ListAuditSuppressions                  | ❌         | ❌    |
| ListAuditTasks                         | ✅         | ❌    |
| ListAuthorizers                        | ❌         | ❌    |
| ListBillingGroups                      | ❌         | ❌    |
| ListCACertificates                     | ❌         | ❌    |
| ListCertificates                       | ✅         | ❌    |
| ListCertificatesByCA                   | ✅         | ❌    |
| ListCustomMetrics                      | ❌         | ❌    |
| ListDetectMitigationActionsExecutions  | ✅         | ❌    |
| ListDetectMitigationActionsTasks       | ✅         | ❌    |
| ListDimensions                         | ❌         | ❌    |
| ListDomainConfigurations               | ✅         | ❌    |
| ListFleetMetrics                       | ❌         | ❌    |
| ListIndices                            | ❌         | ❌    |
| ListJobExecutionsForJob                | ✅         | ❌    |
| ListJobExecutionsForThing              | ✅         | ✅    |
| ListJobTemplates                       | ❌         | ❌    |
| ListJobs                               | ✅         | ✅    |
| ListManagedJobTemplates                | ❌         | ❌    |
| ListMetricValues                       | ✅         | ❌    |
| ListMitigationActions                  | ❌         | ❌    |
| ListOTAUpdates                         | ❌         | ❌    |
| ListOutgoingCertificates               | ❌         | ❌    |
| ListPolicies                           | ✅         | ✅    |
| ListPolicyPrincipals                   | ✅         | ❌    |
| ListPolicyVersions                     | ✅         | ❌    |
| ListPrincipalPolicies                  | ✅         | ❌    |
| ListPrincipalThings                    | ✅         | ❌    |
| ListProvisioningTemplateVersions       | ❌         | ❌    |
| ListProvisioningTemplates              | ❌         | ❌    |
| ListRoleAliases                        | ❌         | ❌    |
| ListScheduledAudits                    | ❌         | ❌    |
| ListSecurityProfiles                   | ❌         | ❌    |
| ListSecurityProfilesForTarget          | ❌         | ❌    |
| ListStreams                            | ❌         | ❌    |
| ListTagsForResource                    | ✅         | ✅    |
| ListTargetsForPolicy                   | ❌         | ❌    |
| ListTargetsForSecurityProfile          | ❌         | ❌    |
| ListThingGroups                        | ✅         | ✅    |
| ListThingGroupsForThing                | ✅         | ✅    |
| ListThingPrincipals                    | ✅         | ✅    |
| ListThingRegistrationTaskReports       | ❌         | ❌    |
| ListThingRegistrationTasks             | ❌         | ❌    |
| ListThingTypes                         | ✅         | ❌    |
| ListThings                             | ✅         | ✅    |
| ListThingsInBillingGroup               | ❌         | ❌    |
| ListThingsInThingGroup                 | ✅         | ✅    |
| ListTopicRuleDestinations              | ❌         | ❌    |
| ListTopicRules                         | ✅         | ✅    |
| ListV2LoggingLevels                    | ❌         | ❌    |
| ListViolationEvents                    | ✅         | ❌    |
| PutVerificationStateOnViolation        | ❌         | ❌    |
| RegisterCACertificate                  | ✅         | ❌    |
| RegisterCertificate                    | ✅         | ✅    |
| RegisterCertificateWithoutCA           | ✅         | ❌    |
| RegisterThing                          | ❌         | ❌    |
| RejectCertificateTransfer              | ❌         | ❌    |
| RemoveThingFromBillingGroup            | ❌         | ❌    |
| RemoveThingFromThingGroup              | ✅         | ✅    |
| ReplaceTopicRule                       | ✅         | ❌    |
| SearchIndex                            | ✅         | ✅    |
| SetDefaultAuthorizer                   | ❌         | ❌    |
| SetDefaultPolicyVersion                | ✅         | ❌    |
| SetLoggingOptions                      | ❌         | ❌    |
| SetV2LoggingLevel                      | ❌         | ❌    |
| SetV2LoggingOptions                    | ❌         | ❌    |
| StartAuditMitigationActionsTask        | ❌         | ❌    |
| StartDetectMitigationActionsTask       | ❌         | ❌    |
| StartOnDemandAuditTask                 | ❌         | ❌    |
| StartThingRegistrationTask             | ❌         | ❌    |
| StopThingRegistrationTask              | ❌         | ❌    |
| TagResource                            | ✅         | ✅    |
| TestAuthorization                      | ❌         | ❌    |
| TestInvokeAuthorizer                   | ❌         | ❌    |
| TransferCertificate                    | ❌         | ❌    |
| UntagResource                          | ❌         | ❌    |
| UpdateAccountAuditConfiguration        | ❌         | ❌    |
| UpdateAuditSuppression                 | ❌         | ❌    |
| UpdateAuthorizer                       | ❌         | ❌    |
| UpdateBillingGroup                     | ❌         | ❌    |
| UpdateCACertificate                    | ✅         | ❌    |
| UpdateCertificate                      | ✅         | ❌    |
| UpdateCustomMetric                     | ❌         | ❌    |
| UpdateDimension                        | ❌         | ❌    |
| UpdateDomainConfiguration              | ✅         | ❌    |
| UpdateDynamicThingGroup                | ✅         | ✅    |
| UpdateEventConfigurations              | ❌         | ❌    |
| UpdateFleetMetric                      | ❌         | ❌    |
| UpdateIndexingConfiguration            | ✅         | ✅    |
| UpdateJob                              | ❌         | ❌    |
| UpdateMitigationAction                 | ❌         | ❌    |
| UpdateProvisioningTemplate             | ❌         | ❌    |
| UpdateRoleAlias                        | ❌         | ❌    |
| UpdateScheduledAudit                   | ❌         | ❌    |
| UpdateSecurityProfile                  | ❌         | ❌    |
| UpdateStream                           | ❌         | ❌    |
| UpdateThing                            | ✅         | ❌    |
| UpdateThingGroup                       | ✅         | ❌    |
| UpdateThingGroupsForThing              | ✅         | ❌    |
| UpdateTopicRuleDestination             | ❌         | ❌    |
| ValidateSecurityProfileBehaviors       | ❌         | ❌    |



## iot-data ##

API returns a response for 57.1% of the operations.

| Operation                              | Implemented | Tested |
|----------------------------------------|-------------|--------|
| DeleteThingShadow                      | ✅         | ❌    |
| GetRetainedMessage                     | ❌         | ❌    |
| GetThingShadow                         | ✅         | ✅    |
| ListNamedShadowsForThing               | ❌         | ❌    |
| ListRetainedMessages                   | ❌         | ❌    |
| Publish                                | ✅         | ✅    |
| UpdateThingShadow                      | ✅         | ✅    |



## iotanalytics ##

API returns a response for 52.9% of the operations.

| Operation                              | Implemented | Tested |
|----------------------------------------|-------------|--------|
| BatchPutMessage                        | ❌         | ❌    |
| CancelPipelineReprocessing             | ❌         | ❌    |
| CreateChannel                          | ✅         | ✅    |
| CreateDataset                          | ✅         | ✅    |
| CreateDatasetContent                   | ❌         | ❌    |
| CreateDatastore                        | ✅         | ✅    |
| CreatePipeline                         | ✅         | ✅    |
| DeleteChannel                          | ✅         | ✅    |
| DeleteDataset                          | ✅         | ✅    |
| DeleteDatasetContent                   | ❌         | ❌    |
| DeleteDatastore                        | ✅         | ✅    |
| DeletePipeline                         | ✅         | ✅    |
| DescribeChannel                        | ✅         | ✅    |
| DescribeDataset                        | ✅         | ✅    |
| DescribeDatastore                      | ✅         | ✅    |
| DescribeLoggingOptions                 | ❌         | ❌    |
| DescribePipeline                       | ✅         | ✅    |
| GetDatasetContent                      | ❌         | ❌    |
| ListChannels                           | ✅         | ✅    |
| ListDatasetContents                    | ✅         | ❌    |
| ListDatasets                           | ✅         | ✅    |
| ListDatastores                         | ✅         | ✅    |
| ListPipelines                          | ✅         | ✅    |
| ListTagsForResource                    | ❌         | ❌    |
| PutLoggingOptions                      | ❌         | ❌    |
| RunPipelineActivity                    | ❌         | ❌    |
| SampleChannelData                      | ✅         | ❌    |
| StartPipelineReprocessing              | ❌         | ❌    |
| TagResource                            | ❌         | ❌    |
| UntagResource                          | ❌         | ❌    |
| UpdateChannel                          | ❌         | ❌    |
| UpdateDataset                          | ❌         | ❌    |
| UpdateDatastore                        | ❌         | ❌    |
| UpdatePipeline                         | ❌         | ❌    |



## iotwireless ##

API returns a response for 15.1% of the operations.

| Operation                              | Implemented | Tested |
|----------------------------------------|-------------|--------|
| AssociateAwsAccountWithPartnerAccount  | ❌         | ❌    |
| AssociateMulticastGroupWithFuotaTask   | ❌         | ❌    |
| AssociateWirelessDeviceWithFuotaTask   | ❌         | ❌    |
| AssociateWirelessDeviceWithMulticastGroup| ❌         | ❌    |
| AssociateWirelessDeviceWithThing       | ❌         | ❌    |
| AssociateWirelessGatewayWithCertificate| ❌         | ❌    |
| AssociateWirelessGatewayWithThing      | ❌         | ❌    |
| CancelMulticastGroupSession            | ❌         | ❌    |
| CreateDestination                      | ❌         | ❌    |
| CreateDeviceProfile                    | ✅         | ✅    |
| CreateFuotaTask                        | ❌         | ❌    |
| CreateMulticastGroup                   | ❌         | ❌    |
| CreateNetworkAnalyzerConfiguration     | ❌         | ❌    |
| CreateServiceProfile                   | ❌         | ❌    |
| CreateWirelessDevice                   | ✅         | ✅    |
| CreateWirelessGateway                  | ✅         | ✅    |
| CreateWirelessGatewayTask              | ❌         | ❌    |
| CreateWirelessGatewayTaskDefinition    | ❌         | ❌    |
| DeleteDestination                      | ❌         | ❌    |
| DeleteDeviceProfile                    | ✅         | ✅    |
| DeleteFuotaTask                        | ❌         | ❌    |
| DeleteMulticastGroup                   | ❌         | ❌    |
| DeleteNetworkAnalyzerConfiguration     | ❌         | ❌    |
| DeleteQueuedMessages                   | ❌         | ❌    |
| DeleteServiceProfile                   | ❌         | ❌    |
| DeleteWirelessDevice                   | ✅         | ✅    |
| DeleteWirelessGateway                  | ✅         | ✅    |
| DeleteWirelessGatewayTask              | ❌         | ❌    |
| DeleteWirelessGatewayTaskDefinition    | ❌         | ❌    |
| DisassociateAwsAccountFromPartnerAccount| ❌         | ❌    |
| DisassociateMulticastGroupFromFuotaTask| ❌         | ❌    |
| DisassociateWirelessDeviceFromFuotaTask| ❌         | ❌    |
| DisassociateWirelessDeviceFromMulticastGroup| ❌         | ❌    |
| DisassociateWirelessDeviceFromThing    | ❌         | ❌    |
| DisassociateWirelessGatewayFromCertificate| ❌         | ❌    |
| DisassociateWirelessGatewayFromThing   | ❌         | ❌    |
| GetDestination                         | ❌         | ❌    |
| GetDeviceProfile                       | ✅         | ✅    |
| GetEventConfigurationByResourceTypes   | ❌         | ❌    |
| GetFuotaTask                           | ❌         | ❌    |
| GetLogLevelsByResourceTypes            | ❌         | ❌    |
| GetMulticastGroup                      | ❌         | ❌    |
| GetMulticastGroupSession               | ❌         | ❌    |
| GetNetworkAnalyzerConfiguration        | ❌         | ❌    |
| GetPartnerAccount                      | ❌         | ❌    |
| GetResourceEventConfiguration          | ❌         | ❌    |
| GetResourceLogLevel                    | ❌         | ❌    |
| GetServiceEndpoint                     | ❌         | ❌    |
| GetServiceProfile                      | ❌         | ❌    |
| GetWirelessDevice                      | ✅         | ✅    |
| GetWirelessDeviceStatistics            | ❌         | ❌    |
| GetWirelessGateway                     | ✅         | ✅    |
| GetWirelessGatewayCertificate          | ❌         | ❌    |
| GetWirelessGatewayFirmwareInformation  | ❌         | ❌    |
| GetWirelessGatewayStatistics           | ❌         | ❌    |
| GetWirelessGatewayTask                 | ❌         | ❌    |
| GetWirelessGatewayTaskDefinition       | ❌         | ❌    |
| ListDestinations                       | ❌         | ❌    |
| ListDeviceProfiles                     | ✅         | ✅    |
| ListEventConfigurations                | ❌         | ❌    |
| ListFuotaTasks                         | ❌         | ❌    |
| ListMulticastGroups                    | ❌         | ❌    |
| ListMulticastGroupsByFuotaTask         | ❌         | ❌    |
| ListNetworkAnalyzerConfigurations      | ❌         | ❌    |
| ListPartnerAccounts                    | ❌         | ❌    |
| ListQueuedMessages                     | ❌         | ❌    |
| ListServiceProfiles                    | ❌         | ❌    |
| ListTagsForResource                    | ❌         | ❌    |
| ListWirelessDevices                    | ✅         | ✅    |
| ListWirelessGatewayTaskDefinitions     | ❌         | ❌    |
| ListWirelessGateways                   | ✅         | ✅    |
| PutResourceLogLevel                    | ❌         | ❌    |
| ResetAllResourceLogLevels              | ❌         | ❌    |
| ResetResourceLogLevel                  | ❌         | ❌    |
| SendDataToMulticastGroup               | ❌         | ❌    |
| SendDataToWirelessDevice               | ❌         | ❌    |
| StartBulkAssociateWirelessDeviceWithMulticastGroup| ❌         | ❌    |
| StartBulkDisassociateWirelessDeviceFromMulticastGroup| ❌         | ❌    |
| StartFuotaTask                         | ❌         | ❌    |
| StartMulticastGroupSession             | ❌         | ❌    |
| TagResource                            | ❌         | ❌    |
| TestWirelessDevice                     | ❌         | ❌    |
| UntagResource                          | ❌         | ❌    |
| UpdateDestination                      | ❌         | ❌    |
| UpdateEventConfigurationByResourceTypes| ❌         | ❌    |
| UpdateFuotaTask                        | ❌         | ❌    |
| UpdateLogLevelsByResourceTypes         | ❌         | ❌    |
| UpdateMulticastGroup                   | ❌         | ❌    |
| UpdateNetworkAnalyzerConfiguration     | ❌         | ❌    |
| UpdatePartnerAccount                   | ❌         | ❌    |
| UpdateResourceEventConfiguration       | ❌         | ❌    |
| UpdateWirelessDevice                   | ✅         | ❌    |
| UpdateWirelessGateway                  | ✅         | ❌    |



## kafka ##

API returns a response for 45.7% of the operations.

| Operation                              | Implemented | Tested |
|----------------------------------------|-------------|--------|
| BatchAssociateScramSecret              | ❌         | ❌    |
| BatchDisassociateScramSecret           | ❌         | ❌    |
| CreateCluster                          | ✅         | ✅    |
| CreateClusterV2                        | ❌         | ❌    |
| CreateConfiguration                    | ✅         | ✅    |
| DeleteCluster                          | ✅         | ✅    |
| DeleteConfiguration                    | ✅         | ✅    |
| DescribeCluster                        | ✅         | ✅    |
| DescribeClusterOperation               | ✅         | ❌    |
| DescribeClusterV2                      | ❌         | ❌    |
| DescribeConfiguration                  | ✅         | ✅    |
| DescribeConfigurationRevision          | ✅         | ✅    |
| GetBootstrapBrokers                    | ✅         | ✅    |
| GetCompatibleKafkaVersions             | ❌         | ❌    |
| ListClusterOperations                  | ❌         | ❌    |
| ListClusters                           | ✅         | ✅    |
| ListClustersV2                         | ❌         | ❌    |
| ListConfigurationRevisions             | ✅         | ✅    |
| ListConfigurations                     | ✅         | ✅    |
| ListKafkaVersions                      | ❌         | ❌    |
| ListNodes                              | ✅         | ✅    |
| ListScramSecrets                       | ❌         | ❌    |
| ListTagsForResource                    | ❌         | ❌    |
| RebootBroker                           | ❌         | ❌    |
| TagResource                            | ❌         | ❌    |
| UntagResource                          | ❌         | ❌    |
| UpdateBrokerCount                      | ❌         | ❌    |
| UpdateBrokerStorage                    | ❌         | ❌    |
| UpdateBrokerType                       | ❌         | ❌    |
| UpdateClusterConfiguration             | ✅         | ❌    |
| UpdateClusterKafkaVersion              | ✅         | ❌    |
| UpdateConfiguration                    | ✅         | ✅    |
| UpdateConnectivity                     | ❌         | ❌    |
| UpdateMonitoring                       | ❌         | ❌    |
| UpdateSecurity                         | ❌         | ❌    |



## kinesis ##

API returns a response for 100.0% of the operations.

| Operation                              | Implemented | Tested |
|----------------------------------------|-------------|--------|
| AddTagsToStream                        | ✅         | ❌    |
| CreateStream                           | ✅         | ✅    |
| DecreaseStreamRetentionPeriod          | ✅         | ❌    |
| DeleteStream                           | ✅         | ✅    |
| DeregisterStreamConsumer               | ✅         | ✅    |
| DescribeLimits                         | ✅         | ❌    |
| DescribeStream                         | ✅         | ✅    |
| DescribeStreamConsumer                 | ✅         | ✅    |
| DescribeStreamSummary                  | ✅         | ✅    |
| DisableEnhancedMonitoring              | ✅         | ❌    |
| EnableEnhancedMonitoring               | ✅         | ❌    |
| GetRecords                             | ✅         | ✅    |
| GetShardIterator                       | ✅         | ✅    |
| IncreaseStreamRetentionPeriod          | ✅         | ❌    |
| ListShards                             | ✅         | ✅    |
| ListStreamConsumers                    | ✅         | ✅    |
| ListStreams                            | ✅         | ✅    |
| ListTagsForStream                      | ✅         | ❌    |
| MergeShards                            | ✅         | ❌    |
| PutRecord                              | ✅         | ✅    |
| PutRecords                             | ✅         | ✅    |
| RegisterStreamConsumer                 | ✅         | ✅    |
| RemoveTagsFromStream                   | ✅         | ❌    |
| SplitShard                             | ✅         | ❌    |
| StartStreamEncryption                  | ✅         | ❌    |
| StopStreamEncryption                   | ✅         | ❌    |
| SubscribeToShard                       | ✅         | ✅    |
| UpdateShardCount                       | ✅         | ❌    |
| UpdateStreamMode                       | ✅         | ❌    |



## kinesisanalytics ##

API returns a response for 55.0% of the operations.

| Operation                              | Implemented | Tested |
|----------------------------------------|-------------|--------|
| AddApplicationCloudWatchLoggingOption  | ❌         | ❌    |
| AddApplicationInput                    | ❌         | ❌    |
| AddApplicationInputProcessingConfiguration| ✅         | ✅    |
| AddApplicationOutput                   | ✅         | ✅    |
| AddApplicationReferenceDataSource      | ❌         | ❌    |
| CreateApplication                      | ✅         | ✅    |
| DeleteApplication                      | ✅         | ✅    |
| DeleteApplicationCloudWatchLoggingOption| ❌         | ❌    |
| DeleteApplicationInputProcessingConfiguration| ✅         | ✅    |
| DeleteApplicationOutput                | ❌         | ❌    |
| DeleteApplicationReferenceDataSource   | ❌         | ❌    |
| DescribeApplication                    | ✅         | ✅    |
| DiscoverInputSchema                    | ❌         | ❌    |
| ListApplications                       | ✅         | ✅    |
| ListTagsForResource                    | ✅         | ✅    |
| StartApplication                       | ❌         | ❌    |
| StopApplication                        | ❌         | ❌    |
| TagResource                            | ✅         | ✅    |
| UntagResource                          | ✅         | ✅    |
| UpdateApplication                      | ✅         | ✅    |



## kinesisanalyticsv2 ##

API returns a response for 35.5% of the operations.

| Operation                              | Implemented | Tested |
|----------------------------------------|-------------|--------|
| AddApplicationCloudWatchLoggingOption  | ❌         | ❌    |
| AddApplicationInput                    | ❌         | ❌    |
| AddApplicationInputProcessingConfiguration| ✅         | ✅    |
| AddApplicationOutput                   | ✅         | ✅    |
| AddApplicationReferenceDataSource      | ❌         | ❌    |
| AddApplicationVpcConfiguration         | ❌         | ❌    |
| CreateApplication                      | ✅         | ✅    |
| CreateApplicationPresignedUrl          | ❌         | ❌    |
| CreateApplicationSnapshot              | ❌         | ❌    |
| DeleteApplication                      | ✅         | ✅    |
| DeleteApplicationCloudWatchLoggingOption| ❌         | ❌    |
| DeleteApplicationInputProcessingConfiguration| ✅         | ✅    |
| DeleteApplicationOutput                | ❌         | ❌    |
| DeleteApplicationReferenceDataSource   | ❌         | ❌    |
| DeleteApplicationSnapshot              | ❌         | ❌    |
| DeleteApplicationVpcConfiguration      | ❌         | ❌    |
| DescribeApplication                    | ✅         | ✅    |
| DescribeApplicationSnapshot            | ❌         | ❌    |
| DescribeApplicationVersion             | ❌         | ❌    |
| DiscoverInputSchema                    | ❌         | ❌    |
| ListApplicationSnapshots               | ❌         | ❌    |
| ListApplicationVersions                | ❌         | ❌    |
| ListApplications                       | ✅         | ✅    |
| ListTagsForResource                    | ✅         | ✅    |
| RollbackApplication                    | ❌         | ❌    |
| StartApplication                       | ❌         | ❌    |
| StopApplication                        | ❌         | ❌    |
| TagResource                            | ✅         | ✅    |
| UntagResource                          | ✅         | ✅    |
| UpdateApplication                      | ✅         | ✅    |
| UpdateApplicationMaintenanceConfiguration| ❌         | ❌    |



## kms ##

API returns a response for 76.0% of the operations.

| Operation                              | Implemented | Tested |
|----------------------------------------|-------------|--------|
| CancelKeyDeletion                      | ✅         | ❌    |
| ConnectCustomKeyStore                  | ❌         | ❌    |
| CreateAlias                            | ✅         | ✅    |
| CreateCustomKeyStore                   | ❌         | ❌    |
| CreateGrant                            | ✅         | ✅    |
| CreateKey                              | ✅         | ✅    |
| Decrypt                                | ✅         | ✅    |
| DeleteAlias                            | ✅         | ✅    |
| DeleteCustomKeyStore                   | ❌         | ❌    |
| DeleteImportedKeyMaterial              | ❌         | ❌    |
| DescribeCustomKeyStores                | ❌         | ❌    |
| DescribeKey                            | ✅         | ✅    |
| DisableKey                             | ✅         | ✅    |
| DisableKeyRotation                     | ✅         | ✅    |
| DisconnectCustomKeyStore               | ❌         | ❌    |
| EnableKey                              | ✅         | ✅    |
| EnableKeyRotation                      | ✅         | ❌    |
| Encrypt                                | ✅         | ✅    |
| GenerateDataKey                        | ✅         | ✅    |
| GenerateDataKeyPair                    | ✅         | ✅    |
| GenerateDataKeyPairWithoutPlaintext    | ✅         | ✅    |
| GenerateDataKeyWithoutPlaintext        | ✅         | ❌    |
| GenerateMac                            | ❌         | ❌    |
| GenerateRandom                         | ✅         | ❌    |
| GetKeyPolicy                           | ✅         | ✅    |
| GetKeyRotationStatus                   | ✅         | ✅    |
| GetParametersForImport                 | ✅         | ✅    |
| GetPublicKey                           | ✅         | ✅    |
| ImportKeyMaterial                      | ✅         | ✅    |
| ListAliases                            | ✅         | ✅    |
| ListGrants                             | ✅         | ✅    |
| ListKeyPolicies                        | ✅         | ❌    |
| ListKeys                               | ✅         | ✅    |
| ListResourceTags                       | ✅         | ✅    |
| ListRetirableGrants                    | ✅         | ❌    |
| PutKeyPolicy                           | ✅         | ❌    |
| ReEncrypt                              | ✅         | ❌    |
| ReplicateKey                           | ❌         | ❌    |
| RetireGrant                            | ✅         | ✅    |
| RevokeGrant                            | ✅         | ✅    |
| ScheduleKeyDeletion                    | ✅         | ✅    |
| Sign                                   | ✅         | ✅    |
| TagResource                            | ✅         | ❌    |
| UntagResource                          | ✅         | ❌    |
| UpdateAlias                            | ✅         | ❌    |
| UpdateCustomKeyStore                   | ❌         | ❌    |
| UpdateKeyDescription                   | ✅         | ❌    |
| UpdatePrimaryRegion                    | ❌         | ❌    |
| Verify                                 | ❌         | ❌    |
| VerifyMac                              | ❌         | ❌    |



## lakeformation ##

API returns a response for 20.5% of the operations.

| Operation                              | Implemented | Tested |
|----------------------------------------|-------------|--------|
| AddLFTagsToResource                    | ❌         | ❌    |
| BatchGrantPermissions                  | ❌         | ❌    |
| BatchRevokePermissions                 | ❌         | ❌    |
| CancelTransaction                      | ❌         | ❌    |
| CommitTransaction                      | ❌         | ❌    |
| CreateDataCellsFilter                  | ❌         | ❌    |
| CreateLFTag                            | ❌         | ❌    |
| DeleteDataCellsFilter                  | ❌         | ❌    |
| DeleteLFTag                            | ❌         | ❌    |
| DeleteObjectsOnCancel                  | ❌         | ❌    |
| DeregisterResource                     | ✅         | ❌    |
| DescribeResource                       | ✅         | ❌    |
| DescribeTransaction                    | ❌         | ❌    |
| ExtendTransaction                      | ❌         | ❌    |
| GetDataLakeSettings                    | ✅         | ❌    |
| GetEffectivePermissionsForPath         | ❌         | ❌    |
| GetLFTag                               | ❌         | ❌    |
| GetQueryState                          | ❌         | ❌    |
| GetQueryStatistics                     | ❌         | ❌    |
| GetResourceLFTags                      | ❌         | ❌    |
| GetTableObjects                        | ❌         | ❌    |
| GetTemporaryGluePartitionCredentials   | ❌         | ❌    |
| GetTemporaryGlueTableCredentials       | ❌         | ❌    |
| GetWorkUnitResults                     | ❌         | ❌    |
| GetWorkUnits                           | ❌         | ❌    |
| GrantPermissions                       | ✅         | ✅    |
| ListDataCellsFilter                    | ❌         | ❌    |
| ListLFTags                             | ❌         | ❌    |
| ListPermissions                        | ✅         | ✅    |
| ListResources                          | ✅         | ❌    |
| ListTableStorageOptimizers             | ❌         | ❌    |
| ListTransactions                       | ❌         | ❌    |
| PutDataLakeSettings                    | ✅         | ❌    |
| RegisterResource                       | ✅         | ❌    |
| RemoveLFTagsFromResource               | ❌         | ❌    |
| RevokePermissions                      | ✅         | ❌    |
| SearchDatabasesByLFTags                | ❌         | ❌    |
| SearchTablesByLFTags                   | ❌         | ❌    |
| StartQueryPlanning                     | ❌         | ❌    |
| StartTransaction                       | ❌         | ❌    |
| UpdateLFTag                            | ❌         | ❌    |
| UpdateResource                         | ❌         | ❌    |
| UpdateTableObjects                     | ❌         | ❌    |
| UpdateTableStorageOptimizer            | ❌         | ❌    |



## lambda ##

API returns a response for 77.8% of the operations.

| Operation                              | Implemented | Tested |
|----------------------------------------|-------------|--------|
| AddLayerVersionPermission              | ✅         | ❌    |
| AddPermission                          | ✅         | ✅    |
| CreateAlias                            | ✅         | ✅    |
| CreateCodeSigningConfig                | ✅         | ✅    |
| CreateEventSourceMapping               | ✅         | ✅    |
| CreateFunction                         | ✅         | ✅    |
| CreateFunctionUrlConfig                | ❌         | ❌    |
| DeleteAlias                            | ✅         | ❌    |
| DeleteCodeSigningConfig                | ✅         | ✅    |
| DeleteEventSourceMapping               | ✅         | ✅    |
| DeleteFunction                         | ✅         | ✅    |
| DeleteFunctionCodeSigningConfig        | ✅         | ✅    |
| DeleteFunctionConcurrency              | ✅         | ✅    |
| DeleteFunctionEventInvokeConfig        | ✅         | ✅    |
| DeleteFunctionUrlConfig                | ❌         | ❌    |
| DeleteLayerVersion                     | ✅         | ✅    |
| DeleteProvisionedConcurrencyConfig     | ❌         | ❌    |
| GetAccountSettings                     | ❌         | ❌    |
| GetAlias                               | ✅         | ❌    |
| GetCodeSigningConfig                   | ✅         | ✅    |
| GetEventSourceMapping                  | ✅         | ✅    |
| GetFunction                            | ✅         | ✅    |
| GetFunctionCodeSigningConfig           | ✅         | ✅    |
| GetFunctionConcurrency                 | ✅         | ✅    |
| GetFunctionConfiguration               | ✅         | ✅    |
| GetFunctionEventInvokeConfig           | ✅         | ✅    |
| GetFunctionUrlConfig                   | ❌         | ❌    |
| GetLayerVersion                        | ✅         | ✅    |
| GetLayerVersionByArn                   | ✅         | ❌    |
| GetLayerVersionPolicy                  | ✅         | ❌    |
| GetPolicy                              | ✅         | ✅    |
| GetProvisionedConcurrencyConfig        | ❌         | ❌    |
| Invoke                                 | ✅         | ✅    |
| InvokeAsync                            | ❌         | ❌    |
| ListAliases                            | ✅         | ✅    |
| ListCodeSigningConfigs                 | ✅         | ❌    |
| ListEventSourceMappings                | ✅         | ✅    |
| ListFunctionEventInvokeConfigs         | ❌         | ❌    |
| ListFunctionUrlConfigs                 | ❌         | ❌    |
| ListFunctions                          | ✅         | ✅    |
| ListFunctionsByCodeSigningConfig       | ❌         | ❌    |
| ListLayerVersions                      | ✅         | ✅    |
| ListLayers                             | ✅         | ✅    |
| ListProvisionedConcurrencyConfigs      | ❌         | ❌    |
| ListTags                               | ✅         | ❌    |
| ListVersionsByFunction                 | ✅         | ✅    |
| PublishLayerVersion                    | ✅         | ✅    |
| PublishVersion                         | ✅         | ❌    |
| PutFunctionCodeSigningConfig           | ✅         | ✅    |
| PutFunctionConcurrency                 | ✅         | ✅    |
| PutFunctionEventInvokeConfig           | ✅         | ✅    |
| PutProvisionedConcurrencyConfig        | ❌         | ❌    |
| RemoveLayerVersionPermission           | ❌         | ❌    |
| RemovePermission                       | ✅         | ✅    |
| TagResource                            | ✅         | ❌    |
| UntagResource                          | ✅         | ❌    |
| UpdateAlias                            | ✅         | ❌    |
| UpdateCodeSigningConfig                | ✅         | ✅    |
| UpdateEventSourceMapping               | ✅         | ✅    |
| UpdateFunctionCode                     | ✅         | ✅    |
| UpdateFunctionConfiguration            | ✅         | ✅    |
| UpdateFunctionEventInvokeConfig        | ✅         | ✅    |
| UpdateFunctionUrlConfig                | ❌         | ❌    |



## logs ##

API returns a response for 59.5% of the operations.

| Operation                              | Implemented | Tested |
|----------------------------------------|-------------|--------|
| AssociateKmsKey                        | ❌         | ❌    |
| CancelExportTask                       | ❌         | ❌    |
| CreateExportTask                       | ✅         | ❌    |
| CreateLogGroup                         | ✅         | ✅    |
| CreateLogStream                        | ✅         | ✅    |
| DeleteDestination                      | ❌         | ❌    |
| DeleteLogGroup                         | ✅         | ✅    |
| DeleteLogStream                        | ✅         | ✅    |
| DeleteMetricFilter                     | ✅         | ✅    |
| DeleteQueryDefinition                  | ❌         | ❌    |
| DeleteResourcePolicy                   | ✅         | ❌    |
| DeleteRetentionPolicy                  | ✅         | ❌    |
| DeleteSubscriptionFilter               | ✅         | ✅    |
| DescribeDestinations                   | ❌         | ❌    |
| DescribeExportTasks                    | ❌         | ❌    |
| DescribeLogGroups                      | ✅         | ✅    |
| DescribeLogStreams                     | ✅         | ✅    |
| DescribeMetricFilters                  | ✅         | ✅    |
| DescribeQueries                        | ❌         | ❌    |
| DescribeQueryDefinitions               | ❌         | ❌    |
| DescribeResourcePolicies               | ✅         | ❌    |
| DescribeSubscriptionFilters            | ✅         | ✅    |
| DisassociateKmsKey                     | ❌         | ❌    |
| FilterLogEvents                        | ✅         | ✅    |
| GetLogEvents                           | ✅         | ✅    |
| GetLogGroupFields                      | ❌         | ❌    |
| GetLogRecord                           | ❌         | ❌    |
| GetQueryResults                        | ❌         | ❌    |
| ListTagsLogGroup                       | ✅         | ✅    |
| PutDestination                         | ❌         | ❌    |
| PutDestinationPolicy                   | ❌         | ❌    |
| PutLogEvents                           | ✅         | ✅    |
| PutMetricFilter                        | ✅         | ✅    |
| PutQueryDefinition                     | ❌         | ❌    |
| PutResourcePolicy                      | ✅         | ✅    |
| PutRetentionPolicy                     | ✅         | ❌    |
| PutSubscriptionFilter                  | ✅         | ✅    |
| StartQuery                             | ✅         | ❌    |
| StopQuery                              | ❌         | ❌    |
| TagLogGroup                            | ✅         | ❌    |
| TestMetricFilter                       | ❌         | ❌    |
| UntagLogGroup                          | ✅         | ❌    |



## mediastore ##

API returns a response for 19.0% of the operations.

| Operation                              | Implemented | Tested |
|----------------------------------------|-------------|--------|
| CreateContainer                        | ✅         | ✅    |
| DeleteContainer                        | ✅         | ✅    |
| DeleteContainerPolicy                  | ❌         | ❌    |
| DeleteCorsPolicy                       | ❌         | ❌    |
| DeleteLifecyclePolicy                  | ❌         | ❌    |
| DeleteMetricPolicy                     | ❌         | ❌    |
| DescribeContainer                      | ✅         | ✅    |
| GetContainerPolicy                     | ❌         | ❌    |
| GetCorsPolicy                          | ❌         | ❌    |
| GetLifecyclePolicy                     | ❌         | ❌    |
| GetMetricPolicy                        | ❌         | ❌    |
| ListContainers                         | ✅         | ✅    |
| ListTagsForResource                    | ❌         | ❌    |
| PutContainerPolicy                     | ❌         | ❌    |
| PutCorsPolicy                          | ❌         | ❌    |
| PutLifecyclePolicy                     | ❌         | ❌    |
| PutMetricPolicy                        | ❌         | ❌    |
| StartAccessLogging                     | ❌         | ❌    |
| StopAccessLogging                      | ❌         | ❌    |
| TagResource                            | ❌         | ❌    |
| UntagResource                          | ❌         | ❌    |



## mediastore-data ##

API returns a response for 80.0% of the operations.

| Operation                              | Implemented | Tested |
|----------------------------------------|-------------|--------|
| DeleteObject                           | ✅         | ✅    |
| DescribeObject                         | ✅         | ✅    |
| GetObject                              | ✅         | ✅    |
| ListItems                              | ❌         | ❌    |
| PutObject                              | ✅         | ✅    |



## mwaa ##

API returns a response for 72.7% of the operations.

| Operation                              | Implemented | Tested |
|----------------------------------------|-------------|--------|
| CreateCliToken                         | ❌         | ❌    |
| CreateEnvironment                      | ✅         | ❌    |
| CreateWebLoginToken                    | ❌         | ❌    |
| DeleteEnvironment                      | ✅         | ❌    |
| GetEnvironment                         | ✅         | ❌    |
| ListEnvironments                       | ✅         | ✅    |
| ListTagsForResource                    | ✅         | ❌    |
| PublishMetrics                         | ❌         | ❌    |
| TagResource                            | ✅         | ❌    |
| UntagResource                          | ✅         | ❌    |
| UpdateEnvironment                      | ✅         | ❌    |



## neptune ##

API returns a response for 62.3% of the operations.

| Operation                              | Implemented | Tested |
|----------------------------------------|-------------|--------|
| AddRoleToDBCluster                     | ❌         | ❌    |
| AddSourceIdentifierToSubscription      | ❌         | ❌    |
| AddTagsToResource                      | ✅         | ❌    |
| ApplyPendingMaintenanceAction          | ❌         | ❌    |
| CopyDBClusterParameterGroup            | ❌         | ❌    |
| CopyDBClusterSnapshot                  | ✅         | ❌    |
| CopyDBParameterGroup                   | ❌         | ❌    |
| CreateDBCluster                        | ✅         | ❌    |
| CreateDBClusterEndpoint                | ✅         | ❌    |
| CreateDBClusterParameterGroup          | ✅         | ❌    |
| CreateDBClusterSnapshot                | ✅         | ❌    |
| CreateDBInstance                       | ✅         | ❌    |
| CreateDBParameterGroup                 | ✅         | ❌    |
| CreateDBSubnetGroup                    | ✅         | ❌    |
| CreateEventSubscription                | ✅         | ❌    |
| CreateGlobalCluster                    | ❌         | ❌    |
| DeleteDBCluster                        | ✅         | ❌    |
| DeleteDBClusterEndpoint                | ✅         | ❌    |
| DeleteDBClusterParameterGroup          | ✅         | ❌    |
| DeleteDBClusterSnapshot                | ✅         | ❌    |
| DeleteDBInstance                       | ✅         | ❌    |
| DeleteDBParameterGroup                 | ✅         | ❌    |
| DeleteDBSubnetGroup                    | ✅         | ❌    |
| DeleteEventSubscription                | ✅         | ❌    |
| DeleteGlobalCluster                    | ❌         | ❌    |
| DescribeDBClusterEndpoints             | ✅         | ❌    |
| DescribeDBClusterParameterGroups       | ✅         | ❌    |
| DescribeDBClusterParameters            | ✅         | ❌    |
| DescribeDBClusterSnapshotAttributes    | ❌         | ❌    |
| DescribeDBClusterSnapshots             | ✅         | ❌    |
| DescribeDBClusters                     | ✅         | ❌    |
| DescribeDBEngineVersions               | ✅         | ❌    |
| DescribeDBInstances                    | ✅         | ❌    |
| DescribeDBParameterGroups              | ✅         | ❌    |
| DescribeDBParameters                   | ✅         | ❌    |
| DescribeDBSubnetGroups                 | ✅         | ❌    |
| DescribeEngineDefaultClusterParameters | ❌         | ❌    |
| DescribeEngineDefaultParameters        | ❌         | ❌    |
| DescribeEventCategories                | ❌         | ❌    |
| DescribeEventSubscriptions             | ✅         | ❌    |
| DescribeEvents                         | ❌         | ❌    |
| DescribeGlobalClusters                 | ✅         | ❌    |
| DescribeOrderableDBInstanceOptions     | ❌         | ❌    |
| DescribePendingMaintenanceActions      | ❌         | ❌    |
| DescribeValidDBInstanceModifications   | ❌         | ❌    |
| FailoverDBCluster                      | ❌         | ❌    |
| FailoverGlobalCluster                  | ❌         | ❌    |
| ListTagsForResource                    | ✅         | ❌    |
| ModifyDBCluster                        | ✅         | ❌    |
| ModifyDBClusterEndpoint                | ✅         | ❌    |
| ModifyDBClusterParameterGroup          | ✅         | ❌    |
| ModifyDBClusterSnapshotAttribute       | ❌         | ❌    |
| ModifyDBInstance                       | ✅         | ❌    |
| ModifyDBParameterGroup                 | ✅         | ❌    |
| ModifyDBSubnetGroup                    | ✅         | ❌    |
| ModifyEventSubscription                | ❌         | ❌    |
| ModifyGlobalCluster                    | ❌         | ❌    |
| PromoteReadReplicaDBCluster            | ❌         | ❌    |
| RebootDBInstance                       | ✅         | ❌    |
| RemoveFromGlobalCluster                | ❌         | ❌    |
| RemoveRoleFromDBCluster                | ❌         | ❌    |
| RemoveSourceIdentifierFromSubscription | ❌         | ❌    |
| RemoveTagsFromResource                 | ✅         | ❌    |
| ResetDBClusterParameterGroup           | ✅         | ❌    |
| ResetDBParameterGroup                  | ❌         | ❌    |
| RestoreDBClusterFromSnapshot           | ✅         | ❌    |
| RestoreDBClusterToPointInTime          | ❌         | ❌    |
| StartDBCluster                         | ✅         | ❌    |
| StopDBCluster                          | ✅         | ❌    |



## opensearch ##

API returns a response for 30.0% of the operations.

| Operation                              | Implemented | Tested |
|----------------------------------------|-------------|--------|
| AcceptInboundConnection                | ❌         | ❌    |
| AddTags                                | ✅         | ✅    |
| AssociatePackage                       | ❌         | ❌    |
| CancelServiceSoftwareUpdate            | ❌         | ❌    |
| CreateDomain                           | ✅         | ✅    |
| CreateOutboundConnection               | ❌         | ❌    |
| CreatePackage                          | ❌         | ❌    |
| DeleteDomain                           | ✅         | ✅    |
| DeleteInboundConnection                | ❌         | ❌    |
| DeleteOutboundConnection               | ❌         | ❌    |
| DeletePackage                          | ❌         | ❌    |
| DescribeDomain                         | ✅         | ✅    |
| DescribeDomainAutoTunes                | ❌         | ❌    |
| DescribeDomainChangeProgress           | ❌         | ❌    |
| DescribeDomainConfig                   | ✅         | ✅    |
| DescribeDomains                        | ✅         | ✅    |
| DescribeInboundConnections             | ❌         | ❌    |
| DescribeInstanceTypeLimits             | ❌         | ❌    |
| DescribeOutboundConnections            | ❌         | ❌    |
| DescribePackages                       | ❌         | ❌    |
| DescribeReservedInstanceOfferings      | ❌         | ❌    |
| DescribeReservedInstances              | ❌         | ❌    |
| DissociatePackage                      | ❌         | ❌    |
| GetCompatibleVersions                  | ✅         | ✅    |
| GetPackageVersionHistory               | ❌         | ❌    |
| GetUpgradeHistory                      | ❌         | ❌    |
| GetUpgradeStatus                       | ❌         | ❌    |
| ListDomainNames                        | ✅         | ✅    |
| ListDomainsForPackage                  | ❌         | ❌    |
| ListInstanceTypeDetails                | ❌         | ❌    |
| ListPackagesForDomain                  | ❌         | ❌    |
| ListTags                               | ✅         | ✅    |
| ListVersions                           | ✅         | ✅    |
| PurchaseReservedInstanceOffering       | ❌         | ❌    |
| RejectInboundConnection                | ❌         | ❌    |
| RemoveTags                             | ✅         | ❌    |
| StartServiceSoftwareUpdate             | ❌         | ❌    |
| UpdateDomainConfig                     | ✅         | ✅    |
| UpdatePackage                          | ❌         | ❌    |
| UpgradeDomain                          | ❌         | ❌    |



## organizations ##

API returns a response for 76.9% of the operations.

| Operation                              | Implemented | Tested |
|----------------------------------------|-------------|--------|
| AcceptHandshake                        | ❌         | ❌    |
| AttachPolicy                           | ✅         | ❌    |
| CancelHandshake                        | ❌         | ❌    |
| CloseAccount                           | ✅         | ❌    |
| CreateAccount                          | ✅         | ✅    |
| CreateGovCloudAccount                  | ❌         | ❌    |
| CreateOrganization                     | ✅         | ✅    |
| CreateOrganizationalUnit               | ✅         | ❌    |
| CreatePolicy                           | ✅         | ❌    |
| DeclineHandshake                       | ❌         | ❌    |
| DeleteOrganization                     | ✅         | ✅    |
| DeleteOrganizationalUnit               | ❌         | ❌    |
| DeletePolicy                           | ✅         | ❌    |
| DeregisterDelegatedAdministrator       | ✅         | ❌    |
| DescribeAccount                        | ✅         | ✅    |
| DescribeCreateAccountStatus            | ✅         | ❌    |
| DescribeEffectivePolicy                | ❌         | ❌    |
| DescribeHandshake                      | ❌         | ❌    |
| DescribeOrganization                   | ✅         | ✅    |
| DescribeOrganizationalUnit             | ✅         | ❌    |
| DescribePolicy                         | ✅         | ❌    |
| DetachPolicy                           | ✅         | ❌    |
| DisableAWSServiceAccess                | ✅         | ❌    |
| DisablePolicyType                      | ✅         | ❌    |
| EnableAWSServiceAccess                 | ✅         | ❌    |
| EnableAllFeatures                      | ❌         | ❌    |
| EnablePolicyType                       | ✅         | ❌    |
| InviteAccountToOrganization            | ❌         | ❌    |
| LeaveOrganization                      | ❌         | ❌    |
| ListAWSServiceAccessForOrganization    | ✅         | ❌    |
| ListAccounts                           | ✅         | ❌    |
| ListAccountsForParent                  | ✅         | ❌    |
| ListChildren                           | ✅         | ❌    |
| ListCreateAccountStatus                | ✅         | ❌    |
| ListDelegatedAdministrators            | ✅         | ❌    |
| ListDelegatedServicesForAccount        | ✅         | ❌    |
| ListHandshakesForAccount               | ❌         | ❌    |
| ListHandshakesForOrganization          | ❌         | ❌    |
| ListOrganizationalUnitsForParent       | ✅         | ❌    |
| ListParents                            | ✅         | ❌    |
| ListPolicies                           | ✅         | ❌    |
| ListPoliciesForTarget                  | ✅         | ❌    |
| ListRoots                              | ✅         | ❌    |
| ListTagsForResource                    | ✅         | ❌    |
| ListTargetsForPolicy                   | ✅         | ❌    |
| MoveAccount                            | ✅         | ❌    |
| RegisterDelegatedAdministrator         | ✅         | ❌    |
| RemoveAccountFromOrganization          | ✅         | ❌    |
| TagResource                            | ✅         | ❌    |
| UntagResource                          | ✅         | ❌    |
| UpdateOrganizationalUnit               | ✅         | ❌    |
| UpdatePolicy                           | ✅         | ❌    |



## qldb ##

API returns a response for 60.0% of the operations.

| Operation                              | Implemented | Tested |
|----------------------------------------|-------------|--------|
| CancelJournalKinesisStream             | ❌         | ❌    |
| CreateLedger                           | ✅         | ✅    |
| DeleteLedger                           | ✅         | ✅    |
| DescribeJournalKinesisStream           | ✅         | ❌    |
| DescribeJournalS3Export                | ✅         | ❌    |
| DescribeLedger                         | ✅         | ✅    |
| ExportJournalToS3                      | ✅         | ❌    |
| GetBlock                               | ❌         | ❌    |
| GetDigest                              | ❌         | ❌    |
| GetRevision                            | ❌         | ❌    |
| ListJournalKinesisStreamsForLedger     | ❌         | ❌    |
| ListJournalS3Exports                   | ❌         | ❌    |
| ListJournalS3ExportsForLedger          | ❌         | ❌    |
| ListLedgers                            | ✅         | ✅    |
| ListTagsForResource                    | ✅         | ✅    |
| StreamJournalToKinesis                 | ✅         | ✅    |
| TagResource                            | ✅         | ❌    |
| UntagResource                          | ✅         | ❌    |
| UpdateLedger                           | ✅         | ✅    |
| UpdateLedgerPermissionsMode            | ❌         | ❌    |



## qldb-session ##

API returns a response for 100.0% of the operations.

| Operation                              | Implemented | Tested |
|----------------------------------------|-------------|--------|
| SendCommand                            | ✅         | ✅    |



## rds ##

API returns a response for 53.3% of the operations.

| Operation                              | Implemented | Tested |
|----------------------------------------|-------------|--------|
| AddRoleToDBCluster                     | ❌         | ❌    |
| AddRoleToDBInstance                    | ❌         | ❌    |
| AddSourceIdentifierToSubscription      | ❌         | ❌    |
| AddTagsToResource                      | ✅         | ✅    |
| ApplyPendingMaintenanceAction          | ❌         | ❌    |
| AuthorizeDBSecurityGroupIngress        | ✅         | ❌    |
| BacktrackDBCluster                     | ❌         | ❌    |
| CancelExportTask                       | ✅         | ❌    |
| CopyDBClusterParameterGroup            | ❌         | ❌    |
| CopyDBClusterSnapshot                  | ✅         | ❌    |
| CopyDBParameterGroup                   | ❌         | ❌    |
| CopyDBSnapshot                         | ✅         | ❌    |
| CopyOptionGroup                        | ❌         | ❌    |
| CreateCustomDBEngineVersion            | ❌         | ❌    |
| CreateDBCluster                        | ✅         | ✅    |
| CreateDBClusterEndpoint                | ✅         | ✅    |
| CreateDBClusterParameterGroup          | ✅         | ✅    |
| CreateDBClusterSnapshot                | ✅         | ✅    |
| CreateDBInstance                       | ✅         | ✅    |
| CreateDBInstanceReadReplica            | ✅         | ❌    |
| CreateDBParameterGroup                 | ✅         | ✅    |
| CreateDBProxy                          | ✅         | ✅    |
| CreateDBProxyEndpoint                  | ❌         | ❌    |
| CreateDBSecurityGroup                  | ✅         | ❌    |
| CreateDBSnapshot                       | ✅         | ✅    |
| CreateDBSubnetGroup                    | ✅         | ✅    |
| CreateEventSubscription                | ✅         | ❌    |
| CreateGlobalCluster                    | ❌         | ❌    |
| CreateOptionGroup                      | ✅         | ❌    |
| DeleteCustomDBEngineVersion            | ❌         | ❌    |
| DeleteDBCluster                        | ✅         | ✅    |
| DeleteDBClusterEndpoint                | ✅         | ✅    |
| DeleteDBClusterParameterGroup          | ✅         | ✅    |
| DeleteDBClusterSnapshot                | ✅         | ✅    |
| DeleteDBInstance                       | ✅         | ✅    |
| DeleteDBInstanceAutomatedBackup        | ❌         | ❌    |
| DeleteDBParameterGroup                 | ✅         | ✅    |
| DeleteDBProxy                          | ✅         | ✅    |
| DeleteDBProxyEndpoint                  | ❌         | ❌    |
| DeleteDBSecurityGroup                  | ✅         | ❌    |
| DeleteDBSnapshot                       | ✅         | ❌    |
| DeleteDBSubnetGroup                    | ✅         | ✅    |
| DeleteEventSubscription                | ✅         | ❌    |
| DeleteGlobalCluster                    | ❌         | ❌    |
| DeleteOptionGroup                      | ✅         | ❌    |
| DeregisterDBProxyTargets               | ✅         | ✅    |
| DescribeAccountAttributes              | ❌         | ❌    |
| DescribeCertificates                   | ✅         | ❌    |
| DescribeDBClusterBacktracks            | ❌         | ❌    |
| DescribeDBClusterEndpoints             | ✅         | ✅    |
| DescribeDBClusterParameterGroups       | ✅         | ✅    |
| DescribeDBClusterParameters            | ✅         | ✅    |
| DescribeDBClusterSnapshotAttributes    | ❌         | ❌    |
| DescribeDBClusterSnapshots             | ✅         | ✅    |
| DescribeDBClusters                     | ✅         | ✅    |
| DescribeDBEngineVersions               | ✅         | ✅    |
| DescribeDBInstanceAutomatedBackups     | ❌         | ❌    |
| DescribeDBInstances                    | ✅         | ✅    |
| DescribeDBLogFiles                     | ❌         | ❌    |
| DescribeDBParameterGroups              | ✅         | ✅    |
| DescribeDBParameters                   | ✅         | ✅    |
| DescribeDBProxies                      | ✅         | ✅    |
| DescribeDBProxyEndpoints               | ❌         | ❌    |
| DescribeDBProxyTargetGroups            | ❌         | ❌    |
| DescribeDBProxyTargets                 | ✅         | ✅    |
| DescribeDBSecurityGroups               | ✅         | ❌    |
| DescribeDBSnapshotAttributes           | ❌         | ❌    |
| DescribeDBSnapshots                    | ✅         | ✅    |
| DescribeDBSubnetGroups                 | ✅         | ✅    |
| DescribeEngineDefaultClusterParameters | ❌         | ❌    |
| DescribeEngineDefaultParameters        | ❌         | ❌    |
| DescribeEventCategories                | ❌         | ❌    |
| DescribeEventSubscriptions             | ✅         | ❌    |
| DescribeEvents                         | ❌         | ❌    |
| DescribeExportTasks                    | ✅         | ❌    |
| DescribeGlobalClusters                 | ✅         | ❌    |
| DescribeOptionGroupOptions             | ✅         | ❌    |
| DescribeOptionGroups                   | ✅         | ❌    |
| DescribeOrderableDBInstanceOptions     | ❌         | ❌    |
| DescribePendingMaintenanceActions      | ❌         | ❌    |
| DescribeReservedDBInstances            | ❌         | ❌    |
| DescribeReservedDBInstancesOfferings   | ❌         | ❌    |
| DescribeSourceRegions                  | ❌         | ❌    |
| DescribeValidDBInstanceModifications   | ❌         | ❌    |
| DownloadDBLogFilePortion               | ❌         | ❌    |
| FailoverDBCluster                      | ❌         | ❌    |
| FailoverGlobalCluster                  | ❌         | ❌    |
| ListTagsForResource                    | ✅         | ✅    |
| ModifyCertificates                     | ✅         | ❌    |
| ModifyCurrentDBClusterCapacity         | ✅         | ❌    |
| ModifyCustomDBEngineVersion            | ❌         | ❌    |
| ModifyDBCluster                        | ✅         | ✅    |
| ModifyDBClusterEndpoint                | ✅         | ✅    |
| ModifyDBClusterParameterGroup          | ✅         | ✅    |
| ModifyDBClusterSnapshotAttribute       | ❌         | ❌    |
| ModifyDBInstance                       | ✅         | ✅    |
| ModifyDBParameterGroup                 | ✅         | ✅    |
| ModifyDBProxy                          | ❌         | ❌    |
| ModifyDBProxyEndpoint                  | ❌         | ❌    |
| ModifyDBProxyTargetGroup               | ❌         | ❌    |
| ModifyDBSnapshot                       | ❌         | ❌    |
| ModifyDBSnapshotAttribute              | ❌         | ❌    |
| ModifyDBSubnetGroup                    | ✅         | ❌    |
| ModifyEventSubscription                | ❌         | ❌    |
| ModifyGlobalCluster                    | ❌         | ❌    |
| ModifyOptionGroup                      | ✅         | ❌    |
| PromoteReadReplica                     | ❌         | ❌    |
| PromoteReadReplicaDBCluster            | ❌         | ❌    |
| PurchaseReservedDBInstancesOffering    | ❌         | ❌    |
| RebootDBCluster                        | ❌         | ❌    |
| RebootDBInstance                       | ✅         | ❌    |
| RegisterDBProxyTargets                 | ✅         | ✅    |
| RemoveFromGlobalCluster                | ❌         | ❌    |
| RemoveRoleFromDBCluster                | ❌         | ❌    |
| RemoveRoleFromDBInstance               | ❌         | ❌    |
| RemoveSourceIdentifierFromSubscription | ❌         | ❌    |
| RemoveTagsFromResource                 | ✅         | ✅    |
| ResetDBClusterParameterGroup           | ✅         | ❌    |
| ResetDBParameterGroup                  | ❌         | ❌    |
| RestoreDBClusterFromS3                 | ❌         | ❌    |
| RestoreDBClusterFromSnapshot           | ✅         | ✅    |
| RestoreDBClusterToPointInTime          | ❌         | ❌    |
| RestoreDBInstanceFromDBSnapshot        | ✅         | ✅    |
| RestoreDBInstanceFromS3                | ❌         | ❌    |
| RestoreDBInstanceToPointInTime         | ❌         | ❌    |
| RevokeDBSecurityGroupIngress           | ❌         | ❌    |
| StartActivityStream                    | ❌         | ❌    |
| StartDBCluster                         | ✅         | ❌    |
| StartDBInstance                        | ✅         | ❌    |
| StartDBInstanceAutomatedBackupsReplication| ❌         | ❌    |
| StartExportTask                        | ✅         | ❌    |
| StopActivityStream                     | ❌         | ❌    |
| StopDBCluster                          | ✅         | ❌    |
| StopDBInstance                         | ✅         | ❌    |
| StopDBInstanceAutomatedBackupsReplication| ❌         | ❌    |



## rds-data ##

API returns a response for 66.7% of the operations.

| Operation                              | Implemented | Tested |
|----------------------------------------|-------------|--------|
| BatchExecuteStatement                  | ❌         | ❌    |
| BeginTransaction                       | ✅         | ✅    |
| CommitTransaction                      | ✅         | ✅    |
| ExecuteSql                             | ✅         | ✅    |
| ExecuteStatement                       | ✅         | ✅    |
| RollbackTransaction                    | ❌         | ❌    |



## redshift ##

API returns a response for 26.9% of the operations.

| Operation                              | Implemented | Tested |
|----------------------------------------|-------------|--------|
| AcceptReservedNodeExchange             | ❌         | ❌    |
| AddPartner                             | ❌         | ❌    |
| AssociateDataShareConsumer             | ❌         | ❌    |
| AuthorizeClusterSecurityGroupIngress   | ✅         | ❌    |
| AuthorizeDataShare                     | ❌         | ❌    |
| AuthorizeEndpointAccess                | ❌         | ❌    |
| AuthorizeSnapshotAccess                | ❌         | ❌    |
| BatchDeleteClusterSnapshots            | ❌         | ❌    |
| BatchModifyClusterSnapshots            | ❌         | ❌    |
| CancelResize                           | ❌         | ❌    |
| CopyClusterSnapshot                    | ❌         | ❌    |
| CreateAuthenticationProfile            | ❌         | ❌    |
| CreateCluster                          | ✅         | ✅    |
| CreateClusterParameterGroup            | ✅         | ✅    |
| CreateClusterSecurityGroup             | ✅         | ❌    |
| CreateClusterSnapshot                  | ✅         | ❌    |
| CreateClusterSubnetGroup               | ✅         | ❌    |
| CreateEndpointAccess                   | ❌         | ❌    |
| CreateEventSubscription                | ❌         | ❌    |
| CreateHsmClientCertificate             | ❌         | ❌    |
| CreateHsmConfiguration                 | ❌         | ❌    |
| CreateScheduledAction                  | ❌         | ❌    |
| CreateSnapshotCopyGrant                | ✅         | ❌    |
| CreateSnapshotSchedule                 | ❌         | ❌    |
| CreateTags                             | ✅         | ❌    |
| CreateUsageLimit                       | ❌         | ❌    |
| DeauthorizeDataShare                   | ❌         | ❌    |
| DeleteAuthenticationProfile            | ❌         | ❌    |
| DeleteCluster                          | ✅         | ✅    |
| DeleteClusterParameterGroup            | ✅         | ❌    |
| DeleteClusterSecurityGroup             | ✅         | ❌    |
| DeleteClusterSnapshot                  | ✅         | ❌    |
| DeleteClusterSubnetGroup               | ✅         | ❌    |
| DeleteEndpointAccess                   | ❌         | ❌    |
| DeleteEventSubscription                | ❌         | ❌    |
| DeleteHsmClientCertificate             | ❌         | ❌    |
| DeleteHsmConfiguration                 | ❌         | ❌    |
| DeletePartner                          | ❌         | ❌    |
| DeleteScheduledAction                  | ❌         | ❌    |
| DeleteSnapshotCopyGrant                | ✅         | ❌    |
| DeleteSnapshotSchedule                 | ❌         | ❌    |
| DeleteTags                             | ✅         | ❌    |
| DeleteUsageLimit                       | ❌         | ❌    |
| DescribeAccountAttributes              | ❌         | ❌    |
| DescribeAuthenticationProfiles         | ❌         | ❌    |
| DescribeClusterDbRevisions             | ❌         | ❌    |
| DescribeClusterParameterGroups         | ✅         | ✅    |
| DescribeClusterParameters              | ✅         | ✅    |
| DescribeClusterSecurityGroups          | ✅         | ❌    |
| DescribeClusterSnapshots               | ✅         | ❌    |
| DescribeClusterSubnetGroups            | ✅         | ❌    |
| DescribeClusterTracks                  | ❌         | ❌    |
| DescribeClusterVersions                | ❌         | ❌    |
| DescribeClusters                       | ✅         | ✅    |
| DescribeDataShares                     | ❌         | ❌    |
| DescribeDataSharesForConsumer          | ❌         | ❌    |
| DescribeDataSharesForProducer          | ❌         | ❌    |
| DescribeDefaultClusterParameters       | ✅         | ✅    |
| DescribeEndpointAccess                 | ❌         | ❌    |
| DescribeEndpointAuthorization          | ❌         | ❌    |
| DescribeEventCategories                | ❌         | ❌    |
| DescribeEventSubscriptions             | ❌         | ❌    |
| DescribeEvents                         | ❌         | ❌    |
| DescribeHsmClientCertificates          | ❌         | ❌    |
| DescribeHsmConfigurations              | ❌         | ❌    |
| DescribeLoggingStatus                  | ❌         | ❌    |
| DescribeNodeConfigurationOptions       | ❌         | ❌    |
| DescribeOrderableClusterOptions        | ❌         | ❌    |
| DescribePartners                       | ❌         | ❌    |
| DescribeReservedNodeExchangeStatus     | ❌         | ❌    |
| DescribeReservedNodeOfferings          | ❌         | ❌    |
| DescribeReservedNodes                  | ❌         | ❌    |
| DescribeResize                         | ❌         | ❌    |
| DescribeScheduledActions               | ❌         | ❌    |
| DescribeSnapshotCopyGrants             | ✅         | ❌    |
| DescribeSnapshotSchedules              | ❌         | ❌    |
| DescribeStorage                        | ❌         | ❌    |
| DescribeTableRestoreStatus             | ❌         | ❌    |
| DescribeTags                           | ✅         | ❌    |
| DescribeUsageLimits                    | ❌         | ❌    |
| DisableLogging                         | ❌         | ❌    |
| DisableSnapshotCopy                    | ✅         | ❌    |
| DisassociateDataShareConsumer          | ❌         | ❌    |
| EnableLogging                          | ❌         | ❌    |
| EnableSnapshotCopy                     | ✅         | ❌    |
| GetClusterCredentials                  | ✅         | ❌    |
| GetClusterCredentialsWithIAM           | ❌         | ❌    |
| GetReservedNodeExchangeConfigurationOptions| ❌         | ❌    |
| GetReservedNodeExchangeOfferings       | ❌         | ❌    |
| ModifyAquaConfiguration                | ❌         | ❌    |
| ModifyAuthenticationProfile            | ❌         | ❌    |
| ModifyCluster                          | ✅         | ❌    |
| ModifyClusterDbRevision                | ❌         | ❌    |
| ModifyClusterIamRoles                  | ❌         | ❌    |
| ModifyClusterMaintenance               | ❌         | ❌    |
| ModifyClusterParameterGroup            | ❌         | ❌    |
| ModifyClusterSnapshot                  | ❌         | ❌    |
| ModifyClusterSnapshotSchedule          | ❌         | ❌    |
| ModifyClusterSubnetGroup               | ❌         | ❌    |
| ModifyEndpointAccess                   | ❌         | ❌    |
| ModifyEventSubscription                | ❌         | ❌    |
| ModifyScheduledAction                  | ❌         | ❌    |
| ModifySnapshotCopyRetentionPeriod      | ✅         | ❌    |
| ModifySnapshotSchedule                 | ❌         | ❌    |
| ModifyUsageLimit                       | ❌         | ❌    |
| PauseCluster                           | ✅         | ❌    |
| PurchaseReservedNodeOffering           | ❌         | ❌    |
| RebootCluster                          | ❌         | ❌    |
| RejectDataShare                        | ❌         | ❌    |
| ResetClusterParameterGroup             | ❌         | ❌    |
| ResizeCluster                          | ❌         | ❌    |
| RestoreFromClusterSnapshot             | ✅         | ❌    |
| RestoreTableFromClusterSnapshot        | ❌         | ❌    |
| ResumeCluster                          | ✅         | ❌    |
| RevokeClusterSecurityGroupIngress      | ❌         | ❌    |
| RevokeEndpointAccess                   | ❌         | ❌    |
| RevokeSnapshotAccess                   | ❌         | ❌    |
| RotateEncryptionKey                    | ❌         | ❌    |
| UpdatePartnerStatus                    | ❌         | ❌    |



## redshift-data ##

API returns a response for 50.0% of the operations.

| Operation                              | Implemented | Tested |
|----------------------------------------|-------------|--------|
| BatchExecuteStatement                  | ❌         | ❌    |
| CancelStatement                        | ❌         | ❌    |
| DescribeStatement                      | ✅         | ✅    |
| DescribeTable                          | ✅         | ✅    |
| ExecuteStatement                       | ✅         | ✅    |
| GetStatementResult                     | ✅         | ✅    |
| ListDatabases                          | ✅         | ✅    |
| ListSchemas                            | ❌         | ❌    |
| ListStatements                         | ❌         | ❌    |
| ListTables                             | ❌         | ❌    |



## resource-groups ##

API returns a response for 87.5% of the operations.

| Operation                              | Implemented | Tested |
|----------------------------------------|-------------|--------|
| CreateGroup                            | ✅         | ✅    |
| DeleteGroup                            | ✅         | ✅    |
| GetGroup                               | ✅         | ✅    |
| GetGroupConfiguration                  | ✅         | ❌    |
| GetGroupQuery                          | ✅         | ❌    |
| GetTags                                | ✅         | ❌    |
| GroupResources                         | ✅         | ❌    |
| ListGroupResources                     | ✅         | ❌    |
| ListGroups                             | ✅         | ✅    |
| PutGroupConfiguration                  | ✅         | ❌    |
| SearchResources                        | ✅         | ❌    |
| Tag                                    | ❌         | ❌    |
| UngroupResources                       | ✅         | ❌    |
| Untag                                  | ❌         | ❌    |
| UpdateGroup                            | ✅         | ❌    |
| UpdateGroupQuery                       | ✅         | ❌    |



## resourcegroupstaggingapi ##

API returns a response for 37.5% of the operations.

| Operation                              | Implemented | Tested |
|----------------------------------------|-------------|--------|
| DescribeReportCreation                 | ❌         | ❌    |
| GetComplianceSummary                   | ❌         | ❌    |
| GetResources                           | ✅         | ✅    |
| GetTagKeys                             | ✅         | ❌    |
| GetTagValues                           | ✅         | ❌    |
| StartReportCreation                    | ❌         | ❌    |
| TagResources                           | ❌         | ❌    |
| UntagResources                         | ❌         | ❌    |



## route53 ##

API returns a response for 100.0% of the operations.

| Operation                              | Implemented | Tested |
|----------------------------------------|-------------|--------|
| ActivateKeySigningKey                  | ✅         | ❌    |
| AssociateVPCWithHostedZone             | ✅         | ✅    |
| ChangeCidrCollection                   | ✅         | ❌    |
| ChangeResourceRecordSets               | ✅         | ✅    |
| ChangeTagsForResource                  | ✅         | ✅    |
| CreateCidrCollection                   | ✅         | ❌    |
| CreateHealthCheck                      | ✅         | ✅    |
| CreateHostedZone                       | ✅         | ✅    |
| CreateKeySigningKey                    | ✅         | ❌    |
| CreateQueryLoggingConfig               | ✅         | ❌    |
| CreateReusableDelegationSet            | ✅         | ✅    |
| CreateTrafficPolicy                    | ✅         | ❌    |
| CreateTrafficPolicyInstance            | ✅         | ❌    |
| CreateTrafficPolicyVersion             | ✅         | ❌    |
| CreateVPCAssociationAuthorization      | ✅         | ❌    |
| DeactivateKeySigningKey                | ✅         | ❌    |
| DeleteCidrCollection                   | ✅         | ❌    |
| DeleteHealthCheck                      | ✅         | ✅    |
| DeleteHostedZone                       | ✅         | ✅    |
| DeleteKeySigningKey                    | ✅         | ❌    |
| DeleteQueryLoggingConfig               | ✅         | ❌    |
| DeleteReusableDelegationSet            | ✅         | ✅    |
| DeleteTrafficPolicy                    | ✅         | ❌    |
| DeleteTrafficPolicyInstance            | ✅         | ❌    |
| DeleteVPCAssociationAuthorization      | ✅         | ❌    |
| DisableHostedZoneDNSSEC                | ✅         | ❌    |
| DisassociateVPCFromHostedZone          | ✅         | ✅    |
| EnableHostedZoneDNSSEC                 | ✅         | ❌    |
| GetAccountLimit                        | ✅         | ❌    |
| GetChange                              | ✅         | ✅    |
| GetCheckerIpRanges                     | ✅         | ❌    |
| GetDNSSEC                              | ✅         | ❌    |
| GetGeoLocation                         | ✅         | ❌    |
| GetHealthCheck                         | ✅         | ✅    |
| GetHealthCheckCount                    | ✅         | ❌    |
| GetHealthCheckLastFailureReason        | ✅         | ❌    |
| GetHealthCheckStatus                   | ✅         | ❌    |
| GetHostedZone                          | ✅         | ✅    |
| GetHostedZoneCount                     | ✅         | ❌    |
| GetHostedZoneLimit                     | ✅         | ❌    |
| GetQueryLoggingConfig                  | ✅         | ❌    |
| GetReusableDelegationSet               | ✅         | ✅    |
| GetReusableDelegationSetLimit          | ✅         | ❌    |
| GetTrafficPolicy                       | ✅         | ❌    |
| GetTrafficPolicyInstance               | ✅         | ❌    |
| GetTrafficPolicyInstanceCount          | ✅         | ❌    |
| ListCidrBlocks                         | ✅         | ❌    |
| ListCidrCollections                    | ✅         | ❌    |
| ListCidrLocations                      | ✅         | ❌    |
| ListGeoLocations                       | ✅         | ❌    |
| ListHealthChecks                       | ✅         | ❌    |
| ListHostedZones                        | ✅         | ✅    |
| ListHostedZonesByName                  | ✅         | ✅    |
| ListHostedZonesByVPC                   | ✅         | ✅    |
| ListQueryLoggingConfigs                | ✅         | ❌    |
| ListResourceRecordSets                 | ✅         | ✅    |
| ListReusableDelegationSets             | ✅         | ✅    |
| ListTagsForResource                    | ✅         | ✅    |
| ListTagsForResources                   | ✅         | ❌    |
| ListTrafficPolicies                    | ✅         | ❌    |
| ListTrafficPolicyInstances             | ✅         | ❌    |
| ListTrafficPolicyInstancesByHostedZone | ✅         | ❌    |
| ListTrafficPolicyInstancesByPolicy     | ✅         | ❌    |
| ListTrafficPolicyVersions              | ✅         | ❌    |
| ListVPCAssociationAuthorizations       | ✅         | ❌    |
| TestDNSAnswer                          | ✅         | ❌    |
| UpdateHealthCheck                      | ✅         | ❌    |
| UpdateHostedZoneComment                | ✅         | ❌    |
| UpdateTrafficPolicyComment             | ✅         | ❌    |
| UpdateTrafficPolicyInstance            | ✅         | ❌    |



## route53resolver ##

API returns a response for 27.0% of the operations.

| Operation                              | Implemented | Tested |
|----------------------------------------|-------------|--------|
| AssociateFirewallRuleGroup             | ❌         | ❌    |
| AssociateResolverEndpointIpAddress     | ❌         | ❌    |
| AssociateResolverQueryLogConfig        | ❌         | ❌    |
| AssociateResolverRule                  | ✅         | ❌    |
| CreateFirewallDomainList               | ❌         | ❌    |
| CreateFirewallRule                     | ❌         | ❌    |
| CreateFirewallRuleGroup                | ❌         | ❌    |
| CreateResolverEndpoint                 | ✅         | ✅    |
| CreateResolverQueryLogConfig           | ❌         | ❌    |
| CreateResolverRule                     | ✅         | ❌    |
| DeleteFirewallDomainList               | ❌         | ❌    |
| DeleteFirewallRule                     | ❌         | ❌    |
| DeleteFirewallRuleGroup                | ❌         | ❌    |
| DeleteResolverEndpoint                 | ✅         | ❌    |
| DeleteResolverQueryLogConfig           | ❌         | ❌    |
| DeleteResolverRule                     | ✅         | ❌    |
| DisassociateFirewallRuleGroup          | ❌         | ❌    |
| DisassociateResolverEndpointIpAddress  | ❌         | ❌    |
| DisassociateResolverQueryLogConfig     | ❌         | ❌    |
| DisassociateResolverRule               | ✅         | ❌    |
| GetFirewallConfig                      | ❌         | ❌    |
| GetFirewallDomainList                  | ❌         | ❌    |
| GetFirewallRuleGroup                   | ❌         | ❌    |
| GetFirewallRuleGroupAssociation        | ❌         | ❌    |
| GetFirewallRuleGroupPolicy             | ❌         | ❌    |
| GetResolverConfig                      | ❌         | ❌    |
| GetResolverDnssecConfig                | ❌         | ❌    |
| GetResolverEndpoint                    | ✅         | ❌    |
| GetResolverQueryLogConfig              | ❌         | ❌    |
| GetResolverQueryLogConfigAssociation   | ❌         | ❌    |
| GetResolverQueryLogConfigPolicy        | ❌         | ❌    |
| GetResolverRule                        | ✅         | ❌    |
| GetResolverRuleAssociation             | ✅         | ❌    |
| GetResolverRulePolicy                  | ❌         | ❌    |
| ImportFirewallDomains                  | ❌         | ❌    |
| ListFirewallConfigs                    | ❌         | ❌    |
| ListFirewallDomainLists                | ❌         | ❌    |
| ListFirewallDomains                    | ❌         | ❌    |
| ListFirewallRuleGroupAssociations      | ❌         | ❌    |
| ListFirewallRuleGroups                 | ❌         | ❌    |
| ListFirewallRules                      | ❌         | ❌    |
| ListResolverConfigs                    | ❌         | ❌    |
| ListResolverDnssecConfigs              | ❌         | ❌    |
| ListResolverEndpointIpAddresses        | ✅         | ❌    |
| ListResolverEndpoints                  | ✅         | ❌    |
| ListResolverQueryLogConfigAssociations | ❌         | ❌    |
| ListResolverQueryLogConfigs            | ❌         | ❌    |
| ListResolverRuleAssociations           | ✅         | ❌    |
| ListResolverRules                      | ✅         | ❌    |
| ListTagsForResource                    | ✅         | ❌    |
| PutFirewallRuleGroupPolicy             | ❌         | ❌    |
| PutResolverQueryLogConfigPolicy        | ❌         | ❌    |
| PutResolverRulePolicy                  | ❌         | ❌    |
| TagResource                            | ✅         | ❌    |
| UntagResource                          | ✅         | ❌    |
| UpdateFirewallConfig                   | ❌         | ❌    |
| UpdateFirewallDomains                  | ❌         | ❌    |
| UpdateFirewallRule                     | ❌         | ❌    |
| UpdateFirewallRuleGroupAssociation     | ❌         | ❌    |
| UpdateResolverConfig                   | ❌         | ❌    |
| UpdateResolverDnssecConfig             | ❌         | ❌    |
| UpdateResolverEndpoint                 | ✅         | ❌    |
| UpdateResolverRule                     | ❌         | ❌    |



## s3 ##

API returns a response for 100.0% of the operations.

| Operation                              | Implemented | Tested |
|----------------------------------------|-------------|--------|
| AbortMultipartUpload                   | ✅         | ❌    |
| CompleteMultipartUpload                | ✅         | ✅    |
| CopyObject                             | ✅         | ✅    |
| CreateBucket                           | ✅         | ✅    |
| CreateMultipartUpload                  | ✅         | ✅    |
| DeleteBucket                           | ✅         | ✅    |
| DeleteBucketAnalyticsConfiguration     | ✅         | ❌    |
| DeleteBucketCors                       | ✅         | ❌    |
| DeleteBucketEncryption                 | ✅         | ❌    |
| DeleteBucketIntelligentTieringConfiguration| ✅         | ❌    |
| DeleteBucketInventoryConfiguration     | ✅         | ❌    |
| DeleteBucketLifecycle                  | ✅         | ✅    |
| DeleteBucketMetricsConfiguration       | ✅         | ❌    |
| DeleteBucketOwnershipControls          | ✅         | ❌    |
| DeleteBucketPolicy                     | ✅         | ✅    |
| DeleteBucketReplication                | ✅         | ❌    |
| DeleteBucketTagging                    | ✅         | ❌    |
| DeleteBucketWebsite                    | ✅         | ❌    |
| DeleteObject                           | ✅         | ✅    |
| DeleteObjectTagging                    | ✅         | ✅    |
| DeleteObjects                          | ✅         | ✅    |
| DeletePublicAccessBlock                | ✅         | ❌    |
| GetBucketAccelerateConfiguration       | ✅         | ✅    |
| GetBucketAcl                           | ✅         | ✅    |
| GetBucketAnalyticsConfiguration        | ✅         | ❌    |
| GetBucketCors                          | ✅         | ✅    |
| GetBucketEncryption                    | ✅         | ✅    |
| GetBucketIntelligentTieringConfiguration| ✅         | ❌    |
| GetBucketInventoryConfiguration        | ✅         | ❌    |
| GetBucketLifecycle                     | ✅         | ❌    |
| GetBucketLifecycleConfiguration        | ✅         | ✅    |
| GetBucketLocation                      | ✅         | ✅    |
| GetBucketLogging                       | ✅         | ✅    |
| GetBucketMetricsConfiguration          | ✅         | ❌    |
| GetBucketNotification                  | ✅         | ❌    |
| GetBucketNotificationConfiguration     | ✅         | ✅    |
| GetBucketOwnershipControls             | ✅         | ❌    |
| GetBucketPolicy                        | ✅         | ✅    |
| GetBucketPolicyStatus                  | ✅         | ❌    |
| GetBucketReplication                   | ✅         | ✅    |
| GetBucketRequestPayment                | ✅         | ✅    |
| GetBucketTagging                       | ✅         | ✅    |
| GetBucketVersioning                    | ✅         | ✅    |
| GetBucketWebsite                       | ✅         | ✅    |
| GetObject                              | ✅         | ✅    |
| GetObjectAcl                           | ✅         | ✅    |
| GetObjectAttributes                    | ✅         | ❌    |
| GetObjectLegalHold                     | ✅         | ❌    |
| GetObjectLockConfiguration             | ✅         | ✅    |
| GetObjectRetention                     | ✅         | ❌    |
| GetObjectTagging                       | ✅         | ❌    |
| GetObjectTorrent                       | ✅         | ❌    |
| GetPublicAccessBlock                   | ✅         | ✅    |
| HeadBucket                             | ✅         | ✅    |
| HeadObject                             | ✅         | ✅    |
| ListBucketAnalyticsConfigurations      | ✅         | ❌    |
| ListBucketIntelligentTieringConfigurations| ✅         | ❌    |
| ListBucketInventoryConfigurations      | ✅         | ❌    |
| ListBucketMetricsConfigurations        | ✅         | ❌    |
| ListBuckets                            | ✅         | ✅    |
| ListMultipartUploads                   | ✅         | ❌    |
| ListObjectVersions                     | ✅         | ✅    |
| ListObjects                            | ✅         | ✅    |
| ListObjectsV2                          | ✅         | ✅    |
| ListParts                              | ✅         | ❌    |
| PutBucketAccelerateConfiguration       | ✅         | ❌    |
| PutBucketAcl                           | ✅         | ❌    |
| PutBucketAnalyticsConfiguration        | ✅         | ❌    |
| PutBucketCors                          | ✅         | ✅    |
| PutBucketEncryption                    | ✅         | ❌    |
| PutBucketIntelligentTieringConfiguration| ✅         | ❌    |
| PutBucketInventoryConfiguration        | ✅         | ❌    |
| PutBucketLifecycle                     | ✅         | ❌    |
| PutBucketLifecycleConfiguration        | ✅         | ✅    |
| PutBucketLogging                       | ✅         | ❌    |
| PutBucketMetricsConfiguration          | ✅         | ❌    |
| PutBucketNotification                  | ✅         | ❌    |
| PutBucketNotificationConfiguration     | ✅         | ✅    |
| PutBucketOwnershipControls             | ✅         | ❌    |
| PutBucketPolicy                        | ✅         | ✅    |
| PutBucketReplication                   | ✅         | ❌    |
| PutBucketRequestPayment                | ✅         | ✅    |
| PutBucketTagging                       | ✅         | ✅    |
| PutBucketVersioning                    | ✅         | ✅    |
| PutBucketWebsite                       | ✅         | ✅    |
| PutObject                              | ✅         | ✅    |
| PutObjectAcl                           | ✅         | ✅    |
| PutObjectLegalHold                     | ✅         | ❌    |
| PutObjectLockConfiguration             | ✅         | ❌    |
| PutObjectRetention                     | ✅         | ❌    |
| PutObjectTagging                       | ✅         | ✅    |
| PutPublicAccessBlock                   | ✅         | ❌    |
| RestoreObject                          | ✅         | ✅    |
| SelectObjectContent                    | ✅         | ✅    |
| UploadPart                             | ✅         | ✅    |
| UploadPartCopy                         | ✅         | ❌    |
| WriteGetObjectResponse                 | ✅         | ❌    |



## s3control ##

API returns a response for 100.0% of the operations.

| Operation                              | Implemented | Tested |
|----------------------------------------|-------------|--------|
| CreateAccessPoint                      | ✅         | ❌    |
| CreateAccessPointForObjectLambda       | ✅         | ❌    |
| CreateBucket                           | ✅         | ❌    |
| CreateJob                              | ✅         | ❌    |
| CreateMultiRegionAccessPoint           | ✅         | ❌    |
| DeleteAccessPoint                      | ✅         | ❌    |
| DeleteAccessPointForObjectLambda       | ✅         | ❌    |
| DeleteAccessPointPolicy                | ✅         | ❌    |
| DeleteAccessPointPolicyForObjectLambda | ✅         | ❌    |
| DeleteBucket                           | ✅         | ❌    |
| DeleteBucketLifecycleConfiguration     | ✅         | ❌    |
| DeleteBucketPolicy                     | ✅         | ❌    |
| DeleteBucketTagging                    | ✅         | ❌    |
| DeleteJobTagging                       | ✅         | ❌    |
| DeleteMultiRegionAccessPoint           | ✅         | ❌    |
| DeletePublicAccessBlock                | ✅         | ✅    |
| DeleteStorageLensConfiguration         | ✅         | ❌    |
| DeleteStorageLensConfigurationTagging  | ✅         | ❌    |
| DescribeJob                            | ✅         | ❌    |
| DescribeMultiRegionAccessPointOperation| ✅         | ❌    |
| GetAccessPoint                         | ✅         | ❌    |
| GetAccessPointConfigurationForObjectLambda| ✅         | ❌    |
| GetAccessPointForObjectLambda          | ✅         | ❌    |
| GetAccessPointPolicy                   | ✅         | ❌    |
| GetAccessPointPolicyForObjectLambda    | ✅         | ❌    |
| GetAccessPointPolicyStatus             | ✅         | ❌    |
| GetAccessPointPolicyStatusForObjectLambda| ✅         | ❌    |
| GetBucket                              | ✅         | ❌    |
| GetBucketLifecycleConfiguration        | ✅         | ❌    |
| GetBucketPolicy                        | ✅         | ❌    |
| GetBucketTagging                       | ✅         | ❌    |
| GetJobTagging                          | ✅         | ❌    |
| GetMultiRegionAccessPoint              | ✅         | ❌    |
| GetMultiRegionAccessPointPolicy        | ✅         | ❌    |
| GetMultiRegionAccessPointPolicyStatus  | ✅         | ❌    |
| GetPublicAccessBlock                   | ✅         | ✅    |
| GetStorageLensConfiguration            | ✅         | ❌    |
| GetStorageLensConfigurationTagging     | ✅         | ❌    |
| ListAccessPoints                       | ✅         | ❌    |
| ListAccessPointsForObjectLambda        | ✅         | ❌    |
| ListJobs                               | ✅         | ❌    |
| ListMultiRegionAccessPoints            | ✅         | ❌    |
| ListRegionalBuckets                    | ✅         | ❌    |
| ListStorageLensConfigurations          | ✅         | ❌    |
| PutAccessPointConfigurationForObjectLambda| ✅         | ❌    |
| PutAccessPointPolicy                   | ✅         | ❌    |
| PutAccessPointPolicyForObjectLambda    | ✅         | ❌    |
| PutBucketLifecycleConfiguration        | ✅         | ❌    |
| PutBucketPolicy                        | ✅         | ❌    |
| PutBucketTagging                       | ✅         | ❌    |
| PutJobTagging                          | ✅         | ❌    |
| PutMultiRegionAccessPointPolicy        | ✅         | ❌    |
| PutPublicAccessBlock                   | ✅         | ✅    |
| PutStorageLensConfiguration            | ✅         | ❌    |
| PutStorageLensConfigurationTagging     | ✅         | ❌    |
| UpdateJobPriority                      | ✅         | ❌    |
| UpdateJobStatus                        | ✅         | ❌    |



## sagemaker ##

API returns a response for 17.3% of the operations.

| Operation                              | Implemented | Tested |
|----------------------------------------|-------------|--------|
| AddAssociation                         | ❌         | ❌    |
| AddTags                                | ✅         | ❌    |
| AssociateTrialComponent                | ✅         | ❌    |
| BatchDescribeModelPackage              | ❌         | ❌    |
| CreateAction                           | ❌         | ❌    |
| CreateAlgorithm                        | ❌         | ❌    |
| CreateApp                              | ❌         | ❌    |
| CreateAppImageConfig                   | ❌         | ❌    |
| CreateArtifact                         | ❌         | ❌    |
| CreateAutoMLJob                        | ❌         | ❌    |
| CreateCodeRepository                   | ❌         | ❌    |
| CreateCompilationJob                   | ❌         | ❌    |
| CreateContext                          | ❌         | ❌    |
| CreateDataQualityJobDefinition         | ❌         | ❌    |
| CreateDeviceFleet                      | ❌         | ❌    |
| CreateDomain                           | ❌         | ❌    |
| CreateEdgePackagingJob                 | ❌         | ❌    |
| CreateEndpoint                         | ✅         | ❌    |
| CreateEndpointConfig                   | ✅         | ❌    |
| CreateExperiment                       | ✅         | ❌    |
| CreateFeatureGroup                     | ❌         | ❌    |
| CreateFlowDefinition                   | ❌         | ❌    |
| CreateHumanTaskUi                      | ❌         | ❌    |
| CreateHyperParameterTuningJob          | ❌         | ❌    |
| CreateImage                            | ❌         | ❌    |
| CreateImageVersion                     | ❌         | ❌    |
| CreateInferenceRecommendationsJob      | ❌         | ❌    |
| CreateLabelingJob                      | ❌         | ❌    |
| CreateModel                            | ✅         | ✅    |
| CreateModelBiasJobDefinition           | ❌         | ❌    |
| CreateModelExplainabilityJobDefinition | ❌         | ❌    |
| CreateModelPackage                     | ❌         | ❌    |
| CreateModelPackageGroup                | ❌         | ❌    |
| CreateModelQualityJobDefinition        | ❌         | ❌    |
| CreateMonitoringSchedule               | ❌         | ❌    |
| CreateNotebookInstance                 | ✅         | ❌    |
| CreateNotebookInstanceLifecycleConfig  | ✅         | ❌    |
| CreatePipeline                         | ❌         | ❌    |
| CreatePresignedDomainUrl               | ❌         | ❌    |
| CreatePresignedNotebookInstanceUrl     | ❌         | ❌    |
| CreateProcessingJob                    | ✅         | ❌    |
| CreateProject                          | ❌         | ❌    |
| CreateStudioLifecycleConfig            | ❌         | ❌    |
| CreateTrainingJob                      | ✅         | ❌    |
| CreateTransformJob                     | ❌         | ❌    |
| CreateTrial                            | ✅         | ❌    |
| CreateTrialComponent                   | ✅         | ❌    |
| CreateUserProfile                      | ❌         | ❌    |
| CreateWorkforce                        | ❌         | ❌    |
| CreateWorkteam                         | ❌         | ❌    |
| DeleteAction                           | ❌         | ❌    |
| DeleteAlgorithm                        | ❌         | ❌    |
| DeleteApp                              | ❌         | ❌    |
| DeleteAppImageConfig                   | ❌         | ❌    |
| DeleteArtifact                         | ❌         | ❌    |
| DeleteAssociation                      | ❌         | ❌    |
| DeleteCodeRepository                   | ❌         | ❌    |
| DeleteContext                          | ❌         | ❌    |
| DeleteDataQualityJobDefinition         | ❌         | ❌    |
| DeleteDeviceFleet                      | ❌         | ❌    |
| DeleteDomain                           | ❌         | ❌    |
| DeleteEndpoint                         | ✅         | ❌    |
| DeleteEndpointConfig                   | ✅         | ❌    |
| DeleteExperiment                       | ✅         | ❌    |
| DeleteFeatureGroup                     | ❌         | ❌    |
| DeleteFlowDefinition                   | ❌         | ❌    |
| DeleteHumanTaskUi                      | ❌         | ❌    |
| DeleteImage                            | ❌         | ❌    |
| DeleteImageVersion                     | ❌         | ❌    |
| DeleteModel                            | ✅         | ❌    |
| DeleteModelBiasJobDefinition           | ❌         | ❌    |
| DeleteModelExplainabilityJobDefinition | ❌         | ❌    |
| DeleteModelPackage                     | ❌         | ❌    |
| DeleteModelPackageGroup                | ❌         | ❌    |
| DeleteModelPackageGroupPolicy          | ❌         | ❌    |
| DeleteModelQualityJobDefinition        | ❌         | ❌    |
| DeleteMonitoringSchedule               | ❌         | ❌    |
| DeleteNotebookInstance                 | ✅         | ❌    |
| DeleteNotebookInstanceLifecycleConfig  | ✅         | ❌    |
| DeletePipeline                         | ❌         | ❌    |
| DeleteProject                          | ❌         | ❌    |
| DeleteStudioLifecycleConfig            | ❌         | ❌    |
| DeleteTags                             | ✅         | ❌    |
| DeleteTrial                            | ✅         | ❌    |
| DeleteTrialComponent                   | ✅         | ❌    |
| DeleteUserProfile                      | ❌         | ❌    |
| DeleteWorkforce                        | ❌         | ❌    |
| DeleteWorkteam                         | ❌         | ❌    |
| DeregisterDevices                      | ❌         | ❌    |
| DescribeAction                         | ❌         | ❌    |
| DescribeAlgorithm                      | ❌         | ❌    |
| DescribeApp                            | ❌         | ❌    |
| DescribeAppImageConfig                 | ❌         | ❌    |
| DescribeArtifact                       | ❌         | ❌    |
| DescribeAutoMLJob                      | ❌         | ❌    |
| DescribeCodeRepository                 | ❌         | ❌    |
| DescribeCompilationJob                 | ❌         | ❌    |
| DescribeContext                        | ❌         | ❌    |
| DescribeDataQualityJobDefinition       | ❌         | ❌    |
| DescribeDevice                         | ❌         | ❌    |
| DescribeDeviceFleet                    | ❌         | ❌    |
| DescribeDomain                         | ❌         | ❌    |
| DescribeEdgePackagingJob               | ❌         | ❌    |
| DescribeEndpoint                       | ✅         | ❌    |
| DescribeEndpointConfig                 | ✅         | ❌    |
| DescribeExperiment                     | ✅         | ❌    |
| DescribeFeatureGroup                   | ❌         | ❌    |
| DescribeFeatureMetadata                | ❌         | ❌    |
| DescribeFlowDefinition                 | ❌         | ❌    |
| DescribeHumanTaskUi                    | ❌         | ❌    |
| DescribeHyperParameterTuningJob        | ❌         | ❌    |
| DescribeImage                          | ❌         | ❌    |
| DescribeImageVersion                   | ❌         | ❌    |
| DescribeInferenceRecommendationsJob    | ❌         | ❌    |
| DescribeLabelingJob                    | ❌         | ❌    |
| DescribeLineageGroup                   | ❌         | ❌    |
| DescribeModel                          | ✅         | ✅    |
| DescribeModelBiasJobDefinition         | ❌         | ❌    |
| DescribeModelExplainabilityJobDefinition| ❌         | ❌    |
| DescribeModelPackage                   | ❌         | ❌    |
| DescribeModelPackageGroup              | ❌         | ❌    |
| DescribeModelQualityJobDefinition      | ❌         | ❌    |
| DescribeMonitoringSchedule             | ❌         | ❌    |
| DescribeNotebookInstance               | ✅         | ❌    |
| DescribeNotebookInstanceLifecycleConfig| ✅         | ❌    |
| DescribePipeline                       | ❌         | ❌    |
| DescribePipelineDefinitionForExecution | ❌         | ❌    |
| DescribePipelineExecution              | ❌         | ❌    |
| DescribeProcessingJob                  | ✅         | ❌    |
| DescribeProject                        | ❌         | ❌    |
| DescribeStudioLifecycleConfig          | ❌         | ❌    |
| DescribeSubscribedWorkteam             | ❌         | ❌    |
| DescribeTrainingJob                    | ✅         | ❌    |
| DescribeTransformJob                   | ❌         | ❌    |
| DescribeTrial                          | ✅         | ❌    |
| DescribeTrialComponent                 | ✅         | ❌    |
| DescribeUserProfile                    | ❌         | ❌    |
| DescribeWorkforce                      | ❌         | ❌    |
| DescribeWorkteam                       | ❌         | ❌    |
| DisableSagemakerServicecatalogPortfolio| ❌         | ❌    |
| DisassociateTrialComponent             | ✅         | ❌    |
| EnableSagemakerServicecatalogPortfolio | ❌         | ❌    |
| GetDeviceFleetReport                   | ❌         | ❌    |
| GetLineageGroupPolicy                  | ❌         | ❌    |
| GetModelPackageGroupPolicy             | ❌         | ❌    |
| GetSagemakerServicecatalogPortfolioStatus| ❌         | ❌    |
| GetSearchSuggestions                   | ❌         | ❌    |
| ListActions                            | ❌         | ❌    |
| ListAlgorithms                         | ❌         | ❌    |
| ListAppImageConfigs                    | ❌         | ❌    |
| ListApps                               | ❌         | ❌    |
| ListArtifacts                          | ❌         | ❌    |
| ListAssociations                       | ✅         | ❌    |
| ListAutoMLJobs                         | ❌         | ❌    |
| ListCandidatesForAutoMLJob             | ❌         | ❌    |
| ListCodeRepositories                   | ❌         | ❌    |
| ListCompilationJobs                    | ❌         | ❌    |
| ListContexts                           | ❌         | ❌    |
| ListDataQualityJobDefinitions          | ❌         | ❌    |
| ListDeviceFleets                       | ❌         | ❌    |
| ListDevices                            | ❌         | ❌    |
| ListDomains                            | ❌         | ❌    |
| ListEdgePackagingJobs                  | ❌         | ❌    |
| ListEndpointConfigs                    | ❌         | ❌    |
| ListEndpoints                          | ❌         | ❌    |
| ListExperiments                        | ✅         | ❌    |
| ListFeatureGroups                      | ❌         | ❌    |
| ListFlowDefinitions                    | ❌         | ❌    |
| ListHumanTaskUis                       | ❌         | ❌    |
| ListHyperParameterTuningJobs           | ❌         | ❌    |
| ListImageVersions                      | ❌         | ❌    |
| ListImages                             | ❌         | ❌    |
| ListInferenceRecommendationsJobs       | ❌         | ❌    |
| ListLabelingJobs                       | ❌         | ❌    |
| ListLabelingJobsForWorkteam            | ❌         | ❌    |
| ListLineageGroups                      | ❌         | ❌    |
| ListModelBiasJobDefinitions            | ❌         | ❌    |
| ListModelExplainabilityJobDefinitions  | ❌         | ❌    |
| ListModelMetadata                      | ❌         | ❌    |
| ListModelPackageGroups                 | ❌         | ❌    |
| ListModelPackages                      | ❌         | ❌    |
| ListModelQualityJobDefinitions         | ❌         | ❌    |
| ListModels                             | ✅         | ❌    |
| ListMonitoringExecutions               | ❌         | ❌    |
| ListMonitoringSchedules                | ❌         | ❌    |
| ListNotebookInstanceLifecycleConfigs   | ❌         | ❌    |
| ListNotebookInstances                  | ❌         | ❌    |
| ListPipelineExecutionSteps             | ❌         | ❌    |
| ListPipelineExecutions                 | ❌         | ❌    |
| ListPipelineParametersForExecution     | ❌         | ❌    |
| ListPipelines                          | ❌         | ❌    |
| ListProcessingJobs                     | ✅         | ❌    |
| ListProjects                           | ❌         | ❌    |
| ListStudioLifecycleConfigs             | ❌         | ❌    |
| ListSubscribedWorkteams                | ❌         | ❌    |
| ListTags                               | ✅         | ❌    |
| ListTrainingJobs                       | ✅         | ❌    |
| ListTrainingJobsForHyperParameterTuningJob| ❌         | ❌    |
| ListTransformJobs                      | ❌         | ❌    |
| ListTrialComponents                    | ✅         | ❌    |
| ListTrials                             | ✅         | ❌    |
| ListUserProfiles                       | ❌         | ❌    |
| ListWorkforces                         | ❌         | ❌    |
| ListWorkteams                          | ❌         | ❌    |
| PutModelPackageGroupPolicy             | ❌         | ❌    |
| QueryLineage                           | ❌         | ❌    |
| RegisterDevices                        | ❌         | ❌    |
| RenderUiTemplate                       | ❌         | ❌    |
| RetryPipelineExecution                 | ❌         | ❌    |
| Search                                 | ✅         | ❌    |
| SendPipelineExecutionStepFailure       | ❌         | ❌    |
| SendPipelineExecutionStepSuccess       | ❌         | ❌    |
| StartMonitoringSchedule                | ❌         | ❌    |
| StartNotebookInstance                  | ✅         | ❌    |
| StartPipelineExecution                 | ❌         | ❌    |
| StopAutoMLJob                          | ❌         | ❌    |
| StopCompilationJob                     | ❌         | ❌    |
| StopEdgePackagingJob                   | ❌         | ❌    |
| StopHyperParameterTuningJob            | ❌         | ❌    |
| StopInferenceRecommendationsJob        | ❌         | ❌    |
| StopLabelingJob                        | ❌         | ❌    |
| StopMonitoringSchedule                 | ❌         | ❌    |
| StopNotebookInstance                   | ✅         | ❌    |
| StopPipelineExecution                  | ❌         | ❌    |
| StopProcessingJob                      | ❌         | ❌    |
| StopTrainingJob                        | ❌         | ❌    |
| StopTransformJob                       | ❌         | ❌    |
| UpdateAction                           | ❌         | ❌    |
| UpdateAppImageConfig                   | ❌         | ❌    |
| UpdateArtifact                         | ❌         | ❌    |
| UpdateCodeRepository                   | ❌         | ❌    |
| UpdateContext                          | ❌         | ❌    |
| UpdateDeviceFleet                      | ❌         | ❌    |
| UpdateDevices                          | ❌         | ❌    |
| UpdateDomain                           | ❌         | ❌    |
| UpdateEndpoint                         | ❌         | ❌    |
| UpdateEndpointWeightsAndCapacities     | ✅         | ❌    |
| UpdateExperiment                       | ❌         | ❌    |
| UpdateFeatureGroup                     | ❌         | ❌    |
| UpdateFeatureMetadata                  | ❌         | ❌    |
| UpdateImage                            | ❌         | ❌    |
| UpdateModelPackage                     | ❌         | ❌    |
| UpdateMonitoringSchedule               | ❌         | ❌    |
| UpdateNotebookInstance                 | ❌         | ❌    |
| UpdateNotebookInstanceLifecycleConfig  | ❌         | ❌    |
| UpdatePipeline                         | ❌         | ❌    |
| UpdatePipelineExecution                | ❌         | ❌    |
| UpdateProject                          | ❌         | ❌    |
| UpdateTrainingJob                      | ❌         | ❌    |
| UpdateTrial                            | ❌         | ❌    |
| UpdateTrialComponent                   | ❌         | ❌    |
| UpdateUserProfile                      | ❌         | ❌    |
| UpdateWorkforce                        | ❌         | ❌    |
| UpdateWorkteam                         | ❌         | ❌    |



## secretsmanager ##

API returns a response for 77.3% of the operations.

| Operation                              | Implemented | Tested |
|----------------------------------------|-------------|--------|
| CancelRotateSecret                     | ❌         | ❌    |
| CreateSecret                           | ✅         | ✅    |
| DeleteResourcePolicy                   | ✅         | ✅    |
| DeleteSecret                           | ✅         | ✅    |
| DescribeSecret                         | ✅         | ✅    |
| GetRandomPassword                      | ✅         | ✅    |
| GetResourcePolicy                      | ✅         | ✅    |
| GetSecretValue                         | ✅         | ✅    |
| ListSecretVersionIds                   | ✅         | ✅    |
| ListSecrets                            | ✅         | ✅    |
| PutResourcePolicy                      | ✅         | ✅    |
| PutSecretValue                         | ✅         | ✅    |
| RemoveRegionsFromReplication           | ❌         | ❌    |
| ReplicateSecretToRegions               | ❌         | ❌    |
| RestoreSecret                          | ✅         | ❌    |
| RotateSecret                           | ✅         | ✅    |
| StopReplicationToReplica               | ❌         | ❌    |
| TagResource                            | ✅         | ✅    |
| UntagResource                          | ✅         | ✅    |
| UpdateSecret                           | ✅         | ✅    |
| UpdateSecretVersionStage               | ✅         | ✅    |
| ValidateResourcePolicy                 | ❌         | ✅    |



## serverlessrepo ##

API returns a response for 57.1% of the operations.

| Operation                              | Implemented | Tested |
|----------------------------------------|-------------|--------|
| CreateApplication                      | ✅         | ✅    |
| CreateApplicationVersion               | ✅         | ✅    |
| CreateCloudFormationChangeSet          | ✅         | ✅    |
| CreateCloudFormationTemplate           | ✅         | ✅    |
| DeleteApplication                      | ✅         | ✅    |
| GetApplication                         | ❌         | ❌    |
| GetApplicationPolicy                   | ❌         | ❌    |
| GetCloudFormationTemplate              | ✅         | ✅    |
| ListApplicationDependencies            | ❌         | ❌    |
| ListApplicationVersions                | ✅         | ✅    |
| ListApplications                       | ✅         | ✅    |
| PutApplicationPolicy                   | ❌         | ❌    |
| UnshareApplication                     | ❌         | ❌    |
| UpdateApplication                      | ❌         | ❌    |



## servicediscovery ##

API returns a response for 73.1% of the operations.

| Operation                              | Implemented | Tested |
|----------------------------------------|-------------|--------|
| CreateHttpNamespace                    | ✅         | ✅    |
| CreatePrivateDnsNamespace              | ✅         | ✅    |
| CreatePublicDnsNamespace               | ✅         | ✅    |
| CreateService                          | ✅         | ✅    |
| DeleteNamespace                        | ✅         | ✅    |
| DeleteService                          | ✅         | ✅    |
| DeregisterInstance                     | ✅         | ✅    |
| DiscoverInstances                      | ❌         | ✅    |
| GetInstance                            | ✅         | ✅    |
| GetInstancesHealthStatus               | ❌         | ❌    |
| GetNamespace                           | ✅         | ✅    |
| GetOperation                           | ✅         | ✅    |
| GetService                             | ✅         | ✅    |
| ListInstances                          | ✅         | ✅    |
| ListNamespaces                         | ✅         | ✅    |
| ListOperations                         | ❌         | ❌    |
| ListServices                           | ✅         | ✅    |
| ListTagsForResource                    | ✅         | ✅    |
| RegisterInstance                       | ✅         | ✅    |
| TagResource                            | ✅         | ✅    |
| UntagResource                          | ✅         | ✅    |
| UpdateHttpNamespace                    | ❌         | ❌    |
| UpdateInstanceCustomHealthStatus       | ❌         | ❌    |
| UpdatePrivateDnsNamespace              | ❌         | ❌    |
| UpdatePublicDnsNamespace               | ❌         | ❌    |
| UpdateService                          | ✅         | ✅    |



## ses ##

API returns a response for 52.1% of the operations.

| Operation                              | Implemented | Tested |
|----------------------------------------|-------------|--------|
| CloneReceiptRuleSet                    | ❌         | ❌    |
| CreateConfigurationSet                 | ✅         | ❌    |
| CreateConfigurationSetEventDestination | ✅         | ❌    |
| CreateConfigurationSetTrackingOptions  | ❌         | ❌    |
| CreateCustomVerificationEmailTemplate  | ❌         | ❌    |
| CreateReceiptFilter                    | ❌         | ❌    |
| CreateReceiptRule                      | ✅         | ✅    |
| CreateReceiptRuleSet                   | ✅         | ✅    |
| CreateTemplate                         | ✅         | ✅    |
| DeleteConfigurationSet                 | ❌         | ❌    |
| DeleteConfigurationSetEventDestination | ❌         | ❌    |
| DeleteConfigurationSetTrackingOptions  | ❌         | ❌    |
| DeleteCustomVerificationEmailTemplate  | ❌         | ❌    |
| DeleteIdentity                         | ✅         | ❌    |
| DeleteIdentityPolicy                   | ❌         | ❌    |
| DeleteReceiptFilter                    | ❌         | ❌    |
| DeleteReceiptRule                      | ✅         | ✅    |
| DeleteReceiptRuleSet                   | ✅         | ✅    |
| DeleteTemplate                         | ✅         | ✅    |
| DeleteVerifiedEmailAddress             | ❌         | ❌    |
| DescribeActiveReceiptRuleSet           | ✅         | ✅    |
| DescribeConfigurationSet               | ❌         | ❌    |
| DescribeReceiptRule                    | ✅         | ✅    |
| DescribeReceiptRuleSet                 | ✅         | ✅    |
| GetAccountSendingEnabled               | ❌         | ❌    |
| GetCustomVerificationEmailTemplate     | ❌         | ❌    |
| GetIdentityDkimAttributes              | ❌         | ❌    |
| GetIdentityMailFromDomainAttributes    | ✅         | ❌    |
| GetIdentityNotificationAttributes      | ✅         | ❌    |
| GetIdentityPolicies                    | ❌         | ❌    |
| GetIdentityVerificationAttributes      | ✅         | ✅    |
| GetSendQuota                           | ✅         | ❌    |
| GetSendStatistics                      | ✅         | ❌    |
| GetTemplate                            | ✅         | ❌    |
| ListConfigurationSets                  | ❌         | ❌    |
| ListCustomVerificationEmailTemplates   | ❌         | ❌    |
| ListIdentities                         | ✅         | ❌    |
| ListIdentityPolicies                   | ❌         | ❌    |
| ListReceiptFilters                     | ❌         | ❌    |
| ListReceiptRuleSets                    | ✅         | ✅    |
| ListTemplates                          | ✅         | ✅    |
| ListVerifiedEmailAddresses             | ✅         | ❌    |
| PutConfigurationSetDeliveryOptions     | ❌         | ❌    |
| PutIdentityPolicy                      | ❌         | ❌    |
| ReorderReceiptRuleSet                  | ❌         | ❌    |
| SendBounce                             | ❌         | ❌    |
| SendBulkTemplatedEmail                 | ✅         | ✅    |
| SendCustomVerificationEmail            | ❌         | ❌    |
| SendEmail                              | ✅         | ✅    |
| SendRawEmail                           | ✅         | ✅    |
| SendTemplatedEmail                     | ✅         | ✅    |
| SetActiveReceiptRuleSet                | ✅         | ✅    |
| SetIdentityDkimEnabled                 | ❌         | ❌    |
| SetIdentityFeedbackForwardingEnabled   | ✅         | ❌    |
| SetIdentityHeadersInNotificationsEnabled| ❌         | ❌    |
| SetIdentityMailFromDomain              | ✅         | ❌    |
| SetIdentityNotificationTopic           | ✅         | ❌    |
| SetReceiptRulePosition                 | ❌         | ❌    |
| TestRenderTemplate                     | ✅         | ❌    |
| UpdateAccountSendingEnabled            | ❌         | ❌    |
| UpdateConfigurationSetEventDestination | ❌         | ❌    |
| UpdateConfigurationSetReputationMetricsEnabled| ❌         | ❌    |
| UpdateConfigurationSetSendingEnabled   | ❌         | ❌    |
| UpdateConfigurationSetTrackingOptions  | ❌         | ❌    |
| UpdateCustomVerificationEmailTemplate  | ❌         | ❌    |
| UpdateReceiptRule                      | ✅         | ❌    |
| UpdateTemplate                         | ✅         | ❌    |
| VerifyDomainDkim                       | ✅         | ❌    |
| VerifyDomainIdentity                   | ✅         | ❌    |
| VerifyEmailAddress                     | ✅         | ✅    |
| VerifyEmailIdentity                    | ✅         | ✅    |



## sesv2 ##

API returns a response for 16.0% of the operations.

| Operation                              | Implemented | Tested |
|----------------------------------------|-------------|--------|
| CreateConfigurationSet                 | ❌         | ❌    |
| CreateConfigurationSetEventDestination | ❌         | ❌    |
| CreateContact                          | ❌         | ❌    |
| CreateContactList                      | ❌         | ❌    |
| CreateCustomVerificationEmailTemplate  | ❌         | ❌    |
| CreateDedicatedIpPool                  | ❌         | ❌    |
| CreateDeliverabilityTestReport         | ❌         | ❌    |
| CreateEmailIdentity                    | ✅         | ✅    |
| CreateEmailIdentityPolicy              | ❌         | ❌    |
| CreateEmailTemplate                    | ✅         | ✅    |
| CreateImportJob                        | ❌         | ❌    |
| DeleteConfigurationSet                 | ❌         | ❌    |
| DeleteConfigurationSetEventDestination | ❌         | ❌    |
| DeleteContact                          | ❌         | ❌    |
| DeleteContactList                      | ❌         | ❌    |
| DeleteCustomVerificationEmailTemplate  | ❌         | ❌    |
| DeleteDedicatedIpPool                  | ❌         | ❌    |
| DeleteEmailIdentity                    | ✅         | ✅    |
| DeleteEmailIdentityPolicy              | ❌         | ❌    |
| DeleteEmailTemplate                    | ✅         | ❌    |
| DeleteSuppressedDestination            | ❌         | ❌    |
| GetAccount                             | ❌         | ❌    |
| GetBlacklistReports                    | ❌         | ❌    |
| GetConfigurationSet                    | ❌         | ❌    |
| GetConfigurationSetEventDestinations   | ❌         | ❌    |
| GetContact                             | ❌         | ❌    |
| GetContactList                         | ❌         | ❌    |
| GetCustomVerificationEmailTemplate     | ❌         | ❌    |
| GetDedicatedIp                         | ❌         | ❌    |
| GetDedicatedIps                        | ❌         | ❌    |
| GetDeliverabilityDashboardOptions      | ❌         | ❌    |
| GetDeliverabilityTestReport            | ❌         | ❌    |
| GetDomainDeliverabilityCampaign        | ❌         | ❌    |
| GetDomainStatisticsReport              | ✅         | ❌    |
| GetEmailIdentity                       | ✅         | ✅    |
| GetEmailIdentityPolicies               | ❌         | ❌    |
| GetEmailTemplate                       | ❌         | ❌    |
| GetImportJob                           | ❌         | ❌    |
| GetSuppressedDestination               | ❌         | ❌    |
| ListConfigurationSets                  | ❌         | ❌    |
| ListContactLists                       | ❌         | ❌    |
| ListContacts                           | ❌         | ❌    |
| ListCustomVerificationEmailTemplates   | ❌         | ❌    |
| ListDedicatedIpPools                   | ❌         | ❌    |
| ListDeliverabilityTestReports          | ❌         | ❌    |
| ListDomainDeliverabilityCampaigns      | ✅         | ❌    |
| ListEmailIdentities                    | ✅         | ✅    |
| ListEmailTemplates                     | ✅         | ❌    |
| ListImportJobs                         | ❌         | ❌    |
| ListSuppressedDestinations             | ✅         | ❌    |
| ListTagsForResource                    | ❌         | ❌    |
| PutAccountDedicatedIpWarmupAttributes  | ❌         | ❌    |
| PutAccountDetails                      | ❌         | ❌    |
| PutAccountSendingAttributes            | ❌         | ❌    |
| PutAccountSuppressionAttributes        | ❌         | ❌    |
| PutConfigurationSetDeliveryOptions     | ❌         | ❌    |
| PutConfigurationSetReputationOptions   | ❌         | ❌    |
| PutConfigurationSetSendingOptions      | ❌         | ❌    |
| PutConfigurationSetSuppressionOptions  | ❌         | ❌    |
| PutConfigurationSetTrackingOptions     | ❌         | ❌    |
| PutDedicatedIpInPool                   | ❌         | ❌    |
| PutDedicatedIpWarmupAttributes         | ❌         | ❌    |
| PutDeliverabilityDashboardOption       | ❌         | ❌    |
| PutEmailIdentityConfigurationSetAttributes| ❌         | ❌    |
| PutEmailIdentityDkimAttributes         | ❌         | ❌    |
| PutEmailIdentityDkimSigningAttributes  | ✅         | ❌    |
| PutEmailIdentityFeedbackAttributes     | ❌         | ❌    |
| PutEmailIdentityMailFromAttributes     | ❌         | ❌    |
| PutSuppressedDestination               | ❌         | ❌    |
| SendBulkEmail                          | ✅         | ✅    |
| SendCustomVerificationEmail            | ❌         | ❌    |
| SendEmail                              | ✅         | ✅    |
| TagResource                            | ❌         | ❌    |
| TestRenderEmailTemplate                | ❌         | ❌    |
| UntagResource                          | ❌         | ❌    |
| UpdateConfigurationSetEventDestination | ❌         | ❌    |
| UpdateContact                          | ❌         | ❌    |
| UpdateContactList                      | ❌         | ❌    |
| UpdateCustomVerificationEmailTemplate  | ❌         | ❌    |
| UpdateEmailIdentityPolicy              | ❌         | ❌    |
| UpdateEmailTemplate                    | ❌         | ❌    |



## sns ##

API returns a response for 85.0% of the operations.

| Operation                              | Implemented | Tested |
|----------------------------------------|-------------|--------|
| AddPermission                          | ✅         | ❌    |
| CheckIfPhoneNumberIsOptedOut           | ✅         | ❌    |
| ConfirmSubscription                    | ✅         | ✅    |
| CreatePlatformApplication              | ✅         | ✅    |
| CreatePlatformEndpoint                 | ✅         | ✅    |
| CreateSMSSandboxPhoneNumber            | ❌         | ❌    |
| CreateTopic                            | ✅         | ✅    |
| DeleteEndpoint                         | ✅         | ✅    |
| DeletePlatformApplication              | ✅         | ✅    |
| DeleteSMSSandboxPhoneNumber            | ❌         | ❌    |
| DeleteTopic                            | ✅         | ✅    |
| GetEndpointAttributes                  | ✅         | ✅    |
| GetPlatformApplicationAttributes       | ✅         | ❌    |
| GetSMSAttributes                       | ✅         | ❌    |
| GetSMSSandboxAccountStatus             | ❌         | ❌    |
| GetSubscriptionAttributes              | ✅         | ✅    |
| GetTopicAttributes                     | ✅         | ✅    |
| ListEndpointsByPlatformApplication     | ✅         | ❌    |
| ListOriginationNumbers                 | ❌         | ❌    |
| ListPhoneNumbersOptedOut               | ✅         | ❌    |
| ListPlatformApplications               | ✅         | ✅    |
| ListSMSSandboxPhoneNumbers             | ❌         | ❌    |
| ListSubscriptions                      | ✅         | ❌    |
| ListSubscriptionsByTopic               | ✅         | ✅    |
| ListTagsForResource                    | ✅         | ✅    |
| ListTopics                             | ✅         | ✅    |
| OptInPhoneNumber                       | ✅         | ❌    |
| Publish                                | ✅         | ✅    |
| PublishBatch                           | ✅         | ✅    |
| RemovePermission                       | ✅         | ❌    |
| SetEndpointAttributes                  | ✅         | ❌    |
| SetPlatformApplicationAttributes       | ✅         | ❌    |
| SetSMSAttributes                       | ✅         | ❌    |
| SetSubscriptionAttributes              | ✅         | ✅    |
| SetTopicAttributes                     | ✅         | ✅    |
| Subscribe                              | ✅         | ✅    |
| TagResource                            | ✅         | ✅    |
| Unsubscribe                            | ✅         | ✅    |
| UntagResource                          | ✅         | ✅    |
| VerifySMSSandboxPhoneNumber            | ❌         | ❌    |



## sqs ##

API returns a response for 100.0% of the operations.

| Operation                              | Implemented | Tested |
|----------------------------------------|-------------|--------|
| AddPermission                          | ✅         | ❌    |
| ChangeMessageVisibility                | ✅         | ✅    |
| ChangeMessageVisibilityBatch           | ✅         | ❌    |
| CreateQueue                            | ✅         | ✅    |
| DeleteMessage                          | ✅         | ✅    |
| DeleteMessageBatch                     | ✅         | ✅    |
| DeleteQueue                            | ✅         | ✅    |
| GetQueueAttributes                     | ✅         | ✅    |
| GetQueueUrl                            | ✅         | ✅    |
| ListDeadLetterSourceQueues             | ✅         | ✅    |
| ListQueueTags                          | ✅         | ✅    |
| ListQueues                             | ✅         | ✅    |
| PurgeQueue                             | ✅         | ✅    |
| ReceiveMessage                         | ✅         | ✅    |
| RemovePermission                       | ✅         | ❌    |
| SendMessage                            | ✅         | ✅    |
| SendMessageBatch                       | ✅         | ✅    |
| SetQueueAttributes                     | ✅         | ✅    |
| TagQueue                               | ✅         | ✅    |
| UntagQueue                             | ✅         | ✅    |



## ssm ##

API returns a response for 23.0% of the operations.

| Operation                              | Implemented | Tested |
|----------------------------------------|-------------|--------|
| AddTagsToResource                      | ✅         | ❌    |
| AssociateOpsItemRelatedItem            | ❌         | ❌    |
| CancelCommand                          | ✅         | ✅    |
| CancelMaintenanceWindowExecution       | ❌         | ❌    |
| CreateActivation                       | ❌         | ❌    |
| CreateAssociation                      | ❌         | ❌    |
| CreateAssociationBatch                 | ❌         | ❌    |
| CreateDocument                         | ✅         | ❌    |
| CreateMaintenanceWindow                | ✅         | ❌    |
| CreateOpsItem                          | ❌         | ❌    |
| CreateOpsMetadata                      | ❌         | ❌    |
| CreatePatchBaseline                    | ❌         | ❌    |
| CreateResourceDataSync                 | ❌         | ❌    |
| DeleteActivation                       | ❌         | ❌    |
| DeleteAssociation                      | ❌         | ❌    |
| DeleteDocument                         | ✅         | ❌    |
| DeleteInventory                        | ❌         | ❌    |
| DeleteMaintenanceWindow                | ✅         | ❌    |
| DeleteOpsMetadata                      | ❌         | ❌    |
| DeleteParameter                        | ✅         | ✅    |
| DeleteParameters                       | ✅         | ❌    |
| DeletePatchBaseline                    | ❌         | ❌    |
| DeleteResourceDataSync                 | ❌         | ❌    |
| DeregisterManagedInstance              | ❌         | ❌    |
| DeregisterPatchBaselineForPatchGroup   | ❌         | ❌    |
| DeregisterTargetFromMaintenanceWindow  | ❌         | ❌    |
| DeregisterTaskFromMaintenanceWindow    | ❌         | ❌    |
| DescribeActivations                    | ❌         | ❌    |
| DescribeAssociation                    | ❌         | ❌    |
| DescribeAssociationExecutionTargets    | ❌         | ❌    |
| DescribeAssociationExecutions          | ❌         | ❌    |
| DescribeAutomationExecutions           | ❌         | ❌    |
| DescribeAutomationStepExecutions       | ❌         | ❌    |
| DescribeAvailablePatches               | ❌         | ❌    |
| DescribeDocument                       | ✅         | ❌    |
| DescribeDocumentPermission             | ✅         | ❌    |
| DescribeEffectiveInstanceAssociations  | ❌         | ❌    |
| DescribeEffectivePatchesForPatchBaseline| ❌         | ❌    |
| DescribeInstanceAssociationsStatus     | ❌         | ❌    |
| DescribeInstanceInformation            | ✅         | ✅    |
| DescribeInstancePatchStates            | ❌         | ❌    |
| DescribeInstancePatchStatesForPatchGroup| ❌         | ❌    |
| DescribeInstancePatches                | ❌         | ❌    |
| DescribeInventoryDeletions             | ❌         | ❌    |
| DescribeMaintenanceWindowExecutionTaskInvocations| ❌         | ❌    |
| DescribeMaintenanceWindowExecutionTasks| ❌         | ❌    |
| DescribeMaintenanceWindowExecutions    | ❌         | ❌    |
| DescribeMaintenanceWindowSchedule      | ❌         | ❌    |
| DescribeMaintenanceWindowTargets       | ❌         | ❌    |
| DescribeMaintenanceWindowTasks         | ❌         | ❌    |
| DescribeMaintenanceWindows             | ✅         | ❌    |
| DescribeMaintenanceWindowsForTarget    | ❌         | ❌    |
| DescribeOpsItems                       | ❌         | ❌    |
| DescribeParameters                     | ✅         | ✅    |
| DescribePatchBaselines                 | ❌         | ❌    |
| DescribePatchGroupState                | ❌         | ❌    |
| DescribePatchGroups                    | ❌         | ❌    |
| DescribePatchProperties                | ❌         | ❌    |
| DescribeSessions                       | ❌         | ❌    |
| DisassociateOpsItemRelatedItem         | ❌         | ❌    |
| GetAutomationExecution                 | ❌         | ❌    |
| GetCalendarState                       | ❌         | ❌    |
| GetCommandInvocation                   | ✅         | ✅    |
| GetConnectionStatus                    | ❌         | ❌    |
| GetDefaultPatchBaseline                | ❌         | ❌    |
| GetDeployablePatchSnapshotForInstance  | ❌         | ❌    |
| GetDocument                            | ✅         | ❌    |
| GetInventory                           | ❌         | ❌    |
| GetInventorySchema                     | ❌         | ❌    |
| GetMaintenanceWindow                   | ✅         | ❌    |
| GetMaintenanceWindowExecution          | ❌         | ❌    |
| GetMaintenanceWindowExecutionTask      | ❌         | ❌    |
| GetMaintenanceWindowExecutionTaskInvocation| ❌         | ❌    |
| GetMaintenanceWindowTask               | ❌         | ❌    |
| GetOpsItem                             | ❌         | ❌    |
| GetOpsMetadata                         | ❌         | ❌    |
| GetOpsSummary                          | ❌         | ❌    |
| GetParameter                           | ✅         | ✅    |
| GetParameterHistory                    | ✅         | ❌    |
| GetParameters                          | ✅         | ✅    |
| GetParametersByPath                    | ✅         | ✅    |
| GetPatchBaseline                       | ❌         | ❌    |
| GetPatchBaselineForPatchGroup          | ❌         | ❌    |
| GetServiceSetting                      | ❌         | ❌    |
| LabelParameterVersion                  | ✅         | ✅    |
| ListAssociationVersions                | ❌         | ❌    |
| ListAssociations                       | ❌         | ❌    |
| ListCommandInvocations                 | ✅         | ❌    |
| ListCommands                           | ✅         | ❌    |
| ListComplianceItems                    | ❌         | ❌    |
| ListComplianceSummaries                | ❌         | ❌    |
| ListDocumentMetadataHistory            | ❌         | ❌    |
| ListDocumentVersions                   | ❌         | ❌    |
| ListDocuments                          | ✅         | ❌    |
| ListInventoryEntries                   | ❌         | ❌    |
| ListOpsItemEvents                      | ❌         | ❌    |
| ListOpsItemRelatedItems                | ❌         | ❌    |
| ListOpsMetadata                        | ❌         | ❌    |
| ListResourceComplianceSummaries        | ❌         | ❌    |
| ListResourceDataSync                   | ❌         | ❌    |
| ListTagsForResource                    | ✅         | ❌    |
| ModifyDocumentPermission               | ✅         | ❌    |
| PutComplianceItems                     | ❌         | ❌    |
| PutInventory                           | ❌         | ❌    |
| PutParameter                           | ✅         | ✅    |
| RegisterDefaultPatchBaseline           | ❌         | ❌    |
| RegisterPatchBaselineForPatchGroup     | ❌         | ❌    |
| RegisterTargetWithMaintenanceWindow    | ❌         | ❌    |
| RegisterTaskWithMaintenanceWindow      | ❌         | ❌    |
| RemoveTagsFromResource                 | ✅         | ❌    |
| ResetServiceSetting                    | ❌         | ❌    |
| ResumeSession                          | ❌         | ❌    |
| SendAutomationSignal                   | ❌         | ❌    |
| SendCommand                            | ✅         | ✅    |
| StartAssociationsOnce                  | ❌         | ❌    |
| StartAutomationExecution               | ❌         | ❌    |
| StartChangeRequestExecution            | ❌         | ❌    |
| StartSession                           | ❌         | ❌    |
| StopAutomationExecution                | ❌         | ❌    |
| TerminateSession                       | ❌         | ❌    |
| UnlabelParameterVersion                | ❌         | ❌    |
| UpdateAssociation                      | ❌         | ❌    |
| UpdateAssociationStatus                | ❌         | ❌    |
| UpdateDocument                         | ✅         | ❌    |
| UpdateDocumentDefaultVersion           | ✅         | ❌    |
| UpdateDocumentMetadata                 | ❌         | ❌    |
| UpdateMaintenanceWindow                | ❌         | ❌    |
| UpdateMaintenanceWindowTarget          | ❌         | ❌    |
| UpdateMaintenanceWindowTask            | ❌         | ❌    |
| UpdateManagedInstanceRole              | ❌         | ❌    |
| UpdateOpsItem                          | ❌         | ❌    |
| UpdateOpsMetadata                      | ❌         | ❌    |
| UpdatePatchBaseline                    | ❌         | ❌    |
| UpdateResourceDataSync                 | ❌         | ❌    |
| UpdateServiceSetting                   | ❌         | ❌    |



## stepfunctions ##

API returns a response for 95.7% of the operations.

| Operation                              | Implemented | Tested |
|----------------------------------------|-------------|--------|
| CreateActivity                         | ✅         | ✅    |
| CreateStateMachine                     | ✅         | ✅    |
| DeleteActivity                         | ✅         | ✅    |
| DeleteStateMachine                     | ✅         | ✅    |
| DescribeActivity                       | ✅         | ✅    |
| DescribeExecution                      | ✅         | ✅    |
| DescribeStateMachine                   | ✅         | ✅    |
| DescribeStateMachineForExecution       | ✅         | ✅    |
| GetActivityTask                        | ✅         | ❌    |
| GetExecutionHistory                    | ✅         | ✅    |
| ListActivities                         | ✅         | ✅    |
| ListExecutions                         | ✅         | ✅    |
| ListStateMachines                      | ✅         | ✅    |
| ListTagsForResource                    | ✅         | ❌    |
| SendTaskFailure                        | ✅         | ❌    |
| SendTaskHeartbeat                      | ✅         | ❌    |
| SendTaskSuccess                        | ✅         | ❌    |
| StartExecution                         | ✅         | ✅    |
| StartSyncExecution                     | ❌         | ❌    |
| StopExecution                          | ✅         | ❌    |
| TagResource                            | ✅         | ❌    |
| UntagResource                          | ✅         | ❌    |
| UpdateStateMachine                     | ✅         | ✅    |



## sts ##

API returns a response for 75.0% of the operations.

| Operation                              | Implemented | Tested |
|----------------------------------------|-------------|--------|
| AssumeRole                             | ✅         | ✅    |
| AssumeRoleWithSAML                     | ✅         | ✅    |
| AssumeRoleWithWebIdentity              | ✅         | ✅    |
| DecodeAuthorizationMessage             | ❌         | ❌    |
| GetAccessKeyInfo                       | ❌         | ❌    |
| GetCallerIdentity                      | ✅         | ✅    |
| GetFederationToken                     | ✅         | ✅    |
| GetSessionToken                        | ✅         | ✅    |



## support ##

API returns a response for 35.7% of the operations.

| Operation                              | Implemented | Tested |
|----------------------------------------|-------------|--------|
| AddAttachmentsToSet                    | ❌         | ❌    |
| AddCommunicationToCase                 | ❌         | ❌    |
| CreateCase                             | ✅         | ✅    |
| DescribeAttachment                     | ❌         | ❌    |
| DescribeCases                          | ✅         | ✅    |
| DescribeCommunications                 | ❌         | ❌    |
| DescribeServices                       | ❌         | ❌    |
| DescribeSeverityLevels                 | ❌         | ❌    |
| DescribeTrustedAdvisorCheckRefreshStatuses| ❌         | ❌    |
| DescribeTrustedAdvisorCheckResult      | ❌         | ❌    |
| DescribeTrustedAdvisorCheckSummaries   | ❌         | ❌    |
| DescribeTrustedAdvisorChecks           | ✅         | ❌    |
| RefreshTrustedAdvisorCheck             | ✅         | ❌    |
| ResolveCase                            | ✅         | ✅    |



## swf ##

API returns a response for 81.1% of the operations.

| Operation                              | Implemented | Tested |
|----------------------------------------|-------------|--------|
| CountClosedWorkflowExecutions          | ❌         | ❌    |
| CountOpenWorkflowExecutions            | ❌         | ❌    |
| CountPendingActivityTasks              | ✅         | ❌    |
| CountPendingDecisionTasks              | ✅         | ❌    |
| DeprecateActivityType                  | ✅         | ❌    |
| DeprecateDomain                        | ✅         | ❌    |
| DeprecateWorkflowType                  | ✅         | ❌    |
| DescribeActivityType                   | ✅         | ❌    |
| DescribeDomain                         | ✅         | ❌    |
| DescribeWorkflowExecution              | ✅         | ❌    |
| DescribeWorkflowType                   | ✅         | ❌    |
| GetWorkflowExecutionHistory            | ✅         | ✅    |
| ListActivityTypes                      | ✅         | ❌    |
| ListClosedWorkflowExecutions           | ✅         | ❌    |
| ListDomains                            | ✅         | ❌    |
| ListOpenWorkflowExecutions             | ✅         | ❌    |
| ListTagsForResource                    | ❌         | ❌    |
| ListWorkflowTypes                      | ✅         | ✅    |
| PollForActivityTask                    | ✅         | ✅    |
| PollForDecisionTask                    | ✅         | ✅    |
| RecordActivityTaskHeartbeat            | ✅         | ❌    |
| RegisterActivityType                   | ✅         | ✅    |
| RegisterDomain                         | ✅         | ✅    |
| RegisterWorkflowType                   | ✅         | ✅    |
| RequestCancelWorkflowExecution         | ❌         | ❌    |
| RespondActivityTaskCanceled            | ❌         | ❌    |
| RespondActivityTaskCompleted           | ✅         | ✅    |
| RespondActivityTaskFailed              | ✅         | ❌    |
| RespondDecisionTaskCompleted           | ✅         | ✅    |
| SignalWorkflowExecution                | ✅         | ❌    |
| StartWorkflowExecution                 | ✅         | ✅    |
| TagResource                            | ❌         | ❌    |
| TerminateWorkflowExecution             | ✅         | ❌    |
| UndeprecateActivityType                | ✅         | ❌    |
| UndeprecateDomain                      | ✅         | ❌    |
| UndeprecateWorkflowType                | ✅         | ❌    |
| UntagResource                          | ❌         | ❌    |



## timestream-query ##

API returns a response for 7.7% of the operations.

| Operation                              | Implemented | Tested |
|----------------------------------------|-------------|--------|
| CancelQuery                            | ❌         | ❌    |
| CreateScheduledQuery                   | ❌         | ❌    |
| DeleteScheduledQuery                   | ❌         | ❌    |
| DescribeEndpoints                      | ❌         | ❌    |
| DescribeScheduledQuery                 | ❌         | ❌    |
| ExecuteScheduledQuery                  | ❌         | ❌    |
| ListScheduledQueries                   | ❌         | ❌    |
| ListTagsForResource                    | ❌         | ❌    |
| PrepareQuery                           | ❌         | ❌    |
| Query                                  | ✅         | ✅    |
| TagResource                            | ❌         | ❌    |
| UntagResource                          | ❌         | ❌    |
| UpdateScheduledQuery                   | ❌         | ❌    |



## timestream-write ##

API returns a response for 60.0% of the operations.

| Operation                              | Implemented | Tested |
|----------------------------------------|-------------|--------|
| CreateDatabase                         | ✅         | ✅    |
| CreateTable                            | ✅         | ✅    |
| DeleteDatabase                         | ✅         | ✅    |
| DeleteTable                            | ✅         | ✅    |
| DescribeDatabase                       | ✅         | ✅    |
| DescribeEndpoints                      | ❌         | ❌    |
| DescribeTable                          | ✅         | ✅    |
| ListDatabases                          | ✅         | ✅    |
| ListTables                             | ✅         | ✅    |
| ListTagsForResource                    | ❌         | ❌    |
| TagResource                            | ❌         | ❌    |
| UntagResource                          | ❌         | ❌    |
| UpdateDatabase                         | ❌         | ❌    |
| UpdateTable                            | ❌         | ❌    |
| WriteRecords                           | ✅         | ✅    |



## transfer ##

API returns a response for 34.4% of the operations.

| Operation                              | Implemented | Tested |
|----------------------------------------|-------------|--------|
| CreateAccess                           | ❌         | ❌    |
| CreateServer                           | ✅         | ✅    |
| CreateUser                             | ✅         | ✅    |
| CreateWorkflow                         | ❌         | ❌    |
| DeleteAccess                           | ❌         | ❌    |
| DeleteServer                           | ✅         | ✅    |
| DeleteSshPublicKey                     | ✅         | ✅    |
| DeleteUser                             | ✅         | ✅    |
| DeleteWorkflow                         | ❌         | ❌    |
| DescribeAccess                         | ❌         | ❌    |
| DescribeExecution                      | ❌         | ❌    |
| DescribeSecurityPolicy                 | ❌         | ❌    |
| DescribeServer                         | ✅         | ✅    |
| DescribeUser                           | ✅         | ✅    |
| DescribeWorkflow                       | ❌         | ❌    |
| ImportSshPublicKey                     | ✅         | ✅    |
| ListAccesses                           | ❌         | ❌    |
| ListExecutions                         | ❌         | ❌    |
| ListSecurityPolicies                   | ❌         | ❌    |
| ListServers                            | ✅         | ❌    |
| ListTagsForResource                    | ❌         | ❌    |
| ListUsers                              | ✅         | ✅    |
| ListWorkflows                          | ❌         | ❌    |
| SendWorkflowStepState                  | ❌         | ❌    |
| StartServer                            | ❌         | ❌    |
| StopServer                             | ❌         | ❌    |
| TagResource                            | ❌         | ❌    |
| TestIdentityProvider                   | ❌         | ❌    |
| UntagResource                          | ❌         | ❌    |
| UpdateAccess                           | ❌         | ❌    |
| UpdateServer                           | ❌         | ❌    |
| UpdateUser                             | ✅         | ✅    |



## xray ##

API returns a response for 100.0% of the operations.

| Operation                              | Implemented | Tested |
|----------------------------------------|-------------|--------|
| BatchGetTraces                         | ✅         | ❌    |
| CreateGroup                            | ✅         | ❌    |
| CreateSamplingRule                     | ✅         | ✅    |
| DeleteGroup                            | ✅         | ❌    |
| DeleteSamplingRule                     | ✅         | ✅    |
| GetEncryptionConfig                    | ✅         | ❌    |
| GetGroup                               | ✅         | ❌    |
| GetGroups                              | ✅         | ❌    |
| GetInsight                             | ✅         | ❌    |
| GetInsightEvents                       | ✅         | ❌    |
| GetInsightImpactGraph                  | ✅         | ❌    |
| GetInsightSummaries                    | ✅         | ❌    |
| GetSamplingRules                       | ✅         | ✅    |
| GetSamplingStatisticSummaries          | ✅         | ❌    |
| GetSamplingTargets                     | ✅         | ❌    |
| GetServiceGraph                        | ✅         | ❌    |
| GetTimeSeriesServiceStatistics         | ✅         | ❌    |
| GetTraceGraph                          | ✅         | ❌    |
| GetTraceSummaries                      | ✅         | ✅    |
| ListTagsForResource                    | ✅         | ❌    |
| PutEncryptionConfig                    | ✅         | ❌    |
| PutTelemetryRecords                    | ✅         | ✅    |
| PutTraceSegments                       | ✅         | ✅    |
| TagResource                            | ✅         | ❌    |
| UntagResource                          | ✅         | ❌    |
| UpdateGroup                            | ✅         | ❌    |
| UpdateSamplingRule                     | ✅         | ✅    |



