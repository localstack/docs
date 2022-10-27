---
title: "LocalStack Coverage"
linkTitle: "LocalStack Coverage"
weight: 100
description: >
  Overview of the implemented AWS APIs in LocalStack
---



<div class="coverage-report">

## acm ##

<table>
  <thead>
    <tr>
      <th>Operation</th>
      <th style="text-align:right">Implemented</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td>AddTagsToCertificate</td>
       <td style="text-align:right">✅</td>
    </tr>
    <tr>
      <td>DeleteCertificate <a href="#misc" title="covered by our integration test suite">✨</a></td>
       <td style="text-align:right">✅</td>
    </tr>
    <tr>
      <td>DescribeCertificate <a href="#misc" title="covered by our integration test suite">✨</a></td>
       <td style="text-align:right">✅</td>
    </tr>
    <tr>
      <td>ExportCertificate</td>
       <td style="text-align:right">✅</td>
    </tr>
    <tr>
      <td>GetCertificate</td>
       <td style="text-align:right">✅</td>
    </tr>
    <tr>
      <td>ImportCertificate <a href="#misc" title="covered by our integration test suite">✨</a></td>
       <td style="text-align:right">✅</td>
    </tr>
    <tr>
      <td>ListCertificates <a href="#misc" title="covered by our integration test suite">✨</a></td>
       <td style="text-align:right">✅</td>
    </tr>
    <tr>
      <td>ListTagsForCertificate <a href="#misc" title="covered by our integration test suite">✨</a></td>
       <td style="text-align:right">✅</td>
    </tr>
    <tr>
      <td>RemoveTagsFromCertificate</td>
       <td style="text-align:right">✅</td>
    </tr>
    <tr>
      <td>RequestCertificate <a href="#misc" title="covered by our integration test suite">✨</a></td>
       <td style="text-align:right">✅</td>
    </tr>
    <tr>
      <td>ResendValidationEmail</td>
       <td style="text-align:right">✅</td>
    </tr>
  </tbody>
  <tbody>    <tr>
      <td><a data-toggle="collapse" href=".acm-notimplemented">Show missing</a></td>
      <td style="text-align:right"></td>
    </tr>
  </tbody>
  <tbody class="collapse acm-notimplemented">     <tr>
      <td>GetAccountConfiguration</td>
       <td style="text-align:right">-</td>
    </tr>
    <tr>
      <td>PutAccountConfiguration</td>
       <td style="text-align:right">-</td>
    </tr>
    <tr>
      <td>RenewCertificate</td>
       <td style="text-align:right">-</td>
    </tr>
    <tr>
      <td>UpdateCertificateOptions</td>
       <td style="text-align:right">-</td>
    </tr>
  </tbody>
 </table>


## amplify ##

<table>
  <thead>
    <tr>
      <th>Operation</th>
      <th style="text-align:right">Implemented</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td>CreateApp (Pro)  <a href="#misc" title="covered by our integration test suite">✨</a></td>
       <td style="text-align:right">✅</td>
    </tr>
    <tr>
      <td>CreateBackendEnvironment (Pro)  <a href="#misc" title="covered by our integration test suite">✨</a></td>
       <td style="text-align:right">✅</td>
    </tr>
    <tr>
      <td>CreateBranch (Pro)  <a href="#misc" title="covered by our integration test suite">✨</a></td>
       <td style="text-align:right">✅</td>
    </tr>
    <tr>
      <td>CreateWebhook (Pro)  <a href="#misc" title="covered by our integration test suite">✨</a></td>
       <td style="text-align:right">✅</td>
    </tr>
    <tr>
      <td>DeleteApp (Pro)  <a href="#misc" title="covered by our integration test suite">✨</a></td>
       <td style="text-align:right">✅</td>
    </tr>
    <tr>
      <td>DeleteBackendEnvironment (Pro)  <a href="#misc" title="covered by our integration test suite">✨</a></td>
       <td style="text-align:right">✅</td>
    </tr>
    <tr>
      <td>DeleteBranch (Pro)  <a href="#misc" title="covered by our integration test suite">✨</a></td>
       <td style="text-align:right">✅</td>
    </tr>
    <tr>
      <td>DeleteWebhook (Pro)  <a href="#misc" title="covered by our integration test suite">✨</a></td>
       <td style="text-align:right">✅</td>
    </tr>
    <tr>
      <td>GetApp (Pro)  <a href="#misc" title="covered by our integration test suite">✨</a></td>
       <td style="text-align:right">✅</td>
    </tr>
    <tr>
      <td>GetBackendEnvironment (Pro)  <a href="#misc" title="covered by our integration test suite">✨</a></td>
       <td style="text-align:right">✅</td>
    </tr>
    <tr>
      <td>GetBranch (Pro)  <a href="#misc" title="covered by our integration test suite">✨</a></td>
       <td style="text-align:right">✅</td>
    </tr>
    <tr>
      <td>GetWebhook (Pro)  <a href="#misc" title="covered by our integration test suite">✨</a></td>
       <td style="text-align:right">✅</td>
    </tr>
    <tr>
      <td>ListApps (Pro)  <a href="#misc" title="covered by our integration test suite">✨</a></td>
       <td style="text-align:right">✅</td>
    </tr>
    <tr>
      <td>ListBranches (Pro)  <a href="#misc" title="covered by our integration test suite">✨</a></td>
       <td style="text-align:right">✅</td>
    </tr>
    <tr>
      <td>ListTagsForResource (Pro)  <a href="#misc" title="covered by our integration test suite">✨</a></td>
       <td style="text-align:right">✅</td>
    </tr>
    <tr>
      <td>TagResource (Pro)  <a href="#misc" title="covered by our integration test suite">✨</a></td>
       <td style="text-align:right">✅</td>
    </tr>
    <tr>
      <td>UntagResource (Pro)  <a href="#misc" title="covered by our integration test suite">✨</a></td>
       <td style="text-align:right">✅</td>
    </tr>
    <tr>
      <td>UpdateApp (Pro)  <a href="#misc" title="covered by our integration test suite">✨</a></td>
       <td style="text-align:right">✅</td>
    </tr>
    <tr>
      <td>UpdateWebhook (Pro)  <a href="#misc" title="covered by our integration test suite">✨</a></td>
       <td style="text-align:right">✅</td>
    </tr>
  </tbody>
  <tbody>    <tr>
      <td><a data-toggle="collapse" href=".amplify-notimplemented">Show missing</a></td>
      <td style="text-align:right"></td>
    </tr>
  </tbody>
  <tbody class="collapse amplify-notimplemented">     <tr>
      <td>CreateDeployment</td>
       <td style="text-align:right">-</td>
    </tr>
    <tr>
      <td>CreateDomainAssociation</td>
       <td style="text-align:right">-</td>
    </tr>
    <tr>
      <td>DeleteDomainAssociation</td>
       <td style="text-align:right">-</td>
    </tr>
    <tr>
      <td>DeleteJob</td>
       <td style="text-align:right">-</td>
    </tr>
    <tr>
      <td>GenerateAccessLogs</td>
       <td style="text-align:right">-</td>
    </tr>
    <tr>
      <td>GetArtifactUrl</td>
       <td style="text-align:right">-</td>
    </tr>
    <tr>
      <td>GetDomainAssociation</td>
       <td style="text-align:right">-</td>
    </tr>
    <tr>
      <td>GetJob</td>
       <td style="text-align:right">-</td>
    </tr>
    <tr>
      <td>ListArtifacts</td>
       <td style="text-align:right">-</td>
    </tr>
    <tr>
      <td>ListBackendEnvironments</td>
       <td style="text-align:right">-</td>
    </tr>
    <tr>
      <td>ListDomainAssociations</td>
       <td style="text-align:right">-</td>
    </tr>
    <tr>
      <td>ListJobs</td>
       <td style="text-align:right">-</td>
    </tr>
    <tr>
      <td>ListWebhooks</td>
       <td style="text-align:right">-</td>
    </tr>
    <tr>
      <td>StartDeployment</td>
       <td style="text-align:right">-</td>
    </tr>
    <tr>
      <td>StartJob</td>
       <td style="text-align:right">-</td>
    </tr>
    <tr>
      <td>StopJob</td>
       <td style="text-align:right">-</td>
    </tr>
    <tr>
      <td>UpdateBranch</td>
       <td style="text-align:right">-</td>
    </tr>
    <tr>
      <td>UpdateDomainAssociation</td>
       <td style="text-align:right">-</td>
    </tr>
  </tbody>
 </table>


## apigateway ##

<table>
  <thead>
    <tr>
      <th>Operation</th>
      <th style="text-align:right">Implemented</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td>CreateApiKey <a href="#misc" title="covered by our integration test suite">✨</a></td>
       <td style="text-align:right">✅</td>
    </tr>
    <tr>
      <td>CreateAuthorizer <a href="#misc" title="covered by our integration test suite">✨</a></td>
       <td style="text-align:right">✅</td>
    </tr>
    <tr>
      <td>CreateBasePathMapping <a href="#misc" title="covered by our integration test suite">✨</a></td>
       <td style="text-align:right">✅</td>
    </tr>
    <tr>
      <td>CreateDeployment <a href="#misc" title="covered by our integration test suite">✨</a></td>
       <td style="text-align:right">✅</td>
    </tr>
    <tr>
      <td>CreateDocumentationPart</td>
       <td style="text-align:right">✅</td>
    </tr>
    <tr>
      <td>CreateDomainName <a href="#misc" title="covered by our integration test suite">✨</a></td>
       <td style="text-align:right">✅</td>
    </tr>
    <tr>
      <td>CreateModel <a href="#misc" title="covered by our integration test suite">✨</a></td>
       <td style="text-align:right">✅</td>
    </tr>
    <tr>
      <td>CreateRequestValidator <a href="#misc" title="covered by our integration test suite">✨</a></td>
       <td style="text-align:right">✅</td>
    </tr>
    <tr>
      <td>CreateResource <a href="#misc" title="covered by our integration test suite">✨</a></td>
       <td style="text-align:right">✅</td>
    </tr>
    <tr>
      <td>CreateRestApi <a href="#misc" title="covered by our integration test suite">✨</a></td>
       <td style="text-align:right">✅</td>
    </tr>
    <tr>
      <td>CreateStage <a href="#misc" title="covered by our integration test suite">✨</a></td>
       <td style="text-align:right">✅</td>
    </tr>
    <tr>
      <td>CreateUsagePlan <a href="#misc" title="covered by our integration test suite">✨</a></td>
       <td style="text-align:right">✅</td>
    </tr>
    <tr>
      <td>CreateUsagePlanKey <a href="#misc" title="covered by our integration test suite">✨</a></td>
       <td style="text-align:right">✅</td>
    </tr>
    <tr>
      <td>CreateVpcLink</td>
       <td style="text-align:right">✅</td>
    </tr>
    <tr>
      <td>DeleteApiKey <a href="#misc" title="covered by our integration test suite">✨</a></td>
       <td style="text-align:right">✅</td>
    </tr>
    <tr>
      <td>DeleteAuthorizer <a href="#misc" title="covered by our integration test suite">✨</a></td>
       <td style="text-align:right">✅</td>
    </tr>
    <tr>
      <td>DeleteBasePathMapping <a href="#misc" title="covered by our integration test suite">✨</a></td>
       <td style="text-align:right">✅</td>
    </tr>
    <tr>
      <td>DeleteClientCertificate</td>
       <td style="text-align:right">✅</td>
    </tr>
    <tr>
      <td>DeleteDeployment</td>
       <td style="text-align:right">✅</td>
    </tr>
    <tr>
      <td>DeleteDocumentationPart</td>
       <td style="text-align:right">✅</td>
    </tr>
    <tr>
      <td>DeleteDomainName <a href="#misc" title="covered by our integration test suite">✨</a></td>
       <td style="text-align:right">✅</td>
    </tr>
    <tr>
      <td>DeleteGatewayResponse</td>
       <td style="text-align:right">✅</td>
    </tr>
    <tr>
      <td>DeleteIntegration <a href="#misc" title="covered by our integration test suite">✨</a></td>
       <td style="text-align:right">✅</td>
    </tr>
    <tr>
      <td>DeleteIntegrationResponse <a href="#misc" title="covered by our integration test suite">✨</a></td>
       <td style="text-align:right">✅</td>
    </tr>
    <tr>
      <td>DeleteMethod <a href="#misc" title="covered by our integration test suite">✨</a></td>
       <td style="text-align:right">✅</td>
    </tr>
    <tr>
      <td>DeleteMethodResponse <a href="#misc" title="covered by our integration test suite">✨</a></td>
       <td style="text-align:right">✅</td>
    </tr>
    <tr>
      <td>DeleteModel</td>
       <td style="text-align:right">✅</td>
    </tr>
    <tr>
      <td>DeleteRequestValidator <a href="#misc" title="covered by our integration test suite">✨</a></td>
       <td style="text-align:right">✅</td>
    </tr>
    <tr>
      <td>DeleteResource <a href="#misc" title="covered by our integration test suite">✨</a></td>
       <td style="text-align:right">✅</td>
    </tr>
    <tr>
      <td>DeleteRestApi <a href="#misc" title="covered by our integration test suite">✨</a></td>
       <td style="text-align:right">✅</td>
    </tr>
    <tr>
      <td>DeleteStage <a href="#misc" title="covered by our integration test suite">✨</a></td>
       <td style="text-align:right">✅</td>
    </tr>
    <tr>
      <td>DeleteUsagePlan</td>
       <td style="text-align:right">✅</td>
    </tr>
    <tr>
      <td>DeleteUsagePlanKey</td>
       <td style="text-align:right">✅</td>
    </tr>
    <tr>
      <td>DeleteVpcLink</td>
       <td style="text-align:right">✅</td>
    </tr>
    <tr>
      <td>GenerateClientCertificate</td>
       <td style="text-align:right">✅</td>
    </tr>
    <tr>
      <td>GetAccount <a href="#misc" title="covered by our integration test suite">✨</a></td>
       <td style="text-align:right">✅</td>
    </tr>
    <tr>
      <td>GetApiKey</td>
       <td style="text-align:right">✅</td>
    </tr>
    <tr>
      <td>GetApiKeys <a href="#misc" title="covered by our integration test suite">✨</a></td>
       <td style="text-align:right">✅</td>
    </tr>
    <tr>
      <td>GetAuthorizer <a href="#misc" title="covered by our integration test suite">✨</a></td>
       <td style="text-align:right">✅</td>
    </tr>
    <tr>
      <td>GetAuthorizers <a href="#misc" title="covered by our integration test suite">✨</a></td>
       <td style="text-align:right">✅</td>
    </tr>
    <tr>
      <td>GetBasePathMapping <a href="#misc" title="covered by our integration test suite">✨</a></td>
       <td style="text-align:right">✅</td>
    </tr>
    <tr>
      <td>GetBasePathMappings <a href="#misc" title="covered by our integration test suite">✨</a></td>
       <td style="text-align:right">✅</td>
    </tr>
    <tr>
      <td>GetClientCertificate</td>
       <td style="text-align:right">✅</td>
    </tr>
    <tr>
      <td>GetClientCertificates</td>
       <td style="text-align:right">✅</td>
    </tr>
    <tr>
      <td>GetDeployment <a href="#misc" title="covered by our integration test suite">✨</a></td>
       <td style="text-align:right">✅</td>
    </tr>
    <tr>
      <td>GetDeployments <a href="#misc" title="covered by our integration test suite">✨</a></td>
       <td style="text-align:right">✅</td>
    </tr>
    <tr>
      <td>GetDocumentationPart</td>
       <td style="text-align:right">✅</td>
    </tr>
    <tr>
      <td>GetDocumentationParts</td>
       <td style="text-align:right">✅</td>
    </tr>
    <tr>
      <td>GetDomainName <a href="#misc" title="covered by our integration test suite">✨</a></td>
       <td style="text-align:right">✅</td>
    </tr>
    <tr>
      <td>GetDomainNames <a href="#misc" title="covered by our integration test suite">✨</a></td>
       <td style="text-align:right">✅</td>
    </tr>
    <tr>
      <td>GetExport <a href="#misc" title="covered by our integration test suite">✨</a></td>
       <td style="text-align:right">✅</td>
    </tr>
    <tr>
      <td>GetGatewayResponse</td>
       <td style="text-align:right">✅</td>
    </tr>
    <tr>
      <td>GetGatewayResponses</td>
       <td style="text-align:right">✅</td>
    </tr>
    <tr>
      <td>GetIntegration <a href="#misc" title="covered by our integration test suite">✨</a></td>
       <td style="text-align:right">✅</td>
    </tr>
    <tr>
      <td>GetIntegrationResponse <a href="#misc" title="covered by our integration test suite">✨</a></td>
       <td style="text-align:right">✅</td>
    </tr>
    <tr>
      <td>GetMethod <a href="#misc" title="covered by our integration test suite">✨</a></td>
       <td style="text-align:right">✅</td>
    </tr>
    <tr>
      <td>GetMethodResponse <a href="#misc" title="covered by our integration test suite">✨</a></td>
       <td style="text-align:right">✅</td>
    </tr>
    <tr>
      <td>GetModel <a href="#misc" title="covered by our integration test suite">✨</a></td>
       <td style="text-align:right">✅</td>
    </tr>
    <tr>
      <td>GetModels <a href="#misc" title="covered by our integration test suite">✨</a></td>
       <td style="text-align:right">✅</td>
    </tr>
    <tr>
      <td>GetRequestValidator <a href="#misc" title="covered by our integration test suite">✨</a></td>
       <td style="text-align:right">✅</td>
    </tr>
    <tr>
      <td>GetRequestValidators <a href="#misc" title="covered by our integration test suite">✨</a></td>
       <td style="text-align:right">✅</td>
    </tr>
    <tr>
      <td>GetResource <a href="#misc" title="covered by our integration test suite">✨</a></td>
       <td style="text-align:right">✅</td>
    </tr>
    <tr>
      <td>GetResources <a href="#misc" title="covered by our integration test suite">✨</a></td>
       <td style="text-align:right">✅</td>
    </tr>
    <tr>
      <td>GetRestApi <a href="#misc" title="covered by our integration test suite">✨</a></td>
       <td style="text-align:right">✅</td>
    </tr>
    <tr>
      <td>GetRestApis <a href="#misc" title="covered by our integration test suite">✨</a></td>
       <td style="text-align:right">✅</td>
    </tr>
    <tr>
      <td>GetStage <a href="#misc" title="covered by our integration test suite">✨</a></td>
       <td style="text-align:right">✅</td>
    </tr>
    <tr>
      <td>GetStages</td>
       <td style="text-align:right">✅</td>
    </tr>
    <tr>
      <td>GetTags <a href="#misc" title="covered by our integration test suite">✨</a></td>
       <td style="text-align:right">✅</td>
    </tr>
    <tr>
      <td>GetUsagePlan</td>
       <td style="text-align:right">✅</td>
    </tr>
    <tr>
      <td>GetUsagePlanKey</td>
       <td style="text-align:right">✅</td>
    </tr>
    <tr>
      <td>GetUsagePlanKeys <a href="#misc" title="covered by our integration test suite">✨</a></td>
       <td style="text-align:right">✅</td>
    </tr>
    <tr>
      <td>GetUsagePlans <a href="#misc" title="covered by our integration test suite">✨</a></td>
       <td style="text-align:right">✅</td>
    </tr>
    <tr>
      <td>GetVpcLink</td>
       <td style="text-align:right">✅</td>
    </tr>
    <tr>
      <td>GetVpcLinks</td>
       <td style="text-align:right">✅</td>
    </tr>
    <tr>
      <td>ImportApiKeys</td>
       <td style="text-align:right">✅</td>
    </tr>
    <tr>
      <td>ImportRestApi <a href="#misc" title="covered by our integration test suite">✨</a></td>
       <td style="text-align:right">✅</td>
    </tr>
    <tr>
      <td>PutGatewayResponse</td>
       <td style="text-align:right">✅</td>
    </tr>
    <tr>
      <td>PutIntegration <a href="#misc" title="covered by our integration test suite">✨</a></td>
       <td style="text-align:right">✅</td>
    </tr>
    <tr>
      <td>PutIntegrationResponse <a href="#misc" title="covered by our integration test suite">✨</a></td>
       <td style="text-align:right">✅</td>
    </tr>
    <tr>
      <td>PutMethod <a href="#misc" title="covered by our integration test suite">✨</a></td>
       <td style="text-align:right">✅</td>
    </tr>
    <tr>
      <td>PutMethodResponse <a href="#misc" title="covered by our integration test suite">✨</a></td>
       <td style="text-align:right">✅</td>
    </tr>
    <tr>
      <td>PutRestApi <a href="#misc" title="covered by our integration test suite">✨</a></td>
       <td style="text-align:right">✅</td>
    </tr>
    <tr>
      <td>TagResource <a href="#misc" title="covered by our integration test suite">✨</a></td>
       <td style="text-align:right">✅</td>
    </tr>
    <tr>
      <td>TestInvokeAuthorizer</td>
       <td style="text-align:right">✅</td>
    </tr>
    <tr>
      <td>TestInvokeMethod <a href="#misc" title="covered by our integration test suite">✨</a></td>
       <td style="text-align:right">✅</td>
    </tr>
    <tr>
      <td>UntagResource</td>
       <td style="text-align:right">✅</td>
    </tr>
    <tr>
      <td>UpdateAccount <a href="#misc" title="covered by our integration test suite">✨</a></td>
       <td style="text-align:right">✅</td>
    </tr>
    <tr>
      <td>UpdateApiKey</td>
       <td style="text-align:right">✅</td>
    </tr>
    <tr>
      <td>UpdateAuthorizer <a href="#misc" title="covered by our integration test suite">✨</a></td>
       <td style="text-align:right">✅</td>
    </tr>
    <tr>
      <td>UpdateBasePathMapping <a href="#misc" title="covered by our integration test suite">✨</a></td>
       <td style="text-align:right">✅</td>
    </tr>
    <tr>
      <td>UpdateClientCertificate</td>
       <td style="text-align:right">✅</td>
    </tr>
    <tr>
      <td>UpdateDeployment <a href="#misc" title="covered by our integration test suite">✨</a></td>
       <td style="text-align:right">✅</td>
    </tr>
    <tr>
      <td>UpdateDocumentationPart</td>
       <td style="text-align:right">✅</td>
    </tr>
    <tr>
      <td>UpdateDomainName</td>
       <td style="text-align:right">✅</td>
    </tr>
    <tr>
      <td>UpdateGatewayResponse</td>
       <td style="text-align:right">✅</td>
    </tr>
    <tr>
      <td>UpdateIntegration</td>
       <td style="text-align:right">✅</td>
    </tr>
    <tr>
      <td>UpdateIntegrationResponse</td>
       <td style="text-align:right">✅</td>
    </tr>
    <tr>
      <td>UpdateMethod <a href="#misc" title="covered by our integration test suite">✨</a></td>
       <td style="text-align:right">✅</td>
    </tr>
    <tr>
      <td>UpdateMethodResponse</td>
       <td style="text-align:right">✅</td>
    </tr>
    <tr>
      <td>UpdateModel</td>
       <td style="text-align:right">✅</td>
    </tr>
    <tr>
      <td>UpdateRequestValidator <a href="#misc" title="covered by our integration test suite">✨</a></td>
       <td style="text-align:right">✅</td>
    </tr>
    <tr>
      <td>UpdateResource <a href="#misc" title="covered by our integration test suite">✨</a></td>
       <td style="text-align:right">✅</td>
    </tr>
    <tr>
      <td>UpdateRestApi <a href="#misc" title="covered by our integration test suite">✨</a></td>
       <td style="text-align:right">✅</td>
    </tr>
    <tr>
      <td>UpdateStage</td>
       <td style="text-align:right">✅</td>
    </tr>
    <tr>
      <td>UpdateUsagePlan</td>
       <td style="text-align:right">✅</td>
    </tr>
    <tr>
      <td>UpdateVpcLink</td>
       <td style="text-align:right">✅</td>
    </tr>
  </tbody>
  <tbody>    <tr>
      <td><a data-toggle="collapse" href=".apigateway-notimplemented">Show missing</a></td>
      <td style="text-align:right"></td>
    </tr>
  </tbody>
  <tbody class="collapse apigateway-notimplemented">     <tr>
      <td>CreateDocumentationVersion</td>
       <td style="text-align:right">-</td>
    </tr>
    <tr>
      <td>DeleteDocumentationVersion</td>
       <td style="text-align:right">-</td>
    </tr>
    <tr>
      <td>FlushStageAuthorizersCache</td>
       <td style="text-align:right">-</td>
    </tr>
    <tr>
      <td>FlushStageCache</td>
       <td style="text-align:right">-</td>
    </tr>
    <tr>
      <td>GetDocumentationVersion</td>
       <td style="text-align:right">-</td>
    </tr>
    <tr>
      <td>GetDocumentationVersions</td>
       <td style="text-align:right">-</td>
    </tr>
    <tr>
      <td>GetModelTemplate</td>
       <td style="text-align:right">-</td>
    </tr>
    <tr>
      <td>GetSdk</td>
       <td style="text-align:right">-</td>
    </tr>
    <tr>
      <td>GetSdkType</td>
       <td style="text-align:right">-</td>
    </tr>
    <tr>
      <td>GetSdkTypes</td>
       <td style="text-align:right">-</td>
    </tr>
    <tr>
      <td>GetUsage</td>
       <td style="text-align:right">-</td>
    </tr>
    <tr>
      <td>ImportDocumentationParts</td>
       <td style="text-align:right">-</td>
    </tr>
    <tr>
      <td>UpdateDocumentationVersion</td>
       <td style="text-align:right">-</td>
    </tr>
    <tr>
      <td>UpdateUsage</td>
       <td style="text-align:right">-</td>
    </tr>
  </tbody>
 </table>


## apigatewaymanagementapi ##

<table>
  <thead>
    <tr>
      <th>Operation</th>
      <th style="text-align:right">Implemented</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td>DeleteConnection (Pro) </td>
       <td style="text-align:right">✅</td>
    </tr>
    <tr>
      <td>GetConnection (Pro) </td>
       <td style="text-align:right">✅</td>
    </tr>
    <tr>
      <td>PostToConnection (Pro)  <a href="#misc" title="covered by our integration test suite">✨</a></td>
       <td style="text-align:right">✅</td>
    </tr>
  </tbody>
 </table>


## apigatewayv2 ##

<table>
  <thead>
    <tr>
      <th>Operation</th>
      <th style="text-align:right">Implemented</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td>CreateApi (Pro)  <a href="#misc" title="covered by our integration test suite">✨</a></td>
       <td style="text-align:right">✅</td>
    </tr>
    <tr>
      <td>CreateApiMapping (Pro)  <a href="#misc" title="covered by our integration test suite">✨</a></td>
       <td style="text-align:right">✅</td>
    </tr>
    <tr>
      <td>CreateAuthorizer (Pro)  <a href="#misc" title="covered by our integration test suite">✨</a></td>
       <td style="text-align:right">✅</td>
    </tr>
    <tr>
      <td>CreateDeployment (Pro)  <a href="#misc" title="covered by our integration test suite">✨</a></td>
       <td style="text-align:right">✅</td>
    </tr>
    <tr>
      <td>CreateDomainName (Pro)  <a href="#misc" title="covered by our integration test suite">✨</a></td>
       <td style="text-align:right">✅</td>
    </tr>
    <tr>
      <td>CreateIntegration (Pro)  <a href="#misc" title="covered by our integration test suite">✨</a></td>
       <td style="text-align:right">✅</td>
    </tr>
    <tr>
      <td>CreateIntegrationResponse (Pro)  <a href="#misc" title="covered by our integration test suite">✨</a></td>
       <td style="text-align:right">✅</td>
    </tr>
    <tr>
      <td>CreateModel (Pro)  <a href="#misc" title="covered by our integration test suite">✨</a></td>
       <td style="text-align:right">✅</td>
    </tr>
    <tr>
      <td>CreateRoute (Pro)  <a href="#misc" title="covered by our integration test suite">✨</a></td>
       <td style="text-align:right">✅</td>
    </tr>
    <tr>
      <td>CreateRouteResponse (Pro)  <a href="#misc" title="covered by our integration test suite">✨</a></td>
       <td style="text-align:right">✅</td>
    </tr>
    <tr>
      <td>CreateStage (Pro)  <a href="#misc" title="covered by our integration test suite">✨</a></td>
       <td style="text-align:right">✅</td>
    </tr>
    <tr>
      <td>CreateVpcLink (Pro)  <a href="#misc" title="covered by our integration test suite">✨</a></td>
       <td style="text-align:right">✅</td>
    </tr>
    <tr>
      <td>DeleteApi (Pro)  <a href="#misc" title="covered by our integration test suite">✨</a></td>
       <td style="text-align:right">✅</td>
    </tr>
    <tr>
      <td>DeleteApiMapping (Pro) </td>
       <td style="text-align:right">✅</td>
    </tr>
    <tr>
      <td>DeleteAuthorizer (Pro)  <a href="#misc" title="covered by our integration test suite">✨</a></td>
       <td style="text-align:right">✅</td>
    </tr>
    <tr>
      <td>DeleteCorsConfiguration (Pro) </td>
       <td style="text-align:right">✅</td>
    </tr>
    <tr>
      <td>DeleteDeployment (Pro)  <a href="#misc" title="covered by our integration test suite">✨</a></td>
       <td style="text-align:right">✅</td>
    </tr>
    <tr>
      <td>DeleteDomainName (Pro)  <a href="#misc" title="covered by our integration test suite">✨</a></td>
       <td style="text-align:right">✅</td>
    </tr>
    <tr>
      <td>DeleteIntegration (Pro)  <a href="#misc" title="covered by our integration test suite">✨</a></td>
       <td style="text-align:right">✅</td>
    </tr>
    <tr>
      <td>DeleteIntegrationResponse (Pro)  <a href="#misc" title="covered by our integration test suite">✨</a></td>
       <td style="text-align:right">✅</td>
    </tr>
    <tr>
      <td>DeleteModel (Pro) </td>
       <td style="text-align:right">✅</td>
    </tr>
    <tr>
      <td>DeleteRoute (Pro)  <a href="#misc" title="covered by our integration test suite">✨</a></td>
       <td style="text-align:right">✅</td>
    </tr>
    <tr>
      <td>DeleteRouteResponse (Pro)  <a href="#misc" title="covered by our integration test suite">✨</a></td>
       <td style="text-align:right">✅</td>
    </tr>
    <tr>
      <td>DeleteStage (Pro)  <a href="#misc" title="covered by our integration test suite">✨</a></td>
       <td style="text-align:right">✅</td>
    </tr>
    <tr>
      <td>DeleteVpcLink (Pro)  <a href="#misc" title="covered by our integration test suite">✨</a></td>
       <td style="text-align:right">✅</td>
    </tr>
    <tr>
      <td>GetApi (Pro)  <a href="#misc" title="covered by our integration test suite">✨</a></td>
       <td style="text-align:right">✅</td>
    </tr>
    <tr>
      <td>GetApiMapping (Pro) </td>
       <td style="text-align:right">✅</td>
    </tr>
    <tr>
      <td>GetApiMappings (Pro) </td>
       <td style="text-align:right">✅</td>
    </tr>
    <tr>
      <td>GetApis (Pro)  <a href="#misc" title="covered by our integration test suite">✨</a></td>
       <td style="text-align:right">✅</td>
    </tr>
    <tr>
      <td>GetAuthorizer (Pro)  <a href="#misc" title="covered by our integration test suite">✨</a></td>
       <td style="text-align:right">✅</td>
    </tr>
    <tr>
      <td>GetAuthorizers (Pro)  <a href="#misc" title="covered by our integration test suite">✨</a></td>
       <td style="text-align:right">✅</td>
    </tr>
    <tr>
      <td>GetDeployment (Pro)  <a href="#misc" title="covered by our integration test suite">✨</a></td>
       <td style="text-align:right">✅</td>
    </tr>
    <tr>
      <td>GetDeployments (Pro)  <a href="#misc" title="covered by our integration test suite">✨</a></td>
       <td style="text-align:right">✅</td>
    </tr>
    <tr>
      <td>GetDomainName (Pro)  <a href="#misc" title="covered by our integration test suite">✨</a></td>
       <td style="text-align:right">✅</td>
    </tr>
    <tr>
      <td>GetDomainNames (Pro)  <a href="#misc" title="covered by our integration test suite">✨</a></td>
       <td style="text-align:right">✅</td>
    </tr>
    <tr>
      <td>GetIntegration (Pro)  <a href="#misc" title="covered by our integration test suite">✨</a></td>
       <td style="text-align:right">✅</td>
    </tr>
    <tr>
      <td>GetIntegrationResponse (Pro)  <a href="#misc" title="covered by our integration test suite">✨</a></td>
       <td style="text-align:right">✅</td>
    </tr>
    <tr>
      <td>GetIntegrationResponses (Pro)  <a href="#misc" title="covered by our integration test suite">✨</a></td>
       <td style="text-align:right">✅</td>
    </tr>
    <tr>
      <td>GetIntegrations (Pro)  <a href="#misc" title="covered by our integration test suite">✨</a></td>
       <td style="text-align:right">✅</td>
    </tr>
    <tr>
      <td>GetModel (Pro) </td>
       <td style="text-align:right">✅</td>
    </tr>
    <tr>
      <td>GetModels (Pro)  <a href="#misc" title="covered by our integration test suite">✨</a></td>
       <td style="text-align:right">✅</td>
    </tr>
    <tr>
      <td>GetRoute (Pro)  <a href="#misc" title="covered by our integration test suite">✨</a></td>
       <td style="text-align:right">✅</td>
    </tr>
    <tr>
      <td>GetRouteResponse (Pro)  <a href="#misc" title="covered by our integration test suite">✨</a></td>
       <td style="text-align:right">✅</td>
    </tr>
    <tr>
      <td>GetRouteResponses (Pro)  <a href="#misc" title="covered by our integration test suite">✨</a></td>
       <td style="text-align:right">✅</td>
    </tr>
    <tr>
      <td>GetRoutes (Pro)  <a href="#misc" title="covered by our integration test suite">✨</a></td>
       <td style="text-align:right">✅</td>
    </tr>
    <tr>
      <td>GetStage (Pro)  <a href="#misc" title="covered by our integration test suite">✨</a></td>
       <td style="text-align:right">✅</td>
    </tr>
    <tr>
      <td>GetStages (Pro) </td>
       <td style="text-align:right">✅</td>
    </tr>
    <tr>
      <td>GetTags (Pro) </td>
       <td style="text-align:right">✅</td>
    </tr>
    <tr>
      <td>GetVpcLink (Pro) </td>
       <td style="text-align:right">✅</td>
    </tr>
    <tr>
      <td>GetVpcLinks (Pro)  <a href="#misc" title="covered by our integration test suite">✨</a></td>
       <td style="text-align:right">✅</td>
    </tr>
    <tr>
      <td>ImportApi (Pro)  <a href="#misc" title="covered by our integration test suite">✨</a></td>
       <td style="text-align:right">✅</td>
    </tr>
    <tr>
      <td>ReimportApi (Pro)  <a href="#misc" title="covered by our integration test suite">✨</a></td>
       <td style="text-align:right">✅</td>
    </tr>
    <tr>
      <td>TagResource (Pro) </td>
       <td style="text-align:right">✅</td>
    </tr>
    <tr>
      <td>UntagResource (Pro) </td>
       <td style="text-align:right">✅</td>
    </tr>
    <tr>
      <td>UpdateApi (Pro) </td>
       <td style="text-align:right">✅</td>
    </tr>
    <tr>
      <td>UpdateApiMapping (Pro) </td>
       <td style="text-align:right">✅</td>
    </tr>
    <tr>
      <td>UpdateAuthorizer (Pro) </td>
       <td style="text-align:right">✅</td>
    </tr>
    <tr>
      <td>UpdateDeployment (Pro) </td>
       <td style="text-align:right">✅</td>
    </tr>
    <tr>
      <td>UpdateDomainName (Pro) </td>
       <td style="text-align:right">✅</td>
    </tr>
    <tr>
      <td>UpdateIntegration (Pro)  <a href="#misc" title="covered by our integration test suite">✨</a></td>
       <td style="text-align:right">✅</td>
    </tr>
    <tr>
      <td>UpdateIntegrationResponse (Pro)  <a href="#misc" title="covered by our integration test suite">✨</a></td>
       <td style="text-align:right">✅</td>
    </tr>
    <tr>
      <td>UpdateModel (Pro) </td>
       <td style="text-align:right">✅</td>
    </tr>
    <tr>
      <td>UpdateRoute (Pro)  <a href="#misc" title="covered by our integration test suite">✨</a></td>
       <td style="text-align:right">✅</td>
    </tr>
    <tr>
      <td>UpdateRouteResponse (Pro)  <a href="#misc" title="covered by our integration test suite">✨</a></td>
       <td style="text-align:right">✅</td>
    </tr>
    <tr>
      <td>UpdateStage (Pro)  <a href="#misc" title="covered by our integration test suite">✨</a></td>
       <td style="text-align:right">✅</td>
    </tr>
    <tr>
      <td>UpdateVpcLink (Pro) </td>
       <td style="text-align:right">✅</td>
    </tr>
  </tbody>
  <tbody>    <tr>
      <td><a data-toggle="collapse" href=".apigatewayv2-notimplemented">Show missing</a></td>
      <td style="text-align:right"></td>
    </tr>
  </tbody>
  <tbody class="collapse apigatewayv2-notimplemented">     <tr>
      <td>DeleteAccessLogSettings</td>
       <td style="text-align:right">-</td>
    </tr>
    <tr>
      <td>DeleteRouteRequestParameter</td>
       <td style="text-align:right">-</td>
    </tr>
    <tr>
      <td>DeleteRouteSettings</td>
       <td style="text-align:right">-</td>
    </tr>
    <tr>
      <td>ExportApi</td>
       <td style="text-align:right">-</td>
    </tr>
    <tr>
      <td>GetModelTemplate</td>
       <td style="text-align:right">-</td>
    </tr>
    <tr>
      <td>ResetAuthorizersCache</td>
       <td style="text-align:right">-</td>
    </tr>
  </tbody>
 </table>


## appconfig ##

<table>
  <thead>
    <tr>
      <th>Operation</th>
      <th style="text-align:right">Implemented</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td>CreateApplication (Pro)  <a href="#misc" title="covered by our integration test suite">✨</a></td>
       <td style="text-align:right">✅</td>
    </tr>
    <tr>
      <td>CreateConfigurationProfile (Pro)  <a href="#misc" title="covered by our integration test suite">✨</a></td>
       <td style="text-align:right">✅</td>
    </tr>
    <tr>
      <td>CreateDeploymentStrategy (Pro)  <a href="#misc" title="covered by our integration test suite">✨</a></td>
       <td style="text-align:right">✅</td>
    </tr>
    <tr>
      <td>CreateEnvironment (Pro)  <a href="#misc" title="covered by our integration test suite">✨</a></td>
       <td style="text-align:right">✅</td>
    </tr>
    <tr>
      <td>CreateHostedConfigurationVersion (Pro)  <a href="#misc" title="covered by our integration test suite">✨</a></td>
       <td style="text-align:right">✅</td>
    </tr>
    <tr>
      <td>DeleteApplication (Pro)  <a href="#misc" title="covered by our integration test suite">✨</a></td>
       <td style="text-align:right">✅</td>
    </tr>
    <tr>
      <td>DeleteConfigurationProfile (Pro)  <a href="#misc" title="covered by our integration test suite">✨</a></td>
       <td style="text-align:right">✅</td>
    </tr>
    <tr>
      <td>DeleteDeploymentStrategy (Pro)  <a href="#misc" title="covered by our integration test suite">✨</a></td>
       <td style="text-align:right">✅</td>
    </tr>
    <tr>
      <td>DeleteEnvironment (Pro)  <a href="#misc" title="covered by our integration test suite">✨</a></td>
       <td style="text-align:right">✅</td>
    </tr>
    <tr>
      <td>DeleteHostedConfigurationVersion (Pro)  <a href="#misc" title="covered by our integration test suite">✨</a></td>
       <td style="text-align:right">✅</td>
    </tr>
    <tr>
      <td>GetApplication (Pro)  <a href="#misc" title="covered by our integration test suite">✨</a></td>
       <td style="text-align:right">✅</td>
    </tr>
    <tr>
      <td>GetConfiguration (Pro)  <a href="#misc" title="covered by our integration test suite">✨</a></td>
       <td style="text-align:right">✅</td>
    </tr>
    <tr>
      <td>GetConfigurationProfile (Pro)  <a href="#misc" title="covered by our integration test suite">✨</a></td>
       <td style="text-align:right">✅</td>
    </tr>
    <tr>
      <td>GetDeployment (Pro) </td>
       <td style="text-align:right">✅</td>
    </tr>
    <tr>
      <td>GetDeploymentStrategy (Pro)  <a href="#misc" title="covered by our integration test suite">✨</a></td>
       <td style="text-align:right">✅</td>
    </tr>
    <tr>
      <td>GetEnvironment (Pro)  <a href="#misc" title="covered by our integration test suite">✨</a></td>
       <td style="text-align:right">✅</td>
    </tr>
    <tr>
      <td>GetHostedConfigurationVersion (Pro)  <a href="#misc" title="covered by our integration test suite">✨</a></td>
       <td style="text-align:right">✅</td>
    </tr>
    <tr>
      <td>ListApplications (Pro)  <a href="#misc" title="covered by our integration test suite">✨</a></td>
       <td style="text-align:right">✅</td>
    </tr>
    <tr>
      <td>ListConfigurationProfiles (Pro)  <a href="#misc" title="covered by our integration test suite">✨</a></td>
       <td style="text-align:right">✅</td>
    </tr>
    <tr>
      <td>ListDeploymentStrategies (Pro)  <a href="#misc" title="covered by our integration test suite">✨</a></td>
       <td style="text-align:right">✅</td>
    </tr>
    <tr>
      <td>ListDeployments (Pro)  <a href="#misc" title="covered by our integration test suite">✨</a></td>
       <td style="text-align:right">✅</td>
    </tr>
    <tr>
      <td>ListEnvironments (Pro)  <a href="#misc" title="covered by our integration test suite">✨</a></td>
       <td style="text-align:right">✅</td>
    </tr>
    <tr>
      <td>ListHostedConfigurationVersions (Pro)  <a href="#misc" title="covered by our integration test suite">✨</a></td>
       <td style="text-align:right">✅</td>
    </tr>
    <tr>
      <td>ListTagsForResource (Pro) </td>
       <td style="text-align:right">✅</td>
    </tr>
    <tr>
      <td>StartDeployment (Pro)  <a href="#misc" title="covered by our integration test suite">✨</a></td>
       <td style="text-align:right">✅</td>
    </tr>
    <tr>
      <td>StopDeployment (Pro) </td>
       <td style="text-align:right">✅</td>
    </tr>
    <tr>
      <td>TagResource (Pro) </td>
       <td style="text-align:right">✅</td>
    </tr>
    <tr>
      <td>UntagResource (Pro) </td>
       <td style="text-align:right">✅</td>
    </tr>
    <tr>
      <td>UpdateApplication (Pro)  <a href="#misc" title="covered by our integration test suite">✨</a></td>
       <td style="text-align:right">✅</td>
    </tr>
    <tr>
      <td>UpdateConfigurationProfile (Pro)  <a href="#misc" title="covered by our integration test suite">✨</a></td>
       <td style="text-align:right">✅</td>
    </tr>
    <tr>
      <td>UpdateDeploymentStrategy (Pro)  <a href="#misc" title="covered by our integration test suite">✨</a></td>
       <td style="text-align:right">✅</td>
    </tr>
    <tr>
      <td>UpdateEnvironment (Pro)  <a href="#misc" title="covered by our integration test suite">✨</a></td>
       <td style="text-align:right">✅</td>
    </tr>
    <tr>
      <td>ValidateConfiguration (Pro)  <a href="#misc" title="covered by our integration test suite">✨</a></td>
       <td style="text-align:right">✅</td>
    </tr>
  </tbody>
  <tbody>    <tr>
      <td><a data-toggle="collapse" href=".appconfig-notimplemented">Show missing</a></td>
      <td style="text-align:right"></td>
    </tr>
  </tbody>
  <tbody class="collapse appconfig-notimplemented">     <tr>
      <td>CreateExtension</td>
       <td style="text-align:right">-</td>
    </tr>
    <tr>
      <td>CreateExtensionAssociation</td>
       <td style="text-align:right">-</td>
    </tr>
    <tr>
      <td>DeleteExtension</td>
       <td style="text-align:right">-</td>
    </tr>
    <tr>
      <td>DeleteExtensionAssociation</td>
       <td style="text-align:right">-</td>
    </tr>
    <tr>
      <td>GetExtension</td>
       <td style="text-align:right">-</td>
    </tr>
    <tr>
      <td>GetExtensionAssociation</td>
       <td style="text-align:right">-</td>
    </tr>
    <tr>
      <td>ListExtensionAssociations</td>
       <td style="text-align:right">-</td>
    </tr>
    <tr>
      <td>ListExtensions</td>
       <td style="text-align:right">-</td>
    </tr>
    <tr>
      <td>UpdateExtension</td>
       <td style="text-align:right">-</td>
    </tr>
    <tr>
      <td>UpdateExtensionAssociation</td>
       <td style="text-align:right">-</td>
    </tr>
  </tbody>
 </table>


## application-autoscaling ##

<table>
  <thead>
    <tr>
      <th>Operation</th>
      <th style="text-align:right">Implemented</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td>DeleteScalingPolicy (Pro)  <a href="#misc" title="covered by our integration test suite">✨</a></td>
       <td style="text-align:right">✅</td>
    </tr>
    <tr>
      <td>DeleteScheduledAction (Pro) </td>
       <td style="text-align:right">✅</td>
    </tr>
    <tr>
      <td>DeregisterScalableTarget (Pro)  <a href="#misc" title="covered by our integration test suite">✨</a></td>
       <td style="text-align:right">✅</td>
    </tr>
    <tr>
      <td>DescribeScalableTargets (Pro)  <a href="#misc" title="covered by our integration test suite">✨</a></td>
       <td style="text-align:right">✅</td>
    </tr>
    <tr>
      <td>DescribeScalingPolicies (Pro)  <a href="#misc" title="covered by our integration test suite">✨</a></td>
       <td style="text-align:right">✅</td>
    </tr>
    <tr>
      <td>DescribeScheduledActions (Pro) </td>
       <td style="text-align:right">✅</td>
    </tr>
    <tr>
      <td>PutScalingPolicy (Pro)  <a href="#misc" title="covered by our integration test suite">✨</a></td>
       <td style="text-align:right">✅</td>
    </tr>
    <tr>
      <td>PutScheduledAction (Pro) </td>
       <td style="text-align:right">✅</td>
    </tr>
    <tr>
      <td>RegisterScalableTarget (Pro)  <a href="#misc" title="covered by our integration test suite">✨</a></td>
       <td style="text-align:right">✅</td>
    </tr>
  </tbody>
  <tbody>    <tr>
      <td><a data-toggle="collapse" href=".application-autoscaling-notimplemented">Show missing</a></td>
      <td style="text-align:right"></td>
    </tr>
  </tbody>
  <tbody class="collapse application-autoscaling-notimplemented">     <tr>
      <td>DescribeScalingActivities</td>
       <td style="text-align:right">-</td>
    </tr>
  </tbody>
 </table>


## appsync ##

<table>
  <thead>
    <tr>
      <th>Operation</th>
      <th style="text-align:right">Implemented</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td>AssociateApi (Pro)  <a href="#misc" title="covered by our integration test suite">✨</a></td>
       <td style="text-align:right">✅</td>
    </tr>
    <tr>
      <td>CreateApiCache (Pro)  <a href="#misc" title="covered by our integration test suite">✨</a></td>
       <td style="text-align:right">✅</td>
    </tr>
    <tr>
      <td>CreateApiKey (Pro)  <a href="#misc" title="covered by our integration test suite">✨</a></td>
       <td style="text-align:right">✅</td>
    </tr>
    <tr>
      <td>CreateDataSource (Pro)  <a href="#misc" title="covered by our integration test suite">✨</a></td>
       <td style="text-align:right">✅</td>
    </tr>
    <tr>
      <td>CreateDomainName (Pro)  <a href="#misc" title="covered by our integration test suite">✨</a></td>
       <td style="text-align:right">✅</td>
    </tr>
    <tr>
      <td>CreateFunction (Pro)  <a href="#misc" title="covered by our integration test suite">✨</a></td>
       <td style="text-align:right">✅</td>
    </tr>
    <tr>
      <td>CreateGraphqlApi (Pro)  <a href="#misc" title="covered by our integration test suite">✨</a></td>
       <td style="text-align:right">✅</td>
    </tr>
    <tr>
      <td>CreateResolver (Pro)  <a href="#misc" title="covered by our integration test suite">✨</a></td>
       <td style="text-align:right">✅</td>
    </tr>
    <tr>
      <td>CreateType (Pro) </td>
       <td style="text-align:right">✅</td>
    </tr>
    <tr>
      <td>DeleteApiCache (Pro) </td>
       <td style="text-align:right">✅</td>
    </tr>
    <tr>
      <td>DeleteApiKey (Pro) </td>
       <td style="text-align:right">✅</td>
    </tr>
    <tr>
      <td>DeleteDataSource (Pro)  <a href="#misc" title="covered by our integration test suite">✨</a></td>
       <td style="text-align:right">✅</td>
    </tr>
    <tr>
      <td>DeleteDomainName (Pro)  <a href="#misc" title="covered by our integration test suite">✨</a></td>
       <td style="text-align:right">✅</td>
    </tr>
    <tr>
      <td>DeleteFunction (Pro) </td>
       <td style="text-align:right">✅</td>
    </tr>
    <tr>
      <td>DeleteGraphqlApi (Pro)  <a href="#misc" title="covered by our integration test suite">✨</a></td>
       <td style="text-align:right">✅</td>
    </tr>
    <tr>
      <td>DeleteResolver (Pro)  <a href="#misc" title="covered by our integration test suite">✨</a></td>
       <td style="text-align:right">✅</td>
    </tr>
    <tr>
      <td>DeleteType (Pro) </td>
       <td style="text-align:right">✅</td>
    </tr>
    <tr>
      <td>DisassociateApi (Pro)  <a href="#misc" title="covered by our integration test suite">✨</a></td>
       <td style="text-align:right">✅</td>
    </tr>
    <tr>
      <td>FlushApiCache (Pro) </td>
       <td style="text-align:right">✅</td>
    </tr>
    <tr>
      <td>GetApiAssociation (Pro)  <a href="#misc" title="covered by our integration test suite">✨</a></td>
       <td style="text-align:right">✅</td>
    </tr>
    <tr>
      <td>GetApiCache (Pro) </td>
       <td style="text-align:right">✅</td>
    </tr>
    <tr>
      <td>GetDataSource (Pro) </td>
       <td style="text-align:right">✅</td>
    </tr>
    <tr>
      <td>GetDomainName (Pro) </td>
       <td style="text-align:right">✅</td>
    </tr>
    <tr>
      <td>GetFunction (Pro)  <a href="#misc" title="covered by our integration test suite">✨</a></td>
       <td style="text-align:right">✅</td>
    </tr>
    <tr>
      <td>GetGraphqlApi (Pro)  <a href="#misc" title="covered by our integration test suite">✨</a></td>
       <td style="text-align:right">✅</td>
    </tr>
    <tr>
      <td>GetIntrospectionSchema (Pro)  <a href="#misc" title="covered by our integration test suite">✨</a></td>
       <td style="text-align:right">✅</td>
    </tr>
    <tr>
      <td>GetResolver (Pro)  <a href="#misc" title="covered by our integration test suite">✨</a></td>
       <td style="text-align:right">✅</td>
    </tr>
    <tr>
      <td>GetSchemaCreationStatus (Pro)  <a href="#misc" title="covered by our integration test suite">✨</a></td>
       <td style="text-align:right">✅</td>
    </tr>
    <tr>
      <td>GetType (Pro)  <a href="#misc" title="covered by our integration test suite">✨</a></td>
       <td style="text-align:right">✅</td>
    </tr>
    <tr>
      <td>ListApiKeys (Pro)  <a href="#misc" title="covered by our integration test suite">✨</a></td>
       <td style="text-align:right">✅</td>
    </tr>
    <tr>
      <td>ListDataSources (Pro)  <a href="#misc" title="covered by our integration test suite">✨</a></td>
       <td style="text-align:right">✅</td>
    </tr>
    <tr>
      <td>ListDomainNames (Pro)  <a href="#misc" title="covered by our integration test suite">✨</a></td>
       <td style="text-align:right">✅</td>
    </tr>
    <tr>
      <td>ListFunctions (Pro)  <a href="#misc" title="covered by our integration test suite">✨</a></td>
       <td style="text-align:right">✅</td>
    </tr>
    <tr>
      <td>ListGraphqlApis (Pro)  <a href="#misc" title="covered by our integration test suite">✨</a></td>
       <td style="text-align:right">✅</td>
    </tr>
    <tr>
      <td>ListResolvers (Pro)  <a href="#misc" title="covered by our integration test suite">✨</a></td>
       <td style="text-align:right">✅</td>
    </tr>
    <tr>
      <td>ListResolversByFunction (Pro) </td>
       <td style="text-align:right">✅</td>
    </tr>
    <tr>
      <td>ListTagsForResource (Pro)  <a href="#misc" title="covered by our integration test suite">✨</a></td>
       <td style="text-align:right">✅</td>
    </tr>
    <tr>
      <td>ListTypes (Pro) </td>
       <td style="text-align:right">✅</td>
    </tr>
    <tr>
      <td>StartSchemaCreation (Pro)  <a href="#misc" title="covered by our integration test suite">✨</a></td>
       <td style="text-align:right">✅</td>
    </tr>
    <tr>
      <td>TagResource (Pro)  <a href="#misc" title="covered by our integration test suite">✨</a></td>
       <td style="text-align:right">✅</td>
    </tr>
    <tr>
      <td>UntagResource (Pro) </td>
       <td style="text-align:right">✅</td>
    </tr>
    <tr>
      <td>UpdateApiCache (Pro)  <a href="#misc" title="covered by our integration test suite">✨</a></td>
       <td style="text-align:right">✅</td>
    </tr>
    <tr>
      <td>UpdateApiKey (Pro)  <a href="#misc" title="covered by our integration test suite">✨</a></td>
       <td style="text-align:right">✅</td>
    </tr>
    <tr>
      <td>UpdateDataSource (Pro) </td>
       <td style="text-align:right">✅</td>
    </tr>
    <tr>
      <td>UpdateDomainName (Pro) </td>
       <td style="text-align:right">✅</td>
    </tr>
    <tr>
      <td>UpdateFunction (Pro) </td>
       <td style="text-align:right">✅</td>
    </tr>
    <tr>
      <td>UpdateGraphqlApi (Pro) </td>
       <td style="text-align:right">✅</td>
    </tr>
    <tr>
      <td>UpdateResolver (Pro)  <a href="#misc" title="covered by our integration test suite">✨</a></td>
       <td style="text-align:right">✅</td>
    </tr>
    <tr>
      <td>UpdateType (Pro) </td>
       <td style="text-align:right">✅</td>
    </tr>
  </tbody>
  <tbody>    <tr>
      <td><a data-toggle="collapse" href=".appsync-notimplemented">Show missing</a></td>
      <td style="text-align:right"></td>
    </tr>
  </tbody>
  <tbody class="collapse appsync-notimplemented">     <tr>
      <td>EvaluateMappingTemplate</td>
       <td style="text-align:right">-</td>
    </tr>
  </tbody>
 </table>


## athena ##

<table>
  <thead>
    <tr>
      <th>Operation</th>
      <th style="text-align:right">Implemented</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td>CreateDataCatalog (Pro)  <a href="#misc" title="covered by our integration test suite">✨</a></td>
       <td style="text-align:right">✅</td>
    </tr>
    <tr>
      <td>CreateNamedQuery (Pro)  <a href="#misc" title="covered by our integration test suite">✨</a></td>
       <td style="text-align:right">✅</td>
    </tr>
    <tr>
      <td>CreateWorkGroup (Pro)  <a href="#misc" title="covered by our integration test suite">✨</a></td>
       <td style="text-align:right">✅</td>
    </tr>
    <tr>
      <td>DeleteDataCatalog (Pro)  <a href="#misc" title="covered by our integration test suite">✨</a></td>
       <td style="text-align:right">✅</td>
    </tr>
    <tr>
      <td>DeleteNamedQuery (Pro)  <a href="#misc" title="covered by our integration test suite">✨</a></td>
       <td style="text-align:right">✅</td>
    </tr>
    <tr>
      <td>DeleteWorkGroup (Pro)  <a href="#misc" title="covered by our integration test suite">✨</a></td>
       <td style="text-align:right">✅</td>
    </tr>
    <tr>
      <td>GetDataCatalog (Pro)  <a href="#misc" title="covered by our integration test suite">✨</a></td>
       <td style="text-align:right">✅</td>
    </tr>
    <tr>
      <td>GetDatabase (Pro) </td>
       <td style="text-align:right">✅</td>
    </tr>
    <tr>
      <td>GetNamedQuery (Pro)  <a href="#misc" title="covered by our integration test suite">✨</a></td>
       <td style="text-align:right">✅</td>
    </tr>
    <tr>
      <td>GetQueryExecution (Pro) </td>
       <td style="text-align:right">✅</td>
    </tr>
    <tr>
      <td>GetQueryResults (Pro) </td>
       <td style="text-align:right">✅</td>
    </tr>
    <tr>
      <td>GetWorkGroup (Pro)  <a href="#misc" title="covered by our integration test suite">✨</a></td>
       <td style="text-align:right">✅</td>
    </tr>
    <tr>
      <td>ListDataCatalogs (Pro)  <a href="#misc" title="covered by our integration test suite">✨</a></td>
       <td style="text-align:right">✅</td>
    </tr>
    <tr>
      <td>ListDatabases (Pro) </td>
       <td style="text-align:right">✅</td>
    </tr>
    <tr>
      <td>ListNamedQueries (Pro)  <a href="#misc" title="covered by our integration test suite">✨</a></td>
       <td style="text-align:right">✅</td>
    </tr>
    <tr>
      <td>ListQueryExecutions (Pro) </td>
       <td style="text-align:right">✅</td>
    </tr>
    <tr>
      <td>ListTagsForResource (Pro)  <a href="#misc" title="covered by our integration test suite">✨</a></td>
       <td style="text-align:right">✅</td>
    </tr>
    <tr>
      <td>ListWorkGroups (Pro)  <a href="#misc" title="covered by our integration test suite">✨</a></td>
       <td style="text-align:right">✅</td>
    </tr>
    <tr>
      <td>StartQueryExecution (Pro) </td>
       <td style="text-align:right">✅</td>
    </tr>
    <tr>
      <td>TagResource (Pro)  <a href="#misc" title="covered by our integration test suite">✨</a></td>
       <td style="text-align:right">✅</td>
    </tr>
    <tr>
      <td>UntagResource (Pro)  <a href="#misc" title="covered by our integration test suite">✨</a></td>
       <td style="text-align:right">✅</td>
    </tr>
  </tbody>
  <tbody>    <tr>
      <td><a data-toggle="collapse" href=".athena-notimplemented">Show missing</a></td>
      <td style="text-align:right"></td>
    </tr>
  </tbody>
  <tbody class="collapse athena-notimplemented">     <tr>
      <td>BatchGetNamedQuery</td>
       <td style="text-align:right">-</td>
    </tr>
    <tr>
      <td>BatchGetPreparedStatement</td>
       <td style="text-align:right">-</td>
    </tr>
    <tr>
      <td>BatchGetQueryExecution</td>
       <td style="text-align:right">-</td>
    </tr>
    <tr>
      <td>CreatePreparedStatement</td>
       <td style="text-align:right">-</td>
    </tr>
    <tr>
      <td>DeletePreparedStatement</td>
       <td style="text-align:right">-</td>
    </tr>
    <tr>
      <td>GetPreparedStatement</td>
       <td style="text-align:right">-</td>
    </tr>
    <tr>
      <td>GetQueryRuntimeStatistics</td>
       <td style="text-align:right">-</td>
    </tr>
    <tr>
      <td>GetTableMetadata</td>
       <td style="text-align:right">-</td>
    </tr>
    <tr>
      <td>ListEngineVersions</td>
       <td style="text-align:right">-</td>
    </tr>
    <tr>
      <td>ListPreparedStatements</td>
       <td style="text-align:right">-</td>
    </tr>
    <tr>
      <td>ListTableMetadata</td>
       <td style="text-align:right">-</td>
    </tr>
    <tr>
      <td>StopQueryExecution</td>
       <td style="text-align:right">-</td>
    </tr>
    <tr>
      <td>UpdateDataCatalog</td>
       <td style="text-align:right">-</td>
    </tr>
    <tr>
      <td>UpdateNamedQuery</td>
       <td style="text-align:right">-</td>
    </tr>
    <tr>
      <td>UpdatePreparedStatement</td>
       <td style="text-align:right">-</td>
    </tr>
    <tr>
      <td>UpdateWorkGroup</td>
       <td style="text-align:right">-</td>
    </tr>
  </tbody>
 </table>


## autoscaling ##

<table>
  <thead>
    <tr>
      <th>Operation</th>
      <th style="text-align:right">Implemented</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td>AttachInstances (Pro) </td>
       <td style="text-align:right">✅</td>
    </tr>
    <tr>
      <td>AttachLoadBalancerTargetGroups (Pro) </td>
       <td style="text-align:right">✅</td>
    </tr>
    <tr>
      <td>AttachLoadBalancers (Pro) </td>
       <td style="text-align:right">✅</td>
    </tr>
    <tr>
      <td>CreateAutoScalingGroup (Pro)  <a href="#misc" title="covered by our integration test suite">✨</a></td>
       <td style="text-align:right">✅</td>
    </tr>
    <tr>
      <td>CreateLaunchConfiguration (Pro)  <a href="#misc" title="covered by our integration test suite">✨</a></td>
       <td style="text-align:right">✅</td>
    </tr>
    <tr>
      <td>CreateOrUpdateTags (Pro) </td>
       <td style="text-align:right">✅</td>
    </tr>
    <tr>
      <td>DeleteAutoScalingGroup (Pro)  <a href="#misc" title="covered by our integration test suite">✨</a></td>
       <td style="text-align:right">✅</td>
    </tr>
    <tr>
      <td>DeleteLaunchConfiguration (Pro)  <a href="#misc" title="covered by our integration test suite">✨</a></td>
       <td style="text-align:right">✅</td>
    </tr>
    <tr>
      <td>DeleteLifecycleHook (Pro) </td>
       <td style="text-align:right">✅</td>
    </tr>
    <tr>
      <td>DeletePolicy (Pro) </td>
       <td style="text-align:right">✅</td>
    </tr>
    <tr>
      <td>DeleteScheduledAction (Pro) </td>
       <td style="text-align:right">✅</td>
    </tr>
    <tr>
      <td>DeleteTags (Pro) </td>
       <td style="text-align:right">✅</td>
    </tr>
    <tr>
      <td>DescribeAutoScalingGroups (Pro) </td>
       <td style="text-align:right">✅</td>
    </tr>
    <tr>
      <td>DescribeAutoScalingInstances (Pro) </td>
       <td style="text-align:right">✅</td>
    </tr>
    <tr>
      <td>DescribeLaunchConfigurations (Pro) </td>
       <td style="text-align:right">✅</td>
    </tr>
    <tr>
      <td>DescribeLifecycleHooks (Pro) </td>
       <td style="text-align:right">✅</td>
    </tr>
    <tr>
      <td>DescribeLoadBalancerTargetGroups (Pro) </td>
       <td style="text-align:right">✅</td>
    </tr>
    <tr>
      <td>DescribeLoadBalancers (Pro) </td>
       <td style="text-align:right">✅</td>
    </tr>
    <tr>
      <td>DescribeMetricCollectionTypes (Pro)  <a href="#misc" title="covered by our integration test suite">✨</a></td>
       <td style="text-align:right">✅</td>
    </tr>
    <tr>
      <td>DescribePolicies (Pro) </td>
       <td style="text-align:right">✅</td>
    </tr>
    <tr>
      <td>DescribeScheduledActions (Pro) </td>
       <td style="text-align:right">✅</td>
    </tr>
    <tr>
      <td>DescribeTags (Pro) </td>
       <td style="text-align:right">✅</td>
    </tr>
    <tr>
      <td>DetachInstances (Pro) </td>
       <td style="text-align:right">✅</td>
    </tr>
    <tr>
      <td>DetachLoadBalancerTargetGroups (Pro) </td>
       <td style="text-align:right">✅</td>
    </tr>
    <tr>
      <td>DetachLoadBalancers (Pro) </td>
       <td style="text-align:right">✅</td>
    </tr>
    <tr>
      <td>DisableMetricsCollection (Pro)  <a href="#misc" title="covered by our integration test suite">✨</a></td>
       <td style="text-align:right">✅</td>
    </tr>
    <tr>
      <td>EnableMetricsCollection (Pro)  <a href="#misc" title="covered by our integration test suite">✨</a></td>
       <td style="text-align:right">✅</td>
    </tr>
    <tr>
      <td>EnterStandby (Pro) </td>
       <td style="text-align:right">✅</td>
    </tr>
    <tr>
      <td>ExecutePolicy (Pro) </td>
       <td style="text-align:right">✅</td>
    </tr>
    <tr>
      <td>ExitStandby (Pro) </td>
       <td style="text-align:right">✅</td>
    </tr>
    <tr>
      <td>PutLifecycleHook (Pro) </td>
       <td style="text-align:right">✅</td>
    </tr>
    <tr>
      <td>PutScalingPolicy (Pro) </td>
       <td style="text-align:right">✅</td>
    </tr>
    <tr>
      <td>PutScheduledUpdateGroupAction (Pro) </td>
       <td style="text-align:right">✅</td>
    </tr>
    <tr>
      <td>ResumeProcesses (Pro) </td>
       <td style="text-align:right">✅</td>
    </tr>
    <tr>
      <td>SetDesiredCapacity (Pro) </td>
       <td style="text-align:right">✅</td>
    </tr>
    <tr>
      <td>SetInstanceHealth (Pro) </td>
       <td style="text-align:right">✅</td>
    </tr>
    <tr>
      <td>SetInstanceProtection (Pro) </td>
       <td style="text-align:right">✅</td>
    </tr>
    <tr>
      <td>SuspendProcesses (Pro) </td>
       <td style="text-align:right">✅</td>
    </tr>
    <tr>
      <td>TerminateInstanceInAutoScalingGroup (Pro) </td>
       <td style="text-align:right">✅</td>
    </tr>
    <tr>
      <td>UpdateAutoScalingGroup (Pro) </td>
       <td style="text-align:right">✅</td>
    </tr>
  </tbody>
  <tbody>    <tr>
      <td><a data-toggle="collapse" href=".autoscaling-notimplemented">Show missing</a></td>
      <td style="text-align:right"></td>
    </tr>
  </tbody>
  <tbody class="collapse autoscaling-notimplemented">     <tr>
      <td>BatchDeleteScheduledAction</td>
       <td style="text-align:right">-</td>
    </tr>
    <tr>
      <td>BatchPutScheduledUpdateGroupAction</td>
       <td style="text-align:right">-</td>
    </tr>
    <tr>
      <td>CancelInstanceRefresh</td>
       <td style="text-align:right">-</td>
    </tr>
    <tr>
      <td>CompleteLifecycleAction</td>
       <td style="text-align:right">-</td>
    </tr>
    <tr>
      <td>DeleteNotificationConfiguration</td>
       <td style="text-align:right">-</td>
    </tr>
    <tr>
      <td>DeleteWarmPool</td>
       <td style="text-align:right">-</td>
    </tr>
    <tr>
      <td>DescribeAccountLimits</td>
       <td style="text-align:right">-</td>
    </tr>
    <tr>
      <td>DescribeAdjustmentTypes</td>
       <td style="text-align:right">-</td>
    </tr>
    <tr>
      <td>DescribeAutoScalingNotificationTypes</td>
       <td style="text-align:right">-</td>
    </tr>
    <tr>
      <td>DescribeInstanceRefreshes</td>
       <td style="text-align:right">-</td>
    </tr>
    <tr>
      <td>DescribeLifecycleHookTypes</td>
       <td style="text-align:right">-</td>
    </tr>
    <tr>
      <td>DescribeNotificationConfigurations</td>
       <td style="text-align:right">-</td>
    </tr>
    <tr>
      <td>DescribeScalingActivities</td>
       <td style="text-align:right">-</td>
    </tr>
    <tr>
      <td>DescribeScalingProcessTypes</td>
       <td style="text-align:right">-</td>
    </tr>
    <tr>
      <td>DescribeTerminationPolicyTypes</td>
       <td style="text-align:right">-</td>
    </tr>
    <tr>
      <td>DescribeWarmPool</td>
       <td style="text-align:right">-</td>
    </tr>
    <tr>
      <td>GetPredictiveScalingForecast</td>
       <td style="text-align:right">-</td>
    </tr>
    <tr>
      <td>PutNotificationConfiguration</td>
       <td style="text-align:right">-</td>
    </tr>
    <tr>
      <td>PutWarmPool</td>
       <td style="text-align:right">-</td>
    </tr>
    <tr>
      <td>RecordLifecycleActionHeartbeat</td>
       <td style="text-align:right">-</td>
    </tr>
    <tr>
      <td>StartInstanceRefresh</td>
       <td style="text-align:right">-</td>
    </tr>
  </tbody>
 </table>


## backup ##

<table>
  <thead>
    <tr>
      <th>Operation</th>
      <th style="text-align:right">Implemented</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td>CreateBackupPlan (Pro)  <a href="#misc" title="covered by our integration test suite">✨</a></td>
       <td style="text-align:right">✅</td>
    </tr>
    <tr>
      <td>CreateBackupSelection (Pro)  <a href="#misc" title="covered by our integration test suite">✨</a></td>
       <td style="text-align:right">✅</td>
    </tr>
    <tr>
      <td>CreateBackupVault (Pro)  <a href="#misc" title="covered by our integration test suite">✨</a></td>
       <td style="text-align:right">✅</td>
    </tr>
    <tr>
      <td>DeleteBackupPlan (Pro)  <a href="#misc" title="covered by our integration test suite">✨</a></td>
       <td style="text-align:right">✅</td>
    </tr>
    <tr>
      <td>DeleteBackupSelection (Pro)  <a href="#misc" title="covered by our integration test suite">✨</a></td>
       <td style="text-align:right">✅</td>
    </tr>
    <tr>
      <td>DeleteBackupVault (Pro)  <a href="#misc" title="covered by our integration test suite">✨</a></td>
       <td style="text-align:right">✅</td>
    </tr>
    <tr>
      <td>DescribeBackupVault (Pro)  <a href="#misc" title="covered by our integration test suite">✨</a></td>
       <td style="text-align:right">✅</td>
    </tr>
    <tr>
      <td>DescribeRestoreJob (Pro)  <a href="#misc" title="covered by our integration test suite">✨</a></td>
       <td style="text-align:right">✅</td>
    </tr>
    <tr>
      <td>GetBackupPlan (Pro)  <a href="#misc" title="covered by our integration test suite">✨</a></td>
       <td style="text-align:right">✅</td>
    </tr>
    <tr>
      <td>GetBackupSelection (Pro)  <a href="#misc" title="covered by our integration test suite">✨</a></td>
       <td style="text-align:right">✅</td>
    </tr>
    <tr>
      <td>ListBackupJobs (Pro) </td>
       <td style="text-align:right">✅</td>
    </tr>
    <tr>
      <td>ListBackupPlans (Pro)  <a href="#misc" title="covered by our integration test suite">✨</a></td>
       <td style="text-align:right">✅</td>
    </tr>
    <tr>
      <td>ListBackupSelections (Pro)  <a href="#misc" title="covered by our integration test suite">✨</a></td>
       <td style="text-align:right">✅</td>
    </tr>
    <tr>
      <td>ListBackupVaults (Pro)  <a href="#misc" title="covered by our integration test suite">✨</a></td>
       <td style="text-align:right">✅</td>
    </tr>
    <tr>
      <td>ListCopyJobs (Pro) </td>
       <td style="text-align:right">✅</td>
    </tr>
    <tr>
      <td>ListRecoveryPointsByBackupVault (Pro)  <a href="#misc" title="covered by our integration test suite">✨</a></td>
       <td style="text-align:right">✅</td>
    </tr>
    <tr>
      <td>ListRecoveryPointsByResource (Pro)  <a href="#misc" title="covered by our integration test suite">✨</a></td>
       <td style="text-align:right">✅</td>
    </tr>
    <tr>
      <td>ListReportJobs (Pro) </td>
       <td style="text-align:right">✅</td>
    </tr>
    <tr>
      <td>ListRestoreJobs (Pro) </td>
       <td style="text-align:right">✅</td>
    </tr>
    <tr>
      <td>StartRestoreJob (Pro)  <a href="#misc" title="covered by our integration test suite">✨</a></td>
       <td style="text-align:right">✅</td>
    </tr>
    <tr>
      <td>UpdateBackupPlan (Pro)  <a href="#misc" title="covered by our integration test suite">✨</a></td>
       <td style="text-align:right">✅</td>
    </tr>
  </tbody>
  <tbody>    <tr>
      <td><a data-toggle="collapse" href=".backup-notimplemented">Show missing</a></td>
      <td style="text-align:right"></td>
    </tr>
  </tbody>
  <tbody class="collapse backup-notimplemented">     <tr>
      <td>CreateFramework</td>
       <td style="text-align:right">-</td>
    </tr>
    <tr>
      <td>CreateReportPlan</td>
       <td style="text-align:right">-</td>
    </tr>
    <tr>
      <td>DeleteBackupVaultAccessPolicy</td>
       <td style="text-align:right">-</td>
    </tr>
    <tr>
      <td>DeleteBackupVaultLockConfiguration</td>
       <td style="text-align:right">-</td>
    </tr>
    <tr>
      <td>DeleteBackupVaultNotifications</td>
       <td style="text-align:right">-</td>
    </tr>
    <tr>
      <td>DeleteFramework</td>
       <td style="text-align:right">-</td>
    </tr>
    <tr>
      <td>DeleteRecoveryPoint</td>
       <td style="text-align:right">-</td>
    </tr>
    <tr>
      <td>DeleteReportPlan</td>
       <td style="text-align:right">-</td>
    </tr>
    <tr>
      <td>DescribeBackupJob</td>
       <td style="text-align:right">-</td>
    </tr>
    <tr>
      <td>DescribeCopyJob</td>
       <td style="text-align:right">-</td>
    </tr>
    <tr>
      <td>DescribeFramework</td>
       <td style="text-align:right">-</td>
    </tr>
    <tr>
      <td>DescribeGlobalSettings</td>
       <td style="text-align:right">-</td>
    </tr>
    <tr>
      <td>DescribeProtectedResource</td>
       <td style="text-align:right">-</td>
    </tr>
    <tr>
      <td>DescribeRecoveryPoint</td>
       <td style="text-align:right">-</td>
    </tr>
    <tr>
      <td>DescribeRegionSettings</td>
       <td style="text-align:right">-</td>
    </tr>
    <tr>
      <td>DescribeReportJob</td>
       <td style="text-align:right">-</td>
    </tr>
    <tr>
      <td>DescribeReportPlan</td>
       <td style="text-align:right">-</td>
    </tr>
    <tr>
      <td>DisassociateRecoveryPoint</td>
       <td style="text-align:right">-</td>
    </tr>
    <tr>
      <td>ExportBackupPlanTemplate</td>
       <td style="text-align:right">-</td>
    </tr>
    <tr>
      <td>GetBackupPlanFromJSON</td>
       <td style="text-align:right">-</td>
    </tr>
    <tr>
      <td>GetBackupPlanFromTemplate</td>
       <td style="text-align:right">-</td>
    </tr>
    <tr>
      <td>GetBackupVaultAccessPolicy</td>
       <td style="text-align:right">-</td>
    </tr>
    <tr>
      <td>GetBackupVaultNotifications</td>
       <td style="text-align:right">-</td>
    </tr>
    <tr>
      <td>GetRecoveryPointRestoreMetadata</td>
       <td style="text-align:right">-</td>
    </tr>
    <tr>
      <td>GetSupportedResourceTypes</td>
       <td style="text-align:right">-</td>
    </tr>
    <tr>
      <td>ListBackupPlanTemplates</td>
       <td style="text-align:right">-</td>
    </tr>
    <tr>
      <td>ListBackupPlanVersions</td>
       <td style="text-align:right">-</td>
    </tr>
    <tr>
      <td>ListFrameworks</td>
       <td style="text-align:right">-</td>
    </tr>
    <tr>
      <td>ListProtectedResources</td>
       <td style="text-align:right">-</td>
    </tr>
    <tr>
      <td>ListReportPlans</td>
       <td style="text-align:right">-</td>
    </tr>
    <tr>
      <td>ListTags</td>
       <td style="text-align:right">-</td>
    </tr>
    <tr>
      <td>PutBackupVaultAccessPolicy</td>
       <td style="text-align:right">-</td>
    </tr>
    <tr>
      <td>PutBackupVaultLockConfiguration</td>
       <td style="text-align:right">-</td>
    </tr>
    <tr>
      <td>PutBackupVaultNotifications</td>
       <td style="text-align:right">-</td>
    </tr>
    <tr>
      <td>StartBackupJob</td>
       <td style="text-align:right">-</td>
    </tr>
    <tr>
      <td>StartCopyJob</td>
       <td style="text-align:right">-</td>
    </tr>
    <tr>
      <td>StartReportJob</td>
       <td style="text-align:right">-</td>
    </tr>
    <tr>
      <td>StopBackupJob</td>
       <td style="text-align:right">-</td>
    </tr>
    <tr>
      <td>TagResource</td>
       <td style="text-align:right">-</td>
    </tr>
    <tr>
      <td>UntagResource</td>
       <td style="text-align:right">-</td>
    </tr>
    <tr>
      <td>UpdateFramework</td>
       <td style="text-align:right">-</td>
    </tr>
    <tr>
      <td>UpdateGlobalSettings</td>
       <td style="text-align:right">-</td>
    </tr>
    <tr>
      <td>UpdateRecoveryPointLifecycle</td>
       <td style="text-align:right">-</td>
    </tr>
    <tr>
      <td>UpdateRegionSettings</td>
       <td style="text-align:right">-</td>
    </tr>
    <tr>
      <td>UpdateReportPlan</td>
       <td style="text-align:right">-</td>
    </tr>
  </tbody>
 </table>


## batch ##

<table>
  <thead>
    <tr>
      <th>Operation</th>
      <th style="text-align:right">Implemented</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td>CancelJob (Pro) </td>
       <td style="text-align:right">✅</td>
    </tr>
    <tr>
      <td>CreateComputeEnvironment (Pro)  <a href="#misc" title="covered by our integration test suite">✨</a></td>
       <td style="text-align:right">✅</td>
    </tr>
    <tr>
      <td>CreateJobQueue (Pro)  <a href="#misc" title="covered by our integration test suite">✨</a></td>
       <td style="text-align:right">✅</td>
    </tr>
    <tr>
      <td>DeleteComputeEnvironment (Pro)  <a href="#misc" title="covered by our integration test suite">✨</a></td>
       <td style="text-align:right">✅</td>
    </tr>
    <tr>
      <td>DeleteJobQueue (Pro)  <a href="#misc" title="covered by our integration test suite">✨</a></td>
       <td style="text-align:right">✅</td>
    </tr>
    <tr>
      <td>DeregisterJobDefinition (Pro)  <a href="#misc" title="covered by our integration test suite">✨</a></td>
       <td style="text-align:right">✅</td>
    </tr>
    <tr>
      <td>DescribeComputeEnvironments (Pro) </td>
       <td style="text-align:right">✅</td>
    </tr>
    <tr>
      <td>DescribeJobDefinitions (Pro)  <a href="#misc" title="covered by our integration test suite">✨</a></td>
       <td style="text-align:right">✅</td>
    </tr>
    <tr>
      <td>DescribeJobQueues (Pro) </td>
       <td style="text-align:right">✅</td>
    </tr>
    <tr>
      <td>DescribeJobs (Pro)  <a href="#misc" title="covered by our integration test suite">✨</a></td>
       <td style="text-align:right">✅</td>
    </tr>
    <tr>
      <td>ListJobs (Pro) </td>
       <td style="text-align:right">✅</td>
    </tr>
    <tr>
      <td>ListTagsForResource (Pro) </td>
       <td style="text-align:right">✅</td>
    </tr>
    <tr>
      <td>RegisterJobDefinition (Pro)  <a href="#misc" title="covered by our integration test suite">✨</a></td>
       <td style="text-align:right">✅</td>
    </tr>
    <tr>
      <td>SubmitJob (Pro)  <a href="#misc" title="covered by our integration test suite">✨</a></td>
       <td style="text-align:right">✅</td>
    </tr>
    <tr>
      <td>TagResource (Pro) </td>
       <td style="text-align:right">✅</td>
    </tr>
    <tr>
      <td>TerminateJob (Pro) </td>
       <td style="text-align:right">✅</td>
    </tr>
    <tr>
      <td>UntagResource (Pro) </td>
       <td style="text-align:right">✅</td>
    </tr>
    <tr>
      <td>UpdateComputeEnvironment (Pro)  <a href="#misc" title="covered by our integration test suite">✨</a></td>
       <td style="text-align:right">✅</td>
    </tr>
    <tr>
      <td>UpdateJobQueue (Pro) </td>
       <td style="text-align:right">✅</td>
    </tr>
  </tbody>
  <tbody>    <tr>
      <td><a data-toggle="collapse" href=".batch-notimplemented">Show missing</a></td>
      <td style="text-align:right"></td>
    </tr>
  </tbody>
  <tbody class="collapse batch-notimplemented">     <tr>
      <td>CreateSchedulingPolicy</td>
       <td style="text-align:right">-</td>
    </tr>
    <tr>
      <td>DeleteSchedulingPolicy</td>
       <td style="text-align:right">-</td>
    </tr>
    <tr>
      <td>DescribeSchedulingPolicies</td>
       <td style="text-align:right">-</td>
    </tr>
    <tr>
      <td>ListSchedulingPolicies</td>
       <td style="text-align:right">-</td>
    </tr>
    <tr>
      <td>UpdateSchedulingPolicy</td>
       <td style="text-align:right">-</td>
    </tr>
  </tbody>
 </table>


## ce ##

<table>
  <thead>
    <tr>
      <th>Operation</th>
      <th style="text-align:right">Implemented</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td>CreateAnomalyMonitor (Pro)  <a href="#misc" title="covered by our integration test suite">✨</a></td>
       <td style="text-align:right">✅</td>
    </tr>
    <tr>
      <td>CreateAnomalySubscription (Pro)  <a href="#misc" title="covered by our integration test suite">✨</a></td>
       <td style="text-align:right">✅</td>
    </tr>
    <tr>
      <td>CreateCostCategoryDefinition (Pro)  <a href="#misc" title="covered by our integration test suite">✨</a></td>
       <td style="text-align:right">✅</td>
    </tr>
    <tr>
      <td>DeleteAnomalyMonitor (Pro)  <a href="#misc" title="covered by our integration test suite">✨</a></td>
       <td style="text-align:right">✅</td>
    </tr>
    <tr>
      <td>DeleteAnomalySubscription (Pro)  <a href="#misc" title="covered by our integration test suite">✨</a></td>
       <td style="text-align:right">✅</td>
    </tr>
    <tr>
      <td>DeleteCostCategoryDefinition (Pro)  <a href="#misc" title="covered by our integration test suite">✨</a></td>
       <td style="text-align:right">✅</td>
    </tr>
    <tr>
      <td>DescribeCostCategoryDefinition (Pro)  <a href="#misc" title="covered by our integration test suite">✨</a></td>
       <td style="text-align:right">✅</td>
    </tr>
    <tr>
      <td>GetAnomalyMonitors (Pro)  <a href="#misc" title="covered by our integration test suite">✨</a></td>
       <td style="text-align:right">✅</td>
    </tr>
    <tr>
      <td>GetAnomalySubscriptions (Pro)  <a href="#misc" title="covered by our integration test suite">✨</a></td>
       <td style="text-align:right">✅</td>
    </tr>
    <tr>
      <td>UpdateAnomalyMonitor (Pro)  <a href="#misc" title="covered by our integration test suite">✨</a></td>
       <td style="text-align:right">✅</td>
    </tr>
    <tr>
      <td>UpdateAnomalySubscription (Pro)  <a href="#misc" title="covered by our integration test suite">✨</a></td>
       <td style="text-align:right">✅</td>
    </tr>
    <tr>
      <td>UpdateCostCategoryDefinition (Pro)  <a href="#misc" title="covered by our integration test suite">✨</a></td>
       <td style="text-align:right">✅</td>
    </tr>
  </tbody>
  <tbody>    <tr>
      <td><a data-toggle="collapse" href=".ce-notimplemented">Show missing</a></td>
      <td style="text-align:right"></td>
    </tr>
  </tbody>
  <tbody class="collapse ce-notimplemented">     <tr>
      <td>GetAnomalies</td>
       <td style="text-align:right">-</td>
    </tr>
    <tr>
      <td>GetCostAndUsage</td>
       <td style="text-align:right">-</td>
    </tr>
    <tr>
      <td>GetCostAndUsageWithResources</td>
       <td style="text-align:right">-</td>
    </tr>
    <tr>
      <td>GetCostCategories</td>
       <td style="text-align:right">-</td>
    </tr>
    <tr>
      <td>GetCostForecast</td>
       <td style="text-align:right">-</td>
    </tr>
    <tr>
      <td>GetDimensionValues</td>
       <td style="text-align:right">-</td>
    </tr>
    <tr>
      <td>GetReservationCoverage</td>
       <td style="text-align:right">-</td>
    </tr>
    <tr>
      <td>GetReservationPurchaseRecommendation</td>
       <td style="text-align:right">-</td>
    </tr>
    <tr>
      <td>GetReservationUtilization</td>
       <td style="text-align:right">-</td>
    </tr>
    <tr>
      <td>GetRightsizingRecommendation</td>
       <td style="text-align:right">-</td>
    </tr>
    <tr>
      <td>GetSavingsPlansCoverage</td>
       <td style="text-align:right">-</td>
    </tr>
    <tr>
      <td>GetSavingsPlansPurchaseRecommendation</td>
       <td style="text-align:right">-</td>
    </tr>
    <tr>
      <td>GetSavingsPlansUtilization</td>
       <td style="text-align:right">-</td>
    </tr>
    <tr>
      <td>GetSavingsPlansUtilizationDetails</td>
       <td style="text-align:right">-</td>
    </tr>
    <tr>
      <td>GetTags</td>
       <td style="text-align:right">-</td>
    </tr>
    <tr>
      <td>GetUsageForecast</td>
       <td style="text-align:right">-</td>
    </tr>
    <tr>
      <td>ListCostAllocationTags</td>
       <td style="text-align:right">-</td>
    </tr>
    <tr>
      <td>ListCostCategoryDefinitions</td>
       <td style="text-align:right">-</td>
    </tr>
    <tr>
      <td>ListTagsForResource</td>
       <td style="text-align:right">-</td>
    </tr>
    <tr>
      <td>ProvideAnomalyFeedback</td>
       <td style="text-align:right">-</td>
    </tr>
    <tr>
      <td>TagResource</td>
       <td style="text-align:right">-</td>
    </tr>
    <tr>
      <td>UntagResource</td>
       <td style="text-align:right">-</td>
    </tr>
    <tr>
      <td>UpdateCostAllocationTagsStatus</td>
       <td style="text-align:right">-</td>
    </tr>
  </tbody>
 </table>


## cloudformation ##

<table>
  <thead>
    <tr>
      <th>Operation</th>
      <th style="text-align:right">Implemented</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td>ActivateType</td>
       <td style="text-align:right">✅</td>
    </tr>
    <tr>
      <td>BatchDescribeTypeConfigurations (Pro) </td>
       <td style="text-align:right">✅</td>
    </tr>
    <tr>
      <td>CreateChangeSet <a href="#misc" title="covered by our integration test suite">✨</a></td>
       <td style="text-align:right">✅</td>
    </tr>
    <tr>
      <td>CreateStack <a href="#misc" title="covered by our integration test suite">✨</a></td>
       <td style="text-align:right">✅</td>
    </tr>
    <tr>
      <td>CreateStackInstances</td>
       <td style="text-align:right">✅</td>
    </tr>
    <tr>
      <td>CreateStackSet</td>
       <td style="text-align:right">✅</td>
    </tr>
    <tr>
      <td>DeleteChangeSet <a href="#misc" title="covered by our integration test suite">✨</a></td>
       <td style="text-align:right">✅</td>
    </tr>
    <tr>
      <td>DeleteStack <a href="#misc" title="covered by our integration test suite">✨</a></td>
       <td style="text-align:right">✅</td>
    </tr>
    <tr>
      <td>DeleteStackSet</td>
       <td style="text-align:right">✅</td>
    </tr>
    <tr>
      <td>DescribeChangeSet <a href="#misc" title="covered by our integration test suite">✨</a></td>
       <td style="text-align:right">✅</td>
    </tr>
    <tr>
      <td>DescribeStackEvents <a href="#misc" title="covered by our integration test suite">✨</a></td>
       <td style="text-align:right">✅</td>
    </tr>
    <tr>
      <td>DescribeStackResource <a href="#misc" title="covered by our integration test suite">✨</a></td>
       <td style="text-align:right">✅</td>
    </tr>
    <tr>
      <td>DescribeStackResources <a href="#misc" title="covered by our integration test suite">✨</a></td>
       <td style="text-align:right">✅</td>
    </tr>
    <tr>
      <td>DescribeStackSet</td>
       <td style="text-align:right">✅</td>
    </tr>
    <tr>
      <td>DescribeStackSetOperation</td>
       <td style="text-align:right">✅</td>
    </tr>
    <tr>
      <td>DescribeStacks <a href="#misc" title="covered by our integration test suite">✨</a></td>
       <td style="text-align:right">✅</td>
    </tr>
    <tr>
      <td>ExecuteChangeSet <a href="#misc" title="covered by our integration test suite">✨</a></td>
       <td style="text-align:right">✅</td>
    </tr>
    <tr>
      <td>GetTemplate <a href="#misc" title="covered by our integration test suite">✨</a></td>
       <td style="text-align:right">✅</td>
    </tr>
    <tr>
      <td>GetTemplateSummary <a href="#misc" title="covered by our integration test suite">✨</a></td>
       <td style="text-align:right">✅</td>
    </tr>
    <tr>
      <td>ListChangeSets</td>
       <td style="text-align:right">✅</td>
    </tr>
    <tr>
      <td>ListExports <a href="#misc" title="covered by our integration test suite">✨</a></td>
       <td style="text-align:right">✅</td>
    </tr>
    <tr>
      <td>ListImports</td>
       <td style="text-align:right">✅</td>
    </tr>
    <tr>
      <td>ListStackInstances</td>
       <td style="text-align:right">✅</td>
    </tr>
    <tr>
      <td>ListStackResources <a href="#misc" title="covered by our integration test suite">✨</a></td>
       <td style="text-align:right">✅</td>
    </tr>
    <tr>
      <td>ListStackSets</td>
       <td style="text-align:right">✅</td>
    </tr>
    <tr>
      <td>ListStacks <a href="#misc" title="covered by our integration test suite">✨</a></td>
       <td style="text-align:right">✅</td>
    </tr>
    <tr>
      <td>UpdateStack <a href="#misc" title="covered by our integration test suite">✨</a></td>
       <td style="text-align:right">✅</td>
    </tr>
    <tr>
      <td>UpdateStackSet</td>
       <td style="text-align:right">✅</td>
    </tr>
    <tr>
      <td>ValidateTemplate <a href="#misc" title="covered by our integration test suite">✨</a></td>
       <td style="text-align:right">✅</td>
    </tr>
  </tbody>
  <tbody>    <tr>
      <td><a data-toggle="collapse" href=".cloudformation-notimplemented">Show missing</a></td>
      <td style="text-align:right"></td>
    </tr>
  </tbody>
  <tbody class="collapse cloudformation-notimplemented">     <tr>
      <td>CancelUpdateStack</td>
       <td style="text-align:right">-</td>
    </tr>
    <tr>
      <td>ContinueUpdateRollback</td>
       <td style="text-align:right">-</td>
    </tr>
    <tr>
      <td>DeactivateType</td>
       <td style="text-align:right">-</td>
    </tr>
    <tr>
      <td>DeleteStackInstances</td>
       <td style="text-align:right">-</td>
    </tr>
    <tr>
      <td>DeregisterType</td>
       <td style="text-align:right">-</td>
    </tr>
    <tr>
      <td>DescribeAccountLimits</td>
       <td style="text-align:right">-</td>
    </tr>
    <tr>
      <td>DescribeChangeSetHooks</td>
       <td style="text-align:right">-</td>
    </tr>
    <tr>
      <td>DescribePublisher</td>
       <td style="text-align:right">-</td>
    </tr>
    <tr>
      <td>DescribeStackDriftDetectionStatus</td>
       <td style="text-align:right">-</td>
    </tr>
    <tr>
      <td>DescribeStackInstance</td>
       <td style="text-align:right">-</td>
    </tr>
    <tr>
      <td>DescribeStackResourceDrifts</td>
       <td style="text-align:right">-</td>
    </tr>
    <tr>
      <td>DescribeType</td>
       <td style="text-align:right">-</td>
    </tr>
    <tr>
      <td>DescribeTypeRegistration</td>
       <td style="text-align:right">-</td>
    </tr>
    <tr>
      <td>DetectStackDrift</td>
       <td style="text-align:right">-</td>
    </tr>
    <tr>
      <td>DetectStackResourceDrift</td>
       <td style="text-align:right">-</td>
    </tr>
    <tr>
      <td>DetectStackSetDrift</td>
       <td style="text-align:right">-</td>
    </tr>
    <tr>
      <td>EstimateTemplateCost</td>
       <td style="text-align:right">-</td>
    </tr>
    <tr>
      <td>GetStackPolicy</td>
       <td style="text-align:right">-</td>
    </tr>
    <tr>
      <td>ImportStacksToStackSet</td>
       <td style="text-align:right">-</td>
    </tr>
    <tr>
      <td>ListStackSetOperationResults</td>
       <td style="text-align:right">-</td>
    </tr>
    <tr>
      <td>ListStackSetOperations</td>
       <td style="text-align:right">-</td>
    </tr>
    <tr>
      <td>ListTypeRegistrations</td>
       <td style="text-align:right">-</td>
    </tr>
    <tr>
      <td>ListTypeVersions</td>
       <td style="text-align:right">-</td>
    </tr>
    <tr>
      <td>ListTypes</td>
       <td style="text-align:right">-</td>
    </tr>
    <tr>
      <td>PublishType</td>
       <td style="text-align:right">-</td>
    </tr>
    <tr>
      <td>RecordHandlerProgress</td>
       <td style="text-align:right">-</td>
    </tr>
    <tr>
      <td>RegisterPublisher</td>
       <td style="text-align:right">-</td>
    </tr>
    <tr>
      <td>RegisterType</td>
       <td style="text-align:right">-</td>
    </tr>
    <tr>
      <td>RollbackStack</td>
       <td style="text-align:right">-</td>
    </tr>
    <tr>
      <td>SetStackPolicy</td>
       <td style="text-align:right">-</td>
    </tr>
    <tr>
      <td>SetTypeConfiguration</td>
       <td style="text-align:right">-</td>
    </tr>
    <tr>
      <td>SetTypeDefaultVersion</td>
       <td style="text-align:right">-</td>
    </tr>
    <tr>
      <td>SignalResource</td>
       <td style="text-align:right">-</td>
    </tr>
    <tr>
      <td>StopStackSetOperation</td>
       <td style="text-align:right">-</td>
    </tr>
    <tr>
      <td>TestType</td>
       <td style="text-align:right">-</td>
    </tr>
    <tr>
      <td>UpdateStackInstances</td>
       <td style="text-align:right">-</td>
    </tr>
    <tr>
      <td>UpdateTerminationProtection</td>
       <td style="text-align:right">-</td>
    </tr>
  </tbody>
 </table>


## cloudfront ##

<table>
  <thead>
    <tr>
      <th>Operation</th>
      <th style="text-align:right">Implemented</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td>CreateCloudFrontOriginAccessIdentity (Pro)  <a href="#misc" title="covered by our integration test suite">✨</a></td>
       <td style="text-align:right">✅</td>
    </tr>
    <tr>
      <td>CreateDistribution (Pro)  <a href="#misc" title="covered by our integration test suite">✨</a></td>
       <td style="text-align:right">✅</td>
    </tr>
    <tr>
      <td>CreateDistributionWithTags (Pro)  <a href="#misc" title="covered by our integration test suite">✨</a></td>
       <td style="text-align:right">✅</td>
    </tr>
    <tr>
      <td>CreateFunction (Pro)  <a href="#misc" title="covered by our integration test suite">✨</a></td>
       <td style="text-align:right">✅</td>
    </tr>
    <tr>
      <td>CreateInvalidation (Pro)  <a href="#misc" title="covered by our integration test suite">✨</a></td>
       <td style="text-align:right">✅</td>
    </tr>
    <tr>
      <td>CreateOriginRequestPolicy (Pro)  <a href="#misc" title="covered by our integration test suite">✨</a></td>
       <td style="text-align:right">✅</td>
    </tr>
    <tr>
      <td>DeleteCloudFrontOriginAccessIdentity (Pro)  <a href="#misc" title="covered by our integration test suite">✨</a></td>
       <td style="text-align:right">✅</td>
    </tr>
    <tr>
      <td>DeleteDistribution (Pro)  <a href="#misc" title="covered by our integration test suite">✨</a></td>
       <td style="text-align:right">✅</td>
    </tr>
    <tr>
      <td>DeleteFunction (Pro)  <a href="#misc" title="covered by our integration test suite">✨</a></td>
       <td style="text-align:right">✅</td>
    </tr>
    <tr>
      <td>DeleteOriginRequestPolicy (Pro)  <a href="#misc" title="covered by our integration test suite">✨</a></td>
       <td style="text-align:right">✅</td>
    </tr>
    <tr>
      <td>GetCloudFrontOriginAccessIdentity (Pro)  <a href="#misc" title="covered by our integration test suite">✨</a></td>
       <td style="text-align:right">✅</td>
    </tr>
    <tr>
      <td>GetDistribution (Pro)  <a href="#misc" title="covered by our integration test suite">✨</a></td>
       <td style="text-align:right">✅</td>
    </tr>
    <tr>
      <td>GetFunction (Pro)  <a href="#misc" title="covered by our integration test suite">✨</a></td>
       <td style="text-align:right">✅</td>
    </tr>
    <tr>
      <td>GetInvalidation (Pro)  <a href="#misc" title="covered by our integration test suite">✨</a></td>
       <td style="text-align:right">✅</td>
    </tr>
    <tr>
      <td>GetOriginRequestPolicy (Pro)  <a href="#misc" title="covered by our integration test suite">✨</a></td>
       <td style="text-align:right">✅</td>
    </tr>
    <tr>
      <td>ListCloudFrontOriginAccessIdentities (Pro)  <a href="#misc" title="covered by our integration test suite">✨</a></td>
       <td style="text-align:right">✅</td>
    </tr>
    <tr>
      <td>ListDistributions (Pro)  <a href="#misc" title="covered by our integration test suite">✨</a></td>
       <td style="text-align:right">✅</td>
    </tr>
    <tr>
      <td>ListFunctions (Pro)  <a href="#misc" title="covered by our integration test suite">✨</a></td>
       <td style="text-align:right">✅</td>
    </tr>
    <tr>
      <td>ListInvalidations (Pro)  <a href="#misc" title="covered by our integration test suite">✨</a></td>
       <td style="text-align:right">✅</td>
    </tr>
    <tr>
      <td>ListOriginRequestPolicies (Pro)  <a href="#misc" title="covered by our integration test suite">✨</a></td>
       <td style="text-align:right">✅</td>
    </tr>
    <tr>
      <td>ListTagsForResource (Pro)  <a href="#misc" title="covered by our integration test suite">✨</a></td>
       <td style="text-align:right">✅</td>
    </tr>
    <tr>
      <td>TagResource (Pro) </td>
       <td style="text-align:right">✅</td>
    </tr>
    <tr>
      <td>UntagResource (Pro)  <a href="#misc" title="covered by our integration test suite">✨</a></td>
       <td style="text-align:right">✅</td>
    </tr>
    <tr>
      <td>UpdateDistribution (Pro)  <a href="#misc" title="covered by our integration test suite">✨</a></td>
       <td style="text-align:right">✅</td>
    </tr>
    <tr>
      <td>UpdateFunction (Pro)  <a href="#misc" title="covered by our integration test suite">✨</a></td>
       <td style="text-align:right">✅</td>
    </tr>
    <tr>
      <td>UpdateOriginRequestPolicy (Pro)  <a href="#misc" title="covered by our integration test suite">✨</a></td>
       <td style="text-align:right">✅</td>
    </tr>
  </tbody>
  <tbody>    <tr>
      <td><a data-toggle="collapse" href=".cloudfront-notimplemented">Show missing</a></td>
      <td style="text-align:right"></td>
    </tr>
  </tbody>
  <tbody class="collapse cloudfront-notimplemented">     <tr>
      <td>AssociateAlias</td>
       <td style="text-align:right">-</td>
    </tr>
    <tr>
      <td>CreateCachePolicy</td>
       <td style="text-align:right">-</td>
    </tr>
    <tr>
      <td>CreateFieldLevelEncryptionConfig</td>
       <td style="text-align:right">-</td>
    </tr>
    <tr>
      <td>CreateFieldLevelEncryptionProfile</td>
       <td style="text-align:right">-</td>
    </tr>
    <tr>
      <td>CreateKeyGroup</td>
       <td style="text-align:right">-</td>
    </tr>
    <tr>
      <td>CreateMonitoringSubscription</td>
       <td style="text-align:right">-</td>
    </tr>
    <tr>
      <td>CreateOriginAccessControl</td>
       <td style="text-align:right">-</td>
    </tr>
    <tr>
      <td>CreatePublicKey</td>
       <td style="text-align:right">-</td>
    </tr>
    <tr>
      <td>CreateRealtimeLogConfig</td>
       <td style="text-align:right">-</td>
    </tr>
    <tr>
      <td>CreateResponseHeadersPolicy</td>
       <td style="text-align:right">-</td>
    </tr>
    <tr>
      <td>CreateStreamingDistribution</td>
       <td style="text-align:right">-</td>
    </tr>
    <tr>
      <td>CreateStreamingDistributionWithTags</td>
       <td style="text-align:right">-</td>
    </tr>
    <tr>
      <td>DeleteCachePolicy</td>
       <td style="text-align:right">-</td>
    </tr>
    <tr>
      <td>DeleteFieldLevelEncryptionConfig</td>
       <td style="text-align:right">-</td>
    </tr>
    <tr>
      <td>DeleteFieldLevelEncryptionProfile</td>
       <td style="text-align:right">-</td>
    </tr>
    <tr>
      <td>DeleteKeyGroup</td>
       <td style="text-align:right">-</td>
    </tr>
    <tr>
      <td>DeleteMonitoringSubscription</td>
       <td style="text-align:right">-</td>
    </tr>
    <tr>
      <td>DeleteOriginAccessControl</td>
       <td style="text-align:right">-</td>
    </tr>
    <tr>
      <td>DeletePublicKey</td>
       <td style="text-align:right">-</td>
    </tr>
    <tr>
      <td>DeleteRealtimeLogConfig</td>
       <td style="text-align:right">-</td>
    </tr>
    <tr>
      <td>DeleteResponseHeadersPolicy</td>
       <td style="text-align:right">-</td>
    </tr>
    <tr>
      <td>DeleteStreamingDistribution</td>
       <td style="text-align:right">-</td>
    </tr>
    <tr>
      <td>DescribeFunction</td>
       <td style="text-align:right">-</td>
    </tr>
    <tr>
      <td>GetCachePolicy</td>
       <td style="text-align:right">-</td>
    </tr>
    <tr>
      <td>GetCachePolicyConfig</td>
       <td style="text-align:right">-</td>
    </tr>
    <tr>
      <td>GetCloudFrontOriginAccessIdentityConfig</td>
       <td style="text-align:right">-</td>
    </tr>
    <tr>
      <td>GetDistributionConfig</td>
       <td style="text-align:right">-</td>
    </tr>
    <tr>
      <td>GetFieldLevelEncryption</td>
       <td style="text-align:right">-</td>
    </tr>
    <tr>
      <td>GetFieldLevelEncryptionConfig</td>
       <td style="text-align:right">-</td>
    </tr>
    <tr>
      <td>GetFieldLevelEncryptionProfile</td>
       <td style="text-align:right">-</td>
    </tr>
    <tr>
      <td>GetFieldLevelEncryptionProfileConfig</td>
       <td style="text-align:right">-</td>
    </tr>
    <tr>
      <td>GetKeyGroup</td>
       <td style="text-align:right">-</td>
    </tr>
    <tr>
      <td>GetKeyGroupConfig</td>
       <td style="text-align:right">-</td>
    </tr>
    <tr>
      <td>GetMonitoringSubscription</td>
       <td style="text-align:right">-</td>
    </tr>
    <tr>
      <td>GetOriginAccessControl</td>
       <td style="text-align:right">-</td>
    </tr>
    <tr>
      <td>GetOriginAccessControlConfig</td>
       <td style="text-align:right">-</td>
    </tr>
    <tr>
      <td>GetOriginRequestPolicyConfig</td>
       <td style="text-align:right">-</td>
    </tr>
    <tr>
      <td>GetPublicKey</td>
       <td style="text-align:right">-</td>
    </tr>
    <tr>
      <td>GetPublicKeyConfig</td>
       <td style="text-align:right">-</td>
    </tr>
    <tr>
      <td>GetRealtimeLogConfig</td>
       <td style="text-align:right">-</td>
    </tr>
    <tr>
      <td>GetResponseHeadersPolicy</td>
       <td style="text-align:right">-</td>
    </tr>
    <tr>
      <td>GetResponseHeadersPolicyConfig</td>
       <td style="text-align:right">-</td>
    </tr>
    <tr>
      <td>GetStreamingDistribution</td>
       <td style="text-align:right">-</td>
    </tr>
    <tr>
      <td>GetStreamingDistributionConfig</td>
       <td style="text-align:right">-</td>
    </tr>
    <tr>
      <td>ListCachePolicies</td>
       <td style="text-align:right">-</td>
    </tr>
    <tr>
      <td>ListConflictingAliases</td>
       <td style="text-align:right">-</td>
    </tr>
    <tr>
      <td>ListDistributionsByCachePolicyId</td>
       <td style="text-align:right">-</td>
    </tr>
    <tr>
      <td>ListDistributionsByKeyGroup</td>
       <td style="text-align:right">-</td>
    </tr>
    <tr>
      <td>ListDistributionsByOriginRequestPolicyId</td>
       <td style="text-align:right">-</td>
    </tr>
    <tr>
      <td>ListDistributionsByRealtimeLogConfig</td>
       <td style="text-align:right">-</td>
    </tr>
    <tr>
      <td>ListDistributionsByResponseHeadersPolicyId</td>
       <td style="text-align:right">-</td>
    </tr>
    <tr>
      <td>ListDistributionsByWebACLId</td>
       <td style="text-align:right">-</td>
    </tr>
    <tr>
      <td>ListFieldLevelEncryptionConfigs</td>
       <td style="text-align:right">-</td>
    </tr>
    <tr>
      <td>ListFieldLevelEncryptionProfiles</td>
       <td style="text-align:right">-</td>
    </tr>
    <tr>
      <td>ListKeyGroups</td>
       <td style="text-align:right">-</td>
    </tr>
    <tr>
      <td>ListOriginAccessControls</td>
       <td style="text-align:right">-</td>
    </tr>
    <tr>
      <td>ListPublicKeys</td>
       <td style="text-align:right">-</td>
    </tr>
    <tr>
      <td>ListRealtimeLogConfigs</td>
       <td style="text-align:right">-</td>
    </tr>
    <tr>
      <td>ListResponseHeadersPolicies</td>
       <td style="text-align:right">-</td>
    </tr>
    <tr>
      <td>ListStreamingDistributions</td>
       <td style="text-align:right">-</td>
    </tr>
    <tr>
      <td>PublishFunction</td>
       <td style="text-align:right">-</td>
    </tr>
    <tr>
      <td>TestFunction</td>
       <td style="text-align:right">-</td>
    </tr>
    <tr>
      <td>UpdateCachePolicy</td>
       <td style="text-align:right">-</td>
    </tr>
    <tr>
      <td>UpdateCloudFrontOriginAccessIdentity</td>
       <td style="text-align:right">-</td>
    </tr>
    <tr>
      <td>UpdateFieldLevelEncryptionConfig</td>
       <td style="text-align:right">-</td>
    </tr>
    <tr>
      <td>UpdateFieldLevelEncryptionProfile</td>
       <td style="text-align:right">-</td>
    </tr>
    <tr>
      <td>UpdateKeyGroup</td>
       <td style="text-align:right">-</td>
    </tr>
    <tr>
      <td>UpdateOriginAccessControl</td>
       <td style="text-align:right">-</td>
    </tr>
    <tr>
      <td>UpdatePublicKey</td>
       <td style="text-align:right">-</td>
    </tr>
    <tr>
      <td>UpdateRealtimeLogConfig</td>
       <td style="text-align:right">-</td>
    </tr>
    <tr>
      <td>UpdateResponseHeadersPolicy</td>
       <td style="text-align:right">-</td>
    </tr>
    <tr>
      <td>UpdateStreamingDistribution</td>
       <td style="text-align:right">-</td>
    </tr>
  </tbody>
 </table>


## cloudtrail ##

<table>
  <thead>
    <tr>
      <th>Operation</th>
      <th style="text-align:right">Implemented</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td>AddTags (Pro) </td>
       <td style="text-align:right">✅</td>
    </tr>
    <tr>
      <td>CreateTrail (Pro)  <a href="#misc" title="covered by our integration test suite">✨</a></td>
       <td style="text-align:right">✅</td>
    </tr>
    <tr>
      <td>DeleteTrail (Pro)  <a href="#misc" title="covered by our integration test suite">✨</a></td>
       <td style="text-align:right">✅</td>
    </tr>
    <tr>
      <td>DescribeTrails (Pro)  <a href="#misc" title="covered by our integration test suite">✨</a></td>
       <td style="text-align:right">✅</td>
    </tr>
    <tr>
      <td>GetEventSelectors (Pro) </td>
       <td style="text-align:right">✅</td>
    </tr>
    <tr>
      <td>GetInsightSelectors (Pro) </td>
       <td style="text-align:right">✅</td>
    </tr>
    <tr>
      <td>GetTrail (Pro)  <a href="#misc" title="covered by our integration test suite">✨</a></td>
       <td style="text-align:right">✅</td>
    </tr>
    <tr>
      <td>GetTrailStatus (Pro)  <a href="#misc" title="covered by our integration test suite">✨</a></td>
       <td style="text-align:right">✅</td>
    </tr>
    <tr>
      <td>ListTags (Pro)  <a href="#misc" title="covered by our integration test suite">✨</a></td>
       <td style="text-align:right">✅</td>
    </tr>
    <tr>
      <td>ListTrails (Pro)  <a href="#misc" title="covered by our integration test suite">✨</a></td>
       <td style="text-align:right">✅</td>
    </tr>
    <tr>
      <td>LookupEvents (Pro)  <a href="#misc" title="covered by our integration test suite">✨</a></td>
       <td style="text-align:right">✅</td>
    </tr>
    <tr>
      <td>PutEventSelectors (Pro)  <a href="#misc" title="covered by our integration test suite">✨</a></td>
       <td style="text-align:right">✅</td>
    </tr>
    <tr>
      <td>PutInsightSelectors (Pro) </td>
       <td style="text-align:right">✅</td>
    </tr>
    <tr>
      <td>RemoveTags (Pro) </td>
       <td style="text-align:right">✅</td>
    </tr>
    <tr>
      <td>StartLogging (Pro)  <a href="#misc" title="covered by our integration test suite">✨</a></td>
       <td style="text-align:right">✅</td>
    </tr>
    <tr>
      <td>StopLogging (Pro)  <a href="#misc" title="covered by our integration test suite">✨</a></td>
       <td style="text-align:right">✅</td>
    </tr>
    <tr>
      <td>UpdateTrail (Pro)  <a href="#misc" title="covered by our integration test suite">✨</a></td>
       <td style="text-align:right">✅</td>
    </tr>
  </tbody>
  <tbody>    <tr>
      <td><a data-toggle="collapse" href=".cloudtrail-notimplemented">Show missing</a></td>
      <td style="text-align:right"></td>
    </tr>
  </tbody>
  <tbody class="collapse cloudtrail-notimplemented">     <tr>
      <td>CancelQuery</td>
       <td style="text-align:right">-</td>
    </tr>
    <tr>
      <td>CreateEventDataStore</td>
       <td style="text-align:right">-</td>
    </tr>
    <tr>
      <td>DeleteEventDataStore</td>
       <td style="text-align:right">-</td>
    </tr>
    <tr>
      <td>DescribeQuery</td>
       <td style="text-align:right">-</td>
    </tr>
    <tr>
      <td>GetChannel</td>
       <td style="text-align:right">-</td>
    </tr>
    <tr>
      <td>GetEventDataStore</td>
       <td style="text-align:right">-</td>
    </tr>
    <tr>
      <td>GetImport</td>
       <td style="text-align:right">-</td>
    </tr>
    <tr>
      <td>GetQueryResults</td>
       <td style="text-align:right">-</td>
    </tr>
    <tr>
      <td>ListChannels</td>
       <td style="text-align:right">-</td>
    </tr>
    <tr>
      <td>ListEventDataStores</td>
       <td style="text-align:right">-</td>
    </tr>
    <tr>
      <td>ListImportFailures</td>
       <td style="text-align:right">-</td>
    </tr>
    <tr>
      <td>ListImports</td>
       <td style="text-align:right">-</td>
    </tr>
    <tr>
      <td>ListPublicKeys</td>
       <td style="text-align:right">-</td>
    </tr>
    <tr>
      <td>ListQueries</td>
       <td style="text-align:right">-</td>
    </tr>
    <tr>
      <td>RestoreEventDataStore</td>
       <td style="text-align:right">-</td>
    </tr>
    <tr>
      <td>StartImport</td>
       <td style="text-align:right">-</td>
    </tr>
    <tr>
      <td>StartQuery</td>
       <td style="text-align:right">-</td>
    </tr>
    <tr>
      <td>StopImport</td>
       <td style="text-align:right">-</td>
    </tr>
    <tr>
      <td>UpdateEventDataStore</td>
       <td style="text-align:right">-</td>
    </tr>
  </tbody>
 </table>


## cloudwatch ##

<table>
  <thead>
    <tr>
      <th>Operation</th>
      <th style="text-align:right">Implemented</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td>DeleteAlarms <a href="#misc" title="covered by our integration test suite">✨</a></td>
       <td style="text-align:right">✅</td>
    </tr>
    <tr>
      <td>DeleteDashboards</td>
       <td style="text-align:right">✅</td>
    </tr>
    <tr>
      <td>DescribeAlarms <a href="#misc" title="covered by our integration test suite">✨</a></td>
       <td style="text-align:right">✅</td>
    </tr>
    <tr>
      <td>DescribeAlarmsForMetric</td>
       <td style="text-align:right">✅</td>
    </tr>
    <tr>
      <td>DisableAlarmActions <a href="#misc" title="covered by our integration test suite">✨</a></td>
       <td style="text-align:right">✅</td>
    </tr>
    <tr>
      <td>EnableAlarmActions <a href="#misc" title="covered by our integration test suite">✨</a></td>
       <td style="text-align:right">✅</td>
    </tr>
    <tr>
      <td>GetDashboard</td>
       <td style="text-align:right">✅</td>
    </tr>
    <tr>
      <td>GetMetricData <a href="#misc" title="covered by our integration test suite">✨</a></td>
       <td style="text-align:right">✅</td>
    </tr>
    <tr>
      <td>GetMetricStatistics <a href="#misc" title="covered by our integration test suite">✨</a></td>
       <td style="text-align:right">✅</td>
    </tr>
    <tr>
      <td>ListDashboards</td>
       <td style="text-align:right">✅</td>
    </tr>
    <tr>
      <td>ListMetrics <a href="#misc" title="covered by our integration test suite">✨</a></td>
       <td style="text-align:right">✅</td>
    </tr>
    <tr>
      <td>ListTagsForResource <a href="#misc" title="covered by our integration test suite">✨</a></td>
       <td style="text-align:right">✅</td>
    </tr>
    <tr>
      <td>PutCompositeAlarm <a href="#misc" title="covered by our integration test suite">✨</a></td>
       <td style="text-align:right">✅</td>
    </tr>
    <tr>
      <td>PutDashboard</td>
       <td style="text-align:right">✅</td>
    </tr>
    <tr>
      <td>PutMetricAlarm <a href="#misc" title="covered by our integration test suite">✨</a></td>
       <td style="text-align:right">✅</td>
    </tr>
    <tr>
      <td>PutMetricData <a href="#misc" title="covered by our integration test suite">✨</a></td>
       <td style="text-align:right">✅</td>
    </tr>
    <tr>
      <td>SetAlarmState <a href="#misc" title="covered by our integration test suite">✨</a></td>
       <td style="text-align:right">✅</td>
    </tr>
    <tr>
      <td>TagResource <a href="#misc" title="covered by our integration test suite">✨</a></td>
       <td style="text-align:right">✅</td>
    </tr>
    <tr>
      <td>UntagResource <a href="#misc" title="covered by our integration test suite">✨</a></td>
       <td style="text-align:right">✅</td>
    </tr>
  </tbody>
  <tbody>    <tr>
      <td><a data-toggle="collapse" href=".cloudwatch-notimplemented">Show missing</a></td>
      <td style="text-align:right"></td>
    </tr>
  </tbody>
  <tbody class="collapse cloudwatch-notimplemented">     <tr>
      <td>DeleteAnomalyDetector</td>
       <td style="text-align:right">-</td>
    </tr>
    <tr>
      <td>DeleteInsightRules</td>
       <td style="text-align:right">-</td>
    </tr>
    <tr>
      <td>DeleteMetricStream</td>
       <td style="text-align:right">-</td>
    </tr>
    <tr>
      <td>DescribeAlarmHistory</td>
       <td style="text-align:right">-</td>
    </tr>
    <tr>
      <td>DescribeAnomalyDetectors</td>
       <td style="text-align:right">-</td>
    </tr>
    <tr>
      <td>DescribeInsightRules</td>
       <td style="text-align:right">-</td>
    </tr>
    <tr>
      <td>DisableInsightRules</td>
       <td style="text-align:right">-</td>
    </tr>
    <tr>
      <td>EnableInsightRules</td>
       <td style="text-align:right">-</td>
    </tr>
    <tr>
      <td>GetInsightRuleReport</td>
       <td style="text-align:right">-</td>
    </tr>
    <tr>
      <td>GetMetricStream</td>
       <td style="text-align:right">-</td>
    </tr>
    <tr>
      <td>GetMetricWidgetImage</td>
       <td style="text-align:right">-</td>
    </tr>
    <tr>
      <td>ListManagedInsightRules</td>
       <td style="text-align:right">-</td>
    </tr>
    <tr>
      <td>ListMetricStreams</td>
       <td style="text-align:right">-</td>
    </tr>
    <tr>
      <td>PutAnomalyDetector</td>
       <td style="text-align:right">-</td>
    </tr>
    <tr>
      <td>PutInsightRule</td>
       <td style="text-align:right">-</td>
    </tr>
    <tr>
      <td>PutManagedInsightRules</td>
       <td style="text-align:right">-</td>
    </tr>
    <tr>
      <td>PutMetricStream</td>
       <td style="text-align:right">-</td>
    </tr>
    <tr>
      <td>StartMetricStreams</td>
       <td style="text-align:right">-</td>
    </tr>
    <tr>
      <td>StopMetricStreams</td>
       <td style="text-align:right">-</td>
    </tr>
  </tbody>
 </table>


## codecommit ##

<table>
  <thead>
    <tr>
      <th>Operation</th>
      <th style="text-align:right">Implemented</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td>CreateBranch (Pro)  <a href="#misc" title="covered by our integration test suite">✨</a></td>
       <td style="text-align:right">✅</td>
    </tr>
    <tr>
      <td>CreateCommit (Pro)  <a href="#misc" title="covered by our integration test suite">✨</a></td>
       <td style="text-align:right">✅</td>
    </tr>
    <tr>
      <td>CreatePullRequest (Pro)  <a href="#misc" title="covered by our integration test suite">✨</a></td>
       <td style="text-align:right">✅</td>
    </tr>
    <tr>
      <td>CreateRepository (Pro)  <a href="#misc" title="covered by our integration test suite">✨</a></td>
       <td style="text-align:right">✅</td>
    </tr>
    <tr>
      <td>DeleteBranch (Pro)  <a href="#misc" title="covered by our integration test suite">✨</a></td>
       <td style="text-align:right">✅</td>
    </tr>
    <tr>
      <td>DeleteRepository (Pro)  <a href="#misc" title="covered by our integration test suite">✨</a></td>
       <td style="text-align:right">✅</td>
    </tr>
    <tr>
      <td>GetBranch (Pro)  <a href="#misc" title="covered by our integration test suite">✨</a></td>
       <td style="text-align:right">✅</td>
    </tr>
    <tr>
      <td>GetFile (Pro)  <a href="#misc" title="covered by our integration test suite">✨</a></td>
       <td style="text-align:right">✅</td>
    </tr>
    <tr>
      <td>GetFolder (Pro)  <a href="#misc" title="covered by our integration test suite">✨</a></td>
       <td style="text-align:right">✅</td>
    </tr>
    <tr>
      <td>GetRepository (Pro)  <a href="#misc" title="covered by our integration test suite">✨</a></td>
       <td style="text-align:right">✅</td>
    </tr>
    <tr>
      <td>ListPullRequests (Pro)  <a href="#misc" title="covered by our integration test suite">✨</a></td>
       <td style="text-align:right">✅</td>
    </tr>
    <tr>
      <td>ListRepositories (Pro) </td>
       <td style="text-align:right">✅</td>
    </tr>
    <tr>
      <td>ListTagsForResource (Pro) </td>
       <td style="text-align:right">✅</td>
    </tr>
    <tr>
      <td>TagResource (Pro) </td>
       <td style="text-align:right">✅</td>
    </tr>
  </tbody>
  <tbody>    <tr>
      <td><a data-toggle="collapse" href=".codecommit-notimplemented">Show missing</a></td>
      <td style="text-align:right"></td>
    </tr>
  </tbody>
  <tbody class="collapse codecommit-notimplemented">     <tr>
      <td>AssociateApprovalRuleTemplateWithRepository</td>
       <td style="text-align:right">-</td>
    </tr>
    <tr>
      <td>BatchAssociateApprovalRuleTemplateWithRepositories</td>
       <td style="text-align:right">-</td>
    </tr>
    <tr>
      <td>BatchDescribeMergeConflicts</td>
       <td style="text-align:right">-</td>
    </tr>
    <tr>
      <td>BatchDisassociateApprovalRuleTemplateFromRepositories</td>
       <td style="text-align:right">-</td>
    </tr>
    <tr>
      <td>BatchGetCommits</td>
       <td style="text-align:right">-</td>
    </tr>
    <tr>
      <td>BatchGetRepositories</td>
       <td style="text-align:right">-</td>
    </tr>
    <tr>
      <td>CreateApprovalRuleTemplate</td>
       <td style="text-align:right">-</td>
    </tr>
    <tr>
      <td>CreatePullRequestApprovalRule</td>
       <td style="text-align:right">-</td>
    </tr>
    <tr>
      <td>CreateUnreferencedMergeCommit</td>
       <td style="text-align:right">-</td>
    </tr>
    <tr>
      <td>DeleteApprovalRuleTemplate</td>
       <td style="text-align:right">-</td>
    </tr>
    <tr>
      <td>DeleteCommentContent</td>
       <td style="text-align:right">-</td>
    </tr>
    <tr>
      <td>DeleteFile</td>
       <td style="text-align:right">-</td>
    </tr>
    <tr>
      <td>DeletePullRequestApprovalRule</td>
       <td style="text-align:right">-</td>
    </tr>
    <tr>
      <td>DescribeMergeConflicts</td>
       <td style="text-align:right">-</td>
    </tr>
    <tr>
      <td>DescribePullRequestEvents</td>
       <td style="text-align:right">-</td>
    </tr>
    <tr>
      <td>DisassociateApprovalRuleTemplateFromRepository</td>
       <td style="text-align:right">-</td>
    </tr>
    <tr>
      <td>EvaluatePullRequestApprovalRules</td>
       <td style="text-align:right">-</td>
    </tr>
    <tr>
      <td>GetApprovalRuleTemplate</td>
       <td style="text-align:right">-</td>
    </tr>
    <tr>
      <td>GetBlob</td>
       <td style="text-align:right">-</td>
    </tr>
    <tr>
      <td>GetComment</td>
       <td style="text-align:right">-</td>
    </tr>
    <tr>
      <td>GetCommentReactions</td>
       <td style="text-align:right">-</td>
    </tr>
    <tr>
      <td>GetCommentsForComparedCommit</td>
       <td style="text-align:right">-</td>
    </tr>
    <tr>
      <td>GetCommentsForPullRequest</td>
       <td style="text-align:right">-</td>
    </tr>
    <tr>
      <td>GetCommit</td>
       <td style="text-align:right">-</td>
    </tr>
    <tr>
      <td>GetDifferences</td>
       <td style="text-align:right">-</td>
    </tr>
    <tr>
      <td>GetMergeCommit</td>
       <td style="text-align:right">-</td>
    </tr>
    <tr>
      <td>GetMergeConflicts</td>
       <td style="text-align:right">-</td>
    </tr>
    <tr>
      <td>GetMergeOptions</td>
       <td style="text-align:right">-</td>
    </tr>
    <tr>
      <td>GetPullRequest</td>
       <td style="text-align:right">-</td>
    </tr>
    <tr>
      <td>GetPullRequestApprovalStates</td>
       <td style="text-align:right">-</td>
    </tr>
    <tr>
      <td>GetPullRequestOverrideState</td>
       <td style="text-align:right">-</td>
    </tr>
    <tr>
      <td>GetRepositoryTriggers</td>
       <td style="text-align:right">-</td>
    </tr>
    <tr>
      <td>ListApprovalRuleTemplates</td>
       <td style="text-align:right">-</td>
    </tr>
    <tr>
      <td>ListAssociatedApprovalRuleTemplatesForRepository</td>
       <td style="text-align:right">-</td>
    </tr>
    <tr>
      <td>ListBranches</td>
       <td style="text-align:right">-</td>
    </tr>
    <tr>
      <td>ListRepositoriesForApprovalRuleTemplate</td>
       <td style="text-align:right">-</td>
    </tr>
    <tr>
      <td>MergeBranchesByFastForward</td>
       <td style="text-align:right">-</td>
    </tr>
    <tr>
      <td>MergeBranchesBySquash</td>
       <td style="text-align:right">-</td>
    </tr>
    <tr>
      <td>MergeBranchesByThreeWay</td>
       <td style="text-align:right">-</td>
    </tr>
    <tr>
      <td>MergePullRequestByFastForward</td>
       <td style="text-align:right">-</td>
    </tr>
    <tr>
      <td>MergePullRequestBySquash</td>
       <td style="text-align:right">-</td>
    </tr>
    <tr>
      <td>MergePullRequestByThreeWay</td>
       <td style="text-align:right">-</td>
    </tr>
    <tr>
      <td>OverridePullRequestApprovalRules</td>
       <td style="text-align:right">-</td>
    </tr>
    <tr>
      <td>PostCommentForComparedCommit</td>
       <td style="text-align:right">-</td>
    </tr>
    <tr>
      <td>PostCommentForPullRequest</td>
       <td style="text-align:right">-</td>
    </tr>
    <tr>
      <td>PostCommentReply</td>
       <td style="text-align:right">-</td>
    </tr>
    <tr>
      <td>PutCommentReaction</td>
       <td style="text-align:right">-</td>
    </tr>
    <tr>
      <td>PutFile</td>
       <td style="text-align:right">-</td>
    </tr>
    <tr>
      <td>PutRepositoryTriggers</td>
       <td style="text-align:right">-</td>
    </tr>
    <tr>
      <td>TestRepositoryTriggers</td>
       <td style="text-align:right">-</td>
    </tr>
    <tr>
      <td>UntagResource</td>
       <td style="text-align:right">-</td>
    </tr>
    <tr>
      <td>UpdateApprovalRuleTemplateContent</td>
       <td style="text-align:right">-</td>
    </tr>
    <tr>
      <td>UpdateApprovalRuleTemplateDescription</td>
       <td style="text-align:right">-</td>
    </tr>
    <tr>
      <td>UpdateApprovalRuleTemplateName</td>
       <td style="text-align:right">-</td>
    </tr>
    <tr>
      <td>UpdateComment</td>
       <td style="text-align:right">-</td>
    </tr>
    <tr>
      <td>UpdateDefaultBranch</td>
       <td style="text-align:right">-</td>
    </tr>
    <tr>
      <td>UpdatePullRequestApprovalRuleContent</td>
       <td style="text-align:right">-</td>
    </tr>
    <tr>
      <td>UpdatePullRequestApprovalState</td>
       <td style="text-align:right">-</td>
    </tr>
    <tr>
      <td>UpdatePullRequestDescription</td>
       <td style="text-align:right">-</td>
    </tr>
    <tr>
      <td>UpdatePullRequestStatus</td>
       <td style="text-align:right">-</td>
    </tr>
    <tr>
      <td>UpdatePullRequestTitle</td>
       <td style="text-align:right">-</td>
    </tr>
    <tr>
      <td>UpdateRepositoryDescription</td>
       <td style="text-align:right">-</td>
    </tr>
    <tr>
      <td>UpdateRepositoryName</td>
       <td style="text-align:right">-</td>
    </tr>
  </tbody>
 </table>


## cognito-identity ##

<table>
  <thead>
    <tr>
      <th>Operation</th>
      <th style="text-align:right">Implemented</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td>CreateIdentityPool (Pro)  <a href="#misc" title="covered by our integration test suite">✨</a></td>
       <td style="text-align:right">✅</td>
    </tr>
    <tr>
      <td>DeleteIdentityPool (Pro)  <a href="#misc" title="covered by our integration test suite">✨</a></td>
       <td style="text-align:right">✅</td>
    </tr>
    <tr>
      <td>DescribeIdentityPool (Pro) </td>
       <td style="text-align:right">✅</td>
    </tr>
    <tr>
      <td>GetCredentialsForIdentity (Pro)  <a href="#misc" title="covered by our integration test suite">✨</a></td>
       <td style="text-align:right">✅</td>
    </tr>
    <tr>
      <td>GetId (Pro)  <a href="#misc" title="covered by our integration test suite">✨</a></td>
       <td style="text-align:right">✅</td>
    </tr>
    <tr>
      <td>GetIdentityPoolRoles (Pro)  <a href="#misc" title="covered by our integration test suite">✨</a></td>
       <td style="text-align:right">✅</td>
    </tr>
    <tr>
      <td>GetOpenIdToken (Pro) </td>
       <td style="text-align:right">✅</td>
    </tr>
    <tr>
      <td>GetOpenIdTokenForDeveloperIdentity (Pro) </td>
       <td style="text-align:right">✅</td>
    </tr>
    <tr>
      <td>ListIdentities (Pro) </td>
       <td style="text-align:right">✅</td>
    </tr>
    <tr>
      <td>ListIdentityPools (Pro)  <a href="#misc" title="covered by our integration test suite">✨</a></td>
       <td style="text-align:right">✅</td>
    </tr>
    <tr>
      <td>SetIdentityPoolRoles (Pro)  <a href="#misc" title="covered by our integration test suite">✨</a></td>
       <td style="text-align:right">✅</td>
    </tr>
    <tr>
      <td>UpdateIdentityPool (Pro) </td>
       <td style="text-align:right">✅</td>
    </tr>
  </tbody>
  <tbody>    <tr>
      <td><a data-toggle="collapse" href=".cognito-identity-notimplemented">Show missing</a></td>
      <td style="text-align:right"></td>
    </tr>
  </tbody>
  <tbody class="collapse cognito-identity-notimplemented">     <tr>
      <td>DeleteIdentities</td>
       <td style="text-align:right">-</td>
    </tr>
    <tr>
      <td>DescribeIdentity</td>
       <td style="text-align:right">-</td>
    </tr>
    <tr>
      <td>GetPrincipalTagAttributeMap</td>
       <td style="text-align:right">-</td>
    </tr>
    <tr>
      <td>ListTagsForResource</td>
       <td style="text-align:right">-</td>
    </tr>
    <tr>
      <td>LookupDeveloperIdentity</td>
       <td style="text-align:right">-</td>
    </tr>
    <tr>
      <td>MergeDeveloperIdentities</td>
       <td style="text-align:right">-</td>
    </tr>
    <tr>
      <td>SetPrincipalTagAttributeMap</td>
       <td style="text-align:right">-</td>
    </tr>
    <tr>
      <td>TagResource</td>
       <td style="text-align:right">-</td>
    </tr>
    <tr>
      <td>UnlinkDeveloperIdentity</td>
       <td style="text-align:right">-</td>
    </tr>
    <tr>
      <td>UnlinkIdentity</td>
       <td style="text-align:right">-</td>
    </tr>
    <tr>
      <td>UntagResource</td>
       <td style="text-align:right">-</td>
    </tr>
  </tbody>
 </table>


## cognito-idp ##

<table>
  <thead>
    <tr>
      <th>Operation</th>
      <th style="text-align:right">Implemented</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td>AddCustomAttributes (Pro)  <a href="#misc" title="covered by our integration test suite">✨</a></td>
       <td style="text-align:right">✅</td>
    </tr>
    <tr>
      <td>AdminAddUserToGroup (Pro)  <a href="#misc" title="covered by our integration test suite">✨</a></td>
       <td style="text-align:right">✅</td>
    </tr>
    <tr>
      <td>AdminConfirmSignUp (Pro)  <a href="#misc" title="covered by our integration test suite">✨</a></td>
       <td style="text-align:right">✅</td>
    </tr>
    <tr>
      <td>AdminCreateUser (Pro)  <a href="#misc" title="covered by our integration test suite">✨</a></td>
       <td style="text-align:right">✅</td>
    </tr>
    <tr>
      <td>AdminDeleteUser (Pro)  <a href="#misc" title="covered by our integration test suite">✨</a></td>
       <td style="text-align:right">✅</td>
    </tr>
    <tr>
      <td>AdminDeleteUserAttributes (Pro)  <a href="#misc" title="covered by our integration test suite">✨</a></td>
       <td style="text-align:right">✅</td>
    </tr>
    <tr>
      <td>AdminDisableUser (Pro)  <a href="#misc" title="covered by our integration test suite">✨</a></td>
       <td style="text-align:right">✅</td>
    </tr>
    <tr>
      <td>AdminEnableUser (Pro) </td>
       <td style="text-align:right">✅</td>
    </tr>
    <tr>
      <td>AdminGetUser (Pro)  <a href="#misc" title="covered by our integration test suite">✨</a></td>
       <td style="text-align:right">✅</td>
    </tr>
    <tr>
      <td>AdminInitiateAuth (Pro)  <a href="#misc" title="covered by our integration test suite">✨</a></td>
       <td style="text-align:right">✅</td>
    </tr>
    <tr>
      <td>AdminListGroupsForUser (Pro)  <a href="#misc" title="covered by our integration test suite">✨</a></td>
       <td style="text-align:right">✅</td>
    </tr>
    <tr>
      <td>AdminRemoveUserFromGroup (Pro) </td>
       <td style="text-align:right">✅</td>
    </tr>
    <tr>
      <td>AdminResetUserPassword (Pro) </td>
       <td style="text-align:right">✅</td>
    </tr>
    <tr>
      <td>AdminRespondToAuthChallenge (Pro)  <a href="#misc" title="covered by our integration test suite">✨</a></td>
       <td style="text-align:right">✅</td>
    </tr>
    <tr>
      <td>AdminSetUserMFAPreference (Pro)  <a href="#misc" title="covered by our integration test suite">✨</a></td>
       <td style="text-align:right">✅</td>
    </tr>
    <tr>
      <td>AdminSetUserPassword (Pro)  <a href="#misc" title="covered by our integration test suite">✨</a></td>
       <td style="text-align:right">✅</td>
    </tr>
    <tr>
      <td>AdminUpdateUserAttributes (Pro)  <a href="#misc" title="covered by our integration test suite">✨</a></td>
       <td style="text-align:right">✅</td>
    </tr>
    <tr>
      <td>AdminUserGlobalSignOut (Pro)  <a href="#misc" title="covered by our integration test suite">✨</a></td>
       <td style="text-align:right">✅</td>
    </tr>
    <tr>
      <td>ChangePassword (Pro)  <a href="#misc" title="covered by our integration test suite">✨</a></td>
       <td style="text-align:right">✅</td>
    </tr>
    <tr>
      <td>ConfirmDevice (Pro) </td>
       <td style="text-align:right">✅</td>
    </tr>
    <tr>
      <td>ConfirmForgotPassword (Pro)  <a href="#misc" title="covered by our integration test suite">✨</a></td>
       <td style="text-align:right">✅</td>
    </tr>
    <tr>
      <td>ConfirmSignUp (Pro) </td>
       <td style="text-align:right">✅</td>
    </tr>
    <tr>
      <td>CreateGroup (Pro)  <a href="#misc" title="covered by our integration test suite">✨</a></td>
       <td style="text-align:right">✅</td>
    </tr>
    <tr>
      <td>CreateIdentityProvider (Pro)  <a href="#misc" title="covered by our integration test suite">✨</a></td>
       <td style="text-align:right">✅</td>
    </tr>
    <tr>
      <td>CreateResourceServer (Pro)  <a href="#misc" title="covered by our integration test suite">✨</a></td>
       <td style="text-align:right">✅</td>
    </tr>
    <tr>
      <td>CreateUserPool (Pro)  <a href="#misc" title="covered by our integration test suite">✨</a></td>
       <td style="text-align:right">✅</td>
    </tr>
    <tr>
      <td>CreateUserPoolClient (Pro)  <a href="#misc" title="covered by our integration test suite">✨</a></td>
       <td style="text-align:right">✅</td>
    </tr>
    <tr>
      <td>CreateUserPoolDomain (Pro)  <a href="#misc" title="covered by our integration test suite">✨</a></td>
       <td style="text-align:right">✅</td>
    </tr>
    <tr>
      <td>DeleteGroup (Pro)  <a href="#misc" title="covered by our integration test suite">✨</a></td>
       <td style="text-align:right">✅</td>
    </tr>
    <tr>
      <td>DeleteIdentityProvider (Pro)  <a href="#misc" title="covered by our integration test suite">✨</a></td>
       <td style="text-align:right">✅</td>
    </tr>
    <tr>
      <td>DeleteResourceServer (Pro)  <a href="#misc" title="covered by our integration test suite">✨</a></td>
       <td style="text-align:right">✅</td>
    </tr>
    <tr>
      <td>DeleteUserAttributes (Pro)  <a href="#misc" title="covered by our integration test suite">✨</a></td>
       <td style="text-align:right">✅</td>
    </tr>
    <tr>
      <td>DeleteUserPool (Pro)  <a href="#misc" title="covered by our integration test suite">✨</a></td>
       <td style="text-align:right">✅</td>
    </tr>
    <tr>
      <td>DeleteUserPoolClient (Pro)  <a href="#misc" title="covered by our integration test suite">✨</a></td>
       <td style="text-align:right">✅</td>
    </tr>
    <tr>
      <td>DeleteUserPoolDomain (Pro)  <a href="#misc" title="covered by our integration test suite">✨</a></td>
       <td style="text-align:right">✅</td>
    </tr>
    <tr>
      <td>DescribeIdentityProvider (Pro)  <a href="#misc" title="covered by our integration test suite">✨</a></td>
       <td style="text-align:right">✅</td>
    </tr>
    <tr>
      <td>DescribeResourceServer (Pro)  <a href="#misc" title="covered by our integration test suite">✨</a></td>
       <td style="text-align:right">✅</td>
    </tr>
    <tr>
      <td>DescribeUserPool (Pro)  <a href="#misc" title="covered by our integration test suite">✨</a></td>
       <td style="text-align:right">✅</td>
    </tr>
    <tr>
      <td>DescribeUserPoolClient (Pro)  <a href="#misc" title="covered by our integration test suite">✨</a></td>
       <td style="text-align:right">✅</td>
    </tr>
    <tr>
      <td>DescribeUserPoolDomain (Pro)  <a href="#misc" title="covered by our integration test suite">✨</a></td>
       <td style="text-align:right">✅</td>
    </tr>
    <tr>
      <td>ForgotPassword (Pro)  <a href="#misc" title="covered by our integration test suite">✨</a></td>
       <td style="text-align:right">✅</td>
    </tr>
    <tr>
      <td>GetGroup (Pro) </td>
       <td style="text-align:right">✅</td>
    </tr>
    <tr>
      <td>GetSigningCertificate (Pro)  <a href="#misc" title="covered by our integration test suite">✨</a></td>
       <td style="text-align:right">✅</td>
    </tr>
    <tr>
      <td>GetUser (Pro)  <a href="#misc" title="covered by our integration test suite">✨</a></td>
       <td style="text-align:right">✅</td>
    </tr>
    <tr>
      <td>GetUserPoolMfaConfig (Pro)  <a href="#misc" title="covered by our integration test suite">✨</a></td>
       <td style="text-align:right">✅</td>
    </tr>
    <tr>
      <td>GlobalSignOut (Pro)  <a href="#misc" title="covered by our integration test suite">✨</a></td>
       <td style="text-align:right">✅</td>
    </tr>
    <tr>
      <td>InitiateAuth (Pro)  <a href="#misc" title="covered by our integration test suite">✨</a></td>
       <td style="text-align:right">✅</td>
    </tr>
    <tr>
      <td>ListGroups (Pro)  <a href="#misc" title="covered by our integration test suite">✨</a></td>
       <td style="text-align:right">✅</td>
    </tr>
    <tr>
      <td>ListIdentityProviders (Pro)  <a href="#misc" title="covered by our integration test suite">✨</a></td>
       <td style="text-align:right">✅</td>
    </tr>
    <tr>
      <td>ListResourceServers (Pro)  <a href="#misc" title="covered by our integration test suite">✨</a></td>
       <td style="text-align:right">✅</td>
    </tr>
    <tr>
      <td>ListTagsForResource (Pro)  <a href="#misc" title="covered by our integration test suite">✨</a></td>
       <td style="text-align:right">✅</td>
    </tr>
    <tr>
      <td>ListUserPoolClients (Pro)  <a href="#misc" title="covered by our integration test suite">✨</a></td>
       <td style="text-align:right">✅</td>
    </tr>
    <tr>
      <td>ListUserPools (Pro)  <a href="#misc" title="covered by our integration test suite">✨</a></td>
       <td style="text-align:right">✅</td>
    </tr>
    <tr>
      <td>ListUsers (Pro)  <a href="#misc" title="covered by our integration test suite">✨</a></td>
       <td style="text-align:right">✅</td>
    </tr>
    <tr>
      <td>ListUsersInGroup (Pro)  <a href="#misc" title="covered by our integration test suite">✨</a></td>
       <td style="text-align:right">✅</td>
    </tr>
    <tr>
      <td>RespondToAuthChallenge (Pro)  <a href="#misc" title="covered by our integration test suite">✨</a></td>
       <td style="text-align:right">✅</td>
    </tr>
    <tr>
      <td>SetUserMFAPreference (Pro)  <a href="#misc" title="covered by our integration test suite">✨</a></td>
       <td style="text-align:right">✅</td>
    </tr>
    <tr>
      <td>SetUserPoolMfaConfig (Pro)  <a href="#misc" title="covered by our integration test suite">✨</a></td>
       <td style="text-align:right">✅</td>
    </tr>
    <tr>
      <td>SignUp (Pro)  <a href="#misc" title="covered by our integration test suite">✨</a></td>
       <td style="text-align:right">✅</td>
    </tr>
    <tr>
      <td>TagResource (Pro)  <a href="#misc" title="covered by our integration test suite">✨</a></td>
       <td style="text-align:right">✅</td>
    </tr>
    <tr>
      <td>UntagResource (Pro)  <a href="#misc" title="covered by our integration test suite">✨</a></td>
       <td style="text-align:right">✅</td>
    </tr>
    <tr>
      <td>UpdateGroup (Pro) </td>
       <td style="text-align:right">✅</td>
    </tr>
    <tr>
      <td>UpdateIdentityProvider (Pro)  <a href="#misc" title="covered by our integration test suite">✨</a></td>
       <td style="text-align:right">✅</td>
    </tr>
    <tr>
      <td>UpdateResourceServer (Pro) </td>
       <td style="text-align:right">✅</td>
    </tr>
    <tr>
      <td>UpdateUserAttributes (Pro) </td>
       <td style="text-align:right">✅</td>
    </tr>
    <tr>
      <td>UpdateUserPool (Pro)  <a href="#misc" title="covered by our integration test suite">✨</a></td>
       <td style="text-align:right">✅</td>
    </tr>
    <tr>
      <td>UpdateUserPoolClient (Pro)  <a href="#misc" title="covered by our integration test suite">✨</a></td>
       <td style="text-align:right">✅</td>
    </tr>
    <tr>
      <td>UpdateUserPoolDomain (Pro) </td>
       <td style="text-align:right">✅</td>
    </tr>
  </tbody>
  <tbody>    <tr>
      <td><a data-toggle="collapse" href=".cognito-idp-notimplemented">Show missing</a></td>
      <td style="text-align:right"></td>
    </tr>
  </tbody>
  <tbody class="collapse cognito-idp-notimplemented">     <tr>
      <td>AdminDisableProviderForUser</td>
       <td style="text-align:right">-</td>
    </tr>
    <tr>
      <td>AdminForgetDevice</td>
       <td style="text-align:right">-</td>
    </tr>
    <tr>
      <td>AdminGetDevice</td>
       <td style="text-align:right">-</td>
    </tr>
    <tr>
      <td>AdminLinkProviderForUser</td>
       <td style="text-align:right">-</td>
    </tr>
    <tr>
      <td>AdminListDevices</td>
       <td style="text-align:right">-</td>
    </tr>
    <tr>
      <td>AdminListUserAuthEvents</td>
       <td style="text-align:right">-</td>
    </tr>
    <tr>
      <td>AdminSetUserSettings</td>
       <td style="text-align:right">-</td>
    </tr>
    <tr>
      <td>AdminUpdateAuthEventFeedback</td>
       <td style="text-align:right">-</td>
    </tr>
    <tr>
      <td>AdminUpdateDeviceStatus</td>
       <td style="text-align:right">-</td>
    </tr>
    <tr>
      <td>AssociateSoftwareToken</td>
       <td style="text-align:right">-</td>
    </tr>
    <tr>
      <td>CreateUserImportJob</td>
       <td style="text-align:right">-</td>
    </tr>
    <tr>
      <td>DeleteUser</td>
       <td style="text-align:right">-</td>
    </tr>
    <tr>
      <td>DescribeRiskConfiguration</td>
       <td style="text-align:right">-</td>
    </tr>
    <tr>
      <td>DescribeUserImportJob</td>
       <td style="text-align:right">-</td>
    </tr>
    <tr>
      <td>ForgetDevice</td>
       <td style="text-align:right">-</td>
    </tr>
    <tr>
      <td>GetCSVHeader</td>
       <td style="text-align:right">-</td>
    </tr>
    <tr>
      <td>GetDevice</td>
       <td style="text-align:right">-</td>
    </tr>
    <tr>
      <td>GetIdentityProviderByIdentifier</td>
       <td style="text-align:right">-</td>
    </tr>
    <tr>
      <td>GetUICustomization</td>
       <td style="text-align:right">-</td>
    </tr>
    <tr>
      <td>GetUserAttributeVerificationCode</td>
       <td style="text-align:right">-</td>
    </tr>
    <tr>
      <td>ListDevices</td>
       <td style="text-align:right">-</td>
    </tr>
    <tr>
      <td>ListUserImportJobs</td>
       <td style="text-align:right">-</td>
    </tr>
    <tr>
      <td>ResendConfirmationCode</td>
       <td style="text-align:right">-</td>
    </tr>
    <tr>
      <td>RevokeToken</td>
       <td style="text-align:right">-</td>
    </tr>
    <tr>
      <td>SetRiskConfiguration</td>
       <td style="text-align:right">-</td>
    </tr>
    <tr>
      <td>SetUICustomization</td>
       <td style="text-align:right">-</td>
    </tr>
    <tr>
      <td>SetUserSettings</td>
       <td style="text-align:right">-</td>
    </tr>
    <tr>
      <td>StartUserImportJob</td>
       <td style="text-align:right">-</td>
    </tr>
    <tr>
      <td>StopUserImportJob</td>
       <td style="text-align:right">-</td>
    </tr>
    <tr>
      <td>UpdateAuthEventFeedback</td>
       <td style="text-align:right">-</td>
    </tr>
    <tr>
      <td>UpdateDeviceStatus</td>
       <td style="text-align:right">-</td>
    </tr>
    <tr>
      <td>VerifySoftwareToken</td>
       <td style="text-align:right">-</td>
    </tr>
    <tr>
      <td>VerifyUserAttribute</td>
       <td style="text-align:right">-</td>
    </tr>
  </tbody>
 </table>


## config ##

<table>
  <thead>
    <tr>
      <th>Operation</th>
      <th style="text-align:right">Implemented</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td>BatchGetAggregateResourceConfig</td>
       <td style="text-align:right">✅</td>
    </tr>
    <tr>
      <td>BatchGetResourceConfig</td>
       <td style="text-align:right">✅</td>
    </tr>
    <tr>
      <td>DeleteAggregationAuthorization</td>
       <td style="text-align:right">✅</td>
    </tr>
    <tr>
      <td>DeleteConfigRule</td>
       <td style="text-align:right">✅</td>
    </tr>
    <tr>
      <td>DeleteConfigurationAggregator</td>
       <td style="text-align:right">✅</td>
    </tr>
    <tr>
      <td>DeleteConfigurationRecorder <a href="#misc" title="covered by our integration test suite">✨</a></td>
       <td style="text-align:right">✅</td>
    </tr>
    <tr>
      <td>DeleteDeliveryChannel <a href="#misc" title="covered by our integration test suite">✨</a></td>
       <td style="text-align:right">✅</td>
    </tr>
    <tr>
      <td>DeleteOrganizationConformancePack</td>
       <td style="text-align:right">✅</td>
    </tr>
    <tr>
      <td>DescribeAggregationAuthorizations</td>
       <td style="text-align:right">✅</td>
    </tr>
    <tr>
      <td>DescribeConfigRules</td>
       <td style="text-align:right">✅</td>
    </tr>
    <tr>
      <td>DescribeConfigurationAggregators</td>
       <td style="text-align:right">✅</td>
    </tr>
    <tr>
      <td>DescribeConfigurationRecorderStatus</td>
       <td style="text-align:right">✅</td>
    </tr>
    <tr>
      <td>DescribeConfigurationRecorders <a href="#misc" title="covered by our integration test suite">✨</a></td>
       <td style="text-align:right">✅</td>
    </tr>
    <tr>
      <td>DescribeDeliveryChannels <a href="#misc" title="covered by our integration test suite">✨</a></td>
       <td style="text-align:right">✅</td>
    </tr>
    <tr>
      <td>DescribeOrganizationConformancePackStatuses</td>
       <td style="text-align:right">✅</td>
    </tr>
    <tr>
      <td>DescribeOrganizationConformancePacks</td>
       <td style="text-align:right">✅</td>
    </tr>
    <tr>
      <td>GetOrganizationConformancePackDetailedStatus</td>
       <td style="text-align:right">✅</td>
    </tr>
    <tr>
      <td>GetResourceConfigHistory</td>
       <td style="text-align:right">✅</td>
    </tr>
    <tr>
      <td>ListAggregateDiscoveredResources</td>
       <td style="text-align:right">✅</td>
    </tr>
    <tr>
      <td>ListDiscoveredResources</td>
       <td style="text-align:right">✅</td>
    </tr>
    <tr>
      <td>ListTagsForResource</td>
       <td style="text-align:right">✅</td>
    </tr>
    <tr>
      <td>PutAggregationAuthorization</td>
       <td style="text-align:right">✅</td>
    </tr>
    <tr>
      <td>PutConfigRule</td>
       <td style="text-align:right">✅</td>
    </tr>
    <tr>
      <td>PutConfigurationAggregator</td>
       <td style="text-align:right">✅</td>
    </tr>
    <tr>
      <td>PutConfigurationRecorder <a href="#misc" title="covered by our integration test suite">✨</a></td>
       <td style="text-align:right">✅</td>
    </tr>
    <tr>
      <td>PutDeliveryChannel <a href="#misc" title="covered by our integration test suite">✨</a></td>
       <td style="text-align:right">✅</td>
    </tr>
    <tr>
      <td>PutEvaluations</td>
       <td style="text-align:right">✅</td>
    </tr>
    <tr>
      <td>PutOrganizationConformancePack</td>
       <td style="text-align:right">✅</td>
    </tr>
    <tr>
      <td>StartConfigurationRecorder</td>
       <td style="text-align:right">✅</td>
    </tr>
    <tr>
      <td>StopConfigurationRecorder</td>
       <td style="text-align:right">✅</td>
    </tr>
    <tr>
      <td>TagResource</td>
       <td style="text-align:right">✅</td>
    </tr>
    <tr>
      <td>UntagResource</td>
       <td style="text-align:right">✅</td>
    </tr>
  </tbody>
  <tbody>    <tr>
      <td><a data-toggle="collapse" href=".config-notimplemented">Show missing</a></td>
      <td style="text-align:right"></td>
    </tr>
  </tbody>
  <tbody class="collapse config-notimplemented">     <tr>
      <td>DeleteConformancePack</td>
       <td style="text-align:right">-</td>
    </tr>
    <tr>
      <td>DeleteEvaluationResults</td>
       <td style="text-align:right">-</td>
    </tr>
    <tr>
      <td>DeleteOrganizationConfigRule</td>
       <td style="text-align:right">-</td>
    </tr>
    <tr>
      <td>DeletePendingAggregationRequest</td>
       <td style="text-align:right">-</td>
    </tr>
    <tr>
      <td>DeleteRemediationConfiguration</td>
       <td style="text-align:right">-</td>
    </tr>
    <tr>
      <td>DeleteRemediationExceptions</td>
       <td style="text-align:right">-</td>
    </tr>
    <tr>
      <td>DeleteResourceConfig</td>
       <td style="text-align:right">-</td>
    </tr>
    <tr>
      <td>DeleteRetentionConfiguration</td>
       <td style="text-align:right">-</td>
    </tr>
    <tr>
      <td>DeleteStoredQuery</td>
       <td style="text-align:right">-</td>
    </tr>
    <tr>
      <td>DeliverConfigSnapshot</td>
       <td style="text-align:right">-</td>
    </tr>
    <tr>
      <td>DescribeAggregateComplianceByConfigRules</td>
       <td style="text-align:right">-</td>
    </tr>
    <tr>
      <td>DescribeAggregateComplianceByConformancePacks</td>
       <td style="text-align:right">-</td>
    </tr>
    <tr>
      <td>DescribeComplianceByConfigRule</td>
       <td style="text-align:right">-</td>
    </tr>
    <tr>
      <td>DescribeComplianceByResource</td>
       <td style="text-align:right">-</td>
    </tr>
    <tr>
      <td>DescribeConfigRuleEvaluationStatus</td>
       <td style="text-align:right">-</td>
    </tr>
    <tr>
      <td>DescribeConfigurationAggregatorSourcesStatus</td>
       <td style="text-align:right">-</td>
    </tr>
    <tr>
      <td>DescribeConformancePackCompliance</td>
       <td style="text-align:right">-</td>
    </tr>
    <tr>
      <td>DescribeConformancePackStatus</td>
       <td style="text-align:right">-</td>
    </tr>
    <tr>
      <td>DescribeConformancePacks</td>
       <td style="text-align:right">-</td>
    </tr>
    <tr>
      <td>DescribeDeliveryChannelStatus</td>
       <td style="text-align:right">-</td>
    </tr>
    <tr>
      <td>DescribeOrganizationConfigRuleStatuses</td>
       <td style="text-align:right">-</td>
    </tr>
    <tr>
      <td>DescribeOrganizationConfigRules</td>
       <td style="text-align:right">-</td>
    </tr>
    <tr>
      <td>DescribePendingAggregationRequests</td>
       <td style="text-align:right">-</td>
    </tr>
    <tr>
      <td>DescribeRemediationConfigurations</td>
       <td style="text-align:right">-</td>
    </tr>
    <tr>
      <td>DescribeRemediationExceptions</td>
       <td style="text-align:right">-</td>
    </tr>
    <tr>
      <td>DescribeRemediationExecutionStatus</td>
       <td style="text-align:right">-</td>
    </tr>
    <tr>
      <td>DescribeRetentionConfigurations</td>
       <td style="text-align:right">-</td>
    </tr>
    <tr>
      <td>GetAggregateComplianceDetailsByConfigRule</td>
       <td style="text-align:right">-</td>
    </tr>
    <tr>
      <td>GetAggregateConfigRuleComplianceSummary</td>
       <td style="text-align:right">-</td>
    </tr>
    <tr>
      <td>GetAggregateConformancePackComplianceSummary</td>
       <td style="text-align:right">-</td>
    </tr>
    <tr>
      <td>GetAggregateDiscoveredResourceCounts</td>
       <td style="text-align:right">-</td>
    </tr>
    <tr>
      <td>GetAggregateResourceConfig</td>
       <td style="text-align:right">-</td>
    </tr>
    <tr>
      <td>GetComplianceDetailsByConfigRule</td>
       <td style="text-align:right">-</td>
    </tr>
    <tr>
      <td>GetComplianceDetailsByResource</td>
       <td style="text-align:right">-</td>
    </tr>
    <tr>
      <td>GetComplianceSummaryByConfigRule</td>
       <td style="text-align:right">-</td>
    </tr>
    <tr>
      <td>GetComplianceSummaryByResourceType</td>
       <td style="text-align:right">-</td>
    </tr>
    <tr>
      <td>GetConformancePackComplianceDetails</td>
       <td style="text-align:right">-</td>
    </tr>
    <tr>
      <td>GetConformancePackComplianceSummary</td>
       <td style="text-align:right">-</td>
    </tr>
    <tr>
      <td>GetCustomRulePolicy</td>
       <td style="text-align:right">-</td>
    </tr>
    <tr>
      <td>GetDiscoveredResourceCounts</td>
       <td style="text-align:right">-</td>
    </tr>
    <tr>
      <td>GetOrganizationConfigRuleDetailedStatus</td>
       <td style="text-align:right">-</td>
    </tr>
    <tr>
      <td>GetOrganizationCustomRulePolicy</td>
       <td style="text-align:right">-</td>
    </tr>
    <tr>
      <td>GetStoredQuery</td>
       <td style="text-align:right">-</td>
    </tr>
    <tr>
      <td>ListConformancePackComplianceScores</td>
       <td style="text-align:right">-</td>
    </tr>
    <tr>
      <td>ListStoredQueries</td>
       <td style="text-align:right">-</td>
    </tr>
    <tr>
      <td>PutConformancePack</td>
       <td style="text-align:right">-</td>
    </tr>
    <tr>
      <td>PutExternalEvaluation</td>
       <td style="text-align:right">-</td>
    </tr>
    <tr>
      <td>PutOrganizationConfigRule</td>
       <td style="text-align:right">-</td>
    </tr>
    <tr>
      <td>PutRemediationConfigurations</td>
       <td style="text-align:right">-</td>
    </tr>
    <tr>
      <td>PutRemediationExceptions</td>
       <td style="text-align:right">-</td>
    </tr>
    <tr>
      <td>PutResourceConfig</td>
       <td style="text-align:right">-</td>
    </tr>
    <tr>
      <td>PutRetentionConfiguration</td>
       <td style="text-align:right">-</td>
    </tr>
    <tr>
      <td>PutStoredQuery</td>
       <td style="text-align:right">-</td>
    </tr>
    <tr>
      <td>SelectAggregateResourceConfig</td>
       <td style="text-align:right">-</td>
    </tr>
    <tr>
      <td>SelectResourceConfig</td>
       <td style="text-align:right">-</td>
    </tr>
    <tr>
      <td>StartConfigRulesEvaluation</td>
       <td style="text-align:right">-</td>
    </tr>
    <tr>
      <td>StartRemediationExecution</td>
       <td style="text-align:right">-</td>
    </tr>
  </tbody>
 </table>


## docdb ##

<table>
  <thead>
    <tr>
      <th>Operation</th>
      <th style="text-align:right">Implemented</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td>AddTagsToResource (Pro) </td>
       <td style="text-align:right">✅</td>
    </tr>
    <tr>
      <td>CopyDBClusterSnapshot (Pro) </td>
       <td style="text-align:right">✅</td>
    </tr>
    <tr>
      <td>CreateDBCluster (Pro) </td>
       <td style="text-align:right">✅</td>
    </tr>
    <tr>
      <td>CreateDBClusterParameterGroup (Pro) </td>
       <td style="text-align:right">✅</td>
    </tr>
    <tr>
      <td>CreateDBClusterSnapshot (Pro) </td>
       <td style="text-align:right">✅</td>
    </tr>
    <tr>
      <td>CreateDBInstance (Pro) </td>
       <td style="text-align:right">✅</td>
    </tr>
    <tr>
      <td>CreateDBSubnetGroup (Pro) </td>
       <td style="text-align:right">✅</td>
    </tr>
    <tr>
      <td>CreateEventSubscription (Pro) </td>
       <td style="text-align:right">✅</td>
    </tr>
    <tr>
      <td>DeleteDBCluster (Pro) </td>
       <td style="text-align:right">✅</td>
    </tr>
    <tr>
      <td>DeleteDBClusterParameterGroup (Pro) </td>
       <td style="text-align:right">✅</td>
    </tr>
    <tr>
      <td>DeleteDBClusterSnapshot (Pro) </td>
       <td style="text-align:right">✅</td>
    </tr>
    <tr>
      <td>DeleteDBInstance (Pro) </td>
       <td style="text-align:right">✅</td>
    </tr>
    <tr>
      <td>DeleteDBSubnetGroup (Pro) </td>
       <td style="text-align:right">✅</td>
    </tr>
    <tr>
      <td>DeleteEventSubscription (Pro) </td>
       <td style="text-align:right">✅</td>
    </tr>
    <tr>
      <td>DescribeCertificates (Pro) </td>
       <td style="text-align:right">✅</td>
    </tr>
    <tr>
      <td>DescribeDBClusterParameterGroups (Pro) </td>
       <td style="text-align:right">✅</td>
    </tr>
    <tr>
      <td>DescribeDBClusterParameters (Pro) </td>
       <td style="text-align:right">✅</td>
    </tr>
    <tr>
      <td>DescribeDBClusterSnapshots (Pro) </td>
       <td style="text-align:right">✅</td>
    </tr>
    <tr>
      <td>DescribeDBClusters (Pro) </td>
       <td style="text-align:right">✅</td>
    </tr>
    <tr>
      <td>DescribeDBEngineVersions (Pro) </td>
       <td style="text-align:right">✅</td>
    </tr>
    <tr>
      <td>DescribeDBInstances (Pro) </td>
       <td style="text-align:right">✅</td>
    </tr>
    <tr>
      <td>DescribeDBSubnetGroups (Pro) </td>
       <td style="text-align:right">✅</td>
    </tr>
    <tr>
      <td>DescribeEventSubscriptions (Pro) </td>
       <td style="text-align:right">✅</td>
    </tr>
    <tr>
      <td>DescribeGlobalClusters (Pro) </td>
       <td style="text-align:right">✅</td>
    </tr>
    <tr>
      <td>ListTagsForResource (Pro) </td>
       <td style="text-align:right">✅</td>
    </tr>
    <tr>
      <td>ModifyDBCluster (Pro) </td>
       <td style="text-align:right">✅</td>
    </tr>
    <tr>
      <td>ModifyDBClusterParameterGroup (Pro) </td>
       <td style="text-align:right">✅</td>
    </tr>
    <tr>
      <td>ModifyDBInstance (Pro) </td>
       <td style="text-align:right">✅</td>
    </tr>
    <tr>
      <td>ModifyDBSubnetGroup (Pro) </td>
       <td style="text-align:right">✅</td>
    </tr>
    <tr>
      <td>RebootDBInstance (Pro) </td>
       <td style="text-align:right">✅</td>
    </tr>
    <tr>
      <td>RemoveTagsFromResource (Pro) </td>
       <td style="text-align:right">✅</td>
    </tr>
    <tr>
      <td>ResetDBClusterParameterGroup (Pro) </td>
       <td style="text-align:right">✅</td>
    </tr>
    <tr>
      <td>RestoreDBClusterFromSnapshot (Pro) </td>
       <td style="text-align:right">✅</td>
    </tr>
    <tr>
      <td>StartDBCluster (Pro) </td>
       <td style="text-align:right">✅</td>
    </tr>
    <tr>
      <td>StopDBCluster (Pro) </td>
       <td style="text-align:right">✅</td>
    </tr>
  </tbody>
  <tbody>    <tr>
      <td><a data-toggle="collapse" href=".docdb-notimplemented">Show missing</a></td>
      <td style="text-align:right"></td>
    </tr>
  </tbody>
  <tbody class="collapse docdb-notimplemented">     <tr>
      <td>AddSourceIdentifierToSubscription</td>
       <td style="text-align:right">-</td>
    </tr>
    <tr>
      <td>ApplyPendingMaintenanceAction</td>
       <td style="text-align:right">-</td>
    </tr>
    <tr>
      <td>CopyDBClusterParameterGroup</td>
       <td style="text-align:right">-</td>
    </tr>
    <tr>
      <td>CreateGlobalCluster</td>
       <td style="text-align:right">-</td>
    </tr>
    <tr>
      <td>DeleteGlobalCluster</td>
       <td style="text-align:right">-</td>
    </tr>
    <tr>
      <td>DescribeDBClusterSnapshotAttributes</td>
       <td style="text-align:right">-</td>
    </tr>
    <tr>
      <td>DescribeEngineDefaultClusterParameters</td>
       <td style="text-align:right">-</td>
    </tr>
    <tr>
      <td>DescribeEventCategories</td>
       <td style="text-align:right">-</td>
    </tr>
    <tr>
      <td>DescribeEvents</td>
       <td style="text-align:right">-</td>
    </tr>
    <tr>
      <td>DescribeOrderableDBInstanceOptions</td>
       <td style="text-align:right">-</td>
    </tr>
    <tr>
      <td>DescribePendingMaintenanceActions</td>
       <td style="text-align:right">-</td>
    </tr>
    <tr>
      <td>FailoverDBCluster</td>
       <td style="text-align:right">-</td>
    </tr>
    <tr>
      <td>ModifyDBClusterSnapshotAttribute</td>
       <td style="text-align:right">-</td>
    </tr>
    <tr>
      <td>ModifyEventSubscription</td>
       <td style="text-align:right">-</td>
    </tr>
    <tr>
      <td>ModifyGlobalCluster</td>
       <td style="text-align:right">-</td>
    </tr>
    <tr>
      <td>RemoveFromGlobalCluster</td>
       <td style="text-align:right">-</td>
    </tr>
    <tr>
      <td>RemoveSourceIdentifierFromSubscription</td>
       <td style="text-align:right">-</td>
    </tr>
    <tr>
      <td>RestoreDBClusterToPointInTime</td>
       <td style="text-align:right">-</td>
    </tr>
  </tbody>
 </table>


## dynamodb ##

<table>
  <thead>
    <tr>
      <th>Operation</th>
      <th style="text-align:right">Implemented</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td>BatchExecuteStatement <a href="#misc" title="covered by our integration test suite">✨</a></td>
       <td style="text-align:right">✅</td>
    </tr>
    <tr>
      <td>BatchGetItem <a href="#misc" title="covered by our integration test suite">✨</a></td>
       <td style="text-align:right">✅</td>
    </tr>
    <tr>
      <td>BatchWriteItem <a href="#misc" title="covered by our integration test suite">✨</a></td>
       <td style="text-align:right">✅</td>
    </tr>
    <tr>
      <td>CreateBackup (Pro)  <a href="#misc" title="covered by our integration test suite">✨</a></td>
       <td style="text-align:right">✅</td>
    </tr>
    <tr>
      <td>CreateGlobalTable <a href="#misc" title="covered by our integration test suite">✨</a></td>
       <td style="text-align:right">✅</td>
    </tr>
    <tr>
      <td>CreateTable <a href="#misc" title="covered by our integration test suite">✨</a></td>
       <td style="text-align:right">✅</td>
    </tr>
    <tr>
      <td>DeleteBackup (Pro)  <a href="#misc" title="covered by our integration test suite">✨</a></td>
       <td style="text-align:right">✅</td>
    </tr>
    <tr>
      <td>DeleteItem <a href="#misc" title="covered by our integration test suite">✨</a></td>
       <td style="text-align:right">✅</td>
    </tr>
    <tr>
      <td>DeleteTable <a href="#misc" title="covered by our integration test suite">✨</a></td>
       <td style="text-align:right">✅</td>
    </tr>
    <tr>
      <td>DescribeGlobalTable <a href="#misc" title="covered by our integration test suite">✨</a></td>
       <td style="text-align:right">✅</td>
    </tr>
    <tr>
      <td>DescribeKinesisStreamingDestination <a href="#misc" title="covered by our integration test suite">✨</a></td>
       <td style="text-align:right">✅</td>
    </tr>
    <tr>
      <td>DescribeLimits</td>
       <td style="text-align:right">✅</td>
    </tr>
    <tr>
      <td>DescribeTable <a href="#misc" title="covered by our integration test suite">✨</a></td>
       <td style="text-align:right">✅</td>
    </tr>
    <tr>
      <td>DescribeTimeToLive <a href="#misc" title="covered by our integration test suite">✨</a></td>
       <td style="text-align:right">✅</td>
    </tr>
    <tr>
      <td>DisableKinesisStreamingDestination <a href="#misc" title="covered by our integration test suite">✨</a></td>
       <td style="text-align:right">✅</td>
    </tr>
    <tr>
      <td>EnableKinesisStreamingDestination <a href="#misc" title="covered by our integration test suite">✨</a></td>
       <td style="text-align:right">✅</td>
    </tr>
    <tr>
      <td>ExecuteStatement <a href="#misc" title="covered by our integration test suite">✨</a></td>
       <td style="text-align:right">✅</td>
    </tr>
    <tr>
      <td>ExecuteTransaction <a href="#misc" title="covered by our integration test suite">✨</a></td>
       <td style="text-align:right">✅</td>
    </tr>
    <tr>
      <td>GetItem <a href="#misc" title="covered by our integration test suite">✨</a></td>
       <td style="text-align:right">✅</td>
    </tr>
    <tr>
      <td>ListBackups (Pro) </td>
       <td style="text-align:right">✅</td>
    </tr>
    <tr>
      <td>ListGlobalTables</td>
       <td style="text-align:right">✅</td>
    </tr>
    <tr>
      <td>ListTables <a href="#misc" title="covered by our integration test suite">✨</a></td>
       <td style="text-align:right">✅</td>
    </tr>
    <tr>
      <td>ListTagsOfResource <a href="#misc" title="covered by our integration test suite">✨</a></td>
       <td style="text-align:right">✅</td>
    </tr>
    <tr>
      <td>PutItem <a href="#misc" title="covered by our integration test suite">✨</a></td>
       <td style="text-align:right">✅</td>
    </tr>
    <tr>
      <td>Query <a href="#misc" title="covered by our integration test suite">✨</a></td>
       <td style="text-align:right">✅</td>
    </tr>
    <tr>
      <td>RestoreTableFromBackup (Pro)  <a href="#misc" title="covered by our integration test suite">✨</a></td>
       <td style="text-align:right">✅</td>
    </tr>
    <tr>
      <td>Scan <a href="#misc" title="covered by our integration test suite">✨</a></td>
       <td style="text-align:right">✅</td>
    </tr>
    <tr>
      <td>TagResource <a href="#misc" title="covered by our integration test suite">✨</a></td>
       <td style="text-align:right">✅</td>
    </tr>
    <tr>
      <td>TransactGetItems <a href="#misc" title="covered by our integration test suite">✨</a></td>
       <td style="text-align:right">✅</td>
    </tr>
    <tr>
      <td>TransactWriteItems <a href="#misc" title="covered by our integration test suite">✨</a></td>
       <td style="text-align:right">✅</td>
    </tr>
    <tr>
      <td>UntagResource <a href="#misc" title="covered by our integration test suite">✨</a></td>
       <td style="text-align:right">✅</td>
    </tr>
    <tr>
      <td>UpdateGlobalTable <a href="#misc" title="covered by our integration test suite">✨</a></td>
       <td style="text-align:right">✅</td>
    </tr>
    <tr>
      <td>UpdateItem <a href="#misc" title="covered by our integration test suite">✨</a></td>
       <td style="text-align:right">✅</td>
    </tr>
    <tr>
      <td>UpdateTable <a href="#misc" title="covered by our integration test suite">✨</a></td>
       <td style="text-align:right">✅</td>
    </tr>
    <tr>
      <td>UpdateTimeToLive <a href="#misc" title="covered by our integration test suite">✨</a></td>
       <td style="text-align:right">✅</td>
    </tr>
  </tbody>
  <tbody>    <tr>
      <td><a data-toggle="collapse" href=".dynamodb-notimplemented">Show missing</a></td>
      <td style="text-align:right"></td>
    </tr>
  </tbody>
  <tbody class="collapse dynamodb-notimplemented">     <tr>
      <td>DescribeBackup</td>
       <td style="text-align:right">-</td>
    </tr>
    <tr>
      <td>DescribeContinuousBackups</td>
       <td style="text-align:right">-</td>
    </tr>
    <tr>
      <td>DescribeContributorInsights</td>
       <td style="text-align:right">-</td>
    </tr>
    <tr>
      <td>DescribeEndpoints</td>
       <td style="text-align:right">-</td>
    </tr>
    <tr>
      <td>DescribeExport</td>
       <td style="text-align:right">-</td>
    </tr>
    <tr>
      <td>DescribeGlobalTableSettings</td>
       <td style="text-align:right">-</td>
    </tr>
    <tr>
      <td>DescribeImport</td>
       <td style="text-align:right">-</td>
    </tr>
    <tr>
      <td>DescribeTableReplicaAutoScaling</td>
       <td style="text-align:right">-</td>
    </tr>
    <tr>
      <td>ExportTableToPointInTime</td>
       <td style="text-align:right">-</td>
    </tr>
    <tr>
      <td>ImportTable</td>
       <td style="text-align:right">-</td>
    </tr>
    <tr>
      <td>ListContributorInsights</td>
       <td style="text-align:right">-</td>
    </tr>
    <tr>
      <td>ListExports</td>
       <td style="text-align:right">-</td>
    </tr>
    <tr>
      <td>ListImports</td>
       <td style="text-align:right">-</td>
    </tr>
    <tr>
      <td>RestoreTableToPointInTime</td>
       <td style="text-align:right">-</td>
    </tr>
    <tr>
      <td>UpdateContinuousBackups</td>
       <td style="text-align:right">-</td>
    </tr>
    <tr>
      <td>UpdateContributorInsights</td>
       <td style="text-align:right">-</td>
    </tr>
    <tr>
      <td>UpdateGlobalTableSettings</td>
       <td style="text-align:right">-</td>
    </tr>
    <tr>
      <td>UpdateTableReplicaAutoScaling</td>
       <td style="text-align:right">-</td>
    </tr>
  </tbody>
 </table>


## dynamodbstreams ##

<table>
  <thead>
    <tr>
      <th>Operation</th>
      <th style="text-align:right">Implemented</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td>DescribeStream <a href="#misc" title="covered by our integration test suite">✨</a></td>
       <td style="text-align:right">✅</td>
    </tr>
    <tr>
      <td>GetRecords <a href="#misc" title="covered by our integration test suite">✨</a></td>
       <td style="text-align:right">✅</td>
    </tr>
    <tr>
      <td>GetShardIterator <a href="#misc" title="covered by our integration test suite">✨</a></td>
       <td style="text-align:right">✅</td>
    </tr>
    <tr>
      <td>ListStreams <a href="#misc" title="covered by our integration test suite">✨</a></td>
       <td style="text-align:right">✅</td>
    </tr>
  </tbody>
 </table>


## ec2 ##

<table>
  <thead>
    <tr>
      <th>Operation</th>
      <th style="text-align:right">Implemented</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td>AcceptReservedInstancesExchangeQuote (Pro) </td>
       <td style="text-align:right">✅</td>
    </tr>
    <tr>
      <td>AcceptTransitGatewayMulticastDomainAssociations (Pro) </td>
       <td style="text-align:right">✅</td>
    </tr>
    <tr>
      <td>AcceptTransitGatewayPeeringAttachment</td>
       <td style="text-align:right">✅</td>
    </tr>
    <tr>
      <td>AcceptTransitGatewayVpcAttachment (Pro) </td>
       <td style="text-align:right">✅</td>
    </tr>
    <tr>
      <td>AcceptVpcEndpointConnections (Pro) </td>
       <td style="text-align:right">✅</td>
    </tr>
    <tr>
      <td>AcceptVpcPeeringConnection <a href="#misc" title="covered by our integration test suite">✨</a></td>
       <td style="text-align:right">✅</td>
    </tr>
    <tr>
      <td>AdvertiseByoipCidr (Pro) </td>
       <td style="text-align:right">✅</td>
    </tr>
    <tr>
      <td>AllocateAddress <a href="#misc" title="covered by our integration test suite">✨</a></td>
       <td style="text-align:right">✅</td>
    </tr>
    <tr>
      <td>AllocateHosts (Pro) </td>
       <td style="text-align:right">✅</td>
    </tr>
    <tr>
      <td>AllocateIpamPoolCidr (Pro) </td>
       <td style="text-align:right">✅</td>
    </tr>
    <tr>
      <td>AssignIpv6Addresses</td>
       <td style="text-align:right">✅</td>
    </tr>
    <tr>
      <td>AssignPrivateIpAddresses</td>
       <td style="text-align:right">✅</td>
    </tr>
    <tr>
      <td>AssociateAddress</td>
       <td style="text-align:right">✅</td>
    </tr>
    <tr>
      <td>AssociateDhcpOptions</td>
       <td style="text-align:right">✅</td>
    </tr>
    <tr>
      <td>AssociateIamInstanceProfile</td>
       <td style="text-align:right">✅</td>
    </tr>
    <tr>
      <td>AssociateRouteTable <a href="#misc" title="covered by our integration test suite">✨</a></td>
       <td style="text-align:right">✅</td>
    </tr>
    <tr>
      <td>AssociateSubnetCidrBlock</td>
       <td style="text-align:right">✅</td>
    </tr>
    <tr>
      <td>AssociateTransitGatewayRouteTable</td>
       <td style="text-align:right">✅</td>
    </tr>
    <tr>
      <td>AssociateVpcCidrBlock</td>
       <td style="text-align:right">✅</td>
    </tr>
    <tr>
      <td>AttachInternetGateway <a href="#misc" title="covered by our integration test suite">✨</a></td>
       <td style="text-align:right">✅</td>
    </tr>
    <tr>
      <td>AttachNetworkInterface</td>
       <td style="text-align:right">✅</td>
    </tr>
    <tr>
      <td>AttachVolume</td>
       <td style="text-align:right">✅</td>
    </tr>
    <tr>
      <td>AttachVpnGateway <a href="#misc" title="covered by our integration test suite">✨</a></td>
       <td style="text-align:right">✅</td>
    </tr>
    <tr>
      <td>AuthorizeSecurityGroupEgress <a href="#misc" title="covered by our integration test suite">✨</a></td>
       <td style="text-align:right">✅</td>
    </tr>
    <tr>
      <td>AuthorizeSecurityGroupIngress <a href="#misc" title="covered by our integration test suite">✨</a></td>
       <td style="text-align:right">✅</td>
    </tr>
    <tr>
      <td>CancelSpotFleetRequests</td>
       <td style="text-align:right">✅</td>
    </tr>
    <tr>
      <td>CancelSpotInstanceRequests</td>
       <td style="text-align:right">✅</td>
    </tr>
    <tr>
      <td>CopyImage</td>
       <td style="text-align:right">✅</td>
    </tr>
    <tr>
      <td>CopySnapshot</td>
       <td style="text-align:right">✅</td>
    </tr>
    <tr>
      <td>CreateCarrierGateway</td>
       <td style="text-align:right">✅</td>
    </tr>
    <tr>
      <td>CreateCustomerGateway</td>
       <td style="text-align:right">✅</td>
    </tr>
    <tr>
      <td>CreateDefaultVpc</td>
       <td style="text-align:right">✅</td>
    </tr>
    <tr>
      <td>CreateDhcpOptions</td>
       <td style="text-align:right">✅</td>
    </tr>
    <tr>
      <td>CreateEgressOnlyInternetGateway</td>
       <td style="text-align:right">✅</td>
    </tr>
    <tr>
      <td>CreateFleet</td>
       <td style="text-align:right">✅</td>
    </tr>
    <tr>
      <td>CreateFlowLogs</td>
       <td style="text-align:right">✅</td>
    </tr>
    <tr>
      <td>CreateImage <a href="#misc" title="covered by our integration test suite">✨</a></td>
       <td style="text-align:right">✅</td>
    </tr>
    <tr>
      <td>CreateInternetGateway <a href="#misc" title="covered by our integration test suite">✨</a></td>
       <td style="text-align:right">✅</td>
    </tr>
    <tr>
      <td>CreateKeyPair <a href="#misc" title="covered by our integration test suite">✨</a></td>
       <td style="text-align:right">✅</td>
    </tr>
    <tr>
      <td>CreateLaunchTemplate</td>
       <td style="text-align:right">✅</td>
    </tr>
    <tr>
      <td>CreateLaunchTemplateVersion</td>
       <td style="text-align:right">✅</td>
    </tr>
    <tr>
      <td>CreateManagedPrefixList</td>
       <td style="text-align:right">✅</td>
    </tr>
    <tr>
      <td>CreateNatGateway <a href="#misc" title="covered by our integration test suite">✨</a></td>
       <td style="text-align:right">✅</td>
    </tr>
    <tr>
      <td>CreateNetworkAcl</td>
       <td style="text-align:right">✅</td>
    </tr>
    <tr>
      <td>CreateNetworkAclEntry</td>
       <td style="text-align:right">✅</td>
    </tr>
    <tr>
      <td>CreateNetworkInterface</td>
       <td style="text-align:right">✅</td>
    </tr>
    <tr>
      <td>CreatePlacementGroup</td>
       <td style="text-align:right">✅</td>
    </tr>
    <tr>
      <td>CreateRoute <a href="#misc" title="covered by our integration test suite">✨</a></td>
       <td style="text-align:right">✅</td>
    </tr>
    <tr>
      <td>CreateRouteTable <a href="#misc" title="covered by our integration test suite">✨</a></td>
       <td style="text-align:right">✅</td>
    </tr>
    <tr>
      <td>CreateSecurityGroup <a href="#misc" title="covered by our integration test suite">✨</a></td>
       <td style="text-align:right">✅</td>
    </tr>
    <tr>
      <td>CreateSnapshot</td>
       <td style="text-align:right">✅</td>
    </tr>
    <tr>
      <td>CreateSnapshots</td>
       <td style="text-align:right">✅</td>
    </tr>
    <tr>
      <td>CreateSpotDatafeedSubscription</td>
       <td style="text-align:right">✅</td>
    </tr>
    <tr>
      <td>CreateSubnet <a href="#misc" title="covered by our integration test suite">✨</a></td>
       <td style="text-align:right">✅</td>
    </tr>
    <tr>
      <td>CreateTags <a href="#misc" title="covered by our integration test suite">✨</a></td>
       <td style="text-align:right">✅</td>
    </tr>
    <tr>
      <td>CreateTransitGateway</td>
       <td style="text-align:right">✅</td>
    </tr>
    <tr>
      <td>CreateTransitGatewayPeeringAttachment</td>
       <td style="text-align:right">✅</td>
    </tr>
    <tr>
      <td>CreateTransitGatewayRoute</td>
       <td style="text-align:right">✅</td>
    </tr>
    <tr>
      <td>CreateTransitGatewayRouteTable</td>
       <td style="text-align:right">✅</td>
    </tr>
    <tr>
      <td>CreateTransitGatewayVpcAttachment</td>
       <td style="text-align:right">✅</td>
    </tr>
    <tr>
      <td>CreateVolume</td>
       <td style="text-align:right">✅</td>
    </tr>
    <tr>
      <td>CreateVpc <a href="#misc" title="covered by our integration test suite">✨</a></td>
       <td style="text-align:right">✅</td>
    </tr>
    <tr>
      <td>CreateVpcEndpoint <a href="#misc" title="covered by our integration test suite">✨</a></td>
       <td style="text-align:right">✅</td>
    </tr>
    <tr>
      <td>CreateVpcEndpointServiceConfiguration</td>
       <td style="text-align:right">✅</td>
    </tr>
    <tr>
      <td>CreateVpcPeeringConnection <a href="#misc" title="covered by our integration test suite">✨</a></td>
       <td style="text-align:right">✅</td>
    </tr>
    <tr>
      <td>CreateVpnConnection</td>
       <td style="text-align:right">✅</td>
    </tr>
    <tr>
      <td>CreateVpnGateway <a href="#misc" title="covered by our integration test suite">✨</a></td>
       <td style="text-align:right">✅</td>
    </tr>
    <tr>
      <td>DeleteCarrierGateway</td>
       <td style="text-align:right">✅</td>
    </tr>
    <tr>
      <td>DeleteCustomerGateway</td>
       <td style="text-align:right">✅</td>
    </tr>
    <tr>
      <td>DeleteDhcpOptions</td>
       <td style="text-align:right">✅</td>
    </tr>
    <tr>
      <td>DeleteEgressOnlyInternetGateway</td>
       <td style="text-align:right">✅</td>
    </tr>
    <tr>
      <td>DeleteFleets</td>
       <td style="text-align:right">✅</td>
    </tr>
    <tr>
      <td>DeleteFlowLogs</td>
       <td style="text-align:right">✅</td>
    </tr>
    <tr>
      <td>DeleteInternetGateway</td>
       <td style="text-align:right">✅</td>
    </tr>
    <tr>
      <td>DeleteKeyPair</td>
       <td style="text-align:right">✅</td>
    </tr>
    <tr>
      <td>DeleteLaunchTemplate</td>
       <td style="text-align:right">✅</td>
    </tr>
    <tr>
      <td>DeleteManagedPrefixList</td>
       <td style="text-align:right">✅</td>
    </tr>
    <tr>
      <td>DeleteNatGateway <a href="#misc" title="covered by our integration test suite">✨</a></td>
       <td style="text-align:right">✅</td>
    </tr>
    <tr>
      <td>DeleteNetworkAcl</td>
       <td style="text-align:right">✅</td>
    </tr>
    <tr>
      <td>DeleteNetworkAclEntry</td>
       <td style="text-align:right">✅</td>
    </tr>
    <tr>
      <td>DeleteNetworkInterface</td>
       <td style="text-align:right">✅</td>
    </tr>
    <tr>
      <td>DeletePlacementGroup</td>
       <td style="text-align:right">✅</td>
    </tr>
    <tr>
      <td>DeleteRoute <a href="#misc" title="covered by our integration test suite">✨</a></td>
       <td style="text-align:right">✅</td>
    </tr>
    <tr>
      <td>DeleteRouteTable <a href="#misc" title="covered by our integration test suite">✨</a></td>
       <td style="text-align:right">✅</td>
    </tr>
    <tr>
      <td>DeleteSecurityGroup <a href="#misc" title="covered by our integration test suite">✨</a></td>
       <td style="text-align:right">✅</td>
    </tr>
    <tr>
      <td>DeleteSnapshot</td>
       <td style="text-align:right">✅</td>
    </tr>
    <tr>
      <td>DeleteSpotDatafeedSubscription</td>
       <td style="text-align:right">✅</td>
    </tr>
    <tr>
      <td>DeleteSubnet <a href="#misc" title="covered by our integration test suite">✨</a></td>
       <td style="text-align:right">✅</td>
    </tr>
    <tr>
      <td>DeleteTags</td>
       <td style="text-align:right">✅</td>
    </tr>
    <tr>
      <td>DeleteTransitGateway</td>
       <td style="text-align:right">✅</td>
    </tr>
    <tr>
      <td>DeleteTransitGatewayPeeringAttachment</td>
       <td style="text-align:right">✅</td>
    </tr>
    <tr>
      <td>DeleteTransitGatewayRoute</td>
       <td style="text-align:right">✅</td>
    </tr>
    <tr>
      <td>DeleteTransitGatewayRouteTable</td>
       <td style="text-align:right">✅</td>
    </tr>
    <tr>
      <td>DeleteTransitGatewayVpcAttachment</td>
       <td style="text-align:right">✅</td>
    </tr>
    <tr>
      <td>DeleteVolume</td>
       <td style="text-align:right">✅</td>
    </tr>
    <tr>
      <td>DeleteVpc <a href="#misc" title="covered by our integration test suite">✨</a></td>
       <td style="text-align:right">✅</td>
    </tr>
    <tr>
      <td>DeleteVpcEndpointServiceConfigurations</td>
       <td style="text-align:right">✅</td>
    </tr>
    <tr>
      <td>DeleteVpcEndpoints <a href="#misc" title="covered by our integration test suite">✨</a></td>
       <td style="text-align:right">✅</td>
    </tr>
    <tr>
      <td>DeleteVpcPeeringConnection <a href="#misc" title="covered by our integration test suite">✨</a></td>
       <td style="text-align:right">✅</td>
    </tr>
    <tr>
      <td>DeleteVpnConnection</td>
       <td style="text-align:right">✅</td>
    </tr>
    <tr>
      <td>DeleteVpnGateway <a href="#misc" title="covered by our integration test suite">✨</a></td>
       <td style="text-align:right">✅</td>
    </tr>
    <tr>
      <td>DeregisterImage</td>
       <td style="text-align:right">✅</td>
    </tr>
    <tr>
      <td>DescribeAccountAttributes <a href="#misc" title="covered by our integration test suite">✨</a></td>
       <td style="text-align:right">✅</td>
    </tr>
    <tr>
      <td>DescribeAddresses</td>
       <td style="text-align:right">✅</td>
    </tr>
    <tr>
      <td>DescribeAvailabilityZones</td>
       <td style="text-align:right">✅</td>
    </tr>
    <tr>
      <td>DescribeCarrierGateways</td>
       <td style="text-align:right">✅</td>
    </tr>
    <tr>
      <td>DescribeCustomerGateways</td>
       <td style="text-align:right">✅</td>
    </tr>
    <tr>
      <td>DescribeDhcpOptions</td>
       <td style="text-align:right">✅</td>
    </tr>
    <tr>
      <td>DescribeEgressOnlyInternetGateways</td>
       <td style="text-align:right">✅</td>
    </tr>
    <tr>
      <td>DescribeFleetInstances</td>
       <td style="text-align:right">✅</td>
    </tr>
    <tr>
      <td>DescribeFleets</td>
       <td style="text-align:right">✅</td>
    </tr>
    <tr>
      <td>DescribeFlowLogs</td>
       <td style="text-align:right">✅</td>
    </tr>
    <tr>
      <td>DescribeIamInstanceProfileAssociations</td>
       <td style="text-align:right">✅</td>
    </tr>
    <tr>
      <td>DescribeImageAttribute</td>
       <td style="text-align:right">✅</td>
    </tr>
    <tr>
      <td>DescribeImages <a href="#misc" title="covered by our integration test suite">✨</a></td>
       <td style="text-align:right">✅</td>
    </tr>
    <tr>
      <td>DescribeInstanceAttribute</td>
       <td style="text-align:right">✅</td>
    </tr>
    <tr>
      <td>DescribeInstanceCreditSpecifications</td>
       <td style="text-align:right">✅</td>
    </tr>
    <tr>
      <td>DescribeInstanceStatus <a href="#misc" title="covered by our integration test suite">✨</a></td>
       <td style="text-align:right">✅</td>
    </tr>
    <tr>
      <td>DescribeInstanceTypeOfferings</td>
       <td style="text-align:right">✅</td>
    </tr>
    <tr>
      <td>DescribeInstanceTypes</td>
       <td style="text-align:right">✅</td>
    </tr>
    <tr>
      <td>DescribeInstances <a href="#misc" title="covered by our integration test suite">✨</a></td>
       <td style="text-align:right">✅</td>
    </tr>
    <tr>
      <td>DescribeInternetGateways <a href="#misc" title="covered by our integration test suite">✨</a></td>
       <td style="text-align:right">✅</td>
    </tr>
    <tr>
      <td>DescribeKeyPairs <a href="#misc" title="covered by our integration test suite">✨</a></td>
       <td style="text-align:right">✅</td>
    </tr>
    <tr>
      <td>DescribeLaunchTemplateVersions</td>
       <td style="text-align:right">✅</td>
    </tr>
    <tr>
      <td>DescribeLaunchTemplates</td>
       <td style="text-align:right">✅</td>
    </tr>
    <tr>
      <td>DescribeManagedPrefixLists</td>
       <td style="text-align:right">✅</td>
    </tr>
    <tr>
      <td>DescribeNatGateways <a href="#misc" title="covered by our integration test suite">✨</a></td>
       <td style="text-align:right">✅</td>
    </tr>
    <tr>
      <td>DescribeNetworkAcls <a href="#misc" title="covered by our integration test suite">✨</a></td>
       <td style="text-align:right">✅</td>
    </tr>
    <tr>
      <td>DescribeNetworkInterfaceAttribute</td>
       <td style="text-align:right">✅</td>
    </tr>
    <tr>
      <td>DescribeNetworkInterfaces <a href="#misc" title="covered by our integration test suite">✨</a></td>
       <td style="text-align:right">✅</td>
    </tr>
    <tr>
      <td>DescribePrefixLists</td>
       <td style="text-align:right">✅</td>
    </tr>
    <tr>
      <td>DescribeRegions</td>
       <td style="text-align:right">✅</td>
    </tr>
    <tr>
      <td>DescribeReservedInstances <a href="#misc" title="covered by our integration test suite">✨</a></td>
       <td style="text-align:right">✅</td>
    </tr>
    <tr>
      <td>DescribeReservedInstancesOfferings <a href="#misc" title="covered by our integration test suite">✨</a></td>
       <td style="text-align:right">✅</td>
    </tr>
    <tr>
      <td>DescribeRouteTables <a href="#misc" title="covered by our integration test suite">✨</a></td>
       <td style="text-align:right">✅</td>
    </tr>
    <tr>
      <td>DescribeSecurityGroups <a href="#misc" title="covered by our integration test suite">✨</a></td>
       <td style="text-align:right">✅</td>
    </tr>
    <tr>
      <td>DescribeSnapshotAttribute</td>
       <td style="text-align:right">✅</td>
    </tr>
    <tr>
      <td>DescribeSnapshots</td>
       <td style="text-align:right">✅</td>
    </tr>
    <tr>
      <td>DescribeSpotFleetInstances</td>
       <td style="text-align:right">✅</td>
    </tr>
    <tr>
      <td>DescribeSpotFleetRequests</td>
       <td style="text-align:right">✅</td>
    </tr>
    <tr>
      <td>DescribeSpotInstanceRequests</td>
       <td style="text-align:right">✅</td>
    </tr>
    <tr>
      <td>DescribeSpotPriceHistory</td>
       <td style="text-align:right">✅</td>
    </tr>
    <tr>
      <td>DescribeSubnets <a href="#misc" title="covered by our integration test suite">✨</a></td>
       <td style="text-align:right">✅</td>
    </tr>
    <tr>
      <td>DescribeTags</td>
       <td style="text-align:right">✅</td>
    </tr>
    <tr>
      <td>DescribeTransitGatewayAttachments</td>
       <td style="text-align:right">✅</td>
    </tr>
    <tr>
      <td>DescribeTransitGatewayPeeringAttachments</td>
       <td style="text-align:right">✅</td>
    </tr>
    <tr>
      <td>DescribeTransitGatewayRouteTables</td>
       <td style="text-align:right">✅</td>
    </tr>
    <tr>
      <td>DescribeTransitGatewayVpcAttachments</td>
       <td style="text-align:right">✅</td>
    </tr>
    <tr>
      <td>DescribeTransitGateways</td>
       <td style="text-align:right">✅</td>
    </tr>
    <tr>
      <td>DescribeVolumes</td>
       <td style="text-align:right">✅</td>
    </tr>
    <tr>
      <td>DescribeVolumesModifications</td>
       <td style="text-align:right">✅</td>
    </tr>
    <tr>
      <td>DescribeVpcAttribute <a href="#misc" title="covered by our integration test suite">✨</a></td>
       <td style="text-align:right">✅</td>
    </tr>
    <tr>
      <td>DescribeVpcClassicLink <a href="#misc" title="covered by our integration test suite">✨</a></td>
       <td style="text-align:right">✅</td>
    </tr>
    <tr>
      <td>DescribeVpcClassicLinkDnsSupport <a href="#misc" title="covered by our integration test suite">✨</a></td>
       <td style="text-align:right">✅</td>
    </tr>
    <tr>
      <td>DescribeVpcEndpointServiceConfigurations</td>
       <td style="text-align:right">✅</td>
    </tr>
    <tr>
      <td>DescribeVpcEndpointServicePermissions</td>
       <td style="text-align:right">✅</td>
    </tr>
    <tr>
      <td>DescribeVpcEndpointServices <a href="#misc" title="covered by our integration test suite">✨</a></td>
       <td style="text-align:right">✅</td>
    </tr>
    <tr>
      <td>DescribeVpcEndpoints <a href="#misc" title="covered by our integration test suite">✨</a></td>
       <td style="text-align:right">✅</td>
    </tr>
    <tr>
      <td>DescribeVpcPeeringConnections <a href="#misc" title="covered by our integration test suite">✨</a></td>
       <td style="text-align:right">✅</td>
    </tr>
    <tr>
      <td>DescribeVpcs <a href="#misc" title="covered by our integration test suite">✨</a></td>
       <td style="text-align:right">✅</td>
    </tr>
    <tr>
      <td>DescribeVpnConnections</td>
       <td style="text-align:right">✅</td>
    </tr>
    <tr>
      <td>DescribeVpnGateways <a href="#misc" title="covered by our integration test suite">✨</a></td>
       <td style="text-align:right">✅</td>
    </tr>
    <tr>
      <td>DetachInternetGateway</td>
       <td style="text-align:right">✅</td>
    </tr>
    <tr>
      <td>DetachNetworkInterface</td>
       <td style="text-align:right">✅</td>
    </tr>
    <tr>
      <td>DetachVolume</td>
       <td style="text-align:right">✅</td>
    </tr>
    <tr>
      <td>DetachVpnGateway <a href="#misc" title="covered by our integration test suite">✨</a></td>
       <td style="text-align:right">✅</td>
    </tr>
    <tr>
      <td>DisableEbsEncryptionByDefault</td>
       <td style="text-align:right">✅</td>
    </tr>
    <tr>
      <td>DisableTransitGatewayRouteTablePropagation</td>
       <td style="text-align:right">✅</td>
    </tr>
    <tr>
      <td>DisableVpcClassicLink</td>
       <td style="text-align:right">✅</td>
    </tr>
    <tr>
      <td>DisableVpcClassicLinkDnsSupport</td>
       <td style="text-align:right">✅</td>
    </tr>
    <tr>
      <td>DisassociateAddress</td>
       <td style="text-align:right">✅</td>
    </tr>
    <tr>
      <td>DisassociateIamInstanceProfile</td>
       <td style="text-align:right">✅</td>
    </tr>
    <tr>
      <td>DisassociateRouteTable <a href="#misc" title="covered by our integration test suite">✨</a></td>
       <td style="text-align:right">✅</td>
    </tr>
    <tr>
      <td>DisassociateSubnetCidrBlock</td>
       <td style="text-align:right">✅</td>
    </tr>
    <tr>
      <td>DisassociateTransitGatewayRouteTable</td>
       <td style="text-align:right">✅</td>
    </tr>
    <tr>
      <td>DisassociateVpcCidrBlock</td>
       <td style="text-align:right">✅</td>
    </tr>
    <tr>
      <td>EnableEbsEncryptionByDefault</td>
       <td style="text-align:right">✅</td>
    </tr>
    <tr>
      <td>EnableTransitGatewayRouteTablePropagation</td>
       <td style="text-align:right">✅</td>
    </tr>
    <tr>
      <td>EnableVolumeIO</td>
       <td style="text-align:right">✅</td>
    </tr>
    <tr>
      <td>EnableVpcClassicLink</td>
       <td style="text-align:right">✅</td>
    </tr>
    <tr>
      <td>EnableVpcClassicLinkDnsSupport</td>
       <td style="text-align:right">✅</td>
    </tr>
    <tr>
      <td>GetConsoleOutput</td>
       <td style="text-align:right">✅</td>
    </tr>
    <tr>
      <td>GetEbsEncryptionByDefault</td>
       <td style="text-align:right">✅</td>
    </tr>
    <tr>
      <td>GetManagedPrefixListEntries</td>
       <td style="text-align:right">✅</td>
    </tr>
    <tr>
      <td>GetTransitGatewayRouteTableAssociations</td>
       <td style="text-align:right">✅</td>
    </tr>
    <tr>
      <td>GetTransitGatewayRouteTablePropagations</td>
       <td style="text-align:right">✅</td>
    </tr>
    <tr>
      <td>ImportKeyPair <a href="#misc" title="covered by our integration test suite">✨</a></td>
       <td style="text-align:right">✅</td>
    </tr>
    <tr>
      <td>ImportVolume</td>
       <td style="text-align:right">✅</td>
    </tr>
    <tr>
      <td>ModifyImageAttribute</td>
       <td style="text-align:right">✅</td>
    </tr>
    <tr>
      <td>ModifyInstanceAttribute</td>
       <td style="text-align:right">✅</td>
    </tr>
    <tr>
      <td>ModifyManagedPrefixList</td>
       <td style="text-align:right">✅</td>
    </tr>
    <tr>
      <td>ModifyNetworkInterfaceAttribute</td>
       <td style="text-align:right">✅</td>
    </tr>
    <tr>
      <td>ModifySnapshotAttribute</td>
       <td style="text-align:right">✅</td>
    </tr>
    <tr>
      <td>ModifySpotFleetRequest</td>
       <td style="text-align:right">✅</td>
    </tr>
    <tr>
      <td>ModifySubnetAttribute <a href="#misc" title="covered by our integration test suite">✨</a></td>
       <td style="text-align:right">✅</td>
    </tr>
    <tr>
      <td>ModifyTransitGateway</td>
       <td style="text-align:right">✅</td>
    </tr>
    <tr>
      <td>ModifyTransitGatewayVpcAttachment</td>
       <td style="text-align:right">✅</td>
    </tr>
    <tr>
      <td>ModifyVolume</td>
       <td style="text-align:right">✅</td>
    </tr>
    <tr>
      <td>ModifyVolumeAttribute</td>
       <td style="text-align:right">✅</td>
    </tr>
    <tr>
      <td>ModifyVpcAttribute</td>
       <td style="text-align:right">✅</td>
    </tr>
    <tr>
      <td>ModifyVpcEndpoint</td>
       <td style="text-align:right">✅</td>
    </tr>
    <tr>
      <td>ModifyVpcEndpointServiceConfiguration</td>
       <td style="text-align:right">✅</td>
    </tr>
    <tr>
      <td>ModifyVpcEndpointServicePermissions</td>
       <td style="text-align:right">✅</td>
    </tr>
    <tr>
      <td>ModifyVpcPeeringConnectionOptions</td>
       <td style="text-align:right">✅</td>
    </tr>
    <tr>
      <td>ModifyVpcTenancy</td>
       <td style="text-align:right">✅</td>
    </tr>
    <tr>
      <td>MonitorInstances</td>
       <td style="text-align:right">✅</td>
    </tr>
    <tr>
      <td>PurchaseReservedInstancesOffering <a href="#misc" title="covered by our integration test suite">✨</a></td>
       <td style="text-align:right">✅</td>
    </tr>
    <tr>
      <td>RebootInstances</td>
       <td style="text-align:right">✅</td>
    </tr>
    <tr>
      <td>RegisterImage</td>
       <td style="text-align:right">✅</td>
    </tr>
    <tr>
      <td>RejectTransitGatewayPeeringAttachment</td>
       <td style="text-align:right">✅</td>
    </tr>
    <tr>
      <td>RejectVpcPeeringConnection</td>
       <td style="text-align:right">✅</td>
    </tr>
    <tr>
      <td>ReleaseAddress <a href="#misc" title="covered by our integration test suite">✨</a></td>
       <td style="text-align:right">✅</td>
    </tr>
    <tr>
      <td>ReplaceIamInstanceProfileAssociation</td>
       <td style="text-align:right">✅</td>
    </tr>
    <tr>
      <td>ReplaceNetworkAclAssociation</td>
       <td style="text-align:right">✅</td>
    </tr>
    <tr>
      <td>ReplaceNetworkAclEntry</td>
       <td style="text-align:right">✅</td>
    </tr>
    <tr>
      <td>ReplaceRoute</td>
       <td style="text-align:right">✅</td>
    </tr>
    <tr>
      <td>ReplaceRouteTableAssociation</td>
       <td style="text-align:right">✅</td>
    </tr>
    <tr>
      <td>RequestSpotFleet</td>
       <td style="text-align:right">✅</td>
    </tr>
    <tr>
      <td>RequestSpotInstances</td>
       <td style="text-align:right">✅</td>
    </tr>
    <tr>
      <td>ResetImageAttribute</td>
       <td style="text-align:right">✅</td>
    </tr>
    <tr>
      <td>ResetNetworkInterfaceAttribute</td>
       <td style="text-align:right">✅</td>
    </tr>
    <tr>
      <td>ResetSnapshotAttribute</td>
       <td style="text-align:right">✅</td>
    </tr>
    <tr>
      <td>RevokeSecurityGroupEgress <a href="#misc" title="covered by our integration test suite">✨</a></td>
       <td style="text-align:right">✅</td>
    </tr>
    <tr>
      <td>RevokeSecurityGroupIngress</td>
       <td style="text-align:right">✅</td>
    </tr>
    <tr>
      <td>RunInstances <a href="#misc" title="covered by our integration test suite">✨</a></td>
       <td style="text-align:right">✅</td>
    </tr>
    <tr>
      <td>SearchTransitGatewayRoutes</td>
       <td style="text-align:right">✅</td>
    </tr>
    <tr>
      <td>StartInstances <a href="#misc" title="covered by our integration test suite">✨</a></td>
       <td style="text-align:right">✅</td>
    </tr>
    <tr>
      <td>StopInstances <a href="#misc" title="covered by our integration test suite">✨</a></td>
       <td style="text-align:right">✅</td>
    </tr>
    <tr>
      <td>TerminateInstances <a href="#misc" title="covered by our integration test suite">✨</a></td>
       <td style="text-align:right">✅</td>
    </tr>
    <tr>
      <td>UnassignIpv6Addresses</td>
       <td style="text-align:right">✅</td>
    </tr>
    <tr>
      <td>UnassignPrivateIpAddresses</td>
       <td style="text-align:right">✅</td>
    </tr>
    <tr>
      <td>UnmonitorInstances</td>
       <td style="text-align:right">✅</td>
    </tr>
    <tr>
      <td>UpdateSecurityGroupRuleDescriptionsEgress</td>
       <td style="text-align:right">✅</td>
    </tr>
    <tr>
      <td>UpdateSecurityGroupRuleDescriptionsIngress</td>
       <td style="text-align:right">✅</td>
    </tr>
  </tbody>
  <tbody>    <tr>
      <td><a data-toggle="collapse" href=".ec2-notimplemented">Show missing</a></td>
      <td style="text-align:right"></td>
    </tr>
  </tbody>
  <tbody class="collapse ec2-notimplemented">     <tr>
      <td>ApplySecurityGroupsToClientVpnTargetNetwork</td>
       <td style="text-align:right">-</td>
    </tr>
    <tr>
      <td>AssociateClientVpnTargetNetwork</td>
       <td style="text-align:right">-</td>
    </tr>
    <tr>
      <td>AssociateEnclaveCertificateIamRole</td>
       <td style="text-align:right">-</td>
    </tr>
    <tr>
      <td>AssociateInstanceEventWindow</td>
       <td style="text-align:right">-</td>
    </tr>
    <tr>
      <td>AssociateTransitGatewayMulticastDomain</td>
       <td style="text-align:right">-</td>
    </tr>
    <tr>
      <td>AssociateTransitGatewayPolicyTable</td>
       <td style="text-align:right">-</td>
    </tr>
    <tr>
      <td>AssociateTrunkInterface</td>
       <td style="text-align:right">-</td>
    </tr>
    <tr>
      <td>AttachClassicLinkVpc</td>
       <td style="text-align:right">-</td>
    </tr>
    <tr>
      <td>AuthorizeClientVpnIngress</td>
       <td style="text-align:right">-</td>
    </tr>
    <tr>
      <td>BundleInstance</td>
       <td style="text-align:right">-</td>
    </tr>
    <tr>
      <td>CancelBundleTask</td>
       <td style="text-align:right">-</td>
    </tr>
    <tr>
      <td>CancelCapacityReservation</td>
       <td style="text-align:right">-</td>
    </tr>
    <tr>
      <td>CancelCapacityReservationFleets</td>
       <td style="text-align:right">-</td>
    </tr>
    <tr>
      <td>CancelConversionTask</td>
       <td style="text-align:right">-</td>
    </tr>
    <tr>
      <td>CancelExportTask</td>
       <td style="text-align:right">-</td>
    </tr>
    <tr>
      <td>CancelImportTask</td>
       <td style="text-align:right">-</td>
    </tr>
    <tr>
      <td>CancelReservedInstancesListing</td>
       <td style="text-align:right">-</td>
    </tr>
    <tr>
      <td>ConfirmProductInstance</td>
       <td style="text-align:right">-</td>
    </tr>
    <tr>
      <td>CopyFpgaImage</td>
       <td style="text-align:right">-</td>
    </tr>
    <tr>
      <td>CreateCapacityReservation</td>
       <td style="text-align:right">-</td>
    </tr>
    <tr>
      <td>CreateCapacityReservationFleet</td>
       <td style="text-align:right">-</td>
    </tr>
    <tr>
      <td>CreateClientVpnEndpoint</td>
       <td style="text-align:right">-</td>
    </tr>
    <tr>
      <td>CreateClientVpnRoute</td>
       <td style="text-align:right">-</td>
    </tr>
    <tr>
      <td>CreateCoipCidr</td>
       <td style="text-align:right">-</td>
    </tr>
    <tr>
      <td>CreateCoipPool</td>
       <td style="text-align:right">-</td>
    </tr>
    <tr>
      <td>CreateDefaultSubnet</td>
       <td style="text-align:right">-</td>
    </tr>
    <tr>
      <td>CreateFpgaImage</td>
       <td style="text-align:right">-</td>
    </tr>
    <tr>
      <td>CreateInstanceEventWindow</td>
       <td style="text-align:right">-</td>
    </tr>
    <tr>
      <td>CreateInstanceExportTask</td>
       <td style="text-align:right">-</td>
    </tr>
    <tr>
      <td>CreateIpam</td>
       <td style="text-align:right">-</td>
    </tr>
    <tr>
      <td>CreateIpamPool</td>
       <td style="text-align:right">-</td>
    </tr>
    <tr>
      <td>CreateIpamScope</td>
       <td style="text-align:right">-</td>
    </tr>
    <tr>
      <td>CreateLocalGatewayRoute</td>
       <td style="text-align:right">-</td>
    </tr>
    <tr>
      <td>CreateLocalGatewayRouteTable</td>
       <td style="text-align:right">-</td>
    </tr>
    <tr>
      <td>CreateLocalGatewayRouteTableVirtualInterfaceGroupAssociation</td>
       <td style="text-align:right">-</td>
    </tr>
    <tr>
      <td>CreateLocalGatewayRouteTableVpcAssociation</td>
       <td style="text-align:right">-</td>
    </tr>
    <tr>
      <td>CreateNetworkInsightsAccessScope</td>
       <td style="text-align:right">-</td>
    </tr>
    <tr>
      <td>CreateNetworkInsightsPath</td>
       <td style="text-align:right">-</td>
    </tr>
    <tr>
      <td>CreateNetworkInterfacePermission</td>
       <td style="text-align:right">-</td>
    </tr>
    <tr>
      <td>CreatePublicIpv4Pool</td>
       <td style="text-align:right">-</td>
    </tr>
    <tr>
      <td>CreateReplaceRootVolumeTask</td>
       <td style="text-align:right">-</td>
    </tr>
    <tr>
      <td>CreateReservedInstancesListing</td>
       <td style="text-align:right">-</td>
    </tr>
    <tr>
      <td>CreateRestoreImageTask</td>
       <td style="text-align:right">-</td>
    </tr>
    <tr>
      <td>CreateStoreImageTask</td>
       <td style="text-align:right">-</td>
    </tr>
    <tr>
      <td>CreateSubnetCidrReservation</td>
       <td style="text-align:right">-</td>
    </tr>
    <tr>
      <td>CreateTrafficMirrorFilter</td>
       <td style="text-align:right">-</td>
    </tr>
    <tr>
      <td>CreateTrafficMirrorFilterRule</td>
       <td style="text-align:right">-</td>
    </tr>
    <tr>
      <td>CreateTrafficMirrorSession</td>
       <td style="text-align:right">-</td>
    </tr>
    <tr>
      <td>CreateTrafficMirrorTarget</td>
       <td style="text-align:right">-</td>
    </tr>
    <tr>
      <td>CreateTransitGatewayConnect</td>
       <td style="text-align:right">-</td>
    </tr>
    <tr>
      <td>CreateTransitGatewayConnectPeer</td>
       <td style="text-align:right">-</td>
    </tr>
    <tr>
      <td>CreateTransitGatewayMulticastDomain</td>
       <td style="text-align:right">-</td>
    </tr>
    <tr>
      <td>CreateTransitGatewayPolicyTable</td>
       <td style="text-align:right">-</td>
    </tr>
    <tr>
      <td>CreateTransitGatewayPrefixListReference</td>
       <td style="text-align:right">-</td>
    </tr>
    <tr>
      <td>CreateTransitGatewayRouteTableAnnouncement</td>
       <td style="text-align:right">-</td>
    </tr>
    <tr>
      <td>CreateVpcEndpointConnectionNotification</td>
       <td style="text-align:right">-</td>
    </tr>
    <tr>
      <td>CreateVpnConnectionRoute</td>
       <td style="text-align:right">-</td>
    </tr>
    <tr>
      <td>DeleteClientVpnEndpoint</td>
       <td style="text-align:right">-</td>
    </tr>
    <tr>
      <td>DeleteClientVpnRoute</td>
       <td style="text-align:right">-</td>
    </tr>
    <tr>
      <td>DeleteCoipCidr</td>
       <td style="text-align:right">-</td>
    </tr>
    <tr>
      <td>DeleteCoipPool</td>
       <td style="text-align:right">-</td>
    </tr>
    <tr>
      <td>DeleteFpgaImage</td>
       <td style="text-align:right">-</td>
    </tr>
    <tr>
      <td>DeleteInstanceEventWindow</td>
       <td style="text-align:right">-</td>
    </tr>
    <tr>
      <td>DeleteIpam</td>
       <td style="text-align:right">-</td>
    </tr>
    <tr>
      <td>DeleteIpamPool</td>
       <td style="text-align:right">-</td>
    </tr>
    <tr>
      <td>DeleteIpamScope</td>
       <td style="text-align:right">-</td>
    </tr>
    <tr>
      <td>DeleteLaunchTemplateVersions</td>
       <td style="text-align:right">-</td>
    </tr>
    <tr>
      <td>DeleteLocalGatewayRoute</td>
       <td style="text-align:right">-</td>
    </tr>
    <tr>
      <td>DeleteLocalGatewayRouteTable</td>
       <td style="text-align:right">-</td>
    </tr>
    <tr>
      <td>DeleteLocalGatewayRouteTableVirtualInterfaceGroupAssociation</td>
       <td style="text-align:right">-</td>
    </tr>
    <tr>
      <td>DeleteLocalGatewayRouteTableVpcAssociation</td>
       <td style="text-align:right">-</td>
    </tr>
    <tr>
      <td>DeleteNetworkInsightsAccessScope</td>
       <td style="text-align:right">-</td>
    </tr>
    <tr>
      <td>DeleteNetworkInsightsAccessScopeAnalysis</td>
       <td style="text-align:right">-</td>
    </tr>
    <tr>
      <td>DeleteNetworkInsightsAnalysis</td>
       <td style="text-align:right">-</td>
    </tr>
    <tr>
      <td>DeleteNetworkInsightsPath</td>
       <td style="text-align:right">-</td>
    </tr>
    <tr>
      <td>DeleteNetworkInterfacePermission</td>
       <td style="text-align:right">-</td>
    </tr>
    <tr>
      <td>DeletePublicIpv4Pool</td>
       <td style="text-align:right">-</td>
    </tr>
    <tr>
      <td>DeleteQueuedReservedInstances</td>
       <td style="text-align:right">-</td>
    </tr>
    <tr>
      <td>DeleteSubnetCidrReservation</td>
       <td style="text-align:right">-</td>
    </tr>
    <tr>
      <td>DeleteTrafficMirrorFilter</td>
       <td style="text-align:right">-</td>
    </tr>
    <tr>
      <td>DeleteTrafficMirrorFilterRule</td>
       <td style="text-align:right">-</td>
    </tr>
    <tr>
      <td>DeleteTrafficMirrorSession</td>
       <td style="text-align:right">-</td>
    </tr>
    <tr>
      <td>DeleteTrafficMirrorTarget</td>
       <td style="text-align:right">-</td>
    </tr>
    <tr>
      <td>DeleteTransitGatewayConnect</td>
       <td style="text-align:right">-</td>
    </tr>
    <tr>
      <td>DeleteTransitGatewayConnectPeer</td>
       <td style="text-align:right">-</td>
    </tr>
    <tr>
      <td>DeleteTransitGatewayMulticastDomain</td>
       <td style="text-align:right">-</td>
    </tr>
    <tr>
      <td>DeleteTransitGatewayPolicyTable</td>
       <td style="text-align:right">-</td>
    </tr>
    <tr>
      <td>DeleteTransitGatewayPrefixListReference</td>
       <td style="text-align:right">-</td>
    </tr>
    <tr>
      <td>DeleteTransitGatewayRouteTableAnnouncement</td>
       <td style="text-align:right">-</td>
    </tr>
    <tr>
      <td>DeleteVpcEndpointConnectionNotifications</td>
       <td style="text-align:right">-</td>
    </tr>
    <tr>
      <td>DeleteVpnConnectionRoute</td>
       <td style="text-align:right">-</td>
    </tr>
    <tr>
      <td>DeprovisionByoipCidr</td>
       <td style="text-align:right">-</td>
    </tr>
    <tr>
      <td>DeprovisionIpamPoolCidr</td>
       <td style="text-align:right">-</td>
    </tr>
    <tr>
      <td>DeprovisionPublicIpv4PoolCidr</td>
       <td style="text-align:right">-</td>
    </tr>
    <tr>
      <td>DeregisterInstanceEventNotificationAttributes</td>
       <td style="text-align:right">-</td>
    </tr>
    <tr>
      <td>DeregisterTransitGatewayMulticastGroupMembers</td>
       <td style="text-align:right">-</td>
    </tr>
    <tr>
      <td>DeregisterTransitGatewayMulticastGroupSources</td>
       <td style="text-align:right">-</td>
    </tr>
    <tr>
      <td>DescribeAddressesAttribute</td>
       <td style="text-align:right">-</td>
    </tr>
    <tr>
      <td>DescribeAggregateIdFormat</td>
       <td style="text-align:right">-</td>
    </tr>
    <tr>
      <td>DescribeBundleTasks</td>
       <td style="text-align:right">-</td>
    </tr>
    <tr>
      <td>DescribeByoipCidrs</td>
       <td style="text-align:right">-</td>
    </tr>
    <tr>
      <td>DescribeCapacityReservationFleets</td>
       <td style="text-align:right">-</td>
    </tr>
    <tr>
      <td>DescribeCapacityReservations</td>
       <td style="text-align:right">-</td>
    </tr>
    <tr>
      <td>DescribeClassicLinkInstances</td>
       <td style="text-align:right">-</td>
    </tr>
    <tr>
      <td>DescribeClientVpnAuthorizationRules</td>
       <td style="text-align:right">-</td>
    </tr>
    <tr>
      <td>DescribeClientVpnConnections</td>
       <td style="text-align:right">-</td>
    </tr>
    <tr>
      <td>DescribeClientVpnEndpoints</td>
       <td style="text-align:right">-</td>
    </tr>
    <tr>
      <td>DescribeClientVpnRoutes</td>
       <td style="text-align:right">-</td>
    </tr>
    <tr>
      <td>DescribeClientVpnTargetNetworks</td>
       <td style="text-align:right">-</td>
    </tr>
    <tr>
      <td>DescribeCoipPools</td>
       <td style="text-align:right">-</td>
    </tr>
    <tr>
      <td>DescribeConversionTasks</td>
       <td style="text-align:right">-</td>
    </tr>
    <tr>
      <td>DescribeElasticGpus</td>
       <td style="text-align:right">-</td>
    </tr>
    <tr>
      <td>DescribeExportImageTasks</td>
       <td style="text-align:right">-</td>
    </tr>
    <tr>
      <td>DescribeExportTasks</td>
       <td style="text-align:right">-</td>
    </tr>
    <tr>
      <td>DescribeFastLaunchImages</td>
       <td style="text-align:right">-</td>
    </tr>
    <tr>
      <td>DescribeFastSnapshotRestores</td>
       <td style="text-align:right">-</td>
    </tr>
    <tr>
      <td>DescribeFleetHistory</td>
       <td style="text-align:right">-</td>
    </tr>
    <tr>
      <td>DescribeFpgaImageAttribute</td>
       <td style="text-align:right">-</td>
    </tr>
    <tr>
      <td>DescribeFpgaImages</td>
       <td style="text-align:right">-</td>
    </tr>
    <tr>
      <td>DescribeHostReservationOfferings</td>
       <td style="text-align:right">-</td>
    </tr>
    <tr>
      <td>DescribeHostReservations</td>
       <td style="text-align:right">-</td>
    </tr>
    <tr>
      <td>DescribeHosts</td>
       <td style="text-align:right">-</td>
    </tr>
    <tr>
      <td>DescribeIdFormat</td>
       <td style="text-align:right">-</td>
    </tr>
    <tr>
      <td>DescribeIdentityIdFormat</td>
       <td style="text-align:right">-</td>
    </tr>
    <tr>
      <td>DescribeImportImageTasks</td>
       <td style="text-align:right">-</td>
    </tr>
    <tr>
      <td>DescribeImportSnapshotTasks</td>
       <td style="text-align:right">-</td>
    </tr>
    <tr>
      <td>DescribeInstanceEventNotificationAttributes</td>
       <td style="text-align:right">-</td>
    </tr>
    <tr>
      <td>DescribeInstanceEventWindows</td>
       <td style="text-align:right">-</td>
    </tr>
    <tr>
      <td>DescribeIpamPools</td>
       <td style="text-align:right">-</td>
    </tr>
    <tr>
      <td>DescribeIpamScopes</td>
       <td style="text-align:right">-</td>
    </tr>
    <tr>
      <td>DescribeIpams</td>
       <td style="text-align:right">-</td>
    </tr>
    <tr>
      <td>DescribeIpv6Pools</td>
       <td style="text-align:right">-</td>
    </tr>
    <tr>
      <td>DescribeLocalGatewayRouteTableVirtualInterfaceGroupAssociations</td>
       <td style="text-align:right">-</td>
    </tr>
    <tr>
      <td>DescribeLocalGatewayRouteTableVpcAssociations</td>
       <td style="text-align:right">-</td>
    </tr>
    <tr>
      <td>DescribeLocalGatewayRouteTables</td>
       <td style="text-align:right">-</td>
    </tr>
    <tr>
      <td>DescribeLocalGatewayVirtualInterfaceGroups</td>
       <td style="text-align:right">-</td>
    </tr>
    <tr>
      <td>DescribeLocalGatewayVirtualInterfaces</td>
       <td style="text-align:right">-</td>
    </tr>
    <tr>
      <td>DescribeLocalGateways</td>
       <td style="text-align:right">-</td>
    </tr>
    <tr>
      <td>DescribeMovingAddresses</td>
       <td style="text-align:right">-</td>
    </tr>
    <tr>
      <td>DescribeNetworkInsightsAccessScopeAnalyses</td>
       <td style="text-align:right">-</td>
    </tr>
    <tr>
      <td>DescribeNetworkInsightsAccessScopes</td>
       <td style="text-align:right">-</td>
    </tr>
    <tr>
      <td>DescribeNetworkInsightsAnalyses</td>
       <td style="text-align:right">-</td>
    </tr>
    <tr>
      <td>DescribeNetworkInsightsPaths</td>
       <td style="text-align:right">-</td>
    </tr>
    <tr>
      <td>DescribeNetworkInterfacePermissions</td>
       <td style="text-align:right">-</td>
    </tr>
    <tr>
      <td>DescribePlacementGroups</td>
       <td style="text-align:right">-</td>
    </tr>
    <tr>
      <td>DescribePrincipalIdFormat</td>
       <td style="text-align:right">-</td>
    </tr>
    <tr>
      <td>DescribePublicIpv4Pools</td>
       <td style="text-align:right">-</td>
    </tr>
    <tr>
      <td>DescribeReplaceRootVolumeTasks</td>
       <td style="text-align:right">-</td>
    </tr>
    <tr>
      <td>DescribeReservedInstancesListings</td>
       <td style="text-align:right">-</td>
    </tr>
    <tr>
      <td>DescribeReservedInstancesModifications</td>
       <td style="text-align:right">-</td>
    </tr>
    <tr>
      <td>DescribeScheduledInstanceAvailability</td>
       <td style="text-align:right">-</td>
    </tr>
    <tr>
      <td>DescribeScheduledInstances</td>
       <td style="text-align:right">-</td>
    </tr>
    <tr>
      <td>DescribeSecurityGroupReferences</td>
       <td style="text-align:right">-</td>
    </tr>
    <tr>
      <td>DescribeSecurityGroupRules</td>
       <td style="text-align:right">-</td>
    </tr>
    <tr>
      <td>DescribeSnapshotTierStatus</td>
       <td style="text-align:right">-</td>
    </tr>
    <tr>
      <td>DescribeSpotDatafeedSubscription</td>
       <td style="text-align:right">-</td>
    </tr>
    <tr>
      <td>DescribeSpotFleetRequestHistory</td>
       <td style="text-align:right">-</td>
    </tr>
    <tr>
      <td>DescribeStaleSecurityGroups</td>
       <td style="text-align:right">-</td>
    </tr>
    <tr>
      <td>DescribeStoreImageTasks</td>
       <td style="text-align:right">-</td>
    </tr>
    <tr>
      <td>DescribeTrafficMirrorFilters</td>
       <td style="text-align:right">-</td>
    </tr>
    <tr>
      <td>DescribeTrafficMirrorSessions</td>
       <td style="text-align:right">-</td>
    </tr>
    <tr>
      <td>DescribeTrafficMirrorTargets</td>
       <td style="text-align:right">-</td>
    </tr>
    <tr>
      <td>DescribeTransitGatewayConnectPeers</td>
       <td style="text-align:right">-</td>
    </tr>
    <tr>
      <td>DescribeTransitGatewayConnects</td>
       <td style="text-align:right">-</td>
    </tr>
    <tr>
      <td>DescribeTransitGatewayMulticastDomains</td>
       <td style="text-align:right">-</td>
    </tr>
    <tr>
      <td>DescribeTransitGatewayPolicyTables</td>
       <td style="text-align:right">-</td>
    </tr>
    <tr>
      <td>DescribeTransitGatewayRouteTableAnnouncements</td>
       <td style="text-align:right">-</td>
    </tr>
    <tr>
      <td>DescribeTrunkInterfaceAssociations</td>
       <td style="text-align:right">-</td>
    </tr>
    <tr>
      <td>DescribeVolumeAttribute</td>
       <td style="text-align:right">-</td>
    </tr>
    <tr>
      <td>DescribeVolumeStatus</td>
       <td style="text-align:right">-</td>
    </tr>
    <tr>
      <td>DescribeVpcEndpointConnectionNotifications</td>
       <td style="text-align:right">-</td>
    </tr>
    <tr>
      <td>DescribeVpcEndpointConnections</td>
       <td style="text-align:right">-</td>
    </tr>
    <tr>
      <td>DetachClassicLinkVpc</td>
       <td style="text-align:right">-</td>
    </tr>
    <tr>
      <td>DisableFastLaunch</td>
       <td style="text-align:right">-</td>
    </tr>
    <tr>
      <td>DisableFastSnapshotRestores</td>
       <td style="text-align:right">-</td>
    </tr>
    <tr>
      <td>DisableImageDeprecation</td>
       <td style="text-align:right">-</td>
    </tr>
    <tr>
      <td>DisableIpamOrganizationAdminAccount</td>
       <td style="text-align:right">-</td>
    </tr>
    <tr>
      <td>DisableSerialConsoleAccess</td>
       <td style="text-align:right">-</td>
    </tr>
    <tr>
      <td>DisableVgwRoutePropagation</td>
       <td style="text-align:right">-</td>
    </tr>
    <tr>
      <td>DisassociateClientVpnTargetNetwork</td>
       <td style="text-align:right">-</td>
    </tr>
    <tr>
      <td>DisassociateEnclaveCertificateIamRole</td>
       <td style="text-align:right">-</td>
    </tr>
    <tr>
      <td>DisassociateInstanceEventWindow</td>
       <td style="text-align:right">-</td>
    </tr>
    <tr>
      <td>DisassociateTransitGatewayMulticastDomain</td>
       <td style="text-align:right">-</td>
    </tr>
    <tr>
      <td>DisassociateTransitGatewayPolicyTable</td>
       <td style="text-align:right">-</td>
    </tr>
    <tr>
      <td>DisassociateTrunkInterface</td>
       <td style="text-align:right">-</td>
    </tr>
    <tr>
      <td>EnableFastLaunch</td>
       <td style="text-align:right">-</td>
    </tr>
    <tr>
      <td>EnableFastSnapshotRestores</td>
       <td style="text-align:right">-</td>
    </tr>
    <tr>
      <td>EnableImageDeprecation</td>
       <td style="text-align:right">-</td>
    </tr>
    <tr>
      <td>EnableIpamOrganizationAdminAccount</td>
       <td style="text-align:right">-</td>
    </tr>
    <tr>
      <td>EnableSerialConsoleAccess</td>
       <td style="text-align:right">-</td>
    </tr>
    <tr>
      <td>EnableVgwRoutePropagation</td>
       <td style="text-align:right">-</td>
    </tr>
    <tr>
      <td>ExportClientVpnClientCertificateRevocationList</td>
       <td style="text-align:right">-</td>
    </tr>
    <tr>
      <td>ExportClientVpnClientConfiguration</td>
       <td style="text-align:right">-</td>
    </tr>
    <tr>
      <td>ExportImage</td>
       <td style="text-align:right">-</td>
    </tr>
    <tr>
      <td>ExportTransitGatewayRoutes</td>
       <td style="text-align:right">-</td>
    </tr>
    <tr>
      <td>GetAssociatedEnclaveCertificateIamRoles</td>
       <td style="text-align:right">-</td>
    </tr>
    <tr>
      <td>GetAssociatedIpv6PoolCidrs</td>
       <td style="text-align:right">-</td>
    </tr>
    <tr>
      <td>GetCapacityReservationUsage</td>
       <td style="text-align:right">-</td>
    </tr>
    <tr>
      <td>GetCoipPoolUsage</td>
       <td style="text-align:right">-</td>
    </tr>
    <tr>
      <td>GetConsoleScreenshot</td>
       <td style="text-align:right">-</td>
    </tr>
    <tr>
      <td>GetDefaultCreditSpecification</td>
       <td style="text-align:right">-</td>
    </tr>
    <tr>
      <td>GetEbsDefaultKmsKeyId</td>
       <td style="text-align:right">-</td>
    </tr>
    <tr>
      <td>GetFlowLogsIntegrationTemplate</td>
       <td style="text-align:right">-</td>
    </tr>
    <tr>
      <td>GetGroupsForCapacityReservation</td>
       <td style="text-align:right">-</td>
    </tr>
    <tr>
      <td>GetHostReservationPurchasePreview</td>
       <td style="text-align:right">-</td>
    </tr>
    <tr>
      <td>GetInstanceTypesFromInstanceRequirements</td>
       <td style="text-align:right">-</td>
    </tr>
    <tr>
      <td>GetInstanceUefiData</td>
       <td style="text-align:right">-</td>
    </tr>
    <tr>
      <td>GetIpamAddressHistory</td>
       <td style="text-align:right">-</td>
    </tr>
    <tr>
      <td>GetIpamPoolAllocations</td>
       <td style="text-align:right">-</td>
    </tr>
    <tr>
      <td>GetIpamPoolCidrs</td>
       <td style="text-align:right">-</td>
    </tr>
    <tr>
      <td>GetIpamResourceCidrs</td>
       <td style="text-align:right">-</td>
    </tr>
    <tr>
      <td>GetLaunchTemplateData</td>
       <td style="text-align:right">-</td>
    </tr>
    <tr>
      <td>GetManagedPrefixListAssociations</td>
       <td style="text-align:right">-</td>
    </tr>
    <tr>
      <td>GetNetworkInsightsAccessScopeAnalysisFindings</td>
       <td style="text-align:right">-</td>
    </tr>
    <tr>
      <td>GetNetworkInsightsAccessScopeContent</td>
       <td style="text-align:right">-</td>
    </tr>
    <tr>
      <td>GetPasswordData</td>
       <td style="text-align:right">-</td>
    </tr>
    <tr>
      <td>GetReservedInstancesExchangeQuote</td>
       <td style="text-align:right">-</td>
    </tr>
    <tr>
      <td>GetSerialConsoleAccessStatus</td>
       <td style="text-align:right">-</td>
    </tr>
    <tr>
      <td>GetSpotPlacementScores</td>
       <td style="text-align:right">-</td>
    </tr>
    <tr>
      <td>GetSubnetCidrReservations</td>
       <td style="text-align:right">-</td>
    </tr>
    <tr>
      <td>GetTransitGatewayAttachmentPropagations</td>
       <td style="text-align:right">-</td>
    </tr>
    <tr>
      <td>GetTransitGatewayMulticastDomainAssociations</td>
       <td style="text-align:right">-</td>
    </tr>
    <tr>
      <td>GetTransitGatewayPolicyTableAssociations</td>
       <td style="text-align:right">-</td>
    </tr>
    <tr>
      <td>GetTransitGatewayPolicyTableEntries</td>
       <td style="text-align:right">-</td>
    </tr>
    <tr>
      <td>GetTransitGatewayPrefixListReferences</td>
       <td style="text-align:right">-</td>
    </tr>
    <tr>
      <td>GetVpnConnectionDeviceSampleConfiguration</td>
       <td style="text-align:right">-</td>
    </tr>
    <tr>
      <td>GetVpnConnectionDeviceTypes</td>
       <td style="text-align:right">-</td>
    </tr>
    <tr>
      <td>ImportClientVpnClientCertificateRevocationList</td>
       <td style="text-align:right">-</td>
    </tr>
    <tr>
      <td>ImportImage</td>
       <td style="text-align:right">-</td>
    </tr>
    <tr>
      <td>ImportInstance</td>
       <td style="text-align:right">-</td>
    </tr>
    <tr>
      <td>ImportSnapshot</td>
       <td style="text-align:right">-</td>
    </tr>
    <tr>
      <td>ListImagesInRecycleBin</td>
       <td style="text-align:right">-</td>
    </tr>
    <tr>
      <td>ListSnapshotsInRecycleBin</td>
       <td style="text-align:right">-</td>
    </tr>
    <tr>
      <td>ModifyAddressAttribute</td>
       <td style="text-align:right">-</td>
    </tr>
    <tr>
      <td>ModifyAvailabilityZoneGroup</td>
       <td style="text-align:right">-</td>
    </tr>
    <tr>
      <td>ModifyCapacityReservation</td>
       <td style="text-align:right">-</td>
    </tr>
    <tr>
      <td>ModifyCapacityReservationFleet</td>
       <td style="text-align:right">-</td>
    </tr>
    <tr>
      <td>ModifyClientVpnEndpoint</td>
       <td style="text-align:right">-</td>
    </tr>
    <tr>
      <td>ModifyDefaultCreditSpecification</td>
       <td style="text-align:right">-</td>
    </tr>
    <tr>
      <td>ModifyEbsDefaultKmsKeyId</td>
       <td style="text-align:right">-</td>
    </tr>
    <tr>
      <td>ModifyFleet</td>
       <td style="text-align:right">-</td>
    </tr>
    <tr>
      <td>ModifyFpgaImageAttribute</td>
       <td style="text-align:right">-</td>
    </tr>
    <tr>
      <td>ModifyHosts</td>
       <td style="text-align:right">-</td>
    </tr>
    <tr>
      <td>ModifyIdFormat</td>
       <td style="text-align:right">-</td>
    </tr>
    <tr>
      <td>ModifyIdentityIdFormat</td>
       <td style="text-align:right">-</td>
    </tr>
    <tr>
      <td>ModifyInstanceCapacityReservationAttributes</td>
       <td style="text-align:right">-</td>
    </tr>
    <tr>
      <td>ModifyInstanceCreditSpecification</td>
       <td style="text-align:right">-</td>
    </tr>
    <tr>
      <td>ModifyInstanceEventStartTime</td>
       <td style="text-align:right">-</td>
    </tr>
    <tr>
      <td>ModifyInstanceEventWindow</td>
       <td style="text-align:right">-</td>
    </tr>
    <tr>
      <td>ModifyInstanceMaintenanceOptions</td>
       <td style="text-align:right">-</td>
    </tr>
    <tr>
      <td>ModifyInstanceMetadataOptions</td>
       <td style="text-align:right">-</td>
    </tr>
    <tr>
      <td>ModifyInstancePlacement</td>
       <td style="text-align:right">-</td>
    </tr>
    <tr>
      <td>ModifyIpam</td>
       <td style="text-align:right">-</td>
    </tr>
    <tr>
      <td>ModifyIpamPool</td>
       <td style="text-align:right">-</td>
    </tr>
    <tr>
      <td>ModifyIpamResourceCidr</td>
       <td style="text-align:right">-</td>
    </tr>
    <tr>
      <td>ModifyIpamScope</td>
       <td style="text-align:right">-</td>
    </tr>
    <tr>
      <td>ModifyLaunchTemplate</td>
       <td style="text-align:right">-</td>
    </tr>
    <tr>
      <td>ModifyLocalGatewayRoute</td>
       <td style="text-align:right">-</td>
    </tr>
    <tr>
      <td>ModifyPrivateDnsNameOptions</td>
       <td style="text-align:right">-</td>
    </tr>
    <tr>
      <td>ModifyReservedInstances</td>
       <td style="text-align:right">-</td>
    </tr>
    <tr>
      <td>ModifySecurityGroupRules</td>
       <td style="text-align:right">-</td>
    </tr>
    <tr>
      <td>ModifySnapshotTier</td>
       <td style="text-align:right">-</td>
    </tr>
    <tr>
      <td>ModifyTrafficMirrorFilterNetworkServices</td>
       <td style="text-align:right">-</td>
    </tr>
    <tr>
      <td>ModifyTrafficMirrorFilterRule</td>
       <td style="text-align:right">-</td>
    </tr>
    <tr>
      <td>ModifyTrafficMirrorSession</td>
       <td style="text-align:right">-</td>
    </tr>
    <tr>
      <td>ModifyTransitGatewayPrefixListReference</td>
       <td style="text-align:right">-</td>
    </tr>
    <tr>
      <td>ModifyVpcEndpointConnectionNotification</td>
       <td style="text-align:right">-</td>
    </tr>
    <tr>
      <td>ModifyVpcEndpointServicePayerResponsibility</td>
       <td style="text-align:right">-</td>
    </tr>
    <tr>
      <td>ModifyVpnConnection</td>
       <td style="text-align:right">-</td>
    </tr>
    <tr>
      <td>ModifyVpnConnectionOptions</td>
       <td style="text-align:right">-</td>
    </tr>
    <tr>
      <td>ModifyVpnTunnelCertificate</td>
       <td style="text-align:right">-</td>
    </tr>
    <tr>
      <td>ModifyVpnTunnelOptions</td>
       <td style="text-align:right">-</td>
    </tr>
    <tr>
      <td>MoveAddressToVpc</td>
       <td style="text-align:right">-</td>
    </tr>
    <tr>
      <td>MoveByoipCidrToIpam</td>
       <td style="text-align:right">-</td>
    </tr>
    <tr>
      <td>ProvisionByoipCidr</td>
       <td style="text-align:right">-</td>
    </tr>
    <tr>
      <td>ProvisionIpamPoolCidr</td>
       <td style="text-align:right">-</td>
    </tr>
    <tr>
      <td>ProvisionPublicIpv4PoolCidr</td>
       <td style="text-align:right">-</td>
    </tr>
    <tr>
      <td>PurchaseHostReservation</td>
       <td style="text-align:right">-</td>
    </tr>
    <tr>
      <td>PurchaseScheduledInstances</td>
       <td style="text-align:right">-</td>
    </tr>
    <tr>
      <td>RegisterInstanceEventNotificationAttributes</td>
       <td style="text-align:right">-</td>
    </tr>
    <tr>
      <td>RegisterTransitGatewayMulticastGroupMembers</td>
       <td style="text-align:right">-</td>
    </tr>
    <tr>
      <td>RegisterTransitGatewayMulticastGroupSources</td>
       <td style="text-align:right">-</td>
    </tr>
    <tr>
      <td>RejectTransitGatewayMulticastDomainAssociations</td>
       <td style="text-align:right">-</td>
    </tr>
    <tr>
      <td>RejectTransitGatewayVpcAttachment</td>
       <td style="text-align:right">-</td>
    </tr>
    <tr>
      <td>RejectVpcEndpointConnections</td>
       <td style="text-align:right">-</td>
    </tr>
    <tr>
      <td>ReleaseHosts</td>
       <td style="text-align:right">-</td>
    </tr>
    <tr>
      <td>ReleaseIpamPoolAllocation</td>
       <td style="text-align:right">-</td>
    </tr>
    <tr>
      <td>ReplaceTransitGatewayRoute</td>
       <td style="text-align:right">-</td>
    </tr>
    <tr>
      <td>ReportInstanceStatus</td>
       <td style="text-align:right">-</td>
    </tr>
    <tr>
      <td>ResetAddressAttribute</td>
       <td style="text-align:right">-</td>
    </tr>
    <tr>
      <td>ResetEbsDefaultKmsKeyId</td>
       <td style="text-align:right">-</td>
    </tr>
    <tr>
      <td>ResetFpgaImageAttribute</td>
       <td style="text-align:right">-</td>
    </tr>
    <tr>
      <td>ResetInstanceAttribute</td>
       <td style="text-align:right">-</td>
    </tr>
    <tr>
      <td>RestoreAddressToClassic</td>
       <td style="text-align:right">-</td>
    </tr>
    <tr>
      <td>RestoreImageFromRecycleBin</td>
       <td style="text-align:right">-</td>
    </tr>
    <tr>
      <td>RestoreManagedPrefixListVersion</td>
       <td style="text-align:right">-</td>
    </tr>
    <tr>
      <td>RestoreSnapshotFromRecycleBin</td>
       <td style="text-align:right">-</td>
    </tr>
    <tr>
      <td>RestoreSnapshotTier</td>
       <td style="text-align:right">-</td>
    </tr>
    <tr>
      <td>RevokeClientVpnIngress</td>
       <td style="text-align:right">-</td>
    </tr>
    <tr>
      <td>RunScheduledInstances</td>
       <td style="text-align:right">-</td>
    </tr>
    <tr>
      <td>SearchLocalGatewayRoutes</td>
       <td style="text-align:right">-</td>
    </tr>
    <tr>
      <td>SearchTransitGatewayMulticastGroups</td>
       <td style="text-align:right">-</td>
    </tr>
    <tr>
      <td>SendDiagnosticInterrupt</td>
       <td style="text-align:right">-</td>
    </tr>
    <tr>
      <td>StartNetworkInsightsAccessScopeAnalysis</td>
       <td style="text-align:right">-</td>
    </tr>
    <tr>
      <td>StartNetworkInsightsAnalysis</td>
       <td style="text-align:right">-</td>
    </tr>
    <tr>
      <td>StartVpcEndpointServicePrivateDnsVerification</td>
       <td style="text-align:right">-</td>
    </tr>
    <tr>
      <td>TerminateClientVpnConnections</td>
       <td style="text-align:right">-</td>
    </tr>
    <tr>
      <td>WithdrawByoipCidr</td>
       <td style="text-align:right">-</td>
    </tr>
  </tbody>
 </table>


## ecr ##

<table>
  <thead>
    <tr>
      <th>Operation</th>
      <th style="text-align:right">Implemented</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td>BatchDeleteImage (Pro)  <a href="#misc" title="covered by our integration test suite">✨</a></td>
       <td style="text-align:right">✅</td>
    </tr>
    <tr>
      <td>BatchGetImage (Pro)  <a href="#misc" title="covered by our integration test suite">✨</a></td>
       <td style="text-align:right">✅</td>
    </tr>
    <tr>
      <td>CreateRepository (Pro)  <a href="#misc" title="covered by our integration test suite">✨</a></td>
       <td style="text-align:right">✅</td>
    </tr>
    <tr>
      <td>DeleteLifecyclePolicy (Pro)  <a href="#misc" title="covered by our integration test suite">✨</a></td>
       <td style="text-align:right">✅</td>
    </tr>
    <tr>
      <td>DeleteRegistryPolicy (Pro) </td>
       <td style="text-align:right">✅</td>
    </tr>
    <tr>
      <td>DeleteRepository (Pro)  <a href="#misc" title="covered by our integration test suite">✨</a></td>
       <td style="text-align:right">✅</td>
    </tr>
    <tr>
      <td>DeleteRepositoryPolicy (Pro) </td>
       <td style="text-align:right">✅</td>
    </tr>
    <tr>
      <td>DescribeImageScanFindings (Pro) </td>
       <td style="text-align:right">✅</td>
    </tr>
    <tr>
      <td>DescribeImages (Pro)  <a href="#misc" title="covered by our integration test suite">✨</a></td>
       <td style="text-align:right">✅</td>
    </tr>
    <tr>
      <td>DescribeRegistry (Pro) </td>
       <td style="text-align:right">✅</td>
    </tr>
    <tr>
      <td>DescribeRepositories (Pro)  <a href="#misc" title="covered by our integration test suite">✨</a></td>
       <td style="text-align:right">✅</td>
    </tr>
    <tr>
      <td>GetAuthorizationToken (Pro)  <a href="#misc" title="covered by our integration test suite">✨</a></td>
       <td style="text-align:right">✅</td>
    </tr>
    <tr>
      <td>GetLifecyclePolicy (Pro)  <a href="#misc" title="covered by our integration test suite">✨</a></td>
       <td style="text-align:right">✅</td>
    </tr>
    <tr>
      <td>GetLifecyclePolicyPreview (Pro) </td>
       <td style="text-align:right">✅</td>
    </tr>
    <tr>
      <td>GetRegistryPolicy (Pro) </td>
       <td style="text-align:right">✅</td>
    </tr>
    <tr>
      <td>GetRepositoryPolicy (Pro) </td>
       <td style="text-align:right">✅</td>
    </tr>
    <tr>
      <td>ListImages (Pro)  <a href="#misc" title="covered by our integration test suite">✨</a></td>
       <td style="text-align:right">✅</td>
    </tr>
    <tr>
      <td>ListTagsForResource (Pro)  <a href="#misc" title="covered by our integration test suite">✨</a></td>
       <td style="text-align:right">✅</td>
    </tr>
    <tr>
      <td>PutImage (Pro) </td>
       <td style="text-align:right">✅</td>
    </tr>
    <tr>
      <td>PutImageScanningConfiguration (Pro) </td>
       <td style="text-align:right">✅</td>
    </tr>
    <tr>
      <td>PutImageTagMutability (Pro)  <a href="#misc" title="covered by our integration test suite">✨</a></td>
       <td style="text-align:right">✅</td>
    </tr>
    <tr>
      <td>PutLifecyclePolicy (Pro)  <a href="#misc" title="covered by our integration test suite">✨</a></td>
       <td style="text-align:right">✅</td>
    </tr>
    <tr>
      <td>PutRegistryPolicy (Pro) </td>
       <td style="text-align:right">✅</td>
    </tr>
    <tr>
      <td>PutReplicationConfiguration (Pro) </td>
       <td style="text-align:right">✅</td>
    </tr>
    <tr>
      <td>SetRepositoryPolicy (Pro) </td>
       <td style="text-align:right">✅</td>
    </tr>
    <tr>
      <td>StartImageScan (Pro) </td>
       <td style="text-align:right">✅</td>
    </tr>
    <tr>
      <td>StartLifecyclePolicyPreview (Pro) </td>
       <td style="text-align:right">✅</td>
    </tr>
    <tr>
      <td>TagResource (Pro)  <a href="#misc" title="covered by our integration test suite">✨</a></td>
       <td style="text-align:right">✅</td>
    </tr>
    <tr>
      <td>UntagResource (Pro)  <a href="#misc" title="covered by our integration test suite">✨</a></td>
       <td style="text-align:right">✅</td>
    </tr>
  </tbody>
  <tbody>    <tr>
      <td><a data-toggle="collapse" href=".ecr-notimplemented">Show missing</a></td>
      <td style="text-align:right"></td>
    </tr>
  </tbody>
  <tbody class="collapse ecr-notimplemented">     <tr>
      <td>BatchCheckLayerAvailability</td>
       <td style="text-align:right">-</td>
    </tr>
    <tr>
      <td>BatchGetRepositoryScanningConfiguration</td>
       <td style="text-align:right">-</td>
    </tr>
    <tr>
      <td>CompleteLayerUpload</td>
       <td style="text-align:right">-</td>
    </tr>
    <tr>
      <td>CreatePullThroughCacheRule</td>
       <td style="text-align:right">-</td>
    </tr>
    <tr>
      <td>DeletePullThroughCacheRule</td>
       <td style="text-align:right">-</td>
    </tr>
    <tr>
      <td>DescribeImageReplicationStatus</td>
       <td style="text-align:right">-</td>
    </tr>
    <tr>
      <td>DescribePullThroughCacheRules</td>
       <td style="text-align:right">-</td>
    </tr>
    <tr>
      <td>GetDownloadUrlForLayer</td>
       <td style="text-align:right">-</td>
    </tr>
    <tr>
      <td>GetRegistryScanningConfiguration</td>
       <td style="text-align:right">-</td>
    </tr>
    <tr>
      <td>InitiateLayerUpload</td>
       <td style="text-align:right">-</td>
    </tr>
    <tr>
      <td>PutRegistryScanningConfiguration</td>
       <td style="text-align:right">-</td>
    </tr>
    <tr>
      <td>UploadLayerPart</td>
       <td style="text-align:right">-</td>
    </tr>
  </tbody>
 </table>


## ecs ##

<table>
  <thead>
    <tr>
      <th>Operation</th>
      <th style="text-align:right">Implemented</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td>CreateCapacityProvider (Pro) </td>
       <td style="text-align:right">✅</td>
    </tr>
    <tr>
      <td>CreateCluster (Pro)  <a href="#misc" title="covered by our integration test suite">✨</a></td>
       <td style="text-align:right">✅</td>
    </tr>
    <tr>
      <td>CreateService (Pro)  <a href="#misc" title="covered by our integration test suite">✨</a></td>
       <td style="text-align:right">✅</td>
    </tr>
    <tr>
      <td>CreateTaskSet (Pro)  <a href="#misc" title="covered by our integration test suite">✨</a></td>
       <td style="text-align:right">✅</td>
    </tr>
    <tr>
      <td>DeleteAccountSetting (Pro) </td>
       <td style="text-align:right">✅</td>
    </tr>
    <tr>
      <td>DeleteAttributes (Pro) </td>
       <td style="text-align:right">✅</td>
    </tr>
    <tr>
      <td>DeleteCapacityProvider (Pro) </td>
       <td style="text-align:right">✅</td>
    </tr>
    <tr>
      <td>DeleteCluster (Pro)  <a href="#misc" title="covered by our integration test suite">✨</a></td>
       <td style="text-align:right">✅</td>
    </tr>
    <tr>
      <td>DeleteService (Pro)  <a href="#misc" title="covered by our integration test suite">✨</a></td>
       <td style="text-align:right">✅</td>
    </tr>
    <tr>
      <td>DeleteTaskSet (Pro) </td>
       <td style="text-align:right">✅</td>
    </tr>
    <tr>
      <td>DeregisterContainerInstance (Pro) </td>
       <td style="text-align:right">✅</td>
    </tr>
    <tr>
      <td>DeregisterTaskDefinition (Pro)  <a href="#misc" title="covered by our integration test suite">✨</a></td>
       <td style="text-align:right">✅</td>
    </tr>
    <tr>
      <td>DescribeCapacityProviders (Pro) </td>
       <td style="text-align:right">✅</td>
    </tr>
    <tr>
      <td>DescribeClusters (Pro)  <a href="#misc" title="covered by our integration test suite">✨</a></td>
       <td style="text-align:right">✅</td>
    </tr>
    <tr>
      <td>DescribeContainerInstances (Pro) </td>
       <td style="text-align:right">✅</td>
    </tr>
    <tr>
      <td>DescribeServices (Pro)  <a href="#misc" title="covered by our integration test suite">✨</a></td>
       <td style="text-align:right">✅</td>
    </tr>
    <tr>
      <td>DescribeTaskDefinition (Pro)  <a href="#misc" title="covered by our integration test suite">✨</a></td>
       <td style="text-align:right">✅</td>
    </tr>
    <tr>
      <td>DescribeTaskSets (Pro) </td>
       <td style="text-align:right">✅</td>
    </tr>
    <tr>
      <td>DescribeTasks (Pro)  <a href="#misc" title="covered by our integration test suite">✨</a></td>
       <td style="text-align:right">✅</td>
    </tr>
    <tr>
      <td>DiscoverPollEndpoint (Pro) </td>
       <td style="text-align:right">✅</td>
    </tr>
    <tr>
      <td>ListAccountSettings (Pro) </td>
       <td style="text-align:right">✅</td>
    </tr>
    <tr>
      <td>ListAttributes (Pro) </td>
       <td style="text-align:right">✅</td>
    </tr>
    <tr>
      <td>ListClusters (Pro)  <a href="#misc" title="covered by our integration test suite">✨</a></td>
       <td style="text-align:right">✅</td>
    </tr>
    <tr>
      <td>ListContainerInstances (Pro) </td>
       <td style="text-align:right">✅</td>
    </tr>
    <tr>
      <td>ListServices (Pro) </td>
       <td style="text-align:right">✅</td>
    </tr>
    <tr>
      <td>ListTagsForResource (Pro)  <a href="#misc" title="covered by our integration test suite">✨</a></td>
       <td style="text-align:right">✅</td>
    </tr>
    <tr>
      <td>ListTaskDefinitionFamilies (Pro) </td>
       <td style="text-align:right">✅</td>
    </tr>
    <tr>
      <td>ListTaskDefinitions (Pro)  <a href="#misc" title="covered by our integration test suite">✨</a></td>
       <td style="text-align:right">✅</td>
    </tr>
    <tr>
      <td>ListTasks (Pro)  <a href="#misc" title="covered by our integration test suite">✨</a></td>
       <td style="text-align:right">✅</td>
    </tr>
    <tr>
      <td>PutAccountSetting (Pro) </td>
       <td style="text-align:right">✅</td>
    </tr>
    <tr>
      <td>PutAttributes (Pro) </td>
       <td style="text-align:right">✅</td>
    </tr>
    <tr>
      <td>PutClusterCapacityProviders (Pro)  <a href="#misc" title="covered by our integration test suite">✨</a></td>
       <td style="text-align:right">✅</td>
    </tr>
    <tr>
      <td>RegisterContainerInstance (Pro) </td>
       <td style="text-align:right">✅</td>
    </tr>
    <tr>
      <td>RegisterTaskDefinition (Pro)  <a href="#misc" title="covered by our integration test suite">✨</a></td>
       <td style="text-align:right">✅</td>
    </tr>
    <tr>
      <td>RunTask (Pro)  <a href="#misc" title="covered by our integration test suite">✨</a></td>
       <td style="text-align:right">✅</td>
    </tr>
    <tr>
      <td>StartTask (Pro) </td>
       <td style="text-align:right">✅</td>
    </tr>
    <tr>
      <td>StopTask (Pro)  <a href="#misc" title="covered by our integration test suite">✨</a></td>
       <td style="text-align:right">✅</td>
    </tr>
    <tr>
      <td>TagResource (Pro)  <a href="#misc" title="covered by our integration test suite">✨</a></td>
       <td style="text-align:right">✅</td>
    </tr>
    <tr>
      <td>UntagResource (Pro) </td>
       <td style="text-align:right">✅</td>
    </tr>
    <tr>
      <td>UpdateCluster (Pro)  <a href="#misc" title="covered by our integration test suite">✨</a></td>
       <td style="text-align:right">✅</td>
    </tr>
    <tr>
      <td>UpdateContainerInstancesState (Pro) </td>
       <td style="text-align:right">✅</td>
    </tr>
    <tr>
      <td>UpdateService (Pro)  <a href="#misc" title="covered by our integration test suite">✨</a></td>
       <td style="text-align:right">✅</td>
    </tr>
    <tr>
      <td>UpdateServicePrimaryTaskSet (Pro) </td>
       <td style="text-align:right">✅</td>
    </tr>
    <tr>
      <td>UpdateTaskSet (Pro) </td>
       <td style="text-align:right">✅</td>
    </tr>
  </tbody>
  <tbody>    <tr>
      <td><a data-toggle="collapse" href=".ecs-notimplemented">Show missing</a></td>
      <td style="text-align:right"></td>
    </tr>
  </tbody>
  <tbody class="collapse ecs-notimplemented">     <tr>
      <td>ExecuteCommand</td>
       <td style="text-align:right">-</td>
    </tr>
    <tr>
      <td>PutAccountSettingDefault</td>
       <td style="text-align:right">-</td>
    </tr>
    <tr>
      <td>SubmitAttachmentStateChanges</td>
       <td style="text-align:right">-</td>
    </tr>
    <tr>
      <td>SubmitContainerStateChange</td>
       <td style="text-align:right">-</td>
    </tr>
    <tr>
      <td>SubmitTaskStateChange</td>
       <td style="text-align:right">-</td>
    </tr>
    <tr>
      <td>UpdateCapacityProvider</td>
       <td style="text-align:right">-</td>
    </tr>
    <tr>
      <td>UpdateClusterSettings</td>
       <td style="text-align:right">-</td>
    </tr>
    <tr>
      <td>UpdateContainerAgent</td>
       <td style="text-align:right">-</td>
    </tr>
  </tbody>
 </table>


## efs ##

<table>
  <thead>
    <tr>
      <th>Operation</th>
      <th style="text-align:right">Implemented</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td>CreateFileSystem (Pro)  <a href="#misc" title="covered by our integration test suite">✨</a></td>
       <td style="text-align:right">✅</td>
    </tr>
    <tr>
      <td>DeleteFileSystem (Pro)  <a href="#misc" title="covered by our integration test suite">✨</a></td>
       <td style="text-align:right">✅</td>
    </tr>
    <tr>
      <td>DescribeFileSystems (Pro)  <a href="#misc" title="covered by our integration test suite">✨</a></td>
       <td style="text-align:right">✅</td>
    </tr>
  </tbody>
  <tbody>    <tr>
      <td><a data-toggle="collapse" href=".efs-notimplemented">Show missing</a></td>
      <td style="text-align:right"></td>
    </tr>
  </tbody>
  <tbody class="collapse efs-notimplemented">     <tr>
      <td>CreateAccessPoint</td>
       <td style="text-align:right">-</td>
    </tr>
    <tr>
      <td>CreateMountTarget</td>
       <td style="text-align:right">-</td>
    </tr>
    <tr>
      <td>CreateReplicationConfiguration</td>
       <td style="text-align:right">-</td>
    </tr>
    <tr>
      <td>CreateTags</td>
       <td style="text-align:right">-</td>
    </tr>
    <tr>
      <td>DeleteAccessPoint</td>
       <td style="text-align:right">-</td>
    </tr>
    <tr>
      <td>DeleteFileSystemPolicy</td>
       <td style="text-align:right">-</td>
    </tr>
    <tr>
      <td>DeleteMountTarget</td>
       <td style="text-align:right">-</td>
    </tr>
    <tr>
      <td>DeleteReplicationConfiguration</td>
       <td style="text-align:right">-</td>
    </tr>
    <tr>
      <td>DeleteTags</td>
       <td style="text-align:right">-</td>
    </tr>
    <tr>
      <td>DescribeAccessPoints</td>
       <td style="text-align:right">-</td>
    </tr>
    <tr>
      <td>DescribeAccountPreferences</td>
       <td style="text-align:right">-</td>
    </tr>
    <tr>
      <td>DescribeBackupPolicy</td>
       <td style="text-align:right">-</td>
    </tr>
    <tr>
      <td>DescribeFileSystemPolicy</td>
       <td style="text-align:right">-</td>
    </tr>
    <tr>
      <td>DescribeLifecycleConfiguration</td>
       <td style="text-align:right">-</td>
    </tr>
    <tr>
      <td>DescribeMountTargetSecurityGroups</td>
       <td style="text-align:right">-</td>
    </tr>
    <tr>
      <td>DescribeMountTargets</td>
       <td style="text-align:right">-</td>
    </tr>
    <tr>
      <td>DescribeReplicationConfigurations</td>
       <td style="text-align:right">-</td>
    </tr>
    <tr>
      <td>DescribeTags</td>
       <td style="text-align:right">-</td>
    </tr>
    <tr>
      <td>ListTagsForResource</td>
       <td style="text-align:right">-</td>
    </tr>
    <tr>
      <td>ModifyMountTargetSecurityGroups</td>
       <td style="text-align:right">-</td>
    </tr>
    <tr>
      <td>PutAccountPreferences</td>
       <td style="text-align:right">-</td>
    </tr>
    <tr>
      <td>PutBackupPolicy</td>
       <td style="text-align:right">-</td>
    </tr>
    <tr>
      <td>PutFileSystemPolicy</td>
       <td style="text-align:right">-</td>
    </tr>
    <tr>
      <td>PutLifecycleConfiguration</td>
       <td style="text-align:right">-</td>
    </tr>
    <tr>
      <td>TagResource</td>
       <td style="text-align:right">-</td>
    </tr>
    <tr>
      <td>UntagResource</td>
       <td style="text-align:right">-</td>
    </tr>
    <tr>
      <td>UpdateFileSystem</td>
       <td style="text-align:right">-</td>
    </tr>
  </tbody>
 </table>


## eks ##

<table>
  <thead>
    <tr>
      <th>Operation</th>
      <th style="text-align:right">Implemented</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td>CreateCluster (Pro)  <a href="#misc" title="covered by our integration test suite">✨</a></td>
       <td style="text-align:right">✅</td>
    </tr>
    <tr>
      <td>CreateFargateProfile (Pro) </td>
       <td style="text-align:right">✅</td>
    </tr>
    <tr>
      <td>CreateNodegroup (Pro) </td>
       <td style="text-align:right">✅</td>
    </tr>
    <tr>
      <td>DeleteCluster (Pro)  <a href="#misc" title="covered by our integration test suite">✨</a></td>
       <td style="text-align:right">✅</td>
    </tr>
    <tr>
      <td>DeleteFargateProfile (Pro) </td>
       <td style="text-align:right">✅</td>
    </tr>
    <tr>
      <td>DeleteNodegroup (Pro) </td>
       <td style="text-align:right">✅</td>
    </tr>
    <tr>
      <td>DescribeCluster (Pro)  <a href="#misc" title="covered by our integration test suite">✨</a></td>
       <td style="text-align:right">✅</td>
    </tr>
    <tr>
      <td>DescribeFargateProfile (Pro) </td>
       <td style="text-align:right">✅</td>
    </tr>
    <tr>
      <td>DescribeNodegroup (Pro) </td>
       <td style="text-align:right">✅</td>
    </tr>
    <tr>
      <td>ListClusters (Pro)  <a href="#misc" title="covered by our integration test suite">✨</a></td>
       <td style="text-align:right">✅</td>
    </tr>
    <tr>
      <td>ListFargateProfiles (Pro) </td>
       <td style="text-align:right">✅</td>
    </tr>
    <tr>
      <td>ListNodegroups (Pro) </td>
       <td style="text-align:right">✅</td>
    </tr>
    <tr>
      <td>UpdateClusterConfig (Pro) </td>
       <td style="text-align:right">✅</td>
    </tr>
    <tr>
      <td>UpdateNodegroupConfig (Pro) </td>
       <td style="text-align:right">✅</td>
    </tr>
    <tr>
      <td>UpdateNodegroupVersion (Pro) </td>
       <td style="text-align:right">✅</td>
    </tr>
  </tbody>
  <tbody>    <tr>
      <td><a data-toggle="collapse" href=".eks-notimplemented">Show missing</a></td>
      <td style="text-align:right"></td>
    </tr>
  </tbody>
  <tbody class="collapse eks-notimplemented">     <tr>
      <td>AssociateEncryptionConfig</td>
       <td style="text-align:right">-</td>
    </tr>
    <tr>
      <td>AssociateIdentityProviderConfig</td>
       <td style="text-align:right">-</td>
    </tr>
    <tr>
      <td>CreateAddon</td>
       <td style="text-align:right">-</td>
    </tr>
    <tr>
      <td>DeleteAddon</td>
       <td style="text-align:right">-</td>
    </tr>
    <tr>
      <td>DeregisterCluster</td>
       <td style="text-align:right">-</td>
    </tr>
    <tr>
      <td>DescribeAddon</td>
       <td style="text-align:right">-</td>
    </tr>
    <tr>
      <td>DescribeAddonVersions</td>
       <td style="text-align:right">-</td>
    </tr>
    <tr>
      <td>DescribeIdentityProviderConfig</td>
       <td style="text-align:right">-</td>
    </tr>
    <tr>
      <td>DescribeUpdate</td>
       <td style="text-align:right">-</td>
    </tr>
    <tr>
      <td>DisassociateIdentityProviderConfig</td>
       <td style="text-align:right">-</td>
    </tr>
    <tr>
      <td>ListAddons</td>
       <td style="text-align:right">-</td>
    </tr>
    <tr>
      <td>ListIdentityProviderConfigs</td>
       <td style="text-align:right">-</td>
    </tr>
    <tr>
      <td>ListTagsForResource</td>
       <td style="text-align:right">-</td>
    </tr>
    <tr>
      <td>ListUpdates</td>
       <td style="text-align:right">-</td>
    </tr>
    <tr>
      <td>RegisterCluster</td>
       <td style="text-align:right">-</td>
    </tr>
    <tr>
      <td>TagResource</td>
       <td style="text-align:right">-</td>
    </tr>
    <tr>
      <td>UntagResource</td>
       <td style="text-align:right">-</td>
    </tr>
    <tr>
      <td>UpdateAddon</td>
       <td style="text-align:right">-</td>
    </tr>
    <tr>
      <td>UpdateClusterVersion</td>
       <td style="text-align:right">-</td>
    </tr>
  </tbody>
 </table>


## elasticache ##

<table>
  <thead>
    <tr>
      <th>Operation</th>
      <th style="text-align:right">Implemented</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td>AddTagsToResource (Pro) </td>
       <td style="text-align:right">✅</td>
    </tr>
    <tr>
      <td>CreateCacheCluster (Pro)  <a href="#misc" title="covered by our integration test suite">✨</a></td>
       <td style="text-align:right">✅</td>
    </tr>
    <tr>
      <td>CreateCacheParameterGroup (Pro)  <a href="#misc" title="covered by our integration test suite">✨</a></td>
       <td style="text-align:right">✅</td>
    </tr>
    <tr>
      <td>CreateCacheSecurityGroup (Pro)  <a href="#misc" title="covered by our integration test suite">✨</a></td>
       <td style="text-align:right">✅</td>
    </tr>
    <tr>
      <td>CreateCacheSubnetGroup (Pro)  <a href="#misc" title="covered by our integration test suite">✨</a></td>
       <td style="text-align:right">✅</td>
    </tr>
    <tr>
      <td>CreateReplicationGroup (Pro)  <a href="#misc" title="covered by our integration test suite">✨</a></td>
       <td style="text-align:right">✅</td>
    </tr>
    <tr>
      <td>DeleteCacheCluster (Pro)  <a href="#misc" title="covered by our integration test suite">✨</a></td>
       <td style="text-align:right">✅</td>
    </tr>
    <tr>
      <td>DeleteCacheParameterGroup (Pro)  <a href="#misc" title="covered by our integration test suite">✨</a></td>
       <td style="text-align:right">✅</td>
    </tr>
    <tr>
      <td>DeleteCacheSecurityGroup (Pro)  <a href="#misc" title="covered by our integration test suite">✨</a></td>
       <td style="text-align:right">✅</td>
    </tr>
    <tr>
      <td>DeleteCacheSubnetGroup (Pro)  <a href="#misc" title="covered by our integration test suite">✨</a></td>
       <td style="text-align:right">✅</td>
    </tr>
    <tr>
      <td>DeleteReplicationGroup (Pro)  <a href="#misc" title="covered by our integration test suite">✨</a></td>
       <td style="text-align:right">✅</td>
    </tr>
    <tr>
      <td>DescribeCacheClusters (Pro)  <a href="#misc" title="covered by our integration test suite">✨</a></td>
       <td style="text-align:right">✅</td>
    </tr>
    <tr>
      <td>DescribeCacheParameterGroups (Pro)  <a href="#misc" title="covered by our integration test suite">✨</a></td>
       <td style="text-align:right">✅</td>
    </tr>
    <tr>
      <td>DescribeCacheParameters (Pro)  <a href="#misc" title="covered by our integration test suite">✨</a></td>
       <td style="text-align:right">✅</td>
    </tr>
    <tr>
      <td>DescribeCacheSecurityGroups (Pro)  <a href="#misc" title="covered by our integration test suite">✨</a></td>
       <td style="text-align:right">✅</td>
    </tr>
    <tr>
      <td>DescribeCacheSubnetGroups (Pro)  <a href="#misc" title="covered by our integration test suite">✨</a></td>
       <td style="text-align:right">✅</td>
    </tr>
    <tr>
      <td>DescribeReplicationGroups (Pro)  <a href="#misc" title="covered by our integration test suite">✨</a></td>
       <td style="text-align:right">✅</td>
    </tr>
    <tr>
      <td>ListTagsForResource (Pro) </td>
       <td style="text-align:right">✅</td>
    </tr>
    <tr>
      <td>ModifyCacheCluster (Pro)  <a href="#misc" title="covered by our integration test suite">✨</a></td>
       <td style="text-align:right">✅</td>
    </tr>
    <tr>
      <td>ModifyCacheParameterGroup (Pro)  <a href="#misc" title="covered by our integration test suite">✨</a></td>
       <td style="text-align:right">✅</td>
    </tr>
    <tr>
      <td>ModifyCacheSubnetGroup (Pro)  <a href="#misc" title="covered by our integration test suite">✨</a></td>
       <td style="text-align:right">✅</td>
    </tr>
    <tr>
      <td>ModifyReplicationGroup (Pro)  <a href="#misc" title="covered by our integration test suite">✨</a></td>
       <td style="text-align:right">✅</td>
    </tr>
    <tr>
      <td>RemoveTagsFromResource (Pro) </td>
       <td style="text-align:right">✅</td>
    </tr>
  </tbody>
  <tbody>    <tr>
      <td><a data-toggle="collapse" href=".elasticache-notimplemented">Show missing</a></td>
      <td style="text-align:right"></td>
    </tr>
  </tbody>
  <tbody class="collapse elasticache-notimplemented">     <tr>
      <td>AuthorizeCacheSecurityGroupIngress</td>
       <td style="text-align:right">-</td>
    </tr>
    <tr>
      <td>BatchApplyUpdateAction</td>
       <td style="text-align:right">-</td>
    </tr>
    <tr>
      <td>BatchStopUpdateAction</td>
       <td style="text-align:right">-</td>
    </tr>
    <tr>
      <td>CompleteMigration</td>
       <td style="text-align:right">-</td>
    </tr>
    <tr>
      <td>CopySnapshot</td>
       <td style="text-align:right">-</td>
    </tr>
    <tr>
      <td>CreateGlobalReplicationGroup</td>
       <td style="text-align:right">-</td>
    </tr>
    <tr>
      <td>CreateSnapshot</td>
       <td style="text-align:right">-</td>
    </tr>
    <tr>
      <td>CreateUser</td>
       <td style="text-align:right">-</td>
    </tr>
    <tr>
      <td>CreateUserGroup</td>
       <td style="text-align:right">-</td>
    </tr>
    <tr>
      <td>DecreaseNodeGroupsInGlobalReplicationGroup</td>
       <td style="text-align:right">-</td>
    </tr>
    <tr>
      <td>DecreaseReplicaCount</td>
       <td style="text-align:right">-</td>
    </tr>
    <tr>
      <td>DeleteGlobalReplicationGroup</td>
       <td style="text-align:right">-</td>
    </tr>
    <tr>
      <td>DeleteSnapshot</td>
       <td style="text-align:right">-</td>
    </tr>
    <tr>
      <td>DeleteUser</td>
       <td style="text-align:right">-</td>
    </tr>
    <tr>
      <td>DeleteUserGroup</td>
       <td style="text-align:right">-</td>
    </tr>
    <tr>
      <td>DescribeCacheEngineVersions</td>
       <td style="text-align:right">-</td>
    </tr>
    <tr>
      <td>DescribeEngineDefaultParameters</td>
       <td style="text-align:right">-</td>
    </tr>
    <tr>
      <td>DescribeEvents</td>
       <td style="text-align:right">-</td>
    </tr>
    <tr>
      <td>DescribeGlobalReplicationGroups</td>
       <td style="text-align:right">-</td>
    </tr>
    <tr>
      <td>DescribeReservedCacheNodes</td>
       <td style="text-align:right">-</td>
    </tr>
    <tr>
      <td>DescribeReservedCacheNodesOfferings</td>
       <td style="text-align:right">-</td>
    </tr>
    <tr>
      <td>DescribeServiceUpdates</td>
       <td style="text-align:right">-</td>
    </tr>
    <tr>
      <td>DescribeSnapshots</td>
       <td style="text-align:right">-</td>
    </tr>
    <tr>
      <td>DescribeUpdateActions</td>
       <td style="text-align:right">-</td>
    </tr>
    <tr>
      <td>DescribeUserGroups</td>
       <td style="text-align:right">-</td>
    </tr>
    <tr>
      <td>DescribeUsers</td>
       <td style="text-align:right">-</td>
    </tr>
    <tr>
      <td>DisassociateGlobalReplicationGroup</td>
       <td style="text-align:right">-</td>
    </tr>
    <tr>
      <td>FailoverGlobalReplicationGroup</td>
       <td style="text-align:right">-</td>
    </tr>
    <tr>
      <td>IncreaseNodeGroupsInGlobalReplicationGroup</td>
       <td style="text-align:right">-</td>
    </tr>
    <tr>
      <td>IncreaseReplicaCount</td>
       <td style="text-align:right">-</td>
    </tr>
    <tr>
      <td>ListAllowedNodeTypeModifications</td>
       <td style="text-align:right">-</td>
    </tr>
    <tr>
      <td>ModifyGlobalReplicationGroup</td>
       <td style="text-align:right">-</td>
    </tr>
    <tr>
      <td>ModifyReplicationGroupShardConfiguration</td>
       <td style="text-align:right">-</td>
    </tr>
    <tr>
      <td>ModifyUser</td>
       <td style="text-align:right">-</td>
    </tr>
    <tr>
      <td>ModifyUserGroup</td>
       <td style="text-align:right">-</td>
    </tr>
    <tr>
      <td>PurchaseReservedCacheNodesOffering</td>
       <td style="text-align:right">-</td>
    </tr>
    <tr>
      <td>RebalanceSlotsInGlobalReplicationGroup</td>
       <td style="text-align:right">-</td>
    </tr>
    <tr>
      <td>RebootCacheCluster</td>
       <td style="text-align:right">-</td>
    </tr>
    <tr>
      <td>ResetCacheParameterGroup</td>
       <td style="text-align:right">-</td>
    </tr>
    <tr>
      <td>RevokeCacheSecurityGroupIngress</td>
       <td style="text-align:right">-</td>
    </tr>
    <tr>
      <td>StartMigration</td>
       <td style="text-align:right">-</td>
    </tr>
    <tr>
      <td>TestFailover</td>
       <td style="text-align:right">-</td>
    </tr>
  </tbody>
 </table>


## elasticbeanstalk ##

<table>
  <thead>
    <tr>
      <th>Operation</th>
      <th style="text-align:right">Implemented</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td>CreateApplication (Pro)  <a href="#misc" title="covered by our integration test suite">✨</a></td>
       <td style="text-align:right">✅</td>
    </tr>
    <tr>
      <td>CreateApplicationVersion (Pro)  <a href="#misc" title="covered by our integration test suite">✨</a></td>
       <td style="text-align:right">✅</td>
    </tr>
    <tr>
      <td>CreateEnvironment (Pro)  <a href="#misc" title="covered by our integration test suite">✨</a></td>
       <td style="text-align:right">✅</td>
    </tr>
    <tr>
      <td>DeleteApplication (Pro)  <a href="#misc" title="covered by our integration test suite">✨</a></td>
       <td style="text-align:right">✅</td>
    </tr>
    <tr>
      <td>DeleteApplicationVersion (Pro)  <a href="#misc" title="covered by our integration test suite">✨</a></td>
       <td style="text-align:right">✅</td>
    </tr>
    <tr>
      <td>DeleteEnvironmentConfiguration (Pro)  <a href="#misc" title="covered by our integration test suite">✨</a></td>
       <td style="text-align:right">✅</td>
    </tr>
    <tr>
      <td>DescribeApplicationVersions (Pro)  <a href="#misc" title="covered by our integration test suite">✨</a></td>
       <td style="text-align:right">✅</td>
    </tr>
    <tr>
      <td>DescribeApplications (Pro)  <a href="#misc" title="covered by our integration test suite">✨</a></td>
       <td style="text-align:right">✅</td>
    </tr>
    <tr>
      <td>DescribeEnvironments (Pro)  <a href="#misc" title="covered by our integration test suite">✨</a></td>
       <td style="text-align:right">✅</td>
    </tr>
    <tr>
      <td>UpdateApplication (Pro)  <a href="#misc" title="covered by our integration test suite">✨</a></td>
       <td style="text-align:right">✅</td>
    </tr>
    <tr>
      <td>UpdateApplicationVersion (Pro)  <a href="#misc" title="covered by our integration test suite">✨</a></td>
       <td style="text-align:right">✅</td>
    </tr>
    <tr>
      <td>UpdateEnvironment (Pro)  <a href="#misc" title="covered by our integration test suite">✨</a></td>
       <td style="text-align:right">✅</td>
    </tr>
  </tbody>
  <tbody>    <tr>
      <td><a data-toggle="collapse" href=".elasticbeanstalk-notimplemented">Show missing</a></td>
      <td style="text-align:right"></td>
    </tr>
  </tbody>
  <tbody class="collapse elasticbeanstalk-notimplemented">     <tr>
      <td>AbortEnvironmentUpdate</td>
       <td style="text-align:right">-</td>
    </tr>
    <tr>
      <td>ApplyEnvironmentManagedAction</td>
       <td style="text-align:right">-</td>
    </tr>
    <tr>
      <td>AssociateEnvironmentOperationsRole</td>
       <td style="text-align:right">-</td>
    </tr>
    <tr>
      <td>CheckDNSAvailability</td>
       <td style="text-align:right">-</td>
    </tr>
    <tr>
      <td>ComposeEnvironments</td>
       <td style="text-align:right">-</td>
    </tr>
    <tr>
      <td>CreateConfigurationTemplate</td>
       <td style="text-align:right">-</td>
    </tr>
    <tr>
      <td>CreatePlatformVersion</td>
       <td style="text-align:right">-</td>
    </tr>
    <tr>
      <td>CreateStorageLocation</td>
       <td style="text-align:right">-</td>
    </tr>
    <tr>
      <td>DeleteConfigurationTemplate</td>
       <td style="text-align:right">-</td>
    </tr>
    <tr>
      <td>DeletePlatformVersion</td>
       <td style="text-align:right">-</td>
    </tr>
    <tr>
      <td>DescribeAccountAttributes</td>
       <td style="text-align:right">-</td>
    </tr>
    <tr>
      <td>DescribeConfigurationOptions</td>
       <td style="text-align:right">-</td>
    </tr>
    <tr>
      <td>DescribeConfigurationSettings</td>
       <td style="text-align:right">-</td>
    </tr>
    <tr>
      <td>DescribeEnvironmentHealth</td>
       <td style="text-align:right">-</td>
    </tr>
    <tr>
      <td>DescribeEnvironmentManagedActionHistory</td>
       <td style="text-align:right">-</td>
    </tr>
    <tr>
      <td>DescribeEnvironmentManagedActions</td>
       <td style="text-align:right">-</td>
    </tr>
    <tr>
      <td>DescribeEnvironmentResources</td>
       <td style="text-align:right">-</td>
    </tr>
    <tr>
      <td>DescribeEvents</td>
       <td style="text-align:right">-</td>
    </tr>
    <tr>
      <td>DescribeInstancesHealth</td>
       <td style="text-align:right">-</td>
    </tr>
    <tr>
      <td>DescribePlatformVersion</td>
       <td style="text-align:right">-</td>
    </tr>
    <tr>
      <td>DisassociateEnvironmentOperationsRole</td>
       <td style="text-align:right">-</td>
    </tr>
    <tr>
      <td>ListAvailableSolutionStacks</td>
       <td style="text-align:right">-</td>
    </tr>
    <tr>
      <td>ListPlatformBranches</td>
       <td style="text-align:right">-</td>
    </tr>
    <tr>
      <td>ListPlatformVersions</td>
       <td style="text-align:right">-</td>
    </tr>
    <tr>
      <td>ListTagsForResource</td>
       <td style="text-align:right">-</td>
    </tr>
    <tr>
      <td>RebuildEnvironment</td>
       <td style="text-align:right">-</td>
    </tr>
    <tr>
      <td>RequestEnvironmentInfo</td>
       <td style="text-align:right">-</td>
    </tr>
    <tr>
      <td>RestartAppServer</td>
       <td style="text-align:right">-</td>
    </tr>
    <tr>
      <td>RetrieveEnvironmentInfo</td>
       <td style="text-align:right">-</td>
    </tr>
    <tr>
      <td>SwapEnvironmentCNAMEs</td>
       <td style="text-align:right">-</td>
    </tr>
    <tr>
      <td>TerminateEnvironment</td>
       <td style="text-align:right">-</td>
    </tr>
    <tr>
      <td>UpdateApplicationResourceLifecycle</td>
       <td style="text-align:right">-</td>
    </tr>
    <tr>
      <td>UpdateConfigurationTemplate</td>
       <td style="text-align:right">-</td>
    </tr>
    <tr>
      <td>UpdateTagsForResource</td>
       <td style="text-align:right">-</td>
    </tr>
    <tr>
      <td>ValidateConfigurationSettings</td>
       <td style="text-align:right">-</td>
    </tr>
  </tbody>
 </table>


## elb ##

<table>
  <thead>
    <tr>
      <th>Operation</th>
      <th style="text-align:right">Implemented</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td>AddTags (Pro) </td>
       <td style="text-align:right">✅</td>
    </tr>
    <tr>
      <td>ApplySecurityGroupsToLoadBalancer (Pro) </td>
       <td style="text-align:right">✅</td>
    </tr>
    <tr>
      <td>AttachLoadBalancerToSubnets (Pro) </td>
       <td style="text-align:right">✅</td>
    </tr>
    <tr>
      <td>ConfigureHealthCheck (Pro) </td>
       <td style="text-align:right">✅</td>
    </tr>
    <tr>
      <td>CreateAppCookieStickinessPolicy (Pro) </td>
       <td style="text-align:right">✅</td>
    </tr>
    <tr>
      <td>CreateLBCookieStickinessPolicy (Pro) </td>
       <td style="text-align:right">✅</td>
    </tr>
    <tr>
      <td>CreateLoadBalancer (Pro) </td>
       <td style="text-align:right">✅</td>
    </tr>
    <tr>
      <td>CreateLoadBalancerListeners (Pro) </td>
       <td style="text-align:right">✅</td>
    </tr>
    <tr>
      <td>CreateLoadBalancerPolicy (Pro) </td>
       <td style="text-align:right">✅</td>
    </tr>
    <tr>
      <td>DeleteLoadBalancer (Pro) </td>
       <td style="text-align:right">✅</td>
    </tr>
    <tr>
      <td>DeleteLoadBalancerListeners (Pro) </td>
       <td style="text-align:right">✅</td>
    </tr>
    <tr>
      <td>DeleteLoadBalancerPolicy (Pro) </td>
       <td style="text-align:right">✅</td>
    </tr>
    <tr>
      <td>DeregisterInstancesFromLoadBalancer (Pro) </td>
       <td style="text-align:right">✅</td>
    </tr>
    <tr>
      <td>DescribeInstanceHealth (Pro) </td>
       <td style="text-align:right">✅</td>
    </tr>
    <tr>
      <td>DescribeLoadBalancerAttributes (Pro) </td>
       <td style="text-align:right">✅</td>
    </tr>
    <tr>
      <td>DescribeLoadBalancerPolicies (Pro) </td>
       <td style="text-align:right">✅</td>
    </tr>
    <tr>
      <td>DescribeLoadBalancers (Pro) </td>
       <td style="text-align:right">✅</td>
    </tr>
    <tr>
      <td>DescribeTags (Pro) </td>
       <td style="text-align:right">✅</td>
    </tr>
    <tr>
      <td>DetachLoadBalancerFromSubnets (Pro) </td>
       <td style="text-align:right">✅</td>
    </tr>
    <tr>
      <td>DisableAvailabilityZonesForLoadBalancer (Pro) </td>
       <td style="text-align:right">✅</td>
    </tr>
    <tr>
      <td>EnableAvailabilityZonesForLoadBalancer (Pro) </td>
       <td style="text-align:right">✅</td>
    </tr>
    <tr>
      <td>ModifyLoadBalancerAttributes (Pro) </td>
       <td style="text-align:right">✅</td>
    </tr>
    <tr>
      <td>RegisterInstancesWithLoadBalancer (Pro) </td>
       <td style="text-align:right">✅</td>
    </tr>
    <tr>
      <td>RemoveTags (Pro) </td>
       <td style="text-align:right">✅</td>
    </tr>
    <tr>
      <td>SetLoadBalancerListenerSSLCertificate (Pro) </td>
       <td style="text-align:right">✅</td>
    </tr>
    <tr>
      <td>SetLoadBalancerPoliciesForBackendServer (Pro) </td>
       <td style="text-align:right">✅</td>
    </tr>
    <tr>
      <td>SetLoadBalancerPoliciesOfListener (Pro) </td>
       <td style="text-align:right">✅</td>
    </tr>
  </tbody>
  <tbody>    <tr>
      <td><a data-toggle="collapse" href=".elb-notimplemented">Show missing</a></td>
      <td style="text-align:right"></td>
    </tr>
  </tbody>
  <tbody class="collapse elb-notimplemented">     <tr>
      <td>DescribeAccountLimits</td>
       <td style="text-align:right">-</td>
    </tr>
    <tr>
      <td>DescribeLoadBalancerPolicyTypes</td>
       <td style="text-align:right">-</td>
    </tr>
  </tbody>
 </table>


## elbv2 ##

<table>
  <thead>
    <tr>
      <th>Operation</th>
      <th style="text-align:right">Implemented</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td>AddListenerCertificates (Pro) </td>
       <td style="text-align:right">✅</td>
    </tr>
    <tr>
      <td>AddTags (Pro) </td>
       <td style="text-align:right">✅</td>
    </tr>
    <tr>
      <td>CreateListener (Pro)  <a href="#misc" title="covered by our integration test suite">✨</a></td>
       <td style="text-align:right">✅</td>
    </tr>
    <tr>
      <td>CreateLoadBalancer (Pro)  <a href="#misc" title="covered by our integration test suite">✨</a></td>
       <td style="text-align:right">✅</td>
    </tr>
    <tr>
      <td>CreateRule (Pro)  <a href="#misc" title="covered by our integration test suite">✨</a></td>
       <td style="text-align:right">✅</td>
    </tr>
    <tr>
      <td>CreateTargetGroup (Pro)  <a href="#misc" title="covered by our integration test suite">✨</a></td>
       <td style="text-align:right">✅</td>
    </tr>
    <tr>
      <td>DeleteListener (Pro)  <a href="#misc" title="covered by our integration test suite">✨</a></td>
       <td style="text-align:right">✅</td>
    </tr>
    <tr>
      <td>DeleteLoadBalancer (Pro)  <a href="#misc" title="covered by our integration test suite">✨</a></td>
       <td style="text-align:right">✅</td>
    </tr>
    <tr>
      <td>DeleteRule (Pro) </td>
       <td style="text-align:right">✅</td>
    </tr>
    <tr>
      <td>DeleteTargetGroup (Pro)  <a href="#misc" title="covered by our integration test suite">✨</a></td>
       <td style="text-align:right">✅</td>
    </tr>
    <tr>
      <td>DeregisterTargets (Pro)  <a href="#misc" title="covered by our integration test suite">✨</a></td>
       <td style="text-align:right">✅</td>
    </tr>
    <tr>
      <td>DescribeAccountLimits (Pro) </td>
       <td style="text-align:right">✅</td>
    </tr>
    <tr>
      <td>DescribeListenerCertificates (Pro) </td>
       <td style="text-align:right">✅</td>
    </tr>
    <tr>
      <td>DescribeListeners (Pro)  <a href="#misc" title="covered by our integration test suite">✨</a></td>
       <td style="text-align:right">✅</td>
    </tr>
    <tr>
      <td>DescribeLoadBalancerAttributes (Pro)  <a href="#misc" title="covered by our integration test suite">✨</a></td>
       <td style="text-align:right">✅</td>
    </tr>
    <tr>
      <td>DescribeLoadBalancers (Pro)  <a href="#misc" title="covered by our integration test suite">✨</a></td>
       <td style="text-align:right">✅</td>
    </tr>
    <tr>
      <td>DescribeRules (Pro)  <a href="#misc" title="covered by our integration test suite">✨</a></td>
       <td style="text-align:right">✅</td>
    </tr>
    <tr>
      <td>DescribeSSLPolicies (Pro) </td>
       <td style="text-align:right">✅</td>
    </tr>
    <tr>
      <td>DescribeTags (Pro) </td>
       <td style="text-align:right">✅</td>
    </tr>
    <tr>
      <td>DescribeTargetGroupAttributes (Pro) </td>
       <td style="text-align:right">✅</td>
    </tr>
    <tr>
      <td>DescribeTargetGroups (Pro)  <a href="#misc" title="covered by our integration test suite">✨</a></td>
       <td style="text-align:right">✅</td>
    </tr>
    <tr>
      <td>DescribeTargetHealth (Pro)  <a href="#misc" title="covered by our integration test suite">✨</a></td>
       <td style="text-align:right">✅</td>
    </tr>
    <tr>
      <td>ModifyListener (Pro) </td>
       <td style="text-align:right">✅</td>
    </tr>
    <tr>
      <td>ModifyLoadBalancerAttributes (Pro)  <a href="#misc" title="covered by our integration test suite">✨</a></td>
       <td style="text-align:right">✅</td>
    </tr>
    <tr>
      <td>ModifyRule (Pro) </td>
       <td style="text-align:right">✅</td>
    </tr>
    <tr>
      <td>ModifyTargetGroup (Pro) </td>
       <td style="text-align:right">✅</td>
    </tr>
    <tr>
      <td>ModifyTargetGroupAttributes (Pro)  <a href="#misc" title="covered by our integration test suite">✨</a></td>
       <td style="text-align:right">✅</td>
    </tr>
    <tr>
      <td>RegisterTargets (Pro)  <a href="#misc" title="covered by our integration test suite">✨</a></td>
       <td style="text-align:right">✅</td>
    </tr>
    <tr>
      <td>RemoveListenerCertificates (Pro) </td>
       <td style="text-align:right">✅</td>
    </tr>
    <tr>
      <td>RemoveTags (Pro) </td>
       <td style="text-align:right">✅</td>
    </tr>
    <tr>
      <td>SetIpAddressType (Pro)  <a href="#misc" title="covered by our integration test suite">✨</a></td>
       <td style="text-align:right">✅</td>
    </tr>
    <tr>
      <td>SetRulePriorities (Pro) </td>
       <td style="text-align:right">✅</td>
    </tr>
    <tr>
      <td>SetSecurityGroups (Pro) </td>
       <td style="text-align:right">✅</td>
    </tr>
    <tr>
      <td>SetSubnets (Pro) </td>
       <td style="text-align:right">✅</td>
    </tr>
  </tbody>
 </table>


## emr ##

<table>
  <thead>
    <tr>
      <th>Operation</th>
      <th style="text-align:right">Implemented</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td>AddInstanceFleet (Pro)  <a href="#misc" title="covered by our integration test suite">✨</a></td>
       <td style="text-align:right">✅</td>
    </tr>
    <tr>
      <td>AddInstanceGroups (Pro) </td>
       <td style="text-align:right">✅</td>
    </tr>
    <tr>
      <td>AddJobFlowSteps (Pro) </td>
       <td style="text-align:right">✅</td>
    </tr>
    <tr>
      <td>AddTags (Pro) </td>
       <td style="text-align:right">✅</td>
    </tr>
    <tr>
      <td>CreateSecurityConfiguration (Pro) </td>
       <td style="text-align:right">✅</td>
    </tr>
    <tr>
      <td>DeleteSecurityConfiguration (Pro) </td>
       <td style="text-align:right">✅</td>
    </tr>
    <tr>
      <td>DescribeCluster (Pro) </td>
       <td style="text-align:right">✅</td>
    </tr>
    <tr>
      <td>DescribeJobFlows (Pro) </td>
       <td style="text-align:right">✅</td>
    </tr>
    <tr>
      <td>DescribeSecurityConfiguration (Pro) </td>
       <td style="text-align:right">✅</td>
    </tr>
    <tr>
      <td>DescribeStep (Pro) </td>
       <td style="text-align:right">✅</td>
    </tr>
    <tr>
      <td>GetAutoTerminationPolicy (Pro)  <a href="#misc" title="covered by our integration test suite">✨</a></td>
       <td style="text-align:right">✅</td>
    </tr>
    <tr>
      <td>GetBlockPublicAccessConfiguration (Pro) </td>
       <td style="text-align:right">✅</td>
    </tr>
    <tr>
      <td>ListBootstrapActions (Pro) </td>
       <td style="text-align:right">✅</td>
    </tr>
    <tr>
      <td>ListClusters (Pro)  <a href="#misc" title="covered by our integration test suite">✨</a></td>
       <td style="text-align:right">✅</td>
    </tr>
    <tr>
      <td>ListInstanceFleets (Pro)  <a href="#misc" title="covered by our integration test suite">✨</a></td>
       <td style="text-align:right">✅</td>
    </tr>
    <tr>
      <td>ListInstanceGroups (Pro) </td>
       <td style="text-align:right">✅</td>
    </tr>
    <tr>
      <td>ListInstances (Pro) </td>
       <td style="text-align:right">✅</td>
    </tr>
    <tr>
      <td>ListSteps (Pro) </td>
       <td style="text-align:right">✅</td>
    </tr>
    <tr>
      <td>ModifyCluster (Pro) </td>
       <td style="text-align:right">✅</td>
    </tr>
    <tr>
      <td>ModifyInstanceFleet (Pro)  <a href="#misc" title="covered by our integration test suite">✨</a></td>
       <td style="text-align:right">✅</td>
    </tr>
    <tr>
      <td>ModifyInstanceGroups (Pro) </td>
       <td style="text-align:right">✅</td>
    </tr>
    <tr>
      <td>PutAutoScalingPolicy (Pro) </td>
       <td style="text-align:right">✅</td>
    </tr>
    <tr>
      <td>PutAutoTerminationPolicy (Pro)  <a href="#misc" title="covered by our integration test suite">✨</a></td>
       <td style="text-align:right">✅</td>
    </tr>
    <tr>
      <td>RemoveAutoScalingPolicy (Pro) </td>
       <td style="text-align:right">✅</td>
    </tr>
    <tr>
      <td>RemoveAutoTerminationPolicy (Pro)  <a href="#misc" title="covered by our integration test suite">✨</a></td>
       <td style="text-align:right">✅</td>
    </tr>
    <tr>
      <td>RemoveTags (Pro) </td>
       <td style="text-align:right">✅</td>
    </tr>
    <tr>
      <td>RunJobFlow (Pro)  <a href="#misc" title="covered by our integration test suite">✨</a></td>
       <td style="text-align:right">✅</td>
    </tr>
    <tr>
      <td>SetTerminationProtection (Pro) </td>
       <td style="text-align:right">✅</td>
    </tr>
    <tr>
      <td>SetVisibleToAllUsers (Pro) </td>
       <td style="text-align:right">✅</td>
    </tr>
    <tr>
      <td>TerminateJobFlows (Pro) </td>
       <td style="text-align:right">✅</td>
    </tr>
  </tbody>
  <tbody>    <tr>
      <td><a data-toggle="collapse" href=".emr-notimplemented">Show missing</a></td>
      <td style="text-align:right"></td>
    </tr>
  </tbody>
  <tbody class="collapse emr-notimplemented">     <tr>
      <td>CancelSteps</td>
       <td style="text-align:right">-</td>
    </tr>
    <tr>
      <td>CreateStudio</td>
       <td style="text-align:right">-</td>
    </tr>
    <tr>
      <td>CreateStudioSessionMapping</td>
       <td style="text-align:right">-</td>
    </tr>
    <tr>
      <td>DeleteStudio</td>
       <td style="text-align:right">-</td>
    </tr>
    <tr>
      <td>DeleteStudioSessionMapping</td>
       <td style="text-align:right">-</td>
    </tr>
    <tr>
      <td>DescribeNotebookExecution</td>
       <td style="text-align:right">-</td>
    </tr>
    <tr>
      <td>DescribeReleaseLabel</td>
       <td style="text-align:right">-</td>
    </tr>
    <tr>
      <td>DescribeStudio</td>
       <td style="text-align:right">-</td>
    </tr>
    <tr>
      <td>GetManagedScalingPolicy</td>
       <td style="text-align:right">-</td>
    </tr>
    <tr>
      <td>GetStudioSessionMapping</td>
       <td style="text-align:right">-</td>
    </tr>
    <tr>
      <td>ListNotebookExecutions</td>
       <td style="text-align:right">-</td>
    </tr>
    <tr>
      <td>ListReleaseLabels</td>
       <td style="text-align:right">-</td>
    </tr>
    <tr>
      <td>ListSecurityConfigurations</td>
       <td style="text-align:right">-</td>
    </tr>
    <tr>
      <td>ListStudioSessionMappings</td>
       <td style="text-align:right">-</td>
    </tr>
    <tr>
      <td>ListStudios</td>
       <td style="text-align:right">-</td>
    </tr>
    <tr>
      <td>PutBlockPublicAccessConfiguration</td>
       <td style="text-align:right">-</td>
    </tr>
    <tr>
      <td>PutManagedScalingPolicy</td>
       <td style="text-align:right">-</td>
    </tr>
    <tr>
      <td>RemoveManagedScalingPolicy</td>
       <td style="text-align:right">-</td>
    </tr>
    <tr>
      <td>StartNotebookExecution</td>
       <td style="text-align:right">-</td>
    </tr>
    <tr>
      <td>StopNotebookExecution</td>
       <td style="text-align:right">-</td>
    </tr>
    <tr>
      <td>UpdateStudio</td>
       <td style="text-align:right">-</td>
    </tr>
    <tr>
      <td>UpdateStudioSessionMapping</td>
       <td style="text-align:right">-</td>
    </tr>
  </tbody>
 </table>


## es ##

<table>
  <thead>
    <tr>
      <th>Operation</th>
      <th style="text-align:right">Implemented</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td>AddTags <a href="#misc" title="covered by our integration test suite">✨</a></td>
       <td style="text-align:right">✅</td>
    </tr>
    <tr>
      <td>CreateElasticsearchDomain <a href="#misc" title="covered by our integration test suite">✨</a></td>
       <td style="text-align:right">✅</td>
    </tr>
    <tr>
      <td>DeleteElasticsearchDomain <a href="#misc" title="covered by our integration test suite">✨</a></td>
       <td style="text-align:right">✅</td>
    </tr>
    <tr>
      <td>DescribeElasticsearchDomain <a href="#misc" title="covered by our integration test suite">✨</a></td>
       <td style="text-align:right">✅</td>
    </tr>
    <tr>
      <td>DescribeElasticsearchDomainConfig <a href="#misc" title="covered by our integration test suite">✨</a></td>
       <td style="text-align:right">✅</td>
    </tr>
    <tr>
      <td>DescribeElasticsearchDomains <a href="#misc" title="covered by our integration test suite">✨</a></td>
       <td style="text-align:right">✅</td>
    </tr>
    <tr>
      <td>GetCompatibleElasticsearchVersions <a href="#misc" title="covered by our integration test suite">✨</a></td>
       <td style="text-align:right">✅</td>
    </tr>
    <tr>
      <td>ListDomainNames <a href="#misc" title="covered by our integration test suite">✨</a></td>
       <td style="text-align:right">✅</td>
    </tr>
    <tr>
      <td>ListElasticsearchVersions <a href="#misc" title="covered by our integration test suite">✨</a></td>
       <td style="text-align:right">✅</td>
    </tr>
    <tr>
      <td>ListTags <a href="#misc" title="covered by our integration test suite">✨</a></td>
       <td style="text-align:right">✅</td>
    </tr>
    <tr>
      <td>RemoveTags</td>
       <td style="text-align:right">✅</td>
    </tr>
    <tr>
      <td>UpdateElasticsearchDomainConfig <a href="#misc" title="covered by our integration test suite">✨</a></td>
       <td style="text-align:right">✅</td>
    </tr>
  </tbody>
  <tbody>    <tr>
      <td><a data-toggle="collapse" href=".es-notimplemented">Show missing</a></td>
      <td style="text-align:right"></td>
    </tr>
  </tbody>
  <tbody class="collapse es-notimplemented">     <tr>
      <td>AcceptInboundCrossClusterSearchConnection</td>
       <td style="text-align:right">-</td>
    </tr>
    <tr>
      <td>AssociatePackage</td>
       <td style="text-align:right">-</td>
    </tr>
    <tr>
      <td>CancelElasticsearchServiceSoftwareUpdate</td>
       <td style="text-align:right">-</td>
    </tr>
    <tr>
      <td>CreateOutboundCrossClusterSearchConnection</td>
       <td style="text-align:right">-</td>
    </tr>
    <tr>
      <td>CreatePackage</td>
       <td style="text-align:right">-</td>
    </tr>
    <tr>
      <td>DeleteElasticsearchServiceRole</td>
       <td style="text-align:right">-</td>
    </tr>
    <tr>
      <td>DeleteInboundCrossClusterSearchConnection</td>
       <td style="text-align:right">-</td>
    </tr>
    <tr>
      <td>DeleteOutboundCrossClusterSearchConnection</td>
       <td style="text-align:right">-</td>
    </tr>
    <tr>
      <td>DeletePackage</td>
       <td style="text-align:right">-</td>
    </tr>
    <tr>
      <td>DescribeDomainAutoTunes</td>
       <td style="text-align:right">-</td>
    </tr>
    <tr>
      <td>DescribeDomainChangeProgress</td>
       <td style="text-align:right">-</td>
    </tr>
    <tr>
      <td>DescribeElasticsearchInstanceTypeLimits</td>
       <td style="text-align:right">-</td>
    </tr>
    <tr>
      <td>DescribeInboundCrossClusterSearchConnections</td>
       <td style="text-align:right">-</td>
    </tr>
    <tr>
      <td>DescribeOutboundCrossClusterSearchConnections</td>
       <td style="text-align:right">-</td>
    </tr>
    <tr>
      <td>DescribePackages</td>
       <td style="text-align:right">-</td>
    </tr>
    <tr>
      <td>DescribeReservedElasticsearchInstanceOfferings</td>
       <td style="text-align:right">-</td>
    </tr>
    <tr>
      <td>DescribeReservedElasticsearchInstances</td>
       <td style="text-align:right">-</td>
    </tr>
    <tr>
      <td>DissociatePackage</td>
       <td style="text-align:right">-</td>
    </tr>
    <tr>
      <td>GetPackageVersionHistory</td>
       <td style="text-align:right">-</td>
    </tr>
    <tr>
      <td>GetUpgradeHistory</td>
       <td style="text-align:right">-</td>
    </tr>
    <tr>
      <td>GetUpgradeStatus</td>
       <td style="text-align:right">-</td>
    </tr>
    <tr>
      <td>ListDomainsForPackage</td>
       <td style="text-align:right">-</td>
    </tr>
    <tr>
      <td>ListElasticsearchInstanceTypes</td>
       <td style="text-align:right">-</td>
    </tr>
    <tr>
      <td>ListPackagesForDomain</td>
       <td style="text-align:right">-</td>
    </tr>
    <tr>
      <td>PurchaseReservedElasticsearchInstanceOffering</td>
       <td style="text-align:right">-</td>
    </tr>
    <tr>
      <td>RejectInboundCrossClusterSearchConnection</td>
       <td style="text-align:right">-</td>
    </tr>
    <tr>
      <td>StartElasticsearchServiceSoftwareUpdate</td>
       <td style="text-align:right">-</td>
    </tr>
    <tr>
      <td>UpdatePackage</td>
       <td style="text-align:right">-</td>
    </tr>
    <tr>
      <td>UpgradeElasticsearchDomain</td>
       <td style="text-align:right">-</td>
    </tr>
  </tbody>
 </table>


## events ##

<table>
  <thead>
    <tr>
      <th>Operation</th>
      <th style="text-align:right">Implemented</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td>CancelReplay</td>
       <td style="text-align:right">✅</td>
    </tr>
    <tr>
      <td>CreateApiDestination <a href="#misc" title="covered by our integration test suite">✨</a></td>
       <td style="text-align:right">✅</td>
    </tr>
    <tr>
      <td>CreateArchive</td>
       <td style="text-align:right">✅</td>
    </tr>
    <tr>
      <td>CreateConnection <a href="#misc" title="covered by our integration test suite">✨</a></td>
       <td style="text-align:right">✅</td>
    </tr>
    <tr>
      <td>CreateEventBus <a href="#misc" title="covered by our integration test suite">✨</a></td>
       <td style="text-align:right">✅</td>
    </tr>
    <tr>
      <td>DeleteApiDestination <a href="#misc" title="covered by our integration test suite">✨</a></td>
       <td style="text-align:right">✅</td>
    </tr>
    <tr>
      <td>DeleteArchive</td>
       <td style="text-align:right">✅</td>
    </tr>
    <tr>
      <td>DeleteConnection <a href="#misc" title="covered by our integration test suite">✨</a></td>
       <td style="text-align:right">✅</td>
    </tr>
    <tr>
      <td>DeleteEventBus <a href="#misc" title="covered by our integration test suite">✨</a></td>
       <td style="text-align:right">✅</td>
    </tr>
    <tr>
      <td>DeleteRule <a href="#misc" title="covered by our integration test suite">✨</a></td>
       <td style="text-align:right">✅</td>
    </tr>
    <tr>
      <td>DescribeApiDestination <a href="#misc" title="covered by our integration test suite">✨</a></td>
       <td style="text-align:right">✅</td>
    </tr>
    <tr>
      <td>DescribeArchive</td>
       <td style="text-align:right">✅</td>
    </tr>
    <tr>
      <td>DescribeConnection <a href="#misc" title="covered by our integration test suite">✨</a></td>
       <td style="text-align:right">✅</td>
    </tr>
    <tr>
      <td>DescribeEventBus <a href="#misc" title="covered by our integration test suite">✨</a></td>
       <td style="text-align:right">✅</td>
    </tr>
    <tr>
      <td>DescribeReplay</td>
       <td style="text-align:right">✅</td>
    </tr>
    <tr>
      <td>DescribeRule <a href="#misc" title="covered by our integration test suite">✨</a></td>
       <td style="text-align:right">✅</td>
    </tr>
    <tr>
      <td>DisableRule <a href="#misc" title="covered by our integration test suite">✨</a></td>
       <td style="text-align:right">✅</td>
    </tr>
    <tr>
      <td>EnableRule</td>
       <td style="text-align:right">✅</td>
    </tr>
    <tr>
      <td>ListApiDestinations</td>
       <td style="text-align:right">✅</td>
    </tr>
    <tr>
      <td>ListArchives</td>
       <td style="text-align:right">✅</td>
    </tr>
    <tr>
      <td>ListConnections <a href="#misc" title="covered by our integration test suite">✨</a></td>
       <td style="text-align:right">✅</td>
    </tr>
    <tr>
      <td>ListEventBuses <a href="#misc" title="covered by our integration test suite">✨</a></td>
       <td style="text-align:right">✅</td>
    </tr>
    <tr>
      <td>ListReplays</td>
       <td style="text-align:right">✅</td>
    </tr>
    <tr>
      <td>ListRuleNamesByTarget</td>
       <td style="text-align:right">✅</td>
    </tr>
    <tr>
      <td>ListRules <a href="#misc" title="covered by our integration test suite">✨</a></td>
       <td style="text-align:right">✅</td>
    </tr>
    <tr>
      <td>ListTagsForResource <a href="#misc" title="covered by our integration test suite">✨</a></td>
       <td style="text-align:right">✅</td>
    </tr>
    <tr>
      <td>ListTargetsByRule <a href="#misc" title="covered by our integration test suite">✨</a></td>
       <td style="text-align:right">✅</td>
    </tr>
    <tr>
      <td>PutEvents <a href="#misc" title="covered by our integration test suite">✨</a></td>
       <td style="text-align:right">✅</td>
    </tr>
    <tr>
      <td>PutPermission <a href="#misc" title="covered by our integration test suite">✨</a></td>
       <td style="text-align:right">✅</td>
    </tr>
    <tr>
      <td>PutRule <a href="#misc" title="covered by our integration test suite">✨</a></td>
       <td style="text-align:right">✅</td>
    </tr>
    <tr>
      <td>PutTargets <a href="#misc" title="covered by our integration test suite">✨</a></td>
       <td style="text-align:right">✅</td>
    </tr>
    <tr>
      <td>RemovePermission <a href="#misc" title="covered by our integration test suite">✨</a></td>
       <td style="text-align:right">✅</td>
    </tr>
    <tr>
      <td>RemoveTargets <a href="#misc" title="covered by our integration test suite">✨</a></td>
       <td style="text-align:right">✅</td>
    </tr>
    <tr>
      <td>StartReplay</td>
       <td style="text-align:right">✅</td>
    </tr>
    <tr>
      <td>TagResource <a href="#misc" title="covered by our integration test suite">✨</a></td>
       <td style="text-align:right">✅</td>
    </tr>
    <tr>
      <td>TestEventPattern</td>
       <td style="text-align:right">✅</td>
    </tr>
    <tr>
      <td>UntagResource <a href="#misc" title="covered by our integration test suite">✨</a></td>
       <td style="text-align:right">✅</td>
    </tr>
    <tr>
      <td>UpdateApiDestination</td>
       <td style="text-align:right">✅</td>
    </tr>
    <tr>
      <td>UpdateArchive</td>
       <td style="text-align:right">✅</td>
    </tr>
    <tr>
      <td>UpdateConnection</td>
       <td style="text-align:right">✅</td>
    </tr>
  </tbody>
  <tbody>    <tr>
      <td><a data-toggle="collapse" href=".events-notimplemented">Show missing</a></td>
      <td style="text-align:right"></td>
    </tr>
  </tbody>
  <tbody class="collapse events-notimplemented">     <tr>
      <td>ActivateEventSource</td>
       <td style="text-align:right">-</td>
    </tr>
    <tr>
      <td>CreateEndpoint</td>
       <td style="text-align:right">-</td>
    </tr>
    <tr>
      <td>CreatePartnerEventSource</td>
       <td style="text-align:right">-</td>
    </tr>
    <tr>
      <td>DeactivateEventSource</td>
       <td style="text-align:right">-</td>
    </tr>
    <tr>
      <td>DeauthorizeConnection</td>
       <td style="text-align:right">-</td>
    </tr>
    <tr>
      <td>DeleteEndpoint</td>
       <td style="text-align:right">-</td>
    </tr>
    <tr>
      <td>DeletePartnerEventSource</td>
       <td style="text-align:right">-</td>
    </tr>
    <tr>
      <td>DescribeEndpoint</td>
       <td style="text-align:right">-</td>
    </tr>
    <tr>
      <td>DescribeEventSource</td>
       <td style="text-align:right">-</td>
    </tr>
    <tr>
      <td>DescribePartnerEventSource</td>
       <td style="text-align:right">-</td>
    </tr>
    <tr>
      <td>ListEndpoints</td>
       <td style="text-align:right">-</td>
    </tr>
    <tr>
      <td>ListEventSources</td>
       <td style="text-align:right">-</td>
    </tr>
    <tr>
      <td>ListPartnerEventSourceAccounts</td>
       <td style="text-align:right">-</td>
    </tr>
    <tr>
      <td>ListPartnerEventSources</td>
       <td style="text-align:right">-</td>
    </tr>
    <tr>
      <td>PutPartnerEvents</td>
       <td style="text-align:right">-</td>
    </tr>
    <tr>
      <td>UpdateEndpoint</td>
       <td style="text-align:right">-</td>
    </tr>
  </tbody>
 </table>


## firehose ##

<table>
  <thead>
    <tr>
      <th>Operation</th>
      <th style="text-align:right">Implemented</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td>CreateDeliveryStream <a href="#misc" title="covered by our integration test suite">✨</a></td>
       <td style="text-align:right">✅</td>
    </tr>
    <tr>
      <td>DeleteDeliveryStream <a href="#misc" title="covered by our integration test suite">✨</a></td>
       <td style="text-align:right">✅</td>
    </tr>
    <tr>
      <td>DescribeDeliveryStream <a href="#misc" title="covered by our integration test suite">✨</a></td>
       <td style="text-align:right">✅</td>
    </tr>
    <tr>
      <td>ListDeliveryStreams <a href="#misc" title="covered by our integration test suite">✨</a></td>
       <td style="text-align:right">✅</td>
    </tr>
    <tr>
      <td>ListTagsForDeliveryStream <a href="#misc" title="covered by our integration test suite">✨</a></td>
       <td style="text-align:right">✅</td>
    </tr>
    <tr>
      <td>PutRecord <a href="#misc" title="covered by our integration test suite">✨</a></td>
       <td style="text-align:right">✅</td>
    </tr>
    <tr>
      <td>PutRecordBatch</td>
       <td style="text-align:right">✅</td>
    </tr>
    <tr>
      <td>TagDeliveryStream</td>
       <td style="text-align:right">✅</td>
    </tr>
    <tr>
      <td>UntagDeliveryStream</td>
       <td style="text-align:right">✅</td>
    </tr>
    <tr>
      <td>UpdateDestination <a href="#misc" title="covered by our integration test suite">✨</a></td>
       <td style="text-align:right">✅</td>
    </tr>
  </tbody>
  <tbody>    <tr>
      <td><a data-toggle="collapse" href=".firehose-notimplemented">Show missing</a></td>
      <td style="text-align:right"></td>
    </tr>
  </tbody>
  <tbody class="collapse firehose-notimplemented">     <tr>
      <td>StartDeliveryStreamEncryption</td>
       <td style="text-align:right">-</td>
    </tr>
    <tr>
      <td>StopDeliveryStreamEncryption</td>
       <td style="text-align:right">-</td>
    </tr>
  </tbody>
 </table>


## fis ##

<table>
  <thead>
    <tr>
      <th>Operation</th>
      <th style="text-align:right">Implemented</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td>CreateExperimentTemplate (Pro)  <a href="#misc" title="covered by our integration test suite">✨</a></td>
       <td style="text-align:right">✅</td>
    </tr>
    <tr>
      <td>DeleteExperimentTemplate (Pro)  <a href="#misc" title="covered by our integration test suite">✨</a></td>
       <td style="text-align:right">✅</td>
    </tr>
    <tr>
      <td>GetExperiment (Pro)  <a href="#misc" title="covered by our integration test suite">✨</a></td>
       <td style="text-align:right">✅</td>
    </tr>
    <tr>
      <td>GetExperimentTemplate (Pro)  <a href="#misc" title="covered by our integration test suite">✨</a></td>
       <td style="text-align:right">✅</td>
    </tr>
    <tr>
      <td>ListExperimentTemplates (Pro)  <a href="#misc" title="covered by our integration test suite">✨</a></td>
       <td style="text-align:right">✅</td>
    </tr>
    <tr>
      <td>ListExperiments (Pro)  <a href="#misc" title="covered by our integration test suite">✨</a></td>
       <td style="text-align:right">✅</td>
    </tr>
    <tr>
      <td>StartExperiment (Pro)  <a href="#misc" title="covered by our integration test suite">✨</a></td>
       <td style="text-align:right">✅</td>
    </tr>
    <tr>
      <td>StopExperiment (Pro)  <a href="#misc" title="covered by our integration test suite">✨</a></td>
       <td style="text-align:right">✅</td>
    </tr>
  </tbody>
  <tbody>    <tr>
      <td><a data-toggle="collapse" href=".fis-notimplemented">Show missing</a></td>
      <td style="text-align:right"></td>
    </tr>
  </tbody>
  <tbody class="collapse fis-notimplemented">     <tr>
      <td>GetAction</td>
       <td style="text-align:right">-</td>
    </tr>
    <tr>
      <td>GetTargetResourceType</td>
       <td style="text-align:right">-</td>
    </tr>
    <tr>
      <td>ListActions</td>
       <td style="text-align:right">-</td>
    </tr>
    <tr>
      <td>ListTagsForResource</td>
       <td style="text-align:right">-</td>
    </tr>
    <tr>
      <td>ListTargetResourceTypes</td>
       <td style="text-align:right">-</td>
    </tr>
    <tr>
      <td>TagResource</td>
       <td style="text-align:right">-</td>
    </tr>
    <tr>
      <td>UntagResource</td>
       <td style="text-align:right">-</td>
    </tr>
    <tr>
      <td>UpdateExperimentTemplate</td>
       <td style="text-align:right">-</td>
    </tr>
  </tbody>
 </table>


## glacier ##

<table>
  <thead>
    <tr>
      <th>Operation</th>
      <th style="text-align:right">Implemented</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td>AddTagsToVault (Pro)  <a href="#misc" title="covered by our integration test suite">✨</a></td>
       <td style="text-align:right">✅</td>
    </tr>
    <tr>
      <td>CreateVault (Pro)  <a href="#misc" title="covered by our integration test suite">✨</a></td>
       <td style="text-align:right">✅</td>
    </tr>
    <tr>
      <td>DeleteArchive (Pro) </td>
       <td style="text-align:right">✅</td>
    </tr>
    <tr>
      <td>DeleteVault (Pro) </td>
       <td style="text-align:right">✅</td>
    </tr>
    <tr>
      <td>DeleteVaultAccessPolicy (Pro) </td>
       <td style="text-align:right">✅</td>
    </tr>
    <tr>
      <td>DeleteVaultNotifications (Pro) </td>
       <td style="text-align:right">✅</td>
    </tr>
    <tr>
      <td>DescribeJob (Pro) </td>
       <td style="text-align:right">✅</td>
    </tr>
    <tr>
      <td>DescribeVault (Pro) </td>
       <td style="text-align:right">✅</td>
    </tr>
    <tr>
      <td>GetJobOutput (Pro)  <a href="#misc" title="covered by our integration test suite">✨</a></td>
       <td style="text-align:right">✅</td>
    </tr>
    <tr>
      <td>GetVaultAccessPolicy (Pro) </td>
       <td style="text-align:right">✅</td>
    </tr>
    <tr>
      <td>GetVaultNotifications (Pro)  <a href="#misc" title="covered by our integration test suite">✨</a></td>
       <td style="text-align:right">✅</td>
    </tr>
    <tr>
      <td>InitiateJob (Pro)  <a href="#misc" title="covered by our integration test suite">✨</a></td>
       <td style="text-align:right">✅</td>
    </tr>
    <tr>
      <td>ListJobs (Pro) </td>
       <td style="text-align:right">✅</td>
    </tr>
    <tr>
      <td>ListTagsForVault (Pro) </td>
       <td style="text-align:right">✅</td>
    </tr>
    <tr>
      <td>ListVaults (Pro) </td>
       <td style="text-align:right">✅</td>
    </tr>
    <tr>
      <td>RemoveTagsFromVault (Pro) </td>
       <td style="text-align:right">✅</td>
    </tr>
    <tr>
      <td>SetVaultAccessPolicy (Pro) </td>
       <td style="text-align:right">✅</td>
    </tr>
    <tr>
      <td>SetVaultNotifications (Pro) </td>
       <td style="text-align:right">✅</td>
    </tr>
    <tr>
      <td>UploadArchive (Pro)  <a href="#misc" title="covered by our integration test suite">✨</a></td>
       <td style="text-align:right">✅</td>
    </tr>
  </tbody>
  <tbody>    <tr>
      <td><a data-toggle="collapse" href=".glacier-notimplemented">Show missing</a></td>
      <td style="text-align:right"></td>
    </tr>
  </tbody>
  <tbody class="collapse glacier-notimplemented">     <tr>
      <td>AbortMultipartUpload</td>
       <td style="text-align:right">-</td>
    </tr>
    <tr>
      <td>AbortVaultLock</td>
       <td style="text-align:right">-</td>
    </tr>
    <tr>
      <td>CompleteMultipartUpload</td>
       <td style="text-align:right">-</td>
    </tr>
    <tr>
      <td>CompleteVaultLock</td>
       <td style="text-align:right">-</td>
    </tr>
    <tr>
      <td>GetDataRetrievalPolicy</td>
       <td style="text-align:right">-</td>
    </tr>
    <tr>
      <td>GetVaultLock</td>
       <td style="text-align:right">-</td>
    </tr>
    <tr>
      <td>InitiateMultipartUpload</td>
       <td style="text-align:right">-</td>
    </tr>
    <tr>
      <td>InitiateVaultLock</td>
       <td style="text-align:right">-</td>
    </tr>
    <tr>
      <td>ListMultipartUploads</td>
       <td style="text-align:right">-</td>
    </tr>
    <tr>
      <td>ListParts</td>
       <td style="text-align:right">-</td>
    </tr>
    <tr>
      <td>ListProvisionedCapacity</td>
       <td style="text-align:right">-</td>
    </tr>
    <tr>
      <td>PurchaseProvisionedCapacity</td>
       <td style="text-align:right">-</td>
    </tr>
    <tr>
      <td>SetDataRetrievalPolicy</td>
       <td style="text-align:right">-</td>
    </tr>
    <tr>
      <td>UploadMultipartPart</td>
       <td style="text-align:right">-</td>
    </tr>
  </tbody>
 </table>


## glue ##

<table>
  <thead>
    <tr>
      <th>Operation</th>
      <th style="text-align:right">Implemented</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td>BatchCreatePartition (Pro) </td>
       <td style="text-align:right">✅</td>
    </tr>
    <tr>
      <td>BatchDeletePartition (Pro) </td>
       <td style="text-align:right">✅</td>
    </tr>
    <tr>
      <td>BatchDeleteTable (Pro) </td>
       <td style="text-align:right">✅</td>
    </tr>
    <tr>
      <td>BatchGetPartition (Pro) </td>
       <td style="text-align:right">✅</td>
    </tr>
    <tr>
      <td>BatchUpdatePartition (Pro) </td>
       <td style="text-align:right">✅</td>
    </tr>
    <tr>
      <td>CheckSchemaVersionValidity (Pro) </td>
       <td style="text-align:right">✅</td>
    </tr>
    <tr>
      <td>CreateClassifier (Pro)  <a href="#misc" title="covered by our integration test suite">✨</a></td>
       <td style="text-align:right">✅</td>
    </tr>
    <tr>
      <td>CreateConnection (Pro)  <a href="#misc" title="covered by our integration test suite">✨</a></td>
       <td style="text-align:right">✅</td>
    </tr>
    <tr>
      <td>CreateCrawler (Pro)  <a href="#misc" title="covered by our integration test suite">✨</a></td>
       <td style="text-align:right">✅</td>
    </tr>
    <tr>
      <td>CreateDatabase (Pro)  <a href="#misc" title="covered by our integration test suite">✨</a></td>
       <td style="text-align:right">✅</td>
    </tr>
    <tr>
      <td>CreateJob (Pro)  <a href="#misc" title="covered by our integration test suite">✨</a></td>
       <td style="text-align:right">✅</td>
    </tr>
    <tr>
      <td>CreatePartition (Pro) </td>
       <td style="text-align:right">✅</td>
    </tr>
    <tr>
      <td>CreatePartitionIndex (Pro) </td>
       <td style="text-align:right">✅</td>
    </tr>
    <tr>
      <td>CreateRegistry (Pro)  <a href="#misc" title="covered by our integration test suite">✨</a></td>
       <td style="text-align:right">✅</td>
    </tr>
    <tr>
      <td>CreateSchema (Pro)  <a href="#misc" title="covered by our integration test suite">✨</a></td>
       <td style="text-align:right">✅</td>
    </tr>
    <tr>
      <td>CreateSecurityConfiguration (Pro)  <a href="#misc" title="covered by our integration test suite">✨</a></td>
       <td style="text-align:right">✅</td>
    </tr>
    <tr>
      <td>CreateTable (Pro)  <a href="#misc" title="covered by our integration test suite">✨</a></td>
       <td style="text-align:right">✅</td>
    </tr>
    <tr>
      <td>CreateTrigger (Pro)  <a href="#misc" title="covered by our integration test suite">✨</a></td>
       <td style="text-align:right">✅</td>
    </tr>
    <tr>
      <td>CreateWorkflow (Pro)  <a href="#misc" title="covered by our integration test suite">✨</a></td>
       <td style="text-align:right">✅</td>
    </tr>
    <tr>
      <td>DeleteClassifier (Pro)  <a href="#misc" title="covered by our integration test suite">✨</a></td>
       <td style="text-align:right">✅</td>
    </tr>
    <tr>
      <td>DeleteConnection (Pro)  <a href="#misc" title="covered by our integration test suite">✨</a></td>
       <td style="text-align:right">✅</td>
    </tr>
    <tr>
      <td>DeleteCrawler (Pro)  <a href="#misc" title="covered by our integration test suite">✨</a></td>
       <td style="text-align:right">✅</td>
    </tr>
    <tr>
      <td>DeleteDatabase (Pro) </td>
       <td style="text-align:right">✅</td>
    </tr>
    <tr>
      <td>DeleteJob (Pro)  <a href="#misc" title="covered by our integration test suite">✨</a></td>
       <td style="text-align:right">✅</td>
    </tr>
    <tr>
      <td>DeletePartition (Pro) </td>
       <td style="text-align:right">✅</td>
    </tr>
    <tr>
      <td>DeletePartitionIndex (Pro) </td>
       <td style="text-align:right">✅</td>
    </tr>
    <tr>
      <td>DeleteRegistry (Pro)  <a href="#misc" title="covered by our integration test suite">✨</a></td>
       <td style="text-align:right">✅</td>
    </tr>
    <tr>
      <td>DeleteResourcePolicy (Pro)  <a href="#misc" title="covered by our integration test suite">✨</a></td>
       <td style="text-align:right">✅</td>
    </tr>
    <tr>
      <td>DeleteSchema (Pro)  <a href="#misc" title="covered by our integration test suite">✨</a></td>
       <td style="text-align:right">✅</td>
    </tr>
    <tr>
      <td>DeleteSchemaVersions (Pro)  <a href="#misc" title="covered by our integration test suite">✨</a></td>
       <td style="text-align:right">✅</td>
    </tr>
    <tr>
      <td>DeleteSecurityConfiguration (Pro)  <a href="#misc" title="covered by our integration test suite">✨</a></td>
       <td style="text-align:right">✅</td>
    </tr>
    <tr>
      <td>DeleteTable (Pro) </td>
       <td style="text-align:right">✅</td>
    </tr>
    <tr>
      <td>DeleteTrigger (Pro)  <a href="#misc" title="covered by our integration test suite">✨</a></td>
       <td style="text-align:right">✅</td>
    </tr>
    <tr>
      <td>DeleteWorkflow (Pro)  <a href="#misc" title="covered by our integration test suite">✨</a></td>
       <td style="text-align:right">✅</td>
    </tr>
    <tr>
      <td>GetCatalogImportStatus (Pro) </td>
       <td style="text-align:right">✅</td>
    </tr>
    <tr>
      <td>GetClassifier (Pro)  <a href="#misc" title="covered by our integration test suite">✨</a></td>
       <td style="text-align:right">✅</td>
    </tr>
    <tr>
      <td>GetClassifiers (Pro)  <a href="#misc" title="covered by our integration test suite">✨</a></td>
       <td style="text-align:right">✅</td>
    </tr>
    <tr>
      <td>GetConnection (Pro)  <a href="#misc" title="covered by our integration test suite">✨</a></td>
       <td style="text-align:right">✅</td>
    </tr>
    <tr>
      <td>GetConnections (Pro)  <a href="#misc" title="covered by our integration test suite">✨</a></td>
       <td style="text-align:right">✅</td>
    </tr>
    <tr>
      <td>GetCrawler (Pro)  <a href="#misc" title="covered by our integration test suite">✨</a></td>
       <td style="text-align:right">✅</td>
    </tr>
    <tr>
      <td>GetCrawlers (Pro)  <a href="#misc" title="covered by our integration test suite">✨</a></td>
       <td style="text-align:right">✅</td>
    </tr>
    <tr>
      <td>GetDatabase (Pro)  <a href="#misc" title="covered by our integration test suite">✨</a></td>
       <td style="text-align:right">✅</td>
    </tr>
    <tr>
      <td>GetDatabases (Pro) </td>
       <td style="text-align:right">✅</td>
    </tr>
    <tr>
      <td>GetJob (Pro)  <a href="#misc" title="covered by our integration test suite">✨</a></td>
       <td style="text-align:right">✅</td>
    </tr>
    <tr>
      <td>GetJobRun (Pro)  <a href="#misc" title="covered by our integration test suite">✨</a></td>
       <td style="text-align:right">✅</td>
    </tr>
    <tr>
      <td>GetJobRuns (Pro)  <a href="#misc" title="covered by our integration test suite">✨</a></td>
       <td style="text-align:right">✅</td>
    </tr>
    <tr>
      <td>GetJobs (Pro)  <a href="#misc" title="covered by our integration test suite">✨</a></td>
       <td style="text-align:right">✅</td>
    </tr>
    <tr>
      <td>GetPartition (Pro) </td>
       <td style="text-align:right">✅</td>
    </tr>
    <tr>
      <td>GetPartitionIndexes (Pro) </td>
       <td style="text-align:right">✅</td>
    </tr>
    <tr>
      <td>GetPartitions (Pro) </td>
       <td style="text-align:right">✅</td>
    </tr>
    <tr>
      <td>GetRegistry (Pro)  <a href="#misc" title="covered by our integration test suite">✨</a></td>
       <td style="text-align:right">✅</td>
    </tr>
    <tr>
      <td>GetResourcePolicy (Pro)  <a href="#misc" title="covered by our integration test suite">✨</a></td>
       <td style="text-align:right">✅</td>
    </tr>
    <tr>
      <td>GetSchema (Pro)  <a href="#misc" title="covered by our integration test suite">✨</a></td>
       <td style="text-align:right">✅</td>
    </tr>
    <tr>
      <td>GetSchemaByDefinition (Pro) </td>
       <td style="text-align:right">✅</td>
    </tr>
    <tr>
      <td>GetSchemaVersion (Pro)  <a href="#misc" title="covered by our integration test suite">✨</a></td>
       <td style="text-align:right">✅</td>
    </tr>
    <tr>
      <td>GetSchemaVersionsDiff (Pro) </td>
       <td style="text-align:right">✅</td>
    </tr>
    <tr>
      <td>GetSecurityConfiguration (Pro)  <a href="#misc" title="covered by our integration test suite">✨</a></td>
       <td style="text-align:right">✅</td>
    </tr>
    <tr>
      <td>GetSecurityConfigurations (Pro)  <a href="#misc" title="covered by our integration test suite">✨</a></td>
       <td style="text-align:right">✅</td>
    </tr>
    <tr>
      <td>GetTable (Pro)  <a href="#misc" title="covered by our integration test suite">✨</a></td>
       <td style="text-align:right">✅</td>
    </tr>
    <tr>
      <td>GetTableVersion (Pro) </td>
       <td style="text-align:right">✅</td>
    </tr>
    <tr>
      <td>GetTableVersions (Pro) </td>
       <td style="text-align:right">✅</td>
    </tr>
    <tr>
      <td>GetTables (Pro) </td>
       <td style="text-align:right">✅</td>
    </tr>
    <tr>
      <td>GetTags (Pro) </td>
       <td style="text-align:right">✅</td>
    </tr>
    <tr>
      <td>GetTrigger (Pro)  <a href="#misc" title="covered by our integration test suite">✨</a></td>
       <td style="text-align:right">✅</td>
    </tr>
    <tr>
      <td>GetWorkflow (Pro)  <a href="#misc" title="covered by our integration test suite">✨</a></td>
       <td style="text-align:right">✅</td>
    </tr>
    <tr>
      <td>ImportCatalogToGlue (Pro) </td>
       <td style="text-align:right">✅</td>
    </tr>
    <tr>
      <td>ListCrawlers (Pro)  <a href="#misc" title="covered by our integration test suite">✨</a></td>
       <td style="text-align:right">✅</td>
    </tr>
    <tr>
      <td>ListJobs (Pro)  <a href="#misc" title="covered by our integration test suite">✨</a></td>
       <td style="text-align:right">✅</td>
    </tr>
    <tr>
      <td>ListRegistries (Pro)  <a href="#misc" title="covered by our integration test suite">✨</a></td>
       <td style="text-align:right">✅</td>
    </tr>
    <tr>
      <td>ListSchemaVersions (Pro)  <a href="#misc" title="covered by our integration test suite">✨</a></td>
       <td style="text-align:right">✅</td>
    </tr>
    <tr>
      <td>ListSchemas (Pro)  <a href="#misc" title="covered by our integration test suite">✨</a></td>
       <td style="text-align:right">✅</td>
    </tr>
    <tr>
      <td>ListWorkflows (Pro)  <a href="#misc" title="covered by our integration test suite">✨</a></td>
       <td style="text-align:right">✅</td>
    </tr>
    <tr>
      <td>PutResourcePolicy (Pro)  <a href="#misc" title="covered by our integration test suite">✨</a></td>
       <td style="text-align:right">✅</td>
    </tr>
    <tr>
      <td>PutSchemaVersionMetadata (Pro)  <a href="#misc" title="covered by our integration test suite">✨</a></td>
       <td style="text-align:right">✅</td>
    </tr>
    <tr>
      <td>QuerySchemaVersionMetadata (Pro)  <a href="#misc" title="covered by our integration test suite">✨</a></td>
       <td style="text-align:right">✅</td>
    </tr>
    <tr>
      <td>RegisterSchemaVersion (Pro)  <a href="#misc" title="covered by our integration test suite">✨</a></td>
       <td style="text-align:right">✅</td>
    </tr>
    <tr>
      <td>RemoveSchemaVersionMetadata (Pro)  <a href="#misc" title="covered by our integration test suite">✨</a></td>
       <td style="text-align:right">✅</td>
    </tr>
    <tr>
      <td>StartCrawler (Pro) </td>
       <td style="text-align:right">✅</td>
    </tr>
    <tr>
      <td>StartJobRun (Pro)  <a href="#misc" title="covered by our integration test suite">✨</a></td>
       <td style="text-align:right">✅</td>
    </tr>
    <tr>
      <td>StartTrigger (Pro) </td>
       <td style="text-align:right">✅</td>
    </tr>
    <tr>
      <td>StopCrawler (Pro) </td>
       <td style="text-align:right">✅</td>
    </tr>
    <tr>
      <td>StopTrigger (Pro) </td>
       <td style="text-align:right">✅</td>
    </tr>
    <tr>
      <td>TagResource (Pro) </td>
       <td style="text-align:right">✅</td>
    </tr>
    <tr>
      <td>UntagResource (Pro) </td>
       <td style="text-align:right">✅</td>
    </tr>
    <tr>
      <td>UpdateClassifier (Pro) </td>
       <td style="text-align:right">✅</td>
    </tr>
    <tr>
      <td>UpdateConnection (Pro) </td>
       <td style="text-align:right">✅</td>
    </tr>
    <tr>
      <td>UpdateCrawler (Pro)  <a href="#misc" title="covered by our integration test suite">✨</a></td>
       <td style="text-align:right">✅</td>
    </tr>
    <tr>
      <td>UpdateDatabase (Pro) </td>
       <td style="text-align:right">✅</td>
    </tr>
    <tr>
      <td>UpdateJob (Pro)  <a href="#misc" title="covered by our integration test suite">✨</a></td>
       <td style="text-align:right">✅</td>
    </tr>
    <tr>
      <td>UpdatePartition (Pro) </td>
       <td style="text-align:right">✅</td>
    </tr>
    <tr>
      <td>UpdateRegistry (Pro)  <a href="#misc" title="covered by our integration test suite">✨</a></td>
       <td style="text-align:right">✅</td>
    </tr>
    <tr>
      <td>UpdateSchema (Pro)  <a href="#misc" title="covered by our integration test suite">✨</a></td>
       <td style="text-align:right">✅</td>
    </tr>
    <tr>
      <td>UpdateTable (Pro) </td>
       <td style="text-align:right">✅</td>
    </tr>
    <tr>
      <td>UpdateTrigger (Pro)  <a href="#misc" title="covered by our integration test suite">✨</a></td>
       <td style="text-align:right">✅</td>
    </tr>
    <tr>
      <td>UpdateWorkflow (Pro) </td>
       <td style="text-align:right">✅</td>
    </tr>
  </tbody>
  <tbody>    <tr>
      <td><a data-toggle="collapse" href=".glue-notimplemented">Show missing</a></td>
      <td style="text-align:right"></td>
    </tr>
  </tbody>
  <tbody class="collapse glue-notimplemented">     <tr>
      <td>BatchDeleteConnection</td>
       <td style="text-align:right">-</td>
    </tr>
    <tr>
      <td>BatchDeleteTableVersion</td>
       <td style="text-align:right">-</td>
    </tr>
    <tr>
      <td>BatchGetBlueprints</td>
       <td style="text-align:right">-</td>
    </tr>
    <tr>
      <td>BatchGetCrawlers</td>
       <td style="text-align:right">-</td>
    </tr>
    <tr>
      <td>BatchGetCustomEntityTypes</td>
       <td style="text-align:right">-</td>
    </tr>
    <tr>
      <td>BatchGetDevEndpoints</td>
       <td style="text-align:right">-</td>
    </tr>
    <tr>
      <td>BatchGetJobs</td>
       <td style="text-align:right">-</td>
    </tr>
    <tr>
      <td>BatchGetTriggers</td>
       <td style="text-align:right">-</td>
    </tr>
    <tr>
      <td>BatchGetWorkflows</td>
       <td style="text-align:right">-</td>
    </tr>
    <tr>
      <td>BatchStopJobRun</td>
       <td style="text-align:right">-</td>
    </tr>
    <tr>
      <td>CancelMLTaskRun</td>
       <td style="text-align:right">-</td>
    </tr>
    <tr>
      <td>CancelStatement</td>
       <td style="text-align:right">-</td>
    </tr>
    <tr>
      <td>CreateBlueprint</td>
       <td style="text-align:right">-</td>
    </tr>
    <tr>
      <td>CreateCustomEntityType</td>
       <td style="text-align:right">-</td>
    </tr>
    <tr>
      <td>CreateDevEndpoint</td>
       <td style="text-align:right">-</td>
    </tr>
    <tr>
      <td>CreateMLTransform</td>
       <td style="text-align:right">-</td>
    </tr>
    <tr>
      <td>CreateScript</td>
       <td style="text-align:right">-</td>
    </tr>
    <tr>
      <td>CreateSession</td>
       <td style="text-align:right">-</td>
    </tr>
    <tr>
      <td>CreateUserDefinedFunction</td>
       <td style="text-align:right">-</td>
    </tr>
    <tr>
      <td>DeleteBlueprint</td>
       <td style="text-align:right">-</td>
    </tr>
    <tr>
      <td>DeleteColumnStatisticsForPartition</td>
       <td style="text-align:right">-</td>
    </tr>
    <tr>
      <td>DeleteColumnStatisticsForTable</td>
       <td style="text-align:right">-</td>
    </tr>
    <tr>
      <td>DeleteCustomEntityType</td>
       <td style="text-align:right">-</td>
    </tr>
    <tr>
      <td>DeleteDevEndpoint</td>
       <td style="text-align:right">-</td>
    </tr>
    <tr>
      <td>DeleteMLTransform</td>
       <td style="text-align:right">-</td>
    </tr>
    <tr>
      <td>DeleteSession</td>
       <td style="text-align:right">-</td>
    </tr>
    <tr>
      <td>DeleteTableVersion</td>
       <td style="text-align:right">-</td>
    </tr>
    <tr>
      <td>DeleteUserDefinedFunction</td>
       <td style="text-align:right">-</td>
    </tr>
    <tr>
      <td>GetBlueprint</td>
       <td style="text-align:right">-</td>
    </tr>
    <tr>
      <td>GetBlueprintRun</td>
       <td style="text-align:right">-</td>
    </tr>
    <tr>
      <td>GetBlueprintRuns</td>
       <td style="text-align:right">-</td>
    </tr>
    <tr>
      <td>GetColumnStatisticsForPartition</td>
       <td style="text-align:right">-</td>
    </tr>
    <tr>
      <td>GetColumnStatisticsForTable</td>
       <td style="text-align:right">-</td>
    </tr>
    <tr>
      <td>GetCrawlerMetrics</td>
       <td style="text-align:right">-</td>
    </tr>
    <tr>
      <td>GetCustomEntityType</td>
       <td style="text-align:right">-</td>
    </tr>
    <tr>
      <td>GetDataCatalogEncryptionSettings</td>
       <td style="text-align:right">-</td>
    </tr>
    <tr>
      <td>GetDataflowGraph</td>
       <td style="text-align:right">-</td>
    </tr>
    <tr>
      <td>GetDevEndpoint</td>
       <td style="text-align:right">-</td>
    </tr>
    <tr>
      <td>GetDevEndpoints</td>
       <td style="text-align:right">-</td>
    </tr>
    <tr>
      <td>GetJobBookmark</td>
       <td style="text-align:right">-</td>
    </tr>
    <tr>
      <td>GetMLTaskRun</td>
       <td style="text-align:right">-</td>
    </tr>
    <tr>
      <td>GetMLTaskRuns</td>
       <td style="text-align:right">-</td>
    </tr>
    <tr>
      <td>GetMLTransform</td>
       <td style="text-align:right">-</td>
    </tr>
    <tr>
      <td>GetMLTransforms</td>
       <td style="text-align:right">-</td>
    </tr>
    <tr>
      <td>GetMapping</td>
       <td style="text-align:right">-</td>
    </tr>
    <tr>
      <td>GetPlan</td>
       <td style="text-align:right">-</td>
    </tr>
    <tr>
      <td>GetResourcePolicies</td>
       <td style="text-align:right">-</td>
    </tr>
    <tr>
      <td>GetSession</td>
       <td style="text-align:right">-</td>
    </tr>
    <tr>
      <td>GetStatement</td>
       <td style="text-align:right">-</td>
    </tr>
    <tr>
      <td>GetTriggers</td>
       <td style="text-align:right">-</td>
    </tr>
    <tr>
      <td>GetUnfilteredPartitionMetadata</td>
       <td style="text-align:right">-</td>
    </tr>
    <tr>
      <td>GetUnfilteredPartitionsMetadata</td>
       <td style="text-align:right">-</td>
    </tr>
    <tr>
      <td>GetUnfilteredTableMetadata</td>
       <td style="text-align:right">-</td>
    </tr>
    <tr>
      <td>GetUserDefinedFunction</td>
       <td style="text-align:right">-</td>
    </tr>
    <tr>
      <td>GetUserDefinedFunctions</td>
       <td style="text-align:right">-</td>
    </tr>
    <tr>
      <td>GetWorkflowRun</td>
       <td style="text-align:right">-</td>
    </tr>
    <tr>
      <td>GetWorkflowRunProperties</td>
       <td style="text-align:right">-</td>
    </tr>
    <tr>
      <td>GetWorkflowRuns</td>
       <td style="text-align:right">-</td>
    </tr>
    <tr>
      <td>ListBlueprints</td>
       <td style="text-align:right">-</td>
    </tr>
    <tr>
      <td>ListCrawls</td>
       <td style="text-align:right">-</td>
    </tr>
    <tr>
      <td>ListCustomEntityTypes</td>
       <td style="text-align:right">-</td>
    </tr>
    <tr>
      <td>ListDevEndpoints</td>
       <td style="text-align:right">-</td>
    </tr>
    <tr>
      <td>ListMLTransforms</td>
       <td style="text-align:right">-</td>
    </tr>
    <tr>
      <td>ListSessions</td>
       <td style="text-align:right">-</td>
    </tr>
    <tr>
      <td>ListStatements</td>
       <td style="text-align:right">-</td>
    </tr>
    <tr>
      <td>ListTriggers</td>
       <td style="text-align:right">-</td>
    </tr>
    <tr>
      <td>PutDataCatalogEncryptionSettings</td>
       <td style="text-align:right">-</td>
    </tr>
    <tr>
      <td>PutWorkflowRunProperties</td>
       <td style="text-align:right">-</td>
    </tr>
    <tr>
      <td>ResetJobBookmark</td>
       <td style="text-align:right">-</td>
    </tr>
    <tr>
      <td>ResumeWorkflowRun</td>
       <td style="text-align:right">-</td>
    </tr>
    <tr>
      <td>RunStatement</td>
       <td style="text-align:right">-</td>
    </tr>
    <tr>
      <td>SearchTables</td>
       <td style="text-align:right">-</td>
    </tr>
    <tr>
      <td>StartBlueprintRun</td>
       <td style="text-align:right">-</td>
    </tr>
    <tr>
      <td>StartCrawlerSchedule</td>
       <td style="text-align:right">-</td>
    </tr>
    <tr>
      <td>StartExportLabelsTaskRun</td>
       <td style="text-align:right">-</td>
    </tr>
    <tr>
      <td>StartImportLabelsTaskRun</td>
       <td style="text-align:right">-</td>
    </tr>
    <tr>
      <td>StartMLEvaluationTaskRun</td>
       <td style="text-align:right">-</td>
    </tr>
    <tr>
      <td>StartMLLabelingSetGenerationTaskRun</td>
       <td style="text-align:right">-</td>
    </tr>
    <tr>
      <td>StartWorkflowRun</td>
       <td style="text-align:right">-</td>
    </tr>
    <tr>
      <td>StopCrawlerSchedule</td>
       <td style="text-align:right">-</td>
    </tr>
    <tr>
      <td>StopSession</td>
       <td style="text-align:right">-</td>
    </tr>
    <tr>
      <td>StopWorkflowRun</td>
       <td style="text-align:right">-</td>
    </tr>
    <tr>
      <td>UpdateBlueprint</td>
       <td style="text-align:right">-</td>
    </tr>
    <tr>
      <td>UpdateColumnStatisticsForPartition</td>
       <td style="text-align:right">-</td>
    </tr>
    <tr>
      <td>UpdateColumnStatisticsForTable</td>
       <td style="text-align:right">-</td>
    </tr>
    <tr>
      <td>UpdateCrawlerSchedule</td>
       <td style="text-align:right">-</td>
    </tr>
    <tr>
      <td>UpdateDevEndpoint</td>
       <td style="text-align:right">-</td>
    </tr>
    <tr>
      <td>UpdateJobFromSourceControl</td>
       <td style="text-align:right">-</td>
    </tr>
    <tr>
      <td>UpdateMLTransform</td>
       <td style="text-align:right">-</td>
    </tr>
    <tr>
      <td>UpdateSourceControlFromJob</td>
       <td style="text-align:right">-</td>
    </tr>
    <tr>
      <td>UpdateUserDefinedFunction</td>
       <td style="text-align:right">-</td>
    </tr>
  </tbody>
 </table>


## iam ##

<table>
  <thead>
    <tr>
      <th>Operation</th>
      <th style="text-align:right">Implemented</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td>AddRoleToInstanceProfile <a href="#misc" title="covered by our integration test suite">✨</a></td>
       <td style="text-align:right">✅</td>
    </tr>
    <tr>
      <td>AddUserToGroup <a href="#misc" title="covered by our integration test suite">✨</a></td>
       <td style="text-align:right">✅</td>
    </tr>
    <tr>
      <td>AttachGroupPolicy <a href="#misc" title="covered by our integration test suite">✨</a></td>
       <td style="text-align:right">✅</td>
    </tr>
    <tr>
      <td>AttachRolePolicy <a href="#misc" title="covered by our integration test suite">✨</a></td>
       <td style="text-align:right">✅</td>
    </tr>
    <tr>
      <td>AttachUserPolicy <a href="#misc" title="covered by our integration test suite">✨</a></td>
       <td style="text-align:right">✅</td>
    </tr>
    <tr>
      <td>CreateAccessKey <a href="#misc" title="covered by our integration test suite">✨</a></td>
       <td style="text-align:right">✅</td>
    </tr>
    <tr>
      <td>CreateAccountAlias</td>
       <td style="text-align:right">✅</td>
    </tr>
    <tr>
      <td>CreateGroup <a href="#misc" title="covered by our integration test suite">✨</a></td>
       <td style="text-align:right">✅</td>
    </tr>
    <tr>
      <td>CreateInstanceProfile <a href="#misc" title="covered by our integration test suite">✨</a></td>
       <td style="text-align:right">✅</td>
    </tr>
    <tr>
      <td>CreateLoginProfile</td>
       <td style="text-align:right">✅</td>
    </tr>
    <tr>
      <td>CreateOpenIDConnectProvider</td>
       <td style="text-align:right">✅</td>
    </tr>
    <tr>
      <td>CreatePolicy <a href="#misc" title="covered by our integration test suite">✨</a></td>
       <td style="text-align:right">✅</td>
    </tr>
    <tr>
      <td>CreatePolicyVersion</td>
       <td style="text-align:right">✅</td>
    </tr>
    <tr>
      <td>CreateRole <a href="#misc" title="covered by our integration test suite">✨</a></td>
       <td style="text-align:right">✅</td>
    </tr>
    <tr>
      <td>CreateSAMLProvider</td>
       <td style="text-align:right">✅</td>
    </tr>
    <tr>
      <td>CreateServiceLinkedRole <a href="#misc" title="covered by our integration test suite">✨</a></td>
       <td style="text-align:right">✅</td>
    </tr>
    <tr>
      <td>CreateUser <a href="#misc" title="covered by our integration test suite">✨</a></td>
       <td style="text-align:right">✅</td>
    </tr>
    <tr>
      <td>CreateVirtualMFADevice</td>
       <td style="text-align:right">✅</td>
    </tr>
    <tr>
      <td>DeactivateMFADevice</td>
       <td style="text-align:right">✅</td>
    </tr>
    <tr>
      <td>DeleteAccessKey <a href="#misc" title="covered by our integration test suite">✨</a></td>
       <td style="text-align:right">✅</td>
    </tr>
    <tr>
      <td>DeleteAccountAlias</td>
       <td style="text-align:right">✅</td>
    </tr>
    <tr>
      <td>DeleteAccountPasswordPolicy</td>
       <td style="text-align:right">✅</td>
    </tr>
    <tr>
      <td>DeleteGroup <a href="#misc" title="covered by our integration test suite">✨</a></td>
       <td style="text-align:right">✅</td>
    </tr>
    <tr>
      <td>DeleteGroupPolicy <a href="#misc" title="covered by our integration test suite">✨</a></td>
       <td style="text-align:right">✅</td>
    </tr>
    <tr>
      <td>DeleteInstanceProfile <a href="#misc" title="covered by our integration test suite">✨</a></td>
       <td style="text-align:right">✅</td>
    </tr>
    <tr>
      <td>DeleteLoginProfile</td>
       <td style="text-align:right">✅</td>
    </tr>
    <tr>
      <td>DeleteOpenIDConnectProvider</td>
       <td style="text-align:right">✅</td>
    </tr>
    <tr>
      <td>DeletePolicy <a href="#misc" title="covered by our integration test suite">✨</a></td>
       <td style="text-align:right">✅</td>
    </tr>
    <tr>
      <td>DeletePolicyVersion</td>
       <td style="text-align:right">✅</td>
    </tr>
    <tr>
      <td>DeleteRole <a href="#misc" title="covered by our integration test suite">✨</a></td>
       <td style="text-align:right">✅</td>
    </tr>
    <tr>
      <td>DeleteRolePermissionsBoundary</td>
       <td style="text-align:right">✅</td>
    </tr>
    <tr>
      <td>DeleteRolePolicy <a href="#misc" title="covered by our integration test suite">✨</a></td>
       <td style="text-align:right">✅</td>
    </tr>
    <tr>
      <td>DeleteSAMLProvider</td>
       <td style="text-align:right">✅</td>
    </tr>
    <tr>
      <td>DeleteSSHPublicKey</td>
       <td style="text-align:right">✅</td>
    </tr>
    <tr>
      <td>DeleteServerCertificate</td>
       <td style="text-align:right">✅</td>
    </tr>
    <tr>
      <td>DeleteServiceLinkedRole <a href="#misc" title="covered by our integration test suite">✨</a></td>
       <td style="text-align:right">✅</td>
    </tr>
    <tr>
      <td>DeleteSigningCertificate</td>
       <td style="text-align:right">✅</td>
    </tr>
    <tr>
      <td>DeleteUser <a href="#misc" title="covered by our integration test suite">✨</a></td>
       <td style="text-align:right">✅</td>
    </tr>
    <tr>
      <td>DeleteUserPermissionsBoundary <a href="#misc" title="covered by our integration test suite">✨</a></td>
       <td style="text-align:right">✅</td>
    </tr>
    <tr>
      <td>DeleteUserPolicy <a href="#misc" title="covered by our integration test suite">✨</a></td>
       <td style="text-align:right">✅</td>
    </tr>
    <tr>
      <td>DeleteVirtualMFADevice</td>
       <td style="text-align:right">✅</td>
    </tr>
    <tr>
      <td>DetachGroupPolicy <a href="#misc" title="covered by our integration test suite">✨</a></td>
       <td style="text-align:right">✅</td>
    </tr>
    <tr>
      <td>DetachRolePolicy <a href="#misc" title="covered by our integration test suite">✨</a></td>
       <td style="text-align:right">✅</td>
    </tr>
    <tr>
      <td>DetachUserPolicy <a href="#misc" title="covered by our integration test suite">✨</a></td>
       <td style="text-align:right">✅</td>
    </tr>
    <tr>
      <td>EnableMFADevice</td>
       <td style="text-align:right">✅</td>
    </tr>
    <tr>
      <td>GenerateCredentialReport</td>
       <td style="text-align:right">✅</td>
    </tr>
    <tr>
      <td>GetAccessKeyLastUsed</td>
       <td style="text-align:right">✅</td>
    </tr>
    <tr>
      <td>GetAccountAuthorizationDetails</td>
       <td style="text-align:right">✅</td>
    </tr>
    <tr>
      <td>GetAccountPasswordPolicy</td>
       <td style="text-align:right">✅</td>
    </tr>
    <tr>
      <td>GetAccountSummary</td>
       <td style="text-align:right">✅</td>
    </tr>
    <tr>
      <td>GetCredentialReport</td>
       <td style="text-align:right">✅</td>
    </tr>
    <tr>
      <td>GetGroup <a href="#misc" title="covered by our integration test suite">✨</a></td>
       <td style="text-align:right">✅</td>
    </tr>
    <tr>
      <td>GetGroupPolicy <a href="#misc" title="covered by our integration test suite">✨</a></td>
       <td style="text-align:right">✅</td>
    </tr>
    <tr>
      <td>GetInstanceProfile <a href="#misc" title="covered by our integration test suite">✨</a></td>
       <td style="text-align:right">✅</td>
    </tr>
    <tr>
      <td>GetLoginProfile</td>
       <td style="text-align:right">✅</td>
    </tr>
    <tr>
      <td>GetOpenIDConnectProvider</td>
       <td style="text-align:right">✅</td>
    </tr>
    <tr>
      <td>GetPolicy <a href="#misc" title="covered by our integration test suite">✨</a></td>
       <td style="text-align:right">✅</td>
    </tr>
    <tr>
      <td>GetPolicyVersion <a href="#misc" title="covered by our integration test suite">✨</a></td>
       <td style="text-align:right">✅</td>
    </tr>
    <tr>
      <td>GetRole <a href="#misc" title="covered by our integration test suite">✨</a></td>
       <td style="text-align:right">✅</td>
    </tr>
    <tr>
      <td>GetRolePolicy <a href="#misc" title="covered by our integration test suite">✨</a></td>
       <td style="text-align:right">✅</td>
    </tr>
    <tr>
      <td>GetSAMLProvider</td>
       <td style="text-align:right">✅</td>
    </tr>
    <tr>
      <td>GetSSHPublicKey</td>
       <td style="text-align:right">✅</td>
    </tr>
    <tr>
      <td>GetServerCertificate</td>
       <td style="text-align:right">✅</td>
    </tr>
    <tr>
      <td>GetServiceLinkedRoleDeletionStatus</td>
       <td style="text-align:right">✅</td>
    </tr>
    <tr>
      <td>GetUser <a href="#misc" title="covered by our integration test suite">✨</a></td>
       <td style="text-align:right">✅</td>
    </tr>
    <tr>
      <td>GetUserPolicy <a href="#misc" title="covered by our integration test suite">✨</a></td>
       <td style="text-align:right">✅</td>
    </tr>
    <tr>
      <td>ListAccessKeys <a href="#misc" title="covered by our integration test suite">✨</a></td>
       <td style="text-align:right">✅</td>
    </tr>
    <tr>
      <td>ListAccountAliases</td>
       <td style="text-align:right">✅</td>
    </tr>
    <tr>
      <td>ListAttachedGroupPolicies <a href="#misc" title="covered by our integration test suite">✨</a></td>
       <td style="text-align:right">✅</td>
    </tr>
    <tr>
      <td>ListAttachedRolePolicies <a href="#misc" title="covered by our integration test suite">✨</a></td>
       <td style="text-align:right">✅</td>
    </tr>
    <tr>
      <td>ListAttachedUserPolicies <a href="#misc" title="covered by our integration test suite">✨</a></td>
       <td style="text-align:right">✅</td>
    </tr>
    <tr>
      <td>ListEntitiesForPolicy</td>
       <td style="text-align:right">✅</td>
    </tr>
    <tr>
      <td>ListGroupPolicies <a href="#misc" title="covered by our integration test suite">✨</a></td>
       <td style="text-align:right">✅</td>
    </tr>
    <tr>
      <td>ListGroups <a href="#misc" title="covered by our integration test suite">✨</a></td>
       <td style="text-align:right">✅</td>
    </tr>
    <tr>
      <td>ListGroupsForUser <a href="#misc" title="covered by our integration test suite">✨</a></td>
       <td style="text-align:right">✅</td>
    </tr>
    <tr>
      <td>ListInstanceProfileTags <a href="#misc" title="covered by our integration test suite">✨</a></td>
       <td style="text-align:right">✅</td>
    </tr>
    <tr>
      <td>ListInstanceProfiles <a href="#misc" title="covered by our integration test suite">✨</a></td>
       <td style="text-align:right">✅</td>
    </tr>
    <tr>
      <td>ListInstanceProfilesForRole <a href="#misc" title="covered by our integration test suite">✨</a></td>
       <td style="text-align:right">✅</td>
    </tr>
    <tr>
      <td>ListMFADevices</td>
       <td style="text-align:right">✅</td>
    </tr>
    <tr>
      <td>ListOpenIDConnectProviderTags</td>
       <td style="text-align:right">✅</td>
    </tr>
    <tr>
      <td>ListOpenIDConnectProviders</td>
       <td style="text-align:right">✅</td>
    </tr>
    <tr>
      <td>ListPolicies <a href="#misc" title="covered by our integration test suite">✨</a></td>
       <td style="text-align:right">✅</td>
    </tr>
    <tr>
      <td>ListPolicyTags</td>
       <td style="text-align:right">✅</td>
    </tr>
    <tr>
      <td>ListPolicyVersions <a href="#misc" title="covered by our integration test suite">✨</a></td>
       <td style="text-align:right">✅</td>
    </tr>
    <tr>
      <td>ListRolePolicies <a href="#misc" title="covered by our integration test suite">✨</a></td>
       <td style="text-align:right">✅</td>
    </tr>
    <tr>
      <td>ListRoleTags</td>
       <td style="text-align:right">✅</td>
    </tr>
    <tr>
      <td>ListRoles <a href="#misc" title="covered by our integration test suite">✨</a></td>
       <td style="text-align:right">✅</td>
    </tr>
    <tr>
      <td>ListSAMLProviders</td>
       <td style="text-align:right">✅</td>
    </tr>
    <tr>
      <td>ListSSHPublicKeys</td>
       <td style="text-align:right">✅</td>
    </tr>
    <tr>
      <td>ListServerCertificates</td>
       <td style="text-align:right">✅</td>
    </tr>
    <tr>
      <td>ListSigningCertificates</td>
       <td style="text-align:right">✅</td>
    </tr>
    <tr>
      <td>ListUserPolicies <a href="#misc" title="covered by our integration test suite">✨</a></td>
       <td style="text-align:right">✅</td>
    </tr>
    <tr>
      <td>ListUserTags</td>
       <td style="text-align:right">✅</td>
    </tr>
    <tr>
      <td>ListUsers <a href="#misc" title="covered by our integration test suite">✨</a></td>
       <td style="text-align:right">✅</td>
    </tr>
    <tr>
      <td>ListVirtualMFADevices</td>
       <td style="text-align:right">✅</td>
    </tr>
    <tr>
      <td>PutGroupPolicy <a href="#misc" title="covered by our integration test suite">✨</a></td>
       <td style="text-align:right">✅</td>
    </tr>
    <tr>
      <td>PutRolePermissionsBoundary <a href="#misc" title="covered by our integration test suite">✨</a></td>
       <td style="text-align:right">✅</td>
    </tr>
    <tr>
      <td>PutRolePolicy <a href="#misc" title="covered by our integration test suite">✨</a></td>
       <td style="text-align:right">✅</td>
    </tr>
    <tr>
      <td>PutUserPermissionsBoundary <a href="#misc" title="covered by our integration test suite">✨</a></td>
       <td style="text-align:right">✅</td>
    </tr>
    <tr>
      <td>PutUserPolicy <a href="#misc" title="covered by our integration test suite">✨</a></td>
       <td style="text-align:right">✅</td>
    </tr>
    <tr>
      <td>RemoveRoleFromInstanceProfile <a href="#misc" title="covered by our integration test suite">✨</a></td>
       <td style="text-align:right">✅</td>
    </tr>
    <tr>
      <td>RemoveUserFromGroup <a href="#misc" title="covered by our integration test suite">✨</a></td>
       <td style="text-align:right">✅</td>
    </tr>
    <tr>
      <td>SetDefaultPolicyVersion</td>
       <td style="text-align:right">✅</td>
    </tr>
    <tr>
      <td>SimulatePrincipalPolicy <a href="#misc" title="covered by our integration test suite">✨</a></td>
       <td style="text-align:right">✅</td>
    </tr>
    <tr>
      <td>TagInstanceProfile <a href="#misc" title="covered by our integration test suite">✨</a></td>
       <td style="text-align:right">✅</td>
    </tr>
    <tr>
      <td>TagOpenIDConnectProvider</td>
       <td style="text-align:right">✅</td>
    </tr>
    <tr>
      <td>TagPolicy</td>
       <td style="text-align:right">✅</td>
    </tr>
    <tr>
      <td>TagRole</td>
       <td style="text-align:right">✅</td>
    </tr>
    <tr>
      <td>TagUser</td>
       <td style="text-align:right">✅</td>
    </tr>
    <tr>
      <td>UntagInstanceProfile <a href="#misc" title="covered by our integration test suite">✨</a></td>
       <td style="text-align:right">✅</td>
    </tr>
    <tr>
      <td>UntagOpenIDConnectProvider</td>
       <td style="text-align:right">✅</td>
    </tr>
    <tr>
      <td>UntagPolicy</td>
       <td style="text-align:right">✅</td>
    </tr>
    <tr>
      <td>UntagRole</td>
       <td style="text-align:right">✅</td>
    </tr>
    <tr>
      <td>UntagUser</td>
       <td style="text-align:right">✅</td>
    </tr>
    <tr>
      <td>UpdateAccessKey</td>
       <td style="text-align:right">✅</td>
    </tr>
    <tr>
      <td>UpdateAccountPasswordPolicy</td>
       <td style="text-align:right">✅</td>
    </tr>
    <tr>
      <td>UpdateAssumeRolePolicy <a href="#misc" title="covered by our integration test suite">✨</a></td>
       <td style="text-align:right">✅</td>
    </tr>
    <tr>
      <td>UpdateGroup</td>
       <td style="text-align:right">✅</td>
    </tr>
    <tr>
      <td>UpdateLoginProfile</td>
       <td style="text-align:right">✅</td>
    </tr>
    <tr>
      <td>UpdateOpenIDConnectProviderThumbprint</td>
       <td style="text-align:right">✅</td>
    </tr>
    <tr>
      <td>UpdateRole <a href="#misc" title="covered by our integration test suite">✨</a></td>
       <td style="text-align:right">✅</td>
    </tr>
    <tr>
      <td>UpdateRoleDescription</td>
       <td style="text-align:right">✅</td>
    </tr>
    <tr>
      <td>UpdateSAMLProvider</td>
       <td style="text-align:right">✅</td>
    </tr>
    <tr>
      <td>UpdateSSHPublicKey</td>
       <td style="text-align:right">✅</td>
    </tr>
    <tr>
      <td>UpdateSigningCertificate</td>
       <td style="text-align:right">✅</td>
    </tr>
    <tr>
      <td>UpdateUser</td>
       <td style="text-align:right">✅</td>
    </tr>
    <tr>
      <td>UploadSSHPublicKey</td>
       <td style="text-align:right">✅</td>
    </tr>
    <tr>
      <td>UploadServerCertificate</td>
       <td style="text-align:right">✅</td>
    </tr>
    <tr>
      <td>UploadSigningCertificate</td>
       <td style="text-align:right">✅</td>
    </tr>
  </tbody>
  <tbody>    <tr>
      <td><a data-toggle="collapse" href=".iam-notimplemented">Show missing</a></td>
      <td style="text-align:right"></td>
    </tr>
  </tbody>
  <tbody class="collapse iam-notimplemented">     <tr>
      <td>AddClientIDToOpenIDConnectProvider</td>
       <td style="text-align:right">-</td>
    </tr>
    <tr>
      <td>ChangePassword</td>
       <td style="text-align:right">-</td>
    </tr>
    <tr>
      <td>CreateServiceSpecificCredential</td>
       <td style="text-align:right">-</td>
    </tr>
    <tr>
      <td>DeleteServiceSpecificCredential</td>
       <td style="text-align:right">-</td>
    </tr>
    <tr>
      <td>GenerateOrganizationsAccessReport</td>
       <td style="text-align:right">-</td>
    </tr>
    <tr>
      <td>GenerateServiceLastAccessedDetails</td>
       <td style="text-align:right">-</td>
    </tr>
    <tr>
      <td>GetContextKeysForCustomPolicy</td>
       <td style="text-align:right">-</td>
    </tr>
    <tr>
      <td>GetContextKeysForPrincipalPolicy</td>
       <td style="text-align:right">-</td>
    </tr>
    <tr>
      <td>GetOrganizationsAccessReport</td>
       <td style="text-align:right">-</td>
    </tr>
    <tr>
      <td>GetServiceLastAccessedDetails</td>
       <td style="text-align:right">-</td>
    </tr>
    <tr>
      <td>GetServiceLastAccessedDetailsWithEntities</td>
       <td style="text-align:right">-</td>
    </tr>
    <tr>
      <td>ListMFADeviceTags</td>
       <td style="text-align:right">-</td>
    </tr>
    <tr>
      <td>ListPoliciesGrantingServiceAccess</td>
       <td style="text-align:right">-</td>
    </tr>
    <tr>
      <td>ListSAMLProviderTags</td>
       <td style="text-align:right">-</td>
    </tr>
    <tr>
      <td>ListServerCertificateTags</td>
       <td style="text-align:right">-</td>
    </tr>
    <tr>
      <td>ListServiceSpecificCredentials</td>
       <td style="text-align:right">-</td>
    </tr>
    <tr>
      <td>RemoveClientIDFromOpenIDConnectProvider</td>
       <td style="text-align:right">-</td>
    </tr>
    <tr>
      <td>ResetServiceSpecificCredential</td>
       <td style="text-align:right">-</td>
    </tr>
    <tr>
      <td>ResyncMFADevice</td>
       <td style="text-align:right">-</td>
    </tr>
    <tr>
      <td>SetSecurityTokenServicePreferences</td>
       <td style="text-align:right">-</td>
    </tr>
    <tr>
      <td>SimulateCustomPolicy</td>
       <td style="text-align:right">-</td>
    </tr>
    <tr>
      <td>TagMFADevice</td>
       <td style="text-align:right">-</td>
    </tr>
    <tr>
      <td>TagSAMLProvider</td>
       <td style="text-align:right">-</td>
    </tr>
    <tr>
      <td>TagServerCertificate</td>
       <td style="text-align:right">-</td>
    </tr>
    <tr>
      <td>UntagMFADevice</td>
       <td style="text-align:right">-</td>
    </tr>
    <tr>
      <td>UntagSAMLProvider</td>
       <td style="text-align:right">-</td>
    </tr>
    <tr>
      <td>UntagServerCertificate</td>
       <td style="text-align:right">-</td>
    </tr>
    <tr>
      <td>UpdateServerCertificate</td>
       <td style="text-align:right">-</td>
    </tr>
    <tr>
      <td>UpdateServiceSpecificCredential</td>
       <td style="text-align:right">-</td>
    </tr>
  </tbody>
 </table>


## iot ##

<table>
  <thead>
    <tr>
      <th>Operation</th>
      <th style="text-align:right">Implemented</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td>AcceptCertificateTransfer (Pro) </td>
       <td style="text-align:right">✅</td>
    </tr>
    <tr>
      <td>AddThingToThingGroup (Pro)  <a href="#misc" title="covered by our integration test suite">✨</a></td>
       <td style="text-align:right">✅</td>
    </tr>
    <tr>
      <td>AttachPolicy (Pro)  <a href="#misc" title="covered by our integration test suite">✨</a></td>
       <td style="text-align:right">✅</td>
    </tr>
    <tr>
      <td>AttachPrincipalPolicy (Pro) </td>
       <td style="text-align:right">✅</td>
    </tr>
    <tr>
      <td>AttachThingPrincipal (Pro)  <a href="#misc" title="covered by our integration test suite">✨</a></td>
       <td style="text-align:right">✅</td>
    </tr>
    <tr>
      <td>CancelJob (Pro) </td>
       <td style="text-align:right">✅</td>
    </tr>
    <tr>
      <td>CancelJobExecution (Pro) </td>
       <td style="text-align:right">✅</td>
    </tr>
    <tr>
      <td>CreateCertificateFromCsr (Pro) </td>
       <td style="text-align:right">✅</td>
    </tr>
    <tr>
      <td>CreateDomainConfiguration (Pro) </td>
       <td style="text-align:right">✅</td>
    </tr>
    <tr>
      <td>CreateDynamicThingGroup (Pro)  <a href="#misc" title="covered by our integration test suite">✨</a></td>
       <td style="text-align:right">✅</td>
    </tr>
    <tr>
      <td>CreateJob (Pro)  <a href="#misc" title="covered by our integration test suite">✨</a></td>
       <td style="text-align:right">✅</td>
    </tr>
    <tr>
      <td>CreateKeysAndCertificate (Pro) </td>
       <td style="text-align:right">✅</td>
    </tr>
    <tr>
      <td>CreatePolicy (Pro)  <a href="#misc" title="covered by our integration test suite">✨</a></td>
       <td style="text-align:right">✅</td>
    </tr>
    <tr>
      <td>CreatePolicyVersion (Pro) </td>
       <td style="text-align:right">✅</td>
    </tr>
    <tr>
      <td>CreateThing (Pro)  <a href="#misc" title="covered by our integration test suite">✨</a></td>
       <td style="text-align:right">✅</td>
    </tr>
    <tr>
      <td>CreateThingGroup (Pro)  <a href="#misc" title="covered by our integration test suite">✨</a></td>
       <td style="text-align:right">✅</td>
    </tr>
    <tr>
      <td>CreateThingType (Pro) </td>
       <td style="text-align:right">✅</td>
    </tr>
    <tr>
      <td>CreateTopicRule (Pro)  <a href="#misc" title="covered by our integration test suite">✨</a></td>
       <td style="text-align:right">✅</td>
    </tr>
    <tr>
      <td>CreateTopicRuleDestination (Pro)  <a href="#misc" title="covered by our integration test suite">✨</a></td>
       <td style="text-align:right">✅</td>
    </tr>
    <tr>
      <td>DeleteCACertificate (Pro) </td>
       <td style="text-align:right">✅</td>
    </tr>
    <tr>
      <td>DeleteCertificate (Pro) </td>
       <td style="text-align:right">✅</td>
    </tr>
    <tr>
      <td>DeleteDomainConfiguration (Pro) </td>
       <td style="text-align:right">✅</td>
    </tr>
    <tr>
      <td>DeleteDynamicThingGroup (Pro)  <a href="#misc" title="covered by our integration test suite">✨</a></td>
       <td style="text-align:right">✅</td>
    </tr>
    <tr>
      <td>DeleteJob (Pro)  <a href="#misc" title="covered by our integration test suite">✨</a></td>
       <td style="text-align:right">✅</td>
    </tr>
    <tr>
      <td>DeleteJobExecution (Pro) </td>
       <td style="text-align:right">✅</td>
    </tr>
    <tr>
      <td>DeletePolicy (Pro)  <a href="#misc" title="covered by our integration test suite">✨</a></td>
       <td style="text-align:right">✅</td>
    </tr>
    <tr>
      <td>DeletePolicyVersion (Pro) </td>
       <td style="text-align:right">✅</td>
    </tr>
    <tr>
      <td>DeleteThing (Pro)  <a href="#misc" title="covered by our integration test suite">✨</a></td>
       <td style="text-align:right">✅</td>
    </tr>
    <tr>
      <td>DeleteThingGroup (Pro)  <a href="#misc" title="covered by our integration test suite">✨</a></td>
       <td style="text-align:right">✅</td>
    </tr>
    <tr>
      <td>DeleteThingType (Pro) </td>
       <td style="text-align:right">✅</td>
    </tr>
    <tr>
      <td>DeleteTopicRule (Pro)  <a href="#misc" title="covered by our integration test suite">✨</a></td>
       <td style="text-align:right">✅</td>
    </tr>
    <tr>
      <td>DeleteTopicRuleDestination (Pro) </td>
       <td style="text-align:right">✅</td>
    </tr>
    <tr>
      <td>DeprecateThingType (Pro) </td>
       <td style="text-align:right">✅</td>
    </tr>
    <tr>
      <td>DescribeCACertificate (Pro) </td>
       <td style="text-align:right">✅</td>
    </tr>
    <tr>
      <td>DescribeCertificate (Pro) </td>
       <td style="text-align:right">✅</td>
    </tr>
    <tr>
      <td>DescribeDomainConfiguration (Pro) </td>
       <td style="text-align:right">✅</td>
    </tr>
    <tr>
      <td>DescribeEndpoint (Pro)  <a href="#misc" title="covered by our integration test suite">✨</a></td>
       <td style="text-align:right">✅</td>
    </tr>
    <tr>
      <td>DescribeJob (Pro)  <a href="#misc" title="covered by our integration test suite">✨</a></td>
       <td style="text-align:right">✅</td>
    </tr>
    <tr>
      <td>DescribeJobExecution (Pro)  <a href="#misc" title="covered by our integration test suite">✨</a></td>
       <td style="text-align:right">✅</td>
    </tr>
    <tr>
      <td>DescribeThing (Pro)  <a href="#misc" title="covered by our integration test suite">✨</a></td>
       <td style="text-align:right">✅</td>
    </tr>
    <tr>
      <td>DescribeThingGroup (Pro)  <a href="#misc" title="covered by our integration test suite">✨</a></td>
       <td style="text-align:right">✅</td>
    </tr>
    <tr>
      <td>DescribeThingType (Pro) </td>
       <td style="text-align:right">✅</td>
    </tr>
    <tr>
      <td>DetachPolicy (Pro) </td>
       <td style="text-align:right">✅</td>
    </tr>
    <tr>
      <td>DetachPrincipalPolicy (Pro) </td>
       <td style="text-align:right">✅</td>
    </tr>
    <tr>
      <td>DetachThingPrincipal (Pro)  <a href="#misc" title="covered by our integration test suite">✨</a></td>
       <td style="text-align:right">✅</td>
    </tr>
    <tr>
      <td>DisableTopicRule (Pro) </td>
       <td style="text-align:right">✅</td>
    </tr>
    <tr>
      <td>EnableTopicRule (Pro) </td>
       <td style="text-align:right">✅</td>
    </tr>
    <tr>
      <td>GetJobDocument (Pro) </td>
       <td style="text-align:right">✅</td>
    </tr>
    <tr>
      <td>GetPolicy (Pro)  <a href="#misc" title="covered by our integration test suite">✨</a></td>
       <td style="text-align:right">✅</td>
    </tr>
    <tr>
      <td>GetPolicyVersion (Pro) </td>
       <td style="text-align:right">✅</td>
    </tr>
    <tr>
      <td>GetRegistrationCode (Pro) </td>
       <td style="text-align:right">✅</td>
    </tr>
    <tr>
      <td>GetTopicRule (Pro)  <a href="#misc" title="covered by our integration test suite">✨</a></td>
       <td style="text-align:right">✅</td>
    </tr>
    <tr>
      <td>GetTopicRuleDestination (Pro) </td>
       <td style="text-align:right">✅</td>
    </tr>
    <tr>
      <td>ListAttachedPolicies (Pro) </td>
       <td style="text-align:right">✅</td>
    </tr>
    <tr>
      <td>ListAuditMitigationActionsTasks (Pro) </td>
       <td style="text-align:right">✅</td>
    </tr>
    <tr>
      <td>ListAuditTasks (Pro) </td>
       <td style="text-align:right">✅</td>
    </tr>
    <tr>
      <td>ListCertificates (Pro) </td>
       <td style="text-align:right">✅</td>
    </tr>
    <tr>
      <td>ListCertificatesByCA (Pro) </td>
       <td style="text-align:right">✅</td>
    </tr>
    <tr>
      <td>ListDetectMitigationActionsExecutions (Pro) </td>
       <td style="text-align:right">✅</td>
    </tr>
    <tr>
      <td>ListDetectMitigationActionsTasks (Pro) </td>
       <td style="text-align:right">✅</td>
    </tr>
    <tr>
      <td>ListDomainConfigurations (Pro) </td>
       <td style="text-align:right">✅</td>
    </tr>
    <tr>
      <td>ListJobExecutionsForJob (Pro) </td>
       <td style="text-align:right">✅</td>
    </tr>
    <tr>
      <td>ListJobExecutionsForThing (Pro)  <a href="#misc" title="covered by our integration test suite">✨</a></td>
       <td style="text-align:right">✅</td>
    </tr>
    <tr>
      <td>ListJobs (Pro)  <a href="#misc" title="covered by our integration test suite">✨</a></td>
       <td style="text-align:right">✅</td>
    </tr>
    <tr>
      <td>ListMetricValues (Pro) </td>
       <td style="text-align:right">✅</td>
    </tr>
    <tr>
      <td>ListPolicies (Pro)  <a href="#misc" title="covered by our integration test suite">✨</a></td>
       <td style="text-align:right">✅</td>
    </tr>
    <tr>
      <td>ListPolicyPrincipals (Pro) </td>
       <td style="text-align:right">✅</td>
    </tr>
    <tr>
      <td>ListPolicyVersions (Pro) </td>
       <td style="text-align:right">✅</td>
    </tr>
    <tr>
      <td>ListPrincipalPolicies (Pro) </td>
       <td style="text-align:right">✅</td>
    </tr>
    <tr>
      <td>ListPrincipalThings (Pro) </td>
       <td style="text-align:right">✅</td>
    </tr>
    <tr>
      <td>ListTagsForResource (Pro)  <a href="#misc" title="covered by our integration test suite">✨</a></td>
       <td style="text-align:right">✅</td>
    </tr>
    <tr>
      <td>ListTargetsForPolicy (Pro) </td>
       <td style="text-align:right">✅</td>
    </tr>
    <tr>
      <td>ListThingGroups (Pro)  <a href="#misc" title="covered by our integration test suite">✨</a></td>
       <td style="text-align:right">✅</td>
    </tr>
    <tr>
      <td>ListThingGroupsForThing (Pro)  <a href="#misc" title="covered by our integration test suite">✨</a></td>
       <td style="text-align:right">✅</td>
    </tr>
    <tr>
      <td>ListThingPrincipals (Pro)  <a href="#misc" title="covered by our integration test suite">✨</a></td>
       <td style="text-align:right">✅</td>
    </tr>
    <tr>
      <td>ListThingTypes (Pro) </td>
       <td style="text-align:right">✅</td>
    </tr>
    <tr>
      <td>ListThings (Pro)  <a href="#misc" title="covered by our integration test suite">✨</a></td>
       <td style="text-align:right">✅</td>
    </tr>
    <tr>
      <td>ListThingsInThingGroup (Pro)  <a href="#misc" title="covered by our integration test suite">✨</a></td>
       <td style="text-align:right">✅</td>
    </tr>
    <tr>
      <td>ListTopicRules (Pro)  <a href="#misc" title="covered by our integration test suite">✨</a></td>
       <td style="text-align:right">✅</td>
    </tr>
    <tr>
      <td>ListViolationEvents (Pro) </td>
       <td style="text-align:right">✅</td>
    </tr>
    <tr>
      <td>RegisterCACertificate (Pro) </td>
       <td style="text-align:right">✅</td>
    </tr>
    <tr>
      <td>RegisterCertificate (Pro)  <a href="#misc" title="covered by our integration test suite">✨</a></td>
       <td style="text-align:right">✅</td>
    </tr>
    <tr>
      <td>RegisterCertificateWithoutCA (Pro) </td>
       <td style="text-align:right">✅</td>
    </tr>
    <tr>
      <td>RemoveThingFromThingGroup (Pro)  <a href="#misc" title="covered by our integration test suite">✨</a></td>
       <td style="text-align:right">✅</td>
    </tr>
    <tr>
      <td>ReplaceTopicRule (Pro) </td>
       <td style="text-align:right">✅</td>
    </tr>
    <tr>
      <td>SearchIndex (Pro)  <a href="#misc" title="covered by our integration test suite">✨</a></td>
       <td style="text-align:right">✅</td>
    </tr>
    <tr>
      <td>SetDefaultPolicyVersion (Pro) </td>
       <td style="text-align:right">✅</td>
    </tr>
    <tr>
      <td>TagResource (Pro)  <a href="#misc" title="covered by our integration test suite">✨</a></td>
       <td style="text-align:right">✅</td>
    </tr>
    <tr>
      <td>UpdateCACertificate (Pro) </td>
       <td style="text-align:right">✅</td>
    </tr>
    <tr>
      <td>UpdateCertificate (Pro) </td>
       <td style="text-align:right">✅</td>
    </tr>
    <tr>
      <td>UpdateDomainConfiguration (Pro) </td>
       <td style="text-align:right">✅</td>
    </tr>
    <tr>
      <td>UpdateDynamicThingGroup (Pro)  <a href="#misc" title="covered by our integration test suite">✨</a></td>
       <td style="text-align:right">✅</td>
    </tr>
    <tr>
      <td>UpdateIndexingConfiguration (Pro)  <a href="#misc" title="covered by our integration test suite">✨</a></td>
       <td style="text-align:right">✅</td>
    </tr>
    <tr>
      <td>UpdateThing (Pro) </td>
       <td style="text-align:right">✅</td>
    </tr>
    <tr>
      <td>UpdateThingGroup (Pro) </td>
       <td style="text-align:right">✅</td>
    </tr>
    <tr>
      <td>UpdateThingGroupsForThing (Pro) </td>
       <td style="text-align:right">✅</td>
    </tr>
  </tbody>
  <tbody>    <tr>
      <td><a data-toggle="collapse" href=".iot-notimplemented">Show missing</a></td>
      <td style="text-align:right"></td>
    </tr>
  </tbody>
  <tbody class="collapse iot-notimplemented">     <tr>
      <td>AddThingToBillingGroup</td>
       <td style="text-align:right">-</td>
    </tr>
    <tr>
      <td>AssociateTargetsWithJob</td>
       <td style="text-align:right">-</td>
    </tr>
    <tr>
      <td>AttachSecurityProfile</td>
       <td style="text-align:right">-</td>
    </tr>
    <tr>
      <td>CancelAuditMitigationActionsTask</td>
       <td style="text-align:right">-</td>
    </tr>
    <tr>
      <td>CancelAuditTask</td>
       <td style="text-align:right">-</td>
    </tr>
    <tr>
      <td>CancelCertificateTransfer</td>
       <td style="text-align:right">-</td>
    </tr>
    <tr>
      <td>CancelDetectMitigationActionsTask</td>
       <td style="text-align:right">-</td>
    </tr>
    <tr>
      <td>ClearDefaultAuthorizer</td>
       <td style="text-align:right">-</td>
    </tr>
    <tr>
      <td>ConfirmTopicRuleDestination</td>
       <td style="text-align:right">-</td>
    </tr>
    <tr>
      <td>CreateAuditSuppression</td>
       <td style="text-align:right">-</td>
    </tr>
    <tr>
      <td>CreateAuthorizer</td>
       <td style="text-align:right">-</td>
    </tr>
    <tr>
      <td>CreateBillingGroup</td>
       <td style="text-align:right">-</td>
    </tr>
    <tr>
      <td>CreateCustomMetric</td>
       <td style="text-align:right">-</td>
    </tr>
    <tr>
      <td>CreateDimension</td>
       <td style="text-align:right">-</td>
    </tr>
    <tr>
      <td>CreateFleetMetric</td>
       <td style="text-align:right">-</td>
    </tr>
    <tr>
      <td>CreateJobTemplate</td>
       <td style="text-align:right">-</td>
    </tr>
    <tr>
      <td>CreateMitigationAction</td>
       <td style="text-align:right">-</td>
    </tr>
    <tr>
      <td>CreateOTAUpdate</td>
       <td style="text-align:right">-</td>
    </tr>
    <tr>
      <td>CreateProvisioningClaim</td>
       <td style="text-align:right">-</td>
    </tr>
    <tr>
      <td>CreateProvisioningTemplate</td>
       <td style="text-align:right">-</td>
    </tr>
    <tr>
      <td>CreateProvisioningTemplateVersion</td>
       <td style="text-align:right">-</td>
    </tr>
    <tr>
      <td>CreateRoleAlias</td>
       <td style="text-align:right">-</td>
    </tr>
    <tr>
      <td>CreateScheduledAudit</td>
       <td style="text-align:right">-</td>
    </tr>
    <tr>
      <td>CreateSecurityProfile</td>
       <td style="text-align:right">-</td>
    </tr>
    <tr>
      <td>CreateStream</td>
       <td style="text-align:right">-</td>
    </tr>
    <tr>
      <td>DeleteAccountAuditConfiguration</td>
       <td style="text-align:right">-</td>
    </tr>
    <tr>
      <td>DeleteAuditSuppression</td>
       <td style="text-align:right">-</td>
    </tr>
    <tr>
      <td>DeleteAuthorizer</td>
       <td style="text-align:right">-</td>
    </tr>
    <tr>
      <td>DeleteBillingGroup</td>
       <td style="text-align:right">-</td>
    </tr>
    <tr>
      <td>DeleteCustomMetric</td>
       <td style="text-align:right">-</td>
    </tr>
    <tr>
      <td>DeleteDimension</td>
       <td style="text-align:right">-</td>
    </tr>
    <tr>
      <td>DeleteFleetMetric</td>
       <td style="text-align:right">-</td>
    </tr>
    <tr>
      <td>DeleteJobTemplate</td>
       <td style="text-align:right">-</td>
    </tr>
    <tr>
      <td>DeleteMitigationAction</td>
       <td style="text-align:right">-</td>
    </tr>
    <tr>
      <td>DeleteOTAUpdate</td>
       <td style="text-align:right">-</td>
    </tr>
    <tr>
      <td>DeleteProvisioningTemplate</td>
       <td style="text-align:right">-</td>
    </tr>
    <tr>
      <td>DeleteProvisioningTemplateVersion</td>
       <td style="text-align:right">-</td>
    </tr>
    <tr>
      <td>DeleteRegistrationCode</td>
       <td style="text-align:right">-</td>
    </tr>
    <tr>
      <td>DeleteRoleAlias</td>
       <td style="text-align:right">-</td>
    </tr>
    <tr>
      <td>DeleteScheduledAudit</td>
       <td style="text-align:right">-</td>
    </tr>
    <tr>
      <td>DeleteSecurityProfile</td>
       <td style="text-align:right">-</td>
    </tr>
    <tr>
      <td>DeleteStream</td>
       <td style="text-align:right">-</td>
    </tr>
    <tr>
      <td>DeleteV2LoggingLevel</td>
       <td style="text-align:right">-</td>
    </tr>
    <tr>
      <td>DescribeAccountAuditConfiguration</td>
       <td style="text-align:right">-</td>
    </tr>
    <tr>
      <td>DescribeAuditFinding</td>
       <td style="text-align:right">-</td>
    </tr>
    <tr>
      <td>DescribeAuditMitigationActionsTask</td>
       <td style="text-align:right">-</td>
    </tr>
    <tr>
      <td>DescribeAuditSuppression</td>
       <td style="text-align:right">-</td>
    </tr>
    <tr>
      <td>DescribeAuditTask</td>
       <td style="text-align:right">-</td>
    </tr>
    <tr>
      <td>DescribeAuthorizer</td>
       <td style="text-align:right">-</td>
    </tr>
    <tr>
      <td>DescribeBillingGroup</td>
       <td style="text-align:right">-</td>
    </tr>
    <tr>
      <td>DescribeCustomMetric</td>
       <td style="text-align:right">-</td>
    </tr>
    <tr>
      <td>DescribeDefaultAuthorizer</td>
       <td style="text-align:right">-</td>
    </tr>
    <tr>
      <td>DescribeDetectMitigationActionsTask</td>
       <td style="text-align:right">-</td>
    </tr>
    <tr>
      <td>DescribeDimension</td>
       <td style="text-align:right">-</td>
    </tr>
    <tr>
      <td>DescribeEventConfigurations</td>
       <td style="text-align:right">-</td>
    </tr>
    <tr>
      <td>DescribeFleetMetric</td>
       <td style="text-align:right">-</td>
    </tr>
    <tr>
      <td>DescribeIndex</td>
       <td style="text-align:right">-</td>
    </tr>
    <tr>
      <td>DescribeJobTemplate</td>
       <td style="text-align:right">-</td>
    </tr>
    <tr>
      <td>DescribeManagedJobTemplate</td>
       <td style="text-align:right">-</td>
    </tr>
    <tr>
      <td>DescribeMitigationAction</td>
       <td style="text-align:right">-</td>
    </tr>
    <tr>
      <td>DescribeProvisioningTemplate</td>
       <td style="text-align:right">-</td>
    </tr>
    <tr>
      <td>DescribeProvisioningTemplateVersion</td>
       <td style="text-align:right">-</td>
    </tr>
    <tr>
      <td>DescribeRoleAlias</td>
       <td style="text-align:right">-</td>
    </tr>
    <tr>
      <td>DescribeScheduledAudit</td>
       <td style="text-align:right">-</td>
    </tr>
    <tr>
      <td>DescribeSecurityProfile</td>
       <td style="text-align:right">-</td>
    </tr>
    <tr>
      <td>DescribeStream</td>
       <td style="text-align:right">-</td>
    </tr>
    <tr>
      <td>DescribeThingRegistrationTask</td>
       <td style="text-align:right">-</td>
    </tr>
    <tr>
      <td>DetachSecurityProfile</td>
       <td style="text-align:right">-</td>
    </tr>
    <tr>
      <td>GetBehaviorModelTrainingSummaries</td>
       <td style="text-align:right">-</td>
    </tr>
    <tr>
      <td>GetBucketsAggregation</td>
       <td style="text-align:right">-</td>
    </tr>
    <tr>
      <td>GetCardinality</td>
       <td style="text-align:right">-</td>
    </tr>
    <tr>
      <td>GetEffectivePolicies</td>
       <td style="text-align:right">-</td>
    </tr>
    <tr>
      <td>GetIndexingConfiguration</td>
       <td style="text-align:right">-</td>
    </tr>
    <tr>
      <td>GetLoggingOptions</td>
       <td style="text-align:right">-</td>
    </tr>
    <tr>
      <td>GetOTAUpdate</td>
       <td style="text-align:right">-</td>
    </tr>
    <tr>
      <td>GetPercentiles</td>
       <td style="text-align:right">-</td>
    </tr>
    <tr>
      <td>GetStatistics</td>
       <td style="text-align:right">-</td>
    </tr>
    <tr>
      <td>GetV2LoggingOptions</td>
       <td style="text-align:right">-</td>
    </tr>
    <tr>
      <td>ListActiveViolations</td>
       <td style="text-align:right">-</td>
    </tr>
    <tr>
      <td>ListAuditFindings</td>
       <td style="text-align:right">-</td>
    </tr>
    <tr>
      <td>ListAuditMitigationActionsExecutions</td>
       <td style="text-align:right">-</td>
    </tr>
    <tr>
      <td>ListAuditSuppressions</td>
       <td style="text-align:right">-</td>
    </tr>
    <tr>
      <td>ListAuthorizers</td>
       <td style="text-align:right">-</td>
    </tr>
    <tr>
      <td>ListBillingGroups</td>
       <td style="text-align:right">-</td>
    </tr>
    <tr>
      <td>ListCACertificates</td>
       <td style="text-align:right">-</td>
    </tr>
    <tr>
      <td>ListCustomMetrics</td>
       <td style="text-align:right">-</td>
    </tr>
    <tr>
      <td>ListDimensions</td>
       <td style="text-align:right">-</td>
    </tr>
    <tr>
      <td>ListFleetMetrics</td>
       <td style="text-align:right">-</td>
    </tr>
    <tr>
      <td>ListIndices</td>
       <td style="text-align:right">-</td>
    </tr>
    <tr>
      <td>ListJobTemplates</td>
       <td style="text-align:right">-</td>
    </tr>
    <tr>
      <td>ListManagedJobTemplates</td>
       <td style="text-align:right">-</td>
    </tr>
    <tr>
      <td>ListMitigationActions</td>
       <td style="text-align:right">-</td>
    </tr>
    <tr>
      <td>ListOTAUpdates</td>
       <td style="text-align:right">-</td>
    </tr>
    <tr>
      <td>ListOutgoingCertificates</td>
       <td style="text-align:right">-</td>
    </tr>
    <tr>
      <td>ListProvisioningTemplateVersions</td>
       <td style="text-align:right">-</td>
    </tr>
    <tr>
      <td>ListProvisioningTemplates</td>
       <td style="text-align:right">-</td>
    </tr>
    <tr>
      <td>ListRoleAliases</td>
       <td style="text-align:right">-</td>
    </tr>
    <tr>
      <td>ListScheduledAudits</td>
       <td style="text-align:right">-</td>
    </tr>
    <tr>
      <td>ListSecurityProfiles</td>
       <td style="text-align:right">-</td>
    </tr>
    <tr>
      <td>ListSecurityProfilesForTarget</td>
       <td style="text-align:right">-</td>
    </tr>
    <tr>
      <td>ListStreams</td>
       <td style="text-align:right">-</td>
    </tr>
    <tr>
      <td>ListTargetsForSecurityProfile</td>
       <td style="text-align:right">-</td>
    </tr>
    <tr>
      <td>ListThingRegistrationTaskReports</td>
       <td style="text-align:right">-</td>
    </tr>
    <tr>
      <td>ListThingRegistrationTasks</td>
       <td style="text-align:right">-</td>
    </tr>
    <tr>
      <td>ListThingsInBillingGroup</td>
       <td style="text-align:right">-</td>
    </tr>
    <tr>
      <td>ListTopicRuleDestinations</td>
       <td style="text-align:right">-</td>
    </tr>
    <tr>
      <td>ListV2LoggingLevels</td>
       <td style="text-align:right">-</td>
    </tr>
    <tr>
      <td>PutVerificationStateOnViolation</td>
       <td style="text-align:right">-</td>
    </tr>
    <tr>
      <td>RegisterThing</td>
       <td style="text-align:right">-</td>
    </tr>
    <tr>
      <td>RejectCertificateTransfer</td>
       <td style="text-align:right">-</td>
    </tr>
    <tr>
      <td>RemoveThingFromBillingGroup</td>
       <td style="text-align:right">-</td>
    </tr>
    <tr>
      <td>SetDefaultAuthorizer</td>
       <td style="text-align:right">-</td>
    </tr>
    <tr>
      <td>SetLoggingOptions</td>
       <td style="text-align:right">-</td>
    </tr>
    <tr>
      <td>SetV2LoggingLevel</td>
       <td style="text-align:right">-</td>
    </tr>
    <tr>
      <td>SetV2LoggingOptions</td>
       <td style="text-align:right">-</td>
    </tr>
    <tr>
      <td>StartAuditMitigationActionsTask</td>
       <td style="text-align:right">-</td>
    </tr>
    <tr>
      <td>StartDetectMitigationActionsTask</td>
       <td style="text-align:right">-</td>
    </tr>
    <tr>
      <td>StartOnDemandAuditTask</td>
       <td style="text-align:right">-</td>
    </tr>
    <tr>
      <td>StartThingRegistrationTask</td>
       <td style="text-align:right">-</td>
    </tr>
    <tr>
      <td>StopThingRegistrationTask</td>
       <td style="text-align:right">-</td>
    </tr>
    <tr>
      <td>TestAuthorization</td>
       <td style="text-align:right">-</td>
    </tr>
    <tr>
      <td>TestInvokeAuthorizer</td>
       <td style="text-align:right">-</td>
    </tr>
    <tr>
      <td>TransferCertificate</td>
       <td style="text-align:right">-</td>
    </tr>
    <tr>
      <td>UntagResource</td>
       <td style="text-align:right">-</td>
    </tr>
    <tr>
      <td>UpdateAccountAuditConfiguration</td>
       <td style="text-align:right">-</td>
    </tr>
    <tr>
      <td>UpdateAuditSuppression</td>
       <td style="text-align:right">-</td>
    </tr>
    <tr>
      <td>UpdateAuthorizer</td>
       <td style="text-align:right">-</td>
    </tr>
    <tr>
      <td>UpdateBillingGroup</td>
       <td style="text-align:right">-</td>
    </tr>
    <tr>
      <td>UpdateCustomMetric</td>
       <td style="text-align:right">-</td>
    </tr>
    <tr>
      <td>UpdateDimension</td>
       <td style="text-align:right">-</td>
    </tr>
    <tr>
      <td>UpdateEventConfigurations</td>
       <td style="text-align:right">-</td>
    </tr>
    <tr>
      <td>UpdateFleetMetric</td>
       <td style="text-align:right">-</td>
    </tr>
    <tr>
      <td>UpdateJob</td>
       <td style="text-align:right">-</td>
    </tr>
    <tr>
      <td>UpdateMitigationAction</td>
       <td style="text-align:right">-</td>
    </tr>
    <tr>
      <td>UpdateProvisioningTemplate</td>
       <td style="text-align:right">-</td>
    </tr>
    <tr>
      <td>UpdateRoleAlias</td>
       <td style="text-align:right">-</td>
    </tr>
    <tr>
      <td>UpdateScheduledAudit</td>
       <td style="text-align:right">-</td>
    </tr>
    <tr>
      <td>UpdateSecurityProfile</td>
       <td style="text-align:right">-</td>
    </tr>
    <tr>
      <td>UpdateStream</td>
       <td style="text-align:right">-</td>
    </tr>
    <tr>
      <td>UpdateTopicRuleDestination</td>
       <td style="text-align:right">-</td>
    </tr>
    <tr>
      <td>ValidateSecurityProfileBehaviors</td>
       <td style="text-align:right">-</td>
    </tr>
  </tbody>
 </table>


## iot-data ##

<table>
  <thead>
    <tr>
      <th>Operation</th>
      <th style="text-align:right">Implemented</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td>DeleteThingShadow (Pro) </td>
       <td style="text-align:right">✅</td>
    </tr>
    <tr>
      <td>GetThingShadow (Pro)  <a href="#misc" title="covered by our integration test suite">✨</a></td>
       <td style="text-align:right">✅</td>
    </tr>
    <tr>
      <td>Publish (Pro)  <a href="#misc" title="covered by our integration test suite">✨</a></td>
       <td style="text-align:right">✅</td>
    </tr>
    <tr>
      <td>UpdateThingShadow (Pro)  <a href="#misc" title="covered by our integration test suite">✨</a></td>
       <td style="text-align:right">✅</td>
    </tr>
  </tbody>
  <tbody>    <tr>
      <td><a data-toggle="collapse" href=".iot-data-notimplemented">Show missing</a></td>
      <td style="text-align:right"></td>
    </tr>
  </tbody>
  <tbody class="collapse iot-data-notimplemented">     <tr>
      <td>GetRetainedMessage</td>
       <td style="text-align:right">-</td>
    </tr>
    <tr>
      <td>ListNamedShadowsForThing</td>
       <td style="text-align:right">-</td>
    </tr>
    <tr>
      <td>ListRetainedMessages</td>
       <td style="text-align:right">-</td>
    </tr>
  </tbody>
 </table>


## iotanalytics ##

<table>
  <thead>
    <tr>
      <th>Operation</th>
      <th style="text-align:right">Implemented</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td>CreateChannel (Pro)  <a href="#misc" title="covered by our integration test suite">✨</a></td>
       <td style="text-align:right">✅</td>
    </tr>
    <tr>
      <td>CreateDataset (Pro)  <a href="#misc" title="covered by our integration test suite">✨</a></td>
       <td style="text-align:right">✅</td>
    </tr>
    <tr>
      <td>CreateDatastore (Pro)  <a href="#misc" title="covered by our integration test suite">✨</a></td>
       <td style="text-align:right">✅</td>
    </tr>
    <tr>
      <td>CreatePipeline (Pro)  <a href="#misc" title="covered by our integration test suite">✨</a></td>
       <td style="text-align:right">✅</td>
    </tr>
    <tr>
      <td>DeleteChannel (Pro)  <a href="#misc" title="covered by our integration test suite">✨</a></td>
       <td style="text-align:right">✅</td>
    </tr>
    <tr>
      <td>DeleteDataset (Pro)  <a href="#misc" title="covered by our integration test suite">✨</a></td>
       <td style="text-align:right">✅</td>
    </tr>
    <tr>
      <td>DeleteDatastore (Pro)  <a href="#misc" title="covered by our integration test suite">✨</a></td>
       <td style="text-align:right">✅</td>
    </tr>
    <tr>
      <td>DeletePipeline (Pro)  <a href="#misc" title="covered by our integration test suite">✨</a></td>
       <td style="text-align:right">✅</td>
    </tr>
    <tr>
      <td>DescribeChannel (Pro)  <a href="#misc" title="covered by our integration test suite">✨</a></td>
       <td style="text-align:right">✅</td>
    </tr>
    <tr>
      <td>DescribeDataset (Pro)  <a href="#misc" title="covered by our integration test suite">✨</a></td>
       <td style="text-align:right">✅</td>
    </tr>
    <tr>
      <td>DescribeDatastore (Pro)  <a href="#misc" title="covered by our integration test suite">✨</a></td>
       <td style="text-align:right">✅</td>
    </tr>
    <tr>
      <td>DescribePipeline (Pro)  <a href="#misc" title="covered by our integration test suite">✨</a></td>
       <td style="text-align:right">✅</td>
    </tr>
    <tr>
      <td>ListChannels (Pro)  <a href="#misc" title="covered by our integration test suite">✨</a></td>
       <td style="text-align:right">✅</td>
    </tr>
    <tr>
      <td>ListDatasetContents (Pro) </td>
       <td style="text-align:right">✅</td>
    </tr>
    <tr>
      <td>ListDatasets (Pro)  <a href="#misc" title="covered by our integration test suite">✨</a></td>
       <td style="text-align:right">✅</td>
    </tr>
    <tr>
      <td>ListDatastores (Pro)  <a href="#misc" title="covered by our integration test suite">✨</a></td>
       <td style="text-align:right">✅</td>
    </tr>
    <tr>
      <td>ListPipelines (Pro)  <a href="#misc" title="covered by our integration test suite">✨</a></td>
       <td style="text-align:right">✅</td>
    </tr>
    <tr>
      <td>SampleChannelData (Pro) </td>
       <td style="text-align:right">✅</td>
    </tr>
  </tbody>
  <tbody>    <tr>
      <td><a data-toggle="collapse" href=".iotanalytics-notimplemented">Show missing</a></td>
      <td style="text-align:right"></td>
    </tr>
  </tbody>
  <tbody class="collapse iotanalytics-notimplemented">     <tr>
      <td>BatchPutMessage</td>
       <td style="text-align:right">-</td>
    </tr>
    <tr>
      <td>CancelPipelineReprocessing</td>
       <td style="text-align:right">-</td>
    </tr>
    <tr>
      <td>CreateDatasetContent</td>
       <td style="text-align:right">-</td>
    </tr>
    <tr>
      <td>DeleteDatasetContent</td>
       <td style="text-align:right">-</td>
    </tr>
    <tr>
      <td>DescribeLoggingOptions</td>
       <td style="text-align:right">-</td>
    </tr>
    <tr>
      <td>GetDatasetContent</td>
       <td style="text-align:right">-</td>
    </tr>
    <tr>
      <td>ListTagsForResource</td>
       <td style="text-align:right">-</td>
    </tr>
    <tr>
      <td>PutLoggingOptions</td>
       <td style="text-align:right">-</td>
    </tr>
    <tr>
      <td>RunPipelineActivity</td>
       <td style="text-align:right">-</td>
    </tr>
    <tr>
      <td>StartPipelineReprocessing</td>
       <td style="text-align:right">-</td>
    </tr>
    <tr>
      <td>TagResource</td>
       <td style="text-align:right">-</td>
    </tr>
    <tr>
      <td>UntagResource</td>
       <td style="text-align:right">-</td>
    </tr>
    <tr>
      <td>UpdateChannel</td>
       <td style="text-align:right">-</td>
    </tr>
    <tr>
      <td>UpdateDataset</td>
       <td style="text-align:right">-</td>
    </tr>
    <tr>
      <td>UpdateDatastore</td>
       <td style="text-align:right">-</td>
    </tr>
    <tr>
      <td>UpdatePipeline</td>
       <td style="text-align:right">-</td>
    </tr>
  </tbody>
 </table>


## iotwireless ##

<table>
  <thead>
    <tr>
      <th>Operation</th>
      <th style="text-align:right">Implemented</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td>CreateDeviceProfile (Pro)  <a href="#misc" title="covered by our integration test suite">✨</a></td>
       <td style="text-align:right">✅</td>
    </tr>
    <tr>
      <td>CreateWirelessDevice (Pro)  <a href="#misc" title="covered by our integration test suite">✨</a></td>
       <td style="text-align:right">✅</td>
    </tr>
    <tr>
      <td>CreateWirelessGateway (Pro)  <a href="#misc" title="covered by our integration test suite">✨</a></td>
       <td style="text-align:right">✅</td>
    </tr>
    <tr>
      <td>DeleteDeviceProfile (Pro)  <a href="#misc" title="covered by our integration test suite">✨</a></td>
       <td style="text-align:right">✅</td>
    </tr>
    <tr>
      <td>DeleteWirelessDevice (Pro)  <a href="#misc" title="covered by our integration test suite">✨</a></td>
       <td style="text-align:right">✅</td>
    </tr>
    <tr>
      <td>DeleteWirelessGateway (Pro)  <a href="#misc" title="covered by our integration test suite">✨</a></td>
       <td style="text-align:right">✅</td>
    </tr>
    <tr>
      <td>GetDeviceProfile (Pro)  <a href="#misc" title="covered by our integration test suite">✨</a></td>
       <td style="text-align:right">✅</td>
    </tr>
    <tr>
      <td>GetWirelessDevice (Pro)  <a href="#misc" title="covered by our integration test suite">✨</a></td>
       <td style="text-align:right">✅</td>
    </tr>
    <tr>
      <td>GetWirelessGateway (Pro)  <a href="#misc" title="covered by our integration test suite">✨</a></td>
       <td style="text-align:right">✅</td>
    </tr>
    <tr>
      <td>ListDeviceProfiles (Pro)  <a href="#misc" title="covered by our integration test suite">✨</a></td>
       <td style="text-align:right">✅</td>
    </tr>
    <tr>
      <td>ListWirelessDevices (Pro)  <a href="#misc" title="covered by our integration test suite">✨</a></td>
       <td style="text-align:right">✅</td>
    </tr>
    <tr>
      <td>ListWirelessGateways (Pro)  <a href="#misc" title="covered by our integration test suite">✨</a></td>
       <td style="text-align:right">✅</td>
    </tr>
    <tr>
      <td>UpdateWirelessDevice (Pro) </td>
       <td style="text-align:right">✅</td>
    </tr>
    <tr>
      <td>UpdateWirelessGateway (Pro) </td>
       <td style="text-align:right">✅</td>
    </tr>
  </tbody>
  <tbody>    <tr>
      <td><a data-toggle="collapse" href=".iotwireless-notimplemented">Show missing</a></td>
      <td style="text-align:right"></td>
    </tr>
  </tbody>
  <tbody class="collapse iotwireless-notimplemented">     <tr>
      <td>AssociateAwsAccountWithPartnerAccount</td>
       <td style="text-align:right">-</td>
    </tr>
    <tr>
      <td>AssociateMulticastGroupWithFuotaTask</td>
       <td style="text-align:right">-</td>
    </tr>
    <tr>
      <td>AssociateWirelessDeviceWithFuotaTask</td>
       <td style="text-align:right">-</td>
    </tr>
    <tr>
      <td>AssociateWirelessDeviceWithMulticastGroup</td>
       <td style="text-align:right">-</td>
    </tr>
    <tr>
      <td>AssociateWirelessDeviceWithThing</td>
       <td style="text-align:right">-</td>
    </tr>
    <tr>
      <td>AssociateWirelessGatewayWithCertificate</td>
       <td style="text-align:right">-</td>
    </tr>
    <tr>
      <td>AssociateWirelessGatewayWithThing</td>
       <td style="text-align:right">-</td>
    </tr>
    <tr>
      <td>CancelMulticastGroupSession</td>
       <td style="text-align:right">-</td>
    </tr>
    <tr>
      <td>CreateDestination</td>
       <td style="text-align:right">-</td>
    </tr>
    <tr>
      <td>CreateFuotaTask</td>
       <td style="text-align:right">-</td>
    </tr>
    <tr>
      <td>CreateMulticastGroup</td>
       <td style="text-align:right">-</td>
    </tr>
    <tr>
      <td>CreateNetworkAnalyzerConfiguration</td>
       <td style="text-align:right">-</td>
    </tr>
    <tr>
      <td>CreateServiceProfile</td>
       <td style="text-align:right">-</td>
    </tr>
    <tr>
      <td>CreateWirelessGatewayTask</td>
       <td style="text-align:right">-</td>
    </tr>
    <tr>
      <td>CreateWirelessGatewayTaskDefinition</td>
       <td style="text-align:right">-</td>
    </tr>
    <tr>
      <td>DeleteDestination</td>
       <td style="text-align:right">-</td>
    </tr>
    <tr>
      <td>DeleteFuotaTask</td>
       <td style="text-align:right">-</td>
    </tr>
    <tr>
      <td>DeleteMulticastGroup</td>
       <td style="text-align:right">-</td>
    </tr>
    <tr>
      <td>DeleteNetworkAnalyzerConfiguration</td>
       <td style="text-align:right">-</td>
    </tr>
    <tr>
      <td>DeleteQueuedMessages</td>
       <td style="text-align:right">-</td>
    </tr>
    <tr>
      <td>DeleteServiceProfile</td>
       <td style="text-align:right">-</td>
    </tr>
    <tr>
      <td>DeleteWirelessGatewayTask</td>
       <td style="text-align:right">-</td>
    </tr>
    <tr>
      <td>DeleteWirelessGatewayTaskDefinition</td>
       <td style="text-align:right">-</td>
    </tr>
    <tr>
      <td>DisassociateAwsAccountFromPartnerAccount</td>
       <td style="text-align:right">-</td>
    </tr>
    <tr>
      <td>DisassociateMulticastGroupFromFuotaTask</td>
       <td style="text-align:right">-</td>
    </tr>
    <tr>
      <td>DisassociateWirelessDeviceFromFuotaTask</td>
       <td style="text-align:right">-</td>
    </tr>
    <tr>
      <td>DisassociateWirelessDeviceFromMulticastGroup</td>
       <td style="text-align:right">-</td>
    </tr>
    <tr>
      <td>DisassociateWirelessDeviceFromThing</td>
       <td style="text-align:right">-</td>
    </tr>
    <tr>
      <td>DisassociateWirelessGatewayFromCertificate</td>
       <td style="text-align:right">-</td>
    </tr>
    <tr>
      <td>DisassociateWirelessGatewayFromThing</td>
       <td style="text-align:right">-</td>
    </tr>
    <tr>
      <td>GetDestination</td>
       <td style="text-align:right">-</td>
    </tr>
    <tr>
      <td>GetEventConfigurationByResourceTypes</td>
       <td style="text-align:right">-</td>
    </tr>
    <tr>
      <td>GetFuotaTask</td>
       <td style="text-align:right">-</td>
    </tr>
    <tr>
      <td>GetLogLevelsByResourceTypes</td>
       <td style="text-align:right">-</td>
    </tr>
    <tr>
      <td>GetMulticastGroup</td>
       <td style="text-align:right">-</td>
    </tr>
    <tr>
      <td>GetMulticastGroupSession</td>
       <td style="text-align:right">-</td>
    </tr>
    <tr>
      <td>GetNetworkAnalyzerConfiguration</td>
       <td style="text-align:right">-</td>
    </tr>
    <tr>
      <td>GetPartnerAccount</td>
       <td style="text-align:right">-</td>
    </tr>
    <tr>
      <td>GetPosition</td>
       <td style="text-align:right">-</td>
    </tr>
    <tr>
      <td>GetPositionConfiguration</td>
       <td style="text-align:right">-</td>
    </tr>
    <tr>
      <td>GetResourceEventConfiguration</td>
       <td style="text-align:right">-</td>
    </tr>
    <tr>
      <td>GetResourceLogLevel</td>
       <td style="text-align:right">-</td>
    </tr>
    <tr>
      <td>GetServiceEndpoint</td>
       <td style="text-align:right">-</td>
    </tr>
    <tr>
      <td>GetServiceProfile</td>
       <td style="text-align:right">-</td>
    </tr>
    <tr>
      <td>GetWirelessDeviceStatistics</td>
       <td style="text-align:right">-</td>
    </tr>
    <tr>
      <td>GetWirelessGatewayCertificate</td>
       <td style="text-align:right">-</td>
    </tr>
    <tr>
      <td>GetWirelessGatewayFirmwareInformation</td>
       <td style="text-align:right">-</td>
    </tr>
    <tr>
      <td>GetWirelessGatewayStatistics</td>
       <td style="text-align:right">-</td>
    </tr>
    <tr>
      <td>GetWirelessGatewayTask</td>
       <td style="text-align:right">-</td>
    </tr>
    <tr>
      <td>GetWirelessGatewayTaskDefinition</td>
       <td style="text-align:right">-</td>
    </tr>
    <tr>
      <td>ListDestinations</td>
       <td style="text-align:right">-</td>
    </tr>
    <tr>
      <td>ListEventConfigurations</td>
       <td style="text-align:right">-</td>
    </tr>
    <tr>
      <td>ListFuotaTasks</td>
       <td style="text-align:right">-</td>
    </tr>
    <tr>
      <td>ListMulticastGroups</td>
       <td style="text-align:right">-</td>
    </tr>
    <tr>
      <td>ListMulticastGroupsByFuotaTask</td>
       <td style="text-align:right">-</td>
    </tr>
    <tr>
      <td>ListNetworkAnalyzerConfigurations</td>
       <td style="text-align:right">-</td>
    </tr>
    <tr>
      <td>ListPartnerAccounts</td>
       <td style="text-align:right">-</td>
    </tr>
    <tr>
      <td>ListPositionConfigurations</td>
       <td style="text-align:right">-</td>
    </tr>
    <tr>
      <td>ListQueuedMessages</td>
       <td style="text-align:right">-</td>
    </tr>
    <tr>
      <td>ListServiceProfiles</td>
       <td style="text-align:right">-</td>
    </tr>
    <tr>
      <td>ListTagsForResource</td>
       <td style="text-align:right">-</td>
    </tr>
    <tr>
      <td>ListWirelessGatewayTaskDefinitions</td>
       <td style="text-align:right">-</td>
    </tr>
    <tr>
      <td>PutPositionConfiguration</td>
       <td style="text-align:right">-</td>
    </tr>
    <tr>
      <td>PutResourceLogLevel</td>
       <td style="text-align:right">-</td>
    </tr>
    <tr>
      <td>ResetAllResourceLogLevels</td>
       <td style="text-align:right">-</td>
    </tr>
    <tr>
      <td>ResetResourceLogLevel</td>
       <td style="text-align:right">-</td>
    </tr>
    <tr>
      <td>SendDataToMulticastGroup</td>
       <td style="text-align:right">-</td>
    </tr>
    <tr>
      <td>SendDataToWirelessDevice</td>
       <td style="text-align:right">-</td>
    </tr>
    <tr>
      <td>StartBulkAssociateWirelessDeviceWithMulticastGroup</td>
       <td style="text-align:right">-</td>
    </tr>
    <tr>
      <td>StartBulkDisassociateWirelessDeviceFromMulticastGroup</td>
       <td style="text-align:right">-</td>
    </tr>
    <tr>
      <td>StartFuotaTask</td>
       <td style="text-align:right">-</td>
    </tr>
    <tr>
      <td>StartMulticastGroupSession</td>
       <td style="text-align:right">-</td>
    </tr>
    <tr>
      <td>TagResource</td>
       <td style="text-align:right">-</td>
    </tr>
    <tr>
      <td>TestWirelessDevice</td>
       <td style="text-align:right">-</td>
    </tr>
    <tr>
      <td>UntagResource</td>
       <td style="text-align:right">-</td>
    </tr>
    <tr>
      <td>UpdateDestination</td>
       <td style="text-align:right">-</td>
    </tr>
    <tr>
      <td>UpdateEventConfigurationByResourceTypes</td>
       <td style="text-align:right">-</td>
    </tr>
    <tr>
      <td>UpdateFuotaTask</td>
       <td style="text-align:right">-</td>
    </tr>
    <tr>
      <td>UpdateLogLevelsByResourceTypes</td>
       <td style="text-align:right">-</td>
    </tr>
    <tr>
      <td>UpdateMulticastGroup</td>
       <td style="text-align:right">-</td>
    </tr>
    <tr>
      <td>UpdateNetworkAnalyzerConfiguration</td>
       <td style="text-align:right">-</td>
    </tr>
    <tr>
      <td>UpdatePartnerAccount</td>
       <td style="text-align:right">-</td>
    </tr>
    <tr>
      <td>UpdatePosition</td>
       <td style="text-align:right">-</td>
    </tr>
    <tr>
      <td>UpdateResourceEventConfiguration</td>
       <td style="text-align:right">-</td>
    </tr>
  </tbody>
 </table>


## kafka ##

<table>
  <thead>
    <tr>
      <th>Operation</th>
      <th style="text-align:right">Implemented</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td>CreateCluster (Pro)  <a href="#misc" title="covered by our integration test suite">✨</a></td>
       <td style="text-align:right">✅</td>
    </tr>
    <tr>
      <td>CreateConfiguration (Pro)  <a href="#misc" title="covered by our integration test suite">✨</a></td>
       <td style="text-align:right">✅</td>
    </tr>
    <tr>
      <td>DeleteCluster (Pro)  <a href="#misc" title="covered by our integration test suite">✨</a></td>
       <td style="text-align:right">✅</td>
    </tr>
    <tr>
      <td>DeleteConfiguration (Pro)  <a href="#misc" title="covered by our integration test suite">✨</a></td>
       <td style="text-align:right">✅</td>
    </tr>
    <tr>
      <td>DescribeCluster (Pro)  <a href="#misc" title="covered by our integration test suite">✨</a></td>
       <td style="text-align:right">✅</td>
    </tr>
    <tr>
      <td>DescribeClusterOperation (Pro) </td>
       <td style="text-align:right">✅</td>
    </tr>
    <tr>
      <td>DescribeConfiguration (Pro)  <a href="#misc" title="covered by our integration test suite">✨</a></td>
       <td style="text-align:right">✅</td>
    </tr>
    <tr>
      <td>DescribeConfigurationRevision (Pro)  <a href="#misc" title="covered by our integration test suite">✨</a></td>
       <td style="text-align:right">✅</td>
    </tr>
    <tr>
      <td>GetBootstrapBrokers (Pro)  <a href="#misc" title="covered by our integration test suite">✨</a></td>
       <td style="text-align:right">✅</td>
    </tr>
    <tr>
      <td>ListClusters (Pro)  <a href="#misc" title="covered by our integration test suite">✨</a></td>
       <td style="text-align:right">✅</td>
    </tr>
    <tr>
      <td>ListConfigurationRevisions (Pro)  <a href="#misc" title="covered by our integration test suite">✨</a></td>
       <td style="text-align:right">✅</td>
    </tr>
    <tr>
      <td>ListConfigurations (Pro)  <a href="#misc" title="covered by our integration test suite">✨</a></td>
       <td style="text-align:right">✅</td>
    </tr>
    <tr>
      <td>ListNodes (Pro)  <a href="#misc" title="covered by our integration test suite">✨</a></td>
       <td style="text-align:right">✅</td>
    </tr>
    <tr>
      <td>UpdateClusterConfiguration (Pro) </td>
       <td style="text-align:right">✅</td>
    </tr>
    <tr>
      <td>UpdateClusterKafkaVersion (Pro) </td>
       <td style="text-align:right">✅</td>
    </tr>
    <tr>
      <td>UpdateConfiguration (Pro)  <a href="#misc" title="covered by our integration test suite">✨</a></td>
       <td style="text-align:right">✅</td>
    </tr>
  </tbody>
  <tbody>    <tr>
      <td><a data-toggle="collapse" href=".kafka-notimplemented">Show missing</a></td>
      <td style="text-align:right"></td>
    </tr>
  </tbody>
  <tbody class="collapse kafka-notimplemented">     <tr>
      <td>BatchAssociateScramSecret</td>
       <td style="text-align:right">-</td>
    </tr>
    <tr>
      <td>BatchDisassociateScramSecret</td>
       <td style="text-align:right">-</td>
    </tr>
    <tr>
      <td>CreateClusterV2</td>
       <td style="text-align:right">-</td>
    </tr>
    <tr>
      <td>DescribeClusterV2</td>
       <td style="text-align:right">-</td>
    </tr>
    <tr>
      <td>GetCompatibleKafkaVersions</td>
       <td style="text-align:right">-</td>
    </tr>
    <tr>
      <td>ListClusterOperations</td>
       <td style="text-align:right">-</td>
    </tr>
    <tr>
      <td>ListClustersV2</td>
       <td style="text-align:right">-</td>
    </tr>
    <tr>
      <td>ListKafkaVersions</td>
       <td style="text-align:right">-</td>
    </tr>
    <tr>
      <td>ListScramSecrets</td>
       <td style="text-align:right">-</td>
    </tr>
    <tr>
      <td>ListTagsForResource</td>
       <td style="text-align:right">-</td>
    </tr>
    <tr>
      <td>RebootBroker</td>
       <td style="text-align:right">-</td>
    </tr>
    <tr>
      <td>TagResource</td>
       <td style="text-align:right">-</td>
    </tr>
    <tr>
      <td>UntagResource</td>
       <td style="text-align:right">-</td>
    </tr>
    <tr>
      <td>UpdateBrokerCount</td>
       <td style="text-align:right">-</td>
    </tr>
    <tr>
      <td>UpdateBrokerStorage</td>
       <td style="text-align:right">-</td>
    </tr>
    <tr>
      <td>UpdateBrokerType</td>
       <td style="text-align:right">-</td>
    </tr>
    <tr>
      <td>UpdateConnectivity</td>
       <td style="text-align:right">-</td>
    </tr>
    <tr>
      <td>UpdateMonitoring</td>
       <td style="text-align:right">-</td>
    </tr>
    <tr>
      <td>UpdateSecurity</td>
       <td style="text-align:right">-</td>
    </tr>
  </tbody>
 </table>


## kinesis ##

<table>
  <thead>
    <tr>
      <th>Operation</th>
      <th style="text-align:right">Implemented</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td>AddTagsToStream <a href="#misc" title="covered by our integration test suite">✨</a></td>
       <td style="text-align:right">✅</td>
    </tr>
    <tr>
      <td>CreateStream <a href="#misc" title="covered by our integration test suite">✨</a></td>
       <td style="text-align:right">✅</td>
    </tr>
    <tr>
      <td>DecreaseStreamRetentionPeriod</td>
       <td style="text-align:right">✅</td>
    </tr>
    <tr>
      <td>DeleteStream <a href="#misc" title="covered by our integration test suite">✨</a></td>
       <td style="text-align:right">✅</td>
    </tr>
    <tr>
      <td>DeregisterStreamConsumer <a href="#misc" title="covered by our integration test suite">✨</a></td>
       <td style="text-align:right">✅</td>
    </tr>
    <tr>
      <td>DescribeLimits</td>
       <td style="text-align:right">✅</td>
    </tr>
    <tr>
      <td>DescribeStream <a href="#misc" title="covered by our integration test suite">✨</a></td>
       <td style="text-align:right">✅</td>
    </tr>
    <tr>
      <td>DescribeStreamConsumer <a href="#misc" title="covered by our integration test suite">✨</a></td>
       <td style="text-align:right">✅</td>
    </tr>
    <tr>
      <td>DescribeStreamSummary <a href="#misc" title="covered by our integration test suite">✨</a></td>
       <td style="text-align:right">✅</td>
    </tr>
    <tr>
      <td>DisableEnhancedMonitoring</td>
       <td style="text-align:right">✅</td>
    </tr>
    <tr>
      <td>EnableEnhancedMonitoring</td>
       <td style="text-align:right">✅</td>
    </tr>
    <tr>
      <td>GetRecords <a href="#misc" title="covered by our integration test suite">✨</a></td>
       <td style="text-align:right">✅</td>
    </tr>
    <tr>
      <td>GetShardIterator <a href="#misc" title="covered by our integration test suite">✨</a></td>
       <td style="text-align:right">✅</td>
    </tr>
    <tr>
      <td>IncreaseStreamRetentionPeriod</td>
       <td style="text-align:right">✅</td>
    </tr>
    <tr>
      <td>ListShards <a href="#misc" title="covered by our integration test suite">✨</a></td>
       <td style="text-align:right">✅</td>
    </tr>
    <tr>
      <td>ListStreamConsumers <a href="#misc" title="covered by our integration test suite">✨</a></td>
       <td style="text-align:right">✅</td>
    </tr>
    <tr>
      <td>ListStreams <a href="#misc" title="covered by our integration test suite">✨</a></td>
       <td style="text-align:right">✅</td>
    </tr>
    <tr>
      <td>ListTagsForStream <a href="#misc" title="covered by our integration test suite">✨</a></td>
       <td style="text-align:right">✅</td>
    </tr>
    <tr>
      <td>MergeShards</td>
       <td style="text-align:right">✅</td>
    </tr>
    <tr>
      <td>PutRecord <a href="#misc" title="covered by our integration test suite">✨</a></td>
       <td style="text-align:right">✅</td>
    </tr>
    <tr>
      <td>PutRecords <a href="#misc" title="covered by our integration test suite">✨</a></td>
       <td style="text-align:right">✅</td>
    </tr>
    <tr>
      <td>RegisterStreamConsumer <a href="#misc" title="covered by our integration test suite">✨</a></td>
       <td style="text-align:right">✅</td>
    </tr>
    <tr>
      <td>RemoveTagsFromStream</td>
       <td style="text-align:right">✅</td>
    </tr>
    <tr>
      <td>SplitShard</td>
       <td style="text-align:right">✅</td>
    </tr>
    <tr>
      <td>StartStreamEncryption</td>
       <td style="text-align:right">✅</td>
    </tr>
    <tr>
      <td>StopStreamEncryption</td>
       <td style="text-align:right">✅</td>
    </tr>
    <tr>
      <td>SubscribeToShard <a href="#misc" title="covered by our integration test suite">✨</a></td>
       <td style="text-align:right">✅</td>
    </tr>
    <tr>
      <td>UpdateShardCount</td>
       <td style="text-align:right">✅</td>
    </tr>
    <tr>
      <td>UpdateStreamMode</td>
       <td style="text-align:right">✅</td>
    </tr>
  </tbody>
 </table>


## kinesisanalytics ##

<table>
  <thead>
    <tr>
      <th>Operation</th>
      <th style="text-align:right">Implemented</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td>AddApplicationInputProcessingConfiguration (Pro)  <a href="#misc" title="covered by our integration test suite">✨</a></td>
       <td style="text-align:right">✅</td>
    </tr>
    <tr>
      <td>AddApplicationOutput (Pro)  <a href="#misc" title="covered by our integration test suite">✨</a></td>
       <td style="text-align:right">✅</td>
    </tr>
    <tr>
      <td>CreateApplication (Pro)  <a href="#misc" title="covered by our integration test suite">✨</a></td>
       <td style="text-align:right">✅</td>
    </tr>
    <tr>
      <td>DeleteApplication (Pro)  <a href="#misc" title="covered by our integration test suite">✨</a></td>
       <td style="text-align:right">✅</td>
    </tr>
    <tr>
      <td>DeleteApplicationInputProcessingConfiguration (Pro)  <a href="#misc" title="covered by our integration test suite">✨</a></td>
       <td style="text-align:right">✅</td>
    </tr>
    <tr>
      <td>DescribeApplication (Pro)  <a href="#misc" title="covered by our integration test suite">✨</a></td>
       <td style="text-align:right">✅</td>
    </tr>
    <tr>
      <td>ListApplications (Pro)  <a href="#misc" title="covered by our integration test suite">✨</a></td>
       <td style="text-align:right">✅</td>
    </tr>
    <tr>
      <td>ListTagsForResource (Pro)  <a href="#misc" title="covered by our integration test suite">✨</a></td>
       <td style="text-align:right">✅</td>
    </tr>
    <tr>
      <td>TagResource (Pro)  <a href="#misc" title="covered by our integration test suite">✨</a></td>
       <td style="text-align:right">✅</td>
    </tr>
    <tr>
      <td>UntagResource (Pro)  <a href="#misc" title="covered by our integration test suite">✨</a></td>
       <td style="text-align:right">✅</td>
    </tr>
    <tr>
      <td>UpdateApplication (Pro)  <a href="#misc" title="covered by our integration test suite">✨</a></td>
       <td style="text-align:right">✅</td>
    </tr>
  </tbody>
  <tbody>    <tr>
      <td><a data-toggle="collapse" href=".kinesisanalytics-notimplemented">Show missing</a></td>
      <td style="text-align:right"></td>
    </tr>
  </tbody>
  <tbody class="collapse kinesisanalytics-notimplemented">     <tr>
      <td>AddApplicationCloudWatchLoggingOption</td>
       <td style="text-align:right">-</td>
    </tr>
    <tr>
      <td>AddApplicationInput</td>
       <td style="text-align:right">-</td>
    </tr>
    <tr>
      <td>AddApplicationReferenceDataSource</td>
       <td style="text-align:right">-</td>
    </tr>
    <tr>
      <td>DeleteApplicationCloudWatchLoggingOption</td>
       <td style="text-align:right">-</td>
    </tr>
    <tr>
      <td>DeleteApplicationOutput</td>
       <td style="text-align:right">-</td>
    </tr>
    <tr>
      <td>DeleteApplicationReferenceDataSource</td>
       <td style="text-align:right">-</td>
    </tr>
    <tr>
      <td>DiscoverInputSchema</td>
       <td style="text-align:right">-</td>
    </tr>
    <tr>
      <td>StartApplication</td>
       <td style="text-align:right">-</td>
    </tr>
    <tr>
      <td>StopApplication</td>
       <td style="text-align:right">-</td>
    </tr>
  </tbody>
 </table>


## kinesisanalyticsv2 ##

<table>
  <thead>
    <tr>
      <th>Operation</th>
      <th style="text-align:right">Implemented</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td>AddApplicationInputProcessingConfiguration (Pro)  <a href="#misc" title="covered by our integration test suite">✨</a></td>
       <td style="text-align:right">✅</td>
    </tr>
    <tr>
      <td>AddApplicationOutput (Pro)  <a href="#misc" title="covered by our integration test suite">✨</a></td>
       <td style="text-align:right">✅</td>
    </tr>
    <tr>
      <td>CreateApplication (Pro)  <a href="#misc" title="covered by our integration test suite">✨</a></td>
       <td style="text-align:right">✅</td>
    </tr>
    <tr>
      <td>DeleteApplication (Pro)  <a href="#misc" title="covered by our integration test suite">✨</a></td>
       <td style="text-align:right">✅</td>
    </tr>
    <tr>
      <td>DeleteApplicationInputProcessingConfiguration (Pro)  <a href="#misc" title="covered by our integration test suite">✨</a></td>
       <td style="text-align:right">✅</td>
    </tr>
    <tr>
      <td>DescribeApplication (Pro)  <a href="#misc" title="covered by our integration test suite">✨</a></td>
       <td style="text-align:right">✅</td>
    </tr>
    <tr>
      <td>ListApplications (Pro)  <a href="#misc" title="covered by our integration test suite">✨</a></td>
       <td style="text-align:right">✅</td>
    </tr>
    <tr>
      <td>ListTagsForResource (Pro)  <a href="#misc" title="covered by our integration test suite">✨</a></td>
       <td style="text-align:right">✅</td>
    </tr>
    <tr>
      <td>TagResource (Pro)  <a href="#misc" title="covered by our integration test suite">✨</a></td>
       <td style="text-align:right">✅</td>
    </tr>
    <tr>
      <td>UntagResource (Pro)  <a href="#misc" title="covered by our integration test suite">✨</a></td>
       <td style="text-align:right">✅</td>
    </tr>
    <tr>
      <td>UpdateApplication (Pro)  <a href="#misc" title="covered by our integration test suite">✨</a></td>
       <td style="text-align:right">✅</td>
    </tr>
  </tbody>
  <tbody>    <tr>
      <td><a data-toggle="collapse" href=".kinesisanalyticsv2-notimplemented">Show missing</a></td>
      <td style="text-align:right"></td>
    </tr>
  </tbody>
  <tbody class="collapse kinesisanalyticsv2-notimplemented">     <tr>
      <td>AddApplicationCloudWatchLoggingOption</td>
       <td style="text-align:right">-</td>
    </tr>
    <tr>
      <td>AddApplicationInput</td>
       <td style="text-align:right">-</td>
    </tr>
    <tr>
      <td>AddApplicationReferenceDataSource</td>
       <td style="text-align:right">-</td>
    </tr>
    <tr>
      <td>AddApplicationVpcConfiguration</td>
       <td style="text-align:right">-</td>
    </tr>
    <tr>
      <td>CreateApplicationPresignedUrl</td>
       <td style="text-align:right">-</td>
    </tr>
    <tr>
      <td>CreateApplicationSnapshot</td>
       <td style="text-align:right">-</td>
    </tr>
    <tr>
      <td>DeleteApplicationCloudWatchLoggingOption</td>
       <td style="text-align:right">-</td>
    </tr>
    <tr>
      <td>DeleteApplicationOutput</td>
       <td style="text-align:right">-</td>
    </tr>
    <tr>
      <td>DeleteApplicationReferenceDataSource</td>
       <td style="text-align:right">-</td>
    </tr>
    <tr>
      <td>DeleteApplicationSnapshot</td>
       <td style="text-align:right">-</td>
    </tr>
    <tr>
      <td>DeleteApplicationVpcConfiguration</td>
       <td style="text-align:right">-</td>
    </tr>
    <tr>
      <td>DescribeApplicationSnapshot</td>
       <td style="text-align:right">-</td>
    </tr>
    <tr>
      <td>DescribeApplicationVersion</td>
       <td style="text-align:right">-</td>
    </tr>
    <tr>
      <td>DiscoverInputSchema</td>
       <td style="text-align:right">-</td>
    </tr>
    <tr>
      <td>ListApplicationSnapshots</td>
       <td style="text-align:right">-</td>
    </tr>
    <tr>
      <td>ListApplicationVersions</td>
       <td style="text-align:right">-</td>
    </tr>
    <tr>
      <td>RollbackApplication</td>
       <td style="text-align:right">-</td>
    </tr>
    <tr>
      <td>StartApplication</td>
       <td style="text-align:right">-</td>
    </tr>
    <tr>
      <td>StopApplication</td>
       <td style="text-align:right">-</td>
    </tr>
    <tr>
      <td>UpdateApplicationMaintenanceConfiguration</td>
       <td style="text-align:right">-</td>
    </tr>
  </tbody>
 </table>


## kms ##

<table>
  <thead>
    <tr>
      <th>Operation</th>
      <th style="text-align:right">Implemented</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td>CancelKeyDeletion <a href="#misc" title="covered by our integration test suite">✨</a></td>
       <td style="text-align:right">✅</td>
    </tr>
    <tr>
      <td>CreateAlias <a href="#misc" title="covered by our integration test suite">✨</a></td>
       <td style="text-align:right">✅</td>
    </tr>
    <tr>
      <td>CreateGrant <a href="#misc" title="covered by our integration test suite">✨</a></td>
       <td style="text-align:right">✅</td>
    </tr>
    <tr>
      <td>CreateKey <a href="#misc" title="covered by our integration test suite">✨</a></td>
       <td style="text-align:right">✅</td>
    </tr>
    <tr>
      <td>Decrypt <a href="#misc" title="covered by our integration test suite">✨</a></td>
       <td style="text-align:right">✅</td>
    </tr>
    <tr>
      <td>DeleteAlias <a href="#misc" title="covered by our integration test suite">✨</a></td>
       <td style="text-align:right">✅</td>
    </tr>
    <tr>
      <td>DescribeKey <a href="#misc" title="covered by our integration test suite">✨</a></td>
       <td style="text-align:right">✅</td>
    </tr>
    <tr>
      <td>DisableKey <a href="#misc" title="covered by our integration test suite">✨</a></td>
       <td style="text-align:right">✅</td>
    </tr>
    <tr>
      <td>DisableKeyRotation <a href="#misc" title="covered by our integration test suite">✨</a></td>
       <td style="text-align:right">✅</td>
    </tr>
    <tr>
      <td>EnableKey <a href="#misc" title="covered by our integration test suite">✨</a></td>
       <td style="text-align:right">✅</td>
    </tr>
    <tr>
      <td>EnableKeyRotation <a href="#misc" title="covered by our integration test suite">✨</a></td>
       <td style="text-align:right">✅</td>
    </tr>
    <tr>
      <td>Encrypt <a href="#misc" title="covered by our integration test suite">✨</a></td>
       <td style="text-align:right">✅</td>
    </tr>
    <tr>
      <td>GenerateDataKey <a href="#misc" title="covered by our integration test suite">✨</a></td>
       <td style="text-align:right">✅</td>
    </tr>
    <tr>
      <td>GenerateDataKeyPair <a href="#misc" title="covered by our integration test suite">✨</a></td>
       <td style="text-align:right">✅</td>
    </tr>
    <tr>
      <td>GenerateDataKeyPairWithoutPlaintext <a href="#misc" title="covered by our integration test suite">✨</a></td>
       <td style="text-align:right">✅</td>
    </tr>
    <tr>
      <td>GenerateDataKeyWithoutPlaintext <a href="#misc" title="covered by our integration test suite">✨</a></td>
       <td style="text-align:right">✅</td>
    </tr>
    <tr>
      <td>GenerateRandom <a href="#misc" title="covered by our integration test suite">✨</a></td>
       <td style="text-align:right">✅</td>
    </tr>
    <tr>
      <td>GetKeyPolicy <a href="#misc" title="covered by our integration test suite">✨</a></td>
       <td style="text-align:right">✅</td>
    </tr>
    <tr>
      <td>GetKeyRotationStatus <a href="#misc" title="covered by our integration test suite">✨</a></td>
       <td style="text-align:right">✅</td>
    </tr>
    <tr>
      <td>GetParametersForImport <a href="#misc" title="covered by our integration test suite">✨</a></td>
       <td style="text-align:right">✅</td>
    </tr>
    <tr>
      <td>GetPublicKey <a href="#misc" title="covered by our integration test suite">✨</a></td>
       <td style="text-align:right">✅</td>
    </tr>
    <tr>
      <td>ImportKeyMaterial <a href="#misc" title="covered by our integration test suite">✨</a></td>
       <td style="text-align:right">✅</td>
    </tr>
    <tr>
      <td>ListAliases <a href="#misc" title="covered by our integration test suite">✨</a></td>
       <td style="text-align:right">✅</td>
    </tr>
    <tr>
      <td>ListGrants <a href="#misc" title="covered by our integration test suite">✨</a></td>
       <td style="text-align:right">✅</td>
    </tr>
    <tr>
      <td>ListKeyPolicies <a href="#misc" title="covered by our integration test suite">✨</a></td>
       <td style="text-align:right">✅</td>
    </tr>
    <tr>
      <td>ListKeys <a href="#misc" title="covered by our integration test suite">✨</a></td>
       <td style="text-align:right">✅</td>
    </tr>
    <tr>
      <td>ListResourceTags <a href="#misc" title="covered by our integration test suite">✨</a></td>
       <td style="text-align:right">✅</td>
    </tr>
    <tr>
      <td>ListRetirableGrants <a href="#misc" title="covered by our integration test suite">✨</a></td>
       <td style="text-align:right">✅</td>
    </tr>
    <tr>
      <td>PutKeyPolicy <a href="#misc" title="covered by our integration test suite">✨</a></td>
       <td style="text-align:right">✅</td>
    </tr>
    <tr>
      <td>ReplicateKey <a href="#misc" title="covered by our integration test suite">✨</a></td>
       <td style="text-align:right">✅</td>
    </tr>
    <tr>
      <td>RetireGrant <a href="#misc" title="covered by our integration test suite">✨</a></td>
       <td style="text-align:right">✅</td>
    </tr>
    <tr>
      <td>RevokeGrant <a href="#misc" title="covered by our integration test suite">✨</a></td>
       <td style="text-align:right">✅</td>
    </tr>
    <tr>
      <td>ScheduleKeyDeletion <a href="#misc" title="covered by our integration test suite">✨</a></td>
       <td style="text-align:right">✅</td>
    </tr>
    <tr>
      <td>Sign <a href="#misc" title="covered by our integration test suite">✨</a></td>
       <td style="text-align:right">✅</td>
    </tr>
    <tr>
      <td>TagResource <a href="#misc" title="covered by our integration test suite">✨</a></td>
       <td style="text-align:right">✅</td>
    </tr>
    <tr>
      <td>UntagResource <a href="#misc" title="covered by our integration test suite">✨</a></td>
       <td style="text-align:right">✅</td>
    </tr>
    <tr>
      <td>UpdateAlias <a href="#misc" title="covered by our integration test suite">✨</a></td>
       <td style="text-align:right">✅</td>
    </tr>
    <tr>
      <td>UpdateKeyDescription <a href="#misc" title="covered by our integration test suite">✨</a></td>
       <td style="text-align:right">✅</td>
    </tr>
    <tr>
      <td>Verify <a href="#misc" title="covered by our integration test suite">✨</a></td>
       <td style="text-align:right">✅</td>
    </tr>
  </tbody>
  <tbody>    <tr>
      <td><a data-toggle="collapse" href=".kms-notimplemented">Show missing</a></td>
      <td style="text-align:right"></td>
    </tr>
  </tbody>
  <tbody class="collapse kms-notimplemented">     <tr>
      <td>ConnectCustomKeyStore</td>
       <td style="text-align:right">-</td>
    </tr>
    <tr>
      <td>CreateCustomKeyStore</td>
       <td style="text-align:right">-</td>
    </tr>
    <tr>
      <td>DeleteCustomKeyStore</td>
       <td style="text-align:right">-</td>
    </tr>
    <tr>
      <td>DeleteImportedKeyMaterial</td>
       <td style="text-align:right">-</td>
    </tr>
    <tr>
      <td>DescribeCustomKeyStores</td>
       <td style="text-align:right">-</td>
    </tr>
    <tr>
      <td>DisconnectCustomKeyStore</td>
       <td style="text-align:right">-</td>
    </tr>
    <tr>
      <td>GenerateMac</td>
       <td style="text-align:right">-</td>
    </tr>
    <tr>
      <td>ReEncrypt</td>
       <td style="text-align:right">-</td>
    </tr>
    <tr>
      <td>UpdateCustomKeyStore</td>
       <td style="text-align:right">-</td>
    </tr>
    <tr>
      <td>UpdatePrimaryRegion</td>
       <td style="text-align:right">-</td>
    </tr>
    <tr>
      <td>VerifyMac</td>
       <td style="text-align:right">-</td>
    </tr>
  </tbody>
 </table>


## lakeformation ##

<table>
  <thead>
    <tr>
      <th>Operation</th>
      <th style="text-align:right">Implemented</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td>DeregisterResource (Pro) </td>
       <td style="text-align:right">✅</td>
    </tr>
    <tr>
      <td>DescribeResource (Pro) </td>
       <td style="text-align:right">✅</td>
    </tr>
    <tr>
      <td>GetDataLakeSettings (Pro) </td>
       <td style="text-align:right">✅</td>
    </tr>
    <tr>
      <td>GrantPermissions (Pro)  <a href="#misc" title="covered by our integration test suite">✨</a></td>
       <td style="text-align:right">✅</td>
    </tr>
    <tr>
      <td>ListPermissions (Pro)  <a href="#misc" title="covered by our integration test suite">✨</a></td>
       <td style="text-align:right">✅</td>
    </tr>
    <tr>
      <td>ListResources (Pro) </td>
       <td style="text-align:right">✅</td>
    </tr>
    <tr>
      <td>PutDataLakeSettings (Pro) </td>
       <td style="text-align:right">✅</td>
    </tr>
    <tr>
      <td>RegisterResource (Pro) </td>
       <td style="text-align:right">✅</td>
    </tr>
    <tr>
      <td>RevokePermissions (Pro) </td>
       <td style="text-align:right">✅</td>
    </tr>
  </tbody>
  <tbody>    <tr>
      <td><a data-toggle="collapse" href=".lakeformation-notimplemented">Show missing</a></td>
      <td style="text-align:right"></td>
    </tr>
  </tbody>
  <tbody class="collapse lakeformation-notimplemented">     <tr>
      <td>AddLFTagsToResource</td>
       <td style="text-align:right">-</td>
    </tr>
    <tr>
      <td>AssumeDecoratedRoleWithSAML</td>
       <td style="text-align:right">-</td>
    </tr>
    <tr>
      <td>BatchGrantPermissions</td>
       <td style="text-align:right">-</td>
    </tr>
    <tr>
      <td>BatchRevokePermissions</td>
       <td style="text-align:right">-</td>
    </tr>
    <tr>
      <td>CancelTransaction</td>
       <td style="text-align:right">-</td>
    </tr>
    <tr>
      <td>CommitTransaction</td>
       <td style="text-align:right">-</td>
    </tr>
    <tr>
      <td>CreateDataCellsFilter</td>
       <td style="text-align:right">-</td>
    </tr>
    <tr>
      <td>CreateLFTag</td>
       <td style="text-align:right">-</td>
    </tr>
    <tr>
      <td>DeleteDataCellsFilter</td>
       <td style="text-align:right">-</td>
    </tr>
    <tr>
      <td>DeleteLFTag</td>
       <td style="text-align:right">-</td>
    </tr>
    <tr>
      <td>DeleteObjectsOnCancel</td>
       <td style="text-align:right">-</td>
    </tr>
    <tr>
      <td>DescribeTransaction</td>
       <td style="text-align:right">-</td>
    </tr>
    <tr>
      <td>ExtendTransaction</td>
       <td style="text-align:right">-</td>
    </tr>
    <tr>
      <td>GetEffectivePermissionsForPath</td>
       <td style="text-align:right">-</td>
    </tr>
    <tr>
      <td>GetLFTag</td>
       <td style="text-align:right">-</td>
    </tr>
    <tr>
      <td>GetQueryState</td>
       <td style="text-align:right">-</td>
    </tr>
    <tr>
      <td>GetQueryStatistics</td>
       <td style="text-align:right">-</td>
    </tr>
    <tr>
      <td>GetResourceLFTags</td>
       <td style="text-align:right">-</td>
    </tr>
    <tr>
      <td>GetTableObjects</td>
       <td style="text-align:right">-</td>
    </tr>
    <tr>
      <td>GetTemporaryGluePartitionCredentials</td>
       <td style="text-align:right">-</td>
    </tr>
    <tr>
      <td>GetTemporaryGlueTableCredentials</td>
       <td style="text-align:right">-</td>
    </tr>
    <tr>
      <td>GetWorkUnitResults</td>
       <td style="text-align:right">-</td>
    </tr>
    <tr>
      <td>GetWorkUnits</td>
       <td style="text-align:right">-</td>
    </tr>
    <tr>
      <td>ListDataCellsFilter</td>
       <td style="text-align:right">-</td>
    </tr>
    <tr>
      <td>ListLFTags</td>
       <td style="text-align:right">-</td>
    </tr>
    <tr>
      <td>ListTableStorageOptimizers</td>
       <td style="text-align:right">-</td>
    </tr>
    <tr>
      <td>ListTransactions</td>
       <td style="text-align:right">-</td>
    </tr>
    <tr>
      <td>RemoveLFTagsFromResource</td>
       <td style="text-align:right">-</td>
    </tr>
    <tr>
      <td>SearchDatabasesByLFTags</td>
       <td style="text-align:right">-</td>
    </tr>
    <tr>
      <td>SearchTablesByLFTags</td>
       <td style="text-align:right">-</td>
    </tr>
    <tr>
      <td>StartQueryPlanning</td>
       <td style="text-align:right">-</td>
    </tr>
    <tr>
      <td>StartTransaction</td>
       <td style="text-align:right">-</td>
    </tr>
    <tr>
      <td>UpdateLFTag</td>
       <td style="text-align:right">-</td>
    </tr>
    <tr>
      <td>UpdateResource</td>
       <td style="text-align:right">-</td>
    </tr>
    <tr>
      <td>UpdateTableObjects</td>
       <td style="text-align:right">-</td>
    </tr>
    <tr>
      <td>UpdateTableStorageOptimizer</td>
       <td style="text-align:right">-</td>
    </tr>
  </tbody>
 </table>


## lambda ##

<table>
  <thead>
    <tr>
      <th>Operation</th>
      <th style="text-align:right">Implemented</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td>AddLayerVersionPermission (Pro) </td>
       <td style="text-align:right">✅</td>
    </tr>
    <tr>
      <td>AddPermission <a href="#misc" title="covered by our integration test suite">✨</a></td>
       <td style="text-align:right">✅</td>
    </tr>
    <tr>
      <td>CreateAlias <a href="#misc" title="covered by our integration test suite">✨</a></td>
       <td style="text-align:right">✅</td>
    </tr>
    <tr>
      <td>CreateCodeSigningConfig <a href="#misc" title="covered by our integration test suite">✨</a></td>
       <td style="text-align:right">✅</td>
    </tr>
    <tr>
      <td>CreateEventSourceMapping <a href="#misc" title="covered by our integration test suite">✨</a></td>
       <td style="text-align:right">✅</td>
    </tr>
    <tr>
      <td>CreateFunction <a href="#misc" title="covered by our integration test suite">✨</a></td>
       <td style="text-align:right">✅</td>
    </tr>
    <tr>
      <td>CreateFunctionUrlConfig <a href="#misc" title="covered by our integration test suite">✨</a></td>
       <td style="text-align:right">✅</td>
    </tr>
    <tr>
      <td>DeleteAlias <a href="#misc" title="covered by our integration test suite">✨</a></td>
       <td style="text-align:right">✅</td>
    </tr>
    <tr>
      <td>DeleteCodeSigningConfig <a href="#misc" title="covered by our integration test suite">✨</a></td>
       <td style="text-align:right">✅</td>
    </tr>
    <tr>
      <td>DeleteEventSourceMapping <a href="#misc" title="covered by our integration test suite">✨</a></td>
       <td style="text-align:right">✅</td>
    </tr>
    <tr>
      <td>DeleteFunction <a href="#misc" title="covered by our integration test suite">✨</a></td>
       <td style="text-align:right">✅</td>
    </tr>
    <tr>
      <td>DeleteFunctionCodeSigningConfig</td>
       <td style="text-align:right">✅</td>
    </tr>
    <tr>
      <td>DeleteFunctionConcurrency</td>
       <td style="text-align:right">✅</td>
    </tr>
    <tr>
      <td>DeleteFunctionEventInvokeConfig <a href="#misc" title="covered by our integration test suite">✨</a></td>
       <td style="text-align:right">✅</td>
    </tr>
    <tr>
      <td>DeleteFunctionUrlConfig <a href="#misc" title="covered by our integration test suite">✨</a></td>
       <td style="text-align:right">✅</td>
    </tr>
    <tr>
      <td>DeleteLayerVersion (Pro)  <a href="#misc" title="covered by our integration test suite">✨</a></td>
       <td style="text-align:right">✅</td>
    </tr>
    <tr>
      <td>GetAlias <a href="#misc" title="covered by our integration test suite">✨</a></td>
       <td style="text-align:right">✅</td>
    </tr>
    <tr>
      <td>GetCodeSigningConfig <a href="#misc" title="covered by our integration test suite">✨</a></td>
       <td style="text-align:right">✅</td>
    </tr>
    <tr>
      <td>GetEventSourceMapping <a href="#misc" title="covered by our integration test suite">✨</a></td>
       <td style="text-align:right">✅</td>
    </tr>
    <tr>
      <td>GetFunction <a href="#misc" title="covered by our integration test suite">✨</a></td>
       <td style="text-align:right">✅</td>
    </tr>
    <tr>
      <td>GetFunctionCodeSigningConfig</td>
       <td style="text-align:right">✅</td>
    </tr>
    <tr>
      <td>GetFunctionConcurrency</td>
       <td style="text-align:right">✅</td>
    </tr>
    <tr>
      <td>GetFunctionConfiguration <a href="#misc" title="covered by our integration test suite">✨</a></td>
       <td style="text-align:right">✅</td>
    </tr>
    <tr>
      <td>GetFunctionEventInvokeConfig <a href="#misc" title="covered by our integration test suite">✨</a></td>
       <td style="text-align:right">✅</td>
    </tr>
    <tr>
      <td>GetFunctionUrlConfig <a href="#misc" title="covered by our integration test suite">✨</a></td>
       <td style="text-align:right">✅</td>
    </tr>
    <tr>
      <td>GetLayerVersion (Pro)  <a href="#misc" title="covered by our integration test suite">✨</a></td>
       <td style="text-align:right">✅</td>
    </tr>
    <tr>
      <td>GetLayerVersionByArn (Pro) </td>
       <td style="text-align:right">✅</td>
    </tr>
    <tr>
      <td>GetLayerVersionPolicy (Pro) </td>
       <td style="text-align:right">✅</td>
    </tr>
    <tr>
      <td>GetPolicy <a href="#misc" title="covered by our integration test suite">✨</a></td>
       <td style="text-align:right">✅</td>
    </tr>
    <tr>
      <td>Invoke <a href="#misc" title="covered by our integration test suite">✨</a></td>
       <td style="text-align:right">✅</td>
    </tr>
    <tr>
      <td>ListAliases <a href="#misc" title="covered by our integration test suite">✨</a></td>
       <td style="text-align:right">✅</td>
    </tr>
    <tr>
      <td>ListCodeSigningConfigs</td>
       <td style="text-align:right">✅</td>
    </tr>
    <tr>
      <td>ListEventSourceMappings <a href="#misc" title="covered by our integration test suite">✨</a></td>
       <td style="text-align:right">✅</td>
    </tr>
    <tr>
      <td>ListFunctions <a href="#misc" title="covered by our integration test suite">✨</a></td>
       <td style="text-align:right">✅</td>
    </tr>
    <tr>
      <td>ListLayerVersions (Pro)  <a href="#misc" title="covered by our integration test suite">✨</a></td>
       <td style="text-align:right">✅</td>
    </tr>
    <tr>
      <td>ListLayers (Pro)  <a href="#misc" title="covered by our integration test suite">✨</a></td>
       <td style="text-align:right">✅</td>
    </tr>
    <tr>
      <td>ListTags</td>
       <td style="text-align:right">✅</td>
    </tr>
    <tr>
      <td>ListVersionsByFunction <a href="#misc" title="covered by our integration test suite">✨</a></td>
       <td style="text-align:right">✅</td>
    </tr>
    <tr>
      <td>PublishLayerVersion (Pro)  <a href="#misc" title="covered by our integration test suite">✨</a></td>
       <td style="text-align:right">✅</td>
    </tr>
    <tr>
      <td>PublishVersion <a href="#misc" title="covered by our integration test suite">✨</a></td>
       <td style="text-align:right">✅</td>
    </tr>
    <tr>
      <td>PutFunctionCodeSigningConfig</td>
       <td style="text-align:right">✅</td>
    </tr>
    <tr>
      <td>PutFunctionConcurrency</td>
       <td style="text-align:right">✅</td>
    </tr>
    <tr>
      <td>PutFunctionEventInvokeConfig <a href="#misc" title="covered by our integration test suite">✨</a></td>
       <td style="text-align:right">✅</td>
    </tr>
    <tr>
      <td>RemovePermission <a href="#misc" title="covered by our integration test suite">✨</a></td>
       <td style="text-align:right">✅</td>
    </tr>
    <tr>
      <td>TagResource</td>
       <td style="text-align:right">✅</td>
    </tr>
    <tr>
      <td>UntagResource</td>
       <td style="text-align:right">✅</td>
    </tr>
    <tr>
      <td>UpdateAlias</td>
       <td style="text-align:right">✅</td>
    </tr>
    <tr>
      <td>UpdateCodeSigningConfig</td>
       <td style="text-align:right">✅</td>
    </tr>
    <tr>
      <td>UpdateEventSourceMapping <a href="#misc" title="covered by our integration test suite">✨</a></td>
       <td style="text-align:right">✅</td>
    </tr>
    <tr>
      <td>UpdateFunctionCode <a href="#misc" title="covered by our integration test suite">✨</a></td>
       <td style="text-align:right">✅</td>
    </tr>
    <tr>
      <td>UpdateFunctionConfiguration <a href="#misc" title="covered by our integration test suite">✨</a></td>
       <td style="text-align:right">✅</td>
    </tr>
    <tr>
      <td>UpdateFunctionEventInvokeConfig</td>
       <td style="text-align:right">✅</td>
    </tr>
    <tr>
      <td>UpdateFunctionUrlConfig <a href="#misc" title="covered by our integration test suite">✨</a></td>
       <td style="text-align:right">✅</td>
    </tr>
  </tbody>
  <tbody>    <tr>
      <td><a data-toggle="collapse" href=".lambda-notimplemented">Show missing</a></td>
      <td style="text-align:right"></td>
    </tr>
  </tbody>
  <tbody class="collapse lambda-notimplemented">     <tr>
      <td>DeleteProvisionedConcurrencyConfig</td>
       <td style="text-align:right">-</td>
    </tr>
    <tr>
      <td>GetAccountSettings</td>
       <td style="text-align:right">-</td>
    </tr>
    <tr>
      <td>GetProvisionedConcurrencyConfig</td>
       <td style="text-align:right">-</td>
    </tr>
    <tr>
      <td>InvokeAsync</td>
       <td style="text-align:right">-</td>
    </tr>
    <tr>
      <td>ListFunctionEventInvokeConfigs</td>
       <td style="text-align:right">-</td>
    </tr>
    <tr>
      <td>ListFunctionUrlConfigs</td>
       <td style="text-align:right">-</td>
    </tr>
    <tr>
      <td>ListFunctionsByCodeSigningConfig</td>
       <td style="text-align:right">-</td>
    </tr>
    <tr>
      <td>ListProvisionedConcurrencyConfigs</td>
       <td style="text-align:right">-</td>
    </tr>
    <tr>
      <td>PutProvisionedConcurrencyConfig</td>
       <td style="text-align:right">-</td>
    </tr>
    <tr>
      <td>RemoveLayerVersionPermission</td>
       <td style="text-align:right">-</td>
    </tr>
  </tbody>
 </table>


## logs ##

<table>
  <thead>
    <tr>
      <th>Operation</th>
      <th style="text-align:right">Implemented</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td>CreateExportTask</td>
       <td style="text-align:right">✅</td>
    </tr>
    <tr>
      <td>CreateLogGroup <a href="#misc" title="covered by our integration test suite">✨</a></td>
       <td style="text-align:right">✅</td>
    </tr>
    <tr>
      <td>CreateLogStream <a href="#misc" title="covered by our integration test suite">✨</a></td>
       <td style="text-align:right">✅</td>
    </tr>
    <tr>
      <td>DeleteLogGroup <a href="#misc" title="covered by our integration test suite">✨</a></td>
       <td style="text-align:right">✅</td>
    </tr>
    <tr>
      <td>DeleteLogStream <a href="#misc" title="covered by our integration test suite">✨</a></td>
       <td style="text-align:right">✅</td>
    </tr>
    <tr>
      <td>DeleteMetricFilter <a href="#misc" title="covered by our integration test suite">✨</a></td>
       <td style="text-align:right">✅</td>
    </tr>
    <tr>
      <td>DeleteResourcePolicy</td>
       <td style="text-align:right">✅</td>
    </tr>
    <tr>
      <td>DeleteRetentionPolicy</td>
       <td style="text-align:right">✅</td>
    </tr>
    <tr>
      <td>DeleteSubscriptionFilter <a href="#misc" title="covered by our integration test suite">✨</a></td>
       <td style="text-align:right">✅</td>
    </tr>
    <tr>
      <td>DescribeLogGroups <a href="#misc" title="covered by our integration test suite">✨</a></td>
       <td style="text-align:right">✅</td>
    </tr>
    <tr>
      <td>DescribeLogStreams <a href="#misc" title="covered by our integration test suite">✨</a></td>
       <td style="text-align:right">✅</td>
    </tr>
    <tr>
      <td>DescribeMetricFilters <a href="#misc" title="covered by our integration test suite">✨</a></td>
       <td style="text-align:right">✅</td>
    </tr>
    <tr>
      <td>DescribeResourcePolicies</td>
       <td style="text-align:right">✅</td>
    </tr>
    <tr>
      <td>DescribeSubscriptionFilters <a href="#misc" title="covered by our integration test suite">✨</a></td>
       <td style="text-align:right">✅</td>
    </tr>
    <tr>
      <td>FilterLogEvents <a href="#misc" title="covered by our integration test suite">✨</a></td>
       <td style="text-align:right">✅</td>
    </tr>
    <tr>
      <td>GetLogEvents <a href="#misc" title="covered by our integration test suite">✨</a></td>
       <td style="text-align:right">✅</td>
    </tr>
    <tr>
      <td>ListTagsLogGroup <a href="#misc" title="covered by our integration test suite">✨</a></td>
       <td style="text-align:right">✅</td>
    </tr>
    <tr>
      <td>PutLogEvents <a href="#misc" title="covered by our integration test suite">✨</a></td>
       <td style="text-align:right">✅</td>
    </tr>
    <tr>
      <td>PutMetricFilter <a href="#misc" title="covered by our integration test suite">✨</a></td>
       <td style="text-align:right">✅</td>
    </tr>
    <tr>
      <td>PutResourcePolicy <a href="#misc" title="covered by our integration test suite">✨</a></td>
       <td style="text-align:right">✅</td>
    </tr>
    <tr>
      <td>PutRetentionPolicy</td>
       <td style="text-align:right">✅</td>
    </tr>
    <tr>
      <td>PutSubscriptionFilter <a href="#misc" title="covered by our integration test suite">✨</a></td>
       <td style="text-align:right">✅</td>
    </tr>
    <tr>
      <td>StartQuery</td>
       <td style="text-align:right">✅</td>
    </tr>
    <tr>
      <td>TagLogGroup</td>
       <td style="text-align:right">✅</td>
    </tr>
    <tr>
      <td>UntagLogGroup</td>
       <td style="text-align:right">✅</td>
    </tr>
  </tbody>
  <tbody>    <tr>
      <td><a data-toggle="collapse" href=".logs-notimplemented">Show missing</a></td>
      <td style="text-align:right"></td>
    </tr>
  </tbody>
  <tbody class="collapse logs-notimplemented">     <tr>
      <td>AssociateKmsKey</td>
       <td style="text-align:right">-</td>
    </tr>
    <tr>
      <td>CancelExportTask</td>
       <td style="text-align:right">-</td>
    </tr>
    <tr>
      <td>DeleteDestination</td>
       <td style="text-align:right">-</td>
    </tr>
    <tr>
      <td>DeleteQueryDefinition</td>
       <td style="text-align:right">-</td>
    </tr>
    <tr>
      <td>DescribeDestinations</td>
       <td style="text-align:right">-</td>
    </tr>
    <tr>
      <td>DescribeExportTasks</td>
       <td style="text-align:right">-</td>
    </tr>
    <tr>
      <td>DescribeQueries</td>
       <td style="text-align:right">-</td>
    </tr>
    <tr>
      <td>DescribeQueryDefinitions</td>
       <td style="text-align:right">-</td>
    </tr>
    <tr>
      <td>DisassociateKmsKey</td>
       <td style="text-align:right">-</td>
    </tr>
    <tr>
      <td>GetLogGroupFields</td>
       <td style="text-align:right">-</td>
    </tr>
    <tr>
      <td>GetLogRecord</td>
       <td style="text-align:right">-</td>
    </tr>
    <tr>
      <td>GetQueryResults</td>
       <td style="text-align:right">-</td>
    </tr>
    <tr>
      <td>PutDestination</td>
       <td style="text-align:right">-</td>
    </tr>
    <tr>
      <td>PutDestinationPolicy</td>
       <td style="text-align:right">-</td>
    </tr>
    <tr>
      <td>PutQueryDefinition</td>
       <td style="text-align:right">-</td>
    </tr>
    <tr>
      <td>StopQuery</td>
       <td style="text-align:right">-</td>
    </tr>
    <tr>
      <td>TestMetricFilter</td>
       <td style="text-align:right">-</td>
    </tr>
  </tbody>
 </table>


## mediastore ##

<table>
  <thead>
    <tr>
      <th>Operation</th>
      <th style="text-align:right">Implemented</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td>CreateContainer (Pro)  <a href="#misc" title="covered by our integration test suite">✨</a></td>
       <td style="text-align:right">✅</td>
    </tr>
    <tr>
      <td>DeleteContainer (Pro)  <a href="#misc" title="covered by our integration test suite">✨</a></td>
       <td style="text-align:right">✅</td>
    </tr>
    <tr>
      <td>DescribeContainer (Pro)  <a href="#misc" title="covered by our integration test suite">✨</a></td>
       <td style="text-align:right">✅</td>
    </tr>
    <tr>
      <td>ListContainers (Pro)  <a href="#misc" title="covered by our integration test suite">✨</a></td>
       <td style="text-align:right">✅</td>
    </tr>
  </tbody>
  <tbody>    <tr>
      <td><a data-toggle="collapse" href=".mediastore-notimplemented">Show missing</a></td>
      <td style="text-align:right"></td>
    </tr>
  </tbody>
  <tbody class="collapse mediastore-notimplemented">     <tr>
      <td>DeleteContainerPolicy</td>
       <td style="text-align:right">-</td>
    </tr>
    <tr>
      <td>DeleteCorsPolicy</td>
       <td style="text-align:right">-</td>
    </tr>
    <tr>
      <td>DeleteLifecyclePolicy</td>
       <td style="text-align:right">-</td>
    </tr>
    <tr>
      <td>DeleteMetricPolicy</td>
       <td style="text-align:right">-</td>
    </tr>
    <tr>
      <td>GetContainerPolicy</td>
       <td style="text-align:right">-</td>
    </tr>
    <tr>
      <td>GetCorsPolicy</td>
       <td style="text-align:right">-</td>
    </tr>
    <tr>
      <td>GetLifecyclePolicy</td>
       <td style="text-align:right">-</td>
    </tr>
    <tr>
      <td>GetMetricPolicy</td>
       <td style="text-align:right">-</td>
    </tr>
    <tr>
      <td>ListTagsForResource</td>
       <td style="text-align:right">-</td>
    </tr>
    <tr>
      <td>PutContainerPolicy</td>
       <td style="text-align:right">-</td>
    </tr>
    <tr>
      <td>PutCorsPolicy</td>
       <td style="text-align:right">-</td>
    </tr>
    <tr>
      <td>PutLifecyclePolicy</td>
       <td style="text-align:right">-</td>
    </tr>
    <tr>
      <td>PutMetricPolicy</td>
       <td style="text-align:right">-</td>
    </tr>
    <tr>
      <td>StartAccessLogging</td>
       <td style="text-align:right">-</td>
    </tr>
    <tr>
      <td>StopAccessLogging</td>
       <td style="text-align:right">-</td>
    </tr>
    <tr>
      <td>TagResource</td>
       <td style="text-align:right">-</td>
    </tr>
    <tr>
      <td>UntagResource</td>
       <td style="text-align:right">-</td>
    </tr>
  </tbody>
 </table>


## mediastore-data ##

<table>
  <thead>
    <tr>
      <th>Operation</th>
      <th style="text-align:right">Implemented</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td>DeleteObject (Pro)  <a href="#misc" title="covered by our integration test suite">✨</a></td>
       <td style="text-align:right">✅</td>
    </tr>
    <tr>
      <td>DescribeObject (Pro)  <a href="#misc" title="covered by our integration test suite">✨</a></td>
       <td style="text-align:right">✅</td>
    </tr>
    <tr>
      <td>GetObject (Pro)  <a href="#misc" title="covered by our integration test suite">✨</a></td>
       <td style="text-align:right">✅</td>
    </tr>
    <tr>
      <td>PutObject (Pro)  <a href="#misc" title="covered by our integration test suite">✨</a></td>
       <td style="text-align:right">✅</td>
    </tr>
  </tbody>
  <tbody>    <tr>
      <td><a data-toggle="collapse" href=".mediastore-data-notimplemented">Show missing</a></td>
      <td style="text-align:right"></td>
    </tr>
  </tbody>
  <tbody class="collapse mediastore-data-notimplemented">     <tr>
      <td>ListItems</td>
       <td style="text-align:right">-</td>
    </tr>
  </tbody>
 </table>


## mq ##

<table>
  <thead>
    <tr>
      <th>Operation</th>
      <th style="text-align:right">Implemented</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td>CreateBroker (Pro)  <a href="#misc" title="covered by our integration test suite">✨</a></td>
       <td style="text-align:right">✅</td>
    </tr>
    <tr>
      <td>CreateConfiguration (Pro)  <a href="#misc" title="covered by our integration test suite">✨</a></td>
       <td style="text-align:right">✅</td>
    </tr>
    <tr>
      <td>CreateTags (Pro)  <a href="#misc" title="covered by our integration test suite">✨</a></td>
       <td style="text-align:right">✅</td>
    </tr>
    <tr>
      <td>CreateUser (Pro) </td>
       <td style="text-align:right">✅</td>
    </tr>
    <tr>
      <td>DeleteBroker (Pro)  <a href="#misc" title="covered by our integration test suite">✨</a></td>
       <td style="text-align:right">✅</td>
    </tr>
    <tr>
      <td>DeleteTags (Pro)  <a href="#misc" title="covered by our integration test suite">✨</a></td>
       <td style="text-align:right">✅</td>
    </tr>
    <tr>
      <td>DeleteUser (Pro) </td>
       <td style="text-align:right">✅</td>
    </tr>
    <tr>
      <td>DescribeBroker (Pro)  <a href="#misc" title="covered by our integration test suite">✨</a></td>
       <td style="text-align:right">✅</td>
    </tr>
    <tr>
      <td>DescribeBrokerEngineTypes (Pro)  <a href="#misc" title="covered by our integration test suite">✨</a></td>
       <td style="text-align:right">✅</td>
    </tr>
    <tr>
      <td>DescribeConfiguration (Pro)  <a href="#misc" title="covered by our integration test suite">✨</a></td>
       <td style="text-align:right">✅</td>
    </tr>
    <tr>
      <td>DescribeConfigurationRevision (Pro) </td>
       <td style="text-align:right">✅</td>
    </tr>
    <tr>
      <td>DescribeUser (Pro) </td>
       <td style="text-align:right">✅</td>
    </tr>
    <tr>
      <td>ListBrokers (Pro)  <a href="#misc" title="covered by our integration test suite">✨</a></td>
       <td style="text-align:right">✅</td>
    </tr>
    <tr>
      <td>ListConfigurations (Pro)  <a href="#misc" title="covered by our integration test suite">✨</a></td>
       <td style="text-align:right">✅</td>
    </tr>
    <tr>
      <td>ListTags (Pro)  <a href="#misc" title="covered by our integration test suite">✨</a></td>
       <td style="text-align:right">✅</td>
    </tr>
    <tr>
      <td>ListUsers (Pro) </td>
       <td style="text-align:right">✅</td>
    </tr>
    <tr>
      <td>RebootBroker (Pro) </td>
       <td style="text-align:right">✅</td>
    </tr>
    <tr>
      <td>UpdateBroker (Pro) </td>
       <td style="text-align:right">✅</td>
    </tr>
    <tr>
      <td>UpdateConfiguration (Pro) </td>
       <td style="text-align:right">✅</td>
    </tr>
    <tr>
      <td>UpdateUser (Pro) </td>
       <td style="text-align:right">✅</td>
    </tr>
  </tbody>
  <tbody>    <tr>
      <td><a data-toggle="collapse" href=".mq-notimplemented">Show missing</a></td>
      <td style="text-align:right"></td>
    </tr>
  </tbody>
  <tbody class="collapse mq-notimplemented">     <tr>
      <td>DescribeBrokerInstanceOptions</td>
       <td style="text-align:right">-</td>
    </tr>
    <tr>
      <td>ListConfigurationRevisions</td>
       <td style="text-align:right">-</td>
    </tr>
  </tbody>
 </table>


## mwaa ##

<table>
  <thead>
    <tr>
      <th>Operation</th>
      <th style="text-align:right">Implemented</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td>CreateEnvironment (Pro) </td>
       <td style="text-align:right">✅</td>
    </tr>
    <tr>
      <td>DeleteEnvironment (Pro) </td>
       <td style="text-align:right">✅</td>
    </tr>
    <tr>
      <td>GetEnvironment (Pro) </td>
       <td style="text-align:right">✅</td>
    </tr>
    <tr>
      <td>ListEnvironments (Pro)  <a href="#misc" title="covered by our integration test suite">✨</a></td>
       <td style="text-align:right">✅</td>
    </tr>
    <tr>
      <td>ListTagsForResource (Pro) </td>
       <td style="text-align:right">✅</td>
    </tr>
    <tr>
      <td>TagResource (Pro) </td>
       <td style="text-align:right">✅</td>
    </tr>
    <tr>
      <td>UntagResource (Pro) </td>
       <td style="text-align:right">✅</td>
    </tr>
    <tr>
      <td>UpdateEnvironment (Pro) </td>
       <td style="text-align:right">✅</td>
    </tr>
  </tbody>
  <tbody>    <tr>
      <td><a data-toggle="collapse" href=".mwaa-notimplemented">Show missing</a></td>
      <td style="text-align:right"></td>
    </tr>
  </tbody>
  <tbody class="collapse mwaa-notimplemented">     <tr>
      <td>CreateCliToken</td>
       <td style="text-align:right">-</td>
    </tr>
    <tr>
      <td>CreateWebLoginToken</td>
       <td style="text-align:right">-</td>
    </tr>
    <tr>
      <td>PublishMetrics</td>
       <td style="text-align:right">-</td>
    </tr>
  </tbody>
 </table>


## neptune ##

<table>
  <thead>
    <tr>
      <th>Operation</th>
      <th style="text-align:right">Implemented</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td>AddTagsToResource (Pro) </td>
       <td style="text-align:right">✅</td>
    </tr>
    <tr>
      <td>CopyDBClusterSnapshot (Pro) </td>
       <td style="text-align:right">✅</td>
    </tr>
    <tr>
      <td>CreateDBCluster (Pro) </td>
       <td style="text-align:right">✅</td>
    </tr>
    <tr>
      <td>CreateDBClusterEndpoint (Pro) </td>
       <td style="text-align:right">✅</td>
    </tr>
    <tr>
      <td>CreateDBClusterParameterGroup (Pro) </td>
       <td style="text-align:right">✅</td>
    </tr>
    <tr>
      <td>CreateDBClusterSnapshot (Pro) </td>
       <td style="text-align:right">✅</td>
    </tr>
    <tr>
      <td>CreateDBInstance (Pro) </td>
       <td style="text-align:right">✅</td>
    </tr>
    <tr>
      <td>CreateDBParameterGroup (Pro) </td>
       <td style="text-align:right">✅</td>
    </tr>
    <tr>
      <td>CreateDBSubnetGroup (Pro) </td>
       <td style="text-align:right">✅</td>
    </tr>
    <tr>
      <td>CreateEventSubscription (Pro) </td>
       <td style="text-align:right">✅</td>
    </tr>
    <tr>
      <td>DeleteDBCluster (Pro) </td>
       <td style="text-align:right">✅</td>
    </tr>
    <tr>
      <td>DeleteDBClusterEndpoint (Pro) </td>
       <td style="text-align:right">✅</td>
    </tr>
    <tr>
      <td>DeleteDBClusterParameterGroup (Pro) </td>
       <td style="text-align:right">✅</td>
    </tr>
    <tr>
      <td>DeleteDBClusterSnapshot (Pro) </td>
       <td style="text-align:right">✅</td>
    </tr>
    <tr>
      <td>DeleteDBInstance (Pro) </td>
       <td style="text-align:right">✅</td>
    </tr>
    <tr>
      <td>DeleteDBParameterGroup (Pro) </td>
       <td style="text-align:right">✅</td>
    </tr>
    <tr>
      <td>DeleteDBSubnetGroup (Pro) </td>
       <td style="text-align:right">✅</td>
    </tr>
    <tr>
      <td>DeleteEventSubscription (Pro) </td>
       <td style="text-align:right">✅</td>
    </tr>
    <tr>
      <td>DescribeDBClusterEndpoints (Pro) </td>
       <td style="text-align:right">✅</td>
    </tr>
    <tr>
      <td>DescribeDBClusterParameterGroups (Pro) </td>
       <td style="text-align:right">✅</td>
    </tr>
    <tr>
      <td>DescribeDBClusterParameters (Pro) </td>
       <td style="text-align:right">✅</td>
    </tr>
    <tr>
      <td>DescribeDBClusterSnapshots (Pro) </td>
       <td style="text-align:right">✅</td>
    </tr>
    <tr>
      <td>DescribeDBClusters (Pro) </td>
       <td style="text-align:right">✅</td>
    </tr>
    <tr>
      <td>DescribeDBEngineVersions (Pro) </td>
       <td style="text-align:right">✅</td>
    </tr>
    <tr>
      <td>DescribeDBInstances (Pro) </td>
       <td style="text-align:right">✅</td>
    </tr>
    <tr>
      <td>DescribeDBParameterGroups (Pro) </td>
       <td style="text-align:right">✅</td>
    </tr>
    <tr>
      <td>DescribeDBParameters (Pro) </td>
       <td style="text-align:right">✅</td>
    </tr>
    <tr>
      <td>DescribeDBSubnetGroups (Pro) </td>
       <td style="text-align:right">✅</td>
    </tr>
    <tr>
      <td>DescribeEventSubscriptions (Pro) </td>
       <td style="text-align:right">✅</td>
    </tr>
    <tr>
      <td>DescribeGlobalClusters (Pro) </td>
       <td style="text-align:right">✅</td>
    </tr>
    <tr>
      <td>ListTagsForResource (Pro) </td>
       <td style="text-align:right">✅</td>
    </tr>
    <tr>
      <td>ModifyDBCluster (Pro) </td>
       <td style="text-align:right">✅</td>
    </tr>
    <tr>
      <td>ModifyDBClusterEndpoint (Pro) </td>
       <td style="text-align:right">✅</td>
    </tr>
    <tr>
      <td>ModifyDBClusterParameterGroup (Pro) </td>
       <td style="text-align:right">✅</td>
    </tr>
    <tr>
      <td>ModifyDBInstance (Pro) </td>
       <td style="text-align:right">✅</td>
    </tr>
    <tr>
      <td>ModifyDBParameterGroup (Pro) </td>
       <td style="text-align:right">✅</td>
    </tr>
    <tr>
      <td>ModifyDBSubnetGroup (Pro) </td>
       <td style="text-align:right">✅</td>
    </tr>
    <tr>
      <td>RebootDBInstance (Pro) </td>
       <td style="text-align:right">✅</td>
    </tr>
    <tr>
      <td>RemoveTagsFromResource (Pro) </td>
       <td style="text-align:right">✅</td>
    </tr>
    <tr>
      <td>ResetDBClusterParameterGroup (Pro) </td>
       <td style="text-align:right">✅</td>
    </tr>
    <tr>
      <td>RestoreDBClusterFromSnapshot (Pro) </td>
       <td style="text-align:right">✅</td>
    </tr>
    <tr>
      <td>StartDBCluster (Pro) </td>
       <td style="text-align:right">✅</td>
    </tr>
    <tr>
      <td>StopDBCluster (Pro) </td>
       <td style="text-align:right">✅</td>
    </tr>
  </tbody>
  <tbody>    <tr>
      <td><a data-toggle="collapse" href=".neptune-notimplemented">Show missing</a></td>
      <td style="text-align:right"></td>
    </tr>
  </tbody>
  <tbody class="collapse neptune-notimplemented">     <tr>
      <td>AddRoleToDBCluster</td>
       <td style="text-align:right">-</td>
    </tr>
    <tr>
      <td>AddSourceIdentifierToSubscription</td>
       <td style="text-align:right">-</td>
    </tr>
    <tr>
      <td>ApplyPendingMaintenanceAction</td>
       <td style="text-align:right">-</td>
    </tr>
    <tr>
      <td>CopyDBClusterParameterGroup</td>
       <td style="text-align:right">-</td>
    </tr>
    <tr>
      <td>CopyDBParameterGroup</td>
       <td style="text-align:right">-</td>
    </tr>
    <tr>
      <td>CreateGlobalCluster</td>
       <td style="text-align:right">-</td>
    </tr>
    <tr>
      <td>DeleteGlobalCluster</td>
       <td style="text-align:right">-</td>
    </tr>
    <tr>
      <td>DescribeDBClusterSnapshotAttributes</td>
       <td style="text-align:right">-</td>
    </tr>
    <tr>
      <td>DescribeEngineDefaultClusterParameters</td>
       <td style="text-align:right">-</td>
    </tr>
    <tr>
      <td>DescribeEngineDefaultParameters</td>
       <td style="text-align:right">-</td>
    </tr>
    <tr>
      <td>DescribeEventCategories</td>
       <td style="text-align:right">-</td>
    </tr>
    <tr>
      <td>DescribeEvents</td>
       <td style="text-align:right">-</td>
    </tr>
    <tr>
      <td>DescribeOrderableDBInstanceOptions</td>
       <td style="text-align:right">-</td>
    </tr>
    <tr>
      <td>DescribePendingMaintenanceActions</td>
       <td style="text-align:right">-</td>
    </tr>
    <tr>
      <td>DescribeValidDBInstanceModifications</td>
       <td style="text-align:right">-</td>
    </tr>
    <tr>
      <td>FailoverDBCluster</td>
       <td style="text-align:right">-</td>
    </tr>
    <tr>
      <td>FailoverGlobalCluster</td>
       <td style="text-align:right">-</td>
    </tr>
    <tr>
      <td>ModifyDBClusterSnapshotAttribute</td>
       <td style="text-align:right">-</td>
    </tr>
    <tr>
      <td>ModifyEventSubscription</td>
       <td style="text-align:right">-</td>
    </tr>
    <tr>
      <td>ModifyGlobalCluster</td>
       <td style="text-align:right">-</td>
    </tr>
    <tr>
      <td>PromoteReadReplicaDBCluster</td>
       <td style="text-align:right">-</td>
    </tr>
    <tr>
      <td>RemoveFromGlobalCluster</td>
       <td style="text-align:right">-</td>
    </tr>
    <tr>
      <td>RemoveRoleFromDBCluster</td>
       <td style="text-align:right">-</td>
    </tr>
    <tr>
      <td>RemoveSourceIdentifierFromSubscription</td>
       <td style="text-align:right">-</td>
    </tr>
    <tr>
      <td>ResetDBParameterGroup</td>
       <td style="text-align:right">-</td>
    </tr>
    <tr>
      <td>RestoreDBClusterToPointInTime</td>
       <td style="text-align:right">-</td>
    </tr>
  </tbody>
 </table>


## opensearch ##

<table>
  <thead>
    <tr>
      <th>Operation</th>
      <th style="text-align:right">Implemented</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td>AddTags <a href="#misc" title="covered by our integration test suite">✨</a></td>
       <td style="text-align:right">✅</td>
    </tr>
    <tr>
      <td>CreateDomain <a href="#misc" title="covered by our integration test suite">✨</a></td>
       <td style="text-align:right">✅</td>
    </tr>
    <tr>
      <td>DeleteDomain <a href="#misc" title="covered by our integration test suite">✨</a></td>
       <td style="text-align:right">✅</td>
    </tr>
    <tr>
      <td>DescribeDomain <a href="#misc" title="covered by our integration test suite">✨</a></td>
       <td style="text-align:right">✅</td>
    </tr>
    <tr>
      <td>DescribeDomainConfig <a href="#misc" title="covered by our integration test suite">✨</a></td>
       <td style="text-align:right">✅</td>
    </tr>
    <tr>
      <td>DescribeDomains <a href="#misc" title="covered by our integration test suite">✨</a></td>
       <td style="text-align:right">✅</td>
    </tr>
    <tr>
      <td>GetCompatibleVersions <a href="#misc" title="covered by our integration test suite">✨</a></td>
       <td style="text-align:right">✅</td>
    </tr>
    <tr>
      <td>ListDomainNames <a href="#misc" title="covered by our integration test suite">✨</a></td>
       <td style="text-align:right">✅</td>
    </tr>
    <tr>
      <td>ListTags <a href="#misc" title="covered by our integration test suite">✨</a></td>
       <td style="text-align:right">✅</td>
    </tr>
    <tr>
      <td>ListVersions <a href="#misc" title="covered by our integration test suite">✨</a></td>
       <td style="text-align:right">✅</td>
    </tr>
    <tr>
      <td>RemoveTags</td>
       <td style="text-align:right">✅</td>
    </tr>
    <tr>
      <td>UpdateDomainConfig <a href="#misc" title="covered by our integration test suite">✨</a></td>
       <td style="text-align:right">✅</td>
    </tr>
  </tbody>
  <tbody>    <tr>
      <td><a data-toggle="collapse" href=".opensearch-notimplemented">Show missing</a></td>
      <td style="text-align:right"></td>
    </tr>
  </tbody>
  <tbody class="collapse opensearch-notimplemented">     <tr>
      <td>AcceptInboundConnection</td>
       <td style="text-align:right">-</td>
    </tr>
    <tr>
      <td>AssociatePackage</td>
       <td style="text-align:right">-</td>
    </tr>
    <tr>
      <td>CancelServiceSoftwareUpdate</td>
       <td style="text-align:right">-</td>
    </tr>
    <tr>
      <td>CreateOutboundConnection</td>
       <td style="text-align:right">-</td>
    </tr>
    <tr>
      <td>CreatePackage</td>
       <td style="text-align:right">-</td>
    </tr>
    <tr>
      <td>DeleteInboundConnection</td>
       <td style="text-align:right">-</td>
    </tr>
    <tr>
      <td>DeleteOutboundConnection</td>
       <td style="text-align:right">-</td>
    </tr>
    <tr>
      <td>DeletePackage</td>
       <td style="text-align:right">-</td>
    </tr>
    <tr>
      <td>DescribeDomainAutoTunes</td>
       <td style="text-align:right">-</td>
    </tr>
    <tr>
      <td>DescribeDomainChangeProgress</td>
       <td style="text-align:right">-</td>
    </tr>
    <tr>
      <td>DescribeInboundConnections</td>
       <td style="text-align:right">-</td>
    </tr>
    <tr>
      <td>DescribeInstanceTypeLimits</td>
       <td style="text-align:right">-</td>
    </tr>
    <tr>
      <td>DescribeOutboundConnections</td>
       <td style="text-align:right">-</td>
    </tr>
    <tr>
      <td>DescribePackages</td>
       <td style="text-align:right">-</td>
    </tr>
    <tr>
      <td>DescribeReservedInstanceOfferings</td>
       <td style="text-align:right">-</td>
    </tr>
    <tr>
      <td>DescribeReservedInstances</td>
       <td style="text-align:right">-</td>
    </tr>
    <tr>
      <td>DissociatePackage</td>
       <td style="text-align:right">-</td>
    </tr>
    <tr>
      <td>GetPackageVersionHistory</td>
       <td style="text-align:right">-</td>
    </tr>
    <tr>
      <td>GetUpgradeHistory</td>
       <td style="text-align:right">-</td>
    </tr>
    <tr>
      <td>GetUpgradeStatus</td>
       <td style="text-align:right">-</td>
    </tr>
    <tr>
      <td>ListDomainsForPackage</td>
       <td style="text-align:right">-</td>
    </tr>
    <tr>
      <td>ListInstanceTypeDetails</td>
       <td style="text-align:right">-</td>
    </tr>
    <tr>
      <td>ListPackagesForDomain</td>
       <td style="text-align:right">-</td>
    </tr>
    <tr>
      <td>PurchaseReservedInstanceOffering</td>
       <td style="text-align:right">-</td>
    </tr>
    <tr>
      <td>RejectInboundConnection</td>
       <td style="text-align:right">-</td>
    </tr>
    <tr>
      <td>StartServiceSoftwareUpdate</td>
       <td style="text-align:right">-</td>
    </tr>
    <tr>
      <td>UpdatePackage</td>
       <td style="text-align:right">-</td>
    </tr>
    <tr>
      <td>UpgradeDomain</td>
       <td style="text-align:right">-</td>
    </tr>
  </tbody>
 </table>


## organizations ##

<table>
  <thead>
    <tr>
      <th>Operation</th>
      <th style="text-align:right">Implemented</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td>AttachPolicy (Pro) </td>
       <td style="text-align:right">✅</td>
    </tr>
    <tr>
      <td>CloseAccount (Pro) </td>
       <td style="text-align:right">✅</td>
    </tr>
    <tr>
      <td>CreateAccount (Pro)  <a href="#misc" title="covered by our integration test suite">✨</a></td>
       <td style="text-align:right">✅</td>
    </tr>
    <tr>
      <td>CreateOrganization (Pro)  <a href="#misc" title="covered by our integration test suite">✨</a></td>
       <td style="text-align:right">✅</td>
    </tr>
    <tr>
      <td>CreateOrganizationalUnit (Pro) </td>
       <td style="text-align:right">✅</td>
    </tr>
    <tr>
      <td>CreatePolicy (Pro)  <a href="#misc" title="covered by our integration test suite">✨</a></td>
       <td style="text-align:right">✅</td>
    </tr>
    <tr>
      <td>DeleteOrganization (Pro)  <a href="#misc" title="covered by our integration test suite">✨</a></td>
       <td style="text-align:right">✅</td>
    </tr>
    <tr>
      <td>DeletePolicy (Pro)  <a href="#misc" title="covered by our integration test suite">✨</a></td>
       <td style="text-align:right">✅</td>
    </tr>
    <tr>
      <td>DeregisterDelegatedAdministrator (Pro) </td>
       <td style="text-align:right">✅</td>
    </tr>
    <tr>
      <td>DescribeAccount (Pro)  <a href="#misc" title="covered by our integration test suite">✨</a></td>
       <td style="text-align:right">✅</td>
    </tr>
    <tr>
      <td>DescribeCreateAccountStatus (Pro) </td>
       <td style="text-align:right">✅</td>
    </tr>
    <tr>
      <td>DescribeOrganization (Pro)  <a href="#misc" title="covered by our integration test suite">✨</a></td>
       <td style="text-align:right">✅</td>
    </tr>
    <tr>
      <td>DescribeOrganizationalUnit (Pro) </td>
       <td style="text-align:right">✅</td>
    </tr>
    <tr>
      <td>DescribePolicy (Pro) </td>
       <td style="text-align:right">✅</td>
    </tr>
    <tr>
      <td>DetachPolicy (Pro) </td>
       <td style="text-align:right">✅</td>
    </tr>
    <tr>
      <td>DisableAWSServiceAccess (Pro) </td>
       <td style="text-align:right">✅</td>
    </tr>
    <tr>
      <td>DisablePolicyType (Pro) </td>
       <td style="text-align:right">✅</td>
    </tr>
    <tr>
      <td>EnableAWSServiceAccess (Pro) </td>
       <td style="text-align:right">✅</td>
    </tr>
    <tr>
      <td>EnablePolicyType (Pro) </td>
       <td style="text-align:right">✅</td>
    </tr>
    <tr>
      <td>ListAWSServiceAccessForOrganization (Pro) </td>
       <td style="text-align:right">✅</td>
    </tr>
    <tr>
      <td>ListAccounts (Pro) </td>
       <td style="text-align:right">✅</td>
    </tr>
    <tr>
      <td>ListAccountsForParent (Pro) </td>
       <td style="text-align:right">✅</td>
    </tr>
    <tr>
      <td>ListChildren (Pro) </td>
       <td style="text-align:right">✅</td>
    </tr>
    <tr>
      <td>ListCreateAccountStatus (Pro) </td>
       <td style="text-align:right">✅</td>
    </tr>
    <tr>
      <td>ListDelegatedAdministrators (Pro) </td>
       <td style="text-align:right">✅</td>
    </tr>
    <tr>
      <td>ListDelegatedServicesForAccount (Pro) </td>
       <td style="text-align:right">✅</td>
    </tr>
    <tr>
      <td>ListOrganizationalUnitsForParent (Pro) </td>
       <td style="text-align:right">✅</td>
    </tr>
    <tr>
      <td>ListParents (Pro) </td>
       <td style="text-align:right">✅</td>
    </tr>
    <tr>
      <td>ListPolicies (Pro) </td>
       <td style="text-align:right">✅</td>
    </tr>
    <tr>
      <td>ListPoliciesForTarget (Pro) </td>
       <td style="text-align:right">✅</td>
    </tr>
    <tr>
      <td>ListRoots (Pro) </td>
       <td style="text-align:right">✅</td>
    </tr>
    <tr>
      <td>ListTagsForResource (Pro)  <a href="#misc" title="covered by our integration test suite">✨</a></td>
       <td style="text-align:right">✅</td>
    </tr>
    <tr>
      <td>ListTargetsForPolicy (Pro) </td>
       <td style="text-align:right">✅</td>
    </tr>
    <tr>
      <td>MoveAccount (Pro) </td>
       <td style="text-align:right">✅</td>
    </tr>
    <tr>
      <td>RegisterDelegatedAdministrator (Pro) </td>
       <td style="text-align:right">✅</td>
    </tr>
    <tr>
      <td>RemoveAccountFromOrganization (Pro)  <a href="#misc" title="covered by our integration test suite">✨</a></td>
       <td style="text-align:right">✅</td>
    </tr>
    <tr>
      <td>TagResource (Pro)  <a href="#misc" title="covered by our integration test suite">✨</a></td>
       <td style="text-align:right">✅</td>
    </tr>
    <tr>
      <td>UntagResource (Pro) </td>
       <td style="text-align:right">✅</td>
    </tr>
    <tr>
      <td>UpdateOrganizationalUnit (Pro) </td>
       <td style="text-align:right">✅</td>
    </tr>
    <tr>
      <td>UpdatePolicy (Pro) </td>
       <td style="text-align:right">✅</td>
    </tr>
  </tbody>
  <tbody>    <tr>
      <td><a data-toggle="collapse" href=".organizations-notimplemented">Show missing</a></td>
      <td style="text-align:right"></td>
    </tr>
  </tbody>
  <tbody class="collapse organizations-notimplemented">     <tr>
      <td>AcceptHandshake</td>
       <td style="text-align:right">-</td>
    </tr>
    <tr>
      <td>CancelHandshake</td>
       <td style="text-align:right">-</td>
    </tr>
    <tr>
      <td>CreateGovCloudAccount</td>
       <td style="text-align:right">-</td>
    </tr>
    <tr>
      <td>DeclineHandshake</td>
       <td style="text-align:right">-</td>
    </tr>
    <tr>
      <td>DeleteOrganizationalUnit</td>
       <td style="text-align:right">-</td>
    </tr>
    <tr>
      <td>DescribeEffectivePolicy</td>
       <td style="text-align:right">-</td>
    </tr>
    <tr>
      <td>DescribeHandshake</td>
       <td style="text-align:right">-</td>
    </tr>
    <tr>
      <td>EnableAllFeatures</td>
       <td style="text-align:right">-</td>
    </tr>
    <tr>
      <td>InviteAccountToOrganization</td>
       <td style="text-align:right">-</td>
    </tr>
    <tr>
      <td>LeaveOrganization</td>
       <td style="text-align:right">-</td>
    </tr>
    <tr>
      <td>ListHandshakesForAccount</td>
       <td style="text-align:right">-</td>
    </tr>
    <tr>
      <td>ListHandshakesForOrganization</td>
       <td style="text-align:right">-</td>
    </tr>
  </tbody>
 </table>


## qldb ##

<table>
  <thead>
    <tr>
      <th>Operation</th>
      <th style="text-align:right">Implemented</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td>CreateLedger (Pro)  <a href="#misc" title="covered by our integration test suite">✨</a></td>
       <td style="text-align:right">✅</td>
    </tr>
    <tr>
      <td>DeleteLedger (Pro)  <a href="#misc" title="covered by our integration test suite">✨</a></td>
       <td style="text-align:right">✅</td>
    </tr>
    <tr>
      <td>DescribeJournalKinesisStream (Pro) </td>
       <td style="text-align:right">✅</td>
    </tr>
    <tr>
      <td>DescribeJournalS3Export (Pro) </td>
       <td style="text-align:right">✅</td>
    </tr>
    <tr>
      <td>DescribeLedger (Pro)  <a href="#misc" title="covered by our integration test suite">✨</a></td>
       <td style="text-align:right">✅</td>
    </tr>
    <tr>
      <td>ExportJournalToS3 (Pro) </td>
       <td style="text-align:right">✅</td>
    </tr>
    <tr>
      <td>ListLedgers (Pro)  <a href="#misc" title="covered by our integration test suite">✨</a></td>
       <td style="text-align:right">✅</td>
    </tr>
    <tr>
      <td>ListTagsForResource (Pro)  <a href="#misc" title="covered by our integration test suite">✨</a></td>
       <td style="text-align:right">✅</td>
    </tr>
    <tr>
      <td>StreamJournalToKinesis (Pro)  <a href="#misc" title="covered by our integration test suite">✨</a></td>
       <td style="text-align:right">✅</td>
    </tr>
    <tr>
      <td>TagResource (Pro) </td>
       <td style="text-align:right">✅</td>
    </tr>
    <tr>
      <td>UntagResource (Pro) </td>
       <td style="text-align:right">✅</td>
    </tr>
    <tr>
      <td>UpdateLedger (Pro)  <a href="#misc" title="covered by our integration test suite">✨</a></td>
       <td style="text-align:right">✅</td>
    </tr>
  </tbody>
  <tbody>    <tr>
      <td><a data-toggle="collapse" href=".qldb-notimplemented">Show missing</a></td>
      <td style="text-align:right"></td>
    </tr>
  </tbody>
  <tbody class="collapse qldb-notimplemented">     <tr>
      <td>CancelJournalKinesisStream</td>
       <td style="text-align:right">-</td>
    </tr>
    <tr>
      <td>GetBlock</td>
       <td style="text-align:right">-</td>
    </tr>
    <tr>
      <td>GetDigest</td>
       <td style="text-align:right">-</td>
    </tr>
    <tr>
      <td>GetRevision</td>
       <td style="text-align:right">-</td>
    </tr>
    <tr>
      <td>ListJournalKinesisStreamsForLedger</td>
       <td style="text-align:right">-</td>
    </tr>
    <tr>
      <td>ListJournalS3Exports</td>
       <td style="text-align:right">-</td>
    </tr>
    <tr>
      <td>ListJournalS3ExportsForLedger</td>
       <td style="text-align:right">-</td>
    </tr>
    <tr>
      <td>UpdateLedgerPermissionsMode</td>
       <td style="text-align:right">-</td>
    </tr>
  </tbody>
 </table>


## qldb-session ##

<table>
  <thead>
    <tr>
      <th>Operation</th>
      <th style="text-align:right">Implemented</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td>SendCommand (Pro)  <a href="#misc" title="covered by our integration test suite">✨</a></td>
       <td style="text-align:right">✅</td>
    </tr>
  </tbody>
 </table>


## rds ##

<table>
  <thead>
    <tr>
      <th>Operation</th>
      <th style="text-align:right">Implemented</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td>AddTagsToResource (Pro)  <a href="#misc" title="covered by our integration test suite">✨</a></td>
       <td style="text-align:right">✅</td>
    </tr>
    <tr>
      <td>AuthorizeDBSecurityGroupIngress (Pro) </td>
       <td style="text-align:right">✅</td>
    </tr>
    <tr>
      <td>CancelExportTask (Pro) </td>
       <td style="text-align:right">✅</td>
    </tr>
    <tr>
      <td>CopyDBClusterSnapshot (Pro) </td>
       <td style="text-align:right">✅</td>
    </tr>
    <tr>
      <td>CopyDBSnapshot (Pro) </td>
       <td style="text-align:right">✅</td>
    </tr>
    <tr>
      <td>CreateDBCluster (Pro)  <a href="#misc" title="covered by our integration test suite">✨</a></td>
       <td style="text-align:right">✅</td>
    </tr>
    <tr>
      <td>CreateDBClusterEndpoint (Pro)  <a href="#misc" title="covered by our integration test suite">✨</a></td>
       <td style="text-align:right">✅</td>
    </tr>
    <tr>
      <td>CreateDBClusterParameterGroup (Pro)  <a href="#misc" title="covered by our integration test suite">✨</a></td>
       <td style="text-align:right">✅</td>
    </tr>
    <tr>
      <td>CreateDBClusterSnapshot (Pro)  <a href="#misc" title="covered by our integration test suite">✨</a></td>
       <td style="text-align:right">✅</td>
    </tr>
    <tr>
      <td>CreateDBInstance (Pro)  <a href="#misc" title="covered by our integration test suite">✨</a></td>
       <td style="text-align:right">✅</td>
    </tr>
    <tr>
      <td>CreateDBInstanceReadReplica (Pro) </td>
       <td style="text-align:right">✅</td>
    </tr>
    <tr>
      <td>CreateDBParameterGroup (Pro)  <a href="#misc" title="covered by our integration test suite">✨</a></td>
       <td style="text-align:right">✅</td>
    </tr>
    <tr>
      <td>CreateDBProxy (Pro)  <a href="#misc" title="covered by our integration test suite">✨</a></td>
       <td style="text-align:right">✅</td>
    </tr>
    <tr>
      <td>CreateDBSecurityGroup (Pro) </td>
       <td style="text-align:right">✅</td>
    </tr>
    <tr>
      <td>CreateDBSnapshot (Pro)  <a href="#misc" title="covered by our integration test suite">✨</a></td>
       <td style="text-align:right">✅</td>
    </tr>
    <tr>
      <td>CreateDBSubnetGroup (Pro)  <a href="#misc" title="covered by our integration test suite">✨</a></td>
       <td style="text-align:right">✅</td>
    </tr>
    <tr>
      <td>CreateEventSubscription (Pro) </td>
       <td style="text-align:right">✅</td>
    </tr>
    <tr>
      <td>CreateOptionGroup (Pro) </td>
       <td style="text-align:right">✅</td>
    </tr>
    <tr>
      <td>DeleteDBCluster (Pro)  <a href="#misc" title="covered by our integration test suite">✨</a></td>
       <td style="text-align:right">✅</td>
    </tr>
    <tr>
      <td>DeleteDBClusterEndpoint (Pro)  <a href="#misc" title="covered by our integration test suite">✨</a></td>
       <td style="text-align:right">✅</td>
    </tr>
    <tr>
      <td>DeleteDBClusterParameterGroup (Pro)  <a href="#misc" title="covered by our integration test suite">✨</a></td>
       <td style="text-align:right">✅</td>
    </tr>
    <tr>
      <td>DeleteDBClusterSnapshot (Pro)  <a href="#misc" title="covered by our integration test suite">✨</a></td>
       <td style="text-align:right">✅</td>
    </tr>
    <tr>
      <td>DeleteDBInstance (Pro)  <a href="#misc" title="covered by our integration test suite">✨</a></td>
       <td style="text-align:right">✅</td>
    </tr>
    <tr>
      <td>DeleteDBParameterGroup (Pro)  <a href="#misc" title="covered by our integration test suite">✨</a></td>
       <td style="text-align:right">✅</td>
    </tr>
    <tr>
      <td>DeleteDBProxy (Pro)  <a href="#misc" title="covered by our integration test suite">✨</a></td>
       <td style="text-align:right">✅</td>
    </tr>
    <tr>
      <td>DeleteDBSecurityGroup (Pro) </td>
       <td style="text-align:right">✅</td>
    </tr>
    <tr>
      <td>DeleteDBSnapshot (Pro) </td>
       <td style="text-align:right">✅</td>
    </tr>
    <tr>
      <td>DeleteDBSubnetGroup (Pro)  <a href="#misc" title="covered by our integration test suite">✨</a></td>
       <td style="text-align:right">✅</td>
    </tr>
    <tr>
      <td>DeleteEventSubscription (Pro) </td>
       <td style="text-align:right">✅</td>
    </tr>
    <tr>
      <td>DeleteOptionGroup (Pro) </td>
       <td style="text-align:right">✅</td>
    </tr>
    <tr>
      <td>DeregisterDBProxyTargets (Pro)  <a href="#misc" title="covered by our integration test suite">✨</a></td>
       <td style="text-align:right">✅</td>
    </tr>
    <tr>
      <td>DescribeCertificates (Pro) </td>
       <td style="text-align:right">✅</td>
    </tr>
    <tr>
      <td>DescribeDBClusterEndpoints (Pro)  <a href="#misc" title="covered by our integration test suite">✨</a></td>
       <td style="text-align:right">✅</td>
    </tr>
    <tr>
      <td>DescribeDBClusterParameterGroups (Pro)  <a href="#misc" title="covered by our integration test suite">✨</a></td>
       <td style="text-align:right">✅</td>
    </tr>
    <tr>
      <td>DescribeDBClusterParameters (Pro)  <a href="#misc" title="covered by our integration test suite">✨</a></td>
       <td style="text-align:right">✅</td>
    </tr>
    <tr>
      <td>DescribeDBClusterSnapshots (Pro)  <a href="#misc" title="covered by our integration test suite">✨</a></td>
       <td style="text-align:right">✅</td>
    </tr>
    <tr>
      <td>DescribeDBClusters (Pro)  <a href="#misc" title="covered by our integration test suite">✨</a></td>
       <td style="text-align:right">✅</td>
    </tr>
    <tr>
      <td>DescribeDBEngineVersions (Pro)  <a href="#misc" title="covered by our integration test suite">✨</a></td>
       <td style="text-align:right">✅</td>
    </tr>
    <tr>
      <td>DescribeDBInstances (Pro)  <a href="#misc" title="covered by our integration test suite">✨</a></td>
       <td style="text-align:right">✅</td>
    </tr>
    <tr>
      <td>DescribeDBParameterGroups (Pro)  <a href="#misc" title="covered by our integration test suite">✨</a></td>
       <td style="text-align:right">✅</td>
    </tr>
    <tr>
      <td>DescribeDBParameters (Pro)  <a href="#misc" title="covered by our integration test suite">✨</a></td>
       <td style="text-align:right">✅</td>
    </tr>
    <tr>
      <td>DescribeDBProxies (Pro)  <a href="#misc" title="covered by our integration test suite">✨</a></td>
       <td style="text-align:right">✅</td>
    </tr>
    <tr>
      <td>DescribeDBProxyTargetGroups (Pro)  <a href="#misc" title="covered by our integration test suite">✨</a></td>
       <td style="text-align:right">✅</td>
    </tr>
    <tr>
      <td>DescribeDBProxyTargets (Pro)  <a href="#misc" title="covered by our integration test suite">✨</a></td>
       <td style="text-align:right">✅</td>
    </tr>
    <tr>
      <td>DescribeDBSecurityGroups (Pro) </td>
       <td style="text-align:right">✅</td>
    </tr>
    <tr>
      <td>DescribeDBSnapshots (Pro)  <a href="#misc" title="covered by our integration test suite">✨</a></td>
       <td style="text-align:right">✅</td>
    </tr>
    <tr>
      <td>DescribeDBSubnetGroups (Pro)  <a href="#misc" title="covered by our integration test suite">✨</a></td>
       <td style="text-align:right">✅</td>
    </tr>
    <tr>
      <td>DescribeEventSubscriptions (Pro) </td>
       <td style="text-align:right">✅</td>
    </tr>
    <tr>
      <td>DescribeExportTasks (Pro) </td>
       <td style="text-align:right">✅</td>
    </tr>
    <tr>
      <td>DescribeGlobalClusters (Pro) </td>
       <td style="text-align:right">✅</td>
    </tr>
    <tr>
      <td>DescribeOptionGroupOptions (Pro) </td>
       <td style="text-align:right">✅</td>
    </tr>
    <tr>
      <td>DescribeOptionGroups (Pro) </td>
       <td style="text-align:right">✅</td>
    </tr>
    <tr>
      <td>ListTagsForResource (Pro)  <a href="#misc" title="covered by our integration test suite">✨</a></td>
       <td style="text-align:right">✅</td>
    </tr>
    <tr>
      <td>ModifyCertificates (Pro) </td>
       <td style="text-align:right">✅</td>
    </tr>
    <tr>
      <td>ModifyCurrentDBClusterCapacity (Pro) </td>
       <td style="text-align:right">✅</td>
    </tr>
    <tr>
      <td>ModifyDBCluster (Pro)  <a href="#misc" title="covered by our integration test suite">✨</a></td>
       <td style="text-align:right">✅</td>
    </tr>
    <tr>
      <td>ModifyDBClusterEndpoint (Pro)  <a href="#misc" title="covered by our integration test suite">✨</a></td>
       <td style="text-align:right">✅</td>
    </tr>
    <tr>
      <td>ModifyDBClusterParameterGroup (Pro)  <a href="#misc" title="covered by our integration test suite">✨</a></td>
       <td style="text-align:right">✅</td>
    </tr>
    <tr>
      <td>ModifyDBInstance (Pro)  <a href="#misc" title="covered by our integration test suite">✨</a></td>
       <td style="text-align:right">✅</td>
    </tr>
    <tr>
      <td>ModifyDBParameterGroup (Pro)  <a href="#misc" title="covered by our integration test suite">✨</a></td>
       <td style="text-align:right">✅</td>
    </tr>
    <tr>
      <td>ModifyDBProxyTargetGroup (Pro)  <a href="#misc" title="covered by our integration test suite">✨</a></td>
       <td style="text-align:right">✅</td>
    </tr>
    <tr>
      <td>ModifyDBSubnetGroup (Pro) </td>
       <td style="text-align:right">✅</td>
    </tr>
    <tr>
      <td>ModifyOptionGroup (Pro) </td>
       <td style="text-align:right">✅</td>
    </tr>
    <tr>
      <td>RebootDBInstance (Pro)  <a href="#misc" title="covered by our integration test suite">✨</a></td>
       <td style="text-align:right">✅</td>
    </tr>
    <tr>
      <td>RegisterDBProxyTargets (Pro)  <a href="#misc" title="covered by our integration test suite">✨</a></td>
       <td style="text-align:right">✅</td>
    </tr>
    <tr>
      <td>RemoveTagsFromResource (Pro)  <a href="#misc" title="covered by our integration test suite">✨</a></td>
       <td style="text-align:right">✅</td>
    </tr>
    <tr>
      <td>ResetDBClusterParameterGroup (Pro) </td>
       <td style="text-align:right">✅</td>
    </tr>
    <tr>
      <td>RestoreDBClusterFromSnapshot (Pro)  <a href="#misc" title="covered by our integration test suite">✨</a></td>
       <td style="text-align:right">✅</td>
    </tr>
    <tr>
      <td>RestoreDBInstanceFromDBSnapshot (Pro)  <a href="#misc" title="covered by our integration test suite">✨</a></td>
       <td style="text-align:right">✅</td>
    </tr>
    <tr>
      <td>StartDBCluster (Pro) </td>
       <td style="text-align:right">✅</td>
    </tr>
    <tr>
      <td>StartDBInstance (Pro) </td>
       <td style="text-align:right">✅</td>
    </tr>
    <tr>
      <td>StartExportTask (Pro) </td>
       <td style="text-align:right">✅</td>
    </tr>
    <tr>
      <td>StopDBCluster (Pro) </td>
       <td style="text-align:right">✅</td>
    </tr>
    <tr>
      <td>StopDBInstance (Pro) </td>
       <td style="text-align:right">✅</td>
    </tr>
  </tbody>
  <tbody>    <tr>
      <td><a data-toggle="collapse" href=".rds-notimplemented">Show missing</a></td>
      <td style="text-align:right"></td>
    </tr>
  </tbody>
  <tbody class="collapse rds-notimplemented">     <tr>
      <td>AddRoleToDBCluster</td>
       <td style="text-align:right">-</td>
    </tr>
    <tr>
      <td>AddRoleToDBInstance</td>
       <td style="text-align:right">-</td>
    </tr>
    <tr>
      <td>AddSourceIdentifierToSubscription</td>
       <td style="text-align:right">-</td>
    </tr>
    <tr>
      <td>ApplyPendingMaintenanceAction</td>
       <td style="text-align:right">-</td>
    </tr>
    <tr>
      <td>BacktrackDBCluster</td>
       <td style="text-align:right">-</td>
    </tr>
    <tr>
      <td>CopyDBClusterParameterGroup</td>
       <td style="text-align:right">-</td>
    </tr>
    <tr>
      <td>CopyDBParameterGroup</td>
       <td style="text-align:right">-</td>
    </tr>
    <tr>
      <td>CopyOptionGroup</td>
       <td style="text-align:right">-</td>
    </tr>
    <tr>
      <td>CreateCustomDBEngineVersion</td>
       <td style="text-align:right">-</td>
    </tr>
    <tr>
      <td>CreateDBProxyEndpoint</td>
       <td style="text-align:right">-</td>
    </tr>
    <tr>
      <td>CreateGlobalCluster</td>
       <td style="text-align:right">-</td>
    </tr>
    <tr>
      <td>DeleteCustomDBEngineVersion</td>
       <td style="text-align:right">-</td>
    </tr>
    <tr>
      <td>DeleteDBInstanceAutomatedBackup</td>
       <td style="text-align:right">-</td>
    </tr>
    <tr>
      <td>DeleteDBProxyEndpoint</td>
       <td style="text-align:right">-</td>
    </tr>
    <tr>
      <td>DeleteGlobalCluster</td>
       <td style="text-align:right">-</td>
    </tr>
    <tr>
      <td>DescribeAccountAttributes</td>
       <td style="text-align:right">-</td>
    </tr>
    <tr>
      <td>DescribeDBClusterBacktracks</td>
       <td style="text-align:right">-</td>
    </tr>
    <tr>
      <td>DescribeDBClusterSnapshotAttributes</td>
       <td style="text-align:right">-</td>
    </tr>
    <tr>
      <td>DescribeDBInstanceAutomatedBackups</td>
       <td style="text-align:right">-</td>
    </tr>
    <tr>
      <td>DescribeDBLogFiles</td>
       <td style="text-align:right">-</td>
    </tr>
    <tr>
      <td>DescribeDBProxyEndpoints</td>
       <td style="text-align:right">-</td>
    </tr>
    <tr>
      <td>DescribeDBSnapshotAttributes</td>
       <td style="text-align:right">-</td>
    </tr>
    <tr>
      <td>DescribeEngineDefaultClusterParameters</td>
       <td style="text-align:right">-</td>
    </tr>
    <tr>
      <td>DescribeEngineDefaultParameters</td>
       <td style="text-align:right">-</td>
    </tr>
    <tr>
      <td>DescribeEventCategories</td>
       <td style="text-align:right">-</td>
    </tr>
    <tr>
      <td>DescribeEvents</td>
       <td style="text-align:right">-</td>
    </tr>
    <tr>
      <td>DescribeOrderableDBInstanceOptions</td>
       <td style="text-align:right">-</td>
    </tr>
    <tr>
      <td>DescribePendingMaintenanceActions</td>
       <td style="text-align:right">-</td>
    </tr>
    <tr>
      <td>DescribeReservedDBInstances</td>
       <td style="text-align:right">-</td>
    </tr>
    <tr>
      <td>DescribeReservedDBInstancesOfferings</td>
       <td style="text-align:right">-</td>
    </tr>
    <tr>
      <td>DescribeSourceRegions</td>
       <td style="text-align:right">-</td>
    </tr>
    <tr>
      <td>DescribeValidDBInstanceModifications</td>
       <td style="text-align:right">-</td>
    </tr>
    <tr>
      <td>DownloadDBLogFilePortion</td>
       <td style="text-align:right">-</td>
    </tr>
    <tr>
      <td>FailoverDBCluster</td>
       <td style="text-align:right">-</td>
    </tr>
    <tr>
      <td>FailoverGlobalCluster</td>
       <td style="text-align:right">-</td>
    </tr>
    <tr>
      <td>ModifyActivityStream</td>
       <td style="text-align:right">-</td>
    </tr>
    <tr>
      <td>ModifyCustomDBEngineVersion</td>
       <td style="text-align:right">-</td>
    </tr>
    <tr>
      <td>ModifyDBClusterSnapshotAttribute</td>
       <td style="text-align:right">-</td>
    </tr>
    <tr>
      <td>ModifyDBProxy</td>
       <td style="text-align:right">-</td>
    </tr>
    <tr>
      <td>ModifyDBProxyEndpoint</td>
       <td style="text-align:right">-</td>
    </tr>
    <tr>
      <td>ModifyDBSnapshot</td>
       <td style="text-align:right">-</td>
    </tr>
    <tr>
      <td>ModifyDBSnapshotAttribute</td>
       <td style="text-align:right">-</td>
    </tr>
    <tr>
      <td>ModifyEventSubscription</td>
       <td style="text-align:right">-</td>
    </tr>
    <tr>
      <td>ModifyGlobalCluster</td>
       <td style="text-align:right">-</td>
    </tr>
    <tr>
      <td>PromoteReadReplica</td>
       <td style="text-align:right">-</td>
    </tr>
    <tr>
      <td>PromoteReadReplicaDBCluster</td>
       <td style="text-align:right">-</td>
    </tr>
    <tr>
      <td>PurchaseReservedDBInstancesOffering</td>
       <td style="text-align:right">-</td>
    </tr>
    <tr>
      <td>RebootDBCluster</td>
       <td style="text-align:right">-</td>
    </tr>
    <tr>
      <td>RemoveFromGlobalCluster</td>
       <td style="text-align:right">-</td>
    </tr>
    <tr>
      <td>RemoveRoleFromDBCluster</td>
       <td style="text-align:right">-</td>
    </tr>
    <tr>
      <td>RemoveRoleFromDBInstance</td>
       <td style="text-align:right">-</td>
    </tr>
    <tr>
      <td>RemoveSourceIdentifierFromSubscription</td>
       <td style="text-align:right">-</td>
    </tr>
    <tr>
      <td>ResetDBParameterGroup</td>
       <td style="text-align:right">-</td>
    </tr>
    <tr>
      <td>RestoreDBClusterFromS3</td>
       <td style="text-align:right">-</td>
    </tr>
    <tr>
      <td>RestoreDBClusterToPointInTime</td>
       <td style="text-align:right">-</td>
    </tr>
    <tr>
      <td>RestoreDBInstanceFromS3</td>
       <td style="text-align:right">-</td>
    </tr>
    <tr>
      <td>RestoreDBInstanceToPointInTime</td>
       <td style="text-align:right">-</td>
    </tr>
    <tr>
      <td>RevokeDBSecurityGroupIngress</td>
       <td style="text-align:right">-</td>
    </tr>
    <tr>
      <td>StartActivityStream</td>
       <td style="text-align:right">-</td>
    </tr>
    <tr>
      <td>StartDBInstanceAutomatedBackupsReplication</td>
       <td style="text-align:right">-</td>
    </tr>
    <tr>
      <td>StopActivityStream</td>
       <td style="text-align:right">-</td>
    </tr>
    <tr>
      <td>StopDBInstanceAutomatedBackupsReplication</td>
       <td style="text-align:right">-</td>
    </tr>
    <tr>
      <td>SwitchoverReadReplica</td>
       <td style="text-align:right">-</td>
    </tr>
  </tbody>
 </table>


## rds-data ##

<table>
  <thead>
    <tr>
      <th>Operation</th>
      <th style="text-align:right">Implemented</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td>BeginTransaction (Pro)  <a href="#misc" title="covered by our integration test suite">✨</a></td>
       <td style="text-align:right">✅</td>
    </tr>
    <tr>
      <td>CommitTransaction (Pro)  <a href="#misc" title="covered by our integration test suite">✨</a></td>
       <td style="text-align:right">✅</td>
    </tr>
    <tr>
      <td>ExecuteSql (Pro)  <a href="#misc" title="covered by our integration test suite">✨</a></td>
       <td style="text-align:right">✅</td>
    </tr>
    <tr>
      <td>ExecuteStatement (Pro)  <a href="#misc" title="covered by our integration test suite">✨</a></td>
       <td style="text-align:right">✅</td>
    </tr>
  </tbody>
  <tbody>    <tr>
      <td><a data-toggle="collapse" href=".rds-data-notimplemented">Show missing</a></td>
      <td style="text-align:right"></td>
    </tr>
  </tbody>
  <tbody class="collapse rds-data-notimplemented">     <tr>
      <td>BatchExecuteStatement</td>
       <td style="text-align:right">-</td>
    </tr>
    <tr>
      <td>RollbackTransaction</td>
       <td style="text-align:right">-</td>
    </tr>
  </tbody>
 </table>


## redshift ##

<table>
  <thead>
    <tr>
      <th>Operation</th>
      <th style="text-align:right">Implemented</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td>AuthorizeClusterSecurityGroupIngress <a href="#misc" title="covered by our integration test suite">✨</a></td>
       <td style="text-align:right">✅</td>
    </tr>
    <tr>
      <td>CreateCluster <a href="#misc" title="covered by our integration test suite">✨</a></td>
       <td style="text-align:right">✅</td>
    </tr>
    <tr>
      <td>CreateClusterParameterGroup <a href="#misc" title="covered by our integration test suite">✨</a></td>
       <td style="text-align:right">✅</td>
    </tr>
    <tr>
      <td>CreateClusterSecurityGroup <a href="#misc" title="covered by our integration test suite">✨</a></td>
       <td style="text-align:right">✅</td>
    </tr>
    <tr>
      <td>CreateClusterSnapshot</td>
       <td style="text-align:right">✅</td>
    </tr>
    <tr>
      <td>CreateClusterSubnetGroup</td>
       <td style="text-align:right">✅</td>
    </tr>
    <tr>
      <td>CreateSnapshotCopyGrant</td>
       <td style="text-align:right">✅</td>
    </tr>
    <tr>
      <td>CreateTags</td>
       <td style="text-align:right">✅</td>
    </tr>
    <tr>
      <td>DeleteCluster <a href="#misc" title="covered by our integration test suite">✨</a></td>
       <td style="text-align:right">✅</td>
    </tr>
    <tr>
      <td>DeleteClusterParameterGroup</td>
       <td style="text-align:right">✅</td>
    </tr>
    <tr>
      <td>DeleteClusterSecurityGroup</td>
       <td style="text-align:right">✅</td>
    </tr>
    <tr>
      <td>DeleteClusterSnapshot</td>
       <td style="text-align:right">✅</td>
    </tr>
    <tr>
      <td>DeleteClusterSubnetGroup</td>
       <td style="text-align:right">✅</td>
    </tr>
    <tr>
      <td>DeleteSnapshotCopyGrant</td>
       <td style="text-align:right">✅</td>
    </tr>
    <tr>
      <td>DeleteTags</td>
       <td style="text-align:right">✅</td>
    </tr>
    <tr>
      <td>DescribeClusterParameterGroups <a href="#misc" title="covered by our integration test suite">✨</a></td>
       <td style="text-align:right">✅</td>
    </tr>
    <tr>
      <td>DescribeClusterParameters (Pro)  <a href="#misc" title="covered by our integration test suite">✨</a></td>
       <td style="text-align:right">✅</td>
    </tr>
    <tr>
      <td>DescribeClusterSecurityGroups <a href="#misc" title="covered by our integration test suite">✨</a></td>
       <td style="text-align:right">✅</td>
    </tr>
    <tr>
      <td>DescribeClusterSnapshots</td>
       <td style="text-align:right">✅</td>
    </tr>
    <tr>
      <td>DescribeClusterSubnetGroups</td>
       <td style="text-align:right">✅</td>
    </tr>
    <tr>
      <td>DescribeClusters <a href="#misc" title="covered by our integration test suite">✨</a></td>
       <td style="text-align:right">✅</td>
    </tr>
    <tr>
      <td>DescribeDefaultClusterParameters (Pro)  <a href="#misc" title="covered by our integration test suite">✨</a></td>
       <td style="text-align:right">✅</td>
    </tr>
    <tr>
      <td>DescribeSnapshotCopyGrants</td>
       <td style="text-align:right">✅</td>
    </tr>
    <tr>
      <td>DescribeTags</td>
       <td style="text-align:right">✅</td>
    </tr>
    <tr>
      <td>DisableSnapshotCopy</td>
       <td style="text-align:right">✅</td>
    </tr>
    <tr>
      <td>EnableSnapshotCopy</td>
       <td style="text-align:right">✅</td>
    </tr>
    <tr>
      <td>GetClusterCredentials</td>
       <td style="text-align:right">✅</td>
    </tr>
    <tr>
      <td>ModifyCluster</td>
       <td style="text-align:right">✅</td>
    </tr>
    <tr>
      <td>ModifySnapshotCopyRetentionPeriod</td>
       <td style="text-align:right">✅</td>
    </tr>
    <tr>
      <td>PauseCluster</td>
       <td style="text-align:right">✅</td>
    </tr>
    <tr>
      <td>RestoreFromClusterSnapshot</td>
       <td style="text-align:right">✅</td>
    </tr>
    <tr>
      <td>ResumeCluster</td>
       <td style="text-align:right">✅</td>
    </tr>
  </tbody>
  <tbody>    <tr>
      <td><a data-toggle="collapse" href=".redshift-notimplemented">Show missing</a></td>
      <td style="text-align:right"></td>
    </tr>
  </tbody>
  <tbody class="collapse redshift-notimplemented">     <tr>
      <td>AcceptReservedNodeExchange</td>
       <td style="text-align:right">-</td>
    </tr>
    <tr>
      <td>AddPartner</td>
       <td style="text-align:right">-</td>
    </tr>
    <tr>
      <td>AssociateDataShareConsumer</td>
       <td style="text-align:right">-</td>
    </tr>
    <tr>
      <td>AuthorizeDataShare</td>
       <td style="text-align:right">-</td>
    </tr>
    <tr>
      <td>AuthorizeEndpointAccess</td>
       <td style="text-align:right">-</td>
    </tr>
    <tr>
      <td>AuthorizeSnapshotAccess</td>
       <td style="text-align:right">-</td>
    </tr>
    <tr>
      <td>BatchDeleteClusterSnapshots</td>
       <td style="text-align:right">-</td>
    </tr>
    <tr>
      <td>BatchModifyClusterSnapshots</td>
       <td style="text-align:right">-</td>
    </tr>
    <tr>
      <td>CancelResize</td>
       <td style="text-align:right">-</td>
    </tr>
    <tr>
      <td>CopyClusterSnapshot</td>
       <td style="text-align:right">-</td>
    </tr>
    <tr>
      <td>CreateAuthenticationProfile</td>
       <td style="text-align:right">-</td>
    </tr>
    <tr>
      <td>CreateEndpointAccess</td>
       <td style="text-align:right">-</td>
    </tr>
    <tr>
      <td>CreateEventSubscription</td>
       <td style="text-align:right">-</td>
    </tr>
    <tr>
      <td>CreateHsmClientCertificate</td>
       <td style="text-align:right">-</td>
    </tr>
    <tr>
      <td>CreateHsmConfiguration</td>
       <td style="text-align:right">-</td>
    </tr>
    <tr>
      <td>CreateScheduledAction</td>
       <td style="text-align:right">-</td>
    </tr>
    <tr>
      <td>CreateSnapshotSchedule</td>
       <td style="text-align:right">-</td>
    </tr>
    <tr>
      <td>CreateUsageLimit</td>
       <td style="text-align:right">-</td>
    </tr>
    <tr>
      <td>DeauthorizeDataShare</td>
       <td style="text-align:right">-</td>
    </tr>
    <tr>
      <td>DeleteAuthenticationProfile</td>
       <td style="text-align:right">-</td>
    </tr>
    <tr>
      <td>DeleteEndpointAccess</td>
       <td style="text-align:right">-</td>
    </tr>
    <tr>
      <td>DeleteEventSubscription</td>
       <td style="text-align:right">-</td>
    </tr>
    <tr>
      <td>DeleteHsmClientCertificate</td>
       <td style="text-align:right">-</td>
    </tr>
    <tr>
      <td>DeleteHsmConfiguration</td>
       <td style="text-align:right">-</td>
    </tr>
    <tr>
      <td>DeletePartner</td>
       <td style="text-align:right">-</td>
    </tr>
    <tr>
      <td>DeleteScheduledAction</td>
       <td style="text-align:right">-</td>
    </tr>
    <tr>
      <td>DeleteSnapshotSchedule</td>
       <td style="text-align:right">-</td>
    </tr>
    <tr>
      <td>DeleteUsageLimit</td>
       <td style="text-align:right">-</td>
    </tr>
    <tr>
      <td>DescribeAccountAttributes</td>
       <td style="text-align:right">-</td>
    </tr>
    <tr>
      <td>DescribeAuthenticationProfiles</td>
       <td style="text-align:right">-</td>
    </tr>
    <tr>
      <td>DescribeClusterDbRevisions</td>
       <td style="text-align:right">-</td>
    </tr>
    <tr>
      <td>DescribeClusterTracks</td>
       <td style="text-align:right">-</td>
    </tr>
    <tr>
      <td>DescribeClusterVersions</td>
       <td style="text-align:right">-</td>
    </tr>
    <tr>
      <td>DescribeDataShares</td>
       <td style="text-align:right">-</td>
    </tr>
    <tr>
      <td>DescribeDataSharesForConsumer</td>
       <td style="text-align:right">-</td>
    </tr>
    <tr>
      <td>DescribeDataSharesForProducer</td>
       <td style="text-align:right">-</td>
    </tr>
    <tr>
      <td>DescribeEndpointAccess</td>
       <td style="text-align:right">-</td>
    </tr>
    <tr>
      <td>DescribeEndpointAuthorization</td>
       <td style="text-align:right">-</td>
    </tr>
    <tr>
      <td>DescribeEventCategories</td>
       <td style="text-align:right">-</td>
    </tr>
    <tr>
      <td>DescribeEventSubscriptions</td>
       <td style="text-align:right">-</td>
    </tr>
    <tr>
      <td>DescribeEvents</td>
       <td style="text-align:right">-</td>
    </tr>
    <tr>
      <td>DescribeHsmClientCertificates</td>
       <td style="text-align:right">-</td>
    </tr>
    <tr>
      <td>DescribeHsmConfigurations</td>
       <td style="text-align:right">-</td>
    </tr>
    <tr>
      <td>DescribeLoggingStatus</td>
       <td style="text-align:right">-</td>
    </tr>
    <tr>
      <td>DescribeNodeConfigurationOptions</td>
       <td style="text-align:right">-</td>
    </tr>
    <tr>
      <td>DescribeOrderableClusterOptions</td>
       <td style="text-align:right">-</td>
    </tr>
    <tr>
      <td>DescribePartners</td>
       <td style="text-align:right">-</td>
    </tr>
    <tr>
      <td>DescribeReservedNodeExchangeStatus</td>
       <td style="text-align:right">-</td>
    </tr>
    <tr>
      <td>DescribeReservedNodeOfferings</td>
       <td style="text-align:right">-</td>
    </tr>
    <tr>
      <td>DescribeReservedNodes</td>
       <td style="text-align:right">-</td>
    </tr>
    <tr>
      <td>DescribeResize</td>
       <td style="text-align:right">-</td>
    </tr>
    <tr>
      <td>DescribeScheduledActions</td>
       <td style="text-align:right">-</td>
    </tr>
    <tr>
      <td>DescribeSnapshotSchedules</td>
       <td style="text-align:right">-</td>
    </tr>
    <tr>
      <td>DescribeStorage</td>
       <td style="text-align:right">-</td>
    </tr>
    <tr>
      <td>DescribeTableRestoreStatus</td>
       <td style="text-align:right">-</td>
    </tr>
    <tr>
      <td>DescribeUsageLimits</td>
       <td style="text-align:right">-</td>
    </tr>
    <tr>
      <td>DisableLogging</td>
       <td style="text-align:right">-</td>
    </tr>
    <tr>
      <td>DisassociateDataShareConsumer</td>
       <td style="text-align:right">-</td>
    </tr>
    <tr>
      <td>EnableLogging</td>
       <td style="text-align:right">-</td>
    </tr>
    <tr>
      <td>GetClusterCredentialsWithIAM</td>
       <td style="text-align:right">-</td>
    </tr>
    <tr>
      <td>GetReservedNodeExchangeConfigurationOptions</td>
       <td style="text-align:right">-</td>
    </tr>
    <tr>
      <td>GetReservedNodeExchangeOfferings</td>
       <td style="text-align:right">-</td>
    </tr>
    <tr>
      <td>ModifyAquaConfiguration</td>
       <td style="text-align:right">-</td>
    </tr>
    <tr>
      <td>ModifyAuthenticationProfile</td>
       <td style="text-align:right">-</td>
    </tr>
    <tr>
      <td>ModifyClusterDbRevision</td>
       <td style="text-align:right">-</td>
    </tr>
    <tr>
      <td>ModifyClusterIamRoles</td>
       <td style="text-align:right">-</td>
    </tr>
    <tr>
      <td>ModifyClusterMaintenance</td>
       <td style="text-align:right">-</td>
    </tr>
    <tr>
      <td>ModifyClusterParameterGroup</td>
       <td style="text-align:right">-</td>
    </tr>
    <tr>
      <td>ModifyClusterSnapshot</td>
       <td style="text-align:right">-</td>
    </tr>
    <tr>
      <td>ModifyClusterSnapshotSchedule</td>
       <td style="text-align:right">-</td>
    </tr>
    <tr>
      <td>ModifyClusterSubnetGroup</td>
       <td style="text-align:right">-</td>
    </tr>
    <tr>
      <td>ModifyEndpointAccess</td>
       <td style="text-align:right">-</td>
    </tr>
    <tr>
      <td>ModifyEventSubscription</td>
       <td style="text-align:right">-</td>
    </tr>
    <tr>
      <td>ModifyScheduledAction</td>
       <td style="text-align:right">-</td>
    </tr>
    <tr>
      <td>ModifySnapshotSchedule</td>
       <td style="text-align:right">-</td>
    </tr>
    <tr>
      <td>ModifyUsageLimit</td>
       <td style="text-align:right">-</td>
    </tr>
    <tr>
      <td>PurchaseReservedNodeOffering</td>
       <td style="text-align:right">-</td>
    </tr>
    <tr>
      <td>RebootCluster</td>
       <td style="text-align:right">-</td>
    </tr>
    <tr>
      <td>RejectDataShare</td>
       <td style="text-align:right">-</td>
    </tr>
    <tr>
      <td>ResetClusterParameterGroup</td>
       <td style="text-align:right">-</td>
    </tr>
    <tr>
      <td>ResizeCluster</td>
       <td style="text-align:right">-</td>
    </tr>
    <tr>
      <td>RestoreTableFromClusterSnapshot</td>
       <td style="text-align:right">-</td>
    </tr>
    <tr>
      <td>RevokeClusterSecurityGroupIngress</td>
       <td style="text-align:right">-</td>
    </tr>
    <tr>
      <td>RevokeEndpointAccess</td>
       <td style="text-align:right">-</td>
    </tr>
    <tr>
      <td>RevokeSnapshotAccess</td>
       <td style="text-align:right">-</td>
    </tr>
    <tr>
      <td>RotateEncryptionKey</td>
       <td style="text-align:right">-</td>
    </tr>
    <tr>
      <td>UpdatePartnerStatus</td>
       <td style="text-align:right">-</td>
    </tr>
  </tbody>
 </table>


## redshift-data ##

<table>
  <thead>
    <tr>
      <th>Operation</th>
      <th style="text-align:right">Implemented</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td>DescribeStatement (Pro)  <a href="#misc" title="covered by our integration test suite">✨</a></td>
       <td style="text-align:right">✅</td>
    </tr>
    <tr>
      <td>DescribeTable (Pro)  <a href="#misc" title="covered by our integration test suite">✨</a></td>
       <td style="text-align:right">✅</td>
    </tr>
    <tr>
      <td>ExecuteStatement (Pro)  <a href="#misc" title="covered by our integration test suite">✨</a></td>
       <td style="text-align:right">✅</td>
    </tr>
    <tr>
      <td>GetStatementResult (Pro)  <a href="#misc" title="covered by our integration test suite">✨</a></td>
       <td style="text-align:right">✅</td>
    </tr>
    <tr>
      <td>ListDatabases (Pro)  <a href="#misc" title="covered by our integration test suite">✨</a></td>
       <td style="text-align:right">✅</td>
    </tr>
    <tr>
      <td>ListTables (Pro)  <a href="#misc" title="covered by our integration test suite">✨</a></td>
       <td style="text-align:right">✅</td>
    </tr>
  </tbody>
  <tbody>    <tr>
      <td><a data-toggle="collapse" href=".redshift-data-notimplemented">Show missing</a></td>
      <td style="text-align:right"></td>
    </tr>
  </tbody>
  <tbody class="collapse redshift-data-notimplemented">     <tr>
      <td>BatchExecuteStatement</td>
       <td style="text-align:right">-</td>
    </tr>
    <tr>
      <td>CancelStatement</td>
       <td style="text-align:right">-</td>
    </tr>
    <tr>
      <td>ListSchemas</td>
       <td style="text-align:right">-</td>
    </tr>
    <tr>
      <td>ListStatements</td>
       <td style="text-align:right">-</td>
    </tr>
  </tbody>
 </table>


## resource-groups ##

<table>
  <thead>
    <tr>
      <th>Operation</th>
      <th style="text-align:right">Implemented</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td>CreateGroup <a href="#misc" title="covered by our integration test suite">✨</a></td>
       <td style="text-align:right">✅</td>
    </tr>
    <tr>
      <td>DeleteGroup <a href="#misc" title="covered by our integration test suite">✨</a></td>
       <td style="text-align:right">✅</td>
    </tr>
    <tr>
      <td>GetGroup <a href="#misc" title="covered by our integration test suite">✨</a></td>
       <td style="text-align:right">✅</td>
    </tr>
    <tr>
      <td>GetGroupConfiguration</td>
       <td style="text-align:right">✅</td>
    </tr>
    <tr>
      <td>GetGroupQuery</td>
       <td style="text-align:right">✅</td>
    </tr>
    <tr>
      <td>ListGroups <a href="#misc" title="covered by our integration test suite">✨</a></td>
       <td style="text-align:right">✅</td>
    </tr>
    <tr>
      <td>PutGroupConfiguration</td>
       <td style="text-align:right">✅</td>
    </tr>
    <tr>
      <td>UpdateGroup</td>
       <td style="text-align:right">✅</td>
    </tr>
    <tr>
      <td>UpdateGroupQuery</td>
       <td style="text-align:right">✅</td>
    </tr>
  </tbody>
  <tbody>    <tr>
      <td><a data-toggle="collapse" href=".resource-groups-notimplemented">Show missing</a></td>
      <td style="text-align:right"></td>
    </tr>
  </tbody>
  <tbody class="collapse resource-groups-notimplemented">     <tr>
      <td>GetTags</td>
       <td style="text-align:right">-</td>
    </tr>
    <tr>
      <td>GroupResources</td>
       <td style="text-align:right">-</td>
    </tr>
    <tr>
      <td>ListGroupResources</td>
       <td style="text-align:right">-</td>
    </tr>
    <tr>
      <td>SearchResources</td>
       <td style="text-align:right">-</td>
    </tr>
    <tr>
      <td>Tag</td>
       <td style="text-align:right">-</td>
    </tr>
    <tr>
      <td>UngroupResources</td>
       <td style="text-align:right">-</td>
    </tr>
    <tr>
      <td>Untag</td>
       <td style="text-align:right">-</td>
    </tr>
  </tbody>
 </table>


## resourcegroupstaggingapi ##

<table>
  <thead>
    <tr>
      <th>Operation</th>
      <th style="text-align:right">Implemented</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td>GetResources <a href="#misc" title="covered by our integration test suite">✨</a></td>
       <td style="text-align:right">✅</td>
    </tr>
    <tr>
      <td>GetTagKeys</td>
       <td style="text-align:right">✅</td>
    </tr>
    <tr>
      <td>GetTagValues</td>
       <td style="text-align:right">✅</td>
    </tr>
  </tbody>
  <tbody>    <tr>
      <td><a data-toggle="collapse" href=".resourcegroupstaggingapi-notimplemented">Show missing</a></td>
      <td style="text-align:right"></td>
    </tr>
  </tbody>
  <tbody class="collapse resourcegroupstaggingapi-notimplemented">     <tr>
      <td>DescribeReportCreation</td>
       <td style="text-align:right">-</td>
    </tr>
    <tr>
      <td>GetComplianceSummary</td>
       <td style="text-align:right">-</td>
    </tr>
    <tr>
      <td>StartReportCreation</td>
       <td style="text-align:right">-</td>
    </tr>
    <tr>
      <td>TagResources</td>
       <td style="text-align:right">-</td>
    </tr>
    <tr>
      <td>UntagResources</td>
       <td style="text-align:right">-</td>
    </tr>
  </tbody>
 </table>


## route53 ##

<table>
  <thead>
    <tr>
      <th>Operation</th>
      <th style="text-align:right">Implemented</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td>AssociateVPCWithHostedZone <a href="#misc" title="covered by our integration test suite">✨</a></td>
       <td style="text-align:right">✅</td>
    </tr>
    <tr>
      <td>ChangeResourceRecordSets <a href="#misc" title="covered by our integration test suite">✨</a></td>
       <td style="text-align:right">✅</td>
    </tr>
    <tr>
      <td>ChangeTagsForResource <a href="#misc" title="covered by our integration test suite">✨</a></td>
       <td style="text-align:right">✅</td>
    </tr>
    <tr>
      <td>CreateHealthCheck <a href="#misc" title="covered by our integration test suite">✨</a></td>
       <td style="text-align:right">✅</td>
    </tr>
    <tr>
      <td>CreateHostedZone <a href="#misc" title="covered by our integration test suite">✨</a></td>
       <td style="text-align:right">✅</td>
    </tr>
    <tr>
      <td>CreateQueryLoggingConfig</td>
       <td style="text-align:right">✅</td>
    </tr>
    <tr>
      <td>CreateReusableDelegationSet <a href="#misc" title="covered by our integration test suite">✨</a></td>
       <td style="text-align:right">✅</td>
    </tr>
    <tr>
      <td>DeleteHealthCheck <a href="#misc" title="covered by our integration test suite">✨</a></td>
       <td style="text-align:right">✅</td>
    </tr>
    <tr>
      <td>DeleteHostedZone <a href="#misc" title="covered by our integration test suite">✨</a></td>
       <td style="text-align:right">✅</td>
    </tr>
    <tr>
      <td>DeleteQueryLoggingConfig</td>
       <td style="text-align:right">✅</td>
    </tr>
    <tr>
      <td>DeleteReusableDelegationSet <a href="#misc" title="covered by our integration test suite">✨</a></td>
       <td style="text-align:right">✅</td>
    </tr>
    <tr>
      <td>DisassociateVPCFromHostedZone <a href="#misc" title="covered by our integration test suite">✨</a></td>
       <td style="text-align:right">✅</td>
    </tr>
    <tr>
      <td>GetChange <a href="#misc" title="covered by our integration test suite">✨</a></td>
       <td style="text-align:right">✅</td>
    </tr>
    <tr>
      <td>GetDNSSEC</td>
       <td style="text-align:right">✅</td>
    </tr>
    <tr>
      <td>GetHealthCheck <a href="#misc" title="covered by our integration test suite">✨</a></td>
       <td style="text-align:right">✅</td>
    </tr>
    <tr>
      <td>GetHostedZone <a href="#misc" title="covered by our integration test suite">✨</a></td>
       <td style="text-align:right">✅</td>
    </tr>
    <tr>
      <td>GetHostedZoneCount</td>
       <td style="text-align:right">✅</td>
    </tr>
    <tr>
      <td>GetQueryLoggingConfig</td>
       <td style="text-align:right">✅</td>
    </tr>
    <tr>
      <td>GetReusableDelegationSet <a href="#misc" title="covered by our integration test suite">✨</a></td>
       <td style="text-align:right">✅</td>
    </tr>
    <tr>
      <td>ListHealthChecks</td>
       <td style="text-align:right">✅</td>
    </tr>
    <tr>
      <td>ListHostedZones <a href="#misc" title="covered by our integration test suite">✨</a></td>
       <td style="text-align:right">✅</td>
    </tr>
    <tr>
      <td>ListHostedZonesByName <a href="#misc" title="covered by our integration test suite">✨</a></td>
       <td style="text-align:right">✅</td>
    </tr>
    <tr>
      <td>ListHostedZonesByVPC <a href="#misc" title="covered by our integration test suite">✨</a></td>
       <td style="text-align:right">✅</td>
    </tr>
    <tr>
      <td>ListQueryLoggingConfigs</td>
       <td style="text-align:right">✅</td>
    </tr>
    <tr>
      <td>ListResourceRecordSets <a href="#misc" title="covered by our integration test suite">✨</a></td>
       <td style="text-align:right">✅</td>
    </tr>
    <tr>
      <td>ListReusableDelegationSets <a href="#misc" title="covered by our integration test suite">✨</a></td>
       <td style="text-align:right">✅</td>
    </tr>
    <tr>
      <td>ListTagsForResource <a href="#misc" title="covered by our integration test suite">✨</a></td>
       <td style="text-align:right">✅</td>
    </tr>
    <tr>
      <td>UpdateHealthCheck</td>
       <td style="text-align:right">✅</td>
    </tr>
    <tr>
      <td>UpdateHostedZoneComment</td>
       <td style="text-align:right">✅</td>
    </tr>
  </tbody>
  <tbody>    <tr>
      <td><a data-toggle="collapse" href=".route53-notimplemented">Show missing</a></td>
      <td style="text-align:right"></td>
    </tr>
  </tbody>
  <tbody class="collapse route53-notimplemented">     <tr>
      <td>ActivateKeySigningKey</td>
       <td style="text-align:right">-</td>
    </tr>
    <tr>
      <td>ChangeCidrCollection</td>
       <td style="text-align:right">-</td>
    </tr>
    <tr>
      <td>CreateCidrCollection</td>
       <td style="text-align:right">-</td>
    </tr>
    <tr>
      <td>CreateKeySigningKey</td>
       <td style="text-align:right">-</td>
    </tr>
    <tr>
      <td>CreateTrafficPolicy</td>
       <td style="text-align:right">-</td>
    </tr>
    <tr>
      <td>CreateTrafficPolicyInstance</td>
       <td style="text-align:right">-</td>
    </tr>
    <tr>
      <td>CreateTrafficPolicyVersion</td>
       <td style="text-align:right">-</td>
    </tr>
    <tr>
      <td>CreateVPCAssociationAuthorization</td>
       <td style="text-align:right">-</td>
    </tr>
    <tr>
      <td>DeactivateKeySigningKey</td>
       <td style="text-align:right">-</td>
    </tr>
    <tr>
      <td>DeleteCidrCollection</td>
       <td style="text-align:right">-</td>
    </tr>
    <tr>
      <td>DeleteKeySigningKey</td>
       <td style="text-align:right">-</td>
    </tr>
    <tr>
      <td>DeleteTrafficPolicy</td>
       <td style="text-align:right">-</td>
    </tr>
    <tr>
      <td>DeleteTrafficPolicyInstance</td>
       <td style="text-align:right">-</td>
    </tr>
    <tr>
      <td>DeleteVPCAssociationAuthorization</td>
       <td style="text-align:right">-</td>
    </tr>
    <tr>
      <td>DisableHostedZoneDNSSEC</td>
       <td style="text-align:right">-</td>
    </tr>
    <tr>
      <td>EnableHostedZoneDNSSEC</td>
       <td style="text-align:right">-</td>
    </tr>
    <tr>
      <td>GetAccountLimit</td>
       <td style="text-align:right">-</td>
    </tr>
    <tr>
      <td>GetCheckerIpRanges</td>
       <td style="text-align:right">-</td>
    </tr>
    <tr>
      <td>GetGeoLocation</td>
       <td style="text-align:right">-</td>
    </tr>
    <tr>
      <td>GetHealthCheckCount</td>
       <td style="text-align:right">-</td>
    </tr>
    <tr>
      <td>GetHealthCheckLastFailureReason</td>
       <td style="text-align:right">-</td>
    </tr>
    <tr>
      <td>GetHealthCheckStatus</td>
       <td style="text-align:right">-</td>
    </tr>
    <tr>
      <td>GetHostedZoneLimit</td>
       <td style="text-align:right">-</td>
    </tr>
    <tr>
      <td>GetReusableDelegationSetLimit</td>
       <td style="text-align:right">-</td>
    </tr>
    <tr>
      <td>GetTrafficPolicy</td>
       <td style="text-align:right">-</td>
    </tr>
    <tr>
      <td>GetTrafficPolicyInstance</td>
       <td style="text-align:right">-</td>
    </tr>
    <tr>
      <td>GetTrafficPolicyInstanceCount</td>
       <td style="text-align:right">-</td>
    </tr>
    <tr>
      <td>ListCidrBlocks</td>
       <td style="text-align:right">-</td>
    </tr>
    <tr>
      <td>ListCidrCollections</td>
       <td style="text-align:right">-</td>
    </tr>
    <tr>
      <td>ListCidrLocations</td>
       <td style="text-align:right">-</td>
    </tr>
    <tr>
      <td>ListGeoLocations</td>
       <td style="text-align:right">-</td>
    </tr>
    <tr>
      <td>ListTagsForResources</td>
       <td style="text-align:right">-</td>
    </tr>
    <tr>
      <td>ListTrafficPolicies</td>
       <td style="text-align:right">-</td>
    </tr>
    <tr>
      <td>ListTrafficPolicyInstances</td>
       <td style="text-align:right">-</td>
    </tr>
    <tr>
      <td>ListTrafficPolicyInstancesByHostedZone</td>
       <td style="text-align:right">-</td>
    </tr>
    <tr>
      <td>ListTrafficPolicyInstancesByPolicy</td>
       <td style="text-align:right">-</td>
    </tr>
    <tr>
      <td>ListTrafficPolicyVersions</td>
       <td style="text-align:right">-</td>
    </tr>
    <tr>
      <td>ListVPCAssociationAuthorizations</td>
       <td style="text-align:right">-</td>
    </tr>
    <tr>
      <td>TestDNSAnswer</td>
       <td style="text-align:right">-</td>
    </tr>
    <tr>
      <td>UpdateTrafficPolicyComment</td>
       <td style="text-align:right">-</td>
    </tr>
    <tr>
      <td>UpdateTrafficPolicyInstance</td>
       <td style="text-align:right">-</td>
    </tr>
  </tbody>
 </table>


## route53resolver ##

<table>
  <thead>
    <tr>
      <th>Operation</th>
      <th style="text-align:right">Implemented</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td>AssociateFirewallRuleGroup</td>
       <td style="text-align:right">✅</td>
    </tr>
    <tr>
      <td>AssociateResolverEndpointIpAddress</td>
       <td style="text-align:right">✅</td>
    </tr>
    <tr>
      <td>AssociateResolverQueryLogConfig</td>
       <td style="text-align:right">✅</td>
    </tr>
    <tr>
      <td>AssociateResolverRule <a href="#misc" title="covered by our integration test suite">✨</a></td>
       <td style="text-align:right">✅</td>
    </tr>
    <tr>
      <td>CreateFirewallDomainList</td>
       <td style="text-align:right">✅</td>
    </tr>
    <tr>
      <td>CreateFirewallRule</td>
       <td style="text-align:right">✅</td>
    </tr>
    <tr>
      <td>CreateFirewallRuleGroup</td>
       <td style="text-align:right">✅</td>
    </tr>
    <tr>
      <td>CreateResolverEndpoint <a href="#misc" title="covered by our integration test suite">✨</a></td>
       <td style="text-align:right">✅</td>
    </tr>
    <tr>
      <td>CreateResolverQueryLogConfig <a href="#misc" title="covered by our integration test suite">✨</a></td>
       <td style="text-align:right">✅</td>
    </tr>
    <tr>
      <td>CreateResolverRule <a href="#misc" title="covered by our integration test suite">✨</a></td>
       <td style="text-align:right">✅</td>
    </tr>
    <tr>
      <td>DeleteFirewallDomainList</td>
       <td style="text-align:right">✅</td>
    </tr>
    <tr>
      <td>DeleteFirewallRule</td>
       <td style="text-align:right">✅</td>
    </tr>
    <tr>
      <td>DeleteFirewallRuleGroup</td>
       <td style="text-align:right">✅</td>
    </tr>
    <tr>
      <td>DeleteResolverEndpoint <a href="#misc" title="covered by our integration test suite">✨</a></td>
       <td style="text-align:right">✅</td>
    </tr>
    <tr>
      <td>DeleteResolverQueryLogConfig <a href="#misc" title="covered by our integration test suite">✨</a></td>
       <td style="text-align:right">✅</td>
    </tr>
    <tr>
      <td>DeleteResolverRule <a href="#misc" title="covered by our integration test suite">✨</a></td>
       <td style="text-align:right">✅</td>
    </tr>
    <tr>
      <td>DisassociateFirewallRuleGroup</td>
       <td style="text-align:right">✅</td>
    </tr>
    <tr>
      <td>DisassociateResolverEndpointIpAddress</td>
       <td style="text-align:right">✅</td>
    </tr>
    <tr>
      <td>DisassociateResolverQueryLogConfig</td>
       <td style="text-align:right">✅</td>
    </tr>
    <tr>
      <td>DisassociateResolverRule <a href="#misc" title="covered by our integration test suite">✨</a></td>
       <td style="text-align:right">✅</td>
    </tr>
    <tr>
      <td>GetFirewallConfig</td>
       <td style="text-align:right">✅</td>
    </tr>
    <tr>
      <td>GetFirewallDomainList</td>
       <td style="text-align:right">✅</td>
    </tr>
    <tr>
      <td>GetFirewallRuleGroup</td>
       <td style="text-align:right">✅</td>
    </tr>
    <tr>
      <td>GetFirewallRuleGroupAssociation</td>
       <td style="text-align:right">✅</td>
    </tr>
    <tr>
      <td>GetResolverEndpoint</td>
       <td style="text-align:right">✅</td>
    </tr>
    <tr>
      <td>GetResolverQueryLogConfig</td>
       <td style="text-align:right">✅</td>
    </tr>
    <tr>
      <td>GetResolverQueryLogConfigAssociation</td>
       <td style="text-align:right">✅</td>
    </tr>
    <tr>
      <td>GetResolverRule</td>
       <td style="text-align:right">✅</td>
    </tr>
    <tr>
      <td>GetResolverRuleAssociation</td>
       <td style="text-align:right">✅</td>
    </tr>
    <tr>
      <td>ListFirewallConfigs</td>
       <td style="text-align:right">✅</td>
    </tr>
    <tr>
      <td>ListFirewallDomainLists</td>
       <td style="text-align:right">✅</td>
    </tr>
    <tr>
      <td>ListFirewallDomains</td>
       <td style="text-align:right">✅</td>
    </tr>
    <tr>
      <td>ListFirewallRuleGroups</td>
       <td style="text-align:right">✅</td>
    </tr>
    <tr>
      <td>ListFirewallRules</td>
       <td style="text-align:right">✅</td>
    </tr>
    <tr>
      <td>ListResolverEndpointIpAddresses</td>
       <td style="text-align:right">✅</td>
    </tr>
    <tr>
      <td>ListResolverEndpoints <a href="#misc" title="covered by our integration test suite">✨</a></td>
       <td style="text-align:right">✅</td>
    </tr>
    <tr>
      <td>ListResolverQueryLogConfigAssociations</td>
       <td style="text-align:right">✅</td>
    </tr>
    <tr>
      <td>ListResolverQueryLogConfigs <a href="#misc" title="covered by our integration test suite">✨</a></td>
       <td style="text-align:right">✅</td>
    </tr>
    <tr>
      <td>ListResolverRuleAssociations <a href="#misc" title="covered by our integration test suite">✨</a></td>
       <td style="text-align:right">✅</td>
    </tr>
    <tr>
      <td>ListResolverRules</td>
       <td style="text-align:right">✅</td>
    </tr>
    <tr>
      <td>ListTagsForResource</td>
       <td style="text-align:right">✅</td>
    </tr>
    <tr>
      <td>TagResource</td>
       <td style="text-align:right">✅</td>
    </tr>
    <tr>
      <td>UntagResource</td>
       <td style="text-align:right">✅</td>
    </tr>
    <tr>
      <td>UpdateFirewallConfig</td>
       <td style="text-align:right">✅</td>
    </tr>
    <tr>
      <td>UpdateFirewallDomains</td>
       <td style="text-align:right">✅</td>
    </tr>
    <tr>
      <td>UpdateFirewallRule</td>
       <td style="text-align:right">✅</td>
    </tr>
    <tr>
      <td>UpdateFirewallRuleGroupAssociation</td>
       <td style="text-align:right">✅</td>
    </tr>
    <tr>
      <td>UpdateResolverEndpoint <a href="#misc" title="covered by our integration test suite">✨</a></td>
       <td style="text-align:right">✅</td>
    </tr>
  </tbody>
  <tbody>    <tr>
      <td><a data-toggle="collapse" href=".route53resolver-notimplemented">Show missing</a></td>
      <td style="text-align:right"></td>
    </tr>
  </tbody>
  <tbody class="collapse route53resolver-notimplemented">     <tr>
      <td>GetFirewallRuleGroupPolicy</td>
       <td style="text-align:right">-</td>
    </tr>
    <tr>
      <td>GetResolverConfig</td>
       <td style="text-align:right">-</td>
    </tr>
    <tr>
      <td>GetResolverDnssecConfig</td>
       <td style="text-align:right">-</td>
    </tr>
    <tr>
      <td>GetResolverQueryLogConfigPolicy</td>
       <td style="text-align:right">-</td>
    </tr>
    <tr>
      <td>GetResolverRulePolicy</td>
       <td style="text-align:right">-</td>
    </tr>
    <tr>
      <td>ImportFirewallDomains</td>
       <td style="text-align:right">-</td>
    </tr>
    <tr>
      <td>ListFirewallRuleGroupAssociations</td>
       <td style="text-align:right">-</td>
    </tr>
    <tr>
      <td>ListResolverConfigs</td>
       <td style="text-align:right">-</td>
    </tr>
    <tr>
      <td>ListResolverDnssecConfigs</td>
       <td style="text-align:right">-</td>
    </tr>
    <tr>
      <td>PutFirewallRuleGroupPolicy</td>
       <td style="text-align:right">-</td>
    </tr>
    <tr>
      <td>PutResolverQueryLogConfigPolicy</td>
       <td style="text-align:right">-</td>
    </tr>
    <tr>
      <td>PutResolverRulePolicy</td>
       <td style="text-align:right">-</td>
    </tr>
    <tr>
      <td>UpdateResolverConfig</td>
       <td style="text-align:right">-</td>
    </tr>
    <tr>
      <td>UpdateResolverDnssecConfig</td>
       <td style="text-align:right">-</td>
    </tr>
    <tr>
      <td>UpdateResolverRule</td>
       <td style="text-align:right">-</td>
    </tr>
  </tbody>
 </table>


## s3 ##

<table>
  <thead>
    <tr>
      <th>Operation</th>
      <th style="text-align:right">Implemented</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td>AbortMultipartUpload</td>
       <td style="text-align:right">✅</td>
    </tr>
    <tr>
      <td>CompleteMultipartUpload <a href="#misc" title="covered by our integration test suite">✨</a></td>
       <td style="text-align:right">✅</td>
    </tr>
    <tr>
      <td>CopyObject <a href="#misc" title="covered by our integration test suite">✨</a></td>
       <td style="text-align:right">✅</td>
    </tr>
    <tr>
      <td>CreateBucket <a href="#misc" title="covered by our integration test suite">✨</a></td>
       <td style="text-align:right">✅</td>
    </tr>
    <tr>
      <td>CreateMultipartUpload <a href="#misc" title="covered by our integration test suite">✨</a></td>
       <td style="text-align:right">✅</td>
    </tr>
    <tr>
      <td>DeleteBucket <a href="#misc" title="covered by our integration test suite">✨</a></td>
       <td style="text-align:right">✅</td>
    </tr>
    <tr>
      <td>DeleteBucketAnalyticsConfiguration</td>
       <td style="text-align:right">✅</td>
    </tr>
    <tr>
      <td>DeleteBucketCors</td>
       <td style="text-align:right">✅</td>
    </tr>
    <tr>
      <td>DeleteBucketEncryption</td>
       <td style="text-align:right">✅</td>
    </tr>
    <tr>
      <td>DeleteBucketIntelligentTieringConfiguration</td>
       <td style="text-align:right">✅</td>
    </tr>
    <tr>
      <td>DeleteBucketInventoryConfiguration</td>
       <td style="text-align:right">✅</td>
    </tr>
    <tr>
      <td>DeleteBucketLifecycle <a href="#misc" title="covered by our integration test suite">✨</a></td>
       <td style="text-align:right">✅</td>
    </tr>
    <tr>
      <td>DeleteBucketMetricsConfiguration</td>
       <td style="text-align:right">✅</td>
    </tr>
    <tr>
      <td>DeleteBucketOwnershipControls</td>
       <td style="text-align:right">✅</td>
    </tr>
    <tr>
      <td>DeleteBucketPolicy <a href="#misc" title="covered by our integration test suite">✨</a></td>
       <td style="text-align:right">✅</td>
    </tr>
    <tr>
      <td>DeleteBucketReplication</td>
       <td style="text-align:right">✅</td>
    </tr>
    <tr>
      <td>DeleteBucketTagging</td>
       <td style="text-align:right">✅</td>
    </tr>
    <tr>
      <td>DeleteBucketWebsite <a href="#misc" title="covered by our integration test suite">✨</a></td>
       <td style="text-align:right">✅</td>
    </tr>
    <tr>
      <td>DeleteObject <a href="#misc" title="covered by our integration test suite">✨</a></td>
       <td style="text-align:right">✅</td>
    </tr>
    <tr>
      <td>DeleteObjectTagging <a href="#misc" title="covered by our integration test suite">✨</a></td>
       <td style="text-align:right">✅</td>
    </tr>
    <tr>
      <td>DeleteObjects <a href="#misc" title="covered by our integration test suite">✨</a></td>
       <td style="text-align:right">✅</td>
    </tr>
    <tr>
      <td>DeletePublicAccessBlock</td>
       <td style="text-align:right">✅</td>
    </tr>
    <tr>
      <td>GetBucketAccelerateConfiguration <a href="#misc" title="covered by our integration test suite">✨</a></td>
       <td style="text-align:right">✅</td>
    </tr>
    <tr>
      <td>GetBucketAcl <a href="#misc" title="covered by our integration test suite">✨</a></td>
       <td style="text-align:right">✅</td>
    </tr>
    <tr>
      <td>GetBucketAnalyticsConfiguration</td>
       <td style="text-align:right">✅</td>
    </tr>
    <tr>
      <td>GetBucketCors <a href="#misc" title="covered by our integration test suite">✨</a></td>
       <td style="text-align:right">✅</td>
    </tr>
    <tr>
      <td>GetBucketEncryption <a href="#misc" title="covered by our integration test suite">✨</a></td>
       <td style="text-align:right">✅</td>
    </tr>
    <tr>
      <td>GetBucketIntelligentTieringConfiguration</td>
       <td style="text-align:right">✅</td>
    </tr>
    <tr>
      <td>GetBucketInventoryConfiguration</td>
       <td style="text-align:right">✅</td>
    </tr>
    <tr>
      <td>GetBucketLifecycle</td>
       <td style="text-align:right">✅</td>
    </tr>
    <tr>
      <td>GetBucketLifecycleConfiguration <a href="#misc" title="covered by our integration test suite">✨</a></td>
       <td style="text-align:right">✅</td>
    </tr>
    <tr>
      <td>GetBucketLocation <a href="#misc" title="covered by our integration test suite">✨</a></td>
       <td style="text-align:right">✅</td>
    </tr>
    <tr>
      <td>GetBucketLogging <a href="#misc" title="covered by our integration test suite">✨</a></td>
       <td style="text-align:right">✅</td>
    </tr>
    <tr>
      <td>GetBucketMetricsConfiguration</td>
       <td style="text-align:right">✅</td>
    </tr>
    <tr>
      <td>GetBucketNotification</td>
       <td style="text-align:right">✅</td>
    </tr>
    <tr>
      <td>GetBucketNotificationConfiguration <a href="#misc" title="covered by our integration test suite">✨</a></td>
       <td style="text-align:right">✅</td>
    </tr>
    <tr>
      <td>GetBucketOwnershipControls</td>
       <td style="text-align:right">✅</td>
    </tr>
    <tr>
      <td>GetBucketPolicy <a href="#misc" title="covered by our integration test suite">✨</a></td>
       <td style="text-align:right">✅</td>
    </tr>
    <tr>
      <td>GetBucketPolicyStatus</td>
       <td style="text-align:right">✅</td>
    </tr>
    <tr>
      <td>GetBucketReplication <a href="#misc" title="covered by our integration test suite">✨</a></td>
       <td style="text-align:right">✅</td>
    </tr>
    <tr>
      <td>GetBucketRequestPayment <a href="#misc" title="covered by our integration test suite">✨</a></td>
       <td style="text-align:right">✅</td>
    </tr>
    <tr>
      <td>GetBucketTagging <a href="#misc" title="covered by our integration test suite">✨</a></td>
       <td style="text-align:right">✅</td>
    </tr>
    <tr>
      <td>GetBucketVersioning <a href="#misc" title="covered by our integration test suite">✨</a></td>
       <td style="text-align:right">✅</td>
    </tr>
    <tr>
      <td>GetBucketWebsite <a href="#misc" title="covered by our integration test suite">✨</a></td>
       <td style="text-align:right">✅</td>
    </tr>
    <tr>
      <td>GetObject <a href="#misc" title="covered by our integration test suite">✨</a></td>
       <td style="text-align:right">✅</td>
    </tr>
    <tr>
      <td>GetObjectAcl</td>
       <td style="text-align:right">✅</td>
    </tr>
    <tr>
      <td>GetObjectAttributes</td>
       <td style="text-align:right">✅</td>
    </tr>
    <tr>
      <td>GetObjectLegalHold</td>
       <td style="text-align:right">✅</td>
    </tr>
    <tr>
      <td>GetObjectLockConfiguration <a href="#misc" title="covered by our integration test suite">✨</a></td>
       <td style="text-align:right">✅</td>
    </tr>
    <tr>
      <td>GetObjectRetention</td>
       <td style="text-align:right">✅</td>
    </tr>
    <tr>
      <td>GetObjectTagging</td>
       <td style="text-align:right">✅</td>
    </tr>
    <tr>
      <td>GetObjectTorrent</td>
       <td style="text-align:right">✅</td>
    </tr>
    <tr>
      <td>GetPublicAccessBlock <a href="#misc" title="covered by our integration test suite">✨</a></td>
       <td style="text-align:right">✅</td>
    </tr>
    <tr>
      <td>HeadBucket <a href="#misc" title="covered by our integration test suite">✨</a></td>
       <td style="text-align:right">✅</td>
    </tr>
    <tr>
      <td>HeadObject <a href="#misc" title="covered by our integration test suite">✨</a></td>
       <td style="text-align:right">✅</td>
    </tr>
    <tr>
      <td>ListBucketAnalyticsConfigurations</td>
       <td style="text-align:right">✅</td>
    </tr>
    <tr>
      <td>ListBucketIntelligentTieringConfigurations</td>
       <td style="text-align:right">✅</td>
    </tr>
    <tr>
      <td>ListBucketInventoryConfigurations</td>
       <td style="text-align:right">✅</td>
    </tr>
    <tr>
      <td>ListBucketMetricsConfigurations</td>
       <td style="text-align:right">✅</td>
    </tr>
    <tr>
      <td>ListBuckets <a href="#misc" title="covered by our integration test suite">✨</a></td>
       <td style="text-align:right">✅</td>
    </tr>
    <tr>
      <td>ListMultipartUploads</td>
       <td style="text-align:right">✅</td>
    </tr>
    <tr>
      <td>ListObjectVersions <a href="#misc" title="covered by our integration test suite">✨</a></td>
       <td style="text-align:right">✅</td>
    </tr>
    <tr>
      <td>ListObjects <a href="#misc" title="covered by our integration test suite">✨</a></td>
       <td style="text-align:right">✅</td>
    </tr>
    <tr>
      <td>ListObjectsV2 <a href="#misc" title="covered by our integration test suite">✨</a></td>
       <td style="text-align:right">✅</td>
    </tr>
    <tr>
      <td>ListParts <a href="#misc" title="covered by our integration test suite">✨</a></td>
       <td style="text-align:right">✅</td>
    </tr>
    <tr>
      <td>PostObject <a href="#misc" title="covered by our integration test suite">✨</a></td>
       <td style="text-align:right">✅</td>
    </tr>
    <tr>
      <td>PutBucketAccelerateConfiguration</td>
       <td style="text-align:right">✅</td>
    </tr>
    <tr>
      <td>PutBucketAcl <a href="#misc" title="covered by our integration test suite">✨</a></td>
       <td style="text-align:right">✅</td>
    </tr>
    <tr>
      <td>PutBucketAnalyticsConfiguration</td>
       <td style="text-align:right">✅</td>
    </tr>
    <tr>
      <td>PutBucketCors <a href="#misc" title="covered by our integration test suite">✨</a></td>
       <td style="text-align:right">✅</td>
    </tr>
    <tr>
      <td>PutBucketEncryption</td>
       <td style="text-align:right">✅</td>
    </tr>
    <tr>
      <td>PutBucketIntelligentTieringConfiguration</td>
       <td style="text-align:right">✅</td>
    </tr>
    <tr>
      <td>PutBucketInventoryConfiguration</td>
       <td style="text-align:right">✅</td>
    </tr>
    <tr>
      <td>PutBucketLifecycle</td>
       <td style="text-align:right">✅</td>
    </tr>
    <tr>
      <td>PutBucketLifecycleConfiguration <a href="#misc" title="covered by our integration test suite">✨</a></td>
       <td style="text-align:right">✅</td>
    </tr>
    <tr>
      <td>PutBucketLogging</td>
       <td style="text-align:right">✅</td>
    </tr>
    <tr>
      <td>PutBucketMetricsConfiguration</td>
       <td style="text-align:right">✅</td>
    </tr>
    <tr>
      <td>PutBucketNotification</td>
       <td style="text-align:right">✅</td>
    </tr>
    <tr>
      <td>PutBucketNotificationConfiguration <a href="#misc" title="covered by our integration test suite">✨</a></td>
       <td style="text-align:right">✅</td>
    </tr>
    <tr>
      <td>PutBucketOwnershipControls</td>
       <td style="text-align:right">✅</td>
    </tr>
    <tr>
      <td>PutBucketPolicy <a href="#misc" title="covered by our integration test suite">✨</a></td>
       <td style="text-align:right">✅</td>
    </tr>
    <tr>
      <td>PutBucketReplication</td>
       <td style="text-align:right">✅</td>
    </tr>
    <tr>
      <td>PutBucketRequestPayment <a href="#misc" title="covered by our integration test suite">✨</a></td>
       <td style="text-align:right">✅</td>
    </tr>
    <tr>
      <td>PutBucketTagging <a href="#misc" title="covered by our integration test suite">✨</a></td>
       <td style="text-align:right">✅</td>
    </tr>
    <tr>
      <td>PutBucketVersioning <a href="#misc" title="covered by our integration test suite">✨</a></td>
       <td style="text-align:right">✅</td>
    </tr>
    <tr>
      <td>PutBucketWebsite <a href="#misc" title="covered by our integration test suite">✨</a></td>
       <td style="text-align:right">✅</td>
    </tr>
    <tr>
      <td>PutObject <a href="#misc" title="covered by our integration test suite">✨</a></td>
       <td style="text-align:right">✅</td>
    </tr>
    <tr>
      <td>PutObjectAcl <a href="#misc" title="covered by our integration test suite">✨</a></td>
       <td style="text-align:right">✅</td>
    </tr>
    <tr>
      <td>PutObjectLegalHold</td>
       <td style="text-align:right">✅</td>
    </tr>
    <tr>
      <td>PutObjectLockConfiguration</td>
       <td style="text-align:right">✅</td>
    </tr>
    <tr>
      <td>PutObjectRetention</td>
       <td style="text-align:right">✅</td>
    </tr>
    <tr>
      <td>PutObjectTagging <a href="#misc" title="covered by our integration test suite">✨</a></td>
       <td style="text-align:right">✅</td>
    </tr>
    <tr>
      <td>PutPublicAccessBlock</td>
       <td style="text-align:right">✅</td>
    </tr>
    <tr>
      <td>RestoreObject <a href="#misc" title="covered by our integration test suite">✨</a></td>
       <td style="text-align:right">✅</td>
    </tr>
    <tr>
      <td>SelectObjectContent <a href="#misc" title="covered by our integration test suite">✨</a></td>
       <td style="text-align:right">✅</td>
    </tr>
    <tr>
      <td>UploadPart <a href="#misc" title="covered by our integration test suite">✨</a></td>
       <td style="text-align:right">✅</td>
    </tr>
    <tr>
      <td>UploadPartCopy</td>
       <td style="text-align:right">✅</td>
    </tr>
    <tr>
      <td>WriteGetObjectResponse</td>
       <td style="text-align:right">✅</td>
    </tr>
  </tbody>
 </table>


## s3control ##

<table>
  <thead>
    <tr>
      <th>Operation</th>
      <th style="text-align:right">Implemented</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td>CreateAccessPoint</td>
       <td style="text-align:right">✅</td>
    </tr>
    <tr>
      <td>CreateBucket</td>
       <td style="text-align:right">✅</td>
    </tr>
    <tr>
      <td>CreateJob</td>
       <td style="text-align:right">✅</td>
    </tr>
    <tr>
      <td>DeleteAccessPoint</td>
       <td style="text-align:right">✅</td>
    </tr>
    <tr>
      <td>DeleteAccessPointPolicy</td>
       <td style="text-align:right">✅</td>
    </tr>
    <tr>
      <td>DeletePublicAccessBlock <a href="#misc" title="covered by our integration test suite">✨</a></td>
       <td style="text-align:right">✅</td>
    </tr>
    <tr>
      <td>GetAccessPoint</td>
       <td style="text-align:right">✅</td>
    </tr>
    <tr>
      <td>GetAccessPointPolicy</td>
       <td style="text-align:right">✅</td>
    </tr>
    <tr>
      <td>GetAccessPointPolicyStatus</td>
       <td style="text-align:right">✅</td>
    </tr>
    <tr>
      <td>GetPublicAccessBlock <a href="#misc" title="covered by our integration test suite">✨</a></td>
       <td style="text-align:right">✅</td>
    </tr>
    <tr>
      <td>ListRegionalBuckets</td>
       <td style="text-align:right">✅</td>
    </tr>
    <tr>
      <td>PutAccessPointPolicy</td>
       <td style="text-align:right">✅</td>
    </tr>
    <tr>
      <td>PutPublicAccessBlock <a href="#misc" title="covered by our integration test suite">✨</a></td>
       <td style="text-align:right">✅</td>
    </tr>
    <tr>
      <td>PutStorageLensConfiguration</td>
       <td style="text-align:right">✅</td>
    </tr>
  </tbody>
  <tbody>    <tr>
      <td><a data-toggle="collapse" href=".s3control-notimplemented">Show missing</a></td>
      <td style="text-align:right"></td>
    </tr>
  </tbody>
  <tbody class="collapse s3control-notimplemented">     <tr>
      <td>CreateAccessPointForObjectLambda</td>
       <td style="text-align:right">-</td>
    </tr>
    <tr>
      <td>CreateMultiRegionAccessPoint</td>
       <td style="text-align:right">-</td>
    </tr>
    <tr>
      <td>DeleteAccessPointForObjectLambda</td>
       <td style="text-align:right">-</td>
    </tr>
    <tr>
      <td>DeleteAccessPointPolicyForObjectLambda</td>
       <td style="text-align:right">-</td>
    </tr>
    <tr>
      <td>DeleteBucket</td>
       <td style="text-align:right">-</td>
    </tr>
    <tr>
      <td>DeleteBucketLifecycleConfiguration</td>
       <td style="text-align:right">-</td>
    </tr>
    <tr>
      <td>DeleteBucketPolicy</td>
       <td style="text-align:right">-</td>
    </tr>
    <tr>
      <td>DeleteBucketTagging</td>
       <td style="text-align:right">-</td>
    </tr>
    <tr>
      <td>DeleteJobTagging</td>
       <td style="text-align:right">-</td>
    </tr>
    <tr>
      <td>DeleteMultiRegionAccessPoint</td>
       <td style="text-align:right">-</td>
    </tr>
    <tr>
      <td>DeleteStorageLensConfiguration</td>
       <td style="text-align:right">-</td>
    </tr>
    <tr>
      <td>DeleteStorageLensConfigurationTagging</td>
       <td style="text-align:right">-</td>
    </tr>
    <tr>
      <td>DescribeJob</td>
       <td style="text-align:right">-</td>
    </tr>
    <tr>
      <td>DescribeMultiRegionAccessPointOperation</td>
       <td style="text-align:right">-</td>
    </tr>
    <tr>
      <td>GetAccessPointConfigurationForObjectLambda</td>
       <td style="text-align:right">-</td>
    </tr>
    <tr>
      <td>GetAccessPointForObjectLambda</td>
       <td style="text-align:right">-</td>
    </tr>
    <tr>
      <td>GetAccessPointPolicyForObjectLambda</td>
       <td style="text-align:right">-</td>
    </tr>
    <tr>
      <td>GetAccessPointPolicyStatusForObjectLambda</td>
       <td style="text-align:right">-</td>
    </tr>
    <tr>
      <td>GetBucket</td>
       <td style="text-align:right">-</td>
    </tr>
    <tr>
      <td>GetBucketLifecycleConfiguration</td>
       <td style="text-align:right">-</td>
    </tr>
    <tr>
      <td>GetBucketPolicy</td>
       <td style="text-align:right">-</td>
    </tr>
    <tr>
      <td>GetBucketTagging</td>
       <td style="text-align:right">-</td>
    </tr>
    <tr>
      <td>GetBucketVersioning</td>
       <td style="text-align:right">-</td>
    </tr>
    <tr>
      <td>GetJobTagging</td>
       <td style="text-align:right">-</td>
    </tr>
    <tr>
      <td>GetMultiRegionAccessPoint</td>
       <td style="text-align:right">-</td>
    </tr>
    <tr>
      <td>GetMultiRegionAccessPointPolicy</td>
       <td style="text-align:right">-</td>
    </tr>
    <tr>
      <td>GetMultiRegionAccessPointPolicyStatus</td>
       <td style="text-align:right">-</td>
    </tr>
    <tr>
      <td>GetStorageLensConfiguration</td>
       <td style="text-align:right">-</td>
    </tr>
    <tr>
      <td>GetStorageLensConfigurationTagging</td>
       <td style="text-align:right">-</td>
    </tr>
    <tr>
      <td>ListAccessPoints</td>
       <td style="text-align:right">-</td>
    </tr>
    <tr>
      <td>ListAccessPointsForObjectLambda</td>
       <td style="text-align:right">-</td>
    </tr>
    <tr>
      <td>ListJobs</td>
       <td style="text-align:right">-</td>
    </tr>
    <tr>
      <td>ListMultiRegionAccessPoints</td>
       <td style="text-align:right">-</td>
    </tr>
    <tr>
      <td>ListStorageLensConfigurations</td>
       <td style="text-align:right">-</td>
    </tr>
    <tr>
      <td>PutAccessPointConfigurationForObjectLambda</td>
       <td style="text-align:right">-</td>
    </tr>
    <tr>
      <td>PutAccessPointPolicyForObjectLambda</td>
       <td style="text-align:right">-</td>
    </tr>
    <tr>
      <td>PutBucketLifecycleConfiguration</td>
       <td style="text-align:right">-</td>
    </tr>
    <tr>
      <td>PutBucketPolicy</td>
       <td style="text-align:right">-</td>
    </tr>
    <tr>
      <td>PutBucketTagging</td>
       <td style="text-align:right">-</td>
    </tr>
    <tr>
      <td>PutBucketVersioning</td>
       <td style="text-align:right">-</td>
    </tr>
    <tr>
      <td>PutJobTagging</td>
       <td style="text-align:right">-</td>
    </tr>
    <tr>
      <td>PutMultiRegionAccessPointPolicy</td>
       <td style="text-align:right">-</td>
    </tr>
    <tr>
      <td>PutStorageLensConfigurationTagging</td>
       <td style="text-align:right">-</td>
    </tr>
    <tr>
      <td>UpdateJobPriority</td>
       <td style="text-align:right">-</td>
    </tr>
    <tr>
      <td>UpdateJobStatus</td>
       <td style="text-align:right">-</td>
    </tr>
  </tbody>
 </table>


## sagemaker ##

<table>
  <thead>
    <tr>
      <th>Operation</th>
      <th style="text-align:right">Implemented</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td>AddTags (Pro) </td>
       <td style="text-align:right">✅</td>
    </tr>
    <tr>
      <td>AssociateTrialComponent (Pro) </td>
       <td style="text-align:right">✅</td>
    </tr>
    <tr>
      <td>CreateEndpoint (Pro) </td>
       <td style="text-align:right">✅</td>
    </tr>
    <tr>
      <td>CreateEndpointConfig (Pro) </td>
       <td style="text-align:right">✅</td>
    </tr>
    <tr>
      <td>CreateExperiment (Pro) </td>
       <td style="text-align:right">✅</td>
    </tr>
    <tr>
      <td>CreateModel (Pro) </td>
       <td style="text-align:right">✅</td>
    </tr>
    <tr>
      <td>CreateNotebookInstance (Pro) </td>
       <td style="text-align:right">✅</td>
    </tr>
    <tr>
      <td>CreateNotebookInstanceLifecycleConfig (Pro) </td>
       <td style="text-align:right">✅</td>
    </tr>
    <tr>
      <td>CreateProcessingJob (Pro) </td>
       <td style="text-align:right">✅</td>
    </tr>
    <tr>
      <td>CreateTrainingJob (Pro) </td>
       <td style="text-align:right">✅</td>
    </tr>
    <tr>
      <td>CreateTrial (Pro) </td>
       <td style="text-align:right">✅</td>
    </tr>
    <tr>
      <td>CreateTrialComponent (Pro) </td>
       <td style="text-align:right">✅</td>
    </tr>
    <tr>
      <td>DeleteEndpoint (Pro) </td>
       <td style="text-align:right">✅</td>
    </tr>
    <tr>
      <td>DeleteEndpointConfig (Pro) </td>
       <td style="text-align:right">✅</td>
    </tr>
    <tr>
      <td>DeleteExperiment (Pro) </td>
       <td style="text-align:right">✅</td>
    </tr>
    <tr>
      <td>DeleteModel (Pro) </td>
       <td style="text-align:right">✅</td>
    </tr>
    <tr>
      <td>DeleteNotebookInstance (Pro) </td>
       <td style="text-align:right">✅</td>
    </tr>
    <tr>
      <td>DeleteNotebookInstanceLifecycleConfig (Pro) </td>
       <td style="text-align:right">✅</td>
    </tr>
    <tr>
      <td>DeleteTags (Pro) </td>
       <td style="text-align:right">✅</td>
    </tr>
    <tr>
      <td>DeleteTrial (Pro) </td>
       <td style="text-align:right">✅</td>
    </tr>
    <tr>
      <td>DeleteTrialComponent (Pro) </td>
       <td style="text-align:right">✅</td>
    </tr>
    <tr>
      <td>DescribeEndpoint (Pro) </td>
       <td style="text-align:right">✅</td>
    </tr>
    <tr>
      <td>DescribeEndpointConfig (Pro) </td>
       <td style="text-align:right">✅</td>
    </tr>
    <tr>
      <td>DescribeExperiment (Pro) </td>
       <td style="text-align:right">✅</td>
    </tr>
    <tr>
      <td>DescribeModel (Pro) </td>
       <td style="text-align:right">✅</td>
    </tr>
    <tr>
      <td>DescribeNotebookInstance (Pro) </td>
       <td style="text-align:right">✅</td>
    </tr>
    <tr>
      <td>DescribeNotebookInstanceLifecycleConfig (Pro) </td>
       <td style="text-align:right">✅</td>
    </tr>
    <tr>
      <td>DescribeProcessingJob (Pro) </td>
       <td style="text-align:right">✅</td>
    </tr>
    <tr>
      <td>DescribeTrainingJob (Pro) </td>
       <td style="text-align:right">✅</td>
    </tr>
    <tr>
      <td>DescribeTrial (Pro) </td>
       <td style="text-align:right">✅</td>
    </tr>
    <tr>
      <td>DescribeTrialComponent (Pro) </td>
       <td style="text-align:right">✅</td>
    </tr>
    <tr>
      <td>DisassociateTrialComponent (Pro) </td>
       <td style="text-align:right">✅</td>
    </tr>
    <tr>
      <td>ListAssociations (Pro) </td>
       <td style="text-align:right">✅</td>
    </tr>
    <tr>
      <td>ListEndpointConfigs (Pro) </td>
       <td style="text-align:right">✅</td>
    </tr>
    <tr>
      <td>ListEndpoints (Pro) </td>
       <td style="text-align:right">✅</td>
    </tr>
    <tr>
      <td>ListExperiments (Pro) </td>
       <td style="text-align:right">✅</td>
    </tr>
    <tr>
      <td>ListModels (Pro) </td>
       <td style="text-align:right">✅</td>
    </tr>
    <tr>
      <td>ListProcessingJobs (Pro) </td>
       <td style="text-align:right">✅</td>
    </tr>
    <tr>
      <td>ListTags (Pro) </td>
       <td style="text-align:right">✅</td>
    </tr>
    <tr>
      <td>ListTrainingJobs (Pro) </td>
       <td style="text-align:right">✅</td>
    </tr>
    <tr>
      <td>ListTrialComponents (Pro) </td>
       <td style="text-align:right">✅</td>
    </tr>
    <tr>
      <td>ListTrials (Pro) </td>
       <td style="text-align:right">✅</td>
    </tr>
    <tr>
      <td>Search (Pro) </td>
       <td style="text-align:right">✅</td>
    </tr>
    <tr>
      <td>StartNotebookInstance (Pro) </td>
       <td style="text-align:right">✅</td>
    </tr>
    <tr>
      <td>StopNotebookInstance (Pro) </td>
       <td style="text-align:right">✅</td>
    </tr>
    <tr>
      <td>UpdateEndpointWeightsAndCapacities (Pro) </td>
       <td style="text-align:right">✅</td>
    </tr>
  </tbody>
  <tbody>    <tr>
      <td><a data-toggle="collapse" href=".sagemaker-notimplemented">Show missing</a></td>
      <td style="text-align:right"></td>
    </tr>
  </tbody>
  <tbody class="collapse sagemaker-notimplemented">     <tr>
      <td>AddAssociation</td>
       <td style="text-align:right">-</td>
    </tr>
    <tr>
      <td>BatchDescribeModelPackage</td>
       <td style="text-align:right">-</td>
    </tr>
    <tr>
      <td>CreateAction</td>
       <td style="text-align:right">-</td>
    </tr>
    <tr>
      <td>CreateAlgorithm</td>
       <td style="text-align:right">-</td>
    </tr>
    <tr>
      <td>CreateApp</td>
       <td style="text-align:right">-</td>
    </tr>
    <tr>
      <td>CreateAppImageConfig</td>
       <td style="text-align:right">-</td>
    </tr>
    <tr>
      <td>CreateArtifact</td>
       <td style="text-align:right">-</td>
    </tr>
    <tr>
      <td>CreateAutoMLJob</td>
       <td style="text-align:right">-</td>
    </tr>
    <tr>
      <td>CreateCodeRepository</td>
       <td style="text-align:right">-</td>
    </tr>
    <tr>
      <td>CreateCompilationJob</td>
       <td style="text-align:right">-</td>
    </tr>
    <tr>
      <td>CreateContext</td>
       <td style="text-align:right">-</td>
    </tr>
    <tr>
      <td>CreateDataQualityJobDefinition</td>
       <td style="text-align:right">-</td>
    </tr>
    <tr>
      <td>CreateDeviceFleet</td>
       <td style="text-align:right">-</td>
    </tr>
    <tr>
      <td>CreateDomain</td>
       <td style="text-align:right">-</td>
    </tr>
    <tr>
      <td>CreateEdgeDeploymentPlan</td>
       <td style="text-align:right">-</td>
    </tr>
    <tr>
      <td>CreateEdgeDeploymentStage</td>
       <td style="text-align:right">-</td>
    </tr>
    <tr>
      <td>CreateEdgePackagingJob</td>
       <td style="text-align:right">-</td>
    </tr>
    <tr>
      <td>CreateFeatureGroup</td>
       <td style="text-align:right">-</td>
    </tr>
    <tr>
      <td>CreateFlowDefinition</td>
       <td style="text-align:right">-</td>
    </tr>
    <tr>
      <td>CreateHumanTaskUi</td>
       <td style="text-align:right">-</td>
    </tr>
    <tr>
      <td>CreateHyperParameterTuningJob</td>
       <td style="text-align:right">-</td>
    </tr>
    <tr>
      <td>CreateImage</td>
       <td style="text-align:right">-</td>
    </tr>
    <tr>
      <td>CreateImageVersion</td>
       <td style="text-align:right">-</td>
    </tr>
    <tr>
      <td>CreateInferenceRecommendationsJob</td>
       <td style="text-align:right">-</td>
    </tr>
    <tr>
      <td>CreateLabelingJob</td>
       <td style="text-align:right">-</td>
    </tr>
    <tr>
      <td>CreateModelBiasJobDefinition</td>
       <td style="text-align:right">-</td>
    </tr>
    <tr>
      <td>CreateModelExplainabilityJobDefinition</td>
       <td style="text-align:right">-</td>
    </tr>
    <tr>
      <td>CreateModelPackage</td>
       <td style="text-align:right">-</td>
    </tr>
    <tr>
      <td>CreateModelPackageGroup</td>
       <td style="text-align:right">-</td>
    </tr>
    <tr>
      <td>CreateModelQualityJobDefinition</td>
       <td style="text-align:right">-</td>
    </tr>
    <tr>
      <td>CreateMonitoringSchedule</td>
       <td style="text-align:right">-</td>
    </tr>
    <tr>
      <td>CreatePipeline</td>
       <td style="text-align:right">-</td>
    </tr>
    <tr>
      <td>CreatePresignedDomainUrl</td>
       <td style="text-align:right">-</td>
    </tr>
    <tr>
      <td>CreatePresignedNotebookInstanceUrl</td>
       <td style="text-align:right">-</td>
    </tr>
    <tr>
      <td>CreateProject</td>
       <td style="text-align:right">-</td>
    </tr>
    <tr>
      <td>CreateStudioLifecycleConfig</td>
       <td style="text-align:right">-</td>
    </tr>
    <tr>
      <td>CreateTransformJob</td>
       <td style="text-align:right">-</td>
    </tr>
    <tr>
      <td>CreateUserProfile</td>
       <td style="text-align:right">-</td>
    </tr>
    <tr>
      <td>CreateWorkforce</td>
       <td style="text-align:right">-</td>
    </tr>
    <tr>
      <td>CreateWorkteam</td>
       <td style="text-align:right">-</td>
    </tr>
    <tr>
      <td>DeleteAction</td>
       <td style="text-align:right">-</td>
    </tr>
    <tr>
      <td>DeleteAlgorithm</td>
       <td style="text-align:right">-</td>
    </tr>
    <tr>
      <td>DeleteApp</td>
       <td style="text-align:right">-</td>
    </tr>
    <tr>
      <td>DeleteAppImageConfig</td>
       <td style="text-align:right">-</td>
    </tr>
    <tr>
      <td>DeleteArtifact</td>
       <td style="text-align:right">-</td>
    </tr>
    <tr>
      <td>DeleteAssociation</td>
       <td style="text-align:right">-</td>
    </tr>
    <tr>
      <td>DeleteCodeRepository</td>
       <td style="text-align:right">-</td>
    </tr>
    <tr>
      <td>DeleteContext</td>
       <td style="text-align:right">-</td>
    </tr>
    <tr>
      <td>DeleteDataQualityJobDefinition</td>
       <td style="text-align:right">-</td>
    </tr>
    <tr>
      <td>DeleteDeviceFleet</td>
       <td style="text-align:right">-</td>
    </tr>
    <tr>
      <td>DeleteDomain</td>
       <td style="text-align:right">-</td>
    </tr>
    <tr>
      <td>DeleteEdgeDeploymentPlan</td>
       <td style="text-align:right">-</td>
    </tr>
    <tr>
      <td>DeleteEdgeDeploymentStage</td>
       <td style="text-align:right">-</td>
    </tr>
    <tr>
      <td>DeleteFeatureGroup</td>
       <td style="text-align:right">-</td>
    </tr>
    <tr>
      <td>DeleteFlowDefinition</td>
       <td style="text-align:right">-</td>
    </tr>
    <tr>
      <td>DeleteHumanTaskUi</td>
       <td style="text-align:right">-</td>
    </tr>
    <tr>
      <td>DeleteImage</td>
       <td style="text-align:right">-</td>
    </tr>
    <tr>
      <td>DeleteImageVersion</td>
       <td style="text-align:right">-</td>
    </tr>
    <tr>
      <td>DeleteModelBiasJobDefinition</td>
       <td style="text-align:right">-</td>
    </tr>
    <tr>
      <td>DeleteModelExplainabilityJobDefinition</td>
       <td style="text-align:right">-</td>
    </tr>
    <tr>
      <td>DeleteModelPackage</td>
       <td style="text-align:right">-</td>
    </tr>
    <tr>
      <td>DeleteModelPackageGroup</td>
       <td style="text-align:right">-</td>
    </tr>
    <tr>
      <td>DeleteModelPackageGroupPolicy</td>
       <td style="text-align:right">-</td>
    </tr>
    <tr>
      <td>DeleteModelQualityJobDefinition</td>
       <td style="text-align:right">-</td>
    </tr>
    <tr>
      <td>DeleteMonitoringSchedule</td>
       <td style="text-align:right">-</td>
    </tr>
    <tr>
      <td>DeletePipeline</td>
       <td style="text-align:right">-</td>
    </tr>
    <tr>
      <td>DeleteProject</td>
       <td style="text-align:right">-</td>
    </tr>
    <tr>
      <td>DeleteStudioLifecycleConfig</td>
       <td style="text-align:right">-</td>
    </tr>
    <tr>
      <td>DeleteUserProfile</td>
       <td style="text-align:right">-</td>
    </tr>
    <tr>
      <td>DeleteWorkforce</td>
       <td style="text-align:right">-</td>
    </tr>
    <tr>
      <td>DeleteWorkteam</td>
       <td style="text-align:right">-</td>
    </tr>
    <tr>
      <td>DeregisterDevices</td>
       <td style="text-align:right">-</td>
    </tr>
    <tr>
      <td>DescribeAction</td>
       <td style="text-align:right">-</td>
    </tr>
    <tr>
      <td>DescribeAlgorithm</td>
       <td style="text-align:right">-</td>
    </tr>
    <tr>
      <td>DescribeApp</td>
       <td style="text-align:right">-</td>
    </tr>
    <tr>
      <td>DescribeAppImageConfig</td>
       <td style="text-align:right">-</td>
    </tr>
    <tr>
      <td>DescribeArtifact</td>
       <td style="text-align:right">-</td>
    </tr>
    <tr>
      <td>DescribeAutoMLJob</td>
       <td style="text-align:right">-</td>
    </tr>
    <tr>
      <td>DescribeCodeRepository</td>
       <td style="text-align:right">-</td>
    </tr>
    <tr>
      <td>DescribeCompilationJob</td>
       <td style="text-align:right">-</td>
    </tr>
    <tr>
      <td>DescribeContext</td>
       <td style="text-align:right">-</td>
    </tr>
    <tr>
      <td>DescribeDataQualityJobDefinition</td>
       <td style="text-align:right">-</td>
    </tr>
    <tr>
      <td>DescribeDevice</td>
       <td style="text-align:right">-</td>
    </tr>
    <tr>
      <td>DescribeDeviceFleet</td>
       <td style="text-align:right">-</td>
    </tr>
    <tr>
      <td>DescribeDomain</td>
       <td style="text-align:right">-</td>
    </tr>
    <tr>
      <td>DescribeEdgeDeploymentPlan</td>
       <td style="text-align:right">-</td>
    </tr>
    <tr>
      <td>DescribeEdgePackagingJob</td>
       <td style="text-align:right">-</td>
    </tr>
    <tr>
      <td>DescribeFeatureGroup</td>
       <td style="text-align:right">-</td>
    </tr>
    <tr>
      <td>DescribeFeatureMetadata</td>
       <td style="text-align:right">-</td>
    </tr>
    <tr>
      <td>DescribeFlowDefinition</td>
       <td style="text-align:right">-</td>
    </tr>
    <tr>
      <td>DescribeHumanTaskUi</td>
       <td style="text-align:right">-</td>
    </tr>
    <tr>
      <td>DescribeHyperParameterTuningJob</td>
       <td style="text-align:right">-</td>
    </tr>
    <tr>
      <td>DescribeImage</td>
       <td style="text-align:right">-</td>
    </tr>
    <tr>
      <td>DescribeImageVersion</td>
       <td style="text-align:right">-</td>
    </tr>
    <tr>
      <td>DescribeInferenceRecommendationsJob</td>
       <td style="text-align:right">-</td>
    </tr>
    <tr>
      <td>DescribeLabelingJob</td>
       <td style="text-align:right">-</td>
    </tr>
    <tr>
      <td>DescribeLineageGroup</td>
       <td style="text-align:right">-</td>
    </tr>
    <tr>
      <td>DescribeModelBiasJobDefinition</td>
       <td style="text-align:right">-</td>
    </tr>
    <tr>
      <td>DescribeModelExplainabilityJobDefinition</td>
       <td style="text-align:right">-</td>
    </tr>
    <tr>
      <td>DescribeModelPackage</td>
       <td style="text-align:right">-</td>
    </tr>
    <tr>
      <td>DescribeModelPackageGroup</td>
       <td style="text-align:right">-</td>
    </tr>
    <tr>
      <td>DescribeModelQualityJobDefinition</td>
       <td style="text-align:right">-</td>
    </tr>
    <tr>
      <td>DescribeMonitoringSchedule</td>
       <td style="text-align:right">-</td>
    </tr>
    <tr>
      <td>DescribePipeline</td>
       <td style="text-align:right">-</td>
    </tr>
    <tr>
      <td>DescribePipelineDefinitionForExecution</td>
       <td style="text-align:right">-</td>
    </tr>
    <tr>
      <td>DescribePipelineExecution</td>
       <td style="text-align:right">-</td>
    </tr>
    <tr>
      <td>DescribeProject</td>
       <td style="text-align:right">-</td>
    </tr>
    <tr>
      <td>DescribeStudioLifecycleConfig</td>
       <td style="text-align:right">-</td>
    </tr>
    <tr>
      <td>DescribeSubscribedWorkteam</td>
       <td style="text-align:right">-</td>
    </tr>
    <tr>
      <td>DescribeTransformJob</td>
       <td style="text-align:right">-</td>
    </tr>
    <tr>
      <td>DescribeUserProfile</td>
       <td style="text-align:right">-</td>
    </tr>
    <tr>
      <td>DescribeWorkforce</td>
       <td style="text-align:right">-</td>
    </tr>
    <tr>
      <td>DescribeWorkteam</td>
       <td style="text-align:right">-</td>
    </tr>
    <tr>
      <td>DisableSagemakerServicecatalogPortfolio</td>
       <td style="text-align:right">-</td>
    </tr>
    <tr>
      <td>EnableSagemakerServicecatalogPortfolio</td>
       <td style="text-align:right">-</td>
    </tr>
    <tr>
      <td>GetDeviceFleetReport</td>
       <td style="text-align:right">-</td>
    </tr>
    <tr>
      <td>GetLineageGroupPolicy</td>
       <td style="text-align:right">-</td>
    </tr>
    <tr>
      <td>GetModelPackageGroupPolicy</td>
       <td style="text-align:right">-</td>
    </tr>
    <tr>
      <td>GetSagemakerServicecatalogPortfolioStatus</td>
       <td style="text-align:right">-</td>
    </tr>
    <tr>
      <td>GetSearchSuggestions</td>
       <td style="text-align:right">-</td>
    </tr>
    <tr>
      <td>ListActions</td>
       <td style="text-align:right">-</td>
    </tr>
    <tr>
      <td>ListAlgorithms</td>
       <td style="text-align:right">-</td>
    </tr>
    <tr>
      <td>ListAppImageConfigs</td>
       <td style="text-align:right">-</td>
    </tr>
    <tr>
      <td>ListApps</td>
       <td style="text-align:right">-</td>
    </tr>
    <tr>
      <td>ListArtifacts</td>
       <td style="text-align:right">-</td>
    </tr>
    <tr>
      <td>ListAutoMLJobs</td>
       <td style="text-align:right">-</td>
    </tr>
    <tr>
      <td>ListCandidatesForAutoMLJob</td>
       <td style="text-align:right">-</td>
    </tr>
    <tr>
      <td>ListCodeRepositories</td>
       <td style="text-align:right">-</td>
    </tr>
    <tr>
      <td>ListCompilationJobs</td>
       <td style="text-align:right">-</td>
    </tr>
    <tr>
      <td>ListContexts</td>
       <td style="text-align:right">-</td>
    </tr>
    <tr>
      <td>ListDataQualityJobDefinitions</td>
       <td style="text-align:right">-</td>
    </tr>
    <tr>
      <td>ListDeviceFleets</td>
       <td style="text-align:right">-</td>
    </tr>
    <tr>
      <td>ListDevices</td>
       <td style="text-align:right">-</td>
    </tr>
    <tr>
      <td>ListDomains</td>
       <td style="text-align:right">-</td>
    </tr>
    <tr>
      <td>ListEdgeDeploymentPlans</td>
       <td style="text-align:right">-</td>
    </tr>
    <tr>
      <td>ListEdgePackagingJobs</td>
       <td style="text-align:right">-</td>
    </tr>
    <tr>
      <td>ListFeatureGroups</td>
       <td style="text-align:right">-</td>
    </tr>
    <tr>
      <td>ListFlowDefinitions</td>
       <td style="text-align:right">-</td>
    </tr>
    <tr>
      <td>ListHumanTaskUis</td>
       <td style="text-align:right">-</td>
    </tr>
    <tr>
      <td>ListHyperParameterTuningJobs</td>
       <td style="text-align:right">-</td>
    </tr>
    <tr>
      <td>ListImageVersions</td>
       <td style="text-align:right">-</td>
    </tr>
    <tr>
      <td>ListImages</td>
       <td style="text-align:right">-</td>
    </tr>
    <tr>
      <td>ListInferenceRecommendationsJobs</td>
       <td style="text-align:right">-</td>
    </tr>
    <tr>
      <td>ListLabelingJobs</td>
       <td style="text-align:right">-</td>
    </tr>
    <tr>
      <td>ListLabelingJobsForWorkteam</td>
       <td style="text-align:right">-</td>
    </tr>
    <tr>
      <td>ListLineageGroups</td>
       <td style="text-align:right">-</td>
    </tr>
    <tr>
      <td>ListModelBiasJobDefinitions</td>
       <td style="text-align:right">-</td>
    </tr>
    <tr>
      <td>ListModelExplainabilityJobDefinitions</td>
       <td style="text-align:right">-</td>
    </tr>
    <tr>
      <td>ListModelMetadata</td>
       <td style="text-align:right">-</td>
    </tr>
    <tr>
      <td>ListModelPackageGroups</td>
       <td style="text-align:right">-</td>
    </tr>
    <tr>
      <td>ListModelPackages</td>
       <td style="text-align:right">-</td>
    </tr>
    <tr>
      <td>ListModelQualityJobDefinitions</td>
       <td style="text-align:right">-</td>
    </tr>
    <tr>
      <td>ListMonitoringExecutions</td>
       <td style="text-align:right">-</td>
    </tr>
    <tr>
      <td>ListMonitoringSchedules</td>
       <td style="text-align:right">-</td>
    </tr>
    <tr>
      <td>ListNotebookInstanceLifecycleConfigs</td>
       <td style="text-align:right">-</td>
    </tr>
    <tr>
      <td>ListNotebookInstances</td>
       <td style="text-align:right">-</td>
    </tr>
    <tr>
      <td>ListPipelineExecutionSteps</td>
       <td style="text-align:right">-</td>
    </tr>
    <tr>
      <td>ListPipelineExecutions</td>
       <td style="text-align:right">-</td>
    </tr>
    <tr>
      <td>ListPipelineParametersForExecution</td>
       <td style="text-align:right">-</td>
    </tr>
    <tr>
      <td>ListPipelines</td>
       <td style="text-align:right">-</td>
    </tr>
    <tr>
      <td>ListProjects</td>
       <td style="text-align:right">-</td>
    </tr>
    <tr>
      <td>ListStageDevices</td>
       <td style="text-align:right">-</td>
    </tr>
    <tr>
      <td>ListStudioLifecycleConfigs</td>
       <td style="text-align:right">-</td>
    </tr>
    <tr>
      <td>ListSubscribedWorkteams</td>
       <td style="text-align:right">-</td>
    </tr>
    <tr>
      <td>ListTrainingJobsForHyperParameterTuningJob</td>
       <td style="text-align:right">-</td>
    </tr>
    <tr>
      <td>ListTransformJobs</td>
       <td style="text-align:right">-</td>
    </tr>
    <tr>
      <td>ListUserProfiles</td>
       <td style="text-align:right">-</td>
    </tr>
    <tr>
      <td>ListWorkforces</td>
       <td style="text-align:right">-</td>
    </tr>
    <tr>
      <td>ListWorkteams</td>
       <td style="text-align:right">-</td>
    </tr>
    <tr>
      <td>PutModelPackageGroupPolicy</td>
       <td style="text-align:right">-</td>
    </tr>
    <tr>
      <td>QueryLineage</td>
       <td style="text-align:right">-</td>
    </tr>
    <tr>
      <td>RegisterDevices</td>
       <td style="text-align:right">-</td>
    </tr>
    <tr>
      <td>RenderUiTemplate</td>
       <td style="text-align:right">-</td>
    </tr>
    <tr>
      <td>RetryPipelineExecution</td>
       <td style="text-align:right">-</td>
    </tr>
    <tr>
      <td>SendPipelineExecutionStepFailure</td>
       <td style="text-align:right">-</td>
    </tr>
    <tr>
      <td>SendPipelineExecutionStepSuccess</td>
       <td style="text-align:right">-</td>
    </tr>
    <tr>
      <td>StartEdgeDeploymentStage</td>
       <td style="text-align:right">-</td>
    </tr>
    <tr>
      <td>StartMonitoringSchedule</td>
       <td style="text-align:right">-</td>
    </tr>
    <tr>
      <td>StartPipelineExecution</td>
       <td style="text-align:right">-</td>
    </tr>
    <tr>
      <td>StopAutoMLJob</td>
       <td style="text-align:right">-</td>
    </tr>
    <tr>
      <td>StopCompilationJob</td>
       <td style="text-align:right">-</td>
    </tr>
    <tr>
      <td>StopEdgeDeploymentStage</td>
       <td style="text-align:right">-</td>
    </tr>
    <tr>
      <td>StopEdgePackagingJob</td>
       <td style="text-align:right">-</td>
    </tr>
    <tr>
      <td>StopHyperParameterTuningJob</td>
       <td style="text-align:right">-</td>
    </tr>
    <tr>
      <td>StopInferenceRecommendationsJob</td>
       <td style="text-align:right">-</td>
    </tr>
    <tr>
      <td>StopLabelingJob</td>
       <td style="text-align:right">-</td>
    </tr>
    <tr>
      <td>StopMonitoringSchedule</td>
       <td style="text-align:right">-</td>
    </tr>
    <tr>
      <td>StopPipelineExecution</td>
       <td style="text-align:right">-</td>
    </tr>
    <tr>
      <td>StopProcessingJob</td>
       <td style="text-align:right">-</td>
    </tr>
    <tr>
      <td>StopTrainingJob</td>
       <td style="text-align:right">-</td>
    </tr>
    <tr>
      <td>StopTransformJob</td>
       <td style="text-align:right">-</td>
    </tr>
    <tr>
      <td>UpdateAction</td>
       <td style="text-align:right">-</td>
    </tr>
    <tr>
      <td>UpdateAppImageConfig</td>
       <td style="text-align:right">-</td>
    </tr>
    <tr>
      <td>UpdateArtifact</td>
       <td style="text-align:right">-</td>
    </tr>
    <tr>
      <td>UpdateCodeRepository</td>
       <td style="text-align:right">-</td>
    </tr>
    <tr>
      <td>UpdateContext</td>
       <td style="text-align:right">-</td>
    </tr>
    <tr>
      <td>UpdateDeviceFleet</td>
       <td style="text-align:right">-</td>
    </tr>
    <tr>
      <td>UpdateDevices</td>
       <td style="text-align:right">-</td>
    </tr>
    <tr>
      <td>UpdateDomain</td>
       <td style="text-align:right">-</td>
    </tr>
    <tr>
      <td>UpdateEndpoint</td>
       <td style="text-align:right">-</td>
    </tr>
    <tr>
      <td>UpdateExperiment</td>
       <td style="text-align:right">-</td>
    </tr>
    <tr>
      <td>UpdateFeatureGroup</td>
       <td style="text-align:right">-</td>
    </tr>
    <tr>
      <td>UpdateFeatureMetadata</td>
       <td style="text-align:right">-</td>
    </tr>
    <tr>
      <td>UpdateImage</td>
       <td style="text-align:right">-</td>
    </tr>
    <tr>
      <td>UpdateModelPackage</td>
       <td style="text-align:right">-</td>
    </tr>
    <tr>
      <td>UpdateMonitoringSchedule</td>
       <td style="text-align:right">-</td>
    </tr>
    <tr>
      <td>UpdateNotebookInstance</td>
       <td style="text-align:right">-</td>
    </tr>
    <tr>
      <td>UpdateNotebookInstanceLifecycleConfig</td>
       <td style="text-align:right">-</td>
    </tr>
    <tr>
      <td>UpdatePipeline</td>
       <td style="text-align:right">-</td>
    </tr>
    <tr>
      <td>UpdatePipelineExecution</td>
       <td style="text-align:right">-</td>
    </tr>
    <tr>
      <td>UpdateProject</td>
       <td style="text-align:right">-</td>
    </tr>
    <tr>
      <td>UpdateTrainingJob</td>
       <td style="text-align:right">-</td>
    </tr>
    <tr>
      <td>UpdateTrial</td>
       <td style="text-align:right">-</td>
    </tr>
    <tr>
      <td>UpdateTrialComponent</td>
       <td style="text-align:right">-</td>
    </tr>
    <tr>
      <td>UpdateUserProfile</td>
       <td style="text-align:right">-</td>
    </tr>
    <tr>
      <td>UpdateWorkforce</td>
       <td style="text-align:right">-</td>
    </tr>
    <tr>
      <td>UpdateWorkteam</td>
       <td style="text-align:right">-</td>
    </tr>
  </tbody>
 </table>


## sagemaker-runtime ##

<table>
  <thead>
    <tr>
      <th>Operation</th>
      <th style="text-align:right">Implemented</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td>InvokeEndpoint (Pro) </td>
       <td style="text-align:right">✅</td>
    </tr>
    <tr>
      <td>InvokeEndpointAsync (Pro) </td>
       <td style="text-align:right">✅</td>
    </tr>
  </tbody>
 </table>


## secretsmanager ##

<table>
  <thead>
    <tr>
      <th>Operation</th>
      <th style="text-align:right">Implemented</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td>CreateSecret <a href="#misc" title="covered by our integration test suite">✨</a></td>
       <td style="text-align:right">✅</td>
    </tr>
    <tr>
      <td>DeleteResourcePolicy <a href="#misc" title="covered by our integration test suite">✨</a></td>
       <td style="text-align:right">✅</td>
    </tr>
    <tr>
      <td>DeleteSecret <a href="#misc" title="covered by our integration test suite">✨</a></td>
       <td style="text-align:right">✅</td>
    </tr>
    <tr>
      <td>DescribeSecret <a href="#misc" title="covered by our integration test suite">✨</a></td>
       <td style="text-align:right">✅</td>
    </tr>
    <tr>
      <td>GetRandomPassword <a href="#misc" title="covered by our integration test suite">✨</a></td>
       <td style="text-align:right">✅</td>
    </tr>
    <tr>
      <td>GetResourcePolicy <a href="#misc" title="covered by our integration test suite">✨</a></td>
       <td style="text-align:right">✅</td>
    </tr>
    <tr>
      <td>GetSecretValue <a href="#misc" title="covered by our integration test suite">✨</a></td>
       <td style="text-align:right">✅</td>
    </tr>
    <tr>
      <td>ListSecretVersionIds <a href="#misc" title="covered by our integration test suite">✨</a></td>
       <td style="text-align:right">✅</td>
    </tr>
    <tr>
      <td>ListSecrets <a href="#misc" title="covered by our integration test suite">✨</a></td>
       <td style="text-align:right">✅</td>
    </tr>
    <tr>
      <td>PutResourcePolicy <a href="#misc" title="covered by our integration test suite">✨</a></td>
       <td style="text-align:right">✅</td>
    </tr>
    <tr>
      <td>PutSecretValue <a href="#misc" title="covered by our integration test suite">✨</a></td>
       <td style="text-align:right">✅</td>
    </tr>
    <tr>
      <td>RestoreSecret</td>
       <td style="text-align:right">✅</td>
    </tr>
    <tr>
      <td>RotateSecret <a href="#misc" title="covered by our integration test suite">✨</a></td>
       <td style="text-align:right">✅</td>
    </tr>
    <tr>
      <td>TagResource <a href="#misc" title="covered by our integration test suite">✨</a></td>
       <td style="text-align:right">✅</td>
    </tr>
    <tr>
      <td>UntagResource <a href="#misc" title="covered by our integration test suite">✨</a></td>
       <td style="text-align:right">✅</td>
    </tr>
    <tr>
      <td>UpdateSecret <a href="#misc" title="covered by our integration test suite">✨</a></td>
       <td style="text-align:right">✅</td>
    </tr>
    <tr>
      <td>UpdateSecretVersionStage <a href="#misc" title="covered by our integration test suite">✨</a></td>
       <td style="text-align:right">✅</td>
    </tr>
  </tbody>
  <tbody>    <tr>
      <td><a data-toggle="collapse" href=".secretsmanager-notimplemented">Show missing</a></td>
      <td style="text-align:right"></td>
    </tr>
  </tbody>
  <tbody class="collapse secretsmanager-notimplemented">     <tr>
      <td>CancelRotateSecret</td>
       <td style="text-align:right">-</td>
    </tr>
    <tr>
      <td>RemoveRegionsFromReplication</td>
       <td style="text-align:right">-</td>
    </tr>
    <tr>
      <td>ReplicateSecretToRegions</td>
       <td style="text-align:right">-</td>
    </tr>
    <tr>
      <td>StopReplicationToReplica</td>
       <td style="text-align:right">-</td>
    </tr>
    <tr>
      <td>ValidateResourcePolicy</td>
       <td style="text-align:right">-</td>
    </tr>
  </tbody>
 </table>


## serverlessrepo ##

<table>
  <thead>
    <tr>
      <th>Operation</th>
      <th style="text-align:right">Implemented</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td>CreateApplication (Pro)  <a href="#misc" title="covered by our integration test suite">✨</a></td>
       <td style="text-align:right">✅</td>
    </tr>
    <tr>
      <td>CreateApplicationVersion (Pro)  <a href="#misc" title="covered by our integration test suite">✨</a></td>
       <td style="text-align:right">✅</td>
    </tr>
    <tr>
      <td>CreateCloudFormationChangeSet (Pro)  <a href="#misc" title="covered by our integration test suite">✨</a></td>
       <td style="text-align:right">✅</td>
    </tr>
    <tr>
      <td>CreateCloudFormationTemplate (Pro)  <a href="#misc" title="covered by our integration test suite">✨</a></td>
       <td style="text-align:right">✅</td>
    </tr>
    <tr>
      <td>DeleteApplication (Pro)  <a href="#misc" title="covered by our integration test suite">✨</a></td>
       <td style="text-align:right">✅</td>
    </tr>
    <tr>
      <td>GetCloudFormationTemplate (Pro)  <a href="#misc" title="covered by our integration test suite">✨</a></td>
       <td style="text-align:right">✅</td>
    </tr>
    <tr>
      <td>ListApplicationVersions (Pro)  <a href="#misc" title="covered by our integration test suite">✨</a></td>
       <td style="text-align:right">✅</td>
    </tr>
    <tr>
      <td>ListApplications (Pro)  <a href="#misc" title="covered by our integration test suite">✨</a></td>
       <td style="text-align:right">✅</td>
    </tr>
  </tbody>
  <tbody>    <tr>
      <td><a data-toggle="collapse" href=".serverlessrepo-notimplemented">Show missing</a></td>
      <td style="text-align:right"></td>
    </tr>
  </tbody>
  <tbody class="collapse serverlessrepo-notimplemented">     <tr>
      <td>GetApplication</td>
       <td style="text-align:right">-</td>
    </tr>
    <tr>
      <td>GetApplicationPolicy</td>
       <td style="text-align:right">-</td>
    </tr>
    <tr>
      <td>ListApplicationDependencies</td>
       <td style="text-align:right">-</td>
    </tr>
    <tr>
      <td>PutApplicationPolicy</td>
       <td style="text-align:right">-</td>
    </tr>
    <tr>
      <td>UnshareApplication</td>
       <td style="text-align:right">-</td>
    </tr>
    <tr>
      <td>UpdateApplication</td>
       <td style="text-align:right">-</td>
    </tr>
  </tbody>
 </table>


## servicediscovery ##

<table>
  <thead>
    <tr>
      <th>Operation</th>
      <th style="text-align:right">Implemented</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td>CreateHttpNamespace (Pro)  <a href="#misc" title="covered by our integration test suite">✨</a></td>
       <td style="text-align:right">✅</td>
    </tr>
    <tr>
      <td>CreatePrivateDnsNamespace (Pro)  <a href="#misc" title="covered by our integration test suite">✨</a></td>
       <td style="text-align:right">✅</td>
    </tr>
    <tr>
      <td>CreatePublicDnsNamespace (Pro)  <a href="#misc" title="covered by our integration test suite">✨</a></td>
       <td style="text-align:right">✅</td>
    </tr>
    <tr>
      <td>CreateService (Pro)  <a href="#misc" title="covered by our integration test suite">✨</a></td>
       <td style="text-align:right">✅</td>
    </tr>
    <tr>
      <td>DeleteNamespace (Pro)  <a href="#misc" title="covered by our integration test suite">✨</a></td>
       <td style="text-align:right">✅</td>
    </tr>
    <tr>
      <td>DeleteService (Pro)  <a href="#misc" title="covered by our integration test suite">✨</a></td>
       <td style="text-align:right">✅</td>
    </tr>
    <tr>
      <td>DeregisterInstance (Pro)  <a href="#misc" title="covered by our integration test suite">✨</a></td>
       <td style="text-align:right">✅</td>
    </tr>
    <tr>
      <td>DiscoverInstances (Pro)  <a href="#misc" title="covered by our integration test suite">✨</a></td>
       <td style="text-align:right">✅</td>
    </tr>
    <tr>
      <td>GetInstance (Pro)  <a href="#misc" title="covered by our integration test suite">✨</a></td>
       <td style="text-align:right">✅</td>
    </tr>
    <tr>
      <td>GetNamespace (Pro)  <a href="#misc" title="covered by our integration test suite">✨</a></td>
       <td style="text-align:right">✅</td>
    </tr>
    <tr>
      <td>GetOperation (Pro)  <a href="#misc" title="covered by our integration test suite">✨</a></td>
       <td style="text-align:right">✅</td>
    </tr>
    <tr>
      <td>GetService (Pro)  <a href="#misc" title="covered by our integration test suite">✨</a></td>
       <td style="text-align:right">✅</td>
    </tr>
    <tr>
      <td>ListInstances (Pro)  <a href="#misc" title="covered by our integration test suite">✨</a></td>
       <td style="text-align:right">✅</td>
    </tr>
    <tr>
      <td>ListNamespaces (Pro)  <a href="#misc" title="covered by our integration test suite">✨</a></td>
       <td style="text-align:right">✅</td>
    </tr>
    <tr>
      <td>ListServices (Pro)  <a href="#misc" title="covered by our integration test suite">✨</a></td>
       <td style="text-align:right">✅</td>
    </tr>
    <tr>
      <td>ListTagsForResource (Pro)  <a href="#misc" title="covered by our integration test suite">✨</a></td>
       <td style="text-align:right">✅</td>
    </tr>
    <tr>
      <td>RegisterInstance (Pro)  <a href="#misc" title="covered by our integration test suite">✨</a></td>
       <td style="text-align:right">✅</td>
    </tr>
    <tr>
      <td>TagResource (Pro)  <a href="#misc" title="covered by our integration test suite">✨</a></td>
       <td style="text-align:right">✅</td>
    </tr>
    <tr>
      <td>UntagResource (Pro)  <a href="#misc" title="covered by our integration test suite">✨</a></td>
       <td style="text-align:right">✅</td>
    </tr>
    <tr>
      <td>UpdateService (Pro)  <a href="#misc" title="covered by our integration test suite">✨</a></td>
       <td style="text-align:right">✅</td>
    </tr>
  </tbody>
  <tbody>    <tr>
      <td><a data-toggle="collapse" href=".servicediscovery-notimplemented">Show missing</a></td>
      <td style="text-align:right"></td>
    </tr>
  </tbody>
  <tbody class="collapse servicediscovery-notimplemented">     <tr>
      <td>GetInstancesHealthStatus</td>
       <td style="text-align:right">-</td>
    </tr>
    <tr>
      <td>ListOperations</td>
       <td style="text-align:right">-</td>
    </tr>
    <tr>
      <td>UpdateHttpNamespace</td>
       <td style="text-align:right">-</td>
    </tr>
    <tr>
      <td>UpdateInstanceCustomHealthStatus</td>
       <td style="text-align:right">-</td>
    </tr>
    <tr>
      <td>UpdatePrivateDnsNamespace</td>
       <td style="text-align:right">-</td>
    </tr>
    <tr>
      <td>UpdatePublicDnsNamespace</td>
       <td style="text-align:right">-</td>
    </tr>
  </tbody>
 </table>


## ses ##

<table>
  <thead>
    <tr>
      <th>Operation</th>
      <th style="text-align:right">Implemented</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td>CloneReceiptRuleSet <a href="#misc" title="covered by our integration test suite">✨</a></td>
       <td style="text-align:right">✅</td>
    </tr>
    <tr>
      <td>CreateConfigurationSet</td>
       <td style="text-align:right">✅</td>
    </tr>
    <tr>
      <td>CreateConfigurationSetEventDestination</td>
       <td style="text-align:right">✅</td>
    </tr>
    <tr>
      <td>CreateReceiptRule <a href="#misc" title="covered by our integration test suite">✨</a></td>
       <td style="text-align:right">✅</td>
    </tr>
    <tr>
      <td>CreateReceiptRuleSet <a href="#misc" title="covered by our integration test suite">✨</a></td>
       <td style="text-align:right">✅</td>
    </tr>
    <tr>
      <td>CreateTemplate <a href="#misc" title="covered by our integration test suite">✨</a></td>
       <td style="text-align:right">✅</td>
    </tr>
    <tr>
      <td>DeleteIdentity</td>
       <td style="text-align:right">✅</td>
    </tr>
    <tr>
      <td>DeleteReceiptRule (Pro)  <a href="#misc" title="covered by our integration test suite">✨</a></td>
       <td style="text-align:right">✅</td>
    </tr>
    <tr>
      <td>DeleteReceiptRuleSet (Pro)  <a href="#misc" title="covered by our integration test suite">✨</a></td>
       <td style="text-align:right">✅</td>
    </tr>
    <tr>
      <td>DeleteTemplate <a href="#misc" title="covered by our integration test suite">✨</a></td>
       <td style="text-align:right">✅</td>
    </tr>
    <tr>
      <td>DescribeActiveReceiptRuleSet (Pro)  <a href="#misc" title="covered by our integration test suite">✨</a></td>
       <td style="text-align:right">✅</td>
    </tr>
    <tr>
      <td>DescribeConfigurationSet</td>
       <td style="text-align:right">✅</td>
    </tr>
    <tr>
      <td>DescribeReceiptRule <a href="#misc" title="covered by our integration test suite">✨</a></td>
       <td style="text-align:right">✅</td>
    </tr>
    <tr>
      <td>DescribeReceiptRuleSet <a href="#misc" title="covered by our integration test suite">✨</a></td>
       <td style="text-align:right">✅</td>
    </tr>
    <tr>
      <td>GetIdentityMailFromDomainAttributes</td>
       <td style="text-align:right">✅</td>
    </tr>
    <tr>
      <td>GetIdentityNotificationAttributes</td>
       <td style="text-align:right">✅</td>
    </tr>
    <tr>
      <td>GetIdentityVerificationAttributes <a href="#misc" title="covered by our integration test suite">✨</a></td>
       <td style="text-align:right">✅</td>
    </tr>
    <tr>
      <td>GetSendQuota</td>
       <td style="text-align:right">✅</td>
    </tr>
    <tr>
      <td>GetSendStatistics</td>
       <td style="text-align:right">✅</td>
    </tr>
    <tr>
      <td>GetTemplate</td>
       <td style="text-align:right">✅</td>
    </tr>
    <tr>
      <td>ListIdentities</td>
       <td style="text-align:right">✅</td>
    </tr>
    <tr>
      <td>ListReceiptRuleSets (Pro)  <a href="#misc" title="covered by our integration test suite">✨</a></td>
       <td style="text-align:right">✅</td>
    </tr>
    <tr>
      <td>ListTemplates <a href="#misc" title="covered by our integration test suite">✨</a></td>
       <td style="text-align:right">✅</td>
    </tr>
    <tr>
      <td>ListVerifiedEmailAddresses</td>
       <td style="text-align:right">✅</td>
    </tr>
    <tr>
      <td>SendBulkTemplatedEmail <a href="#misc" title="covered by our integration test suite">✨</a></td>
       <td style="text-align:right">✅</td>
    </tr>
    <tr>
      <td>SendEmail <a href="#misc" title="covered by our integration test suite">✨</a></td>
       <td style="text-align:right">✅</td>
    </tr>
    <tr>
      <td>SendRawEmail <a href="#misc" title="covered by our integration test suite">✨</a></td>
       <td style="text-align:right">✅</td>
    </tr>
    <tr>
      <td>SendTemplatedEmail <a href="#misc" title="covered by our integration test suite">✨</a></td>
       <td style="text-align:right">✅</td>
    </tr>
    <tr>
      <td>SetActiveReceiptRuleSet (Pro)  <a href="#misc" title="covered by our integration test suite">✨</a></td>
       <td style="text-align:right">✅</td>
    </tr>
    <tr>
      <td>SetIdentityFeedbackForwardingEnabled</td>
       <td style="text-align:right">✅</td>
    </tr>
    <tr>
      <td>SetIdentityMailFromDomain</td>
       <td style="text-align:right">✅</td>
    </tr>
    <tr>
      <td>SetIdentityNotificationTopic</td>
       <td style="text-align:right">✅</td>
    </tr>
    <tr>
      <td>TestRenderTemplate</td>
       <td style="text-align:right">✅</td>
    </tr>
    <tr>
      <td>UpdateReceiptRule</td>
       <td style="text-align:right">✅</td>
    </tr>
    <tr>
      <td>UpdateTemplate</td>
       <td style="text-align:right">✅</td>
    </tr>
    <tr>
      <td>VerifyDomainDkim</td>
       <td style="text-align:right">✅</td>
    </tr>
    <tr>
      <td>VerifyDomainIdentity</td>
       <td style="text-align:right">✅</td>
    </tr>
    <tr>
      <td>VerifyEmailAddress <a href="#misc" title="covered by our integration test suite">✨</a></td>
       <td style="text-align:right">✅</td>
    </tr>
    <tr>
      <td>VerifyEmailIdentity <a href="#misc" title="covered by our integration test suite">✨</a></td>
       <td style="text-align:right">✅</td>
    </tr>
  </tbody>
  <tbody>    <tr>
      <td><a data-toggle="collapse" href=".ses-notimplemented">Show missing</a></td>
      <td style="text-align:right"></td>
    </tr>
  </tbody>
  <tbody class="collapse ses-notimplemented">     <tr>
      <td>CreateConfigurationSetTrackingOptions</td>
       <td style="text-align:right">-</td>
    </tr>
    <tr>
      <td>CreateCustomVerificationEmailTemplate</td>
       <td style="text-align:right">-</td>
    </tr>
    <tr>
      <td>CreateReceiptFilter</td>
       <td style="text-align:right">-</td>
    </tr>
    <tr>
      <td>DeleteConfigurationSet</td>
       <td style="text-align:right">-</td>
    </tr>
    <tr>
      <td>DeleteConfigurationSetEventDestination</td>
       <td style="text-align:right">-</td>
    </tr>
    <tr>
      <td>DeleteConfigurationSetTrackingOptions</td>
       <td style="text-align:right">-</td>
    </tr>
    <tr>
      <td>DeleteCustomVerificationEmailTemplate</td>
       <td style="text-align:right">-</td>
    </tr>
    <tr>
      <td>DeleteIdentityPolicy</td>
       <td style="text-align:right">-</td>
    </tr>
    <tr>
      <td>DeleteReceiptFilter</td>
       <td style="text-align:right">-</td>
    </tr>
    <tr>
      <td>DeleteVerifiedEmailAddress</td>
       <td style="text-align:right">-</td>
    </tr>
    <tr>
      <td>GetAccountSendingEnabled</td>
       <td style="text-align:right">-</td>
    </tr>
    <tr>
      <td>GetCustomVerificationEmailTemplate</td>
       <td style="text-align:right">-</td>
    </tr>
    <tr>
      <td>GetIdentityDkimAttributes</td>
       <td style="text-align:right">-</td>
    </tr>
    <tr>
      <td>GetIdentityPolicies</td>
       <td style="text-align:right">-</td>
    </tr>
    <tr>
      <td>ListConfigurationSets</td>
       <td style="text-align:right">-</td>
    </tr>
    <tr>
      <td>ListCustomVerificationEmailTemplates</td>
       <td style="text-align:right">-</td>
    </tr>
    <tr>
      <td>ListIdentityPolicies</td>
       <td style="text-align:right">-</td>
    </tr>
    <tr>
      <td>ListReceiptFilters</td>
       <td style="text-align:right">-</td>
    </tr>
    <tr>
      <td>PutConfigurationSetDeliveryOptions</td>
       <td style="text-align:right">-</td>
    </tr>
    <tr>
      <td>PutIdentityPolicy</td>
       <td style="text-align:right">-</td>
    </tr>
    <tr>
      <td>ReorderReceiptRuleSet</td>
       <td style="text-align:right">-</td>
    </tr>
    <tr>
      <td>SendBounce</td>
       <td style="text-align:right">-</td>
    </tr>
    <tr>
      <td>SendCustomVerificationEmail</td>
       <td style="text-align:right">-</td>
    </tr>
    <tr>
      <td>SetIdentityDkimEnabled</td>
       <td style="text-align:right">-</td>
    </tr>
    <tr>
      <td>SetIdentityHeadersInNotificationsEnabled</td>
       <td style="text-align:right">-</td>
    </tr>
    <tr>
      <td>SetReceiptRulePosition</td>
       <td style="text-align:right">-</td>
    </tr>
    <tr>
      <td>UpdateAccountSendingEnabled</td>
       <td style="text-align:right">-</td>
    </tr>
    <tr>
      <td>UpdateConfigurationSetEventDestination</td>
       <td style="text-align:right">-</td>
    </tr>
    <tr>
      <td>UpdateConfigurationSetReputationMetricsEnabled</td>
       <td style="text-align:right">-</td>
    </tr>
    <tr>
      <td>UpdateConfigurationSetSendingEnabled</td>
       <td style="text-align:right">-</td>
    </tr>
    <tr>
      <td>UpdateConfigurationSetTrackingOptions</td>
       <td style="text-align:right">-</td>
    </tr>
    <tr>
      <td>UpdateCustomVerificationEmailTemplate</td>
       <td style="text-align:right">-</td>
    </tr>
  </tbody>
 </table>


## sesv2 ##

<table>
  <thead>
    <tr>
      <th>Operation</th>
      <th style="text-align:right">Implemented</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td>CreateEmailIdentity (Pro)  <a href="#misc" title="covered by our integration test suite">✨</a></td>
       <td style="text-align:right">✅</td>
    </tr>
    <tr>
      <td>CreateEmailTemplate (Pro)  <a href="#misc" title="covered by our integration test suite">✨</a></td>
       <td style="text-align:right">✅</td>
    </tr>
    <tr>
      <td>DeleteEmailIdentity (Pro)  <a href="#misc" title="covered by our integration test suite">✨</a></td>
       <td style="text-align:right">✅</td>
    </tr>
    <tr>
      <td>DeleteEmailTemplate (Pro) </td>
       <td style="text-align:right">✅</td>
    </tr>
    <tr>
      <td>GetDomainStatisticsReport (Pro) </td>
       <td style="text-align:right">✅</td>
    </tr>
    <tr>
      <td>GetEmailIdentity (Pro)  <a href="#misc" title="covered by our integration test suite">✨</a></td>
       <td style="text-align:right">✅</td>
    </tr>
    <tr>
      <td>ListDomainDeliverabilityCampaigns (Pro) </td>
       <td style="text-align:right">✅</td>
    </tr>
    <tr>
      <td>ListEmailIdentities (Pro)  <a href="#misc" title="covered by our integration test suite">✨</a></td>
       <td style="text-align:right">✅</td>
    </tr>
    <tr>
      <td>ListEmailTemplates (Pro) </td>
       <td style="text-align:right">✅</td>
    </tr>
    <tr>
      <td>ListSuppressedDestinations (Pro) </td>
       <td style="text-align:right">✅</td>
    </tr>
    <tr>
      <td>PutEmailIdentityDkimSigningAttributes (Pro) </td>
       <td style="text-align:right">✅</td>
    </tr>
    <tr>
      <td>SendBulkEmail (Pro)  <a href="#misc" title="covered by our integration test suite">✨</a></td>
       <td style="text-align:right">✅</td>
    </tr>
    <tr>
      <td>SendEmail (Pro)  <a href="#misc" title="covered by our integration test suite">✨</a></td>
       <td style="text-align:right">✅</td>
    </tr>
  </tbody>
  <tbody>    <tr>
      <td><a data-toggle="collapse" href=".sesv2-notimplemented">Show missing</a></td>
      <td style="text-align:right"></td>
    </tr>
  </tbody>
  <tbody class="collapse sesv2-notimplemented">     <tr>
      <td>CreateConfigurationSet</td>
       <td style="text-align:right">-</td>
    </tr>
    <tr>
      <td>CreateConfigurationSetEventDestination</td>
       <td style="text-align:right">-</td>
    </tr>
    <tr>
      <td>CreateContact</td>
       <td style="text-align:right">-</td>
    </tr>
    <tr>
      <td>CreateContactList</td>
       <td style="text-align:right">-</td>
    </tr>
    <tr>
      <td>CreateCustomVerificationEmailTemplate</td>
       <td style="text-align:right">-</td>
    </tr>
    <tr>
      <td>CreateDedicatedIpPool</td>
       <td style="text-align:right">-</td>
    </tr>
    <tr>
      <td>CreateDeliverabilityTestReport</td>
       <td style="text-align:right">-</td>
    </tr>
    <tr>
      <td>CreateEmailIdentityPolicy</td>
       <td style="text-align:right">-</td>
    </tr>
    <tr>
      <td>CreateImportJob</td>
       <td style="text-align:right">-</td>
    </tr>
    <tr>
      <td>DeleteConfigurationSet</td>
       <td style="text-align:right">-</td>
    </tr>
    <tr>
      <td>DeleteConfigurationSetEventDestination</td>
       <td style="text-align:right">-</td>
    </tr>
    <tr>
      <td>DeleteContact</td>
       <td style="text-align:right">-</td>
    </tr>
    <tr>
      <td>DeleteContactList</td>
       <td style="text-align:right">-</td>
    </tr>
    <tr>
      <td>DeleteCustomVerificationEmailTemplate</td>
       <td style="text-align:right">-</td>
    </tr>
    <tr>
      <td>DeleteDedicatedIpPool</td>
       <td style="text-align:right">-</td>
    </tr>
    <tr>
      <td>DeleteEmailIdentityPolicy</td>
       <td style="text-align:right">-</td>
    </tr>
    <tr>
      <td>DeleteSuppressedDestination</td>
       <td style="text-align:right">-</td>
    </tr>
    <tr>
      <td>GetAccount</td>
       <td style="text-align:right">-</td>
    </tr>
    <tr>
      <td>GetBlacklistReports</td>
       <td style="text-align:right">-</td>
    </tr>
    <tr>
      <td>GetConfigurationSet</td>
       <td style="text-align:right">-</td>
    </tr>
    <tr>
      <td>GetConfigurationSetEventDestinations</td>
       <td style="text-align:right">-</td>
    </tr>
    <tr>
      <td>GetContact</td>
       <td style="text-align:right">-</td>
    </tr>
    <tr>
      <td>GetContactList</td>
       <td style="text-align:right">-</td>
    </tr>
    <tr>
      <td>GetCustomVerificationEmailTemplate</td>
       <td style="text-align:right">-</td>
    </tr>
    <tr>
      <td>GetDedicatedIp</td>
       <td style="text-align:right">-</td>
    </tr>
    <tr>
      <td>GetDedicatedIpPool</td>
       <td style="text-align:right">-</td>
    </tr>
    <tr>
      <td>GetDedicatedIps</td>
       <td style="text-align:right">-</td>
    </tr>
    <tr>
      <td>GetDeliverabilityDashboardOptions</td>
       <td style="text-align:right">-</td>
    </tr>
    <tr>
      <td>GetDeliverabilityTestReport</td>
       <td style="text-align:right">-</td>
    </tr>
    <tr>
      <td>GetDomainDeliverabilityCampaign</td>
       <td style="text-align:right">-</td>
    </tr>
    <tr>
      <td>GetEmailIdentityPolicies</td>
       <td style="text-align:right">-</td>
    </tr>
    <tr>
      <td>GetEmailTemplate</td>
       <td style="text-align:right">-</td>
    </tr>
    <tr>
      <td>GetImportJob</td>
       <td style="text-align:right">-</td>
    </tr>
    <tr>
      <td>GetSuppressedDestination</td>
       <td style="text-align:right">-</td>
    </tr>
    <tr>
      <td>ListConfigurationSets</td>
       <td style="text-align:right">-</td>
    </tr>
    <tr>
      <td>ListContactLists</td>
       <td style="text-align:right">-</td>
    </tr>
    <tr>
      <td>ListContacts</td>
       <td style="text-align:right">-</td>
    </tr>
    <tr>
      <td>ListCustomVerificationEmailTemplates</td>
       <td style="text-align:right">-</td>
    </tr>
    <tr>
      <td>ListDedicatedIpPools</td>
       <td style="text-align:right">-</td>
    </tr>
    <tr>
      <td>ListDeliverabilityTestReports</td>
       <td style="text-align:right">-</td>
    </tr>
    <tr>
      <td>ListImportJobs</td>
       <td style="text-align:right">-</td>
    </tr>
    <tr>
      <td>ListTagsForResource</td>
       <td style="text-align:right">-</td>
    </tr>
    <tr>
      <td>PutAccountDedicatedIpWarmupAttributes</td>
       <td style="text-align:right">-</td>
    </tr>
    <tr>
      <td>PutAccountDetails</td>
       <td style="text-align:right">-</td>
    </tr>
    <tr>
      <td>PutAccountSendingAttributes</td>
       <td style="text-align:right">-</td>
    </tr>
    <tr>
      <td>PutAccountSuppressionAttributes</td>
       <td style="text-align:right">-</td>
    </tr>
    <tr>
      <td>PutConfigurationSetDeliveryOptions</td>
       <td style="text-align:right">-</td>
    </tr>
    <tr>
      <td>PutConfigurationSetReputationOptions</td>
       <td style="text-align:right">-</td>
    </tr>
    <tr>
      <td>PutConfigurationSetSendingOptions</td>
       <td style="text-align:right">-</td>
    </tr>
    <tr>
      <td>PutConfigurationSetSuppressionOptions</td>
       <td style="text-align:right">-</td>
    </tr>
    <tr>
      <td>PutConfigurationSetTrackingOptions</td>
       <td style="text-align:right">-</td>
    </tr>
    <tr>
      <td>PutDedicatedIpInPool</td>
       <td style="text-align:right">-</td>
    </tr>
    <tr>
      <td>PutDedicatedIpWarmupAttributes</td>
       <td style="text-align:right">-</td>
    </tr>
    <tr>
      <td>PutDeliverabilityDashboardOption</td>
       <td style="text-align:right">-</td>
    </tr>
    <tr>
      <td>PutEmailIdentityConfigurationSetAttributes</td>
       <td style="text-align:right">-</td>
    </tr>
    <tr>
      <td>PutEmailIdentityDkimAttributes</td>
       <td style="text-align:right">-</td>
    </tr>
    <tr>
      <td>PutEmailIdentityFeedbackAttributes</td>
       <td style="text-align:right">-</td>
    </tr>
    <tr>
      <td>PutEmailIdentityMailFromAttributes</td>
       <td style="text-align:right">-</td>
    </tr>
    <tr>
      <td>PutSuppressedDestination</td>
       <td style="text-align:right">-</td>
    </tr>
    <tr>
      <td>SendCustomVerificationEmail</td>
       <td style="text-align:right">-</td>
    </tr>
    <tr>
      <td>TagResource</td>
       <td style="text-align:right">-</td>
    </tr>
    <tr>
      <td>TestRenderEmailTemplate</td>
       <td style="text-align:right">-</td>
    </tr>
    <tr>
      <td>UntagResource</td>
       <td style="text-align:right">-</td>
    </tr>
    <tr>
      <td>UpdateConfigurationSetEventDestination</td>
       <td style="text-align:right">-</td>
    </tr>
    <tr>
      <td>UpdateContact</td>
       <td style="text-align:right">-</td>
    </tr>
    <tr>
      <td>UpdateContactList</td>
       <td style="text-align:right">-</td>
    </tr>
    <tr>
      <td>UpdateCustomVerificationEmailTemplate</td>
       <td style="text-align:right">-</td>
    </tr>
    <tr>
      <td>UpdateEmailIdentityPolicy</td>
       <td style="text-align:right">-</td>
    </tr>
    <tr>
      <td>UpdateEmailTemplate</td>
       <td style="text-align:right">-</td>
    </tr>
  </tbody>
 </table>


## sns ##

<table>
  <thead>
    <tr>
      <th>Operation</th>
      <th style="text-align:right">Implemented</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td>AddPermission</td>
       <td style="text-align:right">✅</td>
    </tr>
    <tr>
      <td>CheckIfPhoneNumberIsOptedOut</td>
       <td style="text-align:right">✅</td>
    </tr>
    <tr>
      <td>ConfirmSubscription <a href="#misc" title="covered by our integration test suite">✨</a></td>
       <td style="text-align:right">✅</td>
    </tr>
    <tr>
      <td>CreatePlatformApplication <a href="#misc" title="covered by our integration test suite">✨</a></td>
       <td style="text-align:right">✅</td>
    </tr>
    <tr>
      <td>CreatePlatformEndpoint <a href="#misc" title="covered by our integration test suite">✨</a></td>
       <td style="text-align:right">✅</td>
    </tr>
    <tr>
      <td>CreateTopic <a href="#misc" title="covered by our integration test suite">✨</a></td>
       <td style="text-align:right">✅</td>
    </tr>
    <tr>
      <td>DeleteEndpoint <a href="#misc" title="covered by our integration test suite">✨</a></td>
       <td style="text-align:right">✅</td>
    </tr>
    <tr>
      <td>DeletePlatformApplication <a href="#misc" title="covered by our integration test suite">✨</a></td>
       <td style="text-align:right">✅</td>
    </tr>
    <tr>
      <td>DeleteTopic <a href="#misc" title="covered by our integration test suite">✨</a></td>
       <td style="text-align:right">✅</td>
    </tr>
    <tr>
      <td>GetEndpointAttributes <a href="#misc" title="covered by our integration test suite">✨</a></td>
       <td style="text-align:right">✅</td>
    </tr>
    <tr>
      <td>GetPlatformApplicationAttributes</td>
       <td style="text-align:right">✅</td>
    </tr>
    <tr>
      <td>GetSMSAttributes</td>
       <td style="text-align:right">✅</td>
    </tr>
    <tr>
      <td>GetSubscriptionAttributes <a href="#misc" title="covered by our integration test suite">✨</a></td>
       <td style="text-align:right">✅</td>
    </tr>
    <tr>
      <td>GetTopicAttributes <a href="#misc" title="covered by our integration test suite">✨</a></td>
       <td style="text-align:right">✅</td>
    </tr>
    <tr>
      <td>ListEndpointsByPlatformApplication <a href="#misc" title="covered by our integration test suite">✨</a></td>
       <td style="text-align:right">✅</td>
    </tr>
    <tr>
      <td>ListPhoneNumbersOptedOut</td>
       <td style="text-align:right">✅</td>
    </tr>
    <tr>
      <td>ListPlatformApplications <a href="#misc" title="covered by our integration test suite">✨</a></td>
       <td style="text-align:right">✅</td>
    </tr>
    <tr>
      <td>ListSubscriptions</td>
       <td style="text-align:right">✅</td>
    </tr>
    <tr>
      <td>ListSubscriptionsByTopic <a href="#misc" title="covered by our integration test suite">✨</a></td>
       <td style="text-align:right">✅</td>
    </tr>
    <tr>
      <td>ListTagsForResource <a href="#misc" title="covered by our integration test suite">✨</a></td>
       <td style="text-align:right">✅</td>
    </tr>
    <tr>
      <td>ListTopics <a href="#misc" title="covered by our integration test suite">✨</a></td>
       <td style="text-align:right">✅</td>
    </tr>
    <tr>
      <td>OptInPhoneNumber</td>
       <td style="text-align:right">✅</td>
    </tr>
    <tr>
      <td>Publish <a href="#misc" title="covered by our integration test suite">✨</a></td>
       <td style="text-align:right">✅</td>
    </tr>
    <tr>
      <td>PublishBatch <a href="#misc" title="covered by our integration test suite">✨</a></td>
       <td style="text-align:right">✅</td>
    </tr>
    <tr>
      <td>RemovePermission</td>
       <td style="text-align:right">✅</td>
    </tr>
    <tr>
      <td>SetEndpointAttributes</td>
       <td style="text-align:right">✅</td>
    </tr>
    <tr>
      <td>SetPlatformApplicationAttributes</td>
       <td style="text-align:right">✅</td>
    </tr>
    <tr>
      <td>SetSMSAttributes</td>
       <td style="text-align:right">✅</td>
    </tr>
    <tr>
      <td>SetSubscriptionAttributes <a href="#misc" title="covered by our integration test suite">✨</a></td>
       <td style="text-align:right">✅</td>
    </tr>
    <tr>
      <td>SetTopicAttributes <a href="#misc" title="covered by our integration test suite">✨</a></td>
       <td style="text-align:right">✅</td>
    </tr>
    <tr>
      <td>Subscribe <a href="#misc" title="covered by our integration test suite">✨</a></td>
       <td style="text-align:right">✅</td>
    </tr>
    <tr>
      <td>TagResource <a href="#misc" title="covered by our integration test suite">✨</a></td>
       <td style="text-align:right">✅</td>
    </tr>
    <tr>
      <td>Unsubscribe <a href="#misc" title="covered by our integration test suite">✨</a></td>
       <td style="text-align:right">✅</td>
    </tr>
    <tr>
      <td>UntagResource <a href="#misc" title="covered by our integration test suite">✨</a></td>
       <td style="text-align:right">✅</td>
    </tr>
  </tbody>
  <tbody>    <tr>
      <td><a data-toggle="collapse" href=".sns-notimplemented">Show missing</a></td>
      <td style="text-align:right"></td>
    </tr>
  </tbody>
  <tbody class="collapse sns-notimplemented">     <tr>
      <td>CreateSMSSandboxPhoneNumber</td>
       <td style="text-align:right">-</td>
    </tr>
    <tr>
      <td>DeleteSMSSandboxPhoneNumber</td>
       <td style="text-align:right">-</td>
    </tr>
    <tr>
      <td>GetDataProtectionPolicy</td>
       <td style="text-align:right">-</td>
    </tr>
    <tr>
      <td>GetSMSSandboxAccountStatus</td>
       <td style="text-align:right">-</td>
    </tr>
    <tr>
      <td>ListOriginationNumbers</td>
       <td style="text-align:right">-</td>
    </tr>
    <tr>
      <td>ListSMSSandboxPhoneNumbers</td>
       <td style="text-align:right">-</td>
    </tr>
    <tr>
      <td>PutDataProtectionPolicy</td>
       <td style="text-align:right">-</td>
    </tr>
    <tr>
      <td>VerifySMSSandboxPhoneNumber</td>
       <td style="text-align:right">-</td>
    </tr>
  </tbody>
 </table>


## sqs ##

<table>
  <thead>
    <tr>
      <th>Operation</th>
      <th style="text-align:right">Implemented</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td>AddPermission</td>
       <td style="text-align:right">✅</td>
    </tr>
    <tr>
      <td>ChangeMessageVisibility <a href="#misc" title="covered by our integration test suite">✨</a></td>
       <td style="text-align:right">✅</td>
    </tr>
    <tr>
      <td>ChangeMessageVisibilityBatch</td>
       <td style="text-align:right">✅</td>
    </tr>
    <tr>
      <td>CreateQueue <a href="#misc" title="covered by our integration test suite">✨</a></td>
       <td style="text-align:right">✅</td>
    </tr>
    <tr>
      <td>DeleteMessage <a href="#misc" title="covered by our integration test suite">✨</a></td>
       <td style="text-align:right">✅</td>
    </tr>
    <tr>
      <td>DeleteMessageBatch <a href="#misc" title="covered by our integration test suite">✨</a></td>
       <td style="text-align:right">✅</td>
    </tr>
    <tr>
      <td>DeleteQueue <a href="#misc" title="covered by our integration test suite">✨</a></td>
       <td style="text-align:right">✅</td>
    </tr>
    <tr>
      <td>GetQueueAttributes <a href="#misc" title="covered by our integration test suite">✨</a></td>
       <td style="text-align:right">✅</td>
    </tr>
    <tr>
      <td>GetQueueUrl <a href="#misc" title="covered by our integration test suite">✨</a></td>
       <td style="text-align:right">✅</td>
    </tr>
    <tr>
      <td>ListDeadLetterSourceQueues <a href="#misc" title="covered by our integration test suite">✨</a></td>
       <td style="text-align:right">✅</td>
    </tr>
    <tr>
      <td>ListQueueTags <a href="#misc" title="covered by our integration test suite">✨</a></td>
       <td style="text-align:right">✅</td>
    </tr>
    <tr>
      <td>ListQueues <a href="#misc" title="covered by our integration test suite">✨</a></td>
       <td style="text-align:right">✅</td>
    </tr>
    <tr>
      <td>PurgeQueue <a href="#misc" title="covered by our integration test suite">✨</a></td>
       <td style="text-align:right">✅</td>
    </tr>
    <tr>
      <td>ReceiveMessage <a href="#misc" title="covered by our integration test suite">✨</a></td>
       <td style="text-align:right">✅</td>
    </tr>
    <tr>
      <td>RemovePermission</td>
       <td style="text-align:right">✅</td>
    </tr>
    <tr>
      <td>SendMessage <a href="#misc" title="covered by our integration test suite">✨</a></td>
       <td style="text-align:right">✅</td>
    </tr>
    <tr>
      <td>SendMessageBatch <a href="#misc" title="covered by our integration test suite">✨</a></td>
       <td style="text-align:right">✅</td>
    </tr>
    <tr>
      <td>SetQueueAttributes <a href="#misc" title="covered by our integration test suite">✨</a></td>
       <td style="text-align:right">✅</td>
    </tr>
    <tr>
      <td>TagQueue <a href="#misc" title="covered by our integration test suite">✨</a></td>
       <td style="text-align:right">✅</td>
    </tr>
    <tr>
      <td>UntagQueue <a href="#misc" title="covered by our integration test suite">✨</a></td>
       <td style="text-align:right">✅</td>
    </tr>
  </tbody>
 </table>


## ssm ##

<table>
  <thead>
    <tr>
      <th>Operation</th>
      <th style="text-align:right">Implemented</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td>AddTagsToResource</td>
       <td style="text-align:right">✅</td>
    </tr>
    <tr>
      <td>CancelCommand (Pro)  <a href="#misc" title="covered by our integration test suite">✨</a></td>
       <td style="text-align:right">✅</td>
    </tr>
    <tr>
      <td>CreateDocument</td>
       <td style="text-align:right">✅</td>
    </tr>
    <tr>
      <td>CreateMaintenanceWindow</td>
       <td style="text-align:right">✅</td>
    </tr>
    <tr>
      <td>DeleteDocument</td>
       <td style="text-align:right">✅</td>
    </tr>
    <tr>
      <td>DeleteMaintenanceWindow</td>
       <td style="text-align:right">✅</td>
    </tr>
    <tr>
      <td>DeleteParameter <a href="#misc" title="covered by our integration test suite">✨</a></td>
       <td style="text-align:right">✅</td>
    </tr>
    <tr>
      <td>DeleteParameters</td>
       <td style="text-align:right">✅</td>
    </tr>
    <tr>
      <td>DescribeDocument</td>
       <td style="text-align:right">✅</td>
    </tr>
    <tr>
      <td>DescribeDocumentPermission</td>
       <td style="text-align:right">✅</td>
    </tr>
    <tr>
      <td>DescribeInstanceInformation (Pro)  <a href="#misc" title="covered by our integration test suite">✨</a></td>
       <td style="text-align:right">✅</td>
    </tr>
    <tr>
      <td>DescribeMaintenanceWindows</td>
       <td style="text-align:right">✅</td>
    </tr>
    <tr>
      <td>DescribeParameters <a href="#misc" title="covered by our integration test suite">✨</a></td>
       <td style="text-align:right">✅</td>
    </tr>
    <tr>
      <td>GetCommandInvocation <a href="#misc" title="covered by our integration test suite">✨</a></td>
       <td style="text-align:right">✅</td>
    </tr>
    <tr>
      <td>GetDocument</td>
       <td style="text-align:right">✅</td>
    </tr>
    <tr>
      <td>GetMaintenanceWindow</td>
       <td style="text-align:right">✅</td>
    </tr>
    <tr>
      <td>GetParameter <a href="#misc" title="covered by our integration test suite">✨</a></td>
       <td style="text-align:right">✅</td>
    </tr>
    <tr>
      <td>GetParameterHistory</td>
       <td style="text-align:right">✅</td>
    </tr>
    <tr>
      <td>GetParameters <a href="#misc" title="covered by our integration test suite">✨</a></td>
       <td style="text-align:right">✅</td>
    </tr>
    <tr>
      <td>GetParametersByPath <a href="#misc" title="covered by our integration test suite">✨</a></td>
       <td style="text-align:right">✅</td>
    </tr>
    <tr>
      <td>LabelParameterVersion <a href="#misc" title="covered by our integration test suite">✨</a></td>
       <td style="text-align:right">✅</td>
    </tr>
    <tr>
      <td>ListCommandInvocations (Pro) </td>
       <td style="text-align:right">✅</td>
    </tr>
    <tr>
      <td>ListCommands</td>
       <td style="text-align:right">✅</td>
    </tr>
    <tr>
      <td>ListDocuments</td>
       <td style="text-align:right">✅</td>
    </tr>
    <tr>
      <td>ListTagsForResource</td>
       <td style="text-align:right">✅</td>
    </tr>
    <tr>
      <td>ModifyDocumentPermission</td>
       <td style="text-align:right">✅</td>
    </tr>
    <tr>
      <td>PutParameter <a href="#misc" title="covered by our integration test suite">✨</a></td>
       <td style="text-align:right">✅</td>
    </tr>
    <tr>
      <td>RemoveTagsFromResource</td>
       <td style="text-align:right">✅</td>
    </tr>
    <tr>
      <td>SendCommand <a href="#misc" title="covered by our integration test suite">✨</a></td>
       <td style="text-align:right">✅</td>
    </tr>
    <tr>
      <td>UpdateDocument</td>
       <td style="text-align:right">✅</td>
    </tr>
    <tr>
      <td>UpdateDocumentDefaultVersion</td>
       <td style="text-align:right">✅</td>
    </tr>
  </tbody>
  <tbody>    <tr>
      <td><a data-toggle="collapse" href=".ssm-notimplemented">Show missing</a></td>
      <td style="text-align:right"></td>
    </tr>
  </tbody>
  <tbody class="collapse ssm-notimplemented">     <tr>
      <td>AssociateOpsItemRelatedItem</td>
       <td style="text-align:right">-</td>
    </tr>
    <tr>
      <td>CancelMaintenanceWindowExecution</td>
       <td style="text-align:right">-</td>
    </tr>
    <tr>
      <td>CreateActivation</td>
       <td style="text-align:right">-</td>
    </tr>
    <tr>
      <td>CreateAssociation</td>
       <td style="text-align:right">-</td>
    </tr>
    <tr>
      <td>CreateAssociationBatch</td>
       <td style="text-align:right">-</td>
    </tr>
    <tr>
      <td>CreateOpsItem</td>
       <td style="text-align:right">-</td>
    </tr>
    <tr>
      <td>CreateOpsMetadata</td>
       <td style="text-align:right">-</td>
    </tr>
    <tr>
      <td>CreatePatchBaseline</td>
       <td style="text-align:right">-</td>
    </tr>
    <tr>
      <td>CreateResourceDataSync</td>
       <td style="text-align:right">-</td>
    </tr>
    <tr>
      <td>DeleteActivation</td>
       <td style="text-align:right">-</td>
    </tr>
    <tr>
      <td>DeleteAssociation</td>
       <td style="text-align:right">-</td>
    </tr>
    <tr>
      <td>DeleteInventory</td>
       <td style="text-align:right">-</td>
    </tr>
    <tr>
      <td>DeleteOpsMetadata</td>
       <td style="text-align:right">-</td>
    </tr>
    <tr>
      <td>DeletePatchBaseline</td>
       <td style="text-align:right">-</td>
    </tr>
    <tr>
      <td>DeleteResourceDataSync</td>
       <td style="text-align:right">-</td>
    </tr>
    <tr>
      <td>DeregisterManagedInstance</td>
       <td style="text-align:right">-</td>
    </tr>
    <tr>
      <td>DeregisterPatchBaselineForPatchGroup</td>
       <td style="text-align:right">-</td>
    </tr>
    <tr>
      <td>DeregisterTargetFromMaintenanceWindow</td>
       <td style="text-align:right">-</td>
    </tr>
    <tr>
      <td>DeregisterTaskFromMaintenanceWindow</td>
       <td style="text-align:right">-</td>
    </tr>
    <tr>
      <td>DescribeActivations</td>
       <td style="text-align:right">-</td>
    </tr>
    <tr>
      <td>DescribeAssociation</td>
       <td style="text-align:right">-</td>
    </tr>
    <tr>
      <td>DescribeAssociationExecutionTargets</td>
       <td style="text-align:right">-</td>
    </tr>
    <tr>
      <td>DescribeAssociationExecutions</td>
       <td style="text-align:right">-</td>
    </tr>
    <tr>
      <td>DescribeAutomationExecutions</td>
       <td style="text-align:right">-</td>
    </tr>
    <tr>
      <td>DescribeAutomationStepExecutions</td>
       <td style="text-align:right">-</td>
    </tr>
    <tr>
      <td>DescribeAvailablePatches</td>
       <td style="text-align:right">-</td>
    </tr>
    <tr>
      <td>DescribeEffectiveInstanceAssociations</td>
       <td style="text-align:right">-</td>
    </tr>
    <tr>
      <td>DescribeEffectivePatchesForPatchBaseline</td>
       <td style="text-align:right">-</td>
    </tr>
    <tr>
      <td>DescribeInstanceAssociationsStatus</td>
       <td style="text-align:right">-</td>
    </tr>
    <tr>
      <td>DescribeInstancePatchStates</td>
       <td style="text-align:right">-</td>
    </tr>
    <tr>
      <td>DescribeInstancePatchStatesForPatchGroup</td>
       <td style="text-align:right">-</td>
    </tr>
    <tr>
      <td>DescribeInstancePatches</td>
       <td style="text-align:right">-</td>
    </tr>
    <tr>
      <td>DescribeInventoryDeletions</td>
       <td style="text-align:right">-</td>
    </tr>
    <tr>
      <td>DescribeMaintenanceWindowExecutionTaskInvocations</td>
       <td style="text-align:right">-</td>
    </tr>
    <tr>
      <td>DescribeMaintenanceWindowExecutionTasks</td>
       <td style="text-align:right">-</td>
    </tr>
    <tr>
      <td>DescribeMaintenanceWindowExecutions</td>
       <td style="text-align:right">-</td>
    </tr>
    <tr>
      <td>DescribeMaintenanceWindowSchedule</td>
       <td style="text-align:right">-</td>
    </tr>
    <tr>
      <td>DescribeMaintenanceWindowTargets</td>
       <td style="text-align:right">-</td>
    </tr>
    <tr>
      <td>DescribeMaintenanceWindowTasks</td>
       <td style="text-align:right">-</td>
    </tr>
    <tr>
      <td>DescribeMaintenanceWindowsForTarget</td>
       <td style="text-align:right">-</td>
    </tr>
    <tr>
      <td>DescribeOpsItems</td>
       <td style="text-align:right">-</td>
    </tr>
    <tr>
      <td>DescribePatchBaselines</td>
       <td style="text-align:right">-</td>
    </tr>
    <tr>
      <td>DescribePatchGroupState</td>
       <td style="text-align:right">-</td>
    </tr>
    <tr>
      <td>DescribePatchGroups</td>
       <td style="text-align:right">-</td>
    </tr>
    <tr>
      <td>DescribePatchProperties</td>
       <td style="text-align:right">-</td>
    </tr>
    <tr>
      <td>DescribeSessions</td>
       <td style="text-align:right">-</td>
    </tr>
    <tr>
      <td>DisassociateOpsItemRelatedItem</td>
       <td style="text-align:right">-</td>
    </tr>
    <tr>
      <td>GetAutomationExecution</td>
       <td style="text-align:right">-</td>
    </tr>
    <tr>
      <td>GetCalendarState</td>
       <td style="text-align:right">-</td>
    </tr>
    <tr>
      <td>GetConnectionStatus</td>
       <td style="text-align:right">-</td>
    </tr>
    <tr>
      <td>GetDefaultPatchBaseline</td>
       <td style="text-align:right">-</td>
    </tr>
    <tr>
      <td>GetDeployablePatchSnapshotForInstance</td>
       <td style="text-align:right">-</td>
    </tr>
    <tr>
      <td>GetInventory</td>
       <td style="text-align:right">-</td>
    </tr>
    <tr>
      <td>GetInventorySchema</td>
       <td style="text-align:right">-</td>
    </tr>
    <tr>
      <td>GetMaintenanceWindowExecution</td>
       <td style="text-align:right">-</td>
    </tr>
    <tr>
      <td>GetMaintenanceWindowExecutionTask</td>
       <td style="text-align:right">-</td>
    </tr>
    <tr>
      <td>GetMaintenanceWindowExecutionTaskInvocation</td>
       <td style="text-align:right">-</td>
    </tr>
    <tr>
      <td>GetMaintenanceWindowTask</td>
       <td style="text-align:right">-</td>
    </tr>
    <tr>
      <td>GetOpsItem</td>
       <td style="text-align:right">-</td>
    </tr>
    <tr>
      <td>GetOpsMetadata</td>
       <td style="text-align:right">-</td>
    </tr>
    <tr>
      <td>GetOpsSummary</td>
       <td style="text-align:right">-</td>
    </tr>
    <tr>
      <td>GetPatchBaseline</td>
       <td style="text-align:right">-</td>
    </tr>
    <tr>
      <td>GetPatchBaselineForPatchGroup</td>
       <td style="text-align:right">-</td>
    </tr>
    <tr>
      <td>GetServiceSetting</td>
       <td style="text-align:right">-</td>
    </tr>
    <tr>
      <td>ListAssociationVersions</td>
       <td style="text-align:right">-</td>
    </tr>
    <tr>
      <td>ListAssociations</td>
       <td style="text-align:right">-</td>
    </tr>
    <tr>
      <td>ListComplianceItems</td>
       <td style="text-align:right">-</td>
    </tr>
    <tr>
      <td>ListComplianceSummaries</td>
       <td style="text-align:right">-</td>
    </tr>
    <tr>
      <td>ListDocumentMetadataHistory</td>
       <td style="text-align:right">-</td>
    </tr>
    <tr>
      <td>ListDocumentVersions</td>
       <td style="text-align:right">-</td>
    </tr>
    <tr>
      <td>ListInventoryEntries</td>
       <td style="text-align:right">-</td>
    </tr>
    <tr>
      <td>ListOpsItemEvents</td>
       <td style="text-align:right">-</td>
    </tr>
    <tr>
      <td>ListOpsItemRelatedItems</td>
       <td style="text-align:right">-</td>
    </tr>
    <tr>
      <td>ListOpsMetadata</td>
       <td style="text-align:right">-</td>
    </tr>
    <tr>
      <td>ListResourceComplianceSummaries</td>
       <td style="text-align:right">-</td>
    </tr>
    <tr>
      <td>ListResourceDataSync</td>
       <td style="text-align:right">-</td>
    </tr>
    <tr>
      <td>PutComplianceItems</td>
       <td style="text-align:right">-</td>
    </tr>
    <tr>
      <td>PutInventory</td>
       <td style="text-align:right">-</td>
    </tr>
    <tr>
      <td>RegisterDefaultPatchBaseline</td>
       <td style="text-align:right">-</td>
    </tr>
    <tr>
      <td>RegisterPatchBaselineForPatchGroup</td>
       <td style="text-align:right">-</td>
    </tr>
    <tr>
      <td>RegisterTargetWithMaintenanceWindow</td>
       <td style="text-align:right">-</td>
    </tr>
    <tr>
      <td>RegisterTaskWithMaintenanceWindow</td>
       <td style="text-align:right">-</td>
    </tr>
    <tr>
      <td>ResetServiceSetting</td>
       <td style="text-align:right">-</td>
    </tr>
    <tr>
      <td>ResumeSession</td>
       <td style="text-align:right">-</td>
    </tr>
    <tr>
      <td>SendAutomationSignal</td>
       <td style="text-align:right">-</td>
    </tr>
    <tr>
      <td>StartAssociationsOnce</td>
       <td style="text-align:right">-</td>
    </tr>
    <tr>
      <td>StartAutomationExecution</td>
       <td style="text-align:right">-</td>
    </tr>
    <tr>
      <td>StartChangeRequestExecution</td>
       <td style="text-align:right">-</td>
    </tr>
    <tr>
      <td>StartSession</td>
       <td style="text-align:right">-</td>
    </tr>
    <tr>
      <td>StopAutomationExecution</td>
       <td style="text-align:right">-</td>
    </tr>
    <tr>
      <td>TerminateSession</td>
       <td style="text-align:right">-</td>
    </tr>
    <tr>
      <td>UnlabelParameterVersion</td>
       <td style="text-align:right">-</td>
    </tr>
    <tr>
      <td>UpdateAssociation</td>
       <td style="text-align:right">-</td>
    </tr>
    <tr>
      <td>UpdateAssociationStatus</td>
       <td style="text-align:right">-</td>
    </tr>
    <tr>
      <td>UpdateDocumentMetadata</td>
       <td style="text-align:right">-</td>
    </tr>
    <tr>
      <td>UpdateMaintenanceWindow</td>
       <td style="text-align:right">-</td>
    </tr>
    <tr>
      <td>UpdateMaintenanceWindowTarget</td>
       <td style="text-align:right">-</td>
    </tr>
    <tr>
      <td>UpdateMaintenanceWindowTask</td>
       <td style="text-align:right">-</td>
    </tr>
    <tr>
      <td>UpdateManagedInstanceRole</td>
       <td style="text-align:right">-</td>
    </tr>
    <tr>
      <td>UpdateOpsItem</td>
       <td style="text-align:right">-</td>
    </tr>
    <tr>
      <td>UpdateOpsMetadata</td>
       <td style="text-align:right">-</td>
    </tr>
    <tr>
      <td>UpdatePatchBaseline</td>
       <td style="text-align:right">-</td>
    </tr>
    <tr>
      <td>UpdateResourceDataSync</td>
       <td style="text-align:right">-</td>
    </tr>
    <tr>
      <td>UpdateServiceSetting</td>
       <td style="text-align:right">-</td>
    </tr>
  </tbody>
 </table>


## stepfunctions ##

<table>
  <thead>
    <tr>
      <th>Operation</th>
      <th style="text-align:right">Implemented</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td>CreateActivity <a href="#misc" title="covered by our integration test suite">✨</a></td>
       <td style="text-align:right">✅</td>
    </tr>
    <tr>
      <td>CreateStateMachine <a href="#misc" title="covered by our integration test suite">✨</a></td>
       <td style="text-align:right">✅</td>
    </tr>
    <tr>
      <td>DeleteActivity <a href="#misc" title="covered by our integration test suite">✨</a></td>
       <td style="text-align:right">✅</td>
    </tr>
    <tr>
      <td>DeleteStateMachine <a href="#misc" title="covered by our integration test suite">✨</a></td>
       <td style="text-align:right">✅</td>
    </tr>
    <tr>
      <td>DescribeActivity <a href="#misc" title="covered by our integration test suite">✨</a></td>
       <td style="text-align:right">✅</td>
    </tr>
    <tr>
      <td>DescribeExecution <a href="#misc" title="covered by our integration test suite">✨</a></td>
       <td style="text-align:right">✅</td>
    </tr>
    <tr>
      <td>DescribeStateMachine <a href="#misc" title="covered by our integration test suite">✨</a></td>
       <td style="text-align:right">✅</td>
    </tr>
    <tr>
      <td>DescribeStateMachineForExecution <a href="#misc" title="covered by our integration test suite">✨</a></td>
       <td style="text-align:right">✅</td>
    </tr>
    <tr>
      <td>GetActivityTask</td>
       <td style="text-align:right">✅</td>
    </tr>
    <tr>
      <td>GetExecutionHistory <a href="#misc" title="covered by our integration test suite">✨</a></td>
       <td style="text-align:right">✅</td>
    </tr>
    <tr>
      <td>ListActivities</td>
       <td style="text-align:right">✅</td>
    </tr>
    <tr>
      <td>ListExecutions <a href="#misc" title="covered by our integration test suite">✨</a></td>
       <td style="text-align:right">✅</td>
    </tr>
    <tr>
      <td>ListStateMachines <a href="#misc" title="covered by our integration test suite">✨</a></td>
       <td style="text-align:right">✅</td>
    </tr>
    <tr>
      <td>ListTagsForResource</td>
       <td style="text-align:right">✅</td>
    </tr>
    <tr>
      <td>SendTaskFailure</td>
       <td style="text-align:right">✅</td>
    </tr>
    <tr>
      <td>SendTaskHeartbeat</td>
       <td style="text-align:right">✅</td>
    </tr>
    <tr>
      <td>SendTaskSuccess</td>
       <td style="text-align:right">✅</td>
    </tr>
    <tr>
      <td>StartExecution <a href="#misc" title="covered by our integration test suite">✨</a></td>
       <td style="text-align:right">✅</td>
    </tr>
    <tr>
      <td>StartSyncExecution</td>
       <td style="text-align:right">✅</td>
    </tr>
    <tr>
      <td>StopExecution</td>
       <td style="text-align:right">✅</td>
    </tr>
    <tr>
      <td>TagResource</td>
       <td style="text-align:right">✅</td>
    </tr>
    <tr>
      <td>UntagResource</td>
       <td style="text-align:right">✅</td>
    </tr>
    <tr>
      <td>UpdateStateMachine <a href="#misc" title="covered by our integration test suite">✨</a></td>
       <td style="text-align:right">✅</td>
    </tr>
  </tbody>
 </table>


## sts ##

<table>
  <thead>
    <tr>
      <th>Operation</th>
      <th style="text-align:right">Implemented</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td>AssumeRole <a href="#misc" title="covered by our integration test suite">✨</a></td>
       <td style="text-align:right">✅</td>
    </tr>
    <tr>
      <td>AssumeRoleWithSAML <a href="#misc" title="covered by our integration test suite">✨</a></td>
       <td style="text-align:right">✅</td>
    </tr>
    <tr>
      <td>AssumeRoleWithWebIdentity <a href="#misc" title="covered by our integration test suite">✨</a></td>
       <td style="text-align:right">✅</td>
    </tr>
    <tr>
      <td>GetCallerIdentity <a href="#misc" title="covered by our integration test suite">✨</a></td>
       <td style="text-align:right">✅</td>
    </tr>
    <tr>
      <td>GetFederationToken <a href="#misc" title="covered by our integration test suite">✨</a></td>
       <td style="text-align:right">✅</td>
    </tr>
    <tr>
      <td>GetSessionToken <a href="#misc" title="covered by our integration test suite">✨</a></td>
       <td style="text-align:right">✅</td>
    </tr>
  </tbody>
  <tbody>    <tr>
      <td><a data-toggle="collapse" href=".sts-notimplemented">Show missing</a></td>
      <td style="text-align:right"></td>
    </tr>
  </tbody>
  <tbody class="collapse sts-notimplemented">     <tr>
      <td>DecodeAuthorizationMessage</td>
       <td style="text-align:right">-</td>
    </tr>
    <tr>
      <td>GetAccessKeyInfo</td>
       <td style="text-align:right">-</td>
    </tr>
  </tbody>
 </table>


## support ##

<table>
  <thead>
    <tr>
      <th>Operation</th>
      <th style="text-align:right">Implemented</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td>CreateCase <a href="#misc" title="covered by our integration test suite">✨</a></td>
       <td style="text-align:right">✅</td>
    </tr>
    <tr>
      <td>DescribeCases <a href="#misc" title="covered by our integration test suite">✨</a></td>
       <td style="text-align:right">✅</td>
    </tr>
    <tr>
      <td>DescribeTrustedAdvisorChecks</td>
       <td style="text-align:right">✅</td>
    </tr>
    <tr>
      <td>RefreshTrustedAdvisorCheck</td>
       <td style="text-align:right">✅</td>
    </tr>
    <tr>
      <td>ResolveCase <a href="#misc" title="covered by our integration test suite">✨</a></td>
       <td style="text-align:right">✅</td>
    </tr>
  </tbody>
  <tbody>    <tr>
      <td><a data-toggle="collapse" href=".support-notimplemented">Show missing</a></td>
      <td style="text-align:right"></td>
    </tr>
  </tbody>
  <tbody class="collapse support-notimplemented">     <tr>
      <td>AddAttachmentsToSet</td>
       <td style="text-align:right">-</td>
    </tr>
    <tr>
      <td>AddCommunicationToCase</td>
       <td style="text-align:right">-</td>
    </tr>
    <tr>
      <td>DescribeAttachment</td>
       <td style="text-align:right">-</td>
    </tr>
    <tr>
      <td>DescribeCommunications</td>
       <td style="text-align:right">-</td>
    </tr>
    <tr>
      <td>DescribeServices</td>
       <td style="text-align:right">-</td>
    </tr>
    <tr>
      <td>DescribeSeverityLevels</td>
       <td style="text-align:right">-</td>
    </tr>
    <tr>
      <td>DescribeTrustedAdvisorCheckRefreshStatuses</td>
       <td style="text-align:right">-</td>
    </tr>
    <tr>
      <td>DescribeTrustedAdvisorCheckResult</td>
       <td style="text-align:right">-</td>
    </tr>
    <tr>
      <td>DescribeTrustedAdvisorCheckSummaries</td>
       <td style="text-align:right">-</td>
    </tr>
  </tbody>
 </table>


## swf ##

<table>
  <thead>
    <tr>
      <th>Operation</th>
      <th style="text-align:right">Implemented</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td>CountPendingActivityTasks</td>
       <td style="text-align:right">✅</td>
    </tr>
    <tr>
      <td>CountPendingDecisionTasks</td>
       <td style="text-align:right">✅</td>
    </tr>
    <tr>
      <td>DeprecateActivityType</td>
       <td style="text-align:right">✅</td>
    </tr>
    <tr>
      <td>DeprecateDomain</td>
       <td style="text-align:right">✅</td>
    </tr>
    <tr>
      <td>DeprecateWorkflowType</td>
       <td style="text-align:right">✅</td>
    </tr>
    <tr>
      <td>DescribeActivityType</td>
       <td style="text-align:right">✅</td>
    </tr>
    <tr>
      <td>DescribeDomain</td>
       <td style="text-align:right">✅</td>
    </tr>
    <tr>
      <td>DescribeWorkflowExecution</td>
       <td style="text-align:right">✅</td>
    </tr>
    <tr>
      <td>DescribeWorkflowType</td>
       <td style="text-align:right">✅</td>
    </tr>
    <tr>
      <td>GetWorkflowExecutionHistory <a href="#misc" title="covered by our integration test suite">✨</a></td>
       <td style="text-align:right">✅</td>
    </tr>
    <tr>
      <td>ListActivityTypes</td>
       <td style="text-align:right">✅</td>
    </tr>
    <tr>
      <td>ListClosedWorkflowExecutions</td>
       <td style="text-align:right">✅</td>
    </tr>
    <tr>
      <td>ListDomains</td>
       <td style="text-align:right">✅</td>
    </tr>
    <tr>
      <td>ListOpenWorkflowExecutions</td>
       <td style="text-align:right">✅</td>
    </tr>
    <tr>
      <td>ListWorkflowTypes <a href="#misc" title="covered by our integration test suite">✨</a></td>
       <td style="text-align:right">✅</td>
    </tr>
    <tr>
      <td>PollForActivityTask <a href="#misc" title="covered by our integration test suite">✨</a></td>
       <td style="text-align:right">✅</td>
    </tr>
    <tr>
      <td>PollForDecisionTask <a href="#misc" title="covered by our integration test suite">✨</a></td>
       <td style="text-align:right">✅</td>
    </tr>
    <tr>
      <td>RecordActivityTaskHeartbeat</td>
       <td style="text-align:right">✅</td>
    </tr>
    <tr>
      <td>RegisterActivityType <a href="#misc" title="covered by our integration test suite">✨</a></td>
       <td style="text-align:right">✅</td>
    </tr>
    <tr>
      <td>RegisterDomain <a href="#misc" title="covered by our integration test suite">✨</a></td>
       <td style="text-align:right">✅</td>
    </tr>
    <tr>
      <td>RegisterWorkflowType <a href="#misc" title="covered by our integration test suite">✨</a></td>
       <td style="text-align:right">✅</td>
    </tr>
    <tr>
      <td>RespondActivityTaskCompleted <a href="#misc" title="covered by our integration test suite">✨</a></td>
       <td style="text-align:right">✅</td>
    </tr>
    <tr>
      <td>RespondActivityTaskFailed</td>
       <td style="text-align:right">✅</td>
    </tr>
    <tr>
      <td>RespondDecisionTaskCompleted <a href="#misc" title="covered by our integration test suite">✨</a></td>
       <td style="text-align:right">✅</td>
    </tr>
    <tr>
      <td>SignalWorkflowExecution</td>
       <td style="text-align:right">✅</td>
    </tr>
    <tr>
      <td>StartWorkflowExecution <a href="#misc" title="covered by our integration test suite">✨</a></td>
       <td style="text-align:right">✅</td>
    </tr>
    <tr>
      <td>TerminateWorkflowExecution</td>
       <td style="text-align:right">✅</td>
    </tr>
    <tr>
      <td>UndeprecateActivityType</td>
       <td style="text-align:right">✅</td>
    </tr>
    <tr>
      <td>UndeprecateDomain</td>
       <td style="text-align:right">✅</td>
    </tr>
    <tr>
      <td>UndeprecateWorkflowType</td>
       <td style="text-align:right">✅</td>
    </tr>
  </tbody>
  <tbody>    <tr>
      <td><a data-toggle="collapse" href=".swf-notimplemented">Show missing</a></td>
      <td style="text-align:right"></td>
    </tr>
  </tbody>
  <tbody class="collapse swf-notimplemented">     <tr>
      <td>CountClosedWorkflowExecutions</td>
       <td style="text-align:right">-</td>
    </tr>
    <tr>
      <td>CountOpenWorkflowExecutions</td>
       <td style="text-align:right">-</td>
    </tr>
    <tr>
      <td>ListTagsForResource</td>
       <td style="text-align:right">-</td>
    </tr>
    <tr>
      <td>RequestCancelWorkflowExecution</td>
       <td style="text-align:right">-</td>
    </tr>
    <tr>
      <td>RespondActivityTaskCanceled</td>
       <td style="text-align:right">-</td>
    </tr>
    <tr>
      <td>TagResource</td>
       <td style="text-align:right">-</td>
    </tr>
    <tr>
      <td>UntagResource</td>
       <td style="text-align:right">-</td>
    </tr>
  </tbody>
 </table>


## timestream-query ##

<table>
  <thead>
    <tr>
      <th>Operation</th>
      <th style="text-align:right">Implemented</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td>DescribeEndpoints (Pro)  <a href="#misc" title="covered by our integration test suite">✨</a></td>
       <td style="text-align:right">✅</td>
    </tr>
    <tr>
      <td>Query (Pro)  <a href="#misc" title="covered by our integration test suite">✨</a></td>
       <td style="text-align:right">✅</td>
    </tr>
  </tbody>
  <tbody>    <tr>
      <td><a data-toggle="collapse" href=".timestream-query-notimplemented">Show missing</a></td>
      <td style="text-align:right"></td>
    </tr>
  </tbody>
  <tbody class="collapse timestream-query-notimplemented">     <tr>
      <td>CancelQuery</td>
       <td style="text-align:right">-</td>
    </tr>
    <tr>
      <td>CreateScheduledQuery</td>
       <td style="text-align:right">-</td>
    </tr>
    <tr>
      <td>DeleteScheduledQuery</td>
       <td style="text-align:right">-</td>
    </tr>
    <tr>
      <td>DescribeScheduledQuery</td>
       <td style="text-align:right">-</td>
    </tr>
    <tr>
      <td>ExecuteScheduledQuery</td>
       <td style="text-align:right">-</td>
    </tr>
    <tr>
      <td>ListScheduledQueries</td>
       <td style="text-align:right">-</td>
    </tr>
    <tr>
      <td>ListTagsForResource</td>
       <td style="text-align:right">-</td>
    </tr>
    <tr>
      <td>PrepareQuery</td>
       <td style="text-align:right">-</td>
    </tr>
    <tr>
      <td>TagResource</td>
       <td style="text-align:right">-</td>
    </tr>
    <tr>
      <td>UntagResource</td>
       <td style="text-align:right">-</td>
    </tr>
    <tr>
      <td>UpdateScheduledQuery</td>
       <td style="text-align:right">-</td>
    </tr>
  </tbody>
 </table>


## timestream-write ##

<table>
  <thead>
    <tr>
      <th>Operation</th>
      <th style="text-align:right">Implemented</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td>CreateDatabase (Pro)  <a href="#misc" title="covered by our integration test suite">✨</a></td>
       <td style="text-align:right">✅</td>
    </tr>
    <tr>
      <td>CreateTable (Pro)  <a href="#misc" title="covered by our integration test suite">✨</a></td>
       <td style="text-align:right">✅</td>
    </tr>
    <tr>
      <td>DeleteDatabase (Pro)  <a href="#misc" title="covered by our integration test suite">✨</a></td>
       <td style="text-align:right">✅</td>
    </tr>
    <tr>
      <td>DeleteTable (Pro)  <a href="#misc" title="covered by our integration test suite">✨</a></td>
       <td style="text-align:right">✅</td>
    </tr>
    <tr>
      <td>DescribeDatabase (Pro)  <a href="#misc" title="covered by our integration test suite">✨</a></td>
       <td style="text-align:right">✅</td>
    </tr>
    <tr>
      <td>DescribeEndpoints (Pro) </td>
       <td style="text-align:right">✅</td>
    </tr>
    <tr>
      <td>DescribeTable (Pro)  <a href="#misc" title="covered by our integration test suite">✨</a></td>
       <td style="text-align:right">✅</td>
    </tr>
    <tr>
      <td>ListDatabases (Pro)  <a href="#misc" title="covered by our integration test suite">✨</a></td>
       <td style="text-align:right">✅</td>
    </tr>
    <tr>
      <td>ListTables (Pro)  <a href="#misc" title="covered by our integration test suite">✨</a></td>
       <td style="text-align:right">✅</td>
    </tr>
    <tr>
      <td>WriteRecords (Pro)  <a href="#misc" title="covered by our integration test suite">✨</a></td>
       <td style="text-align:right">✅</td>
    </tr>
  </tbody>
  <tbody>    <tr>
      <td><a data-toggle="collapse" href=".timestream-write-notimplemented">Show missing</a></td>
      <td style="text-align:right"></td>
    </tr>
  </tbody>
  <tbody class="collapse timestream-write-notimplemented">     <tr>
      <td>ListTagsForResource</td>
       <td style="text-align:right">-</td>
    </tr>
    <tr>
      <td>TagResource</td>
       <td style="text-align:right">-</td>
    </tr>
    <tr>
      <td>UntagResource</td>
       <td style="text-align:right">-</td>
    </tr>
    <tr>
      <td>UpdateDatabase</td>
       <td style="text-align:right">-</td>
    </tr>
    <tr>
      <td>UpdateTable</td>
       <td style="text-align:right">-</td>
    </tr>
  </tbody>
 </table>


## transcribe ##

<table>
  <thead>
    <tr>
      <th>Operation</th>
      <th style="text-align:right">Implemented</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td>CreateMedicalVocabulary</td>
       <td style="text-align:right">✅</td>
    </tr>
    <tr>
      <td>CreateVocabulary</td>
       <td style="text-align:right">✅</td>
    </tr>
    <tr>
      <td>DeleteMedicalTranscriptionJob</td>
       <td style="text-align:right">✅</td>
    </tr>
    <tr>
      <td>DeleteMedicalVocabulary</td>
       <td style="text-align:right">✅</td>
    </tr>
    <tr>
      <td>DeleteTranscriptionJob <a href="#misc" title="covered by our integration test suite">✨</a></td>
       <td style="text-align:right">✅</td>
    </tr>
    <tr>
      <td>DeleteVocabulary</td>
       <td style="text-align:right">✅</td>
    </tr>
    <tr>
      <td>GetMedicalTranscriptionJob</td>
       <td style="text-align:right">✅</td>
    </tr>
    <tr>
      <td>GetMedicalVocabulary</td>
       <td style="text-align:right">✅</td>
    </tr>
    <tr>
      <td>GetTranscriptionJob <a href="#misc" title="covered by our integration test suite">✨</a></td>
       <td style="text-align:right">✅</td>
    </tr>
    <tr>
      <td>GetVocabulary</td>
       <td style="text-align:right">✅</td>
    </tr>
    <tr>
      <td>ListMedicalTranscriptionJobs</td>
       <td style="text-align:right">✅</td>
    </tr>
    <tr>
      <td>ListMedicalVocabularies</td>
       <td style="text-align:right">✅</td>
    </tr>
    <tr>
      <td>ListTranscriptionJobs <a href="#misc" title="covered by our integration test suite">✨</a></td>
       <td style="text-align:right">✅</td>
    </tr>
    <tr>
      <td>ListVocabularies</td>
       <td style="text-align:right">✅</td>
    </tr>
    <tr>
      <td>StartMedicalTranscriptionJob</td>
       <td style="text-align:right">✅</td>
    </tr>
    <tr>
      <td>StartTranscriptionJob <a href="#misc" title="covered by our integration test suite">✨</a></td>
       <td style="text-align:right">✅</td>
    </tr>
  </tbody>
  <tbody>    <tr>
      <td><a data-toggle="collapse" href=".transcribe-notimplemented">Show missing</a></td>
      <td style="text-align:right"></td>
    </tr>
  </tbody>
  <tbody class="collapse transcribe-notimplemented">     <tr>
      <td>CreateCallAnalyticsCategory</td>
       <td style="text-align:right">-</td>
    </tr>
    <tr>
      <td>CreateLanguageModel</td>
       <td style="text-align:right">-</td>
    </tr>
    <tr>
      <td>CreateVocabularyFilter</td>
       <td style="text-align:right">-</td>
    </tr>
    <tr>
      <td>DeleteCallAnalyticsCategory</td>
       <td style="text-align:right">-</td>
    </tr>
    <tr>
      <td>DeleteCallAnalyticsJob</td>
       <td style="text-align:right">-</td>
    </tr>
    <tr>
      <td>DeleteLanguageModel</td>
       <td style="text-align:right">-</td>
    </tr>
    <tr>
      <td>DeleteVocabularyFilter</td>
       <td style="text-align:right">-</td>
    </tr>
    <tr>
      <td>DescribeLanguageModel</td>
       <td style="text-align:right">-</td>
    </tr>
    <tr>
      <td>GetCallAnalyticsCategory</td>
       <td style="text-align:right">-</td>
    </tr>
    <tr>
      <td>GetCallAnalyticsJob</td>
       <td style="text-align:right">-</td>
    </tr>
    <tr>
      <td>GetVocabularyFilter</td>
       <td style="text-align:right">-</td>
    </tr>
    <tr>
      <td>ListCallAnalyticsCategories</td>
       <td style="text-align:right">-</td>
    </tr>
    <tr>
      <td>ListCallAnalyticsJobs</td>
       <td style="text-align:right">-</td>
    </tr>
    <tr>
      <td>ListLanguageModels</td>
       <td style="text-align:right">-</td>
    </tr>
    <tr>
      <td>ListTagsForResource</td>
       <td style="text-align:right">-</td>
    </tr>
    <tr>
      <td>ListVocabularyFilters</td>
       <td style="text-align:right">-</td>
    </tr>
    <tr>
      <td>StartCallAnalyticsJob</td>
       <td style="text-align:right">-</td>
    </tr>
    <tr>
      <td>TagResource</td>
       <td style="text-align:right">-</td>
    </tr>
    <tr>
      <td>UntagResource</td>
       <td style="text-align:right">-</td>
    </tr>
    <tr>
      <td>UpdateCallAnalyticsCategory</td>
       <td style="text-align:right">-</td>
    </tr>
    <tr>
      <td>UpdateMedicalVocabulary</td>
       <td style="text-align:right">-</td>
    </tr>
    <tr>
      <td>UpdateVocabulary</td>
       <td style="text-align:right">-</td>
    </tr>
    <tr>
      <td>UpdateVocabularyFilter</td>
       <td style="text-align:right">-</td>
    </tr>
  </tbody>
 </table>


## transfer ##

<table>
  <thead>
    <tr>
      <th>Operation</th>
      <th style="text-align:right">Implemented</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td>CreateServer (Pro)  <a href="#misc" title="covered by our integration test suite">✨</a></td>
       <td style="text-align:right">✅</td>
    </tr>
    <tr>
      <td>CreateUser (Pro)  <a href="#misc" title="covered by our integration test suite">✨</a></td>
       <td style="text-align:right">✅</td>
    </tr>
    <tr>
      <td>DeleteServer (Pro)  <a href="#misc" title="covered by our integration test suite">✨</a></td>
       <td style="text-align:right">✅</td>
    </tr>
    <tr>
      <td>DeleteSshPublicKey (Pro)  <a href="#misc" title="covered by our integration test suite">✨</a></td>
       <td style="text-align:right">✅</td>
    </tr>
    <tr>
      <td>DeleteUser (Pro)  <a href="#misc" title="covered by our integration test suite">✨</a></td>
       <td style="text-align:right">✅</td>
    </tr>
    <tr>
      <td>DescribeServer (Pro)  <a href="#misc" title="covered by our integration test suite">✨</a></td>
       <td style="text-align:right">✅</td>
    </tr>
    <tr>
      <td>DescribeUser (Pro)  <a href="#misc" title="covered by our integration test suite">✨</a></td>
       <td style="text-align:right">✅</td>
    </tr>
    <tr>
      <td>ImportSshPublicKey (Pro)  <a href="#misc" title="covered by our integration test suite">✨</a></td>
       <td style="text-align:right">✅</td>
    </tr>
    <tr>
      <td>ListServers (Pro) </td>
       <td style="text-align:right">✅</td>
    </tr>
    <tr>
      <td>ListUsers (Pro)  <a href="#misc" title="covered by our integration test suite">✨</a></td>
       <td style="text-align:right">✅</td>
    </tr>
    <tr>
      <td>UpdateUser (Pro)  <a href="#misc" title="covered by our integration test suite">✨</a></td>
       <td style="text-align:right">✅</td>
    </tr>
  </tbody>
  <tbody>    <tr>
      <td><a data-toggle="collapse" href=".transfer-notimplemented">Show missing</a></td>
      <td style="text-align:right"></td>
    </tr>
  </tbody>
  <tbody class="collapse transfer-notimplemented">     <tr>
      <td>CreateAccess</td>
       <td style="text-align:right">-</td>
    </tr>
    <tr>
      <td>CreateAgreement</td>
       <td style="text-align:right">-</td>
    </tr>
    <tr>
      <td>CreateConnector</td>
       <td style="text-align:right">-</td>
    </tr>
    <tr>
      <td>CreateProfile</td>
       <td style="text-align:right">-</td>
    </tr>
    <tr>
      <td>CreateWorkflow</td>
       <td style="text-align:right">-</td>
    </tr>
    <tr>
      <td>DeleteAccess</td>
       <td style="text-align:right">-</td>
    </tr>
    <tr>
      <td>DeleteAgreement</td>
       <td style="text-align:right">-</td>
    </tr>
    <tr>
      <td>DeleteCertificate</td>
       <td style="text-align:right">-</td>
    </tr>
    <tr>
      <td>DeleteConnector</td>
       <td style="text-align:right">-</td>
    </tr>
    <tr>
      <td>DeleteHostKey</td>
       <td style="text-align:right">-</td>
    </tr>
    <tr>
      <td>DeleteProfile</td>
       <td style="text-align:right">-</td>
    </tr>
    <tr>
      <td>DeleteWorkflow</td>
       <td style="text-align:right">-</td>
    </tr>
    <tr>
      <td>DescribeAccess</td>
       <td style="text-align:right">-</td>
    </tr>
    <tr>
      <td>DescribeAgreement</td>
       <td style="text-align:right">-</td>
    </tr>
    <tr>
      <td>DescribeCertificate</td>
       <td style="text-align:right">-</td>
    </tr>
    <tr>
      <td>DescribeConnector</td>
       <td style="text-align:right">-</td>
    </tr>
    <tr>
      <td>DescribeExecution</td>
       <td style="text-align:right">-</td>
    </tr>
    <tr>
      <td>DescribeHostKey</td>
       <td style="text-align:right">-</td>
    </tr>
    <tr>
      <td>DescribeProfile</td>
       <td style="text-align:right">-</td>
    </tr>
    <tr>
      <td>DescribeSecurityPolicy</td>
       <td style="text-align:right">-</td>
    </tr>
    <tr>
      <td>DescribeWorkflow</td>
       <td style="text-align:right">-</td>
    </tr>
    <tr>
      <td>ImportCertificate</td>
       <td style="text-align:right">-</td>
    </tr>
    <tr>
      <td>ImportHostKey</td>
       <td style="text-align:right">-</td>
    </tr>
    <tr>
      <td>ListAccesses</td>
       <td style="text-align:right">-</td>
    </tr>
    <tr>
      <td>ListAgreements</td>
       <td style="text-align:right">-</td>
    </tr>
    <tr>
      <td>ListCertificates</td>
       <td style="text-align:right">-</td>
    </tr>
    <tr>
      <td>ListConnectors</td>
       <td style="text-align:right">-</td>
    </tr>
    <tr>
      <td>ListExecutions</td>
       <td style="text-align:right">-</td>
    </tr>
    <tr>
      <td>ListHostKeys</td>
       <td style="text-align:right">-</td>
    </tr>
    <tr>
      <td>ListProfiles</td>
       <td style="text-align:right">-</td>
    </tr>
    <tr>
      <td>ListSecurityPolicies</td>
       <td style="text-align:right">-</td>
    </tr>
    <tr>
      <td>ListTagsForResource</td>
       <td style="text-align:right">-</td>
    </tr>
    <tr>
      <td>ListWorkflows</td>
       <td style="text-align:right">-</td>
    </tr>
    <tr>
      <td>SendWorkflowStepState</td>
       <td style="text-align:right">-</td>
    </tr>
    <tr>
      <td>StartFileTransfer</td>
       <td style="text-align:right">-</td>
    </tr>
    <tr>
      <td>StartServer</td>
       <td style="text-align:right">-</td>
    </tr>
    <tr>
      <td>StopServer</td>
       <td style="text-align:right">-</td>
    </tr>
    <tr>
      <td>TagResource</td>
       <td style="text-align:right">-</td>
    </tr>
    <tr>
      <td>TestIdentityProvider</td>
       <td style="text-align:right">-</td>
    </tr>
    <tr>
      <td>UntagResource</td>
       <td style="text-align:right">-</td>
    </tr>
    <tr>
      <td>UpdateAccess</td>
       <td style="text-align:right">-</td>
    </tr>
    <tr>
      <td>UpdateAgreement</td>
       <td style="text-align:right">-</td>
    </tr>
    <tr>
      <td>UpdateCertificate</td>
       <td style="text-align:right">-</td>
    </tr>
    <tr>
      <td>UpdateConnector</td>
       <td style="text-align:right">-</td>
    </tr>
    <tr>
      <td>UpdateHostKey</td>
       <td style="text-align:right">-</td>
    </tr>
    <tr>
      <td>UpdateProfile</td>
       <td style="text-align:right">-</td>
    </tr>
    <tr>
      <td>UpdateServer</td>
       <td style="text-align:right">-</td>
    </tr>
  </tbody>
 </table>


## xray ##

<table>
  <thead>
    <tr>
      <th>Operation</th>
      <th style="text-align:right">Implemented</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td>BatchGetTraces (Pro) </td>
       <td style="text-align:right">✅</td>
    </tr>
    <tr>
      <td>CreateSamplingRule (Pro)  <a href="#misc" title="covered by our integration test suite">✨</a></td>
       <td style="text-align:right">✅</td>
    </tr>
    <tr>
      <td>DeleteSamplingRule (Pro)  <a href="#misc" title="covered by our integration test suite">✨</a></td>
       <td style="text-align:right">✅</td>
    </tr>
    <tr>
      <td>GetSamplingRules (Pro)  <a href="#misc" title="covered by our integration test suite">✨</a></td>
       <td style="text-align:right">✅</td>
    </tr>
    <tr>
      <td>GetServiceGraph (Pro) </td>
       <td style="text-align:right">✅</td>
    </tr>
    <tr>
      <td>GetTraceGraph (Pro) </td>
       <td style="text-align:right">✅</td>
    </tr>
    <tr>
      <td>GetTraceSummaries (Pro)  <a href="#misc" title="covered by our integration test suite">✨</a></td>
       <td style="text-align:right">✅</td>
    </tr>
    <tr>
      <td>PutTelemetryRecords (Pro)  <a href="#misc" title="covered by our integration test suite">✨</a></td>
       <td style="text-align:right">✅</td>
    </tr>
    <tr>
      <td>PutTraceSegments (Pro)  <a href="#misc" title="covered by our integration test suite">✨</a></td>
       <td style="text-align:right">✅</td>
    </tr>
    <tr>
      <td>UpdateSamplingRule (Pro)  <a href="#misc" title="covered by our integration test suite">✨</a></td>
       <td style="text-align:right">✅</td>
    </tr>
  </tbody>
  <tbody>    <tr>
      <td><a data-toggle="collapse" href=".xray-notimplemented">Show missing</a></td>
      <td style="text-align:right"></td>
    </tr>
  </tbody>
  <tbody class="collapse xray-notimplemented">     <tr>
      <td>CreateGroup</td>
       <td style="text-align:right">-</td>
    </tr>
    <tr>
      <td>DeleteGroup</td>
       <td style="text-align:right">-</td>
    </tr>
    <tr>
      <td>GetEncryptionConfig</td>
       <td style="text-align:right">-</td>
    </tr>
    <tr>
      <td>GetGroup</td>
       <td style="text-align:right">-</td>
    </tr>
    <tr>
      <td>GetGroups</td>
       <td style="text-align:right">-</td>
    </tr>
    <tr>
      <td>GetInsight</td>
       <td style="text-align:right">-</td>
    </tr>
    <tr>
      <td>GetInsightEvents</td>
       <td style="text-align:right">-</td>
    </tr>
    <tr>
      <td>GetInsightImpactGraph</td>
       <td style="text-align:right">-</td>
    </tr>
    <tr>
      <td>GetInsightSummaries</td>
       <td style="text-align:right">-</td>
    </tr>
    <tr>
      <td>GetSamplingStatisticSummaries</td>
       <td style="text-align:right">-</td>
    </tr>
    <tr>
      <td>GetSamplingTargets</td>
       <td style="text-align:right">-</td>
    </tr>
    <tr>
      <td>GetTimeSeriesServiceStatistics</td>
       <td style="text-align:right">-</td>
    </tr>
    <tr>
      <td>ListTagsForResource</td>
       <td style="text-align:right">-</td>
    </tr>
    <tr>
      <td>PutEncryptionConfig</td>
       <td style="text-align:right">-</td>
    </tr>
    <tr>
      <td>TagResource</td>
       <td style="text-align:right">-</td>
    </tr>
    <tr>
      <td>UntagResource</td>
       <td style="text-align:right">-</td>
    </tr>
    <tr>
      <td>UpdateGroup</td>
       <td style="text-align:right">-</td>
    </tr>
  </tbody>
 </table>



## Misc ##

Endpoints marked with ✨ are covered by our integration test suite.

</div>