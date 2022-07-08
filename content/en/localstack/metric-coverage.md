---
title: "LocalStack Metric Coverage"
linkTitle: "LocalStack Metric Coverage"
weight: 100
description: >
  Overview of the implemented AWS APIs and integration test coverage in LocalStack
---



## acm ##


| Operation                              | Implemented |
| -------------------------------------- | ----------: |
| AddTagsToCertificate                   | ✅         |
| DeleteCertificate ✨                    | ✅         |
| DescribeCertificate ✨                  | ✅         |
| ExportCertificate                      | ✅         |
| GetCertificate                         | ✅         |
| ImportCertificate ✨                    | ✅         |
| ListCertificates ✨                     | ✅         |
| ListTagsForCertificate ✨               | ✅         |
| RemoveTagsFromCertificate              | ✅         |
| RequestCertificate ✨                   | ✅         |
| ResendValidationEmail                  | ✅         |
| GetAccountConfiguration                | -         |
| PutAccountConfiguration                | -         |
| RenewCertificate                       | -         |
| UpdateCertificateOptions               | -         |



## amplify ##


| Operation                              | Implemented |
| -------------------------------------- | ----------: |
| CreateApp ✨                            | ✅         |
| CreateBackendEnvironment ✨             | ✅         |
| CreateBranch ✨                         | ✅         |
| CreateWebhook ✨                        | ✅         |
| DeleteApp ✨                            | ✅         |
| DeleteBackendEnvironment ✨             | ✅         |
| DeleteBranch ✨                         | ✅         |
| DeleteWebhook ✨                        | ✅         |
| GetApp ✨                               | ✅         |
| GetBackendEnvironment ✨                | ✅         |
| GetBranch ✨                            | ✅         |
| GetWebhook ✨                           | ✅         |
| ListApps ✨                             | ✅         |
| ListBranches ✨                         | ✅         |
| ListTagsForResource ✨                  | ✅         |
| TagResource ✨                          | ✅         |
| UntagResource ✨                        | ✅         |
| UpdateApp ✨                            | ✅         |
| UpdateWebhook ✨                        | ✅         |
| CreateDeployment                       | -         |
| CreateDomainAssociation                | -         |
| DeleteDomainAssociation                | -         |
| DeleteJob                              | -         |
| GenerateAccessLogs                     | -         |
| GetArtifactUrl                         | -         |
| GetDomainAssociation                   | -         |
| GetJob                                 | -         |
| ListArtifacts                          | -         |
| ListBackendEnvironments                | -         |
| ListDomainAssociations                 | -         |
| ListJobs                               | -         |
| ListWebhooks                           | -         |
| StartDeployment                        | -         |
| StartJob                               | -         |
| StopJob                                | -         |
| UpdateBranch                           | -         |
| UpdateDomainAssociation                | -         |



## apigateway ##


| Operation                              | Implemented |
| -------------------------------------- | ----------: |
| CreateApiKey ✨                         | ✅         |
| CreateAuthorizer ✨                     | ✅         |
| CreateBasePathMapping ✨                | ✅         |
| CreateDeployment ✨                     | ✅         |
| CreateDocumentationPart                | ✅         |
| CreateDomainName ✨                     | ✅         |
| CreateModel ✨                          | ✅         |
| CreateRequestValidator ✨               | ✅         |
| CreateResource ✨                       | ✅         |
| CreateRestApi ✨                        | ✅         |
| CreateStage ✨                          | ✅         |
| CreateUsagePlan ✨                      | ✅         |
| CreateUsagePlanKey ✨                   | ✅         |
| CreateVpcLink                          | ✅         |
| DeleteApiKey ✨                         | ✅         |
| DeleteAuthorizer ✨                     | ✅         |
| DeleteBasePathMapping ✨                | ✅         |
| DeleteClientCertificate                | ✅         |
| DeleteDeployment                       | ✅         |
| DeleteDocumentationPart                | ✅         |
| DeleteDomainName ✨                     | ✅         |
| DeleteGatewayResponse                  | ✅         |
| DeleteIntegration ✨                    | ✅         |
| DeleteIntegrationResponse ✨            | ✅         |
| DeleteMethod ✨                         | ✅         |
| DeleteMethodResponse ✨                 | ✅         |
| DeleteModel                            | ✅         |
| DeleteRequestValidator ✨               | ✅         |
| DeleteResource ✨                       | ✅         |
| DeleteRestApi ✨                        | ✅         |
| DeleteStage ✨                          | ✅         |
| DeleteUsagePlan                        | ✅         |
| DeleteUsagePlanKey                     | ✅         |
| DeleteVpcLink                          | ✅         |
| GenerateClientCertificate              | ✅         |
| GetAccount ✨                           | ✅         |
| GetApiKey                              | ✅         |
| GetApiKeys ✨                           | ✅         |
| GetAuthorizer ✨                        | ✅         |
| GetAuthorizers ✨                       | ✅         |
| GetBasePathMapping ✨                   | ✅         |
| GetBasePathMappings ✨                  | ✅         |
| GetClientCertificate                   | ✅         |
| GetClientCertificates                  | ✅         |
| GetDeployment ✨                        | ✅         |
| GetDeployments ✨                       | ✅         |
| GetDocumentationPart                   | ✅         |
| GetDocumentationParts                  | ✅         |
| GetDomainName ✨                        | ✅         |
| GetDomainNames ✨                       | ✅         |
| GetExport ✨                            | ✅         |
| GetGatewayResponse                     | ✅         |
| GetGatewayResponses                    | ✅         |
| GetIntegration ✨                       | ✅         |
| GetIntegrationResponse ✨               | ✅         |
| GetMethod ✨                            | ✅         |
| GetMethodResponse ✨                    | ✅         |
| GetModel ✨                             | ✅         |
| GetModels ✨                            | ✅         |
| GetRequestValidator ✨                  | ✅         |
| GetRequestValidators ✨                 | ✅         |
| GetResource ✨                          | ✅         |
| GetResources ✨                         | ✅         |
| GetRestApi ✨                           | ✅         |
| GetRestApis ✨                          | ✅         |
| GetStage ✨                             | ✅         |
| GetStages                              | ✅         |
| GetTags ✨                              | ✅         |
| GetUsagePlan                           | ✅         |
| GetUsagePlanKey                        | ✅         |
| GetUsagePlanKeys ✨                     | ✅         |
| GetUsagePlans ✨                        | ✅         |
| GetVpcLink                             | ✅         |
| GetVpcLinks                            | ✅         |
| ImportApiKeys                          | ✅         |
| ImportRestApi ✨                        | ✅         |
| PutGatewayResponse                     | ✅         |
| PutIntegration ✨                       | ✅         |
| PutIntegrationResponse ✨               | ✅         |
| PutMethod ✨                            | ✅         |
| PutMethodResponse ✨                    | ✅         |
| PutRestApi ✨                           | ✅         |
| TagResource ✨                          | ✅         |
| TestInvokeAuthorizer                   | ✅         |
| TestInvokeMethod ✨                     | ✅         |
| UntagResource                          | ✅         |
| UpdateAccount ✨                        | ✅         |
| UpdateApiKey                           | ✅         |
| UpdateAuthorizer ✨                     | ✅         |
| UpdateBasePathMapping ✨                | ✅         |
| UpdateClientCertificate                | ✅         |
| UpdateDeployment                       | ✅         |
| UpdateDocumentationPart                | ✅         |
| UpdateDomainName                       | ✅         |
| UpdateGatewayResponse                  | ✅         |
| UpdateIntegration                      | ✅         |
| UpdateIntegrationResponse              | ✅         |
| UpdateMethod ✨                         | ✅         |
| UpdateMethodResponse                   | ✅         |
| UpdateModel                            | ✅         |
| UpdateRequestValidator ✨               | ✅         |
| UpdateResource ✨                       | ✅         |
| UpdateRestApi ✨                        | ✅         |
| UpdateStage                            | ✅         |
| UpdateUsagePlan                        | ✅         |
| UpdateVpcLink                          | ✅         |
| CreateDocumentationVersion             | -         |
| DeleteDocumentationVersion             | -         |
| FlushStageAuthorizersCache             | -         |
| FlushStageCache                        | -         |
| GetDocumentationVersion                | -         |
| GetDocumentationVersions               | -         |
| GetModelTemplate                       | -         |
| GetSdk                                 | -         |
| GetSdkType                             | -         |
| GetSdkTypes                            | -         |
| GetUsage                               | -         |
| ImportDocumentationParts               | -         |
| UpdateDocumentationVersion             | -         |
| UpdateUsage                            | -         |



## apigatewaymanagementapi ##


| Operation                              | Implemented |
| -------------------------------------- | ----------: |
| DeleteConnection                       | ✅         |
| GetConnection                          | ✅         |
| PostToConnection ✨                     | ✅         |



## apigatewayv2 ##


| Operation                              | Implemented |
| -------------------------------------- | ----------: |
| CreateApi ✨                            | ✅         |
| CreateApiMapping ✨                     | ✅         |
| CreateAuthorizer ✨                     | ✅         |
| CreateDeployment ✨                     | ✅         |
| CreateDomainName ✨                     | ✅         |
| CreateIntegration ✨                    | ✅         |
| CreateIntegrationResponse ✨            | ✅         |
| CreateModel ✨                          | ✅         |
| CreateRoute ✨                          | ✅         |
| CreateRouteResponse ✨                  | ✅         |
| CreateStage ✨                          | ✅         |
| CreateVpcLink ✨                        | ✅         |
| DeleteApi ✨                            | ✅         |
| DeleteApiMapping                       | ✅         |
| DeleteAuthorizer ✨                     | ✅         |
| DeleteCorsConfiguration                | ✅         |
| DeleteDeployment ✨                     | ✅         |
| DeleteDomainName ✨                     | ✅         |
| DeleteIntegration ✨                    | ✅         |
| DeleteIntegrationResponse ✨            | ✅         |
| DeleteModel                            | ✅         |
| DeleteRoute ✨                          | ✅         |
| DeleteRouteResponse ✨                  | ✅         |
| DeleteStage ✨                          | ✅         |
| DeleteVpcLink ✨                        | ✅         |
| GetApi ✨                               | ✅         |
| GetApiMapping                          | ✅         |
| GetApiMappings                         | ✅         |
| GetApis ✨                              | ✅         |
| GetAuthorizer ✨                        | ✅         |
| GetAuthorizers ✨                       | ✅         |
| GetDeployment ✨                        | ✅         |
| GetDeployments ✨                       | ✅         |
| GetDomainName ✨                        | ✅         |
| GetDomainNames ✨                       | ✅         |
| GetIntegration ✨                       | ✅         |
| GetIntegrationResponse ✨               | ✅         |
| GetIntegrationResponses ✨              | ✅         |
| GetIntegrations ✨                      | ✅         |
| GetModel                               | ✅         |
| GetModels ✨                            | ✅         |
| GetRoute ✨                             | ✅         |
| GetRouteResponse ✨                     | ✅         |
| GetRouteResponses ✨                    | ✅         |
| GetRoutes ✨                            | ✅         |
| GetStage ✨                             | ✅         |
| GetStages                              | ✅         |
| GetTags                                | ✅         |
| GetVpcLink                             | ✅         |
| GetVpcLinks ✨                          | ✅         |
| ImportApi ✨                            | ✅         |
| ReimportApi ✨                          | ✅         |
| TagResource                            | ✅         |
| UntagResource                          | ✅         |
| UpdateApi                              | ✅         |
| UpdateApiMapping                       | ✅         |
| UpdateAuthorizer                       | ✅         |
| UpdateDeployment                       | ✅         |
| UpdateDomainName                       | ✅         |
| UpdateIntegration ✨                    | ✅         |
| UpdateIntegrationResponse ✨            | ✅         |
| UpdateModel                            | ✅         |
| UpdateRoute ✨                          | ✅         |
| UpdateRouteResponse ✨                  | ✅         |
| UpdateStage ✨                          | ✅         |
| UpdateVpcLink                          | ✅         |
| DeleteAccessLogSettings                | -         |
| DeleteRouteRequestParameter            | -         |
| DeleteRouteSettings                    | -         |
| ExportApi                              | -         |
| GetModelTemplate                       | -         |
| ResetAuthorizersCache                  | -         |



## appconfig ##


| Operation                              | Implemented |
| -------------------------------------- | ----------: |
| CreateApplication ✨                    | ✅         |
| CreateConfigurationProfile ✨           | ✅         |
| CreateDeploymentStrategy ✨             | ✅         |
| CreateEnvironment ✨                    | ✅         |
| CreateHostedConfigurationVersion ✨     | ✅         |
| DeleteApplication ✨                    | ✅         |
| DeleteConfigurationProfile ✨           | ✅         |
| DeleteDeploymentStrategy ✨             | ✅         |
| DeleteEnvironment ✨                    | ✅         |
| DeleteHostedConfigurationVersion ✨     | ✅         |
| GetApplication ✨                       | ✅         |
| GetConfiguration ✨                     | ✅         |
| GetConfigurationProfile ✨              | ✅         |
| GetDeployment                          | ✅         |
| GetDeploymentStrategy ✨                | ✅         |
| GetEnvironment ✨                       | ✅         |
| GetHostedConfigurationVersion ✨        | ✅         |
| ListApplications ✨                     | ✅         |
| ListConfigurationProfiles ✨            | ✅         |
| ListDeploymentStrategies ✨             | ✅         |
| ListDeployments ✨                      | ✅         |
| ListEnvironments ✨                     | ✅         |
| ListHostedConfigurationVersions ✨      | ✅         |
| ListTagsForResource                    | ✅         |
| StartDeployment ✨                      | ✅         |
| StopDeployment                         | ✅         |
| TagResource                            | ✅         |
| UntagResource                          | ✅         |
| UpdateApplication ✨                    | ✅         |
| UpdateConfigurationProfile ✨           | ✅         |
| UpdateDeploymentStrategy ✨             | ✅         |
| UpdateEnvironment ✨                    | ✅         |
| ValidateConfiguration ✨                | ✅         |



## application-autoscaling ##


| Operation                              | Implemented |
| -------------------------------------- | ----------: |
| DeleteScalingPolicy ✨                  | ✅         |
| DeleteScheduledAction                  | ✅         |
| DeregisterScalableTarget ✨             | ✅         |
| DescribeScalableTargets ✨              | ✅         |
| DescribeScalingPolicies ✨              | ✅         |
| DescribeScheduledActions               | ✅         |
| PutScalingPolicy ✨                     | ✅         |
| PutScheduledAction                     | ✅         |
| RegisterScalableTarget ✨               | ✅         |
| DescribeScalingActivities              | -         |



## appsync ##


| Operation                              | Implemented |
| -------------------------------------- | ----------: |
| CreateApiCache ✨                       | ✅         |
| CreateApiKey ✨                         | ✅         |
| CreateDataSource ✨                     | ✅         |
| CreateDomainName                       | ✅         |
| CreateFunction ✨                       | ✅         |
| CreateGraphqlApi ✨                     | ✅         |
| CreateResolver ✨                       | ✅         |
| CreateType                             | ✅         |
| DeleteApiCache                         | ✅         |
| DeleteApiKey                           | ✅         |
| DeleteDataSource                       | ✅         |
| DeleteDomainName                       | ✅         |
| DeleteFunction                         | ✅         |
| DeleteGraphqlApi ✨                     | ✅         |
| DeleteResolver ✨                       | ✅         |
| DeleteType                             | ✅         |
| FlushApiCache                          | ✅         |
| GetApiCache                            | ✅         |
| GetDataSource                          | ✅         |
| GetDomainName                          | ✅         |
| GetFunction ✨                          | ✅         |
| GetGraphqlApi ✨                        | ✅         |
| GetIntrospectionSchema ✨               | ✅         |
| GetResolver ✨                          | ✅         |
| GetSchemaCreationStatus ✨              | ✅         |
| GetType                                | ✅         |
| ListApiKeys ✨                          | ✅         |
| ListDataSources ✨                      | ✅         |
| ListDomainNames                        | ✅         |
| ListFunctions ✨                        | ✅         |
| ListGraphqlApis ✨                      | ✅         |
| ListResolvers ✨                        | ✅         |
| ListResolversByFunction                | ✅         |
| ListTagsForResource ✨                  | ✅         |
| ListTypes                              | ✅         |
| StartSchemaCreation ✨                  | ✅         |
| TagResource ✨                          | ✅         |
| UntagResource                          | ✅         |
| UpdateApiCache ✨                       | ✅         |
| UpdateApiKey ✨                         | ✅         |
| UpdateDataSource                       | ✅         |
| UpdateDomainName                       | ✅         |
| UpdateFunction                         | ✅         |
| UpdateGraphqlApi                       | ✅         |
| UpdateResolver ✨                       | ✅         |
| UpdateType                             | ✅         |
| AssociateApi                           | -         |
| DisassociateApi                        | -         |
| GetApiAssociation                      | -         |



## athena ##


| Operation                              | Implemented |
| -------------------------------------- | ----------: |
| BatchGetPreparedStatement              | ✅         |
| CreateDataCatalog ✨                    | ✅         |
| CreateNamedQuery ✨                     | ✅         |
| CreateWorkGroup ✨                      | ✅         |
| DeleteDataCatalog ✨                    | ✅         |
| DeleteNamedQuery ✨                     | ✅         |
| DeleteWorkGroup ✨                      | ✅         |
| GetDataCatalog ✨                       | ✅         |
| GetDatabase                            | ✅         |
| GetNamedQuery                          | ✅         |
| GetQueryExecution                      | ✅         |
| GetQueryResults                        | ✅         |
| GetWorkGroup ✨                         | ✅         |
| ListDataCatalogs ✨                     | ✅         |
| ListDatabases                          | ✅         |
| ListNamedQueries ✨                     | ✅         |
| ListQueryExecutions                    | ✅         |
| ListTagsForResource ✨                  | ✅         |
| ListWorkGroups ✨                       | ✅         |
| StartQueryExecution                    | ✅         |
| TagResource ✨                          | ✅         |
| UntagResource ✨                        | ✅         |
| BatchGetNamedQuery                     | -         |
| BatchGetQueryExecution                 | -         |
| CreatePreparedStatement                | -         |
| DeletePreparedStatement                | -         |
| GetPreparedStatement                   | -         |
| GetTableMetadata                       | -         |
| ListEngineVersions                     | -         |
| ListPreparedStatements                 | -         |
| ListTableMetadata                      | -         |
| StopQueryExecution                     | -         |
| UpdateDataCatalog                      | -         |
| UpdateNamedQuery                       | -         |
| UpdatePreparedStatement                | -         |
| UpdateWorkGroup                        | -         |



## autoscaling ##


| Operation                              | Implemented |
| -------------------------------------- | ----------: |
| AttachInstances                        | ✅         |
| AttachLoadBalancerTargetGroups         | ✅         |
| AttachLoadBalancers                    | ✅         |
| CreateAutoScalingGroup                 | ✅         |
| CreateLaunchConfiguration              | ✅         |
| CreateOrUpdateTags                     | ✅         |
| DeleteAutoScalingGroup                 | ✅         |
| DeleteLaunchConfiguration              | ✅         |
| DeleteLifecycleHook                    | ✅         |
| DeletePolicy                           | ✅         |
| DeleteTags                             | ✅         |
| DescribeAutoScalingGroups              | ✅         |
| DescribeAutoScalingInstances           | ✅         |
| DescribeLaunchConfigurations           | ✅         |
| DescribeLifecycleHooks                 | ✅         |
| DescribeLoadBalancerTargetGroups       | ✅         |
| DescribeLoadBalancers                  | ✅         |
| DescribeMetricCollectionTypes ✨        | ✅         |
| DescribePolicies                       | ✅         |
| DescribeTags                           | ✅         |
| DetachInstances                        | ✅         |
| DetachLoadBalancerTargetGroups         | ✅         |
| DetachLoadBalancers                    | ✅         |
| DisableMetricsCollection ✨             | ✅         |
| EnableMetricsCollection ✨              | ✅         |
| EnterStandby                           | ✅         |
| ExecutePolicy                          | ✅         |
| ExitStandby                            | ✅         |
| PutLifecycleHook                       | ✅         |
| PutScalingPolicy                       | ✅         |
| ResumeProcesses                        | ✅         |
| SetDesiredCapacity                     | ✅         |
| SetInstanceHealth                      | ✅         |
| SetInstanceProtection                  | ✅         |
| SuspendProcesses                       | ✅         |
| TerminateInstanceInAutoScalingGroup    | ✅         |
| UpdateAutoScalingGroup                 | ✅         |
| BatchDeleteScheduledAction             | -         |
| BatchPutScheduledUpdateGroupAction     | -         |
| CancelInstanceRefresh                  | -         |
| CompleteLifecycleAction                | -         |
| DeleteNotificationConfiguration        | -         |
| DeleteScheduledAction                  | -         |
| DeleteWarmPool                         | -         |
| DescribeAccountLimits                  | -         |
| DescribeAdjustmentTypes                | -         |
| DescribeAutoScalingNotificationTypes   | -         |
| DescribeInstanceRefreshes              | -         |
| DescribeLifecycleHookTypes             | -         |
| DescribeNotificationConfigurations     | -         |
| DescribeScalingActivities              | -         |
| DescribeScalingProcessTypes            | -         |
| DescribeScheduledActions               | -         |
| DescribeTerminationPolicyTypes         | -         |
| DescribeWarmPool                       | -         |
| GetPredictiveScalingForecast           | -         |
| PutNotificationConfiguration           | -         |
| PutScheduledUpdateGroupAction          | -         |
| PutWarmPool                            | -         |
| RecordLifecycleActionHeartbeat         | -         |
| StartInstanceRefresh                   | -         |



## backup ##


| Operation                              | Implemented |
| -------------------------------------- | ----------: |
| CreateBackupPlan ✨                     | ✅         |
| CreateBackupSelection ✨                | ✅         |
| CreateBackupVault ✨                    | ✅         |
| DeleteBackupPlan ✨                     | ✅         |
| DeleteBackupSelection ✨                | ✅         |
| DeleteBackupVault ✨                    | ✅         |
| DescribeBackupVault ✨                  | ✅         |
| DescribeRestoreJob ✨                   | ✅         |
| GetBackupPlan ✨                        | ✅         |
| GetBackupSelection ✨                   | ✅         |
| ListBackupJobs                         | ✅         |
| ListBackupPlans ✨                      | ✅         |
| ListBackupSelections ✨                 | ✅         |
| ListBackupVaults ✨                     | ✅         |
| ListCopyJobs                           | ✅         |
| ListRecoveryPointsByBackupVault ✨      | ✅         |
| ListRecoveryPointsByResource ✨         | ✅         |
| ListReportJobs                         | ✅         |
| ListRestoreJobs                        | ✅         |
| StartRestoreJob ✨                      | ✅         |
| UpdateBackupPlan ✨                     | ✅         |
| CreateFramework                        | -         |
| CreateReportPlan                       | -         |
| DeleteBackupVaultAccessPolicy          | -         |
| DeleteBackupVaultLockConfiguration     | -         |
| DeleteBackupVaultNotifications         | -         |
| DeleteFramework                        | -         |
| DeleteRecoveryPoint                    | -         |
| DeleteReportPlan                       | -         |
| DescribeBackupJob                      | -         |
| DescribeCopyJob                        | -         |
| DescribeFramework                      | -         |
| DescribeGlobalSettings                 | -         |
| DescribeProtectedResource              | -         |
| DescribeRecoveryPoint                  | -         |
| DescribeRegionSettings                 | -         |
| DescribeReportJob                      | -         |
| DescribeReportPlan                     | -         |
| DisassociateRecoveryPoint              | -         |
| ExportBackupPlanTemplate               | -         |
| GetBackupPlanFromJSON                  | -         |
| GetBackupPlanFromTemplate              | -         |
| GetBackupVaultAccessPolicy             | -         |
| GetBackupVaultNotifications            | -         |
| GetRecoveryPointRestoreMetadata        | -         |
| GetSupportedResourceTypes              | -         |
| ListBackupPlanTemplates                | -         |
| ListBackupPlanVersions                 | -         |
| ListFrameworks                         | -         |
| ListProtectedResources                 | -         |
| ListReportPlans                        | -         |
| ListTags                               | -         |
| PutBackupVaultAccessPolicy             | -         |
| PutBackupVaultLockConfiguration        | -         |
| PutBackupVaultNotifications            | -         |
| StartBackupJob                         | -         |
| StartCopyJob                           | -         |
| StartReportJob                         | -         |
| StopBackupJob                          | -         |
| TagResource                            | -         |
| UntagResource                          | -         |
| UpdateFramework                        | -         |
| UpdateGlobalSettings                   | -         |
| UpdateRecoveryPointLifecycle           | -         |
| UpdateRegionSettings                   | -         |
| UpdateReportPlan                       | -         |



## batch ##


| Operation                              | Implemented |
| -------------------------------------- | ----------: |
| CancelJob                              | ✅         |
| CreateComputeEnvironment ✨             | ✅         |
| CreateJobQueue ✨                       | ✅         |
| CreateSchedulingPolicy                 | ✅         |
| DeleteComputeEnvironment               | ✅         |
| DeleteJobQueue ✨                       | ✅         |
| DeleteSchedulingPolicy                 | ✅         |
| DeregisterJobDefinition ✨              | ✅         |
| DescribeComputeEnvironments            | ✅         |
| DescribeJobDefinitions ✨               | ✅         |
| DescribeJobQueues                      | ✅         |
| DescribeJobs ✨                         | ✅         |
| DescribeSchedulingPolicies             | ✅         |
| ListJobs                               | ✅         |
| ListSchedulingPolicies                 | ✅         |
| ListTagsForResource                    | ✅         |
| RegisterJobDefinition ✨                | ✅         |
| SubmitJob ✨                            | ✅         |
| TagResource                            | ✅         |
| TerminateJob                           | ✅         |
| UntagResource                          | ✅         |
| UpdateComputeEnvironment               | ✅         |
| UpdateJobQueue                         | ✅         |
| UpdateSchedulingPolicy                 | ✅         |



## ce ##


| Operation                              | Implemented |
| -------------------------------------- | ----------: |
| CreateAnomalyMonitor ✨                 | ✅         |
| CreateAnomalySubscription ✨            | ✅         |
| CreateCostCategoryDefinition ✨         | ✅         |
| DeleteAnomalyMonitor ✨                 | ✅         |
| DeleteAnomalySubscription ✨            | ✅         |
| DeleteCostCategoryDefinition ✨         | ✅         |
| DescribeCostCategoryDefinition ✨       | ✅         |
| GetAnomalyMonitors ✨                   | ✅         |
| GetAnomalySubscriptions ✨              | ✅         |
| UpdateAnomalyMonitor ✨                 | ✅         |
| UpdateAnomalySubscription ✨            | ✅         |
| UpdateCostCategoryDefinition ✨         | ✅         |
| GetAnomalies                           | -         |
| GetCostAndUsage                        | -         |
| GetCostAndUsageWithResources           | -         |
| GetCostCategories                      | -         |
| GetCostForecast                        | -         |
| GetDimensionValues                     | -         |
| GetReservationCoverage                 | -         |
| GetReservationPurchaseRecommendation   | -         |
| GetReservationUtilization              | -         |
| GetRightsizingRecommendation           | -         |
| GetSavingsPlansCoverage                | -         |
| GetSavingsPlansPurchaseRecommendation  | -         |
| GetSavingsPlansUtilization             | -         |
| GetSavingsPlansUtilizationDetails      | -         |
| GetTags                                | -         |
| GetUsageForecast                       | -         |
| ListCostAllocationTags                 | -         |
| ListCostCategoryDefinitions            | -         |
| ListTagsForResource                    | -         |
| ProvideAnomalyFeedback                 | -         |
| TagResource                            | -         |
| UntagResource                          | -         |
| UpdateCostAllocationTagsStatus         | -         |



## cloudformation ##


| Operation                              | Implemented |
| -------------------------------------- | ----------: |
| CreateChangeSet ✨                      | ✅         |
| CreateStack ✨                          | ✅         |
| CreateStackInstances                   | ✅         |
| CreateStackSet                         | ✅         |
| DeleteChangeSet ✨                      | ✅         |
| DeleteStack ✨                          | ✅         |
| DeleteStackSet                         | ✅         |
| DescribeChangeSet ✨                    | ✅         |
| DescribeStackEvents ✨                  | ✅         |
| DescribeStackResource ✨                | ✅         |
| DescribeStackResources ✨               | ✅         |
| DescribeStackSet                       | ✅         |
| DescribeStackSetOperation              | ✅         |
| DescribeStacks ✨                       | ✅         |
| ExecuteChangeSet ✨                     | ✅         |
| GetTemplate ✨                          | ✅         |
| GetTemplateSummary ✨                   | ✅         |
| ListChangeSets                         | ✅         |
| ListExports ✨                          | ✅         |
| ListImports                            | ✅         |
| ListStackInstances                     | ✅         |
| ListStackResources ✨                   | ✅         |
| ListStackSets                          | ✅         |
| ListStacks ✨                           | ✅         |
| UpdateStack ✨                          | ✅         |
| UpdateStackSet                         | ✅         |
| ValidateTemplate ✨                     | ✅         |
| ActivateType                           | -         |
| BatchDescribeTypeConfigurations        | -         |
| CancelUpdateStack                      | -         |
| ContinueUpdateRollback                 | -         |
| DeactivateType                         | -         |
| DeleteStackInstances                   | -         |
| DeregisterType                         | -         |
| DescribeAccountLimits                  | -         |
| DescribeChangeSetHooks                 | -         |
| DescribePublisher                      | -         |
| DescribeStackDriftDetectionStatus      | -         |
| DescribeStackInstance                  | -         |
| DescribeStackResourceDrifts            | -         |
| DescribeType                           | -         |
| DescribeTypeRegistration               | -         |
| DetectStackDrift                       | -         |
| DetectStackResourceDrift               | -         |
| DetectStackSetDrift                    | -         |
| EstimateTemplateCost                   | -         |
| GetStackPolicy                         | -         |
| ImportStacksToStackSet                 | -         |
| ListStackSetOperationResults           | -         |
| ListStackSetOperations                 | -         |
| ListTypeRegistrations                  | -         |
| ListTypeVersions                       | -         |
| ListTypes                              | -         |
| PublishType                            | -         |
| RecordHandlerProgress                  | -         |
| RegisterPublisher                      | -         |
| RegisterType                           | -         |
| RollbackStack                          | -         |
| SetStackPolicy                         | -         |
| SetTypeConfiguration                   | -         |
| SetTypeDefaultVersion                  | -         |
| SignalResource                         | -         |
| StopStackSetOperation                  | -         |
| TestType                               | -         |
| UpdateStackInstances                   | -         |
| UpdateTerminationProtection            | -         |



## cloudfront ##


| Operation                              | Implemented |
| -------------------------------------- | ----------: |
| CreateCloudFrontOriginAccessIdentity ✨ | ✅         |
| CreateDistribution ✨                   | ✅         |
| CreateDistributionWithTags ✨           | ✅         |
| CreateFunction ✨                       | ✅         |
| CreateInvalidation ✨                   | ✅         |
| CreateOriginRequestPolicy ✨            | ✅         |
| DeleteCloudFrontOriginAccessIdentity ✨ | ✅         |
| DeleteDistribution ✨                   | ✅         |
| DeleteFunction ✨                       | ✅         |
| DeleteOriginRequestPolicy ✨            | ✅         |
| GetCloudFrontOriginAccessIdentity ✨    | ✅         |
| GetDistribution                        | ✅         |
| GetFunction ✨                          | ✅         |
| GetInvalidation ✨                      | ✅         |
| GetOriginRequestPolicy ✨               | ✅         |
| ListCloudFrontOriginAccessIdentities ✨ | ✅         |
| ListDistributions ✨                    | ✅         |
| ListFunctions ✨                        | ✅         |
| ListInvalidations ✨                    | ✅         |
| ListOriginRequestPolicies ✨            | ✅         |
| ListTagsForResource ✨                  | ✅         |
| TagResource                            | ✅         |
| UntagResource ✨                        | ✅         |
| UpdateDistribution                     | ✅         |
| UpdateFunction ✨                       | ✅         |
| UpdateOriginRequestPolicy ✨            | ✅         |
| AssociateAlias                         | -         |
| CreateCachePolicy                      | -         |
| CreateFieldLevelEncryptionConfig       | -         |
| CreateFieldLevelEncryptionProfile      | -         |
| CreateKeyGroup                         | -         |
| CreateMonitoringSubscription           | -         |
| CreatePublicKey                        | -         |
| CreateRealtimeLogConfig                | -         |
| CreateResponseHeadersPolicy            | -         |
| CreateStreamingDistribution            | -         |
| CreateStreamingDistributionWithTags    | -         |
| DeleteCachePolicy                      | -         |
| DeleteFieldLevelEncryptionConfig       | -         |
| DeleteFieldLevelEncryptionProfile      | -         |
| DeleteKeyGroup                         | -         |
| DeleteMonitoringSubscription           | -         |
| DeletePublicKey                        | -         |
| DeleteRealtimeLogConfig                | -         |
| DeleteResponseHeadersPolicy            | -         |
| DeleteStreamingDistribution            | -         |
| DescribeFunction                       | -         |
| GetCachePolicy                         | -         |
| GetCachePolicyConfig                   | -         |
| GetCloudFrontOriginAccessIdentityConfig | -         |
| GetDistributionConfig                  | -         |
| GetFieldLevelEncryption                | -         |
| GetFieldLevelEncryptionConfig          | -         |
| GetFieldLevelEncryptionProfile         | -         |
| GetFieldLevelEncryptionProfileConfig   | -         |
| GetKeyGroup                            | -         |
| GetKeyGroupConfig                      | -         |
| GetMonitoringSubscription              | -         |
| GetOriginRequestPolicyConfig           | -         |
| GetPublicKey                           | -         |
| GetPublicKeyConfig                     | -         |
| GetRealtimeLogConfig                   | -         |
| GetResponseHeadersPolicy               | -         |
| GetResponseHeadersPolicyConfig         | -         |
| GetStreamingDistribution               | -         |
| GetStreamingDistributionConfig         | -         |
| ListCachePolicies                      | -         |
| ListConflictingAliases                 | -         |
| ListDistributionsByCachePolicyId       | -         |
| ListDistributionsByKeyGroup            | -         |
| ListDistributionsByOriginRequestPolicyId | -         |
| ListDistributionsByRealtimeLogConfig   | -         |
| ListDistributionsByResponseHeadersPolicyId | -         |
| ListDistributionsByWebACLId            | -         |
| ListFieldLevelEncryptionConfigs        | -         |
| ListFieldLevelEncryptionProfiles       | -         |
| ListKeyGroups                          | -         |
| ListPublicKeys                         | -         |
| ListRealtimeLogConfigs                 | -         |
| ListResponseHeadersPolicies            | -         |
| ListStreamingDistributions             | -         |
| PublishFunction                        | -         |
| TestFunction                           | -         |
| UpdateCachePolicy                      | -         |
| UpdateCloudFrontOriginAccessIdentity   | -         |
| UpdateFieldLevelEncryptionConfig       | -         |
| UpdateFieldLevelEncryptionProfile      | -         |
| UpdateKeyGroup                         | -         |
| UpdatePublicKey                        | -         |
| UpdateRealtimeLogConfig                | -         |
| UpdateResponseHeadersPolicy            | -         |
| UpdateStreamingDistribution            | -         |



## cloudtrail ##


| Operation                              | Implemented |
| -------------------------------------- | ----------: |
| AddTags                                | ✅         |
| CreateTrail ✨                          | ✅         |
| DeleteTrail ✨                          | ✅         |
| DescribeTrails ✨                       | ✅         |
| GetEventSelectors                      | ✅         |
| GetInsightSelectors                    | ✅         |
| GetTrail ✨                             | ✅         |
| GetTrailStatus ✨                       | ✅         |
| ListTags ✨                             | ✅         |
| ListTrails ✨                           | ✅         |
| LookupEvents ✨                         | ✅         |
| PutEventSelectors ✨                    | ✅         |
| PutInsightSelectors                    | ✅         |
| RemoveTags                             | ✅         |
| StartLogging ✨                         | ✅         |
| StopLogging ✨                          | ✅         |
| UpdateTrail ✨                          | ✅         |
| CancelQuery                            | -         |
| CreateEventDataStore                   | -         |
| DeleteEventDataStore                   | -         |
| DescribeQuery                          | -         |
| GetEventDataStore                      | -         |
| GetQueryResults                        | -         |
| ListEventDataStores                    | -         |
| ListPublicKeys                         | -         |
| ListQueries                            | -         |
| RestoreEventDataStore                  | -         |
| StartQuery                             | -         |
| UpdateEventDataStore                   | -         |



## cloudwatch ##


| Operation                              | Implemented |
| -------------------------------------- | ----------: |
| DeleteAlarms ✨                         | ✅         |
| DeleteDashboards                       | ✅         |
| DescribeAlarms ✨                       | ✅         |
| DescribeAlarmsForMetric                | ✅         |
| GetDashboard                           | ✅         |
| GetMetricData ✨                        | ✅         |
| GetMetricStatistics ✨                  | ✅         |
| ListDashboards                         | ✅         |
| ListMetrics ✨                          | ✅         |
| ListTagsForResource ✨                  | ✅         |
| PutCompositeAlarm ✨                    | ✅         |
| PutDashboard                           | ✅         |
| PutMetricAlarm ✨                       | ✅         |
| PutMetricData ✨                        | ✅         |
| SetAlarmState ✨                        | ✅         |
| TagResource ✨                          | ✅         |
| UntagResource ✨                        | ✅         |
| DeleteAnomalyDetector                  | -         |
| DeleteInsightRules                     | -         |
| DeleteMetricStream                     | -         |
| DescribeAlarmHistory                   | -         |
| DescribeAnomalyDetectors               | -         |
| DescribeInsightRules                   | -         |
| DisableAlarmActions                    | -         |
| DisableInsightRules                    | -         |
| EnableAlarmActions                     | -         |
| EnableInsightRules                     | -         |
| GetInsightRuleReport                   | -         |
| GetMetricStream                        | -         |
| GetMetricWidgetImage                   | -         |
| ListMetricStreams                      | -         |
| PutAnomalyDetector                     | -         |
| PutInsightRule                         | -         |
| PutMetricStream                        | -         |
| StartMetricStreams                     | -         |
| StopMetricStreams                      | -         |



## codecommit ##


| Operation                              | Implemented |
| -------------------------------------- | ----------: |
| CreateBranch ✨                         | ✅         |
| CreateCommit ✨                         | ✅         |
| CreatePullRequest ✨                    | ✅         |
| CreateRepository ✨                     | ✅         |
| DeleteBranch ✨                         | ✅         |
| DeleteRepository ✨                     | ✅         |
| GetBranch ✨                            | ✅         |
| GetFile ✨                              | ✅         |
| GetFolder ✨                            | ✅         |
| GetRepository ✨                        | ✅         |
| ListPullRequests ✨                     | ✅         |
| ListRepositories                       | ✅         |
| ListTagsForResource                    | ✅         |
| TagResource                            | ✅         |
| AssociateApprovalRuleTemplateWithRepository | -         |
| BatchAssociateApprovalRuleTemplateWithRepositories | -         |
| BatchDescribeMergeConflicts            | -         |
| BatchDisassociateApprovalRuleTemplateFromRepositories | -         |
| BatchGetCommits                        | -         |
| BatchGetRepositories                   | -         |
| CreateApprovalRuleTemplate             | -         |
| CreatePullRequestApprovalRule          | -         |
| CreateUnreferencedMergeCommit          | -         |
| DeleteApprovalRuleTemplate             | -         |
| DeleteCommentContent                   | -         |
| DeleteFile                             | -         |
| DeletePullRequestApprovalRule          | -         |
| DescribeMergeConflicts                 | -         |
| DescribePullRequestEvents              | -         |
| DisassociateApprovalRuleTemplateFromRepository | -         |
| EvaluatePullRequestApprovalRules       | -         |
| GetApprovalRuleTemplate                | -         |
| GetBlob                                | -         |
| GetComment                             | -         |
| GetCommentReactions                    | -         |
| GetCommentsForComparedCommit           | -         |
| GetCommentsForPullRequest              | -         |
| GetCommit                              | -         |
| GetDifferences                         | -         |
| GetMergeCommit                         | -         |
| GetMergeConflicts                      | -         |
| GetMergeOptions                        | -         |
| GetPullRequest                         | -         |
| GetPullRequestApprovalStates           | -         |
| GetPullRequestOverrideState            | -         |
| GetRepositoryTriggers                  | -         |
| ListApprovalRuleTemplates              | -         |
| ListAssociatedApprovalRuleTemplatesForRepository | -         |
| ListBranches                           | -         |
| ListRepositoriesForApprovalRuleTemplate | -         |
| MergeBranchesByFastForward             | -         |
| MergeBranchesBySquash                  | -         |
| MergeBranchesByThreeWay                | -         |
| MergePullRequestByFastForward          | -         |
| MergePullRequestBySquash               | -         |
| MergePullRequestByThreeWay             | -         |
| OverridePullRequestApprovalRules       | -         |
| PostCommentForComparedCommit           | -         |
| PostCommentForPullRequest              | -         |
| PostCommentReply                       | -         |
| PutCommentReaction                     | -         |
| PutFile                                | -         |
| PutRepositoryTriggers                  | -         |
| TestRepositoryTriggers                 | -         |
| UntagResource                          | -         |
| UpdateApprovalRuleTemplateContent      | -         |
| UpdateApprovalRuleTemplateDescription  | -         |
| UpdateApprovalRuleTemplateName         | -         |
| UpdateComment                          | -         |
| UpdateDefaultBranch                    | -         |
| UpdatePullRequestApprovalRuleContent   | -         |
| UpdatePullRequestApprovalState         | -         |
| UpdatePullRequestDescription           | -         |
| UpdatePullRequestStatus                | -         |
| UpdatePullRequestTitle                 | -         |
| UpdateRepositoryDescription            | -         |
| UpdateRepositoryName                   | -         |



## cognito-identity ##


| Operation                              | Implemented |
| -------------------------------------- | ----------: |
| CreateIdentityPool ✨                   | ✅         |
| DeleteIdentityPool ✨                   | ✅         |
| DescribeIdentityPool                   | ✅         |
| GetCredentialsForIdentity ✨            | ✅         |
| GetId ✨                                | ✅         |
| GetIdentityPoolRoles ✨                 | ✅         |
| GetOpenIdToken                         | ✅         |
| GetOpenIdTokenForDeveloperIdentity     | ✅         |
| ListIdentities                         | ✅         |
| ListIdentityPools ✨                    | ✅         |
| SetIdentityPoolRoles ✨                 | ✅         |
| UpdateIdentityPool                     | ✅         |
| DeleteIdentities                       | -         |
| DescribeIdentity                       | -         |
| GetPrincipalTagAttributeMap            | -         |
| ListTagsForResource                    | -         |
| LookupDeveloperIdentity                | -         |
| MergeDeveloperIdentities               | -         |
| SetPrincipalTagAttributeMap            | -         |
| TagResource                            | -         |
| UnlinkDeveloperIdentity                | -         |
| UnlinkIdentity                         | -         |
| UntagResource                          | -         |



## cognito-idp ##


| Operation                              | Implemented |
| -------------------------------------- | ----------: |
| AddCustomAttributes                    | ✅         |
| AdminAddUserToGroup ✨                  | ✅         |
| AdminConfirmSignUp ✨                   | ✅         |
| AdminCreateUser ✨                      | ✅         |
| AdminDeleteUser ✨                      | ✅         |
| AdminDeleteUserAttributes ✨            | ✅         |
| AdminDisableUser ✨                     | ✅         |
| AdminEnableUser                        | ✅         |
| AdminGetUser ✨                         | ✅         |
| AdminInitiateAuth ✨                    | ✅         |
| AdminListGroupsForUser ✨               | ✅         |
| AdminRemoveUserFromGroup               | ✅         |
| AdminResetUserPassword                 | ✅         |
| AdminRespondToAuthChallenge ✨          | ✅         |
| AdminSetUserMFAPreference ✨            | ✅         |
| AdminSetUserPassword ✨                 | ✅         |
| AdminUpdateUserAttributes ✨            | ✅         |
| AdminUserGlobalSignOut ✨               | ✅         |
| ChangePassword ✨                       | ✅         |
| ConfirmDevice                          | ✅         |
| ConfirmForgotPassword ✨                | ✅         |
| ConfirmSignUp                          | ✅         |
| CreateGroup ✨                          | ✅         |
| CreateIdentityProvider ✨               | ✅         |
| CreateResourceServer ✨                 | ✅         |
| CreateUserPool ✨                       | ✅         |
| CreateUserPoolClient ✨                 | ✅         |
| CreateUserPoolDomain                   | ✅         |
| DeleteGroup ✨                          | ✅         |
| DeleteIdentityProvider ✨               | ✅         |
| DeleteResourceServer ✨                 | ✅         |
| DeleteUserAttributes ✨                 | ✅         |
| DeleteUserPool ✨                       | ✅         |
| DeleteUserPoolClient ✨                 | ✅         |
| DeleteUserPoolDomain                   | ✅         |
| DescribeIdentityProvider ✨             | ✅         |
| DescribeResourceServer ✨               | ✅         |
| DescribeUserPool ✨                     | ✅         |
| DescribeUserPoolClient ✨               | ✅         |
| DescribeUserPoolDomain                 | ✅         |
| ForgotPassword ✨                       | ✅         |
| GetGroup                               | ✅         |
| GetSigningCertificate ✨                | ✅         |
| GetUser ✨                              | ✅         |
| GetUserPoolMfaConfig ✨                 | ✅         |
| GlobalSignOut ✨                        | ✅         |
| InitiateAuth ✨                         | ✅         |
| ListGroups ✨                           | ✅         |
| ListIdentityProviders ✨                | ✅         |
| ListResourceServers ✨                  | ✅         |
| ListUserPoolClients ✨                  | ✅         |
| ListUserPools ✨                        | ✅         |
| ListUsers ✨                            | ✅         |
| ListUsersInGroup ✨                     | ✅         |
| RespondToAuthChallenge ✨               | ✅         |
| SetUserMFAPreference ✨                 | ✅         |
| SetUserPoolMfaConfig ✨                 | ✅         |
| SignUp ✨                               | ✅         |
| UpdateGroup                            | ✅         |
| UpdateIdentityProvider ✨               | ✅         |
| UpdateResourceServer                   | ✅         |
| UpdateUserAttributes                   | ✅         |
| UpdateUserPool ✨                       | ✅         |
| UpdateUserPoolClient                   | ✅         |
| AdminDisableProviderForUser            | -         |
| AdminForgetDevice                      | -         |
| AdminGetDevice                         | -         |
| AdminLinkProviderForUser               | -         |
| AdminListDevices                       | -         |
| AdminListUserAuthEvents                | -         |
| AdminSetUserSettings                   | -         |
| AdminUpdateAuthEventFeedback           | -         |
| AdminUpdateDeviceStatus                | -         |
| AssociateSoftwareToken                 | -         |
| CreateUserImportJob                    | -         |
| DeleteUser                             | -         |
| DescribeRiskConfiguration              | -         |
| DescribeUserImportJob                  | -         |
| ForgetDevice                           | -         |
| GetCSVHeader                           | -         |
| GetDevice                              | -         |
| GetIdentityProviderByIdentifier        | -         |
| GetUICustomization                     | -         |
| GetUserAttributeVerificationCode       | -         |
| ListDevices                            | -         |
| ListTagsForResource                    | -         |
| ListUserImportJobs                     | -         |
| ResendConfirmationCode                 | -         |
| RevokeToken                            | -         |
| SetRiskConfiguration                   | -         |
| SetUICustomization                     | -         |
| SetUserSettings                        | -         |
| StartUserImportJob                     | -         |
| StopUserImportJob                      | -         |
| TagResource                            | -         |
| UntagResource                          | -         |
| UpdateAuthEventFeedback                | -         |
| UpdateDeviceStatus                     | -         |
| UpdateUserPoolDomain                   | -         |
| VerifySoftwareToken                    | -         |
| VerifyUserAttribute                    | -         |



## config ##


| Operation                              | Implemented |
| -------------------------------------- | ----------: |
| BatchGetAggregateResourceConfig        | ✅         |
| BatchGetResourceConfig                 | ✅         |
| DeleteAggregationAuthorization         | ✅         |
| DeleteConfigRule                       | ✅         |
| DeleteConfigurationAggregator          | ✅         |
| DeleteConfigurationRecorder ✨          | ✅         |
| DeleteDeliveryChannel ✨                | ✅         |
| DeleteOrganizationConformancePack      | ✅         |
| DescribeAggregationAuthorizations      | ✅         |
| DescribeConfigRules                    | ✅         |
| DescribeConfigurationAggregators       | ✅         |
| DescribeConfigurationRecorderStatus    | ✅         |
| DescribeConfigurationRecorders ✨       | ✅         |
| DescribeDeliveryChannels ✨             | ✅         |
| DescribeOrganizationConformancePackStatuses | ✅         |
| DescribeOrganizationConformancePacks   | ✅         |
| GetOrganizationConformancePackDetailedStatus | ✅         |
| GetResourceConfigHistory               | ✅         |
| ListAggregateDiscoveredResources       | ✅         |
| ListDiscoveredResources                | ✅         |
| ListTagsForResource                    | ✅         |
| PutAggregationAuthorization            | ✅         |
| PutConfigRule                          | ✅         |
| PutConfigurationAggregator             | ✅         |
| PutConfigurationRecorder ✨             | ✅         |
| PutDeliveryChannel ✨                   | ✅         |
| PutEvaluations                         | ✅         |
| PutOrganizationConformancePack         | ✅         |
| StartConfigurationRecorder             | ✅         |
| StopConfigurationRecorder              | ✅         |
| TagResource                            | ✅         |
| UntagResource                          | ✅         |
| DeleteConformancePack                  | -         |
| DeleteEvaluationResults                | -         |
| DeleteOrganizationConfigRule           | -         |
| DeletePendingAggregationRequest        | -         |
| DeleteRemediationConfiguration         | -         |
| DeleteRemediationExceptions            | -         |
| DeleteResourceConfig                   | -         |
| DeleteRetentionConfiguration           | -         |
| DeleteStoredQuery                      | -         |
| DeliverConfigSnapshot                  | -         |
| DescribeAggregateComplianceByConfigRules | -         |
| DescribeAggregateComplianceByConformancePacks | -         |
| DescribeComplianceByConfigRule         | -         |
| DescribeComplianceByResource           | -         |
| DescribeConfigRuleEvaluationStatus     | -         |
| DescribeConfigurationAggregatorSourcesStatus | -         |
| DescribeConformancePackCompliance      | -         |
| DescribeConformancePackStatus          | -         |
| DescribeConformancePacks               | -         |
| DescribeDeliveryChannelStatus          | -         |
| DescribeOrganizationConfigRuleStatuses | -         |
| DescribeOrganizationConfigRules        | -         |
| DescribePendingAggregationRequests     | -         |
| DescribeRemediationConfigurations      | -         |
| DescribeRemediationExceptions          | -         |
| DescribeRemediationExecutionStatus     | -         |
| DescribeRetentionConfigurations        | -         |
| GetAggregateComplianceDetailsByConfigRule | -         |
| GetAggregateConfigRuleComplianceSummary | -         |
| GetAggregateConformancePackComplianceSummary | -         |
| GetAggregateDiscoveredResourceCounts   | -         |
| GetAggregateResourceConfig             | -         |
| GetComplianceDetailsByConfigRule       | -         |
| GetComplianceDetailsByResource         | -         |
| GetComplianceSummaryByConfigRule       | -         |
| GetComplianceSummaryByResourceType     | -         |
| GetConformancePackComplianceDetails    | -         |
| GetConformancePackComplianceSummary    | -         |
| GetCustomRulePolicy                    | -         |
| GetDiscoveredResourceCounts            | -         |
| GetOrganizationConfigRuleDetailedStatus | -         |
| GetOrganizationCustomRulePolicy        | -         |
| GetStoredQuery                         | -         |
| ListStoredQueries                      | -         |
| PutConformancePack                     | -         |
| PutExternalEvaluation                  | -         |
| PutOrganizationConfigRule              | -         |
| PutRemediationConfigurations           | -         |
| PutRemediationExceptions               | -         |
| PutResourceConfig                      | -         |
| PutRetentionConfiguration              | -         |
| PutStoredQuery                         | -         |
| SelectAggregateResourceConfig          | -         |
| SelectResourceConfig                   | -         |
| StartConfigRulesEvaluation             | -         |
| StartRemediationExecution              | -         |



## docdb ##


| Operation                              | Implemented |
| -------------------------------------- | ----------: |
| AddTagsToResource                      | ✅         |
| CopyDBClusterSnapshot                  | ✅         |
| CreateDBCluster                        | ✅         |
| CreateDBClusterParameterGroup          | ✅         |
| CreateDBClusterSnapshot                | ✅         |
| CreateDBInstance                       | ✅         |
| CreateDBSubnetGroup                    | ✅         |
| CreateEventSubscription                | ✅         |
| DeleteDBCluster                        | ✅         |
| DeleteDBClusterParameterGroup          | ✅         |
| DeleteDBClusterSnapshot                | ✅         |
| DeleteDBInstance                       | ✅         |
| DeleteDBSubnetGroup                    | ✅         |
| DeleteEventSubscription                | ✅         |
| DescribeCertificates                   | ✅         |
| DescribeDBClusterParameterGroups       | ✅         |
| DescribeDBClusterParameters            | ✅         |
| DescribeDBClusterSnapshots             | ✅         |
| DescribeDBClusters                     | ✅         |
| DescribeDBEngineVersions               | ✅         |
| DescribeDBInstances                    | ✅         |
| DescribeDBSubnetGroups                 | ✅         |
| DescribeEventSubscriptions             | ✅         |
| DescribeGlobalClusters                 | ✅         |
| ListTagsForResource                    | ✅         |
| ModifyDBCluster                        | ✅         |
| ModifyDBClusterParameterGroup          | ✅         |
| ModifyDBInstance                       | ✅         |
| ModifyDBSubnetGroup                    | ✅         |
| RebootDBInstance                       | ✅         |
| RemoveTagsFromResource                 | ✅         |
| ResetDBClusterParameterGroup           | ✅         |
| RestoreDBClusterFromSnapshot           | ✅         |
| StartDBCluster                         | ✅         |
| StopDBCluster                          | ✅         |
| AddSourceIdentifierToSubscription      | -         |
| ApplyPendingMaintenanceAction          | -         |
| CopyDBClusterParameterGroup            | -         |
| CreateGlobalCluster                    | -         |
| DeleteGlobalCluster                    | -         |
| DescribeDBClusterSnapshotAttributes    | -         |
| DescribeEngineDefaultClusterParameters | -         |
| DescribeEventCategories                | -         |
| DescribeEvents                         | -         |
| DescribeOrderableDBInstanceOptions     | -         |
| DescribePendingMaintenanceActions      | -         |
| FailoverDBCluster                      | -         |
| ModifyDBClusterSnapshotAttribute       | -         |
| ModifyEventSubscription                | -         |
| ModifyGlobalCluster                    | -         |
| RemoveFromGlobalCluster                | -         |
| RemoveSourceIdentifierFromSubscription | -         |
| RestoreDBClusterToPointInTime          | -         |



## dynamodb ##


| Operation                              | Implemented |
| -------------------------------------- | ----------: |
| BatchExecuteStatement ✨                | ✅         |
| BatchGetItem ✨                         | ✅         |
| BatchWriteItem ✨                       | ✅         |
| CreateBackup ✨                         | ✅         |
| CreateGlobalTable ✨                    | ✅         |
| CreateTable ✨                          | ✅         |
| DeleteBackup ✨                         | ✅         |
| DeleteItem ✨                           | ✅         |
| DeleteTable ✨                          | ✅         |
| DescribeGlobalTable ✨                  | ✅         |
| DescribeKinesisStreamingDestination ✨  | ✅         |
| DescribeLimits                         | ✅         |
| DescribeTable ✨                        | ✅         |
| DescribeTimeToLive ✨                   | ✅         |
| DisableKinesisStreamingDestination ✨   | ✅         |
| EnableKinesisStreamingDestination ✨    | ✅         |
| ExecuteStatement ✨                     | ✅         |
| ExecuteTransaction ✨                   | ✅         |
| GetItem ✨                              | ✅         |
| ListBackups                            | ✅         |
| ListGlobalTables                       | ✅         |
| ListTables ✨                           | ✅         |
| ListTagsOfResource ✨                   | ✅         |
| PutItem ✨                              | ✅         |
| Query ✨                                | ✅         |
| RestoreTableFromBackup ✨               | ✅         |
| Scan ✨                                 | ✅         |
| TagResource ✨                          | ✅         |
| TransactGetItems ✨                     | ✅         |
| TransactWriteItems ✨                   | ✅         |
| UntagResource ✨                        | ✅         |
| UpdateGlobalTable ✨                    | ✅         |
| UpdateItem ✨                           | ✅         |
| UpdateTable ✨                          | ✅         |
| UpdateTimeToLive ✨                     | ✅         |
| DescribeBackup                         | -         |
| DescribeContinuousBackups ✨            | -         |
| DescribeContributorInsights            | -         |
| DescribeEndpoints                      | -         |
| DescribeExport                         | -         |
| DescribeGlobalTableSettings            | -         |
| DescribeTableReplicaAutoScaling        | -         |
| ExportTableToPointInTime               | -         |
| ListContributorInsights                | -         |
| ListExports                            | -         |
| RestoreTableToPointInTime              | -         |
| UpdateContinuousBackups                | -         |
| UpdateContributorInsights              | -         |
| UpdateGlobalTableSettings              | -         |
| UpdateTableReplicaAutoScaling          | -         |



## dynamodbstreams ##


| Operation                              | Implemented |
| -------------------------------------- | ----------: |
| DescribeStream ✨                       | ✅         |
| GetRecords ✨                           | ✅         |
| GetShardIterator ✨                     | ✅         |
| ListStreams ✨                          | ✅         |



## ec2 ##


| Operation                              | Implemented |
| -------------------------------------- | ----------: |
| AcceptTransitGatewayPeeringAttachment  | ✅         |
| AcceptVpcPeeringConnection ✨           | ✅         |
| AllocateAddress ✨                      | ✅         |
| AssignIpv6Addresses                    | ✅         |
| AssignPrivateIpAddresses               | ✅         |
| AssociateAddress                       | ✅         |
| AssociateDhcpOptions                   | ✅         |
| AssociateIamInstanceProfile            | ✅         |
| AssociateRouteTable ✨                  | ✅         |
| AssociateSubnetCidrBlock               | ✅         |
| AssociateTransitGatewayRouteTable      | ✅         |
| AssociateVpcCidrBlock                  | ✅         |
| AttachInternetGateway ✨                | ✅         |
| AttachNetworkInterface                 | ✅         |
| AttachVolume                           | ✅         |
| AttachVpnGateway ✨                     | ✅         |
| AuthorizeSecurityGroupEgress ✨         | ✅         |
| AuthorizeSecurityGroupIngress ✨        | ✅         |
| CancelSpotFleetRequests                | ✅         |
| CancelSpotInstanceRequests             | ✅         |
| CopyImage                              | ✅         |
| CopySnapshot                           | ✅         |
| CreateCarrierGateway                   | ✅         |
| CreateCustomerGateway                  | ✅         |
| CreateDhcpOptions                      | ✅         |
| CreateEgressOnlyInternetGateway        | ✅         |
| CreateFlowLogs                         | ✅         |
| CreateImage ✨                          | ✅         |
| CreateInternetGateway ✨                | ✅         |
| CreateKeyPair ✨                        | ✅         |
| CreateLaunchTemplate                   | ✅         |
| CreateLaunchTemplateVersion            | ✅         |
| CreateManagedPrefixList                | ✅         |
| CreateNatGateway ✨                     | ✅         |
| CreateNetworkAcl                       | ✅         |
| CreateNetworkAclEntry                  | ✅         |
| CreateNetworkInterface                 | ✅         |
| CreatePlacementGroup                   | ✅         |
| CreateRoute ✨                          | ✅         |
| CreateRouteTable ✨                     | ✅         |
| CreateSecurityGroup ✨                  | ✅         |
| CreateSnapshot                         | ✅         |
| CreateSnapshots                        | ✅         |
| CreateSpotDatafeedSubscription         | ✅         |
| CreateSubnet ✨                         | ✅         |
| CreateTags ✨                           | ✅         |
| CreateTransitGateway                   | ✅         |
| CreateTransitGatewayPeeringAttachment  | ✅         |
| CreateTransitGatewayRoute              | ✅         |
| CreateTransitGatewayRouteTable         | ✅         |
| CreateTransitGatewayVpcAttachment      | ✅         |
| CreateVolume                           | ✅         |
| CreateVpc ✨                            | ✅         |
| CreateVpcEndpoint ✨                    | ✅         |
| CreateVpcEndpointServiceConfiguration  | ✅         |
| CreateVpcPeeringConnection ✨           | ✅         |
| CreateVpnConnection                    | ✅         |
| CreateVpnGateway ✨                     | ✅         |
| DeleteCarrierGateway                   | ✅         |
| DeleteCustomerGateway                  | ✅         |
| DeleteDhcpOptions                      | ✅         |
| DeleteEgressOnlyInternetGateway        | ✅         |
| DeleteFlowLogs                         | ✅         |
| DeleteInternetGateway                  | ✅         |
| DeleteKeyPair                          | ✅         |
| DeleteLaunchTemplate                   | ✅         |
| DeleteManagedPrefixList                | ✅         |
| DeleteNatGateway ✨                     | ✅         |
| DeleteNetworkAcl                       | ✅         |
| DeleteNetworkAclEntry                  | ✅         |
| DeleteNetworkInterface                 | ✅         |
| DeletePlacementGroup                   | ✅         |
| DeleteRoute ✨                          | ✅         |
| DeleteRouteTable ✨                     | ✅         |
| DeleteSecurityGroup ✨                  | ✅         |
| DeleteSnapshot                         | ✅         |
| DeleteSpotDatafeedSubscription         | ✅         |
| DeleteSubnet ✨                         | ✅         |
| DeleteTags                             | ✅         |
| DeleteTransitGateway                   | ✅         |
| DeleteTransitGatewayPeeringAttachment  | ✅         |
| DeleteTransitGatewayRoute              | ✅         |
| DeleteTransitGatewayRouteTable         | ✅         |
| DeleteTransitGatewayVpcAttachment      | ✅         |
| DeleteVolume                           | ✅         |
| DeleteVpc ✨                            | ✅         |
| DeleteVpcEndpointServiceConfigurations | ✅         |
| DeleteVpcEndpoints ✨                   | ✅         |
| DeleteVpcPeeringConnection ✨           | ✅         |
| DeleteVpnConnection                    | ✅         |
| DeleteVpnGateway ✨                     | ✅         |
| DeregisterImage                        | ✅         |
| DescribeAccountAttributes ✨            | ✅         |
| DescribeAddresses                      | ✅         |
| DescribeAvailabilityZones              | ✅         |
| DescribeCarrierGateways                | ✅         |
| DescribeCustomerGateways               | ✅         |
| DescribeDhcpOptions                    | ✅         |
| DescribeEgressOnlyInternetGateways     | ✅         |
| DescribeFlowLogs                       | ✅         |
| DescribeIamInstanceProfileAssociations | ✅         |
| DescribeImageAttribute                 | ✅         |
| DescribeImages ✨                       | ✅         |
| DescribeInstanceAttribute              | ✅         |
| DescribeInstanceCreditSpecifications   | ✅         |
| DescribeInstanceStatus                 | ✅         |
| DescribeInstanceTypeOfferings          | ✅         |
| DescribeInstanceTypes                  | ✅         |
| DescribeInstances ✨                    | ✅         |
| DescribeInternetGateways ✨             | ✅         |
| DescribeKeyPairs                       | ✅         |
| DescribeLaunchTemplateVersions         | ✅         |
| DescribeLaunchTemplates                | ✅         |
| DescribeManagedPrefixLists             | ✅         |
| DescribeNatGateways ✨                  | ✅         |
| DescribeNetworkAcls ✨                  | ✅         |
| DescribeNetworkInterfaceAttribute      | ✅         |
| DescribeNetworkInterfaces ✨            | ✅         |
| DescribePrefixLists                    | ✅         |
| DescribeRegions                        | ✅         |
| DescribeReservedInstances ✨            | ✅         |
| DescribeReservedInstancesOfferings ✨   | ✅         |
| DescribeRouteTables ✨                  | ✅         |
| DescribeSecurityGroups ✨               | ✅         |
| DescribeSnapshotAttribute              | ✅         |
| DescribeSnapshots                      | ✅         |
| DescribeSpotFleetInstances             | ✅         |
| DescribeSpotFleetRequests              | ✅         |
| DescribeSpotInstanceRequests           | ✅         |
| DescribeSpotPriceHistory               | ✅         |
| DescribeSubnets ✨                      | ✅         |
| DescribeTags                           | ✅         |
| DescribeTransitGatewayAttachments      | ✅         |
| DescribeTransitGatewayPeeringAttachments | ✅         |
| DescribeTransitGatewayRouteTables      | ✅         |
| DescribeTransitGatewayVpcAttachments   | ✅         |
| DescribeTransitGateways                | ✅         |
| DescribeVolumes                        | ✅         |
| DescribeVpcAttribute ✨                 | ✅         |
| DescribeVpcClassicLink ✨               | ✅         |
| DescribeVpcClassicLinkDnsSupport ✨     | ✅         |
| DescribeVpcEndpointServiceConfigurations | ✅         |
| DescribeVpcEndpointServicePermissions  | ✅         |
| DescribeVpcEndpointServices ✨          | ✅         |
| DescribeVpcEndpoints ✨                 | ✅         |
| DescribeVpcPeeringConnections ✨        | ✅         |
| DescribeVpcs ✨                         | ✅         |
| DescribeVpnConnections                 | ✅         |
| DescribeVpnGateways ✨                  | ✅         |
| DetachInternetGateway                  | ✅         |
| DetachNetworkInterface                 | ✅         |
| DetachVolume                           | ✅         |
| DetachVpnGateway ✨                     | ✅         |
| DisableEbsEncryptionByDefault          | ✅         |
| DisableTransitGatewayRouteTablePropagation | ✅         |
| DisableVpcClassicLink                  | ✅         |
| DisableVpcClassicLinkDnsSupport        | ✅         |
| DisassociateAddress                    | ✅         |
| DisassociateIamInstanceProfile         | ✅         |
| DisassociateRouteTable ✨               | ✅         |
| DisassociateSubnetCidrBlock            | ✅         |
| DisassociateTransitGatewayRouteTable   | ✅         |
| DisassociateVpcCidrBlock               | ✅         |
| EnableEbsEncryptionByDefault           | ✅         |
| EnableTransitGatewayRouteTablePropagation | ✅         |
| EnableVolumeIO                         | ✅         |
| EnableVpcClassicLink                   | ✅         |
| EnableVpcClassicLinkDnsSupport         | ✅         |
| GetConsoleOutput                       | ✅         |
| GetEbsEncryptionByDefault              | ✅         |
| GetManagedPrefixListEntries            | ✅         |
| GetTransitGatewayRouteTableAssociations | ✅         |
| GetTransitGatewayRouteTablePropagations | ✅         |
| ImportKeyPair ✨                        | ✅         |
| ImportVolume                           | ✅         |
| ModifyImageAttribute                   | ✅         |
| ModifyInstanceAttribute                | ✅         |
| ModifyManagedPrefixList                | ✅         |
| ModifyNetworkInterfaceAttribute        | ✅         |
| ModifySnapshotAttribute                | ✅         |
| ModifySpotFleetRequest                 | ✅         |
| ModifySubnetAttribute ✨                | ✅         |
| ModifyTransitGateway                   | ✅         |
| ModifyTransitGatewayVpcAttachment      | ✅         |
| ModifyVolumeAttribute                  | ✅         |
| ModifyVpcAttribute                     | ✅         |
| ModifyVpcEndpoint                      | ✅         |
| ModifyVpcEndpointServiceConfiguration  | ✅         |
| ModifyVpcEndpointServicePermissions    | ✅         |
| ModifyVpcPeeringConnectionOptions      | ✅         |
| ModifyVpcTenancy                       | ✅         |
| MonitorInstances                       | ✅         |
| PurchaseReservedInstancesOffering ✨    | ✅         |
| RebootInstances                        | ✅         |
| RegisterImage                          | ✅         |
| RejectTransitGatewayPeeringAttachment  | ✅         |
| RejectVpcPeeringConnection             | ✅         |
| ReleaseAddress ✨                       | ✅         |
| ReplaceIamInstanceProfileAssociation   | ✅         |
| ReplaceNetworkAclAssociation           | ✅         |
| ReplaceNetworkAclEntry                 | ✅         |
| ReplaceRoute                           | ✅         |
| ReplaceRouteTableAssociation           | ✅         |
| RequestSpotFleet                       | ✅         |
| RequestSpotInstances                   | ✅         |
| ResetImageAttribute                    | ✅         |
| ResetNetworkInterfaceAttribute         | ✅         |
| ResetSnapshotAttribute                 | ✅         |
| RevokeSecurityGroupEgress ✨            | ✅         |
| RevokeSecurityGroupIngress             | ✅         |
| RunInstances ✨                         | ✅         |
| SearchTransitGatewayRoutes             | ✅         |
| StartInstances ✨                       | ✅         |
| StopInstances ✨                        | ✅         |
| TerminateInstances ✨                   | ✅         |
| UnassignIpv6Addresses                  | ✅         |
| UnassignPrivateIpAddresses             | ✅         |
| UnmonitorInstances                     | ✅         |
| UpdateSecurityGroupRuleDescriptionsEgress | ✅         |
| UpdateSecurityGroupRuleDescriptionsIngress | ✅         |
| AcceptReservedInstancesExchangeQuote   | -         |
| AcceptTransitGatewayMulticastDomainAssociations | -         |
| AcceptTransitGatewayVpcAttachment      | -         |
| AcceptVpcEndpointConnections           | -         |
| AdvertiseByoipCidr                     | -         |
| AllocateHosts                          | -         |
| AllocateIpamPoolCidr                   | -         |
| ApplySecurityGroupsToClientVpnTargetNetwork | -         |
| AssociateClientVpnTargetNetwork        | -         |
| AssociateEnclaveCertificateIamRole     | -         |
| AssociateInstanceEventWindow           | -         |
| AssociateTransitGatewayMulticastDomain | -         |
| AssociateTrunkInterface                | -         |
| AttachClassicLinkVpc                   | -         |
| AuthorizeClientVpnIngress              | -         |
| BundleInstance                         | -         |
| CancelBundleTask                       | -         |
| CancelCapacityReservation              | -         |
| CancelCapacityReservationFleets        | -         |
| CancelConversionTask                   | -         |
| CancelExportTask                       | -         |
| CancelImportTask                       | -         |
| CancelReservedInstancesListing         | -         |
| ConfirmProductInstance                 | -         |
| CopyFpgaImage                          | -         |
| CreateCapacityReservation              | -         |
| CreateCapacityReservationFleet         | -         |
| CreateClientVpnEndpoint                | -         |
| CreateClientVpnRoute                   | -         |
| CreateDefaultSubnet                    | -         |
| CreateDefaultVpc                       | -         |
| CreateFleet                            | -         |
| CreateFpgaImage                        | -         |
| CreateInstanceEventWindow              | -         |
| CreateInstanceExportTask               | -         |
| CreateIpam                             | -         |
| CreateIpamPool                         | -         |
| CreateIpamScope                        | -         |
| CreateLocalGatewayRoute                | -         |
| CreateLocalGatewayRouteTableVpcAssociation | -         |
| CreateNetworkInsightsAccessScope       | -         |
| CreateNetworkInsightsPath              | -         |
| CreateNetworkInterfacePermission       | -         |
| CreatePublicIpv4Pool                   | -         |
| CreateReplaceRootVolumeTask            | -         |
| CreateReservedInstancesListing         | -         |
| CreateRestoreImageTask                 | -         |
| CreateStoreImageTask                   | -         |
| CreateSubnetCidrReservation            | -         |
| CreateTrafficMirrorFilter              | -         |
| CreateTrafficMirrorFilterRule          | -         |
| CreateTrafficMirrorSession             | -         |
| CreateTrafficMirrorTarget              | -         |
| CreateTransitGatewayConnect            | -         |
| CreateTransitGatewayConnectPeer        | -         |
| CreateTransitGatewayMulticastDomain    | -         |
| CreateTransitGatewayPrefixListReference | -         |
| CreateVpcEndpointConnectionNotification | -         |
| CreateVpnConnectionRoute               | -         |
| DeleteClientVpnEndpoint                | -         |
| DeleteClientVpnRoute                   | -         |
| DeleteFleets                           | -         |
| DeleteFpgaImage                        | -         |
| DeleteInstanceEventWindow              | -         |
| DeleteIpam                             | -         |
| DeleteIpamPool                         | -         |
| DeleteIpamScope                        | -         |
| DeleteLaunchTemplateVersions           | -         |
| DeleteLocalGatewayRoute                | -         |
| DeleteLocalGatewayRouteTableVpcAssociation | -         |
| DeleteNetworkInsightsAccessScope       | -         |
| DeleteNetworkInsightsAccessScopeAnalysis | -         |
| DeleteNetworkInsightsAnalysis          | -         |
| DeleteNetworkInsightsPath              | -         |
| DeleteNetworkInterfacePermission       | -         |
| DeletePublicIpv4Pool                   | -         |
| DeleteQueuedReservedInstances          | -         |
| DeleteSubnetCidrReservation            | -         |
| DeleteTrafficMirrorFilter              | -         |
| DeleteTrafficMirrorFilterRule          | -         |
| DeleteTrafficMirrorSession             | -         |
| DeleteTrafficMirrorTarget              | -         |
| DeleteTransitGatewayConnect            | -         |
| DeleteTransitGatewayConnectPeer        | -         |
| DeleteTransitGatewayMulticastDomain    | -         |
| DeleteTransitGatewayPrefixListReference | -         |
| DeleteVpcEndpointConnectionNotifications | -         |
| DeleteVpnConnectionRoute               | -         |
| DeprovisionByoipCidr                   | -         |
| DeprovisionIpamPoolCidr                | -         |
| DeprovisionPublicIpv4PoolCidr          | -         |
| DeregisterInstanceEventNotificationAttributes | -         |
| DeregisterTransitGatewayMulticastGroupMembers | -         |
| DeregisterTransitGatewayMulticastGroupSources | -         |
| DescribeAddressesAttribute             | -         |
| DescribeAggregateIdFormat              | -         |
| DescribeBundleTasks                    | -         |
| DescribeByoipCidrs                     | -         |
| DescribeCapacityReservationFleets      | -         |
| DescribeCapacityReservations           | -         |
| DescribeClassicLinkInstances           | -         |
| DescribeClientVpnAuthorizationRules    | -         |
| DescribeClientVpnConnections           | -         |
| DescribeClientVpnEndpoints             | -         |
| DescribeClientVpnRoutes                | -         |
| DescribeClientVpnTargetNetworks        | -         |
| DescribeCoipPools                      | -         |
| DescribeConversionTasks                | -         |
| DescribeElasticGpus                    | -         |
| DescribeExportImageTasks               | -         |
| DescribeExportTasks                    | -         |
| DescribeFastLaunchImages               | -         |
| DescribeFastSnapshotRestores           | -         |
| DescribeFleetHistory                   | -         |
| DescribeFleetInstances                 | -         |
| DescribeFleets                         | -         |
| DescribeFpgaImageAttribute             | -         |
| DescribeFpgaImages                     | -         |
| DescribeHostReservationOfferings       | -         |
| DescribeHostReservations               | -         |
| DescribeHosts                          | -         |
| DescribeIdFormat                       | -         |
| DescribeIdentityIdFormat               | -         |
| DescribeImportImageTasks               | -         |
| DescribeImportSnapshotTasks            | -         |
| DescribeInstanceEventNotificationAttributes | -         |
| DescribeInstanceEventWindows           | -         |
| DescribeIpamPools                      | -         |
| DescribeIpamScopes                     | -         |
| DescribeIpams                          | -         |
| DescribeIpv6Pools                      | -         |
| DescribeLocalGatewayRouteTableVirtualInterfaceGroupAssociations | -         |
| DescribeLocalGatewayRouteTableVpcAssociations | -         |
| DescribeLocalGatewayRouteTables        | -         |
| DescribeLocalGatewayVirtualInterfaceGroups | -         |
| DescribeLocalGatewayVirtualInterfaces  | -         |
| DescribeLocalGateways                  | -         |
| DescribeMovingAddresses                | -         |
| DescribeNetworkInsightsAccessScopeAnalyses | -         |
| DescribeNetworkInsightsAccessScopes    | -         |
| DescribeNetworkInsightsAnalyses        | -         |
| DescribeNetworkInsightsPaths           | -         |
| DescribeNetworkInterfacePermissions    | -         |
| DescribePlacementGroups                | -         |
| DescribePrincipalIdFormat              | -         |
| DescribePublicIpv4Pools                | -         |
| DescribeReplaceRootVolumeTasks         | -         |
| DescribeReservedInstancesListings      | -         |
| DescribeReservedInstancesModifications | -         |
| DescribeScheduledInstanceAvailability  | -         |
| DescribeScheduledInstances             | -         |
| DescribeSecurityGroupReferences        | -         |
| DescribeSecurityGroupRules             | -         |
| DescribeSnapshotTierStatus             | -         |
| DescribeSpotDatafeedSubscription       | -         |
| DescribeSpotFleetRequestHistory        | -         |
| DescribeStaleSecurityGroups            | -         |
| DescribeStoreImageTasks                | -         |
| DescribeTrafficMirrorFilters           | -         |
| DescribeTrafficMirrorSessions          | -         |
| DescribeTrafficMirrorTargets           | -         |
| DescribeTransitGatewayConnectPeers     | -         |
| DescribeTransitGatewayConnects         | -         |
| DescribeTransitGatewayMulticastDomains | -         |
| DescribeTrunkInterfaceAssociations     | -         |
| DescribeVolumeAttribute                | -         |
| DescribeVolumeStatus                   | -         |
| DescribeVolumesModifications           | -         |
| DescribeVpcEndpointConnectionNotifications | -         |
| DescribeVpcEndpointConnections         | -         |
| DetachClassicLinkVpc                   | -         |
| DisableFastLaunch                      | -         |
| DisableFastSnapshotRestores            | -         |
| DisableImageDeprecation                | -         |
| DisableIpamOrganizationAdminAccount    | -         |
| DisableSerialConsoleAccess             | -         |
| DisableVgwRoutePropagation             | -         |
| DisassociateClientVpnTargetNetwork     | -         |
| DisassociateEnclaveCertificateIamRole  | -         |
| DisassociateInstanceEventWindow        | -         |
| DisassociateTransitGatewayMulticastDomain | -         |
| DisassociateTrunkInterface             | -         |
| EnableFastLaunch                       | -         |
| EnableFastSnapshotRestores             | -         |
| EnableImageDeprecation                 | -         |
| EnableIpamOrganizationAdminAccount     | -         |
| EnableSerialConsoleAccess              | -         |
| EnableVgwRoutePropagation              | -         |
| ExportClientVpnClientCertificateRevocationList | -         |
| ExportClientVpnClientConfiguration     | -         |
| ExportImage                            | -         |
| ExportTransitGatewayRoutes             | -         |
| GetAssociatedEnclaveCertificateIamRoles | -         |
| GetAssociatedIpv6PoolCidrs             | -         |
| GetCapacityReservationUsage            | -         |
| GetCoipPoolUsage                       | -         |
| GetConsoleScreenshot                   | -         |
| GetDefaultCreditSpecification          | -         |
| GetEbsDefaultKmsKeyId                  | -         |
| GetFlowLogsIntegrationTemplate         | -         |
| GetGroupsForCapacityReservation        | -         |
| GetHostReservationPurchasePreview      | -         |
| GetInstanceTypesFromInstanceRequirements | -         |
| GetInstanceUefiData                    | -         |
| GetIpamAddressHistory                  | -         |
| GetIpamPoolAllocations                 | -         |
| GetIpamPoolCidrs                       | -         |
| GetIpamResourceCidrs                   | -         |
| GetLaunchTemplateData                  | -         |
| GetManagedPrefixListAssociations       | -         |
| GetNetworkInsightsAccessScopeAnalysisFindings | -         |
| GetNetworkInsightsAccessScopeContent   | -         |
| GetPasswordData                        | -         |
| GetReservedInstancesExchangeQuote      | -         |
| GetSerialConsoleAccessStatus           | -         |
| GetSpotPlacementScores                 | -         |
| GetSubnetCidrReservations              | -         |
| GetTransitGatewayAttachmentPropagations | -         |
| GetTransitGatewayMulticastDomainAssociations | -         |
| GetTransitGatewayPrefixListReferences  | -         |
| GetVpnConnectionDeviceSampleConfiguration | -         |
| GetVpnConnectionDeviceTypes            | -         |
| ImportClientVpnClientCertificateRevocationList | -         |
| ImportImage                            | -         |
| ImportInstance                         | -         |
| ImportSnapshot                         | -         |
| ListImagesInRecycleBin                 | -         |
| ListSnapshotsInRecycleBin              | -         |
| ModifyAddressAttribute                 | -         |
| ModifyAvailabilityZoneGroup            | -         |
| ModifyCapacityReservation              | -         |
| ModifyCapacityReservationFleet         | -         |
| ModifyClientVpnEndpoint                | -         |
| ModifyDefaultCreditSpecification       | -         |
| ModifyEbsDefaultKmsKeyId               | -         |
| ModifyFleet                            | -         |
| ModifyFpgaImageAttribute               | -         |
| ModifyHosts                            | -         |
| ModifyIdFormat                         | -         |
| ModifyIdentityIdFormat                 | -         |
| ModifyInstanceCapacityReservationAttributes | -         |
| ModifyInstanceCreditSpecification      | -         |
| ModifyInstanceEventStartTime           | -         |
| ModifyInstanceEventWindow              | -         |
| ModifyInstanceMaintenanceOptions       | -         |
| ModifyInstanceMetadataOptions          | -         |
| ModifyInstancePlacement                | -         |
| ModifyIpam                             | -         |
| ModifyIpamPool                         | -         |
| ModifyIpamResourceCidr                 | -         |
| ModifyIpamScope                        | -         |
| ModifyLaunchTemplate                   | -         |
| ModifyPrivateDnsNameOptions            | -         |
| ModifyReservedInstances                | -         |
| ModifySecurityGroupRules               | -         |
| ModifySnapshotTier                     | -         |
| ModifyTrafficMirrorFilterNetworkServices | -         |
| ModifyTrafficMirrorFilterRule          | -         |
| ModifyTrafficMirrorSession             | -         |
| ModifyTransitGatewayPrefixListReference | -         |
| ModifyVolume                           | -         |
| ModifyVpcEndpointConnectionNotification | -         |
| ModifyVpcEndpointServicePayerResponsibility | -         |
| ModifyVpnConnection                    | -         |
| ModifyVpnConnectionOptions             | -         |
| ModifyVpnTunnelCertificate             | -         |
| ModifyVpnTunnelOptions                 | -         |
| MoveAddressToVpc                       | -         |
| MoveByoipCidrToIpam                    | -         |
| ProvisionByoipCidr                     | -         |
| ProvisionIpamPoolCidr                  | -         |
| ProvisionPublicIpv4PoolCidr            | -         |
| PurchaseHostReservation                | -         |
| PurchaseScheduledInstances             | -         |
| RegisterInstanceEventNotificationAttributes | -         |
| RegisterTransitGatewayMulticastGroupMembers | -         |
| RegisterTransitGatewayMulticastGroupSources | -         |
| RejectTransitGatewayMulticastDomainAssociations | -         |
| RejectTransitGatewayVpcAttachment      | -         |
| RejectVpcEndpointConnections           | -         |
| ReleaseHosts                           | -         |
| ReleaseIpamPoolAllocation              | -         |
| ReplaceTransitGatewayRoute             | -         |
| ReportInstanceStatus                   | -         |
| ResetAddressAttribute                  | -         |
| ResetEbsDefaultKmsKeyId                | -         |
| ResetFpgaImageAttribute                | -         |
| ResetInstanceAttribute                 | -         |
| RestoreAddressToClassic                | -         |
| RestoreImageFromRecycleBin             | -         |
| RestoreManagedPrefixListVersion        | -         |
| RestoreSnapshotFromRecycleBin          | -         |
| RestoreSnapshotTier                    | -         |
| RevokeClientVpnIngress                 | -         |
| RunScheduledInstances                  | -         |
| SearchLocalGatewayRoutes               | -         |
| SearchTransitGatewayMulticastGroups    | -         |
| SendDiagnosticInterrupt                | -         |
| StartNetworkInsightsAccessScopeAnalysis | -         |
| StartNetworkInsightsAnalysis           | -         |
| StartVpcEndpointServicePrivateDnsVerification | -         |
| TerminateClientVpnConnections          | -         |
| WithdrawByoipCidr                      | -         |



## ecr ##


| Operation                              | Implemented |
| -------------------------------------- | ----------: |
| BatchDeleteImage ✨                     | ✅         |
| BatchGetImage ✨                        | ✅         |
| CreateRepository ✨                     | ✅         |
| DeleteLifecyclePolicy ✨                | ✅         |
| DeleteRegistryPolicy                   | ✅         |
| DeleteRepository ✨                     | ✅         |
| DeleteRepositoryPolicy                 | ✅         |
| DescribeImageScanFindings              | ✅         |
| DescribeImages ✨                       | ✅         |
| DescribeRegistry                       | ✅         |
| DescribeRepositories ✨                 | ✅         |
| GetAuthorizationToken ✨                | ✅         |
| GetLifecyclePolicy ✨                   | ✅         |
| GetLifecyclePolicyPreview              | ✅         |
| GetRegistryPolicy                      | ✅         |
| GetRepositoryPolicy                    | ✅         |
| ListImages ✨                           | ✅         |
| ListTagsForResource ✨                  | ✅         |
| PutImage                               | ✅         |
| PutImageScanningConfiguration          | ✅         |
| PutImageTagMutability ✨                | ✅         |
| PutLifecyclePolicy ✨                   | ✅         |
| PutRegistryPolicy                      | ✅         |
| PutReplicationConfiguration            | ✅         |
| SetRepositoryPolicy                    | ✅         |
| StartImageScan                         | ✅         |
| StartLifecyclePolicyPreview            | ✅         |
| TagResource ✨                          | ✅         |
| UntagResource ✨                        | ✅         |
| BatchCheckLayerAvailability            | -         |
| BatchGetRepositoryScanningConfiguration | -         |
| CompleteLayerUpload                    | -         |
| CreatePullThroughCacheRule             | -         |
| DeletePullThroughCacheRule             | -         |
| DescribeImageReplicationStatus         | -         |
| DescribePullThroughCacheRules          | -         |
| GetDownloadUrlForLayer                 | -         |
| GetRegistryScanningConfiguration       | -         |
| InitiateLayerUpload                    | -         |
| PutRegistryScanningConfiguration       | -         |
| UploadLayerPart                        | -         |



## ecs ##


| Operation                              | Implemented |
| -------------------------------------- | ----------: |
| CreateCapacityProvider                 | ✅         |
| CreateCluster ✨                        | ✅         |
| CreateService ✨                        | ✅         |
| CreateTaskSet ✨                        | ✅         |
| DeleteAccountSetting                   | ✅         |
| DeleteAttributes                       | ✅         |
| DeleteCapacityProvider                 | ✅         |
| DeleteCluster ✨                        | ✅         |
| DeleteService ✨                        | ✅         |
| DeleteTaskSet                          | ✅         |
| DeregisterContainerInstance            | ✅         |
| DeregisterTaskDefinition ✨             | ✅         |
| DescribeCapacityProviders              | ✅         |
| DescribeClusters ✨                     | ✅         |
| DescribeContainerInstances             | ✅         |
| DescribeServices ✨                     | ✅         |
| DescribeTaskDefinition ✨               | ✅         |
| DescribeTaskSets                       | ✅         |
| DescribeTasks ✨                        | ✅         |
| DiscoverPollEndpoint                   | ✅         |
| ListAccountSettings                    | ✅         |
| ListAttributes                         | ✅         |
| ListClusters ✨                         | ✅         |
| ListContainerInstances                 | ✅         |
| ListServices                           | ✅         |
| ListTagsForResource                    | ✅         |
| ListTaskDefinitionFamilies             | ✅         |
| ListTaskDefinitions ✨                  | ✅         |
| ListTasks ✨                            | ✅         |
| PutAccountSetting                      | ✅         |
| PutAttributes                          | ✅         |
| PutClusterCapacityProviders ✨          | ✅         |
| RegisterContainerInstance              | ✅         |
| RegisterTaskDefinition ✨               | ✅         |
| RunTask ✨                              | ✅         |
| StartTask                              | ✅         |
| StopTask ✨                             | ✅         |
| TagResource                            | ✅         |
| UntagResource                          | ✅         |
| UpdateCluster ✨                        | ✅         |
| UpdateContainerInstancesState          | ✅         |
| UpdateService                          | ✅         |
| UpdateServicePrimaryTaskSet            | ✅         |
| UpdateTaskSet                          | ✅         |
| ExecuteCommand                         | -         |
| PutAccountSettingDefault               | -         |
| SubmitAttachmentStateChanges           | -         |
| SubmitContainerStateChange             | -         |
| SubmitTaskStateChange                  | -         |
| UpdateCapacityProvider                 | -         |
| UpdateClusterSettings                  | -         |
| UpdateContainerAgent                   | -         |



## efs ##


| Operation                              | Implemented |
| -------------------------------------- | ----------: |
| CreateFileSystem ✨                     | ✅         |
| DeleteFileSystem ✨                     | ✅         |
| DescribeFileSystems ✨                  | ✅         |
| CreateAccessPoint                      | -         |
| CreateMountTarget                      | -         |
| CreateReplicationConfiguration         | -         |
| CreateTags                             | -         |
| DeleteAccessPoint                      | -         |
| DeleteFileSystemPolicy                 | -         |
| DeleteMountTarget                      | -         |
| DeleteReplicationConfiguration         | -         |
| DeleteTags                             | -         |
| DescribeAccessPoints                   | -         |
| DescribeAccountPreferences             | -         |
| DescribeBackupPolicy                   | -         |
| DescribeFileSystemPolicy               | -         |
| DescribeLifecycleConfiguration         | -         |
| DescribeMountTargetSecurityGroups      | -         |
| DescribeMountTargets                   | -         |
| DescribeReplicationConfigurations      | -         |
| DescribeTags                           | -         |
| ListTagsForResource                    | -         |
| ModifyMountTargetSecurityGroups        | -         |
| PutAccountPreferences                  | -         |
| PutBackupPolicy                        | -         |
| PutFileSystemPolicy                    | -         |
| PutLifecycleConfiguration              | -         |
| TagResource                            | -         |
| UntagResource                          | -         |
| UpdateFileSystem                       | -         |



## eks ##


| Operation                              | Implemented |
| -------------------------------------- | ----------: |
| CreateCluster ✨                        | ✅         |
| CreateFargateProfile                   | ✅         |
| CreateNodegroup                        | ✅         |
| DeleteCluster ✨                        | ✅         |
| DeleteFargateProfile                   | ✅         |
| DeleteNodegroup                        | ✅         |
| DescribeCluster ✨                      | ✅         |
| DescribeFargateProfile                 | ✅         |
| DescribeNodegroup                      | ✅         |
| ListClusters                           | ✅         |
| ListFargateProfiles                    | ✅         |
| ListNodegroups                         | ✅         |
| UpdateClusterConfig                    | ✅         |
| UpdateNodegroupConfig                  | ✅         |
| UpdateNodegroupVersion                 | ✅         |
| AssociateEncryptionConfig              | -         |
| AssociateIdentityProviderConfig        | -         |
| CreateAddon                            | -         |
| DeleteAddon                            | -         |
| DeregisterCluster                      | -         |
| DescribeAddon                          | -         |
| DescribeAddonVersions                  | -         |
| DescribeIdentityProviderConfig         | -         |
| DescribeUpdate                         | -         |
| DisassociateIdentityProviderConfig     | -         |
| ListAddons                             | -         |
| ListIdentityProviderConfigs            | -         |
| ListTagsForResource                    | -         |
| ListUpdates                            | -         |
| RegisterCluster                        | -         |
| TagResource                            | -         |
| UntagResource                          | -         |
| UpdateAddon                            | -         |
| UpdateClusterVersion                   | -         |



## elasticache ##


| Operation                              | Implemented |
| -------------------------------------- | ----------: |
| AddTagsToResource                      | ✅         |
| CreateCacheCluster ✨                   | ✅         |
| CreateCacheParameterGroup ✨            | ✅         |
| CreateCacheSecurityGroup ✨             | ✅         |
| CreateCacheSubnetGroup ✨               | ✅         |
| CreateReplicationGroup ✨               | ✅         |
| DeleteCacheCluster ✨                   | ✅         |
| DeleteCacheParameterGroup ✨            | ✅         |
| DeleteCacheSecurityGroup ✨             | ✅         |
| DeleteCacheSubnetGroup ✨               | ✅         |
| DeleteReplicationGroup ✨               | ✅         |
| DescribeCacheClusters ✨                | ✅         |
| DescribeCacheParameterGroups ✨         | ✅         |
| DescribeCacheParameters ✨              | ✅         |
| DescribeCacheSecurityGroups ✨          | ✅         |
| DescribeCacheSubnetGroups ✨            | ✅         |
| DescribeReplicationGroups ✨            | ✅         |
| ListTagsForResource                    | ✅         |
| ModifyCacheCluster ✨                   | ✅         |
| ModifyCacheParameterGroup ✨            | ✅         |
| ModifyCacheSubnetGroup ✨               | ✅         |
| ModifyReplicationGroup ✨               | ✅         |
| RemoveTagsFromResource                 | ✅         |
| AuthorizeCacheSecurityGroupIngress     | -         |
| BatchApplyUpdateAction                 | -         |
| BatchStopUpdateAction                  | -         |
| CompleteMigration                      | -         |
| CopySnapshot                           | -         |
| CreateGlobalReplicationGroup           | -         |
| CreateSnapshot                         | -         |
| CreateUser                             | -         |
| CreateUserGroup                        | -         |
| DecreaseNodeGroupsInGlobalReplicationGroup | -         |
| DecreaseReplicaCount                   | -         |
| DeleteGlobalReplicationGroup           | -         |
| DeleteSnapshot                         | -         |
| DeleteUser                             | -         |
| DeleteUserGroup                        | -         |
| DescribeCacheEngineVersions            | -         |
| DescribeEngineDefaultParameters        | -         |
| DescribeEvents                         | -         |
| DescribeGlobalReplicationGroups        | -         |
| DescribeReservedCacheNodes             | -         |
| DescribeReservedCacheNodesOfferings    | -         |
| DescribeServiceUpdates                 | -         |
| DescribeSnapshots                      | -         |
| DescribeUpdateActions                  | -         |
| DescribeUserGroups                     | -         |
| DescribeUsers                          | -         |
| DisassociateGlobalReplicationGroup     | -         |
| FailoverGlobalReplicationGroup         | -         |
| IncreaseNodeGroupsInGlobalReplicationGroup | -         |
| IncreaseReplicaCount                   | -         |
| ListAllowedNodeTypeModifications       | -         |
| ModifyGlobalReplicationGroup           | -         |
| ModifyReplicationGroupShardConfiguration | -         |
| ModifyUser                             | -         |
| ModifyUserGroup                        | -         |
| PurchaseReservedCacheNodesOffering     | -         |
| RebalanceSlotsInGlobalReplicationGroup | -         |
| RebootCacheCluster                     | -         |
| ResetCacheParameterGroup               | -         |
| RevokeCacheSecurityGroupIngress        | -         |
| StartMigration                         | -         |
| TestFailover                           | -         |



## elasticbeanstalk ##


| Operation                              | Implemented |
| -------------------------------------- | ----------: |
| CreateApplication ✨                    | ✅         |
| CreateApplicationVersion ✨             | ✅         |
| CreateEnvironment ✨                    | ✅         |
| DeleteApplication ✨                    | ✅         |
| DeleteApplicationVersion ✨             | ✅         |
| DeleteEnvironmentConfiguration ✨       | ✅         |
| DescribeApplicationVersions ✨          | ✅         |
| DescribeApplications ✨                 | ✅         |
| DescribeEnvironments ✨                 | ✅         |
| UpdateApplication ✨                    | ✅         |
| UpdateApplicationVersion ✨             | ✅         |
| UpdateEnvironment ✨                    | ✅         |
| AbortEnvironmentUpdate                 | -         |
| ApplyEnvironmentManagedAction          | -         |
| AssociateEnvironmentOperationsRole     | -         |
| CheckDNSAvailability                   | -         |
| ComposeEnvironments                    | -         |
| CreateConfigurationTemplate            | -         |
| CreatePlatformVersion                  | -         |
| CreateStorageLocation                  | -         |
| DeleteConfigurationTemplate            | -         |
| DeletePlatformVersion                  | -         |
| DescribeAccountAttributes              | -         |
| DescribeConfigurationOptions           | -         |
| DescribeConfigurationSettings          | -         |
| DescribeEnvironmentHealth              | -         |
| DescribeEnvironmentManagedActionHistory | -         |
| DescribeEnvironmentManagedActions      | -         |
| DescribeEnvironmentResources           | -         |
| DescribeEvents                         | -         |
| DescribeInstancesHealth                | -         |
| DescribePlatformVersion                | -         |
| DisassociateEnvironmentOperationsRole  | -         |
| ListAvailableSolutionStacks            | -         |
| ListPlatformBranches                   | -         |
| ListPlatformVersions                   | -         |
| ListTagsForResource                    | -         |
| RebuildEnvironment                     | -         |
| RequestEnvironmentInfo                 | -         |
| RestartAppServer                       | -         |
| RetrieveEnvironmentInfo                | -         |
| SwapEnvironmentCNAMEs                  | -         |
| TerminateEnvironment                   | -         |
| UpdateApplicationResourceLifecycle     | -         |
| UpdateConfigurationTemplate            | -         |
| UpdateTagsForResource                  | -         |
| ValidateConfigurationSettings          | -         |



## elb ##


| Operation                              | Implemented |
| -------------------------------------- | ----------: |
| AddTags                                | ✅         |
| ApplySecurityGroupsToLoadBalancer      | ✅         |
| AttachLoadBalancerToSubnets            | ✅         |
| ConfigureHealthCheck                   | ✅         |
| CreateAppCookieStickinessPolicy        | ✅         |
| CreateLBCookieStickinessPolicy         | ✅         |
| CreateLoadBalancer                     | ✅         |
| CreateLoadBalancerListeners            | ✅         |
| CreateLoadBalancerPolicy               | ✅         |
| DeleteLoadBalancer                     | ✅         |
| DeleteLoadBalancerListeners            | ✅         |
| DeleteLoadBalancerPolicy               | ✅         |
| DeregisterInstancesFromLoadBalancer    | ✅         |
| DescribeInstanceHealth                 | ✅         |
| DescribeLoadBalancerAttributes         | ✅         |
| DescribeLoadBalancerPolicies           | ✅         |
| DescribeLoadBalancers                  | ✅         |
| DescribeTags                           | ✅         |
| DetachLoadBalancerFromSubnets          | ✅         |
| DisableAvailabilityZonesForLoadBalancer | ✅         |
| EnableAvailabilityZonesForLoadBalancer | ✅         |
| ModifyLoadBalancerAttributes           | ✅         |
| RegisterInstancesWithLoadBalancer      | ✅         |
| RemoveTags                             | ✅         |
| SetLoadBalancerListenerSSLCertificate  | ✅         |
| SetLoadBalancerPoliciesForBackendServer | ✅         |
| SetLoadBalancerPoliciesOfListener      | ✅         |
| DescribeAccountLimits                  | -         |
| DescribeLoadBalancerPolicyTypes        | -         |



## elbv2 ##


| Operation                              | Implemented |
| -------------------------------------- | ----------: |
| AddListenerCertificates                | ✅         |
| AddTags                                | ✅         |
| CreateListener ✨                       | ✅         |
| CreateLoadBalancer ✨                   | ✅         |
| CreateRule ✨                           | ✅         |
| CreateTargetGroup ✨                    | ✅         |
| DeleteListener                         | ✅         |
| DeleteLoadBalancer                     | ✅         |
| DeleteRule                             | ✅         |
| DeleteTargetGroup                      | ✅         |
| DeregisterTargets                      | ✅         |
| DescribeAccountLimits                  | ✅         |
| DescribeListenerCertificates           | ✅         |
| DescribeListeners ✨                    | ✅         |
| DescribeLoadBalancerAttributes         | ✅         |
| DescribeLoadBalancers ✨                | ✅         |
| DescribeRules ✨                        | ✅         |
| DescribeSSLPolicies                    | ✅         |
| DescribeTags                           | ✅         |
| DescribeTargetGroupAttributes          | ✅         |
| DescribeTargetGroups ✨                 | ✅         |
| DescribeTargetHealth                   | ✅         |
| ModifyListener                         | ✅         |
| ModifyLoadBalancerAttributes ✨         | ✅         |
| ModifyRule                             | ✅         |
| ModifyTargetGroup                      | ✅         |
| ModifyTargetGroupAttributes            | ✅         |
| RegisterTargets ✨                      | ✅         |
| RemoveListenerCertificates             | ✅         |
| RemoveTags                             | ✅         |
| SetIpAddressType                       | ✅         |
| SetRulePriorities                      | ✅         |
| SetSecurityGroups                      | ✅         |
| SetSubnets                             | ✅         |



## emr ##


| Operation                              | Implemented |
| -------------------------------------- | ----------: |
| AddInstanceFleet ✨                     | ✅         |
| AddInstanceGroups                      | ✅         |
| AddJobFlowSteps                        | ✅         |
| AddTags                                | ✅         |
| CreateSecurityConfiguration            | ✅         |
| DeleteSecurityConfiguration            | ✅         |
| DescribeCluster ✨                      | ✅         |
| DescribeJobFlows                       | ✅         |
| DescribeSecurityConfiguration          | ✅         |
| DescribeStep                           | ✅         |
| GetAutoTerminationPolicy ✨             | ✅         |
| GetBlockPublicAccessConfiguration      | ✅         |
| ListBootstrapActions ✨                 | ✅         |
| ListClusters ✨                         | ✅         |
| ListInstanceFleets ✨                   | ✅         |
| ListInstanceGroups ✨                   | ✅         |
| ListInstances                          | ✅         |
| ListSteps ✨                            | ✅         |
| ModifyCluster                          | ✅         |
| ModifyInstanceFleet ✨                  | ✅         |
| ModifyInstanceGroups                   | ✅         |
| PutAutoScalingPolicy                   | ✅         |
| PutAutoTerminationPolicy ✨             | ✅         |
| RemoveAutoScalingPolicy                | ✅         |
| RemoveAutoTerminationPolicy ✨          | ✅         |
| RemoveTags                             | ✅         |
| RunJobFlow ✨                           | ✅         |
| SetTerminationProtection               | ✅         |
| SetVisibleToAllUsers                   | ✅         |
| TerminateJobFlows ✨                    | ✅         |
| CancelSteps                            | -         |
| CreateStudio                           | -         |
| CreateStudioSessionMapping             | -         |
| DeleteStudio                           | -         |
| DeleteStudioSessionMapping             | -         |
| DescribeNotebookExecution              | -         |
| DescribeReleaseLabel                   | -         |
| DescribeStudio                         | -         |
| GetManagedScalingPolicy                | -         |
| GetStudioSessionMapping                | -         |
| ListNotebookExecutions                 | -         |
| ListReleaseLabels                      | -         |
| ListSecurityConfigurations             | -         |
| ListStudioSessionMappings              | -         |
| ListStudios                            | -         |
| PutBlockPublicAccessConfiguration      | -         |
| PutManagedScalingPolicy                | -         |
| RemoveManagedScalingPolicy             | -         |
| StartNotebookExecution                 | -         |
| StopNotebookExecution                  | -         |
| UpdateStudio                           | -         |
| UpdateStudioSessionMapping             | -         |



## es ##


| Operation                              | Implemented |
| -------------------------------------- | ----------: |
| AddTags ✨                              | ✅         |
| CreateElasticsearchDomain ✨            | ✅         |
| DeleteElasticsearchDomain ✨            | ✅         |
| DescribeElasticsearchDomain ✨          | ✅         |
| DescribeElasticsearchDomainConfig ✨    | ✅         |
| DescribeElasticsearchDomains ✨         | ✅         |
| GetCompatibleElasticsearchVersions ✨   | ✅         |
| ListDomainNames ✨                      | ✅         |
| ListElasticsearchVersions ✨            | ✅         |
| ListTags ✨                             | ✅         |
| RemoveTags                             | ✅         |
| UpdateElasticsearchDomainConfig ✨      | ✅         |
| AcceptInboundCrossClusterSearchConnection | -         |
| AssociatePackage                       | -         |
| CancelElasticsearchServiceSoftwareUpdate | -         |
| CreateOutboundCrossClusterSearchConnection | -         |
| CreatePackage                          | -         |
| DeleteElasticsearchServiceRole         | -         |
| DeleteInboundCrossClusterSearchConnection | -         |
| DeleteOutboundCrossClusterSearchConnection | -         |
| DeletePackage                          | -         |
| DescribeDomainAutoTunes                | -         |
| DescribeDomainChangeProgress           | -         |
| DescribeElasticsearchInstanceTypeLimits | -         |
| DescribeInboundCrossClusterSearchConnections | -         |
| DescribeOutboundCrossClusterSearchConnections | -         |
| DescribePackages                       | -         |
| DescribeReservedElasticsearchInstanceOfferings | -         |
| DescribeReservedElasticsearchInstances | -         |
| DissociatePackage                      | -         |
| GetPackageVersionHistory               | -         |
| GetUpgradeHistory                      | -         |
| GetUpgradeStatus                       | -         |
| ListDomainsForPackage                  | -         |
| ListElasticsearchInstanceTypes         | -         |
| ListPackagesForDomain                  | -         |
| PurchaseReservedElasticsearchInstanceOffering | -         |
| RejectInboundCrossClusterSearchConnection | -         |
| StartElasticsearchServiceSoftwareUpdate | -         |
| UpdatePackage                          | -         |
| UpgradeElasticsearchDomain             | -         |



## events ##


| Operation                              | Implemented |
| -------------------------------------- | ----------: |
| CancelReplay                           | ✅         |
| CreateApiDestination ✨                 | ✅         |
| CreateArchive                          | ✅         |
| CreateConnection ✨                     | ✅         |
| CreateEventBus ✨                       | ✅         |
| DeleteApiDestination ✨                 | ✅         |
| DeleteArchive                          | ✅         |
| DeleteConnection ✨                     | ✅         |
| DeleteEventBus ✨                       | ✅         |
| DeleteRule ✨                           | ✅         |
| DescribeApiDestination ✨               | ✅         |
| DescribeArchive                        | ✅         |
| DescribeConnection ✨                   | ✅         |
| DescribeEventBus ✨                     | ✅         |
| DescribeReplay                         | ✅         |
| DescribeRule ✨                         | ✅         |
| DisableRule ✨                          | ✅         |
| EnableRule                             | ✅         |
| ListApiDestinations                    | ✅         |
| ListArchives                           | ✅         |
| ListConnections ✨                      | ✅         |
| ListEventBuses ✨                       | ✅         |
| ListReplays                            | ✅         |
| ListRuleNamesByTarget                  | ✅         |
| ListRules ✨                            | ✅         |
| ListTagsForResource ✨                  | ✅         |
| ListTargetsByRule ✨                    | ✅         |
| PutEvents ✨                            | ✅         |
| PutPermission ✨                        | ✅         |
| PutRule ✨                              | ✅         |
| PutTargets ✨                           | ✅         |
| RemovePermission ✨                     | ✅         |
| RemoveTargets ✨                        | ✅         |
| StartReplay                            | ✅         |
| TagResource ✨                          | ✅         |
| TestEventPattern                       | ✅         |
| UntagResource ✨                        | ✅         |
| UpdateApiDestination                   | ✅         |
| UpdateArchive                          | ✅         |
| UpdateConnection                       | ✅         |
| ActivateEventSource                    | -         |
| CreateEndpoint                         | -         |
| CreatePartnerEventSource               | -         |
| DeactivateEventSource                  | -         |
| DeauthorizeConnection                  | -         |
| DeleteEndpoint                         | -         |
| DeletePartnerEventSource               | -         |
| DescribeEndpoint                       | -         |
| DescribeEventSource                    | -         |
| DescribePartnerEventSource             | -         |
| ListEndpoints                          | -         |
| ListEventSources                       | -         |
| ListPartnerEventSourceAccounts         | -         |
| ListPartnerEventSources                | -         |
| PutPartnerEvents                       | -         |
| UpdateEndpoint                         | -         |



## firehose ##


| Operation                              | Implemented |
| -------------------------------------- | ----------: |
| CreateDeliveryStream ✨                 | ✅         |
| DeleteDeliveryStream ✨                 | ✅         |
| DescribeDeliveryStream ✨               | ✅         |
| ListDeliveryStreams ✨                  | ✅         |
| ListTagsForDeliveryStream ✨            | ✅         |
| PutRecord ✨                            | ✅         |
| PutRecordBatch                         | ✅         |
| TagDeliveryStream                      | ✅         |
| UntagDeliveryStream                    | ✅         |
| UpdateDestination ✨                    | ✅         |
| StartDeliveryStreamEncryption          | -         |
| StopDeliveryStreamEncryption           | -         |



## glacier ##


| Operation                              | Implemented |
| -------------------------------------- | ----------: |
| AbortMultipartUpload                   | ✅         |
| AbortVaultLock                         | ✅         |
| AddTagsToVault ✨                       | ✅         |
| CompleteMultipartUpload                | ✅         |
| CompleteVaultLock                      | ✅         |
| CreateVault ✨                          | ✅         |
| DeleteArchive                          | ✅         |
| DeleteVault ✨                          | ✅         |
| DeleteVaultAccessPolicy                | ✅         |
| DeleteVaultNotifications               | ✅         |
| DescribeJob                            | ✅         |
| DescribeVault ✨                        | ✅         |
| GetDataRetrievalPolicy                 | ✅         |
| GetJobOutput ✨                         | ✅         |
| GetVaultAccessPolicy ✨                 | ✅         |
| GetVaultLock                           | ✅         |
| GetVaultNotifications ✨                | ✅         |
| InitiateJob ✨                          | ✅         |
| InitiateMultipartUpload                | ✅         |
| InitiateVaultLock                      | ✅         |
| ListJobs                               | ✅         |
| ListMultipartUploads                   | ✅         |
| ListParts                              | ✅         |
| ListProvisionedCapacity                | ✅         |
| ListTagsForVault ✨                     | ✅         |
| ListVaults ✨                           | ✅         |
| PurchaseProvisionedCapacity            | ✅         |
| RemoveTagsFromVault                    | ✅         |
| SetDataRetrievalPolicy                 | ✅         |
| SetVaultAccessPolicy                   | ✅         |
| SetVaultNotifications                  | ✅         |
| UploadArchive ✨                        | ✅         |
| UploadMultipartPart                    | ✅         |



## glue ##


| Operation                              | Implemented |
| -------------------------------------- | ----------: |
| BatchCreatePartition                   | ✅         |
| BatchDeletePartition                   | ✅         |
| BatchDeleteTable                       | ✅         |
| BatchGetPartition                      | ✅         |
| BatchUpdatePartition                   | ✅         |
| CheckSchemaVersionValidity             | ✅         |
| CreateClassifier ✨                     | ✅         |
| CreateConnection ✨                     | ✅         |
| CreateCrawler ✨                        | ✅         |
| CreateDatabase ✨                       | ✅         |
| CreateJob ✨                            | ✅         |
| CreatePartition ✨                      | ✅         |
| CreatePartitionIndex ✨                 | ✅         |
| CreateRegistry ✨                       | ✅         |
| CreateSchema ✨                         | ✅         |
| CreateSecurityConfiguration ✨          | ✅         |
| CreateTable ✨                          | ✅         |
| CreateTrigger ✨                        | ✅         |
| CreateWorkflow ✨                       | ✅         |
| DeleteClassifier ✨                     | ✅         |
| DeleteConnection ✨                     | ✅         |
| DeleteCrawler ✨                        | ✅         |
| DeleteDatabase ✨                       | ✅         |
| DeleteJob ✨                            | ✅         |
| DeletePartition ✨                      | ✅         |
| DeletePartitionIndex ✨                 | ✅         |
| DeleteRegistry ✨                       | ✅         |
| DeleteResourcePolicy ✨                 | ✅         |
| DeleteSchema ✨                         | ✅         |
| DeleteSchemaVersions ✨                 | ✅         |
| DeleteSecurityConfiguration ✨          | ✅         |
| DeleteTable ✨                          | ✅         |
| DeleteTrigger ✨                        | ✅         |
| DeleteWorkflow ✨                       | ✅         |
| GetCatalogImportStatus                 | ✅         |
| GetClassifier ✨                        | ✅         |
| GetClassifiers ✨                       | ✅         |
| GetConnection ✨                        | ✅         |
| GetConnections ✨                       | ✅         |
| GetCrawler ✨                           | ✅         |
| GetCrawlers ✨                          | ✅         |
| GetDatabase ✨                          | ✅         |
| GetDatabases ✨                         | ✅         |
| GetJob ✨                               | ✅         |
| GetJobRun ✨                            | ✅         |
| GetJobRuns ✨                           | ✅         |
| GetJobs ✨                              | ✅         |
| GetPartition ✨                         | ✅         |
| GetPartitionIndexes ✨                  | ✅         |
| GetPartitions ✨                        | ✅         |
| GetRegistry ✨                          | ✅         |
| GetResourcePolicy ✨                    | ✅         |
| GetSchema ✨                            | ✅         |
| GetSchemaByDefinition                  | ✅         |
| GetSchemaVersion ✨                     | ✅         |
| GetSchemaVersionsDiff                  | ✅         |
| GetSecurityConfiguration ✨             | ✅         |
| GetSecurityConfigurations ✨            | ✅         |
| GetTable ✨                             | ✅         |
| GetTableVersion                        | ✅         |
| GetTableVersions                       | ✅         |
| GetTables ✨                            | ✅         |
| GetTags                                | ✅         |
| GetTrigger ✨                           | ✅         |
| GetWorkflow ✨                          | ✅         |
| ImportCatalogToGlue                    | ✅         |
| ListJobs ✨                             | ✅         |
| ListRegistries ✨                       | ✅         |
| ListSchemaVersions ✨                   | ✅         |
| ListSchemas ✨                          | ✅         |
| ListWorkflows ✨                        | ✅         |
| PutResourcePolicy ✨                    | ✅         |
| PutSchemaVersionMetadata ✨             | ✅         |
| QuerySchemaVersionMetadata ✨           | ✅         |
| RegisterSchemaVersion ✨                | ✅         |
| RemoveSchemaVersionMetadata ✨          | ✅         |
| StartCrawler ✨                         | ✅         |
| StartJobRun ✨                          | ✅         |
| StartTrigger                           | ✅         |
| StopCrawler                            | ✅         |
| StopTrigger                            | ✅         |
| TagResource                            | ✅         |
| UntagResource                          | ✅         |
| UpdateClassifier                       | ✅         |
| UpdateConnection                       | ✅         |
| UpdateCrawler ✨                        | ✅         |
| UpdateDatabase ✨                       | ✅         |
| UpdateJob ✨                            | ✅         |
| UpdatePartition ✨                      | ✅         |
| UpdateRegistry ✨                       | ✅         |
| UpdateSchema ✨                         | ✅         |
| UpdateTable ✨                          | ✅         |
| UpdateTrigger ✨                        | ✅         |
| UpdateWorkflow                         | ✅         |
| BatchDeleteConnection                  | -         |
| BatchDeleteTableVersion                | -         |
| BatchGetBlueprints                     | -         |
| BatchGetCrawlers                       | -         |
| BatchGetCustomEntityTypes              | -         |
| BatchGetDevEndpoints                   | -         |
| BatchGetJobs                           | -         |
| BatchGetTriggers                       | -         |
| BatchGetWorkflows                      | -         |
| BatchStopJobRun                        | -         |
| CancelMLTaskRun                        | -         |
| CancelStatement                        | -         |
| CreateBlueprint                        | -         |
| CreateCustomEntityType                 | -         |
| CreateDevEndpoint                      | -         |
| CreateMLTransform                      | -         |
| CreateScript                           | -         |
| CreateSession                          | -         |
| CreateUserDefinedFunction              | -         |
| DeleteBlueprint                        | -         |
| DeleteColumnStatisticsForPartition     | -         |
| DeleteColumnStatisticsForTable         | -         |
| DeleteCustomEntityType                 | -         |
| DeleteDevEndpoint                      | -         |
| DeleteMLTransform                      | -         |
| DeleteSession                          | -         |
| DeleteTableVersion                     | -         |
| DeleteUserDefinedFunction              | -         |
| GetBlueprint                           | -         |
| GetBlueprintRun                        | -         |
| GetBlueprintRuns                       | -         |
| GetColumnStatisticsForPartition        | -         |
| GetColumnStatisticsForTable            | -         |
| GetCrawlerMetrics                      | -         |
| GetCustomEntityType                    | -         |
| GetDataCatalogEncryptionSettings       | -         |
| GetDataflowGraph                       | -         |
| GetDevEndpoint                         | -         |
| GetDevEndpoints                        | -         |
| GetJobBookmark                         | -         |
| GetMLTaskRun                           | -         |
| GetMLTaskRuns                          | -         |
| GetMLTransform                         | -         |
| GetMLTransforms                        | -         |
| GetMapping                             | -         |
| GetPlan                                | -         |
| GetResourcePolicies                    | -         |
| GetSession                             | -         |
| GetStatement                           | -         |
| GetTriggers                            | -         |
| GetUnfilteredPartitionMetadata         | -         |
| GetUnfilteredPartitionsMetadata        | -         |
| GetUnfilteredTableMetadata             | -         |
| GetUserDefinedFunction                 | -         |
| GetUserDefinedFunctions                | -         |
| GetWorkflowRun                         | -         |
| GetWorkflowRunProperties               | -         |
| GetWorkflowRuns                        | -         |
| ListBlueprints                         | -         |
| ListCrawlers                           | -         |
| ListCrawls                             | -         |
| ListCustomEntityTypes                  | -         |
| ListDevEndpoints                       | -         |
| ListMLTransforms                       | -         |
| ListSessions                           | -         |
| ListStatements                         | -         |
| ListTriggers                           | -         |
| PutDataCatalogEncryptionSettings       | -         |
| PutWorkflowRunProperties               | -         |
| ResetJobBookmark                       | -         |
| ResumeWorkflowRun                      | -         |
| RunStatement                           | -         |
| SearchTables                           | -         |
| StartBlueprintRun                      | -         |
| StartCrawlerSchedule                   | -         |
| StartExportLabelsTaskRun               | -         |
| StartImportLabelsTaskRun               | -         |
| StartMLEvaluationTaskRun               | -         |
| StartMLLabelingSetGenerationTaskRun    | -         |
| StartWorkflowRun                       | -         |
| StopCrawlerSchedule                    | -         |
| StopSession                            | -         |
| StopWorkflowRun                        | -         |
| UpdateBlueprint                        | -         |
| UpdateColumnStatisticsForPartition     | -         |
| UpdateColumnStatisticsForTable         | -         |
| UpdateCrawlerSchedule                  | -         |
| UpdateDevEndpoint                      | -         |
| UpdateMLTransform                      | -         |
| UpdateUserDefinedFunction              | -         |



## iam ##


| Operation                              | Implemented |
| -------------------------------------- | ----------: |
| AddRoleToInstanceProfile ✨             | ✅         |
| AddUserToGroup                         | ✅         |
| AttachGroupPolicy ✨                    | ✅         |
| AttachRolePolicy ✨                     | ✅         |
| AttachUserPolicy ✨                     | ✅         |
| CreateAccessKey ✨                      | ✅         |
| CreateAccountAlias                     | ✅         |
| CreateGroup ✨                          | ✅         |
| CreateInstanceProfile ✨                | ✅         |
| CreateLoginProfile                     | ✅         |
| CreateOpenIDConnectProvider            | ✅         |
| CreatePolicy ✨                         | ✅         |
| CreatePolicyVersion                    | ✅         |
| CreateRole ✨                           | ✅         |
| CreateSAMLProvider                     | ✅         |
| CreateServiceLinkedRole ✨              | ✅         |
| CreateUser ✨                           | ✅         |
| CreateVirtualMFADevice                 | ✅         |
| DeactivateMFADevice                    | ✅         |
| DeleteAccessKey                        | ✅         |
| DeleteAccountAlias                     | ✅         |
| DeleteAccountPasswordPolicy            | ✅         |
| DeleteGroup ✨                          | ✅         |
| DeleteGroupPolicy ✨                    | ✅         |
| DeleteInstanceProfile ✨                | ✅         |
| DeleteLoginProfile                     | ✅         |
| DeleteOpenIDConnectProvider            | ✅         |
| DeletePolicy ✨                         | ✅         |
| DeletePolicyVersion                    | ✅         |
| DeleteRole ✨                           | ✅         |
| DeleteRolePermissionsBoundary          | ✅         |
| DeleteRolePolicy ✨                     | ✅         |
| DeleteSAMLProvider                     | ✅         |
| DeleteSSHPublicKey                     | ✅         |
| DeleteServerCertificate                | ✅         |
| DeleteServiceLinkedRole ✨              | ✅         |
| DeleteSigningCertificate               | ✅         |
| DeleteUser ✨                           | ✅         |
| DeleteUserPolicy ✨                     | ✅         |
| DeleteVirtualMFADevice                 | ✅         |
| DetachGroupPolicy ✨                    | ✅         |
| DetachRolePolicy ✨                     | ✅         |
| DetachUserPolicy ✨                     | ✅         |
| EnableMFADevice                        | ✅         |
| GenerateCredentialReport               | ✅         |
| GetAccessKeyLastUsed                   | ✅         |
| GetAccountAuthorizationDetails ✨       | ✅         |
| GetAccountPasswordPolicy               | ✅         |
| GetAccountSummary                      | ✅         |
| GetCredentialReport                    | ✅         |
| GetGroup ✨                             | ✅         |
| GetGroupPolicy ✨                       | ✅         |
| GetInstanceProfile ✨                   | ✅         |
| GetLoginProfile                        | ✅         |
| GetOpenIDConnectProvider               | ✅         |
| GetPolicy ✨                            | ✅         |
| GetPolicyVersion ✨                     | ✅         |
| GetRole ✨                              | ✅         |
| GetRolePolicy ✨                        | ✅         |
| GetSAMLProvider                        | ✅         |
| GetSSHPublicKey                        | ✅         |
| GetServerCertificate                   | ✅         |
| GetServiceLinkedRoleDeletionStatus     | ✅         |
| GetUser ✨                              | ✅         |
| GetUserPolicy ✨                        | ✅         |
| ListAccessKeys                         | ✅         |
| ListAccountAliases                     | ✅         |
| ListAttachedGroupPolicies ✨            | ✅         |
| ListAttachedRolePolicies ✨             | ✅         |
| ListAttachedUserPolicies ✨             | ✅         |
| ListEntitiesForPolicy                  | ✅         |
| ListGroupPolicies ✨                    | ✅         |
| ListGroups                             | ✅         |
| ListGroupsForUser                      | ✅         |
| ListInstanceProfileTags ✨              | ✅         |
| ListInstanceProfiles ✨                 | ✅         |
| ListInstanceProfilesForRole ✨          | ✅         |
| ListMFADevices                         | ✅         |
| ListOpenIDConnectProviderTags          | ✅         |
| ListOpenIDConnectProviders             | ✅         |
| ListPolicies ✨                         | ✅         |
| ListPolicyTags                         | ✅         |
| ListPolicyVersions ✨                   | ✅         |
| ListRolePolicies ✨                     | ✅         |
| ListRoleTags                           | ✅         |
| ListRoles ✨                            | ✅         |
| ListSAMLProviders                      | ✅         |
| ListSSHPublicKeys                      | ✅         |
| ListServerCertificates                 | ✅         |
| ListSigningCertificates                | ✅         |
| ListUserPolicies ✨                     | ✅         |
| ListUserTags                           | ✅         |
| ListUsers                              | ✅         |
| ListVirtualMFADevices                  | ✅         |
| PutGroupPolicy ✨                       | ✅         |
| PutRolePermissionsBoundary             | ✅         |
| PutRolePolicy ✨                        | ✅         |
| PutUserPolicy ✨                        | ✅         |
| RemoveRoleFromInstanceProfile ✨        | ✅         |
| RemoveUserFromGroup                    | ✅         |
| SetDefaultPolicyVersion                | ✅         |
| SimulatePrincipalPolicy ✨              | ✅         |
| TagInstanceProfile ✨                   | ✅         |
| TagOpenIDConnectProvider               | ✅         |
| TagPolicy                              | ✅         |
| TagRole                                | ✅         |
| TagUser                                | ✅         |
| UntagInstanceProfile ✨                 | ✅         |
| UntagOpenIDConnectProvider             | ✅         |
| UntagPolicy                            | ✅         |
| UntagRole                              | ✅         |
| UntagUser                              | ✅         |
| UpdateAccessKey                        | ✅         |
| UpdateAccountPasswordPolicy            | ✅         |
| UpdateAssumeRolePolicy                 | ✅         |
| UpdateGroup                            | ✅         |
| UpdateLoginProfile                     | ✅         |
| UpdateOpenIDConnectProviderThumbprint  | ✅         |
| UpdateRole ✨                           | ✅         |
| UpdateRoleDescription                  | ✅         |
| UpdateSAMLProvider                     | ✅         |
| UpdateSSHPublicKey                     | ✅         |
| UpdateSigningCertificate               | ✅         |
| UpdateUser                             | ✅         |
| UploadSSHPublicKey                     | ✅         |
| UploadServerCertificate                | ✅         |
| UploadSigningCertificate               | ✅         |
| AddClientIDToOpenIDConnectProvider     | -         |
| ChangePassword                         | -         |
| CreateServiceSpecificCredential        | -         |
| DeleteServiceSpecificCredential        | -         |
| DeleteUserPermissionsBoundary          | -         |
| GenerateOrganizationsAccessReport      | -         |
| GenerateServiceLastAccessedDetails     | -         |
| GetContextKeysForCustomPolicy          | -         |
| GetContextKeysForPrincipalPolicy       | -         |
| GetOrganizationsAccessReport           | -         |
| GetServiceLastAccessedDetails          | -         |
| GetServiceLastAccessedDetailsWithEntities | -         |
| ListMFADeviceTags                      | -         |
| ListPoliciesGrantingServiceAccess      | -         |
| ListSAMLProviderTags                   | -         |
| ListServerCertificateTags              | -         |
| ListServiceSpecificCredentials         | -         |
| PutUserPermissionsBoundary             | -         |
| RemoveClientIDFromOpenIDConnectProvider | -         |
| ResetServiceSpecificCredential         | -         |
| ResyncMFADevice                        | -         |
| SetSecurityTokenServicePreferences     | -         |
| SimulateCustomPolicy                   | -         |
| TagMFADevice                           | -         |
| TagSAMLProvider                        | -         |
| TagServerCertificate                   | -         |
| UntagMFADevice                         | -         |
| UntagSAMLProvider                      | -         |
| UntagServerCertificate                 | -         |
| UpdateServerCertificate                | -         |
| UpdateServiceSpecificCredential        | -         |



## iot ##


| Operation                              | Implemented |
| -------------------------------------- | ----------: |
| AddThingToThingGroup ✨                 | ✅         |
| AttachPolicy ✨                         | ✅         |
| AttachPrincipalPolicy                  | ✅         |
| AttachThingPrincipal ✨                 | ✅         |
| CancelJob                              | ✅         |
| CancelJobExecution                     | ✅         |
| CreateCertificateFromCsr               | ✅         |
| CreateDomainConfiguration              | ✅         |
| CreateDynamicThingGroup ✨              | ✅         |
| CreateJob ✨                            | ✅         |
| CreateKeysAndCertificate               | ✅         |
| CreatePolicy ✨                         | ✅         |
| CreatePolicyVersion                    | ✅         |
| CreateThing ✨                          | ✅         |
| CreateThingGroup ✨                     | ✅         |
| CreateThingType                        | ✅         |
| CreateTopicRule ✨                      | ✅         |
| CreateTopicRuleDestination ✨           | ✅         |
| DeleteCACertificate                    | ✅         |
| DeleteCertificate                      | ✅         |
| DeleteDomainConfiguration              | ✅         |
| DeleteDynamicThingGroup ✨              | ✅         |
| DeleteJob ✨                            | ✅         |
| DeleteJobExecution                     | ✅         |
| DeletePolicy ✨                         | ✅         |
| DeletePolicyVersion                    | ✅         |
| DeleteThing ✨                          | ✅         |
| DeleteThingGroup ✨                     | ✅         |
| DeleteThingType                        | ✅         |
| DeleteTopicRule ✨                      | ✅         |
| DeleteTopicRuleDestination             | ✅         |
| DeprecateThingType                     | ✅         |
| DescribeCACertificate                  | ✅         |
| DescribeCertificate                    | ✅         |
| DescribeDomainConfiguration            | ✅         |
| DescribeEndpoint ✨                     | ✅         |
| DescribeJob ✨                          | ✅         |
| DescribeJobExecution ✨                 | ✅         |
| DescribeThing ✨                        | ✅         |
| DescribeThingGroup ✨                   | ✅         |
| DescribeThingType                      | ✅         |
| DetachPolicy                           | ✅         |
| DetachPrincipalPolicy                  | ✅         |
| DetachThingPrincipal ✨                 | ✅         |
| DisableTopicRule                       | ✅         |
| EnableTopicRule                        | ✅         |
| GetJobDocument                         | ✅         |
| GetPolicy ✨                            | ✅         |
| GetPolicyVersion                       | ✅         |
| GetRegistrationCode                    | ✅         |
| GetTopicRule ✨                         | ✅         |
| GetTopicRuleDestination                | ✅         |
| ListAttachedPolicies                   | ✅         |
| ListAuditMitigationActionsTasks        | ✅         |
| ListAuditTasks                         | ✅         |
| ListCertificates                       | ✅         |
| ListCertificatesByCA                   | ✅         |
| ListDetectMitigationActionsExecutions  | ✅         |
| ListDetectMitigationActionsTasks       | ✅         |
| ListDomainConfigurations               | ✅         |
| ListJobExecutionsForJob                | ✅         |
| ListJobExecutionsForThing ✨            | ✅         |
| ListJobs ✨                             | ✅         |
| ListMetricValues                       | ✅         |
| ListPolicies ✨                         | ✅         |
| ListPolicyPrincipals                   | ✅         |
| ListPolicyVersions                     | ✅         |
| ListPrincipalPolicies                  | ✅         |
| ListPrincipalThings                    | ✅         |
| ListTagsForResource ✨                  | ✅         |
| ListThingGroups ✨                      | ✅         |
| ListThingGroupsForThing ✨              | ✅         |
| ListThingPrincipals ✨                  | ✅         |
| ListThingTypes                         | ✅         |
| ListThings ✨                           | ✅         |
| ListThingsInThingGroup ✨               | ✅         |
| ListTopicRules ✨                       | ✅         |
| ListViolationEvents                    | ✅         |
| RegisterCACertificate                  | ✅         |
| RegisterCertificate ✨                  | ✅         |
| RegisterCertificateWithoutCA           | ✅         |
| RemoveThingFromThingGroup ✨            | ✅         |
| ReplaceTopicRule                       | ✅         |
| SearchIndex ✨                          | ✅         |
| SetDefaultPolicyVersion                | ✅         |
| TagResource ✨                          | ✅         |
| UpdateCACertificate                    | ✅         |
| UpdateCertificate                      | ✅         |
| UpdateDomainConfiguration              | ✅         |
| UpdateDynamicThingGroup ✨              | ✅         |
| UpdateIndexingConfiguration ✨          | ✅         |
| UpdateThing                            | ✅         |
| UpdateThingGroup                       | ✅         |
| UpdateThingGroupsForThing              | ✅         |
| AcceptCertificateTransfer              | -         |
| AddThingToBillingGroup                 | -         |
| AssociateTargetsWithJob                | -         |
| AttachSecurityProfile                  | -         |
| CancelAuditMitigationActionsTask       | -         |
| CancelAuditTask                        | -         |
| CancelCertificateTransfer              | -         |
| CancelDetectMitigationActionsTask      | -         |
| ClearDefaultAuthorizer                 | -         |
| ConfirmTopicRuleDestination            | -         |
| CreateAuditSuppression                 | -         |
| CreateAuthorizer                       | -         |
| CreateBillingGroup                     | -         |
| CreateCustomMetric                     | -         |
| CreateDimension                        | -         |
| CreateFleetMetric                      | -         |
| CreateJobTemplate                      | -         |
| CreateMitigationAction                 | -         |
| CreateOTAUpdate                        | -         |
| CreateProvisioningClaim                | -         |
| CreateProvisioningTemplate             | -         |
| CreateProvisioningTemplateVersion      | -         |
| CreateRoleAlias                        | -         |
| CreateScheduledAudit                   | -         |
| CreateSecurityProfile                  | -         |
| CreateStream                           | -         |
| DeleteAccountAuditConfiguration        | -         |
| DeleteAuditSuppression                 | -         |
| DeleteAuthorizer                       | -         |
| DeleteBillingGroup                     | -         |
| DeleteCustomMetric                     | -         |
| DeleteDimension                        | -         |
| DeleteFleetMetric                      | -         |
| DeleteJobTemplate                      | -         |
| DeleteMitigationAction                 | -         |
| DeleteOTAUpdate                        | -         |
| DeleteProvisioningTemplate             | -         |
| DeleteProvisioningTemplateVersion      | -         |
| DeleteRegistrationCode                 | -         |
| DeleteRoleAlias                        | -         |
| DeleteScheduledAudit                   | -         |
| DeleteSecurityProfile                  | -         |
| DeleteStream                           | -         |
| DeleteV2LoggingLevel                   | -         |
| DescribeAccountAuditConfiguration      | -         |
| DescribeAuditFinding                   | -         |
| DescribeAuditMitigationActionsTask     | -         |
| DescribeAuditSuppression               | -         |
| DescribeAuditTask                      | -         |
| DescribeAuthorizer                     | -         |
| DescribeBillingGroup                   | -         |
| DescribeCustomMetric                   | -         |
| DescribeDefaultAuthorizer              | -         |
| DescribeDetectMitigationActionsTask    | -         |
| DescribeDimension                      | -         |
| DescribeEventConfigurations            | -         |
| DescribeFleetMetric                    | -         |
| DescribeIndex                          | -         |
| DescribeJobTemplate                    | -         |
| DescribeManagedJobTemplate             | -         |
| DescribeMitigationAction               | -         |
| DescribeProvisioningTemplate           | -         |
| DescribeProvisioningTemplateVersion    | -         |
| DescribeRoleAlias                      | -         |
| DescribeScheduledAudit                 | -         |
| DescribeSecurityProfile                | -         |
| DescribeStream                         | -         |
| DescribeThingRegistrationTask          | -         |
| DetachSecurityProfile                  | -         |
| GetBehaviorModelTrainingSummaries      | -         |
| GetBucketsAggregation                  | -         |
| GetCardinality                         | -         |
| GetEffectivePolicies                   | -         |
| GetIndexingConfiguration               | -         |
| GetLoggingOptions                      | -         |
| GetOTAUpdate                           | -         |
| GetPercentiles                         | -         |
| GetStatistics                          | -         |
| GetV2LoggingOptions                    | -         |
| ListActiveViolations                   | -         |
| ListAuditFindings                      | -         |
| ListAuditMitigationActionsExecutions   | -         |
| ListAuditSuppressions                  | -         |
| ListAuthorizers                        | -         |
| ListBillingGroups                      | -         |
| ListCACertificates                     | -         |
| ListCustomMetrics                      | -         |
| ListDimensions                         | -         |
| ListFleetMetrics                       | -         |
| ListIndices                            | -         |
| ListJobTemplates                       | -         |
| ListManagedJobTemplates                | -         |
| ListMitigationActions                  | -         |
| ListOTAUpdates                         | -         |
| ListOutgoingCertificates               | -         |
| ListProvisioningTemplateVersions       | -         |
| ListProvisioningTemplates              | -         |
| ListRoleAliases                        | -         |
| ListScheduledAudits                    | -         |
| ListSecurityProfiles                   | -         |
| ListSecurityProfilesForTarget          | -         |
| ListStreams                            | -         |
| ListTargetsForPolicy                   | -         |
| ListTargetsForSecurityProfile          | -         |
| ListThingRegistrationTaskReports       | -         |
| ListThingRegistrationTasks             | -         |
| ListThingsInBillingGroup               | -         |
| ListTopicRuleDestinations              | -         |
| ListV2LoggingLevels                    | -         |
| PutVerificationStateOnViolation        | -         |
| RegisterThing                          | -         |
| RejectCertificateTransfer              | -         |
| RemoveThingFromBillingGroup            | -         |
| SetDefaultAuthorizer                   | -         |
| SetLoggingOptions                      | -         |
| SetV2LoggingLevel                      | -         |
| SetV2LoggingOptions                    | -         |
| StartAuditMitigationActionsTask        | -         |
| StartDetectMitigationActionsTask       | -         |
| StartOnDemandAuditTask                 | -         |
| StartThingRegistrationTask             | -         |
| StopThingRegistrationTask              | -         |
| TestAuthorization                      | -         |
| TestInvokeAuthorizer                   | -         |
| TransferCertificate                    | -         |
| UntagResource                          | -         |
| UpdateAccountAuditConfiguration        | -         |
| UpdateAuditSuppression                 | -         |
| UpdateAuthorizer                       | -         |
| UpdateBillingGroup                     | -         |
| UpdateCustomMetric                     | -         |
| UpdateDimension                        | -         |
| UpdateEventConfigurations              | -         |
| UpdateFleetMetric                      | -         |
| UpdateJob                              | -         |
| UpdateMitigationAction                 | -         |
| UpdateProvisioningTemplate             | -         |
| UpdateRoleAlias                        | -         |
| UpdateScheduledAudit                   | -         |
| UpdateSecurityProfile                  | -         |
| UpdateStream                           | -         |
| UpdateTopicRuleDestination             | -         |
| ValidateSecurityProfileBehaviors       | -         |



## iot-data ##


| Operation                              | Implemented |
| -------------------------------------- | ----------: |
| DeleteThingShadow                      | ✅         |
| GetThingShadow ✨                       | ✅         |
| Publish ✨                              | ✅         |
| UpdateThingShadow ✨                    | ✅         |
| GetRetainedMessage                     | -         |
| ListNamedShadowsForThing               | -         |
| ListRetainedMessages                   | -         |



## iotanalytics ##


| Operation                              | Implemented |
| -------------------------------------- | ----------: |
| CreateChannel ✨                        | ✅         |
| CreateDataset ✨                        | ✅         |
| CreateDatastore ✨                      | ✅         |
| CreatePipeline ✨                       | ✅         |
| DeleteChannel ✨                        | ✅         |
| DeleteDataset ✨                        | ✅         |
| DeleteDatastore ✨                      | ✅         |
| DeletePipeline ✨                       | ✅         |
| DescribeChannel ✨                      | ✅         |
| DescribeDataset ✨                      | ✅         |
| DescribeDatastore ✨                    | ✅         |
| DescribePipeline ✨                     | ✅         |
| ListChannels ✨                         | ✅         |
| ListDatasetContents                    | ✅         |
| ListDatasets ✨                         | ✅         |
| ListDatastores ✨                       | ✅         |
| ListPipelines ✨                        | ✅         |
| SampleChannelData                      | ✅         |
| BatchPutMessage                        | -         |
| CancelPipelineReprocessing             | -         |
| CreateDatasetContent                   | -         |
| DeleteDatasetContent                   | -         |
| DescribeLoggingOptions                 | -         |
| GetDatasetContent                      | -         |
| ListTagsForResource                    | -         |
| PutLoggingOptions                      | -         |
| RunPipelineActivity                    | -         |
| StartPipelineReprocessing              | -         |
| TagResource                            | -         |
| UntagResource                          | -         |
| UpdateChannel                          | -         |
| UpdateDataset                          | -         |
| UpdateDatastore                        | -         |
| UpdatePipeline                         | -         |



## iotwireless ##


| Operation                              | Implemented |
| -------------------------------------- | ----------: |
| CreateDeviceProfile ✨                  | ✅         |
| CreateWirelessDevice ✨                 | ✅         |
| CreateWirelessGateway ✨                | ✅         |
| DeleteDeviceProfile ✨                  | ✅         |
| DeleteWirelessDevice ✨                 | ✅         |
| DeleteWirelessGateway ✨                | ✅         |
| GetDeviceProfile ✨                     | ✅         |
| GetWirelessDevice ✨                    | ✅         |
| GetWirelessGateway ✨                   | ✅         |
| ListDeviceProfiles ✨                   | ✅         |
| ListWirelessDevices ✨                  | ✅         |
| ListWirelessGateways ✨                 | ✅         |
| UpdateWirelessDevice                   | ✅         |
| UpdateWirelessGateway                  | ✅         |
| AssociateAwsAccountWithPartnerAccount  | -         |
| AssociateMulticastGroupWithFuotaTask   | -         |
| AssociateWirelessDeviceWithFuotaTask   | -         |
| AssociateWirelessDeviceWithMulticastGroup | -         |
| AssociateWirelessDeviceWithThing       | -         |
| AssociateWirelessGatewayWithCertificate | -         |
| AssociateWirelessGatewayWithThing      | -         |
| CancelMulticastGroupSession            | -         |
| CreateDestination                      | -         |
| CreateFuotaTask                        | -         |
| CreateMulticastGroup                   | -         |
| CreateNetworkAnalyzerConfiguration     | -         |
| CreateServiceProfile                   | -         |
| CreateWirelessGatewayTask              | -         |
| CreateWirelessGatewayTaskDefinition    | -         |
| DeleteDestination                      | -         |
| DeleteFuotaTask                        | -         |
| DeleteMulticastGroup                   | -         |
| DeleteNetworkAnalyzerConfiguration     | -         |
| DeleteQueuedMessages                   | -         |
| DeleteServiceProfile                   | -         |
| DeleteWirelessGatewayTask              | -         |
| DeleteWirelessGatewayTaskDefinition    | -         |
| DisassociateAwsAccountFromPartnerAccount | -         |
| DisassociateMulticastGroupFromFuotaTask | -         |
| DisassociateWirelessDeviceFromFuotaTask | -         |
| DisassociateWirelessDeviceFromMulticastGroup | -         |
| DisassociateWirelessDeviceFromThing    | -         |
| DisassociateWirelessGatewayFromCertificate | -         |
| DisassociateWirelessGatewayFromThing   | -         |
| GetDestination                         | -         |
| GetEventConfigurationByResourceTypes   | -         |
| GetFuotaTask                           | -         |
| GetLogLevelsByResourceTypes            | -         |
| GetMulticastGroup                      | -         |
| GetMulticastGroupSession               | -         |
| GetNetworkAnalyzerConfiguration        | -         |
| GetPartnerAccount                      | -         |
| GetResourceEventConfiguration          | -         |
| GetResourceLogLevel                    | -         |
| GetServiceEndpoint                     | -         |
| GetServiceProfile                      | -         |
| GetWirelessDeviceStatistics            | -         |
| GetWirelessGatewayCertificate          | -         |
| GetWirelessGatewayFirmwareInformation  | -         |
| GetWirelessGatewayStatistics           | -         |
| GetWirelessGatewayTask                 | -         |
| GetWirelessGatewayTaskDefinition       | -         |
| ListDestinations                       | -         |
| ListEventConfigurations                | -         |
| ListFuotaTasks                         | -         |
| ListMulticastGroups                    | -         |
| ListMulticastGroupsByFuotaTask         | -         |
| ListNetworkAnalyzerConfigurations      | -         |
| ListPartnerAccounts                    | -         |
| ListQueuedMessages                     | -         |
| ListServiceProfiles                    | -         |
| ListTagsForResource                    | -         |
| ListWirelessGatewayTaskDefinitions     | -         |
| PutResourceLogLevel                    | -         |
| ResetAllResourceLogLevels              | -         |
| ResetResourceLogLevel                  | -         |
| SendDataToMulticastGroup               | -         |
| SendDataToWirelessDevice               | -         |
| StartBulkAssociateWirelessDeviceWithMulticastGroup | -         |
| StartBulkDisassociateWirelessDeviceFromMulticastGroup | -         |
| StartFuotaTask                         | -         |
| StartMulticastGroupSession             | -         |
| TagResource                            | -         |
| TestWirelessDevice                     | -         |
| UntagResource                          | -         |
| UpdateDestination                      | -         |
| UpdateEventConfigurationByResourceTypes | -         |
| UpdateFuotaTask                        | -         |
| UpdateLogLevelsByResourceTypes         | -         |
| UpdateMulticastGroup                   | -         |
| UpdateNetworkAnalyzerConfiguration     | -         |
| UpdatePartnerAccount                   | -         |
| UpdateResourceEventConfiguration       | -         |



## kafka ##


| Operation                              | Implemented |
| -------------------------------------- | ----------: |
| CreateCluster ✨                        | ✅         |
| CreateConfiguration ✨                  | ✅         |
| DeleteCluster ✨                        | ✅         |
| DeleteConfiguration ✨                  | ✅         |
| DescribeCluster ✨                      | ✅         |
| DescribeClusterOperation               | ✅         |
| DescribeConfiguration ✨                | ✅         |
| DescribeConfigurationRevision ✨        | ✅         |
| GetBootstrapBrokers ✨                  | ✅         |
| ListClusters ✨                         | ✅         |
| ListConfigurationRevisions ✨           | ✅         |
| ListConfigurations ✨                   | ✅         |
| ListNodes ✨                            | ✅         |
| UpdateClusterConfiguration             | ✅         |
| UpdateClusterKafkaVersion              | ✅         |
| UpdateConfiguration ✨                  | ✅         |
| BatchAssociateScramSecret              | -         |
| BatchDisassociateScramSecret           | -         |
| CreateClusterV2                        | -         |
| DescribeClusterV2                      | -         |
| GetCompatibleKafkaVersions             | -         |
| ListClusterOperations                  | -         |
| ListClustersV2                         | -         |
| ListKafkaVersions                      | -         |
| ListScramSecrets                       | -         |
| ListTagsForResource                    | -         |
| RebootBroker                           | -         |
| TagResource                            | -         |
| UntagResource                          | -         |
| UpdateBrokerCount                      | -         |
| UpdateBrokerStorage                    | -         |
| UpdateBrokerType                       | -         |
| UpdateConnectivity                     | -         |
| UpdateMonitoring                       | -         |
| UpdateSecurity                         | -         |



## kinesis ##


| Operation                              | Implemented |
| -------------------------------------- | ----------: |
| AddTagsToStream                        | ✅         |
| CreateStream ✨                         | ✅         |
| DecreaseStreamRetentionPeriod          | ✅         |
| DeleteStream ✨                         | ✅         |
| DeregisterStreamConsumer ✨             | ✅         |
| DescribeLimits                         | ✅         |
| DescribeStream ✨                       | ✅         |
| DescribeStreamConsumer ✨               | ✅         |
| DescribeStreamSummary ✨                | ✅         |
| DisableEnhancedMonitoring              | ✅         |
| EnableEnhancedMonitoring               | ✅         |
| GetRecords ✨                           | ✅         |
| GetShardIterator ✨                     | ✅         |
| IncreaseStreamRetentionPeriod          | ✅         |
| ListShards ✨                           | ✅         |
| ListStreamConsumers ✨                  | ✅         |
| ListStreams ✨                          | ✅         |
| ListTagsForStream                      | ✅         |
| MergeShards                            | ✅         |
| PutRecord ✨                            | ✅         |
| PutRecords ✨                           | ✅         |
| RegisterStreamConsumer ✨               | ✅         |
| RemoveTagsFromStream                   | ✅         |
| SplitShard                             | ✅         |
| StartStreamEncryption                  | ✅         |
| StopStreamEncryption                   | ✅         |
| SubscribeToShard ✨                     | ✅         |
| UpdateShardCount                       | ✅         |
| UpdateStreamMode                       | ✅         |



## kinesisanalytics ##


| Operation                              | Implemented |
| -------------------------------------- | ----------: |
| AddApplicationInputProcessingConfiguration ✨| ✅         |
| AddApplicationOutput ✨                 | ✅         |
| CreateApplication ✨                    | ✅         |
| DeleteApplication ✨                    | ✅         |
| DeleteApplicationInputProcessingConfiguration ✨| ✅         |
| DescribeApplication ✨                  | ✅         |
| ListApplications ✨                     | ✅         |
| ListTagsForResource ✨                  | ✅         |
| TagResource ✨                          | ✅         |
| UntagResource ✨                        | ✅         |
| UpdateApplication ✨                    | ✅         |
| AddApplicationCloudWatchLoggingOption  | -         |
| AddApplicationInput                    | -         |
| AddApplicationReferenceDataSource      | -         |
| DeleteApplicationCloudWatchLoggingOption | -         |
| DeleteApplicationOutput                | -         |
| DeleteApplicationReferenceDataSource   | -         |
| DiscoverInputSchema                    | -         |
| StartApplication                       | -         |
| StopApplication                        | -         |



## kinesisanalyticsv2 ##


| Operation                              | Implemented |
| -------------------------------------- | ----------: |
| AddApplicationInputProcessingConfiguration ✨| ✅         |
| AddApplicationOutput ✨                 | ✅         |
| CreateApplication ✨                    | ✅         |
| DeleteApplication ✨                    | ✅         |
| DeleteApplicationInputProcessingConfiguration ✨| ✅         |
| DescribeApplication ✨                  | ✅         |
| ListApplications ✨                     | ✅         |
| ListTagsForResource ✨                  | ✅         |
| TagResource ✨                          | ✅         |
| UntagResource ✨                        | ✅         |
| UpdateApplication ✨                    | ✅         |
| AddApplicationCloudWatchLoggingOption  | -         |
| AddApplicationInput                    | -         |
| AddApplicationReferenceDataSource      | -         |
| AddApplicationVpcConfiguration         | -         |
| CreateApplicationPresignedUrl          | -         |
| CreateApplicationSnapshot              | -         |
| DeleteApplicationCloudWatchLoggingOption | -         |
| DeleteApplicationOutput                | -         |
| DeleteApplicationReferenceDataSource   | -         |
| DeleteApplicationSnapshot              | -         |
| DeleteApplicationVpcConfiguration      | -         |
| DescribeApplicationSnapshot            | -         |
| DescribeApplicationVersion             | -         |
| DiscoverInputSchema                    | -         |
| ListApplicationSnapshots               | -         |
| ListApplicationVersions                | -         |
| RollbackApplication                    | -         |
| StartApplication                       | -         |
| StopApplication                        | -         |
| UpdateApplicationMaintenanceConfiguration | -         |



## kms ##


| Operation                              | Implemented |
| -------------------------------------- | ----------: |
| CancelKeyDeletion                      | ✅         |
| CreateAlias ✨                          | ✅         |
| CreateGrant ✨                          | ✅         |
| CreateKey ✨                            | ✅         |
| Decrypt ✨                              | ✅         |
| DeleteAlias ✨                          | ✅         |
| DescribeKey ✨                          | ✅         |
| DisableKey ✨                           | ✅         |
| DisableKeyRotation ✨                   | ✅         |
| EnableKey ✨                            | ✅         |
| EnableKeyRotation                      | ✅         |
| Encrypt ✨                              | ✅         |
| GenerateDataKey ✨                      | ✅         |
| GenerateDataKeyPair ✨                  | ✅         |
| GenerateDataKeyPairWithoutPlaintext ✨  | ✅         |
| GenerateDataKeyWithoutPlaintext        | ✅         |
| GenerateRandom                         | ✅         |
| GetKeyPolicy ✨                         | ✅         |
| GetKeyRotationStatus ✨                 | ✅         |
| GetParametersForImport ✨               | ✅         |
| GetPublicKey ✨                         | ✅         |
| ImportKeyMaterial ✨                    | ✅         |
| ListAliases ✨                          | ✅         |
| ListGrants ✨                           | ✅         |
| ListKeyPolicies                        | ✅         |
| ListKeys ✨                             | ✅         |
| ListResourceTags ✨                     | ✅         |
| ListRetirableGrants                    | ✅         |
| PutKeyPolicy                           | ✅         |
| ReEncrypt                              | ✅         |
| RetireGrant ✨                          | ✅         |
| RevokeGrant ✨                          | ✅         |
| ScheduleKeyDeletion ✨                  | ✅         |
| Sign ✨                                 | ✅         |
| TagResource                            | ✅         |
| UntagResource                          | ✅         |
| UpdateAlias                            | ✅         |
| UpdateKeyDescription                   | ✅         |
| ConnectCustomKeyStore                  | -         |
| CreateCustomKeyStore                   | -         |
| DeleteCustomKeyStore                   | -         |
| DeleteImportedKeyMaterial              | -         |
| DescribeCustomKeyStores                | -         |
| DisconnectCustomKeyStore               | -         |
| GenerateMac                            | -         |
| ReplicateKey                           | -         |
| UpdateCustomKeyStore                   | -         |
| UpdatePrimaryRegion                    | -         |
| Verify                                 | -         |
| VerifyMac                              | -         |



## lakeformation ##


| Operation                              | Implemented |
| -------------------------------------- | ----------: |
| DeregisterResource                     | ✅         |
| DescribeResource                       | ✅         |
| GetDataLakeSettings                    | ✅         |
| GrantPermissions ✨                     | ✅         |
| ListPermissions ✨                      | ✅         |
| ListResources                          | ✅         |
| PutDataLakeSettings                    | ✅         |
| RegisterResource                       | ✅         |
| RevokePermissions                      | ✅         |
| AddLFTagsToResource                    | -         |
| BatchGrantPermissions                  | -         |
| BatchRevokePermissions                 | -         |
| CancelTransaction                      | -         |
| CommitTransaction                      | -         |
| CreateDataCellsFilter                  | -         |
| CreateLFTag                            | -         |
| DeleteDataCellsFilter                  | -         |
| DeleteLFTag                            | -         |
| DeleteObjectsOnCancel                  | -         |
| DescribeTransaction                    | -         |
| ExtendTransaction                      | -         |
| GetEffectivePermissionsForPath         | -         |
| GetLFTag                               | -         |
| GetQueryState                          | -         |
| GetQueryStatistics                     | -         |
| GetResourceLFTags                      | -         |
| GetTableObjects                        | -         |
| GetTemporaryGluePartitionCredentials   | -         |
| GetTemporaryGlueTableCredentials       | -         |
| GetWorkUnitResults                     | -         |
| GetWorkUnits                           | -         |
| ListDataCellsFilter                    | -         |
| ListLFTags                             | -         |
| ListTableStorageOptimizers             | -         |
| ListTransactions                       | -         |
| RemoveLFTagsFromResource               | -         |
| SearchDatabasesByLFTags                | -         |
| SearchTablesByLFTags                   | -         |
| StartQueryPlanning                     | -         |
| StartTransaction                       | -         |
| UpdateLFTag                            | -         |
| UpdateResource                         | -         |
| UpdateTableObjects                     | -         |
| UpdateTableStorageOptimizer            | -         |



## lambda ##


| Operation                              | Implemented |
| -------------------------------------- | ----------: |
| AddLayerVersionPermission              | ✅         |
| AddPermission ✨                        | ✅         |
| CreateAlias ✨                          | ✅         |
| CreateCodeSigningConfig ✨              | ✅         |
| CreateEventSourceMapping ✨             | ✅         |
| CreateFunction ✨                       | ✅         |
| DeleteAlias                            | ✅         |
| DeleteCodeSigningConfig ✨              | ✅         |
| DeleteEventSourceMapping ✨             | ✅         |
| DeleteFunction ✨                       | ✅         |
| DeleteFunctionCodeSigningConfig ✨      | ✅         |
| DeleteFunctionConcurrency ✨            | ✅         |
| DeleteFunctionEventInvokeConfig ✨      | ✅         |
| DeleteLayerVersion ✨                   | ✅         |
| GetAlias                               | ✅         |
| GetCodeSigningConfig ✨                 | ✅         |
| GetEventSourceMapping ✨                | ✅         |
| GetFunction ✨                          | ✅         |
| GetFunctionCodeSigningConfig ✨         | ✅         |
| GetFunctionConcurrency ✨               | ✅         |
| GetFunctionConfiguration ✨             | ✅         |
| GetFunctionEventInvokeConfig ✨         | ✅         |
| GetLayerVersion ✨                      | ✅         |
| GetLayerVersionByArn                   | ✅         |
| GetLayerVersionPolicy                  | ✅         |
| GetPolicy ✨                            | ✅         |
| Invoke ✨                               | ✅         |
| ListAliases ✨                          | ✅         |
| ListCodeSigningConfigs                 | ✅         |
| ListEventSourceMappings ✨              | ✅         |
| ListFunctions ✨                        | ✅         |
| ListLayerVersions ✨                    | ✅         |
| ListLayers ✨                           | ✅         |
| ListTags                               | ✅         |
| ListVersionsByFunction ✨               | ✅         |
| PublishLayerVersion ✨                  | ✅         |
| PublishVersion                         | ✅         |
| PutFunctionCodeSigningConfig ✨         | ✅         |
| PutFunctionConcurrency ✨               | ✅         |
| PutFunctionEventInvokeConfig ✨         | ✅         |
| RemovePermission ✨                     | ✅         |
| TagResource                            | ✅         |
| UntagResource                          | ✅         |
| UpdateAlias                            | ✅         |
| UpdateCodeSigningConfig ✨              | ✅         |
| UpdateEventSourceMapping ✨             | ✅         |
| UpdateFunctionCode ✨                   | ✅         |
| UpdateFunctionConfiguration ✨          | ✅         |
| UpdateFunctionEventInvokeConfig ✨      | ✅         |
| CreateFunctionUrlConfig                | -         |
| DeleteFunctionUrlConfig                | -         |
| DeleteProvisionedConcurrencyConfig     | -         |
| GetAccountSettings                     | -         |
| GetFunctionUrlConfig                   | -         |
| GetProvisionedConcurrencyConfig        | -         |
| InvokeAsync                            | -         |
| ListFunctionEventInvokeConfigs         | -         |
| ListFunctionUrlConfigs                 | -         |
| ListFunctionsByCodeSigningConfig       | -         |
| ListProvisionedConcurrencyConfigs      | -         |
| PutProvisionedConcurrencyConfig        | -         |
| RemoveLayerVersionPermission           | -         |
| UpdateFunctionUrlConfig                | -         |



## logs ##


| Operation                              | Implemented |
| -------------------------------------- | ----------: |
| CreateExportTask                       | ✅         |
| CreateLogGroup ✨                       | ✅         |
| CreateLogStream ✨                      | ✅         |
| DeleteLogGroup ✨                       | ✅         |
| DeleteLogStream ✨                      | ✅         |
| DeleteMetricFilter ✨                   | ✅         |
| DeleteResourcePolicy                   | ✅         |
| DeleteRetentionPolicy                  | ✅         |
| DeleteSubscriptionFilter ✨             | ✅         |
| DescribeLogGroups ✨                    | ✅         |
| DescribeLogStreams ✨                   | ✅         |
| DescribeMetricFilters ✨                | ✅         |
| DescribeResourcePolicies               | ✅         |
| DescribeSubscriptionFilters ✨          | ✅         |
| FilterLogEvents ✨                      | ✅         |
| GetLogEvents ✨                         | ✅         |
| ListTagsLogGroup ✨                     | ✅         |
| PutLogEvents ✨                         | ✅         |
| PutMetricFilter ✨                      | ✅         |
| PutResourcePolicy ✨                    | ✅         |
| PutRetentionPolicy                     | ✅         |
| PutSubscriptionFilter ✨                | ✅         |
| StartQuery                             | ✅         |
| TagLogGroup                            | ✅         |
| UntagLogGroup                          | ✅         |
| AssociateKmsKey                        | -         |
| CancelExportTask                       | -         |
| DeleteDestination                      | -         |
| DeleteQueryDefinition                  | -         |
| DescribeDestinations                   | -         |
| DescribeExportTasks                    | -         |
| DescribeQueries                        | -         |
| DescribeQueryDefinitions               | -         |
| DisassociateKmsKey                     | -         |
| GetLogGroupFields                      | -         |
| GetLogRecord                           | -         |
| GetQueryResults                        | -         |
| PutDestination                         | -         |
| PutDestinationPolicy                   | -         |
| PutQueryDefinition                     | -         |
| StopQuery                              | -         |
| TestMetricFilter                       | -         |



## mediastore ##


| Operation                              | Implemented |
| -------------------------------------- | ----------: |
| CreateContainer ✨                      | ✅         |
| DeleteContainer ✨                      | ✅         |
| DescribeContainer ✨                    | ✅         |
| ListContainers ✨                       | ✅         |
| DeleteContainerPolicy                  | -         |
| DeleteCorsPolicy                       | -         |
| DeleteLifecyclePolicy                  | -         |
| DeleteMetricPolicy                     | -         |
| GetContainerPolicy                     | -         |
| GetCorsPolicy                          | -         |
| GetLifecyclePolicy                     | -         |
| GetMetricPolicy                        | -         |
| ListTagsForResource                    | -         |
| PutContainerPolicy                     | -         |
| PutCorsPolicy                          | -         |
| PutLifecyclePolicy                     | -         |
| PutMetricPolicy                        | -         |
| StartAccessLogging                     | -         |
| StopAccessLogging                      | -         |
| TagResource                            | -         |
| UntagResource                          | -         |



## mediastore-data ##


| Operation                              | Implemented |
| -------------------------------------- | ----------: |
| DeleteObject ✨                         | ✅         |
| DescribeObject ✨                       | ✅         |
| GetObject ✨                            | ✅         |
| PutObject ✨                            | ✅         |
| ListItems                              | -         |



## mwaa ##


| Operation                              | Implemented |
| -------------------------------------- | ----------: |
| CreateEnvironment                      | ✅         |
| DeleteEnvironment                      | ✅         |
| GetEnvironment                         | ✅         |
| ListEnvironments ✨                     | ✅         |
| ListTagsForResource                    | ✅         |
| TagResource                            | ✅         |
| UntagResource                          | ✅         |
| UpdateEnvironment                      | ✅         |
| CreateCliToken                         | -         |
| CreateWebLoginToken                    | -         |
| PublishMetrics                         | -         |



## neptune ##


| Operation                              | Implemented |
| -------------------------------------- | ----------: |
| AddTagsToResource                      | ✅         |
| CopyDBClusterSnapshot                  | ✅         |
| CreateDBCluster                        | ✅         |
| CreateDBClusterEndpoint                | ✅         |
| CreateDBClusterParameterGroup          | ✅         |
| CreateDBClusterSnapshot                | ✅         |
| CreateDBInstance                       | ✅         |
| CreateDBParameterGroup                 | ✅         |
| CreateDBSubnetGroup                    | ✅         |
| CreateEventSubscription                | ✅         |
| DeleteDBCluster                        | ✅         |
| DeleteDBClusterEndpoint                | ✅         |
| DeleteDBClusterParameterGroup          | ✅         |
| DeleteDBClusterSnapshot                | ✅         |
| DeleteDBInstance                       | ✅         |
| DeleteDBParameterGroup                 | ✅         |
| DeleteDBSubnetGroup                    | ✅         |
| DeleteEventSubscription                | ✅         |
| DescribeDBClusterEndpoints             | ✅         |
| DescribeDBClusterParameterGroups       | ✅         |
| DescribeDBClusterParameters            | ✅         |
| DescribeDBClusterSnapshots             | ✅         |
| DescribeDBClusters                     | ✅         |
| DescribeDBEngineVersions               | ✅         |
| DescribeDBInstances                    | ✅         |
| DescribeDBParameterGroups              | ✅         |
| DescribeDBParameters                   | ✅         |
| DescribeDBSubnetGroups                 | ✅         |
| DescribeEventSubscriptions             | ✅         |
| DescribeGlobalClusters                 | ✅         |
| ListTagsForResource                    | ✅         |
| ModifyDBCluster                        | ✅         |
| ModifyDBClusterEndpoint                | ✅         |
| ModifyDBClusterParameterGroup          | ✅         |
| ModifyDBInstance                       | ✅         |
| ModifyDBParameterGroup                 | ✅         |
| ModifyDBSubnetGroup                    | ✅         |
| RebootDBInstance                       | ✅         |
| RemoveTagsFromResource                 | ✅         |
| ResetDBClusterParameterGroup           | ✅         |
| RestoreDBClusterFromSnapshot           | ✅         |
| StartDBCluster                         | ✅         |
| StopDBCluster                          | ✅         |
| AddRoleToDBCluster                     | -         |
| AddSourceIdentifierToSubscription      | -         |
| ApplyPendingMaintenanceAction          | -         |
| CopyDBClusterParameterGroup            | -         |
| CopyDBParameterGroup                   | -         |
| CreateGlobalCluster                    | -         |
| DeleteGlobalCluster                    | -         |
| DescribeDBClusterSnapshotAttributes    | -         |
| DescribeEngineDefaultClusterParameters | -         |
| DescribeEngineDefaultParameters        | -         |
| DescribeEventCategories                | -         |
| DescribeEvents                         | -         |
| DescribeOrderableDBInstanceOptions     | -         |
| DescribePendingMaintenanceActions      | -         |
| DescribeValidDBInstanceModifications   | -         |
| FailoverDBCluster                      | -         |
| FailoverGlobalCluster                  | -         |
| ModifyDBClusterSnapshotAttribute       | -         |
| ModifyEventSubscription                | -         |
| ModifyGlobalCluster                    | -         |
| PromoteReadReplicaDBCluster            | -         |
| RemoveFromGlobalCluster                | -         |
| RemoveRoleFromDBCluster                | -         |
| RemoveSourceIdentifierFromSubscription | -         |
| ResetDBParameterGroup                  | -         |
| RestoreDBClusterToPointInTime          | -         |



## opensearch ##


| Operation                              | Implemented |
| -------------------------------------- | ----------: |
| AddTags ✨                              | ✅         |
| CreateDomain ✨                         | ✅         |
| DeleteDomain ✨                         | ✅         |
| DescribeDomain ✨                       | ✅         |
| DescribeDomainConfig ✨                 | ✅         |
| DescribeDomains ✨                      | ✅         |
| GetCompatibleVersions ✨                | ✅         |
| ListDomainNames ✨                      | ✅         |
| ListTags ✨                             | ✅         |
| ListVersions ✨                         | ✅         |
| RemoveTags                             | ✅         |
| UpdateDomainConfig ✨                   | ✅         |
| AcceptInboundConnection                | -         |
| AssociatePackage                       | -         |
| CancelServiceSoftwareUpdate            | -         |
| CreateOutboundConnection               | -         |
| CreatePackage                          | -         |
| DeleteInboundConnection                | -         |
| DeleteOutboundConnection               | -         |
| DeletePackage                          | -         |
| DescribeDomainAutoTunes                | -         |
| DescribeDomainChangeProgress           | -         |
| DescribeInboundConnections             | -         |
| DescribeInstanceTypeLimits             | -         |
| DescribeOutboundConnections            | -         |
| DescribePackages                       | -         |
| DescribeReservedInstanceOfferings      | -         |
| DescribeReservedInstances              | -         |
| DissociatePackage                      | -         |
| GetPackageVersionHistory               | -         |
| GetUpgradeHistory                      | -         |
| GetUpgradeStatus                       | -         |
| ListDomainsForPackage                  | -         |
| ListInstanceTypeDetails                | -         |
| ListPackagesForDomain                  | -         |
| PurchaseReservedInstanceOffering       | -         |
| RejectInboundConnection                | -         |
| StartServiceSoftwareUpdate             | -         |
| UpdatePackage                          | -         |
| UpgradeDomain                          | -         |



## organizations ##


| Operation                              | Implemented |
| -------------------------------------- | ----------: |
| AttachPolicy                           | ✅         |
| CloseAccount                           | ✅         |
| CreateAccount ✨                        | ✅         |
| CreateOrganization ✨                   | ✅         |
| CreateOrganizationalUnit               | ✅         |
| CreatePolicy                           | ✅         |
| DeleteOrganization ✨                   | ✅         |
| DeletePolicy                           | ✅         |
| DeregisterDelegatedAdministrator       | ✅         |
| DescribeAccount ✨                      | ✅         |
| DescribeCreateAccountStatus            | ✅         |
| DescribeOrganization ✨                 | ✅         |
| DescribeOrganizationalUnit             | ✅         |
| DescribePolicy                         | ✅         |
| DetachPolicy                           | ✅         |
| DisableAWSServiceAccess                | ✅         |
| DisablePolicyType                      | ✅         |
| EnableAWSServiceAccess                 | ✅         |
| EnablePolicyType                       | ✅         |
| ListAWSServiceAccessForOrganization    | ✅         |
| ListAccounts                           | ✅         |
| ListAccountsForParent                  | ✅         |
| ListChildren                           | ✅         |
| ListCreateAccountStatus                | ✅         |
| ListDelegatedAdministrators            | ✅         |
| ListDelegatedServicesForAccount        | ✅         |
| ListOrganizationalUnitsForParent       | ✅         |
| ListParents                            | ✅         |
| ListPolicies                           | ✅         |
| ListPoliciesForTarget                  | ✅         |
| ListRoots                              | ✅         |
| ListTagsForResource                    | ✅         |
| ListTargetsForPolicy                   | ✅         |
| MoveAccount                            | ✅         |
| RegisterDelegatedAdministrator         | ✅         |
| RemoveAccountFromOrganization          | ✅         |
| TagResource                            | ✅         |
| UntagResource                          | ✅         |
| UpdateOrganizationalUnit               | ✅         |
| UpdatePolicy                           | ✅         |
| AcceptHandshake                        | -         |
| CancelHandshake                        | -         |
| CreateGovCloudAccount                  | -         |
| DeclineHandshake                       | -         |
| DeleteOrganizationalUnit               | -         |
| DescribeEffectivePolicy                | -         |
| DescribeHandshake                      | -         |
| EnableAllFeatures                      | -         |
| InviteAccountToOrganization            | -         |
| LeaveOrganization                      | -         |
| ListHandshakesForAccount               | -         |
| ListHandshakesForOrganization          | -         |



## qldb ##


| Operation                              | Implemented |
| -------------------------------------- | ----------: |
| CreateLedger ✨                         | ✅         |
| DeleteLedger ✨                         | ✅         |
| DescribeJournalKinesisStream           | ✅         |
| DescribeJournalS3Export                | ✅         |
| DescribeLedger ✨                       | ✅         |
| ExportJournalToS3                      | ✅         |
| ListLedgers ✨                          | ✅         |
| ListTagsForResource ✨                  | ✅         |
| StreamJournalToKinesis ✨               | ✅         |
| TagResource                            | ✅         |
| UntagResource                          | ✅         |
| UpdateLedger ✨                         | ✅         |
| CancelJournalKinesisStream             | -         |
| GetBlock                               | -         |
| GetDigest                              | -         |
| GetRevision                            | -         |
| ListJournalKinesisStreamsForLedger     | -         |
| ListJournalS3Exports                   | -         |
| ListJournalS3ExportsForLedger          | -         |
| UpdateLedgerPermissionsMode            | -         |



## qldb-session ##


| Operation                              | Implemented |
| -------------------------------------- | ----------: |
| SendCommand ✨                          | ✅         |



## rds ##


| Operation                              | Implemented |
| -------------------------------------- | ----------: |
| AddTagsToResource ✨                    | ✅         |
| AuthorizeDBSecurityGroupIngress        | ✅         |
| CancelExportTask                       | ✅         |
| CopyDBClusterSnapshot                  | ✅         |
| CopyDBSnapshot                         | ✅         |
| CreateDBCluster ✨                      | ✅         |
| CreateDBClusterEndpoint ✨              | ✅         |
| CreateDBClusterParameterGroup ✨        | ✅         |
| CreateDBClusterSnapshot ✨              | ✅         |
| CreateDBInstance ✨                     | ✅         |
| CreateDBInstanceReadReplica            | ✅         |
| CreateDBParameterGroup ✨               | ✅         |
| CreateDBProxy ✨                        | ✅         |
| CreateDBSecurityGroup                  | ✅         |
| CreateDBSnapshot ✨                     | ✅         |
| CreateDBSubnetGroup ✨                  | ✅         |
| CreateEventSubscription                | ✅         |
| CreateOptionGroup                      | ✅         |
| DeleteDBCluster ✨                      | ✅         |
| DeleteDBClusterEndpoint ✨              | ✅         |
| DeleteDBClusterParameterGroup ✨        | ✅         |
| DeleteDBClusterSnapshot ✨              | ✅         |
| DeleteDBInstance ✨                     | ✅         |
| DeleteDBParameterGroup ✨               | ✅         |
| DeleteDBProxy ✨                        | ✅         |
| DeleteDBSecurityGroup                  | ✅         |
| DeleteDBSnapshot                       | ✅         |
| DeleteDBSubnetGroup ✨                  | ✅         |
| DeleteEventSubscription                | ✅         |
| DeleteOptionGroup                      | ✅         |
| DeregisterDBProxyTargets ✨             | ✅         |
| DescribeCertificates                   | ✅         |
| DescribeDBClusterEndpoints ✨           | ✅         |
| DescribeDBClusterParameterGroups ✨     | ✅         |
| DescribeDBClusterParameters ✨          | ✅         |
| DescribeDBClusterSnapshots ✨           | ✅         |
| DescribeDBClusters ✨                   | ✅         |
| DescribeDBEngineVersions ✨             | ✅         |
| DescribeDBInstances ✨                  | ✅         |
| DescribeDBParameterGroups ✨            | ✅         |
| DescribeDBParameters ✨                 | ✅         |
| DescribeDBProxies ✨                    | ✅         |
| DescribeDBProxyTargets ✨               | ✅         |
| DescribeDBSecurityGroups               | ✅         |
| DescribeDBSnapshots ✨                  | ✅         |
| DescribeDBSubnetGroups ✨               | ✅         |
| DescribeEventSubscriptions             | ✅         |
| DescribeExportTasks                    | ✅         |
| DescribeGlobalClusters                 | ✅         |
| DescribeOptionGroupOptions             | ✅         |
| DescribeOptionGroups                   | ✅         |
| ListTagsForResource ✨                  | ✅         |
| ModifyCertificates                     | ✅         |
| ModifyCurrentDBClusterCapacity         | ✅         |
| ModifyDBCluster ✨                      | ✅         |
| ModifyDBClusterEndpoint ✨              | ✅         |
| ModifyDBClusterParameterGroup ✨        | ✅         |
| ModifyDBInstance ✨                     | ✅         |
| ModifyDBParameterGroup ✨               | ✅         |
| ModifyDBSubnetGroup                    | ✅         |
| ModifyOptionGroup                      | ✅         |
| RebootDBInstance                       | ✅         |
| RegisterDBProxyTargets ✨               | ✅         |
| RemoveTagsFromResource ✨               | ✅         |
| ResetDBClusterParameterGroup           | ✅         |
| RestoreDBClusterFromSnapshot ✨         | ✅         |
| RestoreDBInstanceFromDBSnapshot ✨      | ✅         |
| StartDBCluster                         | ✅         |
| StartDBInstance                        | ✅         |
| StartExportTask                        | ✅         |
| StopDBCluster                          | ✅         |
| StopDBInstance                         | ✅         |
| AddRoleToDBCluster                     | -         |
| AddRoleToDBInstance                    | -         |
| AddSourceIdentifierToSubscription      | -         |
| ApplyPendingMaintenanceAction          | -         |
| BacktrackDBCluster                     | -         |
| CopyDBClusterParameterGroup            | -         |
| CopyDBParameterGroup                   | -         |
| CopyOptionGroup                        | -         |
| CreateCustomDBEngineVersion            | -         |
| CreateDBProxyEndpoint                  | -         |
| CreateGlobalCluster                    | -         |
| DeleteCustomDBEngineVersion            | -         |
| DeleteDBInstanceAutomatedBackup        | -         |
| DeleteDBProxyEndpoint                  | -         |
| DeleteGlobalCluster                    | -         |
| DescribeAccountAttributes              | -         |
| DescribeDBClusterBacktracks            | -         |
| DescribeDBClusterSnapshotAttributes    | -         |
| DescribeDBInstanceAutomatedBackups     | -         |
| DescribeDBLogFiles                     | -         |
| DescribeDBProxyEndpoints               | -         |
| DescribeDBProxyTargetGroups            | -         |
| DescribeDBSnapshotAttributes           | -         |
| DescribeEngineDefaultClusterParameters | -         |
| DescribeEngineDefaultParameters        | -         |
| DescribeEventCategories                | -         |
| DescribeEvents                         | -         |
| DescribeOrderableDBInstanceOptions     | -         |
| DescribePendingMaintenanceActions      | -         |
| DescribeReservedDBInstances            | -         |
| DescribeReservedDBInstancesOfferings   | -         |
| DescribeSourceRegions                  | -         |
| DescribeValidDBInstanceModifications   | -         |
| DownloadDBLogFilePortion               | -         |
| FailoverDBCluster                      | -         |
| FailoverGlobalCluster                  | -         |
| ModifyCustomDBEngineVersion            | -         |
| ModifyDBClusterSnapshotAttribute       | -         |
| ModifyDBProxy                          | -         |
| ModifyDBProxyEndpoint                  | -         |
| ModifyDBProxyTargetGroup               | -         |
| ModifyDBSnapshot                       | -         |
| ModifyDBSnapshotAttribute              | -         |
| ModifyEventSubscription                | -         |
| ModifyGlobalCluster                    | -         |
| PromoteReadReplica                     | -         |
| PromoteReadReplicaDBCluster            | -         |
| PurchaseReservedDBInstancesOffering    | -         |
| RebootDBCluster                        | -         |
| RemoveFromGlobalCluster                | -         |
| RemoveRoleFromDBCluster                | -         |
| RemoveRoleFromDBInstance               | -         |
| RemoveSourceIdentifierFromSubscription | -         |
| ResetDBParameterGroup                  | -         |
| RestoreDBClusterFromS3                 | -         |
| RestoreDBClusterToPointInTime          | -         |
| RestoreDBInstanceFromS3                | -         |
| RestoreDBInstanceToPointInTime         | -         |
| RevokeDBSecurityGroupIngress           | -         |
| StartActivityStream                    | -         |
| StartDBInstanceAutomatedBackupsReplication | -         |
| StopActivityStream                     | -         |
| StopDBInstanceAutomatedBackupsReplication | -         |



## rds-data ##


| Operation                              | Implemented |
| -------------------------------------- | ----------: |
| BeginTransaction ✨                     | ✅         |
| CommitTransaction ✨                    | ✅         |
| ExecuteSql ✨                           | ✅         |
| ExecuteStatement ✨                     | ✅         |
| BatchExecuteStatement                  | -         |
| RollbackTransaction                    | -         |



## redshift ##


| Operation                              | Implemented |
| -------------------------------------- | ----------: |
| AuthorizeClusterSecurityGroupIngress   | ✅         |
| CreateCluster ✨                        | ✅         |
| CreateClusterParameterGroup ✨          | ✅         |
| CreateClusterSecurityGroup             | ✅         |
| CreateClusterSnapshot                  | ✅         |
| CreateClusterSubnetGroup               | ✅         |
| CreateSnapshotCopyGrant                | ✅         |
| CreateTags                             | ✅         |
| DeleteCluster ✨                        | ✅         |
| DeleteClusterParameterGroup            | ✅         |
| DeleteClusterSecurityGroup             | ✅         |
| DeleteClusterSnapshot                  | ✅         |
| DeleteClusterSubnetGroup               | ✅         |
| DeleteSnapshotCopyGrant                | ✅         |
| DeleteTags                             | ✅         |
| DescribeClusterParameterGroups ✨       | ✅         |
| DescribeClusterParameters ✨            | ✅         |
| DescribeClusterSecurityGroups          | ✅         |
| DescribeClusterSnapshots               | ✅         |
| DescribeClusterSubnetGroups            | ✅         |
| DescribeClusters ✨                     | ✅         |
| DescribeDefaultClusterParameters ✨     | ✅         |
| DescribeSnapshotCopyGrants             | ✅         |
| DescribeTags                           | ✅         |
| DisableSnapshotCopy                    | ✅         |
| EnableSnapshotCopy                     | ✅         |
| GetClusterCredentials                  | ✅         |
| ModifyCluster                          | ✅         |
| ModifySnapshotCopyRetentionPeriod      | ✅         |
| PauseCluster                           | ✅         |
| RestoreFromClusterSnapshot             | ✅         |
| ResumeCluster                          | ✅         |
| AcceptReservedNodeExchange             | -         |
| AddPartner                             | -         |
| AssociateDataShareConsumer             | -         |
| AuthorizeDataShare                     | -         |
| AuthorizeEndpointAccess                | -         |
| AuthorizeSnapshotAccess                | -         |
| BatchDeleteClusterSnapshots            | -         |
| BatchModifyClusterSnapshots            | -         |
| CancelResize                           | -         |
| CopyClusterSnapshot                    | -         |
| CreateAuthenticationProfile            | -         |
| CreateEndpointAccess                   | -         |
| CreateEventSubscription                | -         |
| CreateHsmClientCertificate             | -         |
| CreateHsmConfiguration                 | -         |
| CreateScheduledAction                  | -         |
| CreateSnapshotSchedule                 | -         |
| CreateUsageLimit                       | -         |
| DeauthorizeDataShare                   | -         |
| DeleteAuthenticationProfile            | -         |
| DeleteEndpointAccess                   | -         |
| DeleteEventSubscription                | -         |
| DeleteHsmClientCertificate             | -         |
| DeleteHsmConfiguration                 | -         |
| DeletePartner                          | -         |
| DeleteScheduledAction                  | -         |
| DeleteSnapshotSchedule                 | -         |
| DeleteUsageLimit                       | -         |
| DescribeAccountAttributes              | -         |
| DescribeAuthenticationProfiles         | -         |
| DescribeClusterDbRevisions             | -         |
| DescribeClusterTracks                  | -         |
| DescribeClusterVersions                | -         |
| DescribeDataShares                     | -         |
| DescribeDataSharesForConsumer          | -         |
| DescribeDataSharesForProducer          | -         |
| DescribeEndpointAccess                 | -         |
| DescribeEndpointAuthorization          | -         |
| DescribeEventCategories                | -         |
| DescribeEventSubscriptions             | -         |
| DescribeEvents                         | -         |
| DescribeHsmClientCertificates          | -         |
| DescribeHsmConfigurations              | -         |
| DescribeLoggingStatus                  | -         |
| DescribeNodeConfigurationOptions       | -         |
| DescribeOrderableClusterOptions        | -         |
| DescribePartners                       | -         |
| DescribeReservedNodeExchangeStatus     | -         |
| DescribeReservedNodeOfferings          | -         |
| DescribeReservedNodes                  | -         |
| DescribeResize                         | -         |
| DescribeScheduledActions               | -         |
| DescribeSnapshotSchedules              | -         |
| DescribeStorage                        | -         |
| DescribeTableRestoreStatus             | -         |
| DescribeUsageLimits                    | -         |
| DisableLogging                         | -         |
| DisassociateDataShareConsumer          | -         |
| EnableLogging                          | -         |
| GetClusterCredentialsWithIAM           | -         |
| GetReservedNodeExchangeConfigurationOptions | -         |
| GetReservedNodeExchangeOfferings       | -         |
| ModifyAquaConfiguration                | -         |
| ModifyAuthenticationProfile            | -         |
| ModifyClusterDbRevision                | -         |
| ModifyClusterIamRoles                  | -         |
| ModifyClusterMaintenance               | -         |
| ModifyClusterParameterGroup            | -         |
| ModifyClusterSnapshot                  | -         |
| ModifyClusterSnapshotSchedule          | -         |
| ModifyClusterSubnetGroup               | -         |
| ModifyEndpointAccess                   | -         |
| ModifyEventSubscription                | -         |
| ModifyScheduledAction                  | -         |
| ModifySnapshotSchedule                 | -         |
| ModifyUsageLimit                       | -         |
| PurchaseReservedNodeOffering           | -         |
| RebootCluster                          | -         |
| RejectDataShare                        | -         |
| ResetClusterParameterGroup             | -         |
| ResizeCluster                          | -         |
| RestoreTableFromClusterSnapshot        | -         |
| RevokeClusterSecurityGroupIngress      | -         |
| RevokeEndpointAccess                   | -         |
| RevokeSnapshotAccess                   | -         |
| RotateEncryptionKey                    | -         |
| UpdatePartnerStatus                    | -         |



## redshift-data ##


| Operation                              | Implemented |
| -------------------------------------- | ----------: |
| DescribeStatement ✨                    | ✅         |
| DescribeTable ✨                        | ✅         |
| ExecuteStatement ✨                     | ✅         |
| GetStatementResult ✨                   | ✅         |
| ListDatabases ✨                        | ✅         |
| BatchExecuteStatement                  | -         |
| CancelStatement                        | -         |
| ListSchemas                            | -         |
| ListStatements                         | -         |
| ListTables                             | -         |



## resource-groups ##


| Operation                              | Implemented |
| -------------------------------------- | ----------: |
| CreateGroup ✨                          | ✅         |
| DeleteGroup ✨                          | ✅         |
| GetGroup ✨                             | ✅         |
| GetGroupConfiguration                  | ✅         |
| GetGroupQuery                          | ✅         |
| GetTags                                | ✅         |
| GroupResources                         | ✅         |
| ListGroupResources                     | ✅         |
| ListGroups ✨                           | ✅         |
| PutGroupConfiguration                  | ✅         |
| SearchResources                        | ✅         |
| UngroupResources                       | ✅         |
| UpdateGroup                            | ✅         |
| UpdateGroupQuery                       | ✅         |
| Tag                                    | -         |
| Untag                                  | -         |



## resourcegroupstaggingapi ##


| Operation                              | Implemented |
| -------------------------------------- | ----------: |
| GetResources ✨                         | ✅         |
| GetTagKeys                             | ✅         |
| GetTagValues                           | ✅         |
| DescribeReportCreation                 | -         |
| GetComplianceSummary                   | -         |
| StartReportCreation                    | -         |
| TagResources                           | -         |
| UntagResources                         | -         |



## route53 ##


| Operation                              | Implemented |
| -------------------------------------- | ----------: |
| ActivateKeySigningKey                  | ✅         |
| AssociateVPCWithHostedZone ✨           | ✅         |
| ChangeCidrCollection                   | ✅         |
| ChangeResourceRecordSets ✨             | ✅         |
| ChangeTagsForResource ✨                | ✅         |
| CreateCidrCollection                   | ✅         |
| CreateHealthCheck ✨                    | ✅         |
| CreateHostedZone ✨                     | ✅         |
| CreateKeySigningKey                    | ✅         |
| CreateQueryLoggingConfig               | ✅         |
| CreateReusableDelegationSet ✨          | ✅         |
| CreateTrafficPolicy                    | ✅         |
| CreateTrafficPolicyInstance            | ✅         |
| CreateTrafficPolicyVersion             | ✅         |
| CreateVPCAssociationAuthorization      | ✅         |
| DeactivateKeySigningKey                | ✅         |
| DeleteCidrCollection                   | ✅         |
| DeleteHealthCheck ✨                    | ✅         |
| DeleteHostedZone ✨                     | ✅         |
| DeleteKeySigningKey                    | ✅         |
| DeleteQueryLoggingConfig               | ✅         |
| DeleteReusableDelegationSet ✨          | ✅         |
| DeleteTrafficPolicy                    | ✅         |
| DeleteTrafficPolicyInstance            | ✅         |
| DeleteVPCAssociationAuthorization      | ✅         |
| DisableHostedZoneDNSSEC                | ✅         |
| DisassociateVPCFromHostedZone ✨        | ✅         |
| EnableHostedZoneDNSSEC                 | ✅         |
| GetAccountLimit                        | ✅         |
| GetChange ✨                            | ✅         |
| GetCheckerIpRanges                     | ✅         |
| GetDNSSEC                              | ✅         |
| GetGeoLocation                         | ✅         |
| GetHealthCheck ✨                       | ✅         |
| GetHealthCheckCount                    | ✅         |
| GetHealthCheckLastFailureReason        | ✅         |
| GetHealthCheckStatus                   | ✅         |
| GetHostedZone ✨                        | ✅         |
| GetHostedZoneCount                     | ✅         |
| GetHostedZoneLimit                     | ✅         |
| GetQueryLoggingConfig                  | ✅         |
| GetReusableDelegationSet ✨             | ✅         |
| GetReusableDelegationSetLimit          | ✅         |
| GetTrafficPolicy                       | ✅         |
| GetTrafficPolicyInstance               | ✅         |
| GetTrafficPolicyInstanceCount          | ✅         |
| ListCidrBlocks                         | ✅         |
| ListCidrCollections                    | ✅         |
| ListCidrLocations                      | ✅         |
| ListGeoLocations                       | ✅         |
| ListHealthChecks                       | ✅         |
| ListHostedZones ✨                      | ✅         |
| ListHostedZonesByName ✨                | ✅         |
| ListHostedZonesByVPC ✨                 | ✅         |
| ListQueryLoggingConfigs                | ✅         |
| ListResourceRecordSets ✨               | ✅         |
| ListReusableDelegationSets ✨           | ✅         |
| ListTagsForResource ✨                  | ✅         |
| ListTagsForResources                   | ✅         |
| ListTrafficPolicies                    | ✅         |
| ListTrafficPolicyInstances             | ✅         |
| ListTrafficPolicyInstancesByHostedZone | ✅         |
| ListTrafficPolicyInstancesByPolicy     | ✅         |
| ListTrafficPolicyVersions              | ✅         |
| ListVPCAssociationAuthorizations       | ✅         |
| TestDNSAnswer                          | ✅         |
| UpdateHealthCheck                      | ✅         |
| UpdateHostedZoneComment                | ✅         |
| UpdateTrafficPolicyComment             | ✅         |
| UpdateTrafficPolicyInstance            | ✅         |



## route53resolver ##


| Operation                              | Implemented |
| -------------------------------------- | ----------: |
| AssociateResolverRule                  | ✅         |
| CreateResolverEndpoint ✨               | ✅         |
| CreateResolverRule                     | ✅         |
| DeleteResolverEndpoint                 | ✅         |
| DeleteResolverRule                     | ✅         |
| DisassociateResolverRule               | ✅         |
| GetResolverEndpoint                    | ✅         |
| GetResolverRule                        | ✅         |
| GetResolverRuleAssociation             | ✅         |
| ListResolverEndpointIpAddresses        | ✅         |
| ListResolverEndpoints                  | ✅         |
| ListResolverRuleAssociations           | ✅         |
| ListResolverRules                      | ✅         |
| ListTagsForResource                    | ✅         |
| TagResource                            | ✅         |
| UntagResource                          | ✅         |
| UpdateResolverEndpoint                 | ✅         |
| AssociateFirewallRuleGroup             | -         |
| AssociateResolverEndpointIpAddress     | -         |
| AssociateResolverQueryLogConfig        | -         |
| CreateFirewallDomainList               | -         |
| CreateFirewallRule                     | -         |
| CreateFirewallRuleGroup                | -         |
| CreateResolverQueryLogConfig           | -         |
| DeleteFirewallDomainList               | -         |
| DeleteFirewallRule                     | -         |
| DeleteFirewallRuleGroup                | -         |
| DeleteResolverQueryLogConfig           | -         |
| DisassociateFirewallRuleGroup          | -         |
| DisassociateResolverEndpointIpAddress  | -         |
| DisassociateResolverQueryLogConfig     | -         |
| GetFirewallConfig                      | -         |
| GetFirewallDomainList                  | -         |
| GetFirewallRuleGroup                   | -         |
| GetFirewallRuleGroupAssociation        | -         |
| GetFirewallRuleGroupPolicy             | -         |
| GetResolverConfig                      | -         |
| GetResolverDnssecConfig                | -         |
| GetResolverQueryLogConfig              | -         |
| GetResolverQueryLogConfigAssociation   | -         |
| GetResolverQueryLogConfigPolicy        | -         |
| GetResolverRulePolicy                  | -         |
| ImportFirewallDomains                  | -         |
| ListFirewallConfigs                    | -         |
| ListFirewallDomainLists                | -         |
| ListFirewallDomains                    | -         |
| ListFirewallRuleGroupAssociations      | -         |
| ListFirewallRuleGroups                 | -         |
| ListFirewallRules                      | -         |
| ListResolverConfigs                    | -         |
| ListResolverDnssecConfigs              | -         |
| ListResolverQueryLogConfigAssociations | -         |
| ListResolverQueryLogConfigs            | -         |
| PutFirewallRuleGroupPolicy             | -         |
| PutResolverQueryLogConfigPolicy        | -         |
| PutResolverRulePolicy                  | -         |
| UpdateFirewallConfig                   | -         |
| UpdateFirewallDomains                  | -         |
| UpdateFirewallRule                     | -         |
| UpdateFirewallRuleGroupAssociation     | -         |
| UpdateResolverConfig                   | -         |
| UpdateResolverDnssecConfig             | -         |
| UpdateResolverRule                     | -         |



## s3 ##


| Operation                              | Implemented |
| -------------------------------------- | ----------: |
| AbortMultipartUpload                   | ✅         |
| CompleteMultipartUpload ✨              | ✅         |
| CopyObject ✨                           | ✅         |
| CreateBucket ✨                         | ✅         |
| CreateMultipartUpload ✨                | ✅         |
| DeleteBucket ✨                         | ✅         |
| DeleteBucketAnalyticsConfiguration     | ✅         |
| DeleteBucketCors                       | ✅         |
| DeleteBucketEncryption                 | ✅         |
| DeleteBucketIntelligentTieringConfiguration | ✅         |
| DeleteBucketInventoryConfiguration     | ✅         |
| DeleteBucketLifecycle ✨                | ✅         |
| DeleteBucketMetricsConfiguration       | ✅         |
| DeleteBucketOwnershipControls          | ✅         |
| DeleteBucketPolicy ✨                   | ✅         |
| DeleteBucketReplication                | ✅         |
| DeleteBucketTagging                    | ✅         |
| DeleteBucketWebsite                    | ✅         |
| DeleteObject ✨                         | ✅         |
| DeleteObjectTagging ✨                  | ✅         |
| DeleteObjects ✨                        | ✅         |
| DeletePublicAccessBlock                | ✅         |
| GetBucketAccelerateConfiguration ✨     | ✅         |
| GetBucketAcl ✨                         | ✅         |
| GetBucketAnalyticsConfiguration        | ✅         |
| GetBucketCors ✨                        | ✅         |
| GetBucketEncryption ✨                  | ✅         |
| GetBucketIntelligentTieringConfiguration | ✅         |
| GetBucketInventoryConfiguration        | ✅         |
| GetBucketLifecycle                     | ✅         |
| GetBucketLifecycleConfiguration ✨      | ✅         |
| GetBucketLocation ✨                    | ✅         |
| GetBucketLogging ✨                     | ✅         |
| GetBucketMetricsConfiguration          | ✅         |
| GetBucketNotification                  | ✅         |
| GetBucketNotificationConfiguration ✨   | ✅         |
| GetBucketOwnershipControls             | ✅         |
| GetBucketPolicy ✨                      | ✅         |
| GetBucketPolicyStatus                  | ✅         |
| GetBucketReplication ✨                 | ✅         |
| GetBucketRequestPayment ✨              | ✅         |
| GetBucketTagging ✨                     | ✅         |
| GetBucketVersioning ✨                  | ✅         |
| GetBucketWebsite ✨                     | ✅         |
| GetObject ✨                            | ✅         |
| GetObjectAcl ✨                         | ✅         |
| GetObjectAttributes                    | ✅         |
| GetObjectLegalHold                     | ✅         |
| GetObjectLockConfiguration ✨           | ✅         |
| GetObjectRetention                     | ✅         |
| GetObjectTagging                       | ✅         |
| GetObjectTorrent                       | ✅         |
| GetPublicAccessBlock ✨                 | ✅         |
| HeadBucket ✨                           | ✅         |
| HeadObject ✨                           | ✅         |
| ListBucketAnalyticsConfigurations      | ✅         |
| ListBucketIntelligentTieringConfigurations | ✅         |
| ListBucketInventoryConfigurations      | ✅         |
| ListBucketMetricsConfigurations        | ✅         |
| ListBuckets ✨                          | ✅         |
| ListMultipartUploads                   | ✅         |
| ListObjectVersions ✨                   | ✅         |
| ListObjects ✨                          | ✅         |
| ListObjectsV2 ✨                        | ✅         |
| ListParts                              | ✅         |
| PutBucketAccelerateConfiguration       | ✅         |
| PutBucketAcl                           | ✅         |
| PutBucketAnalyticsConfiguration        | ✅         |
| PutBucketCors ✨                        | ✅         |
| PutBucketEncryption                    | ✅         |
| PutBucketIntelligentTieringConfiguration | ✅         |
| PutBucketInventoryConfiguration        | ✅         |
| PutBucketLifecycle                     | ✅         |
| PutBucketLifecycleConfiguration ✨      | ✅         |
| PutBucketLogging                       | ✅         |
| PutBucketMetricsConfiguration          | ✅         |
| PutBucketNotification                  | ✅         |
| PutBucketNotificationConfiguration ✨   | ✅         |
| PutBucketOwnershipControls             | ✅         |
| PutBucketPolicy ✨                      | ✅         |
| PutBucketReplication                   | ✅         |
| PutBucketRequestPayment ✨              | ✅         |
| PutBucketTagging ✨                     | ✅         |
| PutBucketVersioning ✨                  | ✅         |
| PutBucketWebsite ✨                     | ✅         |
| PutObject ✨                            | ✅         |
| PutObjectAcl ✨                         | ✅         |
| PutObjectLegalHold                     | ✅         |
| PutObjectLockConfiguration             | ✅         |
| PutObjectRetention                     | ✅         |
| PutObjectTagging ✨                     | ✅         |
| PutPublicAccessBlock                   | ✅         |
| RestoreObject ✨                        | ✅         |
| SelectObjectContent ✨                  | ✅         |
| UploadPart ✨                           | ✅         |
| UploadPartCopy                         | ✅         |
| WriteGetObjectResponse                 | ✅         |



## s3control ##


| Operation                              | Implemented |
| -------------------------------------- | ----------: |
| CreateAccessPoint                      | ✅         |
| CreateAccessPointForObjectLambda       | ✅         |
| CreateBucket                           | ✅         |
| CreateJob                              | ✅         |
| CreateMultiRegionAccessPoint           | ✅         |
| DeleteAccessPoint                      | ✅         |
| DeleteAccessPointForObjectLambda       | ✅         |
| DeleteAccessPointPolicy                | ✅         |
| DeleteAccessPointPolicyForObjectLambda | ✅         |
| DeleteBucket                           | ✅         |
| DeleteBucketLifecycleConfiguration     | ✅         |
| DeleteBucketPolicy                     | ✅         |
| DeleteBucketTagging                    | ✅         |
| DeleteJobTagging                       | ✅         |
| DeleteMultiRegionAccessPoint           | ✅         |
| DeletePublicAccessBlock ✨              | ✅         |
| DeleteStorageLensConfiguration         | ✅         |
| DeleteStorageLensConfigurationTagging  | ✅         |
| DescribeJob                            | ✅         |
| DescribeMultiRegionAccessPointOperation | ✅         |
| GetAccessPoint                         | ✅         |
| GetAccessPointConfigurationForObjectLambda | ✅         |
| GetAccessPointForObjectLambda          | ✅         |
| GetAccessPointPolicy                   | ✅         |
| GetAccessPointPolicyForObjectLambda    | ✅         |
| GetAccessPointPolicyStatus             | ✅         |
| GetAccessPointPolicyStatusForObjectLambda | ✅         |
| GetBucket                              | ✅         |
| GetBucketLifecycleConfiguration        | ✅         |
| GetBucketPolicy                        | ✅         |
| GetBucketTagging                       | ✅         |
| GetJobTagging                          | ✅         |
| GetMultiRegionAccessPoint              | ✅         |
| GetMultiRegionAccessPointPolicy        | ✅         |
| GetMultiRegionAccessPointPolicyStatus  | ✅         |
| GetPublicAccessBlock ✨                 | ✅         |
| GetStorageLensConfiguration            | ✅         |
| GetStorageLensConfigurationTagging     | ✅         |
| ListAccessPoints                       | ✅         |
| ListAccessPointsForObjectLambda        | ✅         |
| ListJobs                               | ✅         |
| ListMultiRegionAccessPoints            | ✅         |
| ListRegionalBuckets                    | ✅         |
| ListStorageLensConfigurations          | ✅         |
| PutAccessPointConfigurationForObjectLambda | ✅         |
| PutAccessPointPolicy                   | ✅         |
| PutAccessPointPolicyForObjectLambda    | ✅         |
| PutBucketLifecycleConfiguration        | ✅         |
| PutBucketPolicy                        | ✅         |
| PutBucketTagging                       | ✅         |
| PutJobTagging                          | ✅         |
| PutMultiRegionAccessPointPolicy        | ✅         |
| PutPublicAccessBlock ✨                 | ✅         |
| PutStorageLensConfiguration            | ✅         |
| PutStorageLensConfigurationTagging     | ✅         |
| UpdateJobPriority                      | ✅         |
| UpdateJobStatus                        | ✅         |



## sagemaker ##


| Operation                              | Implemented |
| -------------------------------------- | ----------: |
| AddTags                                | ✅         |
| AssociateTrialComponent                | ✅         |
| CreateEndpoint                         | ✅         |
| CreateEndpointConfig                   | ✅         |
| CreateExperiment                       | ✅         |
| CreateModel ✨                          | ✅         |
| CreateNotebookInstance                 | ✅         |
| CreateNotebookInstanceLifecycleConfig  | ✅         |
| CreateProcessingJob                    | ✅         |
| CreateTrainingJob                      | ✅         |
| CreateTrial                            | ✅         |
| CreateTrialComponent                   | ✅         |
| DeleteEndpoint                         | ✅         |
| DeleteEndpointConfig                   | ✅         |
| DeleteExperiment                       | ✅         |
| DeleteModel                            | ✅         |
| DeleteNotebookInstance                 | ✅         |
| DeleteNotebookInstanceLifecycleConfig  | ✅         |
| DeleteTags                             | ✅         |
| DeleteTrial                            | ✅         |
| DeleteTrialComponent                   | ✅         |
| DescribeEndpoint                       | ✅         |
| DescribeEndpointConfig                 | ✅         |
| DescribeExperiment                     | ✅         |
| DescribeModel ✨                        | ✅         |
| DescribeNotebookInstance               | ✅         |
| DescribeNotebookInstanceLifecycleConfig | ✅         |
| DescribeProcessingJob                  | ✅         |
| DescribeTrainingJob                    | ✅         |
| DescribeTrial                          | ✅         |
| DescribeTrialComponent                 | ✅         |
| DisassociateTrialComponent             | ✅         |
| ListAssociations                       | ✅         |
| ListExperiments                        | ✅         |
| ListModels                             | ✅         |
| ListProcessingJobs                     | ✅         |
| ListTags                               | ✅         |
| ListTrainingJobs                       | ✅         |
| ListTrialComponents                    | ✅         |
| ListTrials                             | ✅         |
| Search                                 | ✅         |
| StartNotebookInstance                  | ✅         |
| StopNotebookInstance                   | ✅         |
| UpdateEndpointWeightsAndCapacities     | ✅         |
| AddAssociation                         | -         |
| BatchDescribeModelPackage              | -         |
| CreateAction                           | -         |
| CreateAlgorithm                        | -         |
| CreateApp                              | -         |
| CreateAppImageConfig                   | -         |
| CreateArtifact                         | -         |
| CreateAutoMLJob                        | -         |
| CreateCodeRepository                   | -         |
| CreateCompilationJob                   | -         |
| CreateContext                          | -         |
| CreateDataQualityJobDefinition         | -         |
| CreateDeviceFleet                      | -         |
| CreateDomain                           | -         |
| CreateEdgePackagingJob                 | -         |
| CreateFeatureGroup                     | -         |
| CreateFlowDefinition                   | -         |
| CreateHumanTaskUi                      | -         |
| CreateHyperParameterTuningJob          | -         |
| CreateImage                            | -         |
| CreateImageVersion                     | -         |
| CreateInferenceRecommendationsJob      | -         |
| CreateLabelingJob                      | -         |
| CreateModelBiasJobDefinition           | -         |
| CreateModelExplainabilityJobDefinition | -         |
| CreateModelPackage                     | -         |
| CreateModelPackageGroup                | -         |
| CreateModelQualityJobDefinition        | -         |
| CreateMonitoringSchedule               | -         |
| CreatePipeline                         | -         |
| CreatePresignedDomainUrl               | -         |
| CreatePresignedNotebookInstanceUrl     | -         |
| CreateProject                          | -         |
| CreateStudioLifecycleConfig            | -         |
| CreateTransformJob                     | -         |
| CreateUserProfile                      | -         |
| CreateWorkforce                        | -         |
| CreateWorkteam                         | -         |
| DeleteAction                           | -         |
| DeleteAlgorithm                        | -         |
| DeleteApp                              | -         |
| DeleteAppImageConfig                   | -         |
| DeleteArtifact                         | -         |
| DeleteAssociation                      | -         |
| DeleteCodeRepository                   | -         |
| DeleteContext                          | -         |
| DeleteDataQualityJobDefinition         | -         |
| DeleteDeviceFleet                      | -         |
| DeleteDomain                           | -         |
| DeleteFeatureGroup                     | -         |
| DeleteFlowDefinition                   | -         |
| DeleteHumanTaskUi                      | -         |
| DeleteImage                            | -         |
| DeleteImageVersion                     | -         |
| DeleteModelBiasJobDefinition           | -         |
| DeleteModelExplainabilityJobDefinition | -         |
| DeleteModelPackage                     | -         |
| DeleteModelPackageGroup                | -         |
| DeleteModelPackageGroupPolicy          | -         |
| DeleteModelQualityJobDefinition        | -         |
| DeleteMonitoringSchedule               | -         |
| DeletePipeline                         | -         |
| DeleteProject                          | -         |
| DeleteStudioLifecycleConfig            | -         |
| DeleteUserProfile                      | -         |
| DeleteWorkforce                        | -         |
| DeleteWorkteam                         | -         |
| DeregisterDevices                      | -         |
| DescribeAction                         | -         |
| DescribeAlgorithm                      | -         |
| DescribeApp                            | -         |
| DescribeAppImageConfig                 | -         |
| DescribeArtifact                       | -         |
| DescribeAutoMLJob                      | -         |
| DescribeCodeRepository                 | -         |
| DescribeCompilationJob                 | -         |
| DescribeContext                        | -         |
| DescribeDataQualityJobDefinition       | -         |
| DescribeDevice                         | -         |
| DescribeDeviceFleet                    | -         |
| DescribeDomain                         | -         |
| DescribeEdgePackagingJob               | -         |
| DescribeFeatureGroup                   | -         |
| DescribeFeatureMetadata                | -         |
| DescribeFlowDefinition                 | -         |
| DescribeHumanTaskUi                    | -         |
| DescribeHyperParameterTuningJob        | -         |
| DescribeImage                          | -         |
| DescribeImageVersion                   | -         |
| DescribeInferenceRecommendationsJob    | -         |
| DescribeLabelingJob                    | -         |
| DescribeLineageGroup                   | -         |
| DescribeModelBiasJobDefinition         | -         |
| DescribeModelExplainabilityJobDefinition | -         |
| DescribeModelPackage                   | -         |
| DescribeModelPackageGroup              | -         |
| DescribeModelQualityJobDefinition      | -         |
| DescribeMonitoringSchedule             | -         |
| DescribePipeline                       | -         |
| DescribePipelineDefinitionForExecution | -         |
| DescribePipelineExecution              | -         |
| DescribeProject                        | -         |
| DescribeStudioLifecycleConfig          | -         |
| DescribeSubscribedWorkteam             | -         |
| DescribeTransformJob                   | -         |
| DescribeUserProfile                    | -         |
| DescribeWorkforce                      | -         |
| DescribeWorkteam                       | -         |
| DisableSagemakerServicecatalogPortfolio | -         |
| EnableSagemakerServicecatalogPortfolio | -         |
| GetDeviceFleetReport                   | -         |
| GetLineageGroupPolicy                  | -         |
| GetModelPackageGroupPolicy             | -         |
| GetSagemakerServicecatalogPortfolioStatus | -         |
| GetSearchSuggestions                   | -         |
| ListActions                            | -         |
| ListAlgorithms                         | -         |
| ListAppImageConfigs                    | -         |
| ListApps                               | -         |
| ListArtifacts                          | -         |
| ListAutoMLJobs                         | -         |
| ListCandidatesForAutoMLJob             | -         |
| ListCodeRepositories                   | -         |
| ListCompilationJobs                    | -         |
| ListContexts                           | -         |
| ListDataQualityJobDefinitions          | -         |
| ListDeviceFleets                       | -         |
| ListDevices                            | -         |
| ListDomains                            | -         |
| ListEdgePackagingJobs                  | -         |
| ListEndpointConfigs                    | -         |
| ListEndpoints                          | -         |
| ListFeatureGroups                      | -         |
| ListFlowDefinitions                    | -         |
| ListHumanTaskUis                       | -         |
| ListHyperParameterTuningJobs           | -         |
| ListImageVersions                      | -         |
| ListImages                             | -         |
| ListInferenceRecommendationsJobs       | -         |
| ListLabelingJobs                       | -         |
| ListLabelingJobsForWorkteam            | -         |
| ListLineageGroups                      | -         |
| ListModelBiasJobDefinitions            | -         |
| ListModelExplainabilityJobDefinitions  | -         |
| ListModelMetadata                      | -         |
| ListModelPackageGroups                 | -         |
| ListModelPackages                      | -         |
| ListModelQualityJobDefinitions         | -         |
| ListMonitoringExecutions               | -         |
| ListMonitoringSchedules                | -         |
| ListNotebookInstanceLifecycleConfigs   | -         |
| ListNotebookInstances                  | -         |
| ListPipelineExecutionSteps             | -         |
| ListPipelineExecutions                 | -         |
| ListPipelineParametersForExecution     | -         |
| ListPipelines                          | -         |
| ListProjects                           | -         |
| ListStudioLifecycleConfigs             | -         |
| ListSubscribedWorkteams                | -         |
| ListTrainingJobsForHyperParameterTuningJob | -         |
| ListTransformJobs                      | -         |
| ListUserProfiles                       | -         |
| ListWorkforces                         | -         |
| ListWorkteams                          | -         |
| PutModelPackageGroupPolicy             | -         |
| QueryLineage                           | -         |
| RegisterDevices                        | -         |
| RenderUiTemplate                       | -         |
| RetryPipelineExecution                 | -         |
| SendPipelineExecutionStepFailure       | -         |
| SendPipelineExecutionStepSuccess       | -         |
| StartMonitoringSchedule                | -         |
| StartPipelineExecution                 | -         |
| StopAutoMLJob                          | -         |
| StopCompilationJob                     | -         |
| StopEdgePackagingJob                   | -         |
| StopHyperParameterTuningJob            | -         |
| StopInferenceRecommendationsJob        | -         |
| StopLabelingJob                        | -         |
| StopMonitoringSchedule                 | -         |
| StopPipelineExecution                  | -         |
| StopProcessingJob                      | -         |
| StopTrainingJob                        | -         |
| StopTransformJob                       | -         |
| UpdateAction                           | -         |
| UpdateAppImageConfig                   | -         |
| UpdateArtifact                         | -         |
| UpdateCodeRepository                   | -         |
| UpdateContext                          | -         |
| UpdateDeviceFleet                      | -         |
| UpdateDevices                          | -         |
| UpdateDomain                           | -         |
| UpdateEndpoint                         | -         |
| UpdateExperiment                       | -         |
| UpdateFeatureGroup                     | -         |
| UpdateFeatureMetadata                  | -         |
| UpdateImage                            | -         |
| UpdateModelPackage                     | -         |
| UpdateMonitoringSchedule               | -         |
| UpdateNotebookInstance                 | -         |
| UpdateNotebookInstanceLifecycleConfig  | -         |
| UpdatePipeline                         | -         |
| UpdatePipelineExecution                | -         |
| UpdateProject                          | -         |
| UpdateTrainingJob                      | -         |
| UpdateTrial                            | -         |
| UpdateTrialComponent                   | -         |
| UpdateUserProfile                      | -         |
| UpdateWorkforce                        | -         |
| UpdateWorkteam                         | -         |



## secretsmanager ##


| Operation                              | Implemented |
| -------------------------------------- | ----------: |
| CreateSecret ✨                         | ✅         |
| DeleteResourcePolicy ✨                 | ✅         |
| DeleteSecret ✨                         | ✅         |
| DescribeSecret ✨                       | ✅         |
| GetRandomPassword ✨                    | ✅         |
| GetResourcePolicy ✨                    | ✅         |
| GetSecretValue ✨                       | ✅         |
| ListSecretVersionIds ✨                 | ✅         |
| ListSecrets ✨                          | ✅         |
| PutResourcePolicy ✨                    | ✅         |
| PutSecretValue ✨                       | ✅         |
| RestoreSecret                          | ✅         |
| RotateSecret ✨                         | ✅         |
| TagResource ✨                          | ✅         |
| UntagResource ✨                        | ✅         |
| UpdateSecret ✨                         | ✅         |
| UpdateSecretVersionStage ✨             | ✅         |
| CancelRotateSecret                     | -         |
| RemoveRegionsFromReplication           | -         |
| ReplicateSecretToRegions               | -         |
| StopReplicationToReplica               | -         |
| ValidateResourcePolicy ✨               | -         |



## serverlessrepo ##


| Operation                              | Implemented |
| -------------------------------------- | ----------: |
| CreateApplication ✨                    | ✅         |
| CreateApplicationVersion ✨             | ✅         |
| CreateCloudFormationChangeSet ✨        | ✅         |
| CreateCloudFormationTemplate ✨         | ✅         |
| DeleteApplication ✨                    | ✅         |
| GetCloudFormationTemplate ✨            | ✅         |
| ListApplicationVersions ✨              | ✅         |
| ListApplications ✨                     | ✅         |
| GetApplication                         | -         |
| GetApplicationPolicy                   | -         |
| ListApplicationDependencies            | -         |
| PutApplicationPolicy                   | -         |
| UnshareApplication                     | -         |
| UpdateApplication                      | -         |



## servicediscovery ##


| Operation                              | Implemented |
| -------------------------------------- | ----------: |
| CreateHttpNamespace ✨                  | ✅         |
| CreatePrivateDnsNamespace ✨            | ✅         |
| CreatePublicDnsNamespace ✨             | ✅         |
| CreateService ✨                        | ✅         |
| DeleteNamespace ✨                      | ✅         |
| DeleteService ✨                        | ✅         |
| DeregisterInstance ✨                   | ✅         |
| GetInstance ✨                          | ✅         |
| GetNamespace ✨                         | ✅         |
| GetOperation ✨                         | ✅         |
| GetService ✨                           | ✅         |
| ListInstances ✨                        | ✅         |
| ListNamespaces ✨                       | ✅         |
| ListServices ✨                         | ✅         |
| ListTagsForResource ✨                  | ✅         |
| RegisterInstance ✨                     | ✅         |
| TagResource ✨                          | ✅         |
| UntagResource ✨                        | ✅         |
| UpdateService ✨                        | ✅         |
| DiscoverInstances ✨                    | -         |
| GetInstancesHealthStatus               | -         |
| ListOperations                         | -         |
| UpdateHttpNamespace                    | -         |
| UpdateInstanceCustomHealthStatus       | -         |
| UpdatePrivateDnsNamespace              | -         |
| UpdatePublicDnsNamespace               | -         |



## ses ##


| Operation                              | Implemented |
| -------------------------------------- | ----------: |
| CreateConfigurationSet                 | ✅         |
| CreateConfigurationSetEventDestination | ✅         |
| CreateReceiptRule ✨                    | ✅         |
| CreateReceiptRuleSet ✨                 | ✅         |
| CreateTemplate ✨                       | ✅         |
| DeleteIdentity                         | ✅         |
| DeleteReceiptRule ✨                    | ✅         |
| DeleteReceiptRuleSet ✨                 | ✅         |
| DeleteTemplate ✨                       | ✅         |
| DescribeActiveReceiptRuleSet ✨         | ✅         |
| DescribeReceiptRule ✨                  | ✅         |
| DescribeReceiptRuleSet ✨               | ✅         |
| GetIdentityMailFromDomainAttributes    | ✅         |
| GetIdentityNotificationAttributes      | ✅         |
| GetIdentityVerificationAttributes ✨    | ✅         |
| GetSendQuota                           | ✅         |
| GetSendStatistics                      | ✅         |
| GetTemplate                            | ✅         |
| ListIdentities                         | ✅         |
| ListReceiptRuleSets ✨                  | ✅         |
| ListTemplates ✨                        | ✅         |
| ListVerifiedEmailAddresses             | ✅         |
| SendBulkTemplatedEmail ✨               | ✅         |
| SendEmail ✨                            | ✅         |
| SendRawEmail ✨                         | ✅         |
| SendTemplatedEmail ✨                   | ✅         |
| SetActiveReceiptRuleSet ✨              | ✅         |
| SetIdentityFeedbackForwardingEnabled   | ✅         |
| SetIdentityMailFromDomain              | ✅         |
| SetIdentityNotificationTopic           | ✅         |
| TestRenderTemplate                     | ✅         |
| UpdateReceiptRule                      | ✅         |
| UpdateTemplate                         | ✅         |
| VerifyDomainDkim                       | ✅         |
| VerifyDomainIdentity                   | ✅         |
| VerifyEmailAddress ✨                   | ✅         |
| VerifyEmailIdentity ✨                  | ✅         |
| CloneReceiptRuleSet                    | -         |
| CreateConfigurationSetTrackingOptions  | -         |
| CreateCustomVerificationEmailTemplate  | -         |
| CreateReceiptFilter                    | -         |
| DeleteConfigurationSet                 | -         |
| DeleteConfigurationSetEventDestination | -         |
| DeleteConfigurationSetTrackingOptions  | -         |
| DeleteCustomVerificationEmailTemplate  | -         |
| DeleteIdentityPolicy                   | -         |
| DeleteReceiptFilter                    | -         |
| DeleteVerifiedEmailAddress             | -         |
| DescribeConfigurationSet               | -         |
| GetAccountSendingEnabled               | -         |
| GetCustomVerificationEmailTemplate     | -         |
| GetIdentityDkimAttributes              | -         |
| GetIdentityPolicies                    | -         |
| ListConfigurationSets                  | -         |
| ListCustomVerificationEmailTemplates   | -         |
| ListIdentityPolicies                   | -         |
| ListReceiptFilters                     | -         |
| PutConfigurationSetDeliveryOptions     | -         |
| PutIdentityPolicy                      | -         |
| ReorderReceiptRuleSet                  | -         |
| SendBounce                             | -         |
| SendCustomVerificationEmail            | -         |
| SetIdentityDkimEnabled                 | -         |
| SetIdentityHeadersInNotificationsEnabled | -         |
| SetReceiptRulePosition                 | -         |
| UpdateAccountSendingEnabled            | -         |
| UpdateConfigurationSetEventDestination | -         |
| UpdateConfigurationSetReputationMetricsEnabled | -         |
| UpdateConfigurationSetSendingEnabled   | -         |
| UpdateConfigurationSetTrackingOptions  | -         |
| UpdateCustomVerificationEmailTemplate  | -         |



## sesv2 ##


| Operation                              | Implemented |
| -------------------------------------- | ----------: |
| CreateEmailIdentity ✨                  | ✅         |
| CreateEmailTemplate ✨                  | ✅         |
| DeleteEmailIdentity ✨                  | ✅         |
| DeleteEmailTemplate                    | ✅         |
| GetDomainStatisticsReport              | ✅         |
| GetEmailIdentity ✨                     | ✅         |
| ListDomainDeliverabilityCampaigns      | ✅         |
| ListEmailIdentities ✨                  | ✅         |
| ListEmailTemplates                     | ✅         |
| ListSuppressedDestinations             | ✅         |
| PutEmailIdentityDkimSigningAttributes  | ✅         |
| SendBulkEmail ✨                        | ✅         |
| SendEmail ✨                            | ✅         |
| CreateConfigurationSet                 | -         |
| CreateConfigurationSetEventDestination | -         |
| CreateContact                          | -         |
| CreateContactList                      | -         |
| CreateCustomVerificationEmailTemplate  | -         |
| CreateDedicatedIpPool                  | -         |
| CreateDeliverabilityTestReport         | -         |
| CreateEmailIdentityPolicy              | -         |
| CreateImportJob                        | -         |
| DeleteConfigurationSet                 | -         |
| DeleteConfigurationSetEventDestination | -         |
| DeleteContact                          | -         |
| DeleteContactList                      | -         |
| DeleteCustomVerificationEmailTemplate  | -         |
| DeleteDedicatedIpPool                  | -         |
| DeleteEmailIdentityPolicy              | -         |
| DeleteSuppressedDestination            | -         |
| GetAccount                             | -         |
| GetBlacklistReports                    | -         |
| GetConfigurationSet                    | -         |
| GetConfigurationSetEventDestinations   | -         |
| GetContact                             | -         |
| GetContactList                         | -         |
| GetCustomVerificationEmailTemplate     | -         |
| GetDedicatedIp                         | -         |
| GetDedicatedIps                        | -         |
| GetDeliverabilityDashboardOptions      | -         |
| GetDeliverabilityTestReport            | -         |
| GetDomainDeliverabilityCampaign        | -         |
| GetEmailIdentityPolicies               | -         |
| GetEmailTemplate                       | -         |
| GetImportJob                           | -         |
| GetSuppressedDestination               | -         |
| ListConfigurationSets                  | -         |
| ListContactLists                       | -         |
| ListContacts                           | -         |
| ListCustomVerificationEmailTemplates   | -         |
| ListDedicatedIpPools                   | -         |
| ListDeliverabilityTestReports          | -         |
| ListImportJobs                         | -         |
| ListTagsForResource                    | -         |
| PutAccountDedicatedIpWarmupAttributes  | -         |
| PutAccountDetails                      | -         |
| PutAccountSendingAttributes            | -         |
| PutAccountSuppressionAttributes        | -         |
| PutConfigurationSetDeliveryOptions     | -         |
| PutConfigurationSetReputationOptions   | -         |
| PutConfigurationSetSendingOptions      | -         |
| PutConfigurationSetSuppressionOptions  | -         |
| PutConfigurationSetTrackingOptions     | -         |
| PutDedicatedIpInPool                   | -         |
| PutDedicatedIpWarmupAttributes         | -         |
| PutDeliverabilityDashboardOption       | -         |
| PutEmailIdentityConfigurationSetAttributes | -         |
| PutEmailIdentityDkimAttributes         | -         |
| PutEmailIdentityFeedbackAttributes     | -         |
| PutEmailIdentityMailFromAttributes     | -         |
| PutSuppressedDestination               | -         |
| SendCustomVerificationEmail            | -         |
| TagResource                            | -         |
| TestRenderEmailTemplate                | -         |
| UntagResource                          | -         |
| UpdateConfigurationSetEventDestination | -         |
| UpdateContact                          | -         |
| UpdateContactList                      | -         |
| UpdateCustomVerificationEmailTemplate  | -         |
| UpdateEmailIdentityPolicy              | -         |
| UpdateEmailTemplate                    | -         |



## sns ##


| Operation                              | Implemented |
| -------------------------------------- | ----------: |
| AddPermission                          | ✅         |
| CheckIfPhoneNumberIsOptedOut           | ✅         |
| ConfirmSubscription ✨                  | ✅         |
| CreatePlatformApplication ✨            | ✅         |
| CreatePlatformEndpoint ✨               | ✅         |
| CreateTopic ✨                          | ✅         |
| DeleteEndpoint ✨                       | ✅         |
| DeletePlatformApplication ✨            | ✅         |
| DeleteTopic ✨                          | ✅         |
| GetEndpointAttributes ✨                | ✅         |
| GetPlatformApplicationAttributes       | ✅         |
| GetSMSAttributes                       | ✅         |
| GetSubscriptionAttributes ✨            | ✅         |
| GetTopicAttributes ✨                   | ✅         |
| ListEndpointsByPlatformApplication     | ✅         |
| ListPhoneNumbersOptedOut               | ✅         |
| ListPlatformApplications ✨             | ✅         |
| ListSubscriptions                      | ✅         |
| ListSubscriptionsByTopic ✨             | ✅         |
| ListTagsForResource ✨                  | ✅         |
| ListTopics ✨                           | ✅         |
| OptInPhoneNumber                       | ✅         |
| Publish ✨                              | ✅         |
| PublishBatch ✨                         | ✅         |
| RemovePermission                       | ✅         |
| SetEndpointAttributes                  | ✅         |
| SetPlatformApplicationAttributes       | ✅         |
| SetSMSAttributes                       | ✅         |
| SetSubscriptionAttributes ✨            | ✅         |
| SetTopicAttributes ✨                   | ✅         |
| Subscribe ✨                            | ✅         |
| TagResource ✨                          | ✅         |
| Unsubscribe ✨                          | ✅         |
| UntagResource ✨                        | ✅         |
| CreateSMSSandboxPhoneNumber            | -         |
| DeleteSMSSandboxPhoneNumber            | -         |
| GetSMSSandboxAccountStatus             | -         |
| ListOriginationNumbers                 | -         |
| ListSMSSandboxPhoneNumbers             | -         |
| VerifySMSSandboxPhoneNumber            | -         |



## sqs ##


| Operation                              | Implemented |
| -------------------------------------- | ----------: |
| AddPermission                          | ✅         |
| ChangeMessageVisibility ✨              | ✅         |
| ChangeMessageVisibilityBatch           | ✅         |
| CreateQueue ✨                          | ✅         |
| DeleteMessage ✨                        | ✅         |
| DeleteMessageBatch ✨                   | ✅         |
| DeleteQueue ✨                          | ✅         |
| GetQueueAttributes ✨                   | ✅         |
| GetQueueUrl ✨                          | ✅         |
| ListDeadLetterSourceQueues ✨           | ✅         |
| ListQueueTags ✨                        | ✅         |
| ListQueues ✨                           | ✅         |
| PurgeQueue ✨                           | ✅         |
| ReceiveMessage ✨                       | ✅         |
| RemovePermission                       | ✅         |
| SendMessage ✨                          | ✅         |
| SendMessageBatch ✨                     | ✅         |
| SetQueueAttributes ✨                   | ✅         |
| TagQueue ✨                             | ✅         |
| UntagQueue ✨                           | ✅         |



## ssm ##


| Operation                              | Implemented |
| -------------------------------------- | ----------: |
| AddTagsToResource                      | ✅         |
| CancelCommand ✨                        | ✅         |
| CreateDocument                         | ✅         |
| CreateMaintenanceWindow                | ✅         |
| DeleteDocument                         | ✅         |
| DeleteMaintenanceWindow                | ✅         |
| DeleteParameter ✨                      | ✅         |
| DeleteParameters                       | ✅         |
| DescribeDocument                       | ✅         |
| DescribeDocumentPermission             | ✅         |
| DescribeInstanceInformation ✨          | ✅         |
| DescribeMaintenanceWindows             | ✅         |
| DescribeParameters ✨                   | ✅         |
| GetCommandInvocation ✨                 | ✅         |
| GetDocument                            | ✅         |
| GetMaintenanceWindow                   | ✅         |
| GetParameter ✨                         | ✅         |
| GetParameterHistory                    | ✅         |
| GetParameters ✨                        | ✅         |
| GetParametersByPath ✨                  | ✅         |
| LabelParameterVersion ✨                | ✅         |
| ListCommandInvocations                 | ✅         |
| ListCommands                           | ✅         |
| ListDocuments                          | ✅         |
| ListTagsForResource                    | ✅         |
| ModifyDocumentPermission               | ✅         |
| PutParameter ✨                         | ✅         |
| RemoveTagsFromResource                 | ✅         |
| SendCommand ✨                          | ✅         |
| UpdateDocument                         | ✅         |
| UpdateDocumentDefaultVersion           | ✅         |
| AssociateOpsItemRelatedItem            | -         |
| CancelMaintenanceWindowExecution       | -         |
| CreateActivation                       | -         |
| CreateAssociation                      | -         |
| CreateAssociationBatch                 | -         |
| CreateOpsItem                          | -         |
| CreateOpsMetadata                      | -         |
| CreatePatchBaseline                    | -         |
| CreateResourceDataSync                 | -         |
| DeleteActivation                       | -         |
| DeleteAssociation                      | -         |
| DeleteInventory                        | -         |
| DeleteOpsMetadata                      | -         |
| DeletePatchBaseline                    | -         |
| DeleteResourceDataSync                 | -         |
| DeregisterManagedInstance              | -         |
| DeregisterPatchBaselineForPatchGroup   | -         |
| DeregisterTargetFromMaintenanceWindow  | -         |
| DeregisterTaskFromMaintenanceWindow    | -         |
| DescribeActivations                    | -         |
| DescribeAssociation                    | -         |
| DescribeAssociationExecutionTargets    | -         |
| DescribeAssociationExecutions          | -         |
| DescribeAutomationExecutions           | -         |
| DescribeAutomationStepExecutions       | -         |
| DescribeAvailablePatches               | -         |
| DescribeEffectiveInstanceAssociations  | -         |
| DescribeEffectivePatchesForPatchBaseline | -         |
| DescribeInstanceAssociationsStatus     | -         |
| DescribeInstancePatchStates            | -         |
| DescribeInstancePatchStatesForPatchGroup | -         |
| DescribeInstancePatches                | -         |
| DescribeInventoryDeletions             | -         |
| DescribeMaintenanceWindowExecutionTaskInvocations | -         |
| DescribeMaintenanceWindowExecutionTasks | -         |
| DescribeMaintenanceWindowExecutions    | -         |
| DescribeMaintenanceWindowSchedule      | -         |
| DescribeMaintenanceWindowTargets       | -         |
| DescribeMaintenanceWindowTasks         | -         |
| DescribeMaintenanceWindowsForTarget    | -         |
| DescribeOpsItems                       | -         |
| DescribePatchBaselines                 | -         |
| DescribePatchGroupState                | -         |
| DescribePatchGroups                    | -         |
| DescribePatchProperties                | -         |
| DescribeSessions                       | -         |
| DisassociateOpsItemRelatedItem         | -         |
| GetAutomationExecution                 | -         |
| GetCalendarState                       | -         |
| GetConnectionStatus                    | -         |
| GetDefaultPatchBaseline                | -         |
| GetDeployablePatchSnapshotForInstance  | -         |
| GetInventory                           | -         |
| GetInventorySchema                     | -         |
| GetMaintenanceWindowExecution          | -         |
| GetMaintenanceWindowExecutionTask      | -         |
| GetMaintenanceWindowExecutionTaskInvocation | -         |
| GetMaintenanceWindowTask               | -         |
| GetOpsItem                             | -         |
| GetOpsMetadata                         | -         |
| GetOpsSummary                          | -         |
| GetPatchBaseline                       | -         |
| GetPatchBaselineForPatchGroup          | -         |
| GetServiceSetting                      | -         |
| ListAssociationVersions                | -         |
| ListAssociations                       | -         |
| ListComplianceItems                    | -         |
| ListComplianceSummaries                | -         |
| ListDocumentMetadataHistory            | -         |
| ListDocumentVersions                   | -         |
| ListInventoryEntries                   | -         |
| ListOpsItemEvents                      | -         |
| ListOpsItemRelatedItems                | -         |
| ListOpsMetadata                        | -         |
| ListResourceComplianceSummaries        | -         |
| ListResourceDataSync                   | -         |
| PutComplianceItems                     | -         |
| PutInventory                           | -         |
| RegisterDefaultPatchBaseline           | -         |
| RegisterPatchBaselineForPatchGroup     | -         |
| RegisterTargetWithMaintenanceWindow    | -         |
| RegisterTaskWithMaintenanceWindow      | -         |
| ResetServiceSetting                    | -         |
| ResumeSession                          | -         |
| SendAutomationSignal                   | -         |
| StartAssociationsOnce                  | -         |
| StartAutomationExecution               | -         |
| StartChangeRequestExecution            | -         |
| StartSession                           | -         |
| StopAutomationExecution                | -         |
| TerminateSession                       | -         |
| UnlabelParameterVersion                | -         |
| UpdateAssociation                      | -         |
| UpdateAssociationStatus                | -         |
| UpdateDocumentMetadata                 | -         |
| UpdateMaintenanceWindow                | -         |
| UpdateMaintenanceWindowTarget          | -         |
| UpdateMaintenanceWindowTask            | -         |
| UpdateManagedInstanceRole              | -         |
| UpdateOpsItem                          | -         |
| UpdateOpsMetadata                      | -         |
| UpdatePatchBaseline                    | -         |
| UpdateResourceDataSync                 | -         |
| UpdateServiceSetting                   | -         |



## stepfunctions ##


| Operation                              | Implemented |
| -------------------------------------- | ----------: |
| CreateActivity ✨                       | ✅         |
| CreateStateMachine ✨                   | ✅         |
| DeleteActivity ✨                       | ✅         |
| DeleteStateMachine ✨                   | ✅         |
| DescribeActivity ✨                     | ✅         |
| DescribeExecution ✨                    | ✅         |
| DescribeStateMachine ✨                 | ✅         |
| DescribeStateMachineForExecution ✨     | ✅         |
| GetActivityTask                        | ✅         |
| GetExecutionHistory ✨                  | ✅         |
| ListActivities ✨                       | ✅         |
| ListExecutions ✨                       | ✅         |
| ListStateMachines ✨                    | ✅         |
| ListTagsForResource                    | ✅         |
| SendTaskFailure                        | ✅         |
| SendTaskHeartbeat                      | ✅         |
| SendTaskSuccess                        | ✅         |
| StartExecution ✨                       | ✅         |
| StopExecution                          | ✅         |
| TagResource                            | ✅         |
| UntagResource                          | ✅         |
| UpdateStateMachine ✨                   | ✅         |
| StartSyncExecution                     | -         |



## sts ##


| Operation                              | Implemented |
| -------------------------------------- | ----------: |
| AssumeRole ✨                           | ✅         |
| AssumeRoleWithSAML ✨                   | ✅         |
| AssumeRoleWithWebIdentity ✨            | ✅         |
| GetCallerIdentity ✨                    | ✅         |
| GetFederationToken ✨                   | ✅         |
| GetSessionToken ✨                      | ✅         |
| DecodeAuthorizationMessage             | -         |
| GetAccessKeyInfo                       | -         |



## support ##


| Operation                              | Implemented |
| -------------------------------------- | ----------: |
| CreateCase ✨                           | ✅         |
| DescribeCases ✨                        | ✅         |
| DescribeTrustedAdvisorChecks           | ✅         |
| RefreshTrustedAdvisorCheck             | ✅         |
| ResolveCase ✨                          | ✅         |
| AddAttachmentsToSet                    | -         |
| AddCommunicationToCase                 | -         |
| DescribeAttachment                     | -         |
| DescribeCommunications                 | -         |
| DescribeServices                       | -         |
| DescribeSeverityLevels                 | -         |
| DescribeTrustedAdvisorCheckRefreshStatuses | -         |
| DescribeTrustedAdvisorCheckResult      | -         |
| DescribeTrustedAdvisorCheckSummaries   | -         |



## swf ##


| Operation                              | Implemented |
| -------------------------------------- | ----------: |
| CountPendingActivityTasks              | ✅         |
| CountPendingDecisionTasks              | ✅         |
| DeprecateActivityType                  | ✅         |
| DeprecateDomain                        | ✅         |
| DeprecateWorkflowType                  | ✅         |
| DescribeActivityType                   | ✅         |
| DescribeDomain                         | ✅         |
| DescribeWorkflowExecution              | ✅         |
| DescribeWorkflowType                   | ✅         |
| GetWorkflowExecutionHistory ✨          | ✅         |
| ListActivityTypes                      | ✅         |
| ListClosedWorkflowExecutions           | ✅         |
| ListDomains                            | ✅         |
| ListOpenWorkflowExecutions             | ✅         |
| ListWorkflowTypes ✨                    | ✅         |
| PollForActivityTask ✨                  | ✅         |
| PollForDecisionTask ✨                  | ✅         |
| RecordActivityTaskHeartbeat            | ✅         |
| RegisterActivityType ✨                 | ✅         |
| RegisterDomain ✨                       | ✅         |
| RegisterWorkflowType ✨                 | ✅         |
| RespondActivityTaskCompleted ✨         | ✅         |
| RespondActivityTaskFailed              | ✅         |
| RespondDecisionTaskCompleted ✨         | ✅         |
| SignalWorkflowExecution                | ✅         |
| StartWorkflowExecution ✨               | ✅         |
| TerminateWorkflowExecution             | ✅         |
| UndeprecateActivityType                | ✅         |
| UndeprecateDomain                      | ✅         |
| UndeprecateWorkflowType                | ✅         |
| CountClosedWorkflowExecutions          | -         |
| CountOpenWorkflowExecutions            | -         |
| ListTagsForResource                    | -         |
| RequestCancelWorkflowExecution         | -         |
| RespondActivityTaskCanceled            | -         |
| TagResource                            | -         |
| UntagResource                          | -         |



## timestream-query ##


| Operation                              | Implemented |
| -------------------------------------- | ----------: |
| Query ✨                                | ✅         |
| CancelQuery                            | -         |
| CreateScheduledQuery                   | -         |
| DeleteScheduledQuery                   | -         |
| DescribeEndpoints                      | -         |
| DescribeScheduledQuery                 | -         |
| ExecuteScheduledQuery                  | -         |
| ListScheduledQueries                   | -         |
| ListTagsForResource                    | -         |
| PrepareQuery                           | -         |
| TagResource                            | -         |
| UntagResource                          | -         |
| UpdateScheduledQuery                   | -         |



## timestream-write ##


| Operation                              | Implemented |
| -------------------------------------- | ----------: |
| CreateDatabase ✨                       | ✅         |
| CreateTable ✨                          | ✅         |
| DeleteDatabase ✨                       | ✅         |
| DeleteTable ✨                          | ✅         |
| DescribeDatabase ✨                     | ✅         |
| DescribeTable ✨                        | ✅         |
| ListDatabases ✨                        | ✅         |
| ListTables ✨                           | ✅         |
| WriteRecords ✨                         | ✅         |
| DescribeEndpoints                      | -         |
| ListTagsForResource                    | -         |
| TagResource                            | -         |
| UntagResource                          | -         |
| UpdateDatabase                         | -         |
| UpdateTable                            | -         |



## transfer ##


| Operation                              | Implemented |
| -------------------------------------- | ----------: |
| CreateServer ✨                         | ✅         |
| CreateUser ✨                           | ✅         |
| DeleteServer ✨                         | ✅         |
| DeleteSshPublicKey ✨                   | ✅         |
| DeleteUser ✨                           | ✅         |
| DescribeServer ✨                       | ✅         |
| DescribeUser ✨                         | ✅         |
| ImportSshPublicKey ✨                   | ✅         |
| ListServers                            | ✅         |
| ListUsers ✨                            | ✅         |
| UpdateUser ✨                           | ✅         |
| CreateAccess                           | -         |
| CreateWorkflow                         | -         |
| DeleteAccess                           | -         |
| DeleteWorkflow                         | -         |
| DescribeAccess                         | -         |
| DescribeExecution                      | -         |
| DescribeSecurityPolicy                 | -         |
| DescribeWorkflow                       | -         |
| ListAccesses                           | -         |
| ListExecutions                         | -         |
| ListSecurityPolicies                   | -         |
| ListTagsForResource                    | -         |
| ListWorkflows                          | -         |
| SendWorkflowStepState                  | -         |
| StartServer                            | -         |
| StopServer                             | -         |
| TagResource                            | -         |
| TestIdentityProvider                   | -         |
| UntagResource                          | -         |
| UpdateAccess                           | -         |
| UpdateServer                           | -         |



## xray ##


| Operation                              | Implemented |
| -------------------------------------- | ----------: |
| BatchGetTraces                         | ✅         |
| CreateGroup                            | ✅         |
| CreateSamplingRule ✨                   | ✅         |
| DeleteGroup                            | ✅         |
| DeleteSamplingRule ✨                   | ✅         |
| GetEncryptionConfig                    | ✅         |
| GetGroup                               | ✅         |
| GetGroups                              | ✅         |
| GetInsight                             | ✅         |
| GetInsightEvents                       | ✅         |
| GetInsightImpactGraph                  | ✅         |
| GetInsightSummaries                    | ✅         |
| GetSamplingRules ✨                     | ✅         |
| GetSamplingStatisticSummaries          | ✅         |
| GetSamplingTargets                     | ✅         |
| GetServiceGraph                        | ✅         |
| GetTimeSeriesServiceStatistics         | ✅         |
| GetTraceGraph                          | ✅         |
| GetTraceSummaries ✨                    | ✅         |
| ListTagsForResource                    | ✅         |
| PutEncryptionConfig                    | ✅         |
| PutTelemetryRecords ✨                  | ✅         |
| PutTraceSegments ✨                     | ✅         |
| TagResource                            | ✅         |
| UntagResource                          | ✅         |
| UpdateGroup                            | ✅         |
| UpdateSamplingRule ✨                   | ✅         |



