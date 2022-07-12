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
    <tr>
      <td><a data-toggle="collapse" href=".acm-notimplemented">Show more</a></td>
      <td style="text-align:right"></td>
    </tr>
    <tr class="collapse acm-notimplemented">
      <td>GetAccountConfiguration</td>
       <td style="text-align:right">-</td>
    </tr>
    <tr class="collapse acm-notimplemented">
      <td>PutAccountConfiguration</td>
       <td style="text-align:right">-</td>
    </tr>
    <tr class="collapse acm-notimplemented">
      <td>RenewCertificate</td>
       <td style="text-align:right">-</td>
    </tr>
    <tr class="collapse acm-notimplemented">
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
      <td>CreateApp <a href="#misc" title="covered by our integration test suite">✨</a></td>
       <td style="text-align:right">✅</td>
    </tr>
    <tr>
      <td>CreateBackendEnvironment <a href="#misc" title="covered by our integration test suite">✨</a></td>
       <td style="text-align:right">✅</td>
    </tr>
    <tr>
      <td>CreateBranch <a href="#misc" title="covered by our integration test suite">✨</a></td>
       <td style="text-align:right">✅</td>
    </tr>
    <tr>
      <td>CreateWebhook <a href="#misc" title="covered by our integration test suite">✨</a></td>
       <td style="text-align:right">✅</td>
    </tr>
    <tr>
      <td>DeleteApp <a href="#misc" title="covered by our integration test suite">✨</a></td>
       <td style="text-align:right">✅</td>
    </tr>
    <tr>
      <td>DeleteBackendEnvironment <a href="#misc" title="covered by our integration test suite">✨</a></td>
       <td style="text-align:right">✅</td>
    </tr>
    <tr>
      <td>DeleteBranch <a href="#misc" title="covered by our integration test suite">✨</a></td>
       <td style="text-align:right">✅</td>
    </tr>
    <tr>
      <td>DeleteWebhook <a href="#misc" title="covered by our integration test suite">✨</a></td>
       <td style="text-align:right">✅</td>
    </tr>
    <tr>
      <td>GetApp <a href="#misc" title="covered by our integration test suite">✨</a></td>
       <td style="text-align:right">✅</td>
    </tr>
    <tr>
      <td>GetBackendEnvironment <a href="#misc" title="covered by our integration test suite">✨</a></td>
       <td style="text-align:right">✅</td>
    </tr>
    <tr>
      <td>GetBranch <a href="#misc" title="covered by our integration test suite">✨</a></td>
       <td style="text-align:right">✅</td>
    </tr>
    <tr>
      <td>GetWebhook <a href="#misc" title="covered by our integration test suite">✨</a></td>
       <td style="text-align:right">✅</td>
    </tr>
    <tr>
      <td>ListApps <a href="#misc" title="covered by our integration test suite">✨</a></td>
       <td style="text-align:right">✅</td>
    </tr>
    <tr>
      <td>ListBranches <a href="#misc" title="covered by our integration test suite">✨</a></td>
       <td style="text-align:right">✅</td>
    </tr>
    <tr>
      <td>ListTagsForResource <a href="#misc" title="covered by our integration test suite">✨</a></td>
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
      <td>UpdateApp <a href="#misc" title="covered by our integration test suite">✨</a></td>
       <td style="text-align:right">✅</td>
    </tr>
    <tr>
      <td>UpdateWebhook <a href="#misc" title="covered by our integration test suite">✨</a></td>
       <td style="text-align:right">✅</td>
    </tr>
    <tr>
      <td><a data-toggle="collapse" href=".acm-notimplemented">Show more</a></td>
      <td style="text-align:right"></td>
    </tr>
    <tr class="collapse acm-notimplemented">
      <td>CreateDeployment</td>
       <td style="text-align:right">-</td>
    </tr>
    <tr class="collapse acm-notimplemented">
      <td>CreateDomainAssociation</td>
       <td style="text-align:right">-</td>
    </tr>
    <tr class="collapse acm-notimplemented">
      <td>DeleteDomainAssociation</td>
       <td style="text-align:right">-</td>
    </tr>
    <tr class="collapse acm-notimplemented">
      <td>DeleteJob</td>
       <td style="text-align:right">-</td>
    </tr>
    <tr class="collapse acm-notimplemented">
      <td>GenerateAccessLogs</td>
       <td style="text-align:right">-</td>
    </tr>
    <tr class="collapse acm-notimplemented">
      <td>GetArtifactUrl</td>
       <td style="text-align:right">-</td>
    </tr>
    <tr class="collapse acm-notimplemented">
      <td>GetDomainAssociation</td>
       <td style="text-align:right">-</td>
    </tr>
    <tr class="collapse acm-notimplemented">
      <td>GetJob</td>
       <td style="text-align:right">-</td>
    </tr>
    <tr class="collapse acm-notimplemented">
      <td>ListArtifacts</td>
       <td style="text-align:right">-</td>
    </tr>
    <tr class="collapse acm-notimplemented">
      <td>ListBackendEnvironments</td>
       <td style="text-align:right">-</td>
    </tr>
    <tr class="collapse acm-notimplemented">
      <td>ListDomainAssociations</td>
       <td style="text-align:right">-</td>
    </tr>
    <tr class="collapse acm-notimplemented">
      <td>ListJobs</td>
       <td style="text-align:right">-</td>
    </tr>
    <tr class="collapse acm-notimplemented">
      <td>ListWebhooks</td>
       <td style="text-align:right">-</td>
    </tr>
    <tr class="collapse acm-notimplemented">
      <td>StartDeployment</td>
       <td style="text-align:right">-</td>
    </tr>
    <tr class="collapse acm-notimplemented">
      <td>StartJob</td>
       <td style="text-align:right">-</td>
    </tr>
    <tr class="collapse acm-notimplemented">
      <td>StopJob</td>
       <td style="text-align:right">-</td>
    </tr>
    <tr class="collapse acm-notimplemented">
      <td>UpdateBranch</td>
       <td style="text-align:right">-</td>
    </tr>
    <tr class="collapse acm-notimplemented">
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
      <td>UpdateDeployment</td>
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
    <tr>
      <td><a data-toggle="collapse" href=".acm-notimplemented">Show more</a></td>
      <td style="text-align:right"></td>
    </tr>
    <tr class="collapse acm-notimplemented">
      <td>CreateDocumentationVersion</td>
       <td style="text-align:right">-</td>
    </tr>
    <tr class="collapse acm-notimplemented">
      <td>DeleteDocumentationVersion</td>
       <td style="text-align:right">-</td>
    </tr>
    <tr class="collapse acm-notimplemented">
      <td>FlushStageAuthorizersCache</td>
       <td style="text-align:right">-</td>
    </tr>
    <tr class="collapse acm-notimplemented">
      <td>FlushStageCache</td>
       <td style="text-align:right">-</td>
    </tr>
    <tr class="collapse acm-notimplemented">
      <td>GetDocumentationVersion</td>
       <td style="text-align:right">-</td>
    </tr>
    <tr class="collapse acm-notimplemented">
      <td>GetDocumentationVersions</td>
       <td style="text-align:right">-</td>
    </tr>
    <tr class="collapse acm-notimplemented">
      <td>GetModelTemplate</td>
       <td style="text-align:right">-</td>
    </tr>
    <tr class="collapse acm-notimplemented">
      <td>GetSdk</td>
       <td style="text-align:right">-</td>
    </tr>
    <tr class="collapse acm-notimplemented">
      <td>GetSdkType</td>
       <td style="text-align:right">-</td>
    </tr>
    <tr class="collapse acm-notimplemented">
      <td>GetSdkTypes</td>
       <td style="text-align:right">-</td>
    </tr>
    <tr class="collapse acm-notimplemented">
      <td>GetUsage</td>
       <td style="text-align:right">-</td>
    </tr>
    <tr class="collapse acm-notimplemented">
      <td>ImportDocumentationParts</td>
       <td style="text-align:right">-</td>
    </tr>
    <tr class="collapse acm-notimplemented">
      <td>UpdateDocumentationVersion</td>
       <td style="text-align:right">-</td>
    </tr>
    <tr class="collapse acm-notimplemented">
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
      <td>DeleteConnection</td>
       <td style="text-align:right">✅</td>
    </tr>
    <tr>
      <td>GetConnection</td>
       <td style="text-align:right">✅</td>
    </tr>
    <tr>
      <td>PostToConnection <a href="#misc" title="covered by our integration test suite">✨</a></td>
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
      <td>CreateApi <a href="#misc" title="covered by our integration test suite">✨</a></td>
       <td style="text-align:right">✅</td>
    </tr>
    <tr>
      <td>CreateApiMapping <a href="#misc" title="covered by our integration test suite">✨</a></td>
       <td style="text-align:right">✅</td>
    </tr>
    <tr>
      <td>CreateAuthorizer <a href="#misc" title="covered by our integration test suite">✨</a></td>
       <td style="text-align:right">✅</td>
    </tr>
    <tr>
      <td>CreateDeployment <a href="#misc" title="covered by our integration test suite">✨</a></td>
       <td style="text-align:right">✅</td>
    </tr>
    <tr>
      <td>CreateDomainName <a href="#misc" title="covered by our integration test suite">✨</a></td>
       <td style="text-align:right">✅</td>
    </tr>
    <tr>
      <td>CreateIntegration <a href="#misc" title="covered by our integration test suite">✨</a></td>
       <td style="text-align:right">✅</td>
    </tr>
    <tr>
      <td>CreateIntegrationResponse <a href="#misc" title="covered by our integration test suite">✨</a></td>
       <td style="text-align:right">✅</td>
    </tr>
    <tr>
      <td>CreateModel <a href="#misc" title="covered by our integration test suite">✨</a></td>
       <td style="text-align:right">✅</td>
    </tr>
    <tr>
      <td>CreateRoute <a href="#misc" title="covered by our integration test suite">✨</a></td>
       <td style="text-align:right">✅</td>
    </tr>
    <tr>
      <td>CreateRouteResponse <a href="#misc" title="covered by our integration test suite">✨</a></td>
       <td style="text-align:right">✅</td>
    </tr>
    <tr>
      <td>CreateStage <a href="#misc" title="covered by our integration test suite">✨</a></td>
       <td style="text-align:right">✅</td>
    </tr>
    <tr>
      <td>CreateVpcLink <a href="#misc" title="covered by our integration test suite">✨</a></td>
       <td style="text-align:right">✅</td>
    </tr>
    <tr>
      <td>DeleteApi <a href="#misc" title="covered by our integration test suite">✨</a></td>
       <td style="text-align:right">✅</td>
    </tr>
    <tr>
      <td>DeleteApiMapping</td>
       <td style="text-align:right">✅</td>
    </tr>
    <tr>
      <td>DeleteAuthorizer <a href="#misc" title="covered by our integration test suite">✨</a></td>
       <td style="text-align:right">✅</td>
    </tr>
    <tr>
      <td>DeleteCorsConfiguration</td>
       <td style="text-align:right">✅</td>
    </tr>
    <tr>
      <td>DeleteDeployment <a href="#misc" title="covered by our integration test suite">✨</a></td>
       <td style="text-align:right">✅</td>
    </tr>
    <tr>
      <td>DeleteDomainName <a href="#misc" title="covered by our integration test suite">✨</a></td>
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
      <td>DeleteModel</td>
       <td style="text-align:right">✅</td>
    </tr>
    <tr>
      <td>DeleteRoute <a href="#misc" title="covered by our integration test suite">✨</a></td>
       <td style="text-align:right">✅</td>
    </tr>
    <tr>
      <td>DeleteRouteResponse <a href="#misc" title="covered by our integration test suite">✨</a></td>
       <td style="text-align:right">✅</td>
    </tr>
    <tr>
      <td>DeleteStage <a href="#misc" title="covered by our integration test suite">✨</a></td>
       <td style="text-align:right">✅</td>
    </tr>
    <tr>
      <td>DeleteVpcLink <a href="#misc" title="covered by our integration test suite">✨</a></td>
       <td style="text-align:right">✅</td>
    </tr>
    <tr>
      <td>GetApi <a href="#misc" title="covered by our integration test suite">✨</a></td>
       <td style="text-align:right">✅</td>
    </tr>
    <tr>
      <td>GetApiMapping</td>
       <td style="text-align:right">✅</td>
    </tr>
    <tr>
      <td>GetApiMappings</td>
       <td style="text-align:right">✅</td>
    </tr>
    <tr>
      <td>GetApis <a href="#misc" title="covered by our integration test suite">✨</a></td>
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
      <td>GetDeployment <a href="#misc" title="covered by our integration test suite">✨</a></td>
       <td style="text-align:right">✅</td>
    </tr>
    <tr>
      <td>GetDeployments <a href="#misc" title="covered by our integration test suite">✨</a></td>
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
      <td>GetIntegration <a href="#misc" title="covered by our integration test suite">✨</a></td>
       <td style="text-align:right">✅</td>
    </tr>
    <tr>
      <td>GetIntegrationResponse <a href="#misc" title="covered by our integration test suite">✨</a></td>
       <td style="text-align:right">✅</td>
    </tr>
    <tr>
      <td>GetIntegrationResponses <a href="#misc" title="covered by our integration test suite">✨</a></td>
       <td style="text-align:right">✅</td>
    </tr>
    <tr>
      <td>GetIntegrations <a href="#misc" title="covered by our integration test suite">✨</a></td>
       <td style="text-align:right">✅</td>
    </tr>
    <tr>
      <td>GetModel</td>
       <td style="text-align:right">✅</td>
    </tr>
    <tr>
      <td>GetModels <a href="#misc" title="covered by our integration test suite">✨</a></td>
       <td style="text-align:right">✅</td>
    </tr>
    <tr>
      <td>GetRoute <a href="#misc" title="covered by our integration test suite">✨</a></td>
       <td style="text-align:right">✅</td>
    </tr>
    <tr>
      <td>GetRouteResponse <a href="#misc" title="covered by our integration test suite">✨</a></td>
       <td style="text-align:right">✅</td>
    </tr>
    <tr>
      <td>GetRouteResponses <a href="#misc" title="covered by our integration test suite">✨</a></td>
       <td style="text-align:right">✅</td>
    </tr>
    <tr>
      <td>GetRoutes <a href="#misc" title="covered by our integration test suite">✨</a></td>
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
      <td>GetTags</td>
       <td style="text-align:right">✅</td>
    </tr>
    <tr>
      <td>GetVpcLink</td>
       <td style="text-align:right">✅</td>
    </tr>
    <tr>
      <td>GetVpcLinks <a href="#misc" title="covered by our integration test suite">✨</a></td>
       <td style="text-align:right">✅</td>
    </tr>
    <tr>
      <td>ImportApi <a href="#misc" title="covered by our integration test suite">✨</a></td>
       <td style="text-align:right">✅</td>
    </tr>
    <tr>
      <td>ReimportApi <a href="#misc" title="covered by our integration test suite">✨</a></td>
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
      <td>UpdateApi</td>
       <td style="text-align:right">✅</td>
    </tr>
    <tr>
      <td>UpdateApiMapping</td>
       <td style="text-align:right">✅</td>
    </tr>
    <tr>
      <td>UpdateAuthorizer</td>
       <td style="text-align:right">✅</td>
    </tr>
    <tr>
      <td>UpdateDeployment</td>
       <td style="text-align:right">✅</td>
    </tr>
    <tr>
      <td>UpdateDomainName</td>
       <td style="text-align:right">✅</td>
    </tr>
    <tr>
      <td>UpdateIntegration <a href="#misc" title="covered by our integration test suite">✨</a></td>
       <td style="text-align:right">✅</td>
    </tr>
    <tr>
      <td>UpdateIntegrationResponse <a href="#misc" title="covered by our integration test suite">✨</a></td>
       <td style="text-align:right">✅</td>
    </tr>
    <tr>
      <td>UpdateModel</td>
       <td style="text-align:right">✅</td>
    </tr>
    <tr>
      <td>UpdateRoute <a href="#misc" title="covered by our integration test suite">✨</a></td>
       <td style="text-align:right">✅</td>
    </tr>
    <tr>
      <td>UpdateRouteResponse <a href="#misc" title="covered by our integration test suite">✨</a></td>
       <td style="text-align:right">✅</td>
    </tr>
    <tr>
      <td>UpdateStage <a href="#misc" title="covered by our integration test suite">✨</a></td>
       <td style="text-align:right">✅</td>
    </tr>
    <tr>
      <td>UpdateVpcLink</td>
       <td style="text-align:right">✅</td>
    </tr>
    <tr>
      <td><a data-toggle="collapse" href=".acm-notimplemented">Show more</a></td>
      <td style="text-align:right"></td>
    </tr>
    <tr class="collapse acm-notimplemented">
      <td>DeleteAccessLogSettings</td>
       <td style="text-align:right">-</td>
    </tr>
    <tr class="collapse acm-notimplemented">
      <td>DeleteRouteRequestParameter</td>
       <td style="text-align:right">-</td>
    </tr>
    <tr class="collapse acm-notimplemented">
      <td>DeleteRouteSettings</td>
       <td style="text-align:right">-</td>
    </tr>
    <tr class="collapse acm-notimplemented">
      <td>ExportApi</td>
       <td style="text-align:right">-</td>
    </tr>
    <tr class="collapse acm-notimplemented">
      <td>GetModelTemplate</td>
       <td style="text-align:right">-</td>
    </tr>
    <tr class="collapse acm-notimplemented">
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
      <td>CreateApplication <a href="#misc" title="covered by our integration test suite">✨</a></td>
       <td style="text-align:right">✅</td>
    </tr>
    <tr>
      <td>CreateConfigurationProfile <a href="#misc" title="covered by our integration test suite">✨</a></td>
       <td style="text-align:right">✅</td>
    </tr>
    <tr>
      <td>CreateDeploymentStrategy <a href="#misc" title="covered by our integration test suite">✨</a></td>
       <td style="text-align:right">✅</td>
    </tr>
    <tr>
      <td>CreateEnvironment <a href="#misc" title="covered by our integration test suite">✨</a></td>
       <td style="text-align:right">✅</td>
    </tr>
    <tr>
      <td>CreateHostedConfigurationVersion <a href="#misc" title="covered by our integration test suite">✨</a></td>
       <td style="text-align:right">✅</td>
    </tr>
    <tr>
      <td>DeleteApplication <a href="#misc" title="covered by our integration test suite">✨</a></td>
       <td style="text-align:right">✅</td>
    </tr>
    <tr>
      <td>DeleteConfigurationProfile <a href="#misc" title="covered by our integration test suite">✨</a></td>
       <td style="text-align:right">✅</td>
    </tr>
    <tr>
      <td>DeleteDeploymentStrategy <a href="#misc" title="covered by our integration test suite">✨</a></td>
       <td style="text-align:right">✅</td>
    </tr>
    <tr>
      <td>DeleteEnvironment <a href="#misc" title="covered by our integration test suite">✨</a></td>
       <td style="text-align:right">✅</td>
    </tr>
    <tr>
      <td>DeleteHostedConfigurationVersion <a href="#misc" title="covered by our integration test suite">✨</a></td>
       <td style="text-align:right">✅</td>
    </tr>
    <tr>
      <td>GetApplication <a href="#misc" title="covered by our integration test suite">✨</a></td>
       <td style="text-align:right">✅</td>
    </tr>
    <tr>
      <td>GetConfiguration <a href="#misc" title="covered by our integration test suite">✨</a></td>
       <td style="text-align:right">✅</td>
    </tr>
    <tr>
      <td>GetConfigurationProfile <a href="#misc" title="covered by our integration test suite">✨</a></td>
       <td style="text-align:right">✅</td>
    </tr>
    <tr>
      <td>GetDeployment</td>
       <td style="text-align:right">✅</td>
    </tr>
    <tr>
      <td>GetDeploymentStrategy <a href="#misc" title="covered by our integration test suite">✨</a></td>
       <td style="text-align:right">✅</td>
    </tr>
    <tr>
      <td>GetEnvironment <a href="#misc" title="covered by our integration test suite">✨</a></td>
       <td style="text-align:right">✅</td>
    </tr>
    <tr>
      <td>GetHostedConfigurationVersion <a href="#misc" title="covered by our integration test suite">✨</a></td>
       <td style="text-align:right">✅</td>
    </tr>
    <tr>
      <td>ListApplications <a href="#misc" title="covered by our integration test suite">✨</a></td>
       <td style="text-align:right">✅</td>
    </tr>
    <tr>
      <td>ListConfigurationProfiles <a href="#misc" title="covered by our integration test suite">✨</a></td>
       <td style="text-align:right">✅</td>
    </tr>
    <tr>
      <td>ListDeploymentStrategies <a href="#misc" title="covered by our integration test suite">✨</a></td>
       <td style="text-align:right">✅</td>
    </tr>
    <tr>
      <td>ListDeployments <a href="#misc" title="covered by our integration test suite">✨</a></td>
       <td style="text-align:right">✅</td>
    </tr>
    <tr>
      <td>ListEnvironments <a href="#misc" title="covered by our integration test suite">✨</a></td>
       <td style="text-align:right">✅</td>
    </tr>
    <tr>
      <td>ListHostedConfigurationVersions <a href="#misc" title="covered by our integration test suite">✨</a></td>
       <td style="text-align:right">✅</td>
    </tr>
    <tr>
      <td>ListTagsForResource</td>
       <td style="text-align:right">✅</td>
    </tr>
    <tr>
      <td>StartDeployment <a href="#misc" title="covered by our integration test suite">✨</a></td>
       <td style="text-align:right">✅</td>
    </tr>
    <tr>
      <td>StopDeployment</td>
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
      <td>UpdateApplication <a href="#misc" title="covered by our integration test suite">✨</a></td>
       <td style="text-align:right">✅</td>
    </tr>
    <tr>
      <td>UpdateConfigurationProfile <a href="#misc" title="covered by our integration test suite">✨</a></td>
       <td style="text-align:right">✅</td>
    </tr>
    <tr>
      <td>UpdateDeploymentStrategy <a href="#misc" title="covered by our integration test suite">✨</a></td>
       <td style="text-align:right">✅</td>
    </tr>
    <tr>
      <td>UpdateEnvironment <a href="#misc" title="covered by our integration test suite">✨</a></td>
       <td style="text-align:right">✅</td>
    </tr>
    <tr>
      <td>ValidateConfiguration <a href="#misc" title="covered by our integration test suite">✨</a></td>
       <td style="text-align:right">✅</td>
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
      <td>DeleteScalingPolicy <a href="#misc" title="covered by our integration test suite">✨</a></td>
       <td style="text-align:right">✅</td>
    </tr>
    <tr>
      <td>DeleteScheduledAction</td>
       <td style="text-align:right">✅</td>
    </tr>
    <tr>
      <td>DeregisterScalableTarget <a href="#misc" title="covered by our integration test suite">✨</a></td>
       <td style="text-align:right">✅</td>
    </tr>
    <tr>
      <td>DescribeScalableTargets <a href="#misc" title="covered by our integration test suite">✨</a></td>
       <td style="text-align:right">✅</td>
    </tr>
    <tr>
      <td>DescribeScalingPolicies <a href="#misc" title="covered by our integration test suite">✨</a></td>
       <td style="text-align:right">✅</td>
    </tr>
    <tr>
      <td>DescribeScheduledActions</td>
       <td style="text-align:right">✅</td>
    </tr>
    <tr>
      <td>PutScalingPolicy <a href="#misc" title="covered by our integration test suite">✨</a></td>
       <td style="text-align:right">✅</td>
    </tr>
    <tr>
      <td>PutScheduledAction</td>
       <td style="text-align:right">✅</td>
    </tr>
    <tr>
      <td>RegisterScalableTarget <a href="#misc" title="covered by our integration test suite">✨</a></td>
       <td style="text-align:right">✅</td>
    </tr>
    <tr>
      <td><a data-toggle="collapse" href=".acm-notimplemented">Show more</a></td>
      <td style="text-align:right"></td>
    </tr>
    <tr class="collapse acm-notimplemented">
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
      <td>CreateApiCache <a href="#misc" title="covered by our integration test suite">✨</a></td>
       <td style="text-align:right">✅</td>
    </tr>
    <tr>
      <td>CreateApiKey <a href="#misc" title="covered by our integration test suite">✨</a></td>
       <td style="text-align:right">✅</td>
    </tr>
    <tr>
      <td>CreateDataSource <a href="#misc" title="covered by our integration test suite">✨</a></td>
       <td style="text-align:right">✅</td>
    </tr>
    <tr>
      <td>CreateDomainName</td>
       <td style="text-align:right">✅</td>
    </tr>
    <tr>
      <td>CreateFunction <a href="#misc" title="covered by our integration test suite">✨</a></td>
       <td style="text-align:right">✅</td>
    </tr>
    <tr>
      <td>CreateGraphqlApi <a href="#misc" title="covered by our integration test suite">✨</a></td>
       <td style="text-align:right">✅</td>
    </tr>
    <tr>
      <td>CreateResolver <a href="#misc" title="covered by our integration test suite">✨</a></td>
       <td style="text-align:right">✅</td>
    </tr>
    <tr>
      <td>CreateType</td>
       <td style="text-align:right">✅</td>
    </tr>
    <tr>
      <td>DeleteApiCache</td>
       <td style="text-align:right">✅</td>
    </tr>
    <tr>
      <td>DeleteApiKey</td>
       <td style="text-align:right">✅</td>
    </tr>
    <tr>
      <td>DeleteDataSource</td>
       <td style="text-align:right">✅</td>
    </tr>
    <tr>
      <td>DeleteDomainName</td>
       <td style="text-align:right">✅</td>
    </tr>
    <tr>
      <td>DeleteFunction</td>
       <td style="text-align:right">✅</td>
    </tr>
    <tr>
      <td>DeleteGraphqlApi <a href="#misc" title="covered by our integration test suite">✨</a></td>
       <td style="text-align:right">✅</td>
    </tr>
    <tr>
      <td>DeleteResolver <a href="#misc" title="covered by our integration test suite">✨</a></td>
       <td style="text-align:right">✅</td>
    </tr>
    <tr>
      <td>DeleteType</td>
       <td style="text-align:right">✅</td>
    </tr>
    <tr>
      <td>FlushApiCache</td>
       <td style="text-align:right">✅</td>
    </tr>
    <tr>
      <td>GetApiCache</td>
       <td style="text-align:right">✅</td>
    </tr>
    <tr>
      <td>GetDataSource</td>
       <td style="text-align:right">✅</td>
    </tr>
    <tr>
      <td>GetDomainName</td>
       <td style="text-align:right">✅</td>
    </tr>
    <tr>
      <td>GetFunction <a href="#misc" title="covered by our integration test suite">✨</a></td>
       <td style="text-align:right">✅</td>
    </tr>
    <tr>
      <td>GetGraphqlApi <a href="#misc" title="covered by our integration test suite">✨</a></td>
       <td style="text-align:right">✅</td>
    </tr>
    <tr>
      <td>GetIntrospectionSchema <a href="#misc" title="covered by our integration test suite">✨</a></td>
       <td style="text-align:right">✅</td>
    </tr>
    <tr>
      <td>GetResolver <a href="#misc" title="covered by our integration test suite">✨</a></td>
       <td style="text-align:right">✅</td>
    </tr>
    <tr>
      <td>GetSchemaCreationStatus <a href="#misc" title="covered by our integration test suite">✨</a></td>
       <td style="text-align:right">✅</td>
    </tr>
    <tr>
      <td>GetType</td>
       <td style="text-align:right">✅</td>
    </tr>
    <tr>
      <td>ListApiKeys <a href="#misc" title="covered by our integration test suite">✨</a></td>
       <td style="text-align:right">✅</td>
    </tr>
    <tr>
      <td>ListDataSources <a href="#misc" title="covered by our integration test suite">✨</a></td>
       <td style="text-align:right">✅</td>
    </tr>
    <tr>
      <td>ListDomainNames</td>
       <td style="text-align:right">✅</td>
    </tr>
    <tr>
      <td>ListFunctions <a href="#misc" title="covered by our integration test suite">✨</a></td>
       <td style="text-align:right">✅</td>
    </tr>
    <tr>
      <td>ListGraphqlApis <a href="#misc" title="covered by our integration test suite">✨</a></td>
       <td style="text-align:right">✅</td>
    </tr>
    <tr>
      <td>ListResolvers <a href="#misc" title="covered by our integration test suite">✨</a></td>
       <td style="text-align:right">✅</td>
    </tr>
    <tr>
      <td>ListResolversByFunction</td>
       <td style="text-align:right">✅</td>
    </tr>
    <tr>
      <td>ListTagsForResource <a href="#misc" title="covered by our integration test suite">✨</a></td>
       <td style="text-align:right">✅</td>
    </tr>
    <tr>
      <td>ListTypes</td>
       <td style="text-align:right">✅</td>
    </tr>
    <tr>
      <td>StartSchemaCreation <a href="#misc" title="covered by our integration test suite">✨</a></td>
       <td style="text-align:right">✅</td>
    </tr>
    <tr>
      <td>TagResource <a href="#misc" title="covered by our integration test suite">✨</a></td>
       <td style="text-align:right">✅</td>
    </tr>
    <tr>
      <td>UntagResource</td>
       <td style="text-align:right">✅</td>
    </tr>
    <tr>
      <td>UpdateApiCache <a href="#misc" title="covered by our integration test suite">✨</a></td>
       <td style="text-align:right">✅</td>
    </tr>
    <tr>
      <td>UpdateApiKey <a href="#misc" title="covered by our integration test suite">✨</a></td>
       <td style="text-align:right">✅</td>
    </tr>
    <tr>
      <td>UpdateDataSource</td>
       <td style="text-align:right">✅</td>
    </tr>
    <tr>
      <td>UpdateDomainName</td>
       <td style="text-align:right">✅</td>
    </tr>
    <tr>
      <td>UpdateFunction</td>
       <td style="text-align:right">✅</td>
    </tr>
    <tr>
      <td>UpdateGraphqlApi</td>
       <td style="text-align:right">✅</td>
    </tr>
    <tr>
      <td>UpdateResolver <a href="#misc" title="covered by our integration test suite">✨</a></td>
       <td style="text-align:right">✅</td>
    </tr>
    <tr>
      <td>UpdateType</td>
       <td style="text-align:right">✅</td>
    </tr>
    <tr>
      <td><a data-toggle="collapse" href=".acm-notimplemented">Show more</a></td>
      <td style="text-align:right"></td>
    </tr>
    <tr class="collapse acm-notimplemented">
      <td>AssociateApi</td>
       <td style="text-align:right">-</td>
    </tr>
    <tr class="collapse acm-notimplemented">
      <td>DisassociateApi</td>
       <td style="text-align:right">-</td>
    </tr>
    <tr class="collapse acm-notimplemented">
      <td>GetApiAssociation</td>
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
      <td>BatchGetPreparedStatement</td>
       <td style="text-align:right">✅</td>
    </tr>
    <tr>
      <td>CreateDataCatalog <a href="#misc" title="covered by our integration test suite">✨</a></td>
       <td style="text-align:right">✅</td>
    </tr>
    <tr>
      <td>CreateNamedQuery <a href="#misc" title="covered by our integration test suite">✨</a></td>
       <td style="text-align:right">✅</td>
    </tr>
    <tr>
      <td>CreateWorkGroup <a href="#misc" title="covered by our integration test suite">✨</a></td>
       <td style="text-align:right">✅</td>
    </tr>
    <tr>
      <td>DeleteDataCatalog <a href="#misc" title="covered by our integration test suite">✨</a></td>
       <td style="text-align:right">✅</td>
    </tr>
    <tr>
      <td>DeleteNamedQuery <a href="#misc" title="covered by our integration test suite">✨</a></td>
       <td style="text-align:right">✅</td>
    </tr>
    <tr>
      <td>DeleteWorkGroup <a href="#misc" title="covered by our integration test suite">✨</a></td>
       <td style="text-align:right">✅</td>
    </tr>
    <tr>
      <td>GetDataCatalog <a href="#misc" title="covered by our integration test suite">✨</a></td>
       <td style="text-align:right">✅</td>
    </tr>
    <tr>
      <td>GetDatabase</td>
       <td style="text-align:right">✅</td>
    </tr>
    <tr>
      <td>GetNamedQuery</td>
       <td style="text-align:right">✅</td>
    </tr>
    <tr>
      <td>GetQueryExecution</td>
       <td style="text-align:right">✅</td>
    </tr>
    <tr>
      <td>GetQueryResults</td>
       <td style="text-align:right">✅</td>
    </tr>
    <tr>
      <td>GetWorkGroup <a href="#misc" title="covered by our integration test suite">✨</a></td>
       <td style="text-align:right">✅</td>
    </tr>
    <tr>
      <td>ListDataCatalogs <a href="#misc" title="covered by our integration test suite">✨</a></td>
       <td style="text-align:right">✅</td>
    </tr>
    <tr>
      <td>ListDatabases</td>
       <td style="text-align:right">✅</td>
    </tr>
    <tr>
      <td>ListNamedQueries <a href="#misc" title="covered by our integration test suite">✨</a></td>
       <td style="text-align:right">✅</td>
    </tr>
    <tr>
      <td>ListQueryExecutions</td>
       <td style="text-align:right">✅</td>
    </tr>
    <tr>
      <td>ListTagsForResource <a href="#misc" title="covered by our integration test suite">✨</a></td>
       <td style="text-align:right">✅</td>
    </tr>
    <tr>
      <td>ListWorkGroups <a href="#misc" title="covered by our integration test suite">✨</a></td>
       <td style="text-align:right">✅</td>
    </tr>
    <tr>
      <td>StartQueryExecution</td>
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
      <td><a data-toggle="collapse" href=".acm-notimplemented">Show more</a></td>
      <td style="text-align:right"></td>
    </tr>
    <tr class="collapse acm-notimplemented">
      <td>BatchGetNamedQuery</td>
       <td style="text-align:right">-</td>
    </tr>
    <tr class="collapse acm-notimplemented">
      <td>BatchGetQueryExecution</td>
       <td style="text-align:right">-</td>
    </tr>
    <tr class="collapse acm-notimplemented">
      <td>CreatePreparedStatement</td>
       <td style="text-align:right">-</td>
    </tr>
    <tr class="collapse acm-notimplemented">
      <td>DeletePreparedStatement</td>
       <td style="text-align:right">-</td>
    </tr>
    <tr class="collapse acm-notimplemented">
      <td>GetPreparedStatement</td>
       <td style="text-align:right">-</td>
    </tr>
    <tr class="collapse acm-notimplemented">
      <td>GetTableMetadata</td>
       <td style="text-align:right">-</td>
    </tr>
    <tr class="collapse acm-notimplemented">
      <td>ListEngineVersions</td>
       <td style="text-align:right">-</td>
    </tr>
    <tr class="collapse acm-notimplemented">
      <td>ListPreparedStatements</td>
       <td style="text-align:right">-</td>
    </tr>
    <tr class="collapse acm-notimplemented">
      <td>ListTableMetadata</td>
       <td style="text-align:right">-</td>
    </tr>
    <tr class="collapse acm-notimplemented">
      <td>StopQueryExecution</td>
       <td style="text-align:right">-</td>
    </tr>
    <tr class="collapse acm-notimplemented">
      <td>UpdateDataCatalog</td>
       <td style="text-align:right">-</td>
    </tr>
    <tr class="collapse acm-notimplemented">
      <td>UpdateNamedQuery</td>
       <td style="text-align:right">-</td>
    </tr>
    <tr class="collapse acm-notimplemented">
      <td>UpdatePreparedStatement</td>
       <td style="text-align:right">-</td>
    </tr>
    <tr class="collapse acm-notimplemented">
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
      <td>AttachInstances</td>
       <td style="text-align:right">✅</td>
    </tr>
    <tr>
      <td>AttachLoadBalancerTargetGroups</td>
       <td style="text-align:right">✅</td>
    </tr>
    <tr>
      <td>AttachLoadBalancers</td>
       <td style="text-align:right">✅</td>
    </tr>
    <tr>
      <td>CreateAutoScalingGroup</td>
       <td style="text-align:right">✅</td>
    </tr>
    <tr>
      <td>CreateLaunchConfiguration</td>
       <td style="text-align:right">✅</td>
    </tr>
    <tr>
      <td>CreateOrUpdateTags</td>
       <td style="text-align:right">✅</td>
    </tr>
    <tr>
      <td>DeleteAutoScalingGroup</td>
       <td style="text-align:right">✅</td>
    </tr>
    <tr>
      <td>DeleteLaunchConfiguration</td>
       <td style="text-align:right">✅</td>
    </tr>
    <tr>
      <td>DeleteLifecycleHook</td>
       <td style="text-align:right">✅</td>
    </tr>
    <tr>
      <td>DeletePolicy</td>
       <td style="text-align:right">✅</td>
    </tr>
    <tr>
      <td>DeleteTags</td>
       <td style="text-align:right">✅</td>
    </tr>
    <tr>
      <td>DescribeAutoScalingGroups</td>
       <td style="text-align:right">✅</td>
    </tr>
    <tr>
      <td>DescribeAutoScalingInstances</td>
       <td style="text-align:right">✅</td>
    </tr>
    <tr>
      <td>DescribeLaunchConfigurations</td>
       <td style="text-align:right">✅</td>
    </tr>
    <tr>
      <td>DescribeLifecycleHooks</td>
       <td style="text-align:right">✅</td>
    </tr>
    <tr>
      <td>DescribeLoadBalancerTargetGroups</td>
       <td style="text-align:right">✅</td>
    </tr>
    <tr>
      <td>DescribeLoadBalancers</td>
       <td style="text-align:right">✅</td>
    </tr>
    <tr>
      <td>DescribeMetricCollectionTypes <a href="#misc" title="covered by our integration test suite">✨</a></td>
       <td style="text-align:right">✅</td>
    </tr>
    <tr>
      <td>DescribePolicies</td>
       <td style="text-align:right">✅</td>
    </tr>
    <tr>
      <td>DescribeTags</td>
       <td style="text-align:right">✅</td>
    </tr>
    <tr>
      <td>DetachInstances</td>
       <td style="text-align:right">✅</td>
    </tr>
    <tr>
      <td>DetachLoadBalancerTargetGroups</td>
       <td style="text-align:right">✅</td>
    </tr>
    <tr>
      <td>DetachLoadBalancers</td>
       <td style="text-align:right">✅</td>
    </tr>
    <tr>
      <td>DisableMetricsCollection <a href="#misc" title="covered by our integration test suite">✨</a></td>
       <td style="text-align:right">✅</td>
    </tr>
    <tr>
      <td>EnableMetricsCollection <a href="#misc" title="covered by our integration test suite">✨</a></td>
       <td style="text-align:right">✅</td>
    </tr>
    <tr>
      <td>EnterStandby</td>
       <td style="text-align:right">✅</td>
    </tr>
    <tr>
      <td>ExecutePolicy</td>
       <td style="text-align:right">✅</td>
    </tr>
    <tr>
      <td>ExitStandby</td>
       <td style="text-align:right">✅</td>
    </tr>
    <tr>
      <td>PutLifecycleHook</td>
       <td style="text-align:right">✅</td>
    </tr>
    <tr>
      <td>PutScalingPolicy</td>
       <td style="text-align:right">✅</td>
    </tr>
    <tr>
      <td>ResumeProcesses</td>
       <td style="text-align:right">✅</td>
    </tr>
    <tr>
      <td>SetDesiredCapacity</td>
       <td style="text-align:right">✅</td>
    </tr>
    <tr>
      <td>SetInstanceHealth</td>
       <td style="text-align:right">✅</td>
    </tr>
    <tr>
      <td>SetInstanceProtection</td>
       <td style="text-align:right">✅</td>
    </tr>
    <tr>
      <td>SuspendProcesses</td>
       <td style="text-align:right">✅</td>
    </tr>
    <tr>
      <td>TerminateInstanceInAutoScalingGroup</td>
       <td style="text-align:right">✅</td>
    </tr>
    <tr>
      <td>UpdateAutoScalingGroup</td>
       <td style="text-align:right">✅</td>
    </tr>
    <tr>
      <td><a data-toggle="collapse" href=".acm-notimplemented">Show more</a></td>
      <td style="text-align:right"></td>
    </tr>
    <tr class="collapse acm-notimplemented">
      <td>BatchDeleteScheduledAction</td>
       <td style="text-align:right">-</td>
    </tr>
    <tr class="collapse acm-notimplemented">
      <td>BatchPutScheduledUpdateGroupAction</td>
       <td style="text-align:right">-</td>
    </tr>
    <tr class="collapse acm-notimplemented">
      <td>CancelInstanceRefresh</td>
       <td style="text-align:right">-</td>
    </tr>
    <tr class="collapse acm-notimplemented">
      <td>CompleteLifecycleAction</td>
       <td style="text-align:right">-</td>
    </tr>
    <tr class="collapse acm-notimplemented">
      <td>DeleteNotificationConfiguration</td>
       <td style="text-align:right">-</td>
    </tr>
    <tr class="collapse acm-notimplemented">
      <td>DeleteScheduledAction</td>
       <td style="text-align:right">-</td>
    </tr>
    <tr class="collapse acm-notimplemented">
      <td>DeleteWarmPool</td>
       <td style="text-align:right">-</td>
    </tr>
    <tr class="collapse acm-notimplemented">
      <td>DescribeAccountLimits</td>
       <td style="text-align:right">-</td>
    </tr>
    <tr class="collapse acm-notimplemented">
      <td>DescribeAdjustmentTypes</td>
       <td style="text-align:right">-</td>
    </tr>
    <tr class="collapse acm-notimplemented">
      <td>DescribeAutoScalingNotificationTypes</td>
       <td style="text-align:right">-</td>
    </tr>
    <tr class="collapse acm-notimplemented">
      <td>DescribeInstanceRefreshes</td>
       <td style="text-align:right">-</td>
    </tr>
    <tr class="collapse acm-notimplemented">
      <td>DescribeLifecycleHookTypes</td>
       <td style="text-align:right">-</td>
    </tr>
    <tr class="collapse acm-notimplemented">
      <td>DescribeNotificationConfigurations</td>
       <td style="text-align:right">-</td>
    </tr>
    <tr class="collapse acm-notimplemented">
      <td>DescribeScalingActivities</td>
       <td style="text-align:right">-</td>
    </tr>
    <tr class="collapse acm-notimplemented">
      <td>DescribeScalingProcessTypes</td>
       <td style="text-align:right">-</td>
    </tr>
    <tr class="collapse acm-notimplemented">
      <td>DescribeScheduledActions</td>
       <td style="text-align:right">-</td>
    </tr>
    <tr class="collapse acm-notimplemented">
      <td>DescribeTerminationPolicyTypes</td>
       <td style="text-align:right">-</td>
    </tr>
    <tr class="collapse acm-notimplemented">
      <td>DescribeWarmPool</td>
       <td style="text-align:right">-</td>
    </tr>
    <tr class="collapse acm-notimplemented">
      <td>GetPredictiveScalingForecast</td>
       <td style="text-align:right">-</td>
    </tr>
    <tr class="collapse acm-notimplemented">
      <td>PutNotificationConfiguration</td>
       <td style="text-align:right">-</td>
    </tr>
    <tr class="collapse acm-notimplemented">
      <td>PutScheduledUpdateGroupAction</td>
       <td style="text-align:right">-</td>
    </tr>
    <tr class="collapse acm-notimplemented">
      <td>PutWarmPool</td>
       <td style="text-align:right">-</td>
    </tr>
    <tr class="collapse acm-notimplemented">
      <td>RecordLifecycleActionHeartbeat</td>
       <td style="text-align:right">-</td>
    </tr>
    <tr class="collapse acm-notimplemented">
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
      <td>CreateBackupPlan <a href="#misc" title="covered by our integration test suite">✨</a></td>
       <td style="text-align:right">✅</td>
    </tr>
    <tr>
      <td>CreateBackupSelection <a href="#misc" title="covered by our integration test suite">✨</a></td>
       <td style="text-align:right">✅</td>
    </tr>
    <tr>
      <td>CreateBackupVault <a href="#misc" title="covered by our integration test suite">✨</a></td>
       <td style="text-align:right">✅</td>
    </tr>
    <tr>
      <td>DeleteBackupPlan <a href="#misc" title="covered by our integration test suite">✨</a></td>
       <td style="text-align:right">✅</td>
    </tr>
    <tr>
      <td>DeleteBackupSelection <a href="#misc" title="covered by our integration test suite">✨</a></td>
       <td style="text-align:right">✅</td>
    </tr>
    <tr>
      <td>DeleteBackupVault <a href="#misc" title="covered by our integration test suite">✨</a></td>
       <td style="text-align:right">✅</td>
    </tr>
    <tr>
      <td>DescribeBackupVault <a href="#misc" title="covered by our integration test suite">✨</a></td>
       <td style="text-align:right">✅</td>
    </tr>
    <tr>
      <td>DescribeRestoreJob <a href="#misc" title="covered by our integration test suite">✨</a></td>
       <td style="text-align:right">✅</td>
    </tr>
    <tr>
      <td>GetBackupPlan <a href="#misc" title="covered by our integration test suite">✨</a></td>
       <td style="text-align:right">✅</td>
    </tr>
    <tr>
      <td>GetBackupSelection <a href="#misc" title="covered by our integration test suite">✨</a></td>
       <td style="text-align:right">✅</td>
    </tr>
    <tr>
      <td>ListBackupJobs</td>
       <td style="text-align:right">✅</td>
    </tr>
    <tr>
      <td>ListBackupPlans <a href="#misc" title="covered by our integration test suite">✨</a></td>
       <td style="text-align:right">✅</td>
    </tr>
    <tr>
      <td>ListBackupSelections <a href="#misc" title="covered by our integration test suite">✨</a></td>
       <td style="text-align:right">✅</td>
    </tr>
    <tr>
      <td>ListBackupVaults <a href="#misc" title="covered by our integration test suite">✨</a></td>
       <td style="text-align:right">✅</td>
    </tr>
    <tr>
      <td>ListCopyJobs</td>
       <td style="text-align:right">✅</td>
    </tr>
    <tr>
      <td>ListRecoveryPointsByBackupVault <a href="#misc" title="covered by our integration test suite">✨</a></td>
       <td style="text-align:right">✅</td>
    </tr>
    <tr>
      <td>ListRecoveryPointsByResource <a href="#misc" title="covered by our integration test suite">✨</a></td>
       <td style="text-align:right">✅</td>
    </tr>
    <tr>
      <td>ListReportJobs</td>
       <td style="text-align:right">✅</td>
    </tr>
    <tr>
      <td>ListRestoreJobs</td>
       <td style="text-align:right">✅</td>
    </tr>
    <tr>
      <td>StartRestoreJob <a href="#misc" title="covered by our integration test suite">✨</a></td>
       <td style="text-align:right">✅</td>
    </tr>
    <tr>
      <td>UpdateBackupPlan <a href="#misc" title="covered by our integration test suite">✨</a></td>
       <td style="text-align:right">✅</td>
    </tr>
    <tr>
      <td><a data-toggle="collapse" href=".acm-notimplemented">Show more</a></td>
      <td style="text-align:right"></td>
    </tr>
    <tr class="collapse acm-notimplemented">
      <td>CreateFramework</td>
       <td style="text-align:right">-</td>
    </tr>
    <tr class="collapse acm-notimplemented">
      <td>CreateReportPlan</td>
       <td style="text-align:right">-</td>
    </tr>
    <tr class="collapse acm-notimplemented">
      <td>DeleteBackupVaultAccessPolicy</td>
       <td style="text-align:right">-</td>
    </tr>
    <tr class="collapse acm-notimplemented">
      <td>DeleteBackupVaultLockConfiguration</td>
       <td style="text-align:right">-</td>
    </tr>
    <tr class="collapse acm-notimplemented">
      <td>DeleteBackupVaultNotifications</td>
       <td style="text-align:right">-</td>
    </tr>
    <tr class="collapse acm-notimplemented">
      <td>DeleteFramework</td>
       <td style="text-align:right">-</td>
    </tr>
    <tr class="collapse acm-notimplemented">
      <td>DeleteRecoveryPoint</td>
       <td style="text-align:right">-</td>
    </tr>
    <tr class="collapse acm-notimplemented">
      <td>DeleteReportPlan</td>
       <td style="text-align:right">-</td>
    </tr>
    <tr class="collapse acm-notimplemented">
      <td>DescribeBackupJob</td>
       <td style="text-align:right">-</td>
    </tr>
    <tr class="collapse acm-notimplemented">
      <td>DescribeCopyJob</td>
       <td style="text-align:right">-</td>
    </tr>
    <tr class="collapse acm-notimplemented">
      <td>DescribeFramework</td>
       <td style="text-align:right">-</td>
    </tr>
    <tr class="collapse acm-notimplemented">
      <td>DescribeGlobalSettings</td>
       <td style="text-align:right">-</td>
    </tr>
    <tr class="collapse acm-notimplemented">
      <td>DescribeProtectedResource</td>
       <td style="text-align:right">-</td>
    </tr>
    <tr class="collapse acm-notimplemented">
      <td>DescribeRecoveryPoint</td>
       <td style="text-align:right">-</td>
    </tr>
    <tr class="collapse acm-notimplemented">
      <td>DescribeRegionSettings</td>
       <td style="text-align:right">-</td>
    </tr>
    <tr class="collapse acm-notimplemented">
      <td>DescribeReportJob</td>
       <td style="text-align:right">-</td>
    </tr>
    <tr class="collapse acm-notimplemented">
      <td>DescribeReportPlan</td>
       <td style="text-align:right">-</td>
    </tr>
    <tr class="collapse acm-notimplemented">
      <td>DisassociateRecoveryPoint</td>
       <td style="text-align:right">-</td>
    </tr>
    <tr class="collapse acm-notimplemented">
      <td>ExportBackupPlanTemplate</td>
       <td style="text-align:right">-</td>
    </tr>
    <tr class="collapse acm-notimplemented">
      <td>GetBackupPlanFromJSON</td>
       <td style="text-align:right">-</td>
    </tr>
    <tr class="collapse acm-notimplemented">
      <td>GetBackupPlanFromTemplate</td>
       <td style="text-align:right">-</td>
    </tr>
    <tr class="collapse acm-notimplemented">
      <td>GetBackupVaultAccessPolicy</td>
       <td style="text-align:right">-</td>
    </tr>
    <tr class="collapse acm-notimplemented">
      <td>GetBackupVaultNotifications</td>
       <td style="text-align:right">-</td>
    </tr>
    <tr class="collapse acm-notimplemented">
      <td>GetRecoveryPointRestoreMetadata</td>
       <td style="text-align:right">-</td>
    </tr>
    <tr class="collapse acm-notimplemented">
      <td>GetSupportedResourceTypes</td>
       <td style="text-align:right">-</td>
    </tr>
    <tr class="collapse acm-notimplemented">
      <td>ListBackupPlanTemplates</td>
       <td style="text-align:right">-</td>
    </tr>
    <tr class="collapse acm-notimplemented">
      <td>ListBackupPlanVersions</td>
       <td style="text-align:right">-</td>
    </tr>
    <tr class="collapse acm-notimplemented">
      <td>ListFrameworks</td>
       <td style="text-align:right">-</td>
    </tr>
    <tr class="collapse acm-notimplemented">
      <td>ListProtectedResources</td>
       <td style="text-align:right">-</td>
    </tr>
    <tr class="collapse acm-notimplemented">
      <td>ListReportPlans</td>
       <td style="text-align:right">-</td>
    </tr>
    <tr class="collapse acm-notimplemented">
      <td>ListTags</td>
       <td style="text-align:right">-</td>
    </tr>
    <tr class="collapse acm-notimplemented">
      <td>PutBackupVaultAccessPolicy</td>
       <td style="text-align:right">-</td>
    </tr>
    <tr class="collapse acm-notimplemented">
      <td>PutBackupVaultLockConfiguration</td>
       <td style="text-align:right">-</td>
    </tr>
    <tr class="collapse acm-notimplemented">
      <td>PutBackupVaultNotifications</td>
       <td style="text-align:right">-</td>
    </tr>
    <tr class="collapse acm-notimplemented">
      <td>StartBackupJob</td>
       <td style="text-align:right">-</td>
    </tr>
    <tr class="collapse acm-notimplemented">
      <td>StartCopyJob</td>
       <td style="text-align:right">-</td>
    </tr>
    <tr class="collapse acm-notimplemented">
      <td>StartReportJob</td>
       <td style="text-align:right">-</td>
    </tr>
    <tr class="collapse acm-notimplemented">
      <td>StopBackupJob</td>
       <td style="text-align:right">-</td>
    </tr>
    <tr class="collapse acm-notimplemented">
      <td>TagResource</td>
       <td style="text-align:right">-</td>
    </tr>
    <tr class="collapse acm-notimplemented">
      <td>UntagResource</td>
       <td style="text-align:right">-</td>
    </tr>
    <tr class="collapse acm-notimplemented">
      <td>UpdateFramework</td>
       <td style="text-align:right">-</td>
    </tr>
    <tr class="collapse acm-notimplemented">
      <td>UpdateGlobalSettings</td>
       <td style="text-align:right">-</td>
    </tr>
    <tr class="collapse acm-notimplemented">
      <td>UpdateRecoveryPointLifecycle</td>
       <td style="text-align:right">-</td>
    </tr>
    <tr class="collapse acm-notimplemented">
      <td>UpdateRegionSettings</td>
       <td style="text-align:right">-</td>
    </tr>
    <tr class="collapse acm-notimplemented">
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
      <td>CancelJob</td>
       <td style="text-align:right">✅</td>
    </tr>
    <tr>
      <td>CreateComputeEnvironment <a href="#misc" title="covered by our integration test suite">✨</a></td>
       <td style="text-align:right">✅</td>
    </tr>
    <tr>
      <td>CreateJobQueue <a href="#misc" title="covered by our integration test suite">✨</a></td>
       <td style="text-align:right">✅</td>
    </tr>
    <tr>
      <td>CreateSchedulingPolicy</td>
       <td style="text-align:right">✅</td>
    </tr>
    <tr>
      <td>DeleteComputeEnvironment</td>
       <td style="text-align:right">✅</td>
    </tr>
    <tr>
      <td>DeleteJobQueue <a href="#misc" title="covered by our integration test suite">✨</a></td>
       <td style="text-align:right">✅</td>
    </tr>
    <tr>
      <td>DeleteSchedulingPolicy</td>
       <td style="text-align:right">✅</td>
    </tr>
    <tr>
      <td>DeregisterJobDefinition <a href="#misc" title="covered by our integration test suite">✨</a></td>
       <td style="text-align:right">✅</td>
    </tr>
    <tr>
      <td>DescribeComputeEnvironments</td>
       <td style="text-align:right">✅</td>
    </tr>
    <tr>
      <td>DescribeJobDefinitions <a href="#misc" title="covered by our integration test suite">✨</a></td>
       <td style="text-align:right">✅</td>
    </tr>
    <tr>
      <td>DescribeJobQueues</td>
       <td style="text-align:right">✅</td>
    </tr>
    <tr>
      <td>DescribeJobs <a href="#misc" title="covered by our integration test suite">✨</a></td>
       <td style="text-align:right">✅</td>
    </tr>
    <tr>
      <td>DescribeSchedulingPolicies</td>
       <td style="text-align:right">✅</td>
    </tr>
    <tr>
      <td>ListJobs</td>
       <td style="text-align:right">✅</td>
    </tr>
    <tr>
      <td>ListSchedulingPolicies</td>
       <td style="text-align:right">✅</td>
    </tr>
    <tr>
      <td>ListTagsForResource</td>
       <td style="text-align:right">✅</td>
    </tr>
    <tr>
      <td>RegisterJobDefinition <a href="#misc" title="covered by our integration test suite">✨</a></td>
       <td style="text-align:right">✅</td>
    </tr>
    <tr>
      <td>SubmitJob <a href="#misc" title="covered by our integration test suite">✨</a></td>
       <td style="text-align:right">✅</td>
    </tr>
    <tr>
      <td>TagResource</td>
       <td style="text-align:right">✅</td>
    </tr>
    <tr>
      <td>TerminateJob</td>
       <td style="text-align:right">✅</td>
    </tr>
    <tr>
      <td>UntagResource</td>
       <td style="text-align:right">✅</td>
    </tr>
    <tr>
      <td>UpdateComputeEnvironment</td>
       <td style="text-align:right">✅</td>
    </tr>
    <tr>
      <td>UpdateJobQueue</td>
       <td style="text-align:right">✅</td>
    </tr>
    <tr>
      <td>UpdateSchedulingPolicy</td>
       <td style="text-align:right">✅</td>
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
      <td>CreateAnomalyMonitor <a href="#misc" title="covered by our integration test suite">✨</a></td>
       <td style="text-align:right">✅</td>
    </tr>
    <tr>
      <td>CreateAnomalySubscription <a href="#misc" title="covered by our integration test suite">✨</a></td>
       <td style="text-align:right">✅</td>
    </tr>
    <tr>
      <td>CreateCostCategoryDefinition <a href="#misc" title="covered by our integration test suite">✨</a></td>
       <td style="text-align:right">✅</td>
    </tr>
    <tr>
      <td>DeleteAnomalyMonitor <a href="#misc" title="covered by our integration test suite">✨</a></td>
       <td style="text-align:right">✅</td>
    </tr>
    <tr>
      <td>DeleteAnomalySubscription <a href="#misc" title="covered by our integration test suite">✨</a></td>
       <td style="text-align:right">✅</td>
    </tr>
    <tr>
      <td>DeleteCostCategoryDefinition <a href="#misc" title="covered by our integration test suite">✨</a></td>
       <td style="text-align:right">✅</td>
    </tr>
    <tr>
      <td>DescribeCostCategoryDefinition <a href="#misc" title="covered by our integration test suite">✨</a></td>
       <td style="text-align:right">✅</td>
    </tr>
    <tr>
      <td>GetAnomalyMonitors <a href="#misc" title="covered by our integration test suite">✨</a></td>
       <td style="text-align:right">✅</td>
    </tr>
    <tr>
      <td>GetAnomalySubscriptions <a href="#misc" title="covered by our integration test suite">✨</a></td>
       <td style="text-align:right">✅</td>
    </tr>
    <tr>
      <td>UpdateAnomalyMonitor <a href="#misc" title="covered by our integration test suite">✨</a></td>
       <td style="text-align:right">✅</td>
    </tr>
    <tr>
      <td>UpdateAnomalySubscription <a href="#misc" title="covered by our integration test suite">✨</a></td>
       <td style="text-align:right">✅</td>
    </tr>
    <tr>
      <td>UpdateCostCategoryDefinition <a href="#misc" title="covered by our integration test suite">✨</a></td>
       <td style="text-align:right">✅</td>
    </tr>
    <tr>
      <td><a data-toggle="collapse" href=".acm-notimplemented">Show more</a></td>
      <td style="text-align:right"></td>
    </tr>
    <tr class="collapse acm-notimplemented">
      <td>GetAnomalies</td>
       <td style="text-align:right">-</td>
    </tr>
    <tr class="collapse acm-notimplemented">
      <td>GetCostAndUsage</td>
       <td style="text-align:right">-</td>
    </tr>
    <tr class="collapse acm-notimplemented">
      <td>GetCostAndUsageWithResources</td>
       <td style="text-align:right">-</td>
    </tr>
    <tr class="collapse acm-notimplemented">
      <td>GetCostCategories</td>
       <td style="text-align:right">-</td>
    </tr>
    <tr class="collapse acm-notimplemented">
      <td>GetCostForecast</td>
       <td style="text-align:right">-</td>
    </tr>
    <tr class="collapse acm-notimplemented">
      <td>GetDimensionValues</td>
       <td style="text-align:right">-</td>
    </tr>
    <tr class="collapse acm-notimplemented">
      <td>GetReservationCoverage</td>
       <td style="text-align:right">-</td>
    </tr>
    <tr class="collapse acm-notimplemented">
      <td>GetReservationPurchaseRecommendation</td>
       <td style="text-align:right">-</td>
    </tr>
    <tr class="collapse acm-notimplemented">
      <td>GetReservationUtilization</td>
       <td style="text-align:right">-</td>
    </tr>
    <tr class="collapse acm-notimplemented">
      <td>GetRightsizingRecommendation</td>
       <td style="text-align:right">-</td>
    </tr>
    <tr class="collapse acm-notimplemented">
      <td>GetSavingsPlansCoverage</td>
       <td style="text-align:right">-</td>
    </tr>
    <tr class="collapse acm-notimplemented">
      <td>GetSavingsPlansPurchaseRecommendation</td>
       <td style="text-align:right">-</td>
    </tr>
    <tr class="collapse acm-notimplemented">
      <td>GetSavingsPlansUtilization</td>
       <td style="text-align:right">-</td>
    </tr>
    <tr class="collapse acm-notimplemented">
      <td>GetSavingsPlansUtilizationDetails</td>
       <td style="text-align:right">-</td>
    </tr>
    <tr class="collapse acm-notimplemented">
      <td>GetTags</td>
       <td style="text-align:right">-</td>
    </tr>
    <tr class="collapse acm-notimplemented">
      <td>GetUsageForecast</td>
       <td style="text-align:right">-</td>
    </tr>
    <tr class="collapse acm-notimplemented">
      <td>ListCostAllocationTags</td>
       <td style="text-align:right">-</td>
    </tr>
    <tr class="collapse acm-notimplemented">
      <td>ListCostCategoryDefinitions</td>
       <td style="text-align:right">-</td>
    </tr>
    <tr class="collapse acm-notimplemented">
      <td>ListTagsForResource</td>
       <td style="text-align:right">-</td>
    </tr>
    <tr class="collapse acm-notimplemented">
      <td>ProvideAnomalyFeedback</td>
       <td style="text-align:right">-</td>
    </tr>
    <tr class="collapse acm-notimplemented">
      <td>TagResource</td>
       <td style="text-align:right">-</td>
    </tr>
    <tr class="collapse acm-notimplemented">
      <td>UntagResource</td>
       <td style="text-align:right">-</td>
    </tr>
    <tr class="collapse acm-notimplemented">
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
    <tr>
      <td><a data-toggle="collapse" href=".acm-notimplemented">Show more</a></td>
      <td style="text-align:right"></td>
    </tr>
    <tr class="collapse acm-notimplemented">
      <td>ActivateType</td>
       <td style="text-align:right">-</td>
    </tr>
    <tr class="collapse acm-notimplemented">
      <td>BatchDescribeTypeConfigurations</td>
       <td style="text-align:right">-</td>
    </tr>
    <tr class="collapse acm-notimplemented">
      <td>CancelUpdateStack</td>
       <td style="text-align:right">-</td>
    </tr>
    <tr class="collapse acm-notimplemented">
      <td>ContinueUpdateRollback</td>
       <td style="text-align:right">-</td>
    </tr>
    <tr class="collapse acm-notimplemented">
      <td>DeactivateType</td>
       <td style="text-align:right">-</td>
    </tr>
    <tr class="collapse acm-notimplemented">
      <td>DeleteStackInstances</td>
       <td style="text-align:right">-</td>
    </tr>
    <tr class="collapse acm-notimplemented">
      <td>DeregisterType</td>
       <td style="text-align:right">-</td>
    </tr>
    <tr class="collapse acm-notimplemented">
      <td>DescribeAccountLimits</td>
       <td style="text-align:right">-</td>
    </tr>
    <tr class="collapse acm-notimplemented">
      <td>DescribeChangeSetHooks</td>
       <td style="text-align:right">-</td>
    </tr>
    <tr class="collapse acm-notimplemented">
      <td>DescribePublisher</td>
       <td style="text-align:right">-</td>
    </tr>
    <tr class="collapse acm-notimplemented">
      <td>DescribeStackDriftDetectionStatus</td>
       <td style="text-align:right">-</td>
    </tr>
    <tr class="collapse acm-notimplemented">
      <td>DescribeStackInstance</td>
       <td style="text-align:right">-</td>
    </tr>
    <tr class="collapse acm-notimplemented">
      <td>DescribeStackResourceDrifts</td>
       <td style="text-align:right">-</td>
    </tr>
    <tr class="collapse acm-notimplemented">
      <td>DescribeType</td>
       <td style="text-align:right">-</td>
    </tr>
    <tr class="collapse acm-notimplemented">
      <td>DescribeTypeRegistration</td>
       <td style="text-align:right">-</td>
    </tr>
    <tr class="collapse acm-notimplemented">
      <td>DetectStackDrift</td>
       <td style="text-align:right">-</td>
    </tr>
    <tr class="collapse acm-notimplemented">
      <td>DetectStackResourceDrift</td>
       <td style="text-align:right">-</td>
    </tr>
    <tr class="collapse acm-notimplemented">
      <td>DetectStackSetDrift</td>
       <td style="text-align:right">-</td>
    </tr>
    <tr class="collapse acm-notimplemented">
      <td>EstimateTemplateCost</td>
       <td style="text-align:right">-</td>
    </tr>
    <tr class="collapse acm-notimplemented">
      <td>GetStackPolicy</td>
       <td style="text-align:right">-</td>
    </tr>
    <tr class="collapse acm-notimplemented">
      <td>ImportStacksToStackSet</td>
       <td style="text-align:right">-</td>
    </tr>
    <tr class="collapse acm-notimplemented">
      <td>ListStackSetOperationResults</td>
       <td style="text-align:right">-</td>
    </tr>
    <tr class="collapse acm-notimplemented">
      <td>ListStackSetOperations</td>
       <td style="text-align:right">-</td>
    </tr>
    <tr class="collapse acm-notimplemented">
      <td>ListTypeRegistrations</td>
       <td style="text-align:right">-</td>
    </tr>
    <tr class="collapse acm-notimplemented">
      <td>ListTypeVersions</td>
       <td style="text-align:right">-</td>
    </tr>
    <tr class="collapse acm-notimplemented">
      <td>ListTypes</td>
       <td style="text-align:right">-</td>
    </tr>
    <tr class="collapse acm-notimplemented">
      <td>PublishType</td>
       <td style="text-align:right">-</td>
    </tr>
    <tr class="collapse acm-notimplemented">
      <td>RecordHandlerProgress</td>
       <td style="text-align:right">-</td>
    </tr>
    <tr class="collapse acm-notimplemented">
      <td>RegisterPublisher</td>
       <td style="text-align:right">-</td>
    </tr>
    <tr class="collapse acm-notimplemented">
      <td>RegisterType</td>
       <td style="text-align:right">-</td>
    </tr>
    <tr class="collapse acm-notimplemented">
      <td>RollbackStack</td>
       <td style="text-align:right">-</td>
    </tr>
    <tr class="collapse acm-notimplemented">
      <td>SetStackPolicy</td>
       <td style="text-align:right">-</td>
    </tr>
    <tr class="collapse acm-notimplemented">
      <td>SetTypeConfiguration</td>
       <td style="text-align:right">-</td>
    </tr>
    <tr class="collapse acm-notimplemented">
      <td>SetTypeDefaultVersion</td>
       <td style="text-align:right">-</td>
    </tr>
    <tr class="collapse acm-notimplemented">
      <td>SignalResource</td>
       <td style="text-align:right">-</td>
    </tr>
    <tr class="collapse acm-notimplemented">
      <td>StopStackSetOperation</td>
       <td style="text-align:right">-</td>
    </tr>
    <tr class="collapse acm-notimplemented">
      <td>TestType</td>
       <td style="text-align:right">-</td>
    </tr>
    <tr class="collapse acm-notimplemented">
      <td>UpdateStackInstances</td>
       <td style="text-align:right">-</td>
    </tr>
    <tr class="collapse acm-notimplemented">
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
      <td>CreateCloudFrontOriginAccessIdentity <a href="#misc" title="covered by our integration test suite">✨</a></td>
       <td style="text-align:right">✅</td>
    </tr>
    <tr>
      <td>CreateDistribution <a href="#misc" title="covered by our integration test suite">✨</a></td>
       <td style="text-align:right">✅</td>
    </tr>
    <tr>
      <td>CreateDistributionWithTags <a href="#misc" title="covered by our integration test suite">✨</a></td>
       <td style="text-align:right">✅</td>
    </tr>
    <tr>
      <td>CreateFunction <a href="#misc" title="covered by our integration test suite">✨</a></td>
       <td style="text-align:right">✅</td>
    </tr>
    <tr>
      <td>CreateInvalidation <a href="#misc" title="covered by our integration test suite">✨</a></td>
       <td style="text-align:right">✅</td>
    </tr>
    <tr>
      <td>CreateOriginRequestPolicy <a href="#misc" title="covered by our integration test suite">✨</a></td>
       <td style="text-align:right">✅</td>
    </tr>
    <tr>
      <td>DeleteCloudFrontOriginAccessIdentity <a href="#misc" title="covered by our integration test suite">✨</a></td>
       <td style="text-align:right">✅</td>
    </tr>
    <tr>
      <td>DeleteDistribution <a href="#misc" title="covered by our integration test suite">✨</a></td>
       <td style="text-align:right">✅</td>
    </tr>
    <tr>
      <td>DeleteFunction <a href="#misc" title="covered by our integration test suite">✨</a></td>
       <td style="text-align:right">✅</td>
    </tr>
    <tr>
      <td>DeleteOriginRequestPolicy <a href="#misc" title="covered by our integration test suite">✨</a></td>
       <td style="text-align:right">✅</td>
    </tr>
    <tr>
      <td>GetCloudFrontOriginAccessIdentity <a href="#misc" title="covered by our integration test suite">✨</a></td>
       <td style="text-align:right">✅</td>
    </tr>
    <tr>
      <td>GetDistribution</td>
       <td style="text-align:right">✅</td>
    </tr>
    <tr>
      <td>GetFunction <a href="#misc" title="covered by our integration test suite">✨</a></td>
       <td style="text-align:right">✅</td>
    </tr>
    <tr>
      <td>GetInvalidation <a href="#misc" title="covered by our integration test suite">✨</a></td>
       <td style="text-align:right">✅</td>
    </tr>
    <tr>
      <td>GetOriginRequestPolicy <a href="#misc" title="covered by our integration test suite">✨</a></td>
       <td style="text-align:right">✅</td>
    </tr>
    <tr>
      <td>ListCloudFrontOriginAccessIdentities <a href="#misc" title="covered by our integration test suite">✨</a></td>
       <td style="text-align:right">✅</td>
    </tr>
    <tr>
      <td>ListDistributions <a href="#misc" title="covered by our integration test suite">✨</a></td>
       <td style="text-align:right">✅</td>
    </tr>
    <tr>
      <td>ListFunctions <a href="#misc" title="covered by our integration test suite">✨</a></td>
       <td style="text-align:right">✅</td>
    </tr>
    <tr>
      <td>ListInvalidations <a href="#misc" title="covered by our integration test suite">✨</a></td>
       <td style="text-align:right">✅</td>
    </tr>
    <tr>
      <td>ListOriginRequestPolicies <a href="#misc" title="covered by our integration test suite">✨</a></td>
       <td style="text-align:right">✅</td>
    </tr>
    <tr>
      <td>ListTagsForResource <a href="#misc" title="covered by our integration test suite">✨</a></td>
       <td style="text-align:right">✅</td>
    </tr>
    <tr>
      <td>TagResource</td>
       <td style="text-align:right">✅</td>
    </tr>
    <tr>
      <td>UntagResource <a href="#misc" title="covered by our integration test suite">✨</a></td>
       <td style="text-align:right">✅</td>
    </tr>
    <tr>
      <td>UpdateDistribution</td>
       <td style="text-align:right">✅</td>
    </tr>
    <tr>
      <td>UpdateFunction <a href="#misc" title="covered by our integration test suite">✨</a></td>
       <td style="text-align:right">✅</td>
    </tr>
    <tr>
      <td>UpdateOriginRequestPolicy <a href="#misc" title="covered by our integration test suite">✨</a></td>
       <td style="text-align:right">✅</td>
    </tr>
    <tr>
      <td><a data-toggle="collapse" href=".acm-notimplemented">Show more</a></td>
      <td style="text-align:right"></td>
    </tr>
    <tr class="collapse acm-notimplemented">
      <td>AssociateAlias</td>
       <td style="text-align:right">-</td>
    </tr>
    <tr class="collapse acm-notimplemented">
      <td>CreateCachePolicy</td>
       <td style="text-align:right">-</td>
    </tr>
    <tr class="collapse acm-notimplemented">
      <td>CreateFieldLevelEncryptionConfig</td>
       <td style="text-align:right">-</td>
    </tr>
    <tr class="collapse acm-notimplemented">
      <td>CreateFieldLevelEncryptionProfile</td>
       <td style="text-align:right">-</td>
    </tr>
    <tr class="collapse acm-notimplemented">
      <td>CreateKeyGroup</td>
       <td style="text-align:right">-</td>
    </tr>
    <tr class="collapse acm-notimplemented">
      <td>CreateMonitoringSubscription</td>
       <td style="text-align:right">-</td>
    </tr>
    <tr class="collapse acm-notimplemented">
      <td>CreatePublicKey</td>
       <td style="text-align:right">-</td>
    </tr>
    <tr class="collapse acm-notimplemented">
      <td>CreateRealtimeLogConfig</td>
       <td style="text-align:right">-</td>
    </tr>
    <tr class="collapse acm-notimplemented">
      <td>CreateResponseHeadersPolicy</td>
       <td style="text-align:right">-</td>
    </tr>
    <tr class="collapse acm-notimplemented">
      <td>CreateStreamingDistribution</td>
       <td style="text-align:right">-</td>
    </tr>
    <tr class="collapse acm-notimplemented">
      <td>CreateStreamingDistributionWithTags</td>
       <td style="text-align:right">-</td>
    </tr>
    <tr class="collapse acm-notimplemented">
      <td>DeleteCachePolicy</td>
       <td style="text-align:right">-</td>
    </tr>
    <tr class="collapse acm-notimplemented">
      <td>DeleteFieldLevelEncryptionConfig</td>
       <td style="text-align:right">-</td>
    </tr>
    <tr class="collapse acm-notimplemented">
      <td>DeleteFieldLevelEncryptionProfile</td>
       <td style="text-align:right">-</td>
    </tr>
    <tr class="collapse acm-notimplemented">
      <td>DeleteKeyGroup</td>
       <td style="text-align:right">-</td>
    </tr>
    <tr class="collapse acm-notimplemented">
      <td>DeleteMonitoringSubscription</td>
       <td style="text-align:right">-</td>
    </tr>
    <tr class="collapse acm-notimplemented">
      <td>DeletePublicKey</td>
       <td style="text-align:right">-</td>
    </tr>
    <tr class="collapse acm-notimplemented">
      <td>DeleteRealtimeLogConfig</td>
       <td style="text-align:right">-</td>
    </tr>
    <tr class="collapse acm-notimplemented">
      <td>DeleteResponseHeadersPolicy</td>
       <td style="text-align:right">-</td>
    </tr>
    <tr class="collapse acm-notimplemented">
      <td>DeleteStreamingDistribution</td>
       <td style="text-align:right">-</td>
    </tr>
    <tr class="collapse acm-notimplemented">
      <td>DescribeFunction</td>
       <td style="text-align:right">-</td>
    </tr>
    <tr class="collapse acm-notimplemented">
      <td>GetCachePolicy</td>
       <td style="text-align:right">-</td>
    </tr>
    <tr class="collapse acm-notimplemented">
      <td>GetCachePolicyConfig</td>
       <td style="text-align:right">-</td>
    </tr>
    <tr class="collapse acm-notimplemented">
      <td>GetCloudFrontOriginAccessIdentityConfig</td>
       <td style="text-align:right">-</td>
    </tr>
    <tr class="collapse acm-notimplemented">
      <td>GetDistributionConfig</td>
       <td style="text-align:right">-</td>
    </tr>
    <tr class="collapse acm-notimplemented">
      <td>GetFieldLevelEncryption</td>
       <td style="text-align:right">-</td>
    </tr>
    <tr class="collapse acm-notimplemented">
      <td>GetFieldLevelEncryptionConfig</td>
       <td style="text-align:right">-</td>
    </tr>
    <tr class="collapse acm-notimplemented">
      <td>GetFieldLevelEncryptionProfile</td>
       <td style="text-align:right">-</td>
    </tr>
    <tr class="collapse acm-notimplemented">
      <td>GetFieldLevelEncryptionProfileConfig</td>
       <td style="text-align:right">-</td>
    </tr>
    <tr class="collapse acm-notimplemented">
      <td>GetKeyGroup</td>
       <td style="text-align:right">-</td>
    </tr>
    <tr class="collapse acm-notimplemented">
      <td>GetKeyGroupConfig</td>
       <td style="text-align:right">-</td>
    </tr>
    <tr class="collapse acm-notimplemented">
      <td>GetMonitoringSubscription</td>
       <td style="text-align:right">-</td>
    </tr>
    <tr class="collapse acm-notimplemented">
      <td>GetOriginRequestPolicyConfig</td>
       <td style="text-align:right">-</td>
    </tr>
    <tr class="collapse acm-notimplemented">
      <td>GetPublicKey</td>
       <td style="text-align:right">-</td>
    </tr>
    <tr class="collapse acm-notimplemented">
      <td>GetPublicKeyConfig</td>
       <td style="text-align:right">-</td>
    </tr>
    <tr class="collapse acm-notimplemented">
      <td>GetRealtimeLogConfig</td>
       <td style="text-align:right">-</td>
    </tr>
    <tr class="collapse acm-notimplemented">
      <td>GetResponseHeadersPolicy</td>
       <td style="text-align:right">-</td>
    </tr>
    <tr class="collapse acm-notimplemented">
      <td>GetResponseHeadersPolicyConfig</td>
       <td style="text-align:right">-</td>
    </tr>
    <tr class="collapse acm-notimplemented">
      <td>GetStreamingDistribution</td>
       <td style="text-align:right">-</td>
    </tr>
    <tr class="collapse acm-notimplemented">
      <td>GetStreamingDistributionConfig</td>
       <td style="text-align:right">-</td>
    </tr>
    <tr class="collapse acm-notimplemented">
      <td>ListCachePolicies</td>
       <td style="text-align:right">-</td>
    </tr>
    <tr class="collapse acm-notimplemented">
      <td>ListConflictingAliases</td>
       <td style="text-align:right">-</td>
    </tr>
    <tr class="collapse acm-notimplemented">
      <td>ListDistributionsByCachePolicyId</td>
       <td style="text-align:right">-</td>
    </tr>
    <tr class="collapse acm-notimplemented">
      <td>ListDistributionsByKeyGroup</td>
       <td style="text-align:right">-</td>
    </tr>
    <tr class="collapse acm-notimplemented">
      <td>ListDistributionsByOriginRequestPolicyId</td>
       <td style="text-align:right">-</td>
    </tr>
    <tr class="collapse acm-notimplemented">
      <td>ListDistributionsByRealtimeLogConfig</td>
       <td style="text-align:right">-</td>
    </tr>
    <tr class="collapse acm-notimplemented">
      <td>ListDistributionsByResponseHeadersPolicyId</td>
       <td style="text-align:right">-</td>
    </tr>
    <tr class="collapse acm-notimplemented">
      <td>ListDistributionsByWebACLId</td>
       <td style="text-align:right">-</td>
    </tr>
    <tr class="collapse acm-notimplemented">
      <td>ListFieldLevelEncryptionConfigs</td>
       <td style="text-align:right">-</td>
    </tr>
    <tr class="collapse acm-notimplemented">
      <td>ListFieldLevelEncryptionProfiles</td>
       <td style="text-align:right">-</td>
    </tr>
    <tr class="collapse acm-notimplemented">
      <td>ListKeyGroups</td>
       <td style="text-align:right">-</td>
    </tr>
    <tr class="collapse acm-notimplemented">
      <td>ListPublicKeys</td>
       <td style="text-align:right">-</td>
    </tr>
    <tr class="collapse acm-notimplemented">
      <td>ListRealtimeLogConfigs</td>
       <td style="text-align:right">-</td>
    </tr>
    <tr class="collapse acm-notimplemented">
      <td>ListResponseHeadersPolicies</td>
       <td style="text-align:right">-</td>
    </tr>
    <tr class="collapse acm-notimplemented">
      <td>ListStreamingDistributions</td>
       <td style="text-align:right">-</td>
    </tr>
    <tr class="collapse acm-notimplemented">
      <td>PublishFunction</td>
       <td style="text-align:right">-</td>
    </tr>
    <tr class="collapse acm-notimplemented">
      <td>TestFunction</td>
       <td style="text-align:right">-</td>
    </tr>
    <tr class="collapse acm-notimplemented">
      <td>UpdateCachePolicy</td>
       <td style="text-align:right">-</td>
    </tr>
    <tr class="collapse acm-notimplemented">
      <td>UpdateCloudFrontOriginAccessIdentity</td>
       <td style="text-align:right">-</td>
    </tr>
    <tr class="collapse acm-notimplemented">
      <td>UpdateFieldLevelEncryptionConfig</td>
       <td style="text-align:right">-</td>
    </tr>
    <tr class="collapse acm-notimplemented">
      <td>UpdateFieldLevelEncryptionProfile</td>
       <td style="text-align:right">-</td>
    </tr>
    <tr class="collapse acm-notimplemented">
      <td>UpdateKeyGroup</td>
       <td style="text-align:right">-</td>
    </tr>
    <tr class="collapse acm-notimplemented">
      <td>UpdatePublicKey</td>
       <td style="text-align:right">-</td>
    </tr>
    <tr class="collapse acm-notimplemented">
      <td>UpdateRealtimeLogConfig</td>
       <td style="text-align:right">-</td>
    </tr>
    <tr class="collapse acm-notimplemented">
      <td>UpdateResponseHeadersPolicy</td>
       <td style="text-align:right">-</td>
    </tr>
    <tr class="collapse acm-notimplemented">
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
      <td>AddTags</td>
       <td style="text-align:right">✅</td>
    </tr>
    <tr>
      <td>CreateTrail <a href="#misc" title="covered by our integration test suite">✨</a></td>
       <td style="text-align:right">✅</td>
    </tr>
    <tr>
      <td>DeleteTrail <a href="#misc" title="covered by our integration test suite">✨</a></td>
       <td style="text-align:right">✅</td>
    </tr>
    <tr>
      <td>DescribeTrails <a href="#misc" title="covered by our integration test suite">✨</a></td>
       <td style="text-align:right">✅</td>
    </tr>
    <tr>
      <td>GetEventSelectors</td>
       <td style="text-align:right">✅</td>
    </tr>
    <tr>
      <td>GetInsightSelectors</td>
       <td style="text-align:right">✅</td>
    </tr>
    <tr>
      <td>GetTrail <a href="#misc" title="covered by our integration test suite">✨</a></td>
       <td style="text-align:right">✅</td>
    </tr>
    <tr>
      <td>GetTrailStatus <a href="#misc" title="covered by our integration test suite">✨</a></td>
       <td style="text-align:right">✅</td>
    </tr>
    <tr>
      <td>ListTags <a href="#misc" title="covered by our integration test suite">✨</a></td>
       <td style="text-align:right">✅</td>
    </tr>
    <tr>
      <td>ListTrails <a href="#misc" title="covered by our integration test suite">✨</a></td>
       <td style="text-align:right">✅</td>
    </tr>
    <tr>
      <td>LookupEvents <a href="#misc" title="covered by our integration test suite">✨</a></td>
       <td style="text-align:right">✅</td>
    </tr>
    <tr>
      <td>PutEventSelectors <a href="#misc" title="covered by our integration test suite">✨</a></td>
       <td style="text-align:right">✅</td>
    </tr>
    <tr>
      <td>PutInsightSelectors</td>
       <td style="text-align:right">✅</td>
    </tr>
    <tr>
      <td>RemoveTags</td>
       <td style="text-align:right">✅</td>
    </tr>
    <tr>
      <td>StartLogging <a href="#misc" title="covered by our integration test suite">✨</a></td>
       <td style="text-align:right">✅</td>
    </tr>
    <tr>
      <td>StopLogging <a href="#misc" title="covered by our integration test suite">✨</a></td>
       <td style="text-align:right">✅</td>
    </tr>
    <tr>
      <td>UpdateTrail <a href="#misc" title="covered by our integration test suite">✨</a></td>
       <td style="text-align:right">✅</td>
    </tr>
    <tr>
      <td><a data-toggle="collapse" href=".acm-notimplemented">Show more</a></td>
      <td style="text-align:right"></td>
    </tr>
    <tr class="collapse acm-notimplemented">
      <td>CancelQuery</td>
       <td style="text-align:right">-</td>
    </tr>
    <tr class="collapse acm-notimplemented">
      <td>CreateEventDataStore</td>
       <td style="text-align:right">-</td>
    </tr>
    <tr class="collapse acm-notimplemented">
      <td>DeleteEventDataStore</td>
       <td style="text-align:right">-</td>
    </tr>
    <tr class="collapse acm-notimplemented">
      <td>DescribeQuery</td>
       <td style="text-align:right">-</td>
    </tr>
    <tr class="collapse acm-notimplemented">
      <td>GetEventDataStore</td>
       <td style="text-align:right">-</td>
    </tr>
    <tr class="collapse acm-notimplemented">
      <td>GetQueryResults</td>
       <td style="text-align:right">-</td>
    </tr>
    <tr class="collapse acm-notimplemented">
      <td>ListEventDataStores</td>
       <td style="text-align:right">-</td>
    </tr>
    <tr class="collapse acm-notimplemented">
      <td>ListPublicKeys</td>
       <td style="text-align:right">-</td>
    </tr>
    <tr class="collapse acm-notimplemented">
      <td>ListQueries</td>
       <td style="text-align:right">-</td>
    </tr>
    <tr class="collapse acm-notimplemented">
      <td>RestoreEventDataStore</td>
       <td style="text-align:right">-</td>
    </tr>
    <tr class="collapse acm-notimplemented">
      <td>StartQuery</td>
       <td style="text-align:right">-</td>
    </tr>
    <tr class="collapse acm-notimplemented">
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
    <tr>
      <td><a data-toggle="collapse" href=".acm-notimplemented">Show more</a></td>
      <td style="text-align:right"></td>
    </tr>
    <tr class="collapse acm-notimplemented">
      <td>DeleteAnomalyDetector</td>
       <td style="text-align:right">-</td>
    </tr>
    <tr class="collapse acm-notimplemented">
      <td>DeleteInsightRules</td>
       <td style="text-align:right">-</td>
    </tr>
    <tr class="collapse acm-notimplemented">
      <td>DeleteMetricStream</td>
       <td style="text-align:right">-</td>
    </tr>
    <tr class="collapse acm-notimplemented">
      <td>DescribeAlarmHistory</td>
       <td style="text-align:right">-</td>
    </tr>
    <tr class="collapse acm-notimplemented">
      <td>DescribeAnomalyDetectors</td>
       <td style="text-align:right">-</td>
    </tr>
    <tr class="collapse acm-notimplemented">
      <td>DescribeInsightRules</td>
       <td style="text-align:right">-</td>
    </tr>
    <tr class="collapse acm-notimplemented">
      <td>DisableAlarmActions</td>
       <td style="text-align:right">-</td>
    </tr>
    <tr class="collapse acm-notimplemented">
      <td>DisableInsightRules</td>
       <td style="text-align:right">-</td>
    </tr>
    <tr class="collapse acm-notimplemented">
      <td>EnableAlarmActions</td>
       <td style="text-align:right">-</td>
    </tr>
    <tr class="collapse acm-notimplemented">
      <td>EnableInsightRules</td>
       <td style="text-align:right">-</td>
    </tr>
    <tr class="collapse acm-notimplemented">
      <td>GetInsightRuleReport</td>
       <td style="text-align:right">-</td>
    </tr>
    <tr class="collapse acm-notimplemented">
      <td>GetMetricStream</td>
       <td style="text-align:right">-</td>
    </tr>
    <tr class="collapse acm-notimplemented">
      <td>GetMetricWidgetImage</td>
       <td style="text-align:right">-</td>
    </tr>
    <tr class="collapse acm-notimplemented">
      <td>ListMetricStreams</td>
       <td style="text-align:right">-</td>
    </tr>
    <tr class="collapse acm-notimplemented">
      <td>PutAnomalyDetector</td>
       <td style="text-align:right">-</td>
    </tr>
    <tr class="collapse acm-notimplemented">
      <td>PutInsightRule</td>
       <td style="text-align:right">-</td>
    </tr>
    <tr class="collapse acm-notimplemented">
      <td>PutMetricStream</td>
       <td style="text-align:right">-</td>
    </tr>
    <tr class="collapse acm-notimplemented">
      <td>StartMetricStreams</td>
       <td style="text-align:right">-</td>
    </tr>
    <tr class="collapse acm-notimplemented">
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
      <td>CreateBranch <a href="#misc" title="covered by our integration test suite">✨</a></td>
       <td style="text-align:right">✅</td>
    </tr>
    <tr>
      <td>CreateCommit <a href="#misc" title="covered by our integration test suite">✨</a></td>
       <td style="text-align:right">✅</td>
    </tr>
    <tr>
      <td>CreatePullRequest <a href="#misc" title="covered by our integration test suite">✨</a></td>
       <td style="text-align:right">✅</td>
    </tr>
    <tr>
      <td>CreateRepository <a href="#misc" title="covered by our integration test suite">✨</a></td>
       <td style="text-align:right">✅</td>
    </tr>
    <tr>
      <td>DeleteBranch <a href="#misc" title="covered by our integration test suite">✨</a></td>
       <td style="text-align:right">✅</td>
    </tr>
    <tr>
      <td>DeleteRepository <a href="#misc" title="covered by our integration test suite">✨</a></td>
       <td style="text-align:right">✅</td>
    </tr>
    <tr>
      <td>GetBranch <a href="#misc" title="covered by our integration test suite">✨</a></td>
       <td style="text-align:right">✅</td>
    </tr>
    <tr>
      <td>GetFile <a href="#misc" title="covered by our integration test suite">✨</a></td>
       <td style="text-align:right">✅</td>
    </tr>
    <tr>
      <td>GetFolder <a href="#misc" title="covered by our integration test suite">✨</a></td>
       <td style="text-align:right">✅</td>
    </tr>
    <tr>
      <td>GetRepository <a href="#misc" title="covered by our integration test suite">✨</a></td>
       <td style="text-align:right">✅</td>
    </tr>
    <tr>
      <td>ListPullRequests <a href="#misc" title="covered by our integration test suite">✨</a></td>
       <td style="text-align:right">✅</td>
    </tr>
    <tr>
      <td>ListRepositories</td>
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
      <td><a data-toggle="collapse" href=".acm-notimplemented">Show more</a></td>
      <td style="text-align:right"></td>
    </tr>
    <tr class="collapse acm-notimplemented">
      <td>AssociateApprovalRuleTemplateWithRepository</td>
       <td style="text-align:right">-</td>
    </tr>
    <tr class="collapse acm-notimplemented">
      <td>BatchAssociateApprovalRuleTemplateWithRepositories</td>
       <td style="text-align:right">-</td>
    </tr>
    <tr class="collapse acm-notimplemented">
      <td>BatchDescribeMergeConflicts</td>
       <td style="text-align:right">-</td>
    </tr>
    <tr class="collapse acm-notimplemented">
      <td>BatchDisassociateApprovalRuleTemplateFromRepositories</td>
       <td style="text-align:right">-</td>
    </tr>
    <tr class="collapse acm-notimplemented">
      <td>BatchGetCommits</td>
       <td style="text-align:right">-</td>
    </tr>
    <tr class="collapse acm-notimplemented">
      <td>BatchGetRepositories</td>
       <td style="text-align:right">-</td>
    </tr>
    <tr class="collapse acm-notimplemented">
      <td>CreateApprovalRuleTemplate</td>
       <td style="text-align:right">-</td>
    </tr>
    <tr class="collapse acm-notimplemented">
      <td>CreatePullRequestApprovalRule</td>
       <td style="text-align:right">-</td>
    </tr>
    <tr class="collapse acm-notimplemented">
      <td>CreateUnreferencedMergeCommit</td>
       <td style="text-align:right">-</td>
    </tr>
    <tr class="collapse acm-notimplemented">
      <td>DeleteApprovalRuleTemplate</td>
       <td style="text-align:right">-</td>
    </tr>
    <tr class="collapse acm-notimplemented">
      <td>DeleteCommentContent</td>
       <td style="text-align:right">-</td>
    </tr>
    <tr class="collapse acm-notimplemented">
      <td>DeleteFile</td>
       <td style="text-align:right">-</td>
    </tr>
    <tr class="collapse acm-notimplemented">
      <td>DeletePullRequestApprovalRule</td>
       <td style="text-align:right">-</td>
    </tr>
    <tr class="collapse acm-notimplemented">
      <td>DescribeMergeConflicts</td>
       <td style="text-align:right">-</td>
    </tr>
    <tr class="collapse acm-notimplemented">
      <td>DescribePullRequestEvents</td>
       <td style="text-align:right">-</td>
    </tr>
    <tr class="collapse acm-notimplemented">
      <td>DisassociateApprovalRuleTemplateFromRepository</td>
       <td style="text-align:right">-</td>
    </tr>
    <tr class="collapse acm-notimplemented">
      <td>EvaluatePullRequestApprovalRules</td>
       <td style="text-align:right">-</td>
    </tr>
    <tr class="collapse acm-notimplemented">
      <td>GetApprovalRuleTemplate</td>
       <td style="text-align:right">-</td>
    </tr>
    <tr class="collapse acm-notimplemented">
      <td>GetBlob</td>
       <td style="text-align:right">-</td>
    </tr>
    <tr class="collapse acm-notimplemented">
      <td>GetComment</td>
       <td style="text-align:right">-</td>
    </tr>
    <tr class="collapse acm-notimplemented">
      <td>GetCommentReactions</td>
       <td style="text-align:right">-</td>
    </tr>
    <tr class="collapse acm-notimplemented">
      <td>GetCommentsForComparedCommit</td>
       <td style="text-align:right">-</td>
    </tr>
    <tr class="collapse acm-notimplemented">
      <td>GetCommentsForPullRequest</td>
       <td style="text-align:right">-</td>
    </tr>
    <tr class="collapse acm-notimplemented">
      <td>GetCommit</td>
       <td style="text-align:right">-</td>
    </tr>
    <tr class="collapse acm-notimplemented">
      <td>GetDifferences</td>
       <td style="text-align:right">-</td>
    </tr>
    <tr class="collapse acm-notimplemented">
      <td>GetMergeCommit</td>
       <td style="text-align:right">-</td>
    </tr>
    <tr class="collapse acm-notimplemented">
      <td>GetMergeConflicts</td>
       <td style="text-align:right">-</td>
    </tr>
    <tr class="collapse acm-notimplemented">
      <td>GetMergeOptions</td>
       <td style="text-align:right">-</td>
    </tr>
    <tr class="collapse acm-notimplemented">
      <td>GetPullRequest</td>
       <td style="text-align:right">-</td>
    </tr>
    <tr class="collapse acm-notimplemented">
      <td>GetPullRequestApprovalStates</td>
       <td style="text-align:right">-</td>
    </tr>
    <tr class="collapse acm-notimplemented">
      <td>GetPullRequestOverrideState</td>
       <td style="text-align:right">-</td>
    </tr>
    <tr class="collapse acm-notimplemented">
      <td>GetRepositoryTriggers</td>
       <td style="text-align:right">-</td>
    </tr>
    <tr class="collapse acm-notimplemented">
      <td>ListApprovalRuleTemplates</td>
       <td style="text-align:right">-</td>
    </tr>
    <tr class="collapse acm-notimplemented">
      <td>ListAssociatedApprovalRuleTemplatesForRepository</td>
       <td style="text-align:right">-</td>
    </tr>
    <tr class="collapse acm-notimplemented">
      <td>ListBranches</td>
       <td style="text-align:right">-</td>
    </tr>
    <tr class="collapse acm-notimplemented">
      <td>ListRepositoriesForApprovalRuleTemplate</td>
       <td style="text-align:right">-</td>
    </tr>
    <tr class="collapse acm-notimplemented">
      <td>MergeBranchesByFastForward</td>
       <td style="text-align:right">-</td>
    </tr>
    <tr class="collapse acm-notimplemented">
      <td>MergeBranchesBySquash</td>
       <td style="text-align:right">-</td>
    </tr>
    <tr class="collapse acm-notimplemented">
      <td>MergeBranchesByThreeWay</td>
       <td style="text-align:right">-</td>
    </tr>
    <tr class="collapse acm-notimplemented">
      <td>MergePullRequestByFastForward</td>
       <td style="text-align:right">-</td>
    </tr>
    <tr class="collapse acm-notimplemented">
      <td>MergePullRequestBySquash</td>
       <td style="text-align:right">-</td>
    </tr>
    <tr class="collapse acm-notimplemented">
      <td>MergePullRequestByThreeWay</td>
       <td style="text-align:right">-</td>
    </tr>
    <tr class="collapse acm-notimplemented">
      <td>OverridePullRequestApprovalRules</td>
       <td style="text-align:right">-</td>
    </tr>
    <tr class="collapse acm-notimplemented">
      <td>PostCommentForComparedCommit</td>
       <td style="text-align:right">-</td>
    </tr>
    <tr class="collapse acm-notimplemented">
      <td>PostCommentForPullRequest</td>
       <td style="text-align:right">-</td>
    </tr>
    <tr class="collapse acm-notimplemented">
      <td>PostCommentReply</td>
       <td style="text-align:right">-</td>
    </tr>
    <tr class="collapse acm-notimplemented">
      <td>PutCommentReaction</td>
       <td style="text-align:right">-</td>
    </tr>
    <tr class="collapse acm-notimplemented">
      <td>PutFile</td>
       <td style="text-align:right">-</td>
    </tr>
    <tr class="collapse acm-notimplemented">
      <td>PutRepositoryTriggers</td>
       <td style="text-align:right">-</td>
    </tr>
    <tr class="collapse acm-notimplemented">
      <td>TestRepositoryTriggers</td>
       <td style="text-align:right">-</td>
    </tr>
    <tr class="collapse acm-notimplemented">
      <td>UntagResource</td>
       <td style="text-align:right">-</td>
    </tr>
    <tr class="collapse acm-notimplemented">
      <td>UpdateApprovalRuleTemplateContent</td>
       <td style="text-align:right">-</td>
    </tr>
    <tr class="collapse acm-notimplemented">
      <td>UpdateApprovalRuleTemplateDescription</td>
       <td style="text-align:right">-</td>
    </tr>
    <tr class="collapse acm-notimplemented">
      <td>UpdateApprovalRuleTemplateName</td>
       <td style="text-align:right">-</td>
    </tr>
    <tr class="collapse acm-notimplemented">
      <td>UpdateComment</td>
       <td style="text-align:right">-</td>
    </tr>
    <tr class="collapse acm-notimplemented">
      <td>UpdateDefaultBranch</td>
       <td style="text-align:right">-</td>
    </tr>
    <tr class="collapse acm-notimplemented">
      <td>UpdatePullRequestApprovalRuleContent</td>
       <td style="text-align:right">-</td>
    </tr>
    <tr class="collapse acm-notimplemented">
      <td>UpdatePullRequestApprovalState</td>
       <td style="text-align:right">-</td>
    </tr>
    <tr class="collapse acm-notimplemented">
      <td>UpdatePullRequestDescription</td>
       <td style="text-align:right">-</td>
    </tr>
    <tr class="collapse acm-notimplemented">
      <td>UpdatePullRequestStatus</td>
       <td style="text-align:right">-</td>
    </tr>
    <tr class="collapse acm-notimplemented">
      <td>UpdatePullRequestTitle</td>
       <td style="text-align:right">-</td>
    </tr>
    <tr class="collapse acm-notimplemented">
      <td>UpdateRepositoryDescription</td>
       <td style="text-align:right">-</td>
    </tr>
    <tr class="collapse acm-notimplemented">
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
      <td>CreateIdentityPool <a href="#misc" title="covered by our integration test suite">✨</a></td>
       <td style="text-align:right">✅</td>
    </tr>
    <tr>
      <td>DeleteIdentityPool <a href="#misc" title="covered by our integration test suite">✨</a></td>
       <td style="text-align:right">✅</td>
    </tr>
    <tr>
      <td>DescribeIdentityPool</td>
       <td style="text-align:right">✅</td>
    </tr>
    <tr>
      <td>GetCredentialsForIdentity <a href="#misc" title="covered by our integration test suite">✨</a></td>
       <td style="text-align:right">✅</td>
    </tr>
    <tr>
      <td>GetId <a href="#misc" title="covered by our integration test suite">✨</a></td>
       <td style="text-align:right">✅</td>
    </tr>
    <tr>
      <td>GetIdentityPoolRoles <a href="#misc" title="covered by our integration test suite">✨</a></td>
       <td style="text-align:right">✅</td>
    </tr>
    <tr>
      <td>GetOpenIdToken</td>
       <td style="text-align:right">✅</td>
    </tr>
    <tr>
      <td>GetOpenIdTokenForDeveloperIdentity</td>
       <td style="text-align:right">✅</td>
    </tr>
    <tr>
      <td>ListIdentities</td>
       <td style="text-align:right">✅</td>
    </tr>
    <tr>
      <td>ListIdentityPools <a href="#misc" title="covered by our integration test suite">✨</a></td>
       <td style="text-align:right">✅</td>
    </tr>
    <tr>
      <td>SetIdentityPoolRoles <a href="#misc" title="covered by our integration test suite">✨</a></td>
       <td style="text-align:right">✅</td>
    </tr>
    <tr>
      <td>UpdateIdentityPool</td>
       <td style="text-align:right">✅</td>
    </tr>
    <tr>
      <td><a data-toggle="collapse" href=".acm-notimplemented">Show more</a></td>
      <td style="text-align:right"></td>
    </tr>
    <tr class="collapse acm-notimplemented">
      <td>DeleteIdentities</td>
       <td style="text-align:right">-</td>
    </tr>
    <tr class="collapse acm-notimplemented">
      <td>DescribeIdentity</td>
       <td style="text-align:right">-</td>
    </tr>
    <tr class="collapse acm-notimplemented">
      <td>GetPrincipalTagAttributeMap</td>
       <td style="text-align:right">-</td>
    </tr>
    <tr class="collapse acm-notimplemented">
      <td>ListTagsForResource</td>
       <td style="text-align:right">-</td>
    </tr>
    <tr class="collapse acm-notimplemented">
      <td>LookupDeveloperIdentity</td>
       <td style="text-align:right">-</td>
    </tr>
    <tr class="collapse acm-notimplemented">
      <td>MergeDeveloperIdentities</td>
       <td style="text-align:right">-</td>
    </tr>
    <tr class="collapse acm-notimplemented">
      <td>SetPrincipalTagAttributeMap</td>
       <td style="text-align:right">-</td>
    </tr>
    <tr class="collapse acm-notimplemented">
      <td>TagResource</td>
       <td style="text-align:right">-</td>
    </tr>
    <tr class="collapse acm-notimplemented">
      <td>UnlinkDeveloperIdentity</td>
       <td style="text-align:right">-</td>
    </tr>
    <tr class="collapse acm-notimplemented">
      <td>UnlinkIdentity</td>
       <td style="text-align:right">-</td>
    </tr>
    <tr class="collapse acm-notimplemented">
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
      <td>AddCustomAttributes</td>
       <td style="text-align:right">✅</td>
    </tr>
    <tr>
      <td>AdminAddUserToGroup <a href="#misc" title="covered by our integration test suite">✨</a></td>
       <td style="text-align:right">✅</td>
    </tr>
    <tr>
      <td>AdminConfirmSignUp <a href="#misc" title="covered by our integration test suite">✨</a></td>
       <td style="text-align:right">✅</td>
    </tr>
    <tr>
      <td>AdminCreateUser <a href="#misc" title="covered by our integration test suite">✨</a></td>
       <td style="text-align:right">✅</td>
    </tr>
    <tr>
      <td>AdminDeleteUser <a href="#misc" title="covered by our integration test suite">✨</a></td>
       <td style="text-align:right">✅</td>
    </tr>
    <tr>
      <td>AdminDeleteUserAttributes <a href="#misc" title="covered by our integration test suite">✨</a></td>
       <td style="text-align:right">✅</td>
    </tr>
    <tr>
      <td>AdminDisableUser <a href="#misc" title="covered by our integration test suite">✨</a></td>
       <td style="text-align:right">✅</td>
    </tr>
    <tr>
      <td>AdminEnableUser</td>
       <td style="text-align:right">✅</td>
    </tr>
    <tr>
      <td>AdminGetUser <a href="#misc" title="covered by our integration test suite">✨</a></td>
       <td style="text-align:right">✅</td>
    </tr>
    <tr>
      <td>AdminInitiateAuth <a href="#misc" title="covered by our integration test suite">✨</a></td>
       <td style="text-align:right">✅</td>
    </tr>
    <tr>
      <td>AdminListGroupsForUser <a href="#misc" title="covered by our integration test suite">✨</a></td>
       <td style="text-align:right">✅</td>
    </tr>
    <tr>
      <td>AdminRemoveUserFromGroup</td>
       <td style="text-align:right">✅</td>
    </tr>
    <tr>
      <td>AdminResetUserPassword</td>
       <td style="text-align:right">✅</td>
    </tr>
    <tr>
      <td>AdminRespondToAuthChallenge <a href="#misc" title="covered by our integration test suite">✨</a></td>
       <td style="text-align:right">✅</td>
    </tr>
    <tr>
      <td>AdminSetUserMFAPreference <a href="#misc" title="covered by our integration test suite">✨</a></td>
       <td style="text-align:right">✅</td>
    </tr>
    <tr>
      <td>AdminSetUserPassword <a href="#misc" title="covered by our integration test suite">✨</a></td>
       <td style="text-align:right">✅</td>
    </tr>
    <tr>
      <td>AdminUpdateUserAttributes <a href="#misc" title="covered by our integration test suite">✨</a></td>
       <td style="text-align:right">✅</td>
    </tr>
    <tr>
      <td>AdminUserGlobalSignOut <a href="#misc" title="covered by our integration test suite">✨</a></td>
       <td style="text-align:right">✅</td>
    </tr>
    <tr>
      <td>ChangePassword <a href="#misc" title="covered by our integration test suite">✨</a></td>
       <td style="text-align:right">✅</td>
    </tr>
    <tr>
      <td>ConfirmDevice</td>
       <td style="text-align:right">✅</td>
    </tr>
    <tr>
      <td>ConfirmForgotPassword <a href="#misc" title="covered by our integration test suite">✨</a></td>
       <td style="text-align:right">✅</td>
    </tr>
    <tr>
      <td>ConfirmSignUp</td>
       <td style="text-align:right">✅</td>
    </tr>
    <tr>
      <td>CreateGroup <a href="#misc" title="covered by our integration test suite">✨</a></td>
       <td style="text-align:right">✅</td>
    </tr>
    <tr>
      <td>CreateIdentityProvider <a href="#misc" title="covered by our integration test suite">✨</a></td>
       <td style="text-align:right">✅</td>
    </tr>
    <tr>
      <td>CreateResourceServer <a href="#misc" title="covered by our integration test suite">✨</a></td>
       <td style="text-align:right">✅</td>
    </tr>
    <tr>
      <td>CreateUserPool <a href="#misc" title="covered by our integration test suite">✨</a></td>
       <td style="text-align:right">✅</td>
    </tr>
    <tr>
      <td>CreateUserPoolClient <a href="#misc" title="covered by our integration test suite">✨</a></td>
       <td style="text-align:right">✅</td>
    </tr>
    <tr>
      <td>CreateUserPoolDomain</td>
       <td style="text-align:right">✅</td>
    </tr>
    <tr>
      <td>DeleteGroup <a href="#misc" title="covered by our integration test suite">✨</a></td>
       <td style="text-align:right">✅</td>
    </tr>
    <tr>
      <td>DeleteIdentityProvider <a href="#misc" title="covered by our integration test suite">✨</a></td>
       <td style="text-align:right">✅</td>
    </tr>
    <tr>
      <td>DeleteResourceServer <a href="#misc" title="covered by our integration test suite">✨</a></td>
       <td style="text-align:right">✅</td>
    </tr>
    <tr>
      <td>DeleteUserAttributes <a href="#misc" title="covered by our integration test suite">✨</a></td>
       <td style="text-align:right">✅</td>
    </tr>
    <tr>
      <td>DeleteUserPool <a href="#misc" title="covered by our integration test suite">✨</a></td>
       <td style="text-align:right">✅</td>
    </tr>
    <tr>
      <td>DeleteUserPoolClient <a href="#misc" title="covered by our integration test suite">✨</a></td>
       <td style="text-align:right">✅</td>
    </tr>
    <tr>
      <td>DeleteUserPoolDomain</td>
       <td style="text-align:right">✅</td>
    </tr>
    <tr>
      <td>DescribeIdentityProvider <a href="#misc" title="covered by our integration test suite">✨</a></td>
       <td style="text-align:right">✅</td>
    </tr>
    <tr>
      <td>DescribeResourceServer <a href="#misc" title="covered by our integration test suite">✨</a></td>
       <td style="text-align:right">✅</td>
    </tr>
    <tr>
      <td>DescribeUserPool <a href="#misc" title="covered by our integration test suite">✨</a></td>
       <td style="text-align:right">✅</td>
    </tr>
    <tr>
      <td>DescribeUserPoolClient <a href="#misc" title="covered by our integration test suite">✨</a></td>
       <td style="text-align:right">✅</td>
    </tr>
    <tr>
      <td>DescribeUserPoolDomain</td>
       <td style="text-align:right">✅</td>
    </tr>
    <tr>
      <td>ForgotPassword <a href="#misc" title="covered by our integration test suite">✨</a></td>
       <td style="text-align:right">✅</td>
    </tr>
    <tr>
      <td>GetGroup</td>
       <td style="text-align:right">✅</td>
    </tr>
    <tr>
      <td>GetSigningCertificate <a href="#misc" title="covered by our integration test suite">✨</a></td>
       <td style="text-align:right">✅</td>
    </tr>
    <tr>
      <td>GetUser <a href="#misc" title="covered by our integration test suite">✨</a></td>
       <td style="text-align:right">✅</td>
    </tr>
    <tr>
      <td>GetUserPoolMfaConfig <a href="#misc" title="covered by our integration test suite">✨</a></td>
       <td style="text-align:right">✅</td>
    </tr>
    <tr>
      <td>GlobalSignOut <a href="#misc" title="covered by our integration test suite">✨</a></td>
       <td style="text-align:right">✅</td>
    </tr>
    <tr>
      <td>InitiateAuth <a href="#misc" title="covered by our integration test suite">✨</a></td>
       <td style="text-align:right">✅</td>
    </tr>
    <tr>
      <td>ListGroups <a href="#misc" title="covered by our integration test suite">✨</a></td>
       <td style="text-align:right">✅</td>
    </tr>
    <tr>
      <td>ListIdentityProviders <a href="#misc" title="covered by our integration test suite">✨</a></td>
       <td style="text-align:right">✅</td>
    </tr>
    <tr>
      <td>ListResourceServers <a href="#misc" title="covered by our integration test suite">✨</a></td>
       <td style="text-align:right">✅</td>
    </tr>
    <tr>
      <td>ListUserPoolClients <a href="#misc" title="covered by our integration test suite">✨</a></td>
       <td style="text-align:right">✅</td>
    </tr>
    <tr>
      <td>ListUserPools <a href="#misc" title="covered by our integration test suite">✨</a></td>
       <td style="text-align:right">✅</td>
    </tr>
    <tr>
      <td>ListUsers <a href="#misc" title="covered by our integration test suite">✨</a></td>
       <td style="text-align:right">✅</td>
    </tr>
    <tr>
      <td>ListUsersInGroup <a href="#misc" title="covered by our integration test suite">✨</a></td>
       <td style="text-align:right">✅</td>
    </tr>
    <tr>
      <td>RespondToAuthChallenge <a href="#misc" title="covered by our integration test suite">✨</a></td>
       <td style="text-align:right">✅</td>
    </tr>
    <tr>
      <td>SetUserMFAPreference <a href="#misc" title="covered by our integration test suite">✨</a></td>
       <td style="text-align:right">✅</td>
    </tr>
    <tr>
      <td>SetUserPoolMfaConfig <a href="#misc" title="covered by our integration test suite">✨</a></td>
       <td style="text-align:right">✅</td>
    </tr>
    <tr>
      <td>SignUp <a href="#misc" title="covered by our integration test suite">✨</a></td>
       <td style="text-align:right">✅</td>
    </tr>
    <tr>
      <td>UpdateGroup</td>
       <td style="text-align:right">✅</td>
    </tr>
    <tr>
      <td>UpdateIdentityProvider <a href="#misc" title="covered by our integration test suite">✨</a></td>
       <td style="text-align:right">✅</td>
    </tr>
    <tr>
      <td>UpdateResourceServer</td>
       <td style="text-align:right">✅</td>
    </tr>
    <tr>
      <td>UpdateUserAttributes</td>
       <td style="text-align:right">✅</td>
    </tr>
    <tr>
      <td>UpdateUserPool <a href="#misc" title="covered by our integration test suite">✨</a></td>
       <td style="text-align:right">✅</td>
    </tr>
    <tr>
      <td>UpdateUserPoolClient</td>
       <td style="text-align:right">✅</td>
    </tr>
    <tr>
      <td><a data-toggle="collapse" href=".acm-notimplemented">Show more</a></td>
      <td style="text-align:right"></td>
    </tr>
    <tr class="collapse acm-notimplemented">
      <td>AdminDisableProviderForUser</td>
       <td style="text-align:right">-</td>
    </tr>
    <tr class="collapse acm-notimplemented">
      <td>AdminForgetDevice</td>
       <td style="text-align:right">-</td>
    </tr>
    <tr class="collapse acm-notimplemented">
      <td>AdminGetDevice</td>
       <td style="text-align:right">-</td>
    </tr>
    <tr class="collapse acm-notimplemented">
      <td>AdminLinkProviderForUser</td>
       <td style="text-align:right">-</td>
    </tr>
    <tr class="collapse acm-notimplemented">
      <td>AdminListDevices</td>
       <td style="text-align:right">-</td>
    </tr>
    <tr class="collapse acm-notimplemented">
      <td>AdminListUserAuthEvents</td>
       <td style="text-align:right">-</td>
    </tr>
    <tr class="collapse acm-notimplemented">
      <td>AdminSetUserSettings</td>
       <td style="text-align:right">-</td>
    </tr>
    <tr class="collapse acm-notimplemented">
      <td>AdminUpdateAuthEventFeedback</td>
       <td style="text-align:right">-</td>
    </tr>
    <tr class="collapse acm-notimplemented">
      <td>AdminUpdateDeviceStatus</td>
       <td style="text-align:right">-</td>
    </tr>
    <tr class="collapse acm-notimplemented">
      <td>AssociateSoftwareToken</td>
       <td style="text-align:right">-</td>
    </tr>
    <tr class="collapse acm-notimplemented">
      <td>CreateUserImportJob</td>
       <td style="text-align:right">-</td>
    </tr>
    <tr class="collapse acm-notimplemented">
      <td>DeleteUser</td>
       <td style="text-align:right">-</td>
    </tr>
    <tr class="collapse acm-notimplemented">
      <td>DescribeRiskConfiguration</td>
       <td style="text-align:right">-</td>
    </tr>
    <tr class="collapse acm-notimplemented">
      <td>DescribeUserImportJob</td>
       <td style="text-align:right">-</td>
    </tr>
    <tr class="collapse acm-notimplemented">
      <td>ForgetDevice</td>
       <td style="text-align:right">-</td>
    </tr>
    <tr class="collapse acm-notimplemented">
      <td>GetCSVHeader</td>
       <td style="text-align:right">-</td>
    </tr>
    <tr class="collapse acm-notimplemented">
      <td>GetDevice</td>
       <td style="text-align:right">-</td>
    </tr>
    <tr class="collapse acm-notimplemented">
      <td>GetIdentityProviderByIdentifier</td>
       <td style="text-align:right">-</td>
    </tr>
    <tr class="collapse acm-notimplemented">
      <td>GetUICustomization</td>
       <td style="text-align:right">-</td>
    </tr>
    <tr class="collapse acm-notimplemented">
      <td>GetUserAttributeVerificationCode</td>
       <td style="text-align:right">-</td>
    </tr>
    <tr class="collapse acm-notimplemented">
      <td>ListDevices</td>
       <td style="text-align:right">-</td>
    </tr>
    <tr class="collapse acm-notimplemented">
      <td>ListTagsForResource</td>
       <td style="text-align:right">-</td>
    </tr>
    <tr class="collapse acm-notimplemented">
      <td>ListUserImportJobs</td>
       <td style="text-align:right">-</td>
    </tr>
    <tr class="collapse acm-notimplemented">
      <td>ResendConfirmationCode</td>
       <td style="text-align:right">-</td>
    </tr>
    <tr class="collapse acm-notimplemented">
      <td>RevokeToken</td>
       <td style="text-align:right">-</td>
    </tr>
    <tr class="collapse acm-notimplemented">
      <td>SetRiskConfiguration</td>
       <td style="text-align:right">-</td>
    </tr>
    <tr class="collapse acm-notimplemented">
      <td>SetUICustomization</td>
       <td style="text-align:right">-</td>
    </tr>
    <tr class="collapse acm-notimplemented">
      <td>SetUserSettings</td>
       <td style="text-align:right">-</td>
    </tr>
    <tr class="collapse acm-notimplemented">
      <td>StartUserImportJob</td>
       <td style="text-align:right">-</td>
    </tr>
    <tr class="collapse acm-notimplemented">
      <td>StopUserImportJob</td>
       <td style="text-align:right">-</td>
    </tr>
    <tr class="collapse acm-notimplemented">
      <td>TagResource</td>
       <td style="text-align:right">-</td>
    </tr>
    <tr class="collapse acm-notimplemented">
      <td>UntagResource</td>
       <td style="text-align:right">-</td>
    </tr>
    <tr class="collapse acm-notimplemented">
      <td>UpdateAuthEventFeedback</td>
       <td style="text-align:right">-</td>
    </tr>
    <tr class="collapse acm-notimplemented">
      <td>UpdateDeviceStatus</td>
       <td style="text-align:right">-</td>
    </tr>
    <tr class="collapse acm-notimplemented">
      <td>UpdateUserPoolDomain</td>
       <td style="text-align:right">-</td>
    </tr>
    <tr class="collapse acm-notimplemented">
      <td>VerifySoftwareToken</td>
       <td style="text-align:right">-</td>
    </tr>
    <tr class="collapse acm-notimplemented">
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
    <tr>
      <td><a data-toggle="collapse" href=".acm-notimplemented">Show more</a></td>
      <td style="text-align:right"></td>
    </tr>
    <tr class="collapse acm-notimplemented">
      <td>DeleteConformancePack</td>
       <td style="text-align:right">-</td>
    </tr>
    <tr class="collapse acm-notimplemented">
      <td>DeleteEvaluationResults</td>
       <td style="text-align:right">-</td>
    </tr>
    <tr class="collapse acm-notimplemented">
      <td>DeleteOrganizationConfigRule</td>
       <td style="text-align:right">-</td>
    </tr>
    <tr class="collapse acm-notimplemented">
      <td>DeletePendingAggregationRequest</td>
       <td style="text-align:right">-</td>
    </tr>
    <tr class="collapse acm-notimplemented">
      <td>DeleteRemediationConfiguration</td>
       <td style="text-align:right">-</td>
    </tr>
    <tr class="collapse acm-notimplemented">
      <td>DeleteRemediationExceptions</td>
       <td style="text-align:right">-</td>
    </tr>
    <tr class="collapse acm-notimplemented">
      <td>DeleteResourceConfig</td>
       <td style="text-align:right">-</td>
    </tr>
    <tr class="collapse acm-notimplemented">
      <td>DeleteRetentionConfiguration</td>
       <td style="text-align:right">-</td>
    </tr>
    <tr class="collapse acm-notimplemented">
      <td>DeleteStoredQuery</td>
       <td style="text-align:right">-</td>
    </tr>
    <tr class="collapse acm-notimplemented">
      <td>DeliverConfigSnapshot</td>
       <td style="text-align:right">-</td>
    </tr>
    <tr class="collapse acm-notimplemented">
      <td>DescribeAggregateComplianceByConfigRules</td>
       <td style="text-align:right">-</td>
    </tr>
    <tr class="collapse acm-notimplemented">
      <td>DescribeAggregateComplianceByConformancePacks</td>
       <td style="text-align:right">-</td>
    </tr>
    <tr class="collapse acm-notimplemented">
      <td>DescribeComplianceByConfigRule</td>
       <td style="text-align:right">-</td>
    </tr>
    <tr class="collapse acm-notimplemented">
      <td>DescribeComplianceByResource</td>
       <td style="text-align:right">-</td>
    </tr>
    <tr class="collapse acm-notimplemented">
      <td>DescribeConfigRuleEvaluationStatus</td>
       <td style="text-align:right">-</td>
    </tr>
    <tr class="collapse acm-notimplemented">
      <td>DescribeConfigurationAggregatorSourcesStatus</td>
       <td style="text-align:right">-</td>
    </tr>
    <tr class="collapse acm-notimplemented">
      <td>DescribeConformancePackCompliance</td>
       <td style="text-align:right">-</td>
    </tr>
    <tr class="collapse acm-notimplemented">
      <td>DescribeConformancePackStatus</td>
       <td style="text-align:right">-</td>
    </tr>
    <tr class="collapse acm-notimplemented">
      <td>DescribeConformancePacks</td>
       <td style="text-align:right">-</td>
    </tr>
    <tr class="collapse acm-notimplemented">
      <td>DescribeDeliveryChannelStatus</td>
       <td style="text-align:right">-</td>
    </tr>
    <tr class="collapse acm-notimplemented">
      <td>DescribeOrganizationConfigRuleStatuses</td>
       <td style="text-align:right">-</td>
    </tr>
    <tr class="collapse acm-notimplemented">
      <td>DescribeOrganizationConfigRules</td>
       <td style="text-align:right">-</td>
    </tr>
    <tr class="collapse acm-notimplemented">
      <td>DescribePendingAggregationRequests</td>
       <td style="text-align:right">-</td>
    </tr>
    <tr class="collapse acm-notimplemented">
      <td>DescribeRemediationConfigurations</td>
       <td style="text-align:right">-</td>
    </tr>
    <tr class="collapse acm-notimplemented">
      <td>DescribeRemediationExceptions</td>
       <td style="text-align:right">-</td>
    </tr>
    <tr class="collapse acm-notimplemented">
      <td>DescribeRemediationExecutionStatus</td>
       <td style="text-align:right">-</td>
    </tr>
    <tr class="collapse acm-notimplemented">
      <td>DescribeRetentionConfigurations</td>
       <td style="text-align:right">-</td>
    </tr>
    <tr class="collapse acm-notimplemented">
      <td>GetAggregateComplianceDetailsByConfigRule</td>
       <td style="text-align:right">-</td>
    </tr>
    <tr class="collapse acm-notimplemented">
      <td>GetAggregateConfigRuleComplianceSummary</td>
       <td style="text-align:right">-</td>
    </tr>
    <tr class="collapse acm-notimplemented">
      <td>GetAggregateConformancePackComplianceSummary</td>
       <td style="text-align:right">-</td>
    </tr>
    <tr class="collapse acm-notimplemented">
      <td>GetAggregateDiscoveredResourceCounts</td>
       <td style="text-align:right">-</td>
    </tr>
    <tr class="collapse acm-notimplemented">
      <td>GetAggregateResourceConfig</td>
       <td style="text-align:right">-</td>
    </tr>
    <tr class="collapse acm-notimplemented">
      <td>GetComplianceDetailsByConfigRule</td>
       <td style="text-align:right">-</td>
    </tr>
    <tr class="collapse acm-notimplemented">
      <td>GetComplianceDetailsByResource</td>
       <td style="text-align:right">-</td>
    </tr>
    <tr class="collapse acm-notimplemented">
      <td>GetComplianceSummaryByConfigRule</td>
       <td style="text-align:right">-</td>
    </tr>
    <tr class="collapse acm-notimplemented">
      <td>GetComplianceSummaryByResourceType</td>
       <td style="text-align:right">-</td>
    </tr>
    <tr class="collapse acm-notimplemented">
      <td>GetConformancePackComplianceDetails</td>
       <td style="text-align:right">-</td>
    </tr>
    <tr class="collapse acm-notimplemented">
      <td>GetConformancePackComplianceSummary</td>
       <td style="text-align:right">-</td>
    </tr>
    <tr class="collapse acm-notimplemented">
      <td>GetCustomRulePolicy</td>
       <td style="text-align:right">-</td>
    </tr>
    <tr class="collapse acm-notimplemented">
      <td>GetDiscoveredResourceCounts</td>
       <td style="text-align:right">-</td>
    </tr>
    <tr class="collapse acm-notimplemented">
      <td>GetOrganizationConfigRuleDetailedStatus</td>
       <td style="text-align:right">-</td>
    </tr>
    <tr class="collapse acm-notimplemented">
      <td>GetOrganizationCustomRulePolicy</td>
       <td style="text-align:right">-</td>
    </tr>
    <tr class="collapse acm-notimplemented">
      <td>GetStoredQuery</td>
       <td style="text-align:right">-</td>
    </tr>
    <tr class="collapse acm-notimplemented">
      <td>ListStoredQueries</td>
       <td style="text-align:right">-</td>
    </tr>
    <tr class="collapse acm-notimplemented">
      <td>PutConformancePack</td>
       <td style="text-align:right">-</td>
    </tr>
    <tr class="collapse acm-notimplemented">
      <td>PutExternalEvaluation</td>
       <td style="text-align:right">-</td>
    </tr>
    <tr class="collapse acm-notimplemented">
      <td>PutOrganizationConfigRule</td>
       <td style="text-align:right">-</td>
    </tr>
    <tr class="collapse acm-notimplemented">
      <td>PutRemediationConfigurations</td>
       <td style="text-align:right">-</td>
    </tr>
    <tr class="collapse acm-notimplemented">
      <td>PutRemediationExceptions</td>
       <td style="text-align:right">-</td>
    </tr>
    <tr class="collapse acm-notimplemented">
      <td>PutResourceConfig</td>
       <td style="text-align:right">-</td>
    </tr>
    <tr class="collapse acm-notimplemented">
      <td>PutRetentionConfiguration</td>
       <td style="text-align:right">-</td>
    </tr>
    <tr class="collapse acm-notimplemented">
      <td>PutStoredQuery</td>
       <td style="text-align:right">-</td>
    </tr>
    <tr class="collapse acm-notimplemented">
      <td>SelectAggregateResourceConfig</td>
       <td style="text-align:right">-</td>
    </tr>
    <tr class="collapse acm-notimplemented">
      <td>SelectResourceConfig</td>
       <td style="text-align:right">-</td>
    </tr>
    <tr class="collapse acm-notimplemented">
      <td>StartConfigRulesEvaluation</td>
       <td style="text-align:right">-</td>
    </tr>
    <tr class="collapse acm-notimplemented">
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
      <td>AddTagsToResource</td>
       <td style="text-align:right">✅</td>
    </tr>
    <tr>
      <td>CopyDBClusterSnapshot</td>
       <td style="text-align:right">✅</td>
    </tr>
    <tr>
      <td>CreateDBCluster</td>
       <td style="text-align:right">✅</td>
    </tr>
    <tr>
      <td>CreateDBClusterParameterGroup</td>
       <td style="text-align:right">✅</td>
    </tr>
    <tr>
      <td>CreateDBClusterSnapshot</td>
       <td style="text-align:right">✅</td>
    </tr>
    <tr>
      <td>CreateDBInstance</td>
       <td style="text-align:right">✅</td>
    </tr>
    <tr>
      <td>CreateDBSubnetGroup</td>
       <td style="text-align:right">✅</td>
    </tr>
    <tr>
      <td>CreateEventSubscription</td>
       <td style="text-align:right">✅</td>
    </tr>
    <tr>
      <td>DeleteDBCluster</td>
       <td style="text-align:right">✅</td>
    </tr>
    <tr>
      <td>DeleteDBClusterParameterGroup</td>
       <td style="text-align:right">✅</td>
    </tr>
    <tr>
      <td>DeleteDBClusterSnapshot</td>
       <td style="text-align:right">✅</td>
    </tr>
    <tr>
      <td>DeleteDBInstance</td>
       <td style="text-align:right">✅</td>
    </tr>
    <tr>
      <td>DeleteDBSubnetGroup</td>
       <td style="text-align:right">✅</td>
    </tr>
    <tr>
      <td>DeleteEventSubscription</td>
       <td style="text-align:right">✅</td>
    </tr>
    <tr>
      <td>DescribeCertificates</td>
       <td style="text-align:right">✅</td>
    </tr>
    <tr>
      <td>DescribeDBClusterParameterGroups</td>
       <td style="text-align:right">✅</td>
    </tr>
    <tr>
      <td>DescribeDBClusterParameters</td>
       <td style="text-align:right">✅</td>
    </tr>
    <tr>
      <td>DescribeDBClusterSnapshots</td>
       <td style="text-align:right">✅</td>
    </tr>
    <tr>
      <td>DescribeDBClusters</td>
       <td style="text-align:right">✅</td>
    </tr>
    <tr>
      <td>DescribeDBEngineVersions</td>
       <td style="text-align:right">✅</td>
    </tr>
    <tr>
      <td>DescribeDBInstances</td>
       <td style="text-align:right">✅</td>
    </tr>
    <tr>
      <td>DescribeDBSubnetGroups</td>
       <td style="text-align:right">✅</td>
    </tr>
    <tr>
      <td>DescribeEventSubscriptions</td>
       <td style="text-align:right">✅</td>
    </tr>
    <tr>
      <td>DescribeGlobalClusters</td>
       <td style="text-align:right">✅</td>
    </tr>
    <tr>
      <td>ListTagsForResource</td>
       <td style="text-align:right">✅</td>
    </tr>
    <tr>
      <td>ModifyDBCluster</td>
       <td style="text-align:right">✅</td>
    </tr>
    <tr>
      <td>ModifyDBClusterParameterGroup</td>
       <td style="text-align:right">✅</td>
    </tr>
    <tr>
      <td>ModifyDBInstance</td>
       <td style="text-align:right">✅</td>
    </tr>
    <tr>
      <td>ModifyDBSubnetGroup</td>
       <td style="text-align:right">✅</td>
    </tr>
    <tr>
      <td>RebootDBInstance</td>
       <td style="text-align:right">✅</td>
    </tr>
    <tr>
      <td>RemoveTagsFromResource</td>
       <td style="text-align:right">✅</td>
    </tr>
    <tr>
      <td>ResetDBClusterParameterGroup</td>
       <td style="text-align:right">✅</td>
    </tr>
    <tr>
      <td>RestoreDBClusterFromSnapshot</td>
       <td style="text-align:right">✅</td>
    </tr>
    <tr>
      <td>StartDBCluster</td>
       <td style="text-align:right">✅</td>
    </tr>
    <tr>
      <td>StopDBCluster</td>
       <td style="text-align:right">✅</td>
    </tr>
    <tr>
      <td><a data-toggle="collapse" href=".acm-notimplemented">Show more</a></td>
      <td style="text-align:right"></td>
    </tr>
    <tr class="collapse acm-notimplemented">
      <td>AddSourceIdentifierToSubscription</td>
       <td style="text-align:right">-</td>
    </tr>
    <tr class="collapse acm-notimplemented">
      <td>ApplyPendingMaintenanceAction</td>
       <td style="text-align:right">-</td>
    </tr>
    <tr class="collapse acm-notimplemented">
      <td>CopyDBClusterParameterGroup</td>
       <td style="text-align:right">-</td>
    </tr>
    <tr class="collapse acm-notimplemented">
      <td>CreateGlobalCluster</td>
       <td style="text-align:right">-</td>
    </tr>
    <tr class="collapse acm-notimplemented">
      <td>DeleteGlobalCluster</td>
       <td style="text-align:right">-</td>
    </tr>
    <tr class="collapse acm-notimplemented">
      <td>DescribeDBClusterSnapshotAttributes</td>
       <td style="text-align:right">-</td>
    </tr>
    <tr class="collapse acm-notimplemented">
      <td>DescribeEngineDefaultClusterParameters</td>
       <td style="text-align:right">-</td>
    </tr>
    <tr class="collapse acm-notimplemented">
      <td>DescribeEventCategories</td>
       <td style="text-align:right">-</td>
    </tr>
    <tr class="collapse acm-notimplemented">
      <td>DescribeEvents</td>
       <td style="text-align:right">-</td>
    </tr>
    <tr class="collapse acm-notimplemented">
      <td>DescribeOrderableDBInstanceOptions</td>
       <td style="text-align:right">-</td>
    </tr>
    <tr class="collapse acm-notimplemented">
      <td>DescribePendingMaintenanceActions</td>
       <td style="text-align:right">-</td>
    </tr>
    <tr class="collapse acm-notimplemented">
      <td>FailoverDBCluster</td>
       <td style="text-align:right">-</td>
    </tr>
    <tr class="collapse acm-notimplemented">
      <td>ModifyDBClusterSnapshotAttribute</td>
       <td style="text-align:right">-</td>
    </tr>
    <tr class="collapse acm-notimplemented">
      <td>ModifyEventSubscription</td>
       <td style="text-align:right">-</td>
    </tr>
    <tr class="collapse acm-notimplemented">
      <td>ModifyGlobalCluster</td>
       <td style="text-align:right">-</td>
    </tr>
    <tr class="collapse acm-notimplemented">
      <td>RemoveFromGlobalCluster</td>
       <td style="text-align:right">-</td>
    </tr>
    <tr class="collapse acm-notimplemented">
      <td>RemoveSourceIdentifierFromSubscription</td>
       <td style="text-align:right">-</td>
    </tr>
    <tr class="collapse acm-notimplemented">
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
      <td>CreateBackup <a href="#misc" title="covered by our integration test suite">✨</a></td>
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
      <td>DeleteBackup <a href="#misc" title="covered by our integration test suite">✨</a></td>
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
      <td>ListBackups</td>
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
      <td>RestoreTableFromBackup <a href="#misc" title="covered by our integration test suite">✨</a></td>
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
    <tr>
      <td><a data-toggle="collapse" href=".acm-notimplemented">Show more</a></td>
      <td style="text-align:right"></td>
    </tr>
    <tr class="collapse acm-notimplemented">
      <td>DescribeBackup</td>
       <td style="text-align:right">-</td>
    </tr>
    <tr class="collapse acm-notimplemented">
      <td>DescribeContinuousBackups</td>
       <td style="text-align:right">-</td>
    </tr>
    <tr class="collapse acm-notimplemented">
      <td>DescribeContributorInsights</td>
       <td style="text-align:right">-</td>
    </tr>
    <tr class="collapse acm-notimplemented">
      <td>DescribeEndpoints</td>
       <td style="text-align:right">-</td>
    </tr>
    <tr class="collapse acm-notimplemented">
      <td>DescribeExport</td>
       <td style="text-align:right">-</td>
    </tr>
    <tr class="collapse acm-notimplemented">
      <td>DescribeGlobalTableSettings</td>
       <td style="text-align:right">-</td>
    </tr>
    <tr class="collapse acm-notimplemented">
      <td>DescribeTableReplicaAutoScaling</td>
       <td style="text-align:right">-</td>
    </tr>
    <tr class="collapse acm-notimplemented">
      <td>ExportTableToPointInTime</td>
       <td style="text-align:right">-</td>
    </tr>
    <tr class="collapse acm-notimplemented">
      <td>ListContributorInsights</td>
       <td style="text-align:right">-</td>
    </tr>
    <tr class="collapse acm-notimplemented">
      <td>ListExports</td>
       <td style="text-align:right">-</td>
    </tr>
    <tr class="collapse acm-notimplemented">
      <td>RestoreTableToPointInTime</td>
       <td style="text-align:right">-</td>
    </tr>
    <tr class="collapse acm-notimplemented">
      <td>UpdateContinuousBackups</td>
       <td style="text-align:right">-</td>
    </tr>
    <tr class="collapse acm-notimplemented">
      <td>UpdateContributorInsights</td>
       <td style="text-align:right">-</td>
    </tr>
    <tr class="collapse acm-notimplemented">
      <td>UpdateGlobalTableSettings</td>
       <td style="text-align:right">-</td>
    </tr>
    <tr class="collapse acm-notimplemented">
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
      <td>AcceptTransitGatewayPeeringAttachment</td>
       <td style="text-align:right">✅</td>
    </tr>
    <tr>
      <td>AcceptVpcPeeringConnection <a href="#misc" title="covered by our integration test suite">✨</a></td>
       <td style="text-align:right">✅</td>
    </tr>
    <tr>
      <td>AllocateAddress <a href="#misc" title="covered by our integration test suite">✨</a></td>
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
      <td>CreateDhcpOptions</td>
       <td style="text-align:right">✅</td>
    </tr>
    <tr>
      <td>CreateEgressOnlyInternetGateway</td>
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
      <td>DescribeInstanceStatus</td>
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
      <td>DescribeKeyPairs</td>
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
    <tr>
      <td><a data-toggle="collapse" href=".acm-notimplemented">Show more</a></td>
      <td style="text-align:right"></td>
    </tr>
    <tr class="collapse acm-notimplemented">
      <td>AcceptReservedInstancesExchangeQuote</td>
       <td style="text-align:right">-</td>
    </tr>
    <tr class="collapse acm-notimplemented">
      <td>AcceptTransitGatewayMulticastDomainAssociations</td>
       <td style="text-align:right">-</td>
    </tr>
    <tr class="collapse acm-notimplemented">
      <td>AcceptTransitGatewayVpcAttachment</td>
       <td style="text-align:right">-</td>
    </tr>
    <tr class="collapse acm-notimplemented">
      <td>AcceptVpcEndpointConnections</td>
       <td style="text-align:right">-</td>
    </tr>
    <tr class="collapse acm-notimplemented">
      <td>AdvertiseByoipCidr</td>
       <td style="text-align:right">-</td>
    </tr>
    <tr class="collapse acm-notimplemented">
      <td>AllocateHosts</td>
       <td style="text-align:right">-</td>
    </tr>
    <tr class="collapse acm-notimplemented">
      <td>AllocateIpamPoolCidr</td>
       <td style="text-align:right">-</td>
    </tr>
    <tr class="collapse acm-notimplemented">
      <td>ApplySecurityGroupsToClientVpnTargetNetwork</td>
       <td style="text-align:right">-</td>
    </tr>
    <tr class="collapse acm-notimplemented">
      <td>AssociateClientVpnTargetNetwork</td>
       <td style="text-align:right">-</td>
    </tr>
    <tr class="collapse acm-notimplemented">
      <td>AssociateEnclaveCertificateIamRole</td>
       <td style="text-align:right">-</td>
    </tr>
    <tr class="collapse acm-notimplemented">
      <td>AssociateInstanceEventWindow</td>
       <td style="text-align:right">-</td>
    </tr>
    <tr class="collapse acm-notimplemented">
      <td>AssociateTransitGatewayMulticastDomain</td>
       <td style="text-align:right">-</td>
    </tr>
    <tr class="collapse acm-notimplemented">
      <td>AssociateTrunkInterface</td>
       <td style="text-align:right">-</td>
    </tr>
    <tr class="collapse acm-notimplemented">
      <td>AttachClassicLinkVpc</td>
       <td style="text-align:right">-</td>
    </tr>
    <tr class="collapse acm-notimplemented">
      <td>AuthorizeClientVpnIngress</td>
       <td style="text-align:right">-</td>
    </tr>
    <tr class="collapse acm-notimplemented">
      <td>BundleInstance</td>
       <td style="text-align:right">-</td>
    </tr>
    <tr class="collapse acm-notimplemented">
      <td>CancelBundleTask</td>
       <td style="text-align:right">-</td>
    </tr>
    <tr class="collapse acm-notimplemented">
      <td>CancelCapacityReservation</td>
       <td style="text-align:right">-</td>
    </tr>
    <tr class="collapse acm-notimplemented">
      <td>CancelCapacityReservationFleets</td>
       <td style="text-align:right">-</td>
    </tr>
    <tr class="collapse acm-notimplemented">
      <td>CancelConversionTask</td>
       <td style="text-align:right">-</td>
    </tr>
    <tr class="collapse acm-notimplemented">
      <td>CancelExportTask</td>
       <td style="text-align:right">-</td>
    </tr>
    <tr class="collapse acm-notimplemented">
      <td>CancelImportTask</td>
       <td style="text-align:right">-</td>
    </tr>
    <tr class="collapse acm-notimplemented">
      <td>CancelReservedInstancesListing</td>
       <td style="text-align:right">-</td>
    </tr>
    <tr class="collapse acm-notimplemented">
      <td>ConfirmProductInstance</td>
       <td style="text-align:right">-</td>
    </tr>
    <tr class="collapse acm-notimplemented">
      <td>CopyFpgaImage</td>
       <td style="text-align:right">-</td>
    </tr>
    <tr class="collapse acm-notimplemented">
      <td>CreateCapacityReservation</td>
       <td style="text-align:right">-</td>
    </tr>
    <tr class="collapse acm-notimplemented">
      <td>CreateCapacityReservationFleet</td>
       <td style="text-align:right">-</td>
    </tr>
    <tr class="collapse acm-notimplemented">
      <td>CreateClientVpnEndpoint</td>
       <td style="text-align:right">-</td>
    </tr>
    <tr class="collapse acm-notimplemented">
      <td>CreateClientVpnRoute</td>
       <td style="text-align:right">-</td>
    </tr>
    <tr class="collapse acm-notimplemented">
      <td>CreateDefaultSubnet</td>
       <td style="text-align:right">-</td>
    </tr>
    <tr class="collapse acm-notimplemented">
      <td>CreateDefaultVpc</td>
       <td style="text-align:right">-</td>
    </tr>
    <tr class="collapse acm-notimplemented">
      <td>CreateFleet</td>
       <td style="text-align:right">-</td>
    </tr>
    <tr class="collapse acm-notimplemented">
      <td>CreateFpgaImage</td>
       <td style="text-align:right">-</td>
    </tr>
    <tr class="collapse acm-notimplemented">
      <td>CreateInstanceEventWindow</td>
       <td style="text-align:right">-</td>
    </tr>
    <tr class="collapse acm-notimplemented">
      <td>CreateInstanceExportTask</td>
       <td style="text-align:right">-</td>
    </tr>
    <tr class="collapse acm-notimplemented">
      <td>CreateIpam</td>
       <td style="text-align:right">-</td>
    </tr>
    <tr class="collapse acm-notimplemented">
      <td>CreateIpamPool</td>
       <td style="text-align:right">-</td>
    </tr>
    <tr class="collapse acm-notimplemented">
      <td>CreateIpamScope</td>
       <td style="text-align:right">-</td>
    </tr>
    <tr class="collapse acm-notimplemented">
      <td>CreateLocalGatewayRoute</td>
       <td style="text-align:right">-</td>
    </tr>
    <tr class="collapse acm-notimplemented">
      <td>CreateLocalGatewayRouteTableVpcAssociation</td>
       <td style="text-align:right">-</td>
    </tr>
    <tr class="collapse acm-notimplemented">
      <td>CreateNetworkInsightsAccessScope</td>
       <td style="text-align:right">-</td>
    </tr>
    <tr class="collapse acm-notimplemented">
      <td>CreateNetworkInsightsPath</td>
       <td style="text-align:right">-</td>
    </tr>
    <tr class="collapse acm-notimplemented">
      <td>CreateNetworkInterfacePermission</td>
       <td style="text-align:right">-</td>
    </tr>
    <tr class="collapse acm-notimplemented">
      <td>CreatePublicIpv4Pool</td>
       <td style="text-align:right">-</td>
    </tr>
    <tr class="collapse acm-notimplemented">
      <td>CreateReplaceRootVolumeTask</td>
       <td style="text-align:right">-</td>
    </tr>
    <tr class="collapse acm-notimplemented">
      <td>CreateReservedInstancesListing</td>
       <td style="text-align:right">-</td>
    </tr>
    <tr class="collapse acm-notimplemented">
      <td>CreateRestoreImageTask</td>
       <td style="text-align:right">-</td>
    </tr>
    <tr class="collapse acm-notimplemented">
      <td>CreateStoreImageTask</td>
       <td style="text-align:right">-</td>
    </tr>
    <tr class="collapse acm-notimplemented">
      <td>CreateSubnetCidrReservation</td>
       <td style="text-align:right">-</td>
    </tr>
    <tr class="collapse acm-notimplemented">
      <td>CreateTrafficMirrorFilter</td>
       <td style="text-align:right">-</td>
    </tr>
    <tr class="collapse acm-notimplemented">
      <td>CreateTrafficMirrorFilterRule</td>
       <td style="text-align:right">-</td>
    </tr>
    <tr class="collapse acm-notimplemented">
      <td>CreateTrafficMirrorSession</td>
       <td style="text-align:right">-</td>
    </tr>
    <tr class="collapse acm-notimplemented">
      <td>CreateTrafficMirrorTarget</td>
       <td style="text-align:right">-</td>
    </tr>
    <tr class="collapse acm-notimplemented">
      <td>CreateTransitGatewayConnect</td>
       <td style="text-align:right">-</td>
    </tr>
    <tr class="collapse acm-notimplemented">
      <td>CreateTransitGatewayConnectPeer</td>
       <td style="text-align:right">-</td>
    </tr>
    <tr class="collapse acm-notimplemented">
      <td>CreateTransitGatewayMulticastDomain</td>
       <td style="text-align:right">-</td>
    </tr>
    <tr class="collapse acm-notimplemented">
      <td>CreateTransitGatewayPrefixListReference</td>
       <td style="text-align:right">-</td>
    </tr>
    <tr class="collapse acm-notimplemented">
      <td>CreateVpcEndpointConnectionNotification</td>
       <td style="text-align:right">-</td>
    </tr>
    <tr class="collapse acm-notimplemented">
      <td>CreateVpnConnectionRoute</td>
       <td style="text-align:right">-</td>
    </tr>
    <tr class="collapse acm-notimplemented">
      <td>DeleteClientVpnEndpoint</td>
       <td style="text-align:right">-</td>
    </tr>
    <tr class="collapse acm-notimplemented">
      <td>DeleteClientVpnRoute</td>
       <td style="text-align:right">-</td>
    </tr>
    <tr class="collapse acm-notimplemented">
      <td>DeleteFleets</td>
       <td style="text-align:right">-</td>
    </tr>
    <tr class="collapse acm-notimplemented">
      <td>DeleteFpgaImage</td>
       <td style="text-align:right">-</td>
    </tr>
    <tr class="collapse acm-notimplemented">
      <td>DeleteInstanceEventWindow</td>
       <td style="text-align:right">-</td>
    </tr>
    <tr class="collapse acm-notimplemented">
      <td>DeleteIpam</td>
       <td style="text-align:right">-</td>
    </tr>
    <tr class="collapse acm-notimplemented">
      <td>DeleteIpamPool</td>
       <td style="text-align:right">-</td>
    </tr>
    <tr class="collapse acm-notimplemented">
      <td>DeleteIpamScope</td>
       <td style="text-align:right">-</td>
    </tr>
    <tr class="collapse acm-notimplemented">
      <td>DeleteLaunchTemplateVersions</td>
       <td style="text-align:right">-</td>
    </tr>
    <tr class="collapse acm-notimplemented">
      <td>DeleteLocalGatewayRoute</td>
       <td style="text-align:right">-</td>
    </tr>
    <tr class="collapse acm-notimplemented">
      <td>DeleteLocalGatewayRouteTableVpcAssociation</td>
       <td style="text-align:right">-</td>
    </tr>
    <tr class="collapse acm-notimplemented">
      <td>DeleteNetworkInsightsAccessScope</td>
       <td style="text-align:right">-</td>
    </tr>
    <tr class="collapse acm-notimplemented">
      <td>DeleteNetworkInsightsAccessScopeAnalysis</td>
       <td style="text-align:right">-</td>
    </tr>
    <tr class="collapse acm-notimplemented">
      <td>DeleteNetworkInsightsAnalysis</td>
       <td style="text-align:right">-</td>
    </tr>
    <tr class="collapse acm-notimplemented">
      <td>DeleteNetworkInsightsPath</td>
       <td style="text-align:right">-</td>
    </tr>
    <tr class="collapse acm-notimplemented">
      <td>DeleteNetworkInterfacePermission</td>
       <td style="text-align:right">-</td>
    </tr>
    <tr class="collapse acm-notimplemented">
      <td>DeletePublicIpv4Pool</td>
       <td style="text-align:right">-</td>
    </tr>
    <tr class="collapse acm-notimplemented">
      <td>DeleteQueuedReservedInstances</td>
       <td style="text-align:right">-</td>
    </tr>
    <tr class="collapse acm-notimplemented">
      <td>DeleteSubnetCidrReservation</td>
       <td style="text-align:right">-</td>
    </tr>
    <tr class="collapse acm-notimplemented">
      <td>DeleteTrafficMirrorFilter</td>
       <td style="text-align:right">-</td>
    </tr>
    <tr class="collapse acm-notimplemented">
      <td>DeleteTrafficMirrorFilterRule</td>
       <td style="text-align:right">-</td>
    </tr>
    <tr class="collapse acm-notimplemented">
      <td>DeleteTrafficMirrorSession</td>
       <td style="text-align:right">-</td>
    </tr>
    <tr class="collapse acm-notimplemented">
      <td>DeleteTrafficMirrorTarget</td>
       <td style="text-align:right">-</td>
    </tr>
    <tr class="collapse acm-notimplemented">
      <td>DeleteTransitGatewayConnect</td>
       <td style="text-align:right">-</td>
    </tr>
    <tr class="collapse acm-notimplemented">
      <td>DeleteTransitGatewayConnectPeer</td>
       <td style="text-align:right">-</td>
    </tr>
    <tr class="collapse acm-notimplemented">
      <td>DeleteTransitGatewayMulticastDomain</td>
       <td style="text-align:right">-</td>
    </tr>
    <tr class="collapse acm-notimplemented">
      <td>DeleteTransitGatewayPrefixListReference</td>
       <td style="text-align:right">-</td>
    </tr>
    <tr class="collapse acm-notimplemented">
      <td>DeleteVpcEndpointConnectionNotifications</td>
       <td style="text-align:right">-</td>
    </tr>
    <tr class="collapse acm-notimplemented">
      <td>DeleteVpnConnectionRoute</td>
       <td style="text-align:right">-</td>
    </tr>
    <tr class="collapse acm-notimplemented">
      <td>DeprovisionByoipCidr</td>
       <td style="text-align:right">-</td>
    </tr>
    <tr class="collapse acm-notimplemented">
      <td>DeprovisionIpamPoolCidr</td>
       <td style="text-align:right">-</td>
    </tr>
    <tr class="collapse acm-notimplemented">
      <td>DeprovisionPublicIpv4PoolCidr</td>
       <td style="text-align:right">-</td>
    </tr>
    <tr class="collapse acm-notimplemented">
      <td>DeregisterInstanceEventNotificationAttributes</td>
       <td style="text-align:right">-</td>
    </tr>
    <tr class="collapse acm-notimplemented">
      <td>DeregisterTransitGatewayMulticastGroupMembers</td>
       <td style="text-align:right">-</td>
    </tr>
    <tr class="collapse acm-notimplemented">
      <td>DeregisterTransitGatewayMulticastGroupSources</td>
       <td style="text-align:right">-</td>
    </tr>
    <tr class="collapse acm-notimplemented">
      <td>DescribeAddressesAttribute</td>
       <td style="text-align:right">-</td>
    </tr>
    <tr class="collapse acm-notimplemented">
      <td>DescribeAggregateIdFormat</td>
       <td style="text-align:right">-</td>
    </tr>
    <tr class="collapse acm-notimplemented">
      <td>DescribeBundleTasks</td>
       <td style="text-align:right">-</td>
    </tr>
    <tr class="collapse acm-notimplemented">
      <td>DescribeByoipCidrs</td>
       <td style="text-align:right">-</td>
    </tr>
    <tr class="collapse acm-notimplemented">
      <td>DescribeCapacityReservationFleets</td>
       <td style="text-align:right">-</td>
    </tr>
    <tr class="collapse acm-notimplemented">
      <td>DescribeCapacityReservations</td>
       <td style="text-align:right">-</td>
    </tr>
    <tr class="collapse acm-notimplemented">
      <td>DescribeClassicLinkInstances</td>
       <td style="text-align:right">-</td>
    </tr>
    <tr class="collapse acm-notimplemented">
      <td>DescribeClientVpnAuthorizationRules</td>
       <td style="text-align:right">-</td>
    </tr>
    <tr class="collapse acm-notimplemented">
      <td>DescribeClientVpnConnections</td>
       <td style="text-align:right">-</td>
    </tr>
    <tr class="collapse acm-notimplemented">
      <td>DescribeClientVpnEndpoints</td>
       <td style="text-align:right">-</td>
    </tr>
    <tr class="collapse acm-notimplemented">
      <td>DescribeClientVpnRoutes</td>
       <td style="text-align:right">-</td>
    </tr>
    <tr class="collapse acm-notimplemented">
      <td>DescribeClientVpnTargetNetworks</td>
       <td style="text-align:right">-</td>
    </tr>
    <tr class="collapse acm-notimplemented">
      <td>DescribeCoipPools</td>
       <td style="text-align:right">-</td>
    </tr>
    <tr class="collapse acm-notimplemented">
      <td>DescribeConversionTasks</td>
       <td style="text-align:right">-</td>
    </tr>
    <tr class="collapse acm-notimplemented">
      <td>DescribeElasticGpus</td>
       <td style="text-align:right">-</td>
    </tr>
    <tr class="collapse acm-notimplemented">
      <td>DescribeExportImageTasks</td>
       <td style="text-align:right">-</td>
    </tr>
    <tr class="collapse acm-notimplemented">
      <td>DescribeExportTasks</td>
       <td style="text-align:right">-</td>
    </tr>
    <tr class="collapse acm-notimplemented">
      <td>DescribeFastLaunchImages</td>
       <td style="text-align:right">-</td>
    </tr>
    <tr class="collapse acm-notimplemented">
      <td>DescribeFastSnapshotRestores</td>
       <td style="text-align:right">-</td>
    </tr>
    <tr class="collapse acm-notimplemented">
      <td>DescribeFleetHistory</td>
       <td style="text-align:right">-</td>
    </tr>
    <tr class="collapse acm-notimplemented">
      <td>DescribeFleetInstances</td>
       <td style="text-align:right">-</td>
    </tr>
    <tr class="collapse acm-notimplemented">
      <td>DescribeFleets</td>
       <td style="text-align:right">-</td>
    </tr>
    <tr class="collapse acm-notimplemented">
      <td>DescribeFpgaImageAttribute</td>
       <td style="text-align:right">-</td>
    </tr>
    <tr class="collapse acm-notimplemented">
      <td>DescribeFpgaImages</td>
       <td style="text-align:right">-</td>
    </tr>
    <tr class="collapse acm-notimplemented">
      <td>DescribeHostReservationOfferings</td>
       <td style="text-align:right">-</td>
    </tr>
    <tr class="collapse acm-notimplemented">
      <td>DescribeHostReservations</td>
       <td style="text-align:right">-</td>
    </tr>
    <tr class="collapse acm-notimplemented">
      <td>DescribeHosts</td>
       <td style="text-align:right">-</td>
    </tr>
    <tr class="collapse acm-notimplemented">
      <td>DescribeIdFormat</td>
       <td style="text-align:right">-</td>
    </tr>
    <tr class="collapse acm-notimplemented">
      <td>DescribeIdentityIdFormat</td>
       <td style="text-align:right">-</td>
    </tr>
    <tr class="collapse acm-notimplemented">
      <td>DescribeImportImageTasks</td>
       <td style="text-align:right">-</td>
    </tr>
    <tr class="collapse acm-notimplemented">
      <td>DescribeImportSnapshotTasks</td>
       <td style="text-align:right">-</td>
    </tr>
    <tr class="collapse acm-notimplemented">
      <td>DescribeInstanceEventNotificationAttributes</td>
       <td style="text-align:right">-</td>
    </tr>
    <tr class="collapse acm-notimplemented">
      <td>DescribeInstanceEventWindows</td>
       <td style="text-align:right">-</td>
    </tr>
    <tr class="collapse acm-notimplemented">
      <td>DescribeIpamPools</td>
       <td style="text-align:right">-</td>
    </tr>
    <tr class="collapse acm-notimplemented">
      <td>DescribeIpamScopes</td>
       <td style="text-align:right">-</td>
    </tr>
    <tr class="collapse acm-notimplemented">
      <td>DescribeIpams</td>
       <td style="text-align:right">-</td>
    </tr>
    <tr class="collapse acm-notimplemented">
      <td>DescribeIpv6Pools</td>
       <td style="text-align:right">-</td>
    </tr>
    <tr class="collapse acm-notimplemented">
      <td>DescribeLocalGatewayRouteTableVirtualInterfaceGroupAssociations</td>
       <td style="text-align:right">-</td>
    </tr>
    <tr class="collapse acm-notimplemented">
      <td>DescribeLocalGatewayRouteTableVpcAssociations</td>
       <td style="text-align:right">-</td>
    </tr>
    <tr class="collapse acm-notimplemented">
      <td>DescribeLocalGatewayRouteTables</td>
       <td style="text-align:right">-</td>
    </tr>
    <tr class="collapse acm-notimplemented">
      <td>DescribeLocalGatewayVirtualInterfaceGroups</td>
       <td style="text-align:right">-</td>
    </tr>
    <tr class="collapse acm-notimplemented">
      <td>DescribeLocalGatewayVirtualInterfaces</td>
       <td style="text-align:right">-</td>
    </tr>
    <tr class="collapse acm-notimplemented">
      <td>DescribeLocalGateways</td>
       <td style="text-align:right">-</td>
    </tr>
    <tr class="collapse acm-notimplemented">
      <td>DescribeMovingAddresses</td>
       <td style="text-align:right">-</td>
    </tr>
    <tr class="collapse acm-notimplemented">
      <td>DescribeNetworkInsightsAccessScopeAnalyses</td>
       <td style="text-align:right">-</td>
    </tr>
    <tr class="collapse acm-notimplemented">
      <td>DescribeNetworkInsightsAccessScopes</td>
       <td style="text-align:right">-</td>
    </tr>
    <tr class="collapse acm-notimplemented">
      <td>DescribeNetworkInsightsAnalyses</td>
       <td style="text-align:right">-</td>
    </tr>
    <tr class="collapse acm-notimplemented">
      <td>DescribeNetworkInsightsPaths</td>
       <td style="text-align:right">-</td>
    </tr>
    <tr class="collapse acm-notimplemented">
      <td>DescribeNetworkInterfacePermissions</td>
       <td style="text-align:right">-</td>
    </tr>
    <tr class="collapse acm-notimplemented">
      <td>DescribePlacementGroups</td>
       <td style="text-align:right">-</td>
    </tr>
    <tr class="collapse acm-notimplemented">
      <td>DescribePrincipalIdFormat</td>
       <td style="text-align:right">-</td>
    </tr>
    <tr class="collapse acm-notimplemented">
      <td>DescribePublicIpv4Pools</td>
       <td style="text-align:right">-</td>
    </tr>
    <tr class="collapse acm-notimplemented">
      <td>DescribeReplaceRootVolumeTasks</td>
       <td style="text-align:right">-</td>
    </tr>
    <tr class="collapse acm-notimplemented">
      <td>DescribeReservedInstancesListings</td>
       <td style="text-align:right">-</td>
    </tr>
    <tr class="collapse acm-notimplemented">
      <td>DescribeReservedInstancesModifications</td>
       <td style="text-align:right">-</td>
    </tr>
    <tr class="collapse acm-notimplemented">
      <td>DescribeScheduledInstanceAvailability</td>
       <td style="text-align:right">-</td>
    </tr>
    <tr class="collapse acm-notimplemented">
      <td>DescribeScheduledInstances</td>
       <td style="text-align:right">-</td>
    </tr>
    <tr class="collapse acm-notimplemented">
      <td>DescribeSecurityGroupReferences</td>
       <td style="text-align:right">-</td>
    </tr>
    <tr class="collapse acm-notimplemented">
      <td>DescribeSecurityGroupRules</td>
       <td style="text-align:right">-</td>
    </tr>
    <tr class="collapse acm-notimplemented">
      <td>DescribeSnapshotTierStatus</td>
       <td style="text-align:right">-</td>
    </tr>
    <tr class="collapse acm-notimplemented">
      <td>DescribeSpotDatafeedSubscription</td>
       <td style="text-align:right">-</td>
    </tr>
    <tr class="collapse acm-notimplemented">
      <td>DescribeSpotFleetRequestHistory</td>
       <td style="text-align:right">-</td>
    </tr>
    <tr class="collapse acm-notimplemented">
      <td>DescribeStaleSecurityGroups</td>
       <td style="text-align:right">-</td>
    </tr>
    <tr class="collapse acm-notimplemented">
      <td>DescribeStoreImageTasks</td>
       <td style="text-align:right">-</td>
    </tr>
    <tr class="collapse acm-notimplemented">
      <td>DescribeTrafficMirrorFilters</td>
       <td style="text-align:right">-</td>
    </tr>
    <tr class="collapse acm-notimplemented">
      <td>DescribeTrafficMirrorSessions</td>
       <td style="text-align:right">-</td>
    </tr>
    <tr class="collapse acm-notimplemented">
      <td>DescribeTrafficMirrorTargets</td>
       <td style="text-align:right">-</td>
    </tr>
    <tr class="collapse acm-notimplemented">
      <td>DescribeTransitGatewayConnectPeers</td>
       <td style="text-align:right">-</td>
    </tr>
    <tr class="collapse acm-notimplemented">
      <td>DescribeTransitGatewayConnects</td>
       <td style="text-align:right">-</td>
    </tr>
    <tr class="collapse acm-notimplemented">
      <td>DescribeTransitGatewayMulticastDomains</td>
       <td style="text-align:right">-</td>
    </tr>
    <tr class="collapse acm-notimplemented">
      <td>DescribeTrunkInterfaceAssociations</td>
       <td style="text-align:right">-</td>
    </tr>
    <tr class="collapse acm-notimplemented">
      <td>DescribeVolumeAttribute</td>
       <td style="text-align:right">-</td>
    </tr>
    <tr class="collapse acm-notimplemented">
      <td>DescribeVolumeStatus</td>
       <td style="text-align:right">-</td>
    </tr>
    <tr class="collapse acm-notimplemented">
      <td>DescribeVolumesModifications</td>
       <td style="text-align:right">-</td>
    </tr>
    <tr class="collapse acm-notimplemented">
      <td>DescribeVpcEndpointConnectionNotifications</td>
       <td style="text-align:right">-</td>
    </tr>
    <tr class="collapse acm-notimplemented">
      <td>DescribeVpcEndpointConnections</td>
       <td style="text-align:right">-</td>
    </tr>
    <tr class="collapse acm-notimplemented">
      <td>DetachClassicLinkVpc</td>
       <td style="text-align:right">-</td>
    </tr>
    <tr class="collapse acm-notimplemented">
      <td>DisableFastLaunch</td>
       <td style="text-align:right">-</td>
    </tr>
    <tr class="collapse acm-notimplemented">
      <td>DisableFastSnapshotRestores</td>
       <td style="text-align:right">-</td>
    </tr>
    <tr class="collapse acm-notimplemented">
      <td>DisableImageDeprecation</td>
       <td style="text-align:right">-</td>
    </tr>
    <tr class="collapse acm-notimplemented">
      <td>DisableIpamOrganizationAdminAccount</td>
       <td style="text-align:right">-</td>
    </tr>
    <tr class="collapse acm-notimplemented">
      <td>DisableSerialConsoleAccess</td>
       <td style="text-align:right">-</td>
    </tr>
    <tr class="collapse acm-notimplemented">
      <td>DisableVgwRoutePropagation</td>
       <td style="text-align:right">-</td>
    </tr>
    <tr class="collapse acm-notimplemented">
      <td>DisassociateClientVpnTargetNetwork</td>
       <td style="text-align:right">-</td>
    </tr>
    <tr class="collapse acm-notimplemented">
      <td>DisassociateEnclaveCertificateIamRole</td>
       <td style="text-align:right">-</td>
    </tr>
    <tr class="collapse acm-notimplemented">
      <td>DisassociateInstanceEventWindow</td>
       <td style="text-align:right">-</td>
    </tr>
    <tr class="collapse acm-notimplemented">
      <td>DisassociateTransitGatewayMulticastDomain</td>
       <td style="text-align:right">-</td>
    </tr>
    <tr class="collapse acm-notimplemented">
      <td>DisassociateTrunkInterface</td>
       <td style="text-align:right">-</td>
    </tr>
    <tr class="collapse acm-notimplemented">
      <td>EnableFastLaunch</td>
       <td style="text-align:right">-</td>
    </tr>
    <tr class="collapse acm-notimplemented">
      <td>EnableFastSnapshotRestores</td>
       <td style="text-align:right">-</td>
    </tr>
    <tr class="collapse acm-notimplemented">
      <td>EnableImageDeprecation</td>
       <td style="text-align:right">-</td>
    </tr>
    <tr class="collapse acm-notimplemented">
      <td>EnableIpamOrganizationAdminAccount</td>
       <td style="text-align:right">-</td>
    </tr>
    <tr class="collapse acm-notimplemented">
      <td>EnableSerialConsoleAccess</td>
       <td style="text-align:right">-</td>
    </tr>
    <tr class="collapse acm-notimplemented">
      <td>EnableVgwRoutePropagation</td>
       <td style="text-align:right">-</td>
    </tr>
    <tr class="collapse acm-notimplemented">
      <td>ExportClientVpnClientCertificateRevocationList</td>
       <td style="text-align:right">-</td>
    </tr>
    <tr class="collapse acm-notimplemented">
      <td>ExportClientVpnClientConfiguration</td>
       <td style="text-align:right">-</td>
    </tr>
    <tr class="collapse acm-notimplemented">
      <td>ExportImage</td>
       <td style="text-align:right">-</td>
    </tr>
    <tr class="collapse acm-notimplemented">
      <td>ExportTransitGatewayRoutes</td>
       <td style="text-align:right">-</td>
    </tr>
    <tr class="collapse acm-notimplemented">
      <td>GetAssociatedEnclaveCertificateIamRoles</td>
       <td style="text-align:right">-</td>
    </tr>
    <tr class="collapse acm-notimplemented">
      <td>GetAssociatedIpv6PoolCidrs</td>
       <td style="text-align:right">-</td>
    </tr>
    <tr class="collapse acm-notimplemented">
      <td>GetCapacityReservationUsage</td>
       <td style="text-align:right">-</td>
    </tr>
    <tr class="collapse acm-notimplemented">
      <td>GetCoipPoolUsage</td>
       <td style="text-align:right">-</td>
    </tr>
    <tr class="collapse acm-notimplemented">
      <td>GetConsoleScreenshot</td>
       <td style="text-align:right">-</td>
    </tr>
    <tr class="collapse acm-notimplemented">
      <td>GetDefaultCreditSpecification</td>
       <td style="text-align:right">-</td>
    </tr>
    <tr class="collapse acm-notimplemented">
      <td>GetEbsDefaultKmsKeyId</td>
       <td style="text-align:right">-</td>
    </tr>
    <tr class="collapse acm-notimplemented">
      <td>GetFlowLogsIntegrationTemplate</td>
       <td style="text-align:right">-</td>
    </tr>
    <tr class="collapse acm-notimplemented">
      <td>GetGroupsForCapacityReservation</td>
       <td style="text-align:right">-</td>
    </tr>
    <tr class="collapse acm-notimplemented">
      <td>GetHostReservationPurchasePreview</td>
       <td style="text-align:right">-</td>
    </tr>
    <tr class="collapse acm-notimplemented">
      <td>GetInstanceTypesFromInstanceRequirements</td>
       <td style="text-align:right">-</td>
    </tr>
    <tr class="collapse acm-notimplemented">
      <td>GetInstanceUefiData</td>
       <td style="text-align:right">-</td>
    </tr>
    <tr class="collapse acm-notimplemented">
      <td>GetIpamAddressHistory</td>
       <td style="text-align:right">-</td>
    </tr>
    <tr class="collapse acm-notimplemented">
      <td>GetIpamPoolAllocations</td>
       <td style="text-align:right">-</td>
    </tr>
    <tr class="collapse acm-notimplemented">
      <td>GetIpamPoolCidrs</td>
       <td style="text-align:right">-</td>
    </tr>
    <tr class="collapse acm-notimplemented">
      <td>GetIpamResourceCidrs</td>
       <td style="text-align:right">-</td>
    </tr>
    <tr class="collapse acm-notimplemented">
      <td>GetLaunchTemplateData</td>
       <td style="text-align:right">-</td>
    </tr>
    <tr class="collapse acm-notimplemented">
      <td>GetManagedPrefixListAssociations</td>
       <td style="text-align:right">-</td>
    </tr>
    <tr class="collapse acm-notimplemented">
      <td>GetNetworkInsightsAccessScopeAnalysisFindings</td>
       <td style="text-align:right">-</td>
    </tr>
    <tr class="collapse acm-notimplemented">
      <td>GetNetworkInsightsAccessScopeContent</td>
       <td style="text-align:right">-</td>
    </tr>
    <tr class="collapse acm-notimplemented">
      <td>GetPasswordData</td>
       <td style="text-align:right">-</td>
    </tr>
    <tr class="collapse acm-notimplemented">
      <td>GetReservedInstancesExchangeQuote</td>
       <td style="text-align:right">-</td>
    </tr>
    <tr class="collapse acm-notimplemented">
      <td>GetSerialConsoleAccessStatus</td>
       <td style="text-align:right">-</td>
    </tr>
    <tr class="collapse acm-notimplemented">
      <td>GetSpotPlacementScores</td>
       <td style="text-align:right">-</td>
    </tr>
    <tr class="collapse acm-notimplemented">
      <td>GetSubnetCidrReservations</td>
       <td style="text-align:right">-</td>
    </tr>
    <tr class="collapse acm-notimplemented">
      <td>GetTransitGatewayAttachmentPropagations</td>
       <td style="text-align:right">-</td>
    </tr>
    <tr class="collapse acm-notimplemented">
      <td>GetTransitGatewayMulticastDomainAssociations</td>
       <td style="text-align:right">-</td>
    </tr>
    <tr class="collapse acm-notimplemented">
      <td>GetTransitGatewayPrefixListReferences</td>
       <td style="text-align:right">-</td>
    </tr>
    <tr class="collapse acm-notimplemented">
      <td>GetVpnConnectionDeviceSampleConfiguration</td>
       <td style="text-align:right">-</td>
    </tr>
    <tr class="collapse acm-notimplemented">
      <td>GetVpnConnectionDeviceTypes</td>
       <td style="text-align:right">-</td>
    </tr>
    <tr class="collapse acm-notimplemented">
      <td>ImportClientVpnClientCertificateRevocationList</td>
       <td style="text-align:right">-</td>
    </tr>
    <tr class="collapse acm-notimplemented">
      <td>ImportImage</td>
       <td style="text-align:right">-</td>
    </tr>
    <tr class="collapse acm-notimplemented">
      <td>ImportInstance</td>
       <td style="text-align:right">-</td>
    </tr>
    <tr class="collapse acm-notimplemented">
      <td>ImportSnapshot</td>
       <td style="text-align:right">-</td>
    </tr>
    <tr class="collapse acm-notimplemented">
      <td>ListImagesInRecycleBin</td>
       <td style="text-align:right">-</td>
    </tr>
    <tr class="collapse acm-notimplemented">
      <td>ListSnapshotsInRecycleBin</td>
       <td style="text-align:right">-</td>
    </tr>
    <tr class="collapse acm-notimplemented">
      <td>ModifyAddressAttribute</td>
       <td style="text-align:right">-</td>
    </tr>
    <tr class="collapse acm-notimplemented">
      <td>ModifyAvailabilityZoneGroup</td>
       <td style="text-align:right">-</td>
    </tr>
    <tr class="collapse acm-notimplemented">
      <td>ModifyCapacityReservation</td>
       <td style="text-align:right">-</td>
    </tr>
    <tr class="collapse acm-notimplemented">
      <td>ModifyCapacityReservationFleet</td>
       <td style="text-align:right">-</td>
    </tr>
    <tr class="collapse acm-notimplemented">
      <td>ModifyClientVpnEndpoint</td>
       <td style="text-align:right">-</td>
    </tr>
    <tr class="collapse acm-notimplemented">
      <td>ModifyDefaultCreditSpecification</td>
       <td style="text-align:right">-</td>
    </tr>
    <tr class="collapse acm-notimplemented">
      <td>ModifyEbsDefaultKmsKeyId</td>
       <td style="text-align:right">-</td>
    </tr>
    <tr class="collapse acm-notimplemented">
      <td>ModifyFleet</td>
       <td style="text-align:right">-</td>
    </tr>
    <tr class="collapse acm-notimplemented">
      <td>ModifyFpgaImageAttribute</td>
       <td style="text-align:right">-</td>
    </tr>
    <tr class="collapse acm-notimplemented">
      <td>ModifyHosts</td>
       <td style="text-align:right">-</td>
    </tr>
    <tr class="collapse acm-notimplemented">
      <td>ModifyIdFormat</td>
       <td style="text-align:right">-</td>
    </tr>
    <tr class="collapse acm-notimplemented">
      <td>ModifyIdentityIdFormat</td>
       <td style="text-align:right">-</td>
    </tr>
    <tr class="collapse acm-notimplemented">
      <td>ModifyInstanceCapacityReservationAttributes</td>
       <td style="text-align:right">-</td>
    </tr>
    <tr class="collapse acm-notimplemented">
      <td>ModifyInstanceCreditSpecification</td>
       <td style="text-align:right">-</td>
    </tr>
    <tr class="collapse acm-notimplemented">
      <td>ModifyInstanceEventStartTime</td>
       <td style="text-align:right">-</td>
    </tr>
    <tr class="collapse acm-notimplemented">
      <td>ModifyInstanceEventWindow</td>
       <td style="text-align:right">-</td>
    </tr>
    <tr class="collapse acm-notimplemented">
      <td>ModifyInstanceMaintenanceOptions</td>
       <td style="text-align:right">-</td>
    </tr>
    <tr class="collapse acm-notimplemented">
      <td>ModifyInstanceMetadataOptions</td>
       <td style="text-align:right">-</td>
    </tr>
    <tr class="collapse acm-notimplemented">
      <td>ModifyInstancePlacement</td>
       <td style="text-align:right">-</td>
    </tr>
    <tr class="collapse acm-notimplemented">
      <td>ModifyIpam</td>
       <td style="text-align:right">-</td>
    </tr>
    <tr class="collapse acm-notimplemented">
      <td>ModifyIpamPool</td>
       <td style="text-align:right">-</td>
    </tr>
    <tr class="collapse acm-notimplemented">
      <td>ModifyIpamResourceCidr</td>
       <td style="text-align:right">-</td>
    </tr>
    <tr class="collapse acm-notimplemented">
      <td>ModifyIpamScope</td>
       <td style="text-align:right">-</td>
    </tr>
    <tr class="collapse acm-notimplemented">
      <td>ModifyLaunchTemplate</td>
       <td style="text-align:right">-</td>
    </tr>
    <tr class="collapse acm-notimplemented">
      <td>ModifyPrivateDnsNameOptions</td>
       <td style="text-align:right">-</td>
    </tr>
    <tr class="collapse acm-notimplemented">
      <td>ModifyReservedInstances</td>
       <td style="text-align:right">-</td>
    </tr>
    <tr class="collapse acm-notimplemented">
      <td>ModifySecurityGroupRules</td>
       <td style="text-align:right">-</td>
    </tr>
    <tr class="collapse acm-notimplemented">
      <td>ModifySnapshotTier</td>
       <td style="text-align:right">-</td>
    </tr>
    <tr class="collapse acm-notimplemented">
      <td>ModifyTrafficMirrorFilterNetworkServices</td>
       <td style="text-align:right">-</td>
    </tr>
    <tr class="collapse acm-notimplemented">
      <td>ModifyTrafficMirrorFilterRule</td>
       <td style="text-align:right">-</td>
    </tr>
    <tr class="collapse acm-notimplemented">
      <td>ModifyTrafficMirrorSession</td>
       <td style="text-align:right">-</td>
    </tr>
    <tr class="collapse acm-notimplemented">
      <td>ModifyTransitGatewayPrefixListReference</td>
       <td style="text-align:right">-</td>
    </tr>
    <tr class="collapse acm-notimplemented">
      <td>ModifyVolume</td>
       <td style="text-align:right">-</td>
    </tr>
    <tr class="collapse acm-notimplemented">
      <td>ModifyVpcEndpointConnectionNotification</td>
       <td style="text-align:right">-</td>
    </tr>
    <tr class="collapse acm-notimplemented">
      <td>ModifyVpcEndpointServicePayerResponsibility</td>
       <td style="text-align:right">-</td>
    </tr>
    <tr class="collapse acm-notimplemented">
      <td>ModifyVpnConnection</td>
       <td style="text-align:right">-</td>
    </tr>
    <tr class="collapse acm-notimplemented">
      <td>ModifyVpnConnectionOptions</td>
       <td style="text-align:right">-</td>
    </tr>
    <tr class="collapse acm-notimplemented">
      <td>ModifyVpnTunnelCertificate</td>
       <td style="text-align:right">-</td>
    </tr>
    <tr class="collapse acm-notimplemented">
      <td>ModifyVpnTunnelOptions</td>
       <td style="text-align:right">-</td>
    </tr>
    <tr class="collapse acm-notimplemented">
      <td>MoveAddressToVpc</td>
       <td style="text-align:right">-</td>
    </tr>
    <tr class="collapse acm-notimplemented">
      <td>MoveByoipCidrToIpam</td>
       <td style="text-align:right">-</td>
    </tr>
    <tr class="collapse acm-notimplemented">
      <td>ProvisionByoipCidr</td>
       <td style="text-align:right">-</td>
    </tr>
    <tr class="collapse acm-notimplemented">
      <td>ProvisionIpamPoolCidr</td>
       <td style="text-align:right">-</td>
    </tr>
    <tr class="collapse acm-notimplemented">
      <td>ProvisionPublicIpv4PoolCidr</td>
       <td style="text-align:right">-</td>
    </tr>
    <tr class="collapse acm-notimplemented">
      <td>PurchaseHostReservation</td>
       <td style="text-align:right">-</td>
    </tr>
    <tr class="collapse acm-notimplemented">
      <td>PurchaseScheduledInstances</td>
       <td style="text-align:right">-</td>
    </tr>
    <tr class="collapse acm-notimplemented">
      <td>RegisterInstanceEventNotificationAttributes</td>
       <td style="text-align:right">-</td>
    </tr>
    <tr class="collapse acm-notimplemented">
      <td>RegisterTransitGatewayMulticastGroupMembers</td>
       <td style="text-align:right">-</td>
    </tr>
    <tr class="collapse acm-notimplemented">
      <td>RegisterTransitGatewayMulticastGroupSources</td>
       <td style="text-align:right">-</td>
    </tr>
    <tr class="collapse acm-notimplemented">
      <td>RejectTransitGatewayMulticastDomainAssociations</td>
       <td style="text-align:right">-</td>
    </tr>
    <tr class="collapse acm-notimplemented">
      <td>RejectTransitGatewayVpcAttachment</td>
       <td style="text-align:right">-</td>
    </tr>
    <tr class="collapse acm-notimplemented">
      <td>RejectVpcEndpointConnections</td>
       <td style="text-align:right">-</td>
    </tr>
    <tr class="collapse acm-notimplemented">
      <td>ReleaseHosts</td>
       <td style="text-align:right">-</td>
    </tr>
    <tr class="collapse acm-notimplemented">
      <td>ReleaseIpamPoolAllocation</td>
       <td style="text-align:right">-</td>
    </tr>
    <tr class="collapse acm-notimplemented">
      <td>ReplaceTransitGatewayRoute</td>
       <td style="text-align:right">-</td>
    </tr>
    <tr class="collapse acm-notimplemented">
      <td>ReportInstanceStatus</td>
       <td style="text-align:right">-</td>
    </tr>
    <tr class="collapse acm-notimplemented">
      <td>ResetAddressAttribute</td>
       <td style="text-align:right">-</td>
    </tr>
    <tr class="collapse acm-notimplemented">
      <td>ResetEbsDefaultKmsKeyId</td>
       <td style="text-align:right">-</td>
    </tr>
    <tr class="collapse acm-notimplemented">
      <td>ResetFpgaImageAttribute</td>
       <td style="text-align:right">-</td>
    </tr>
    <tr class="collapse acm-notimplemented">
      <td>ResetInstanceAttribute</td>
       <td style="text-align:right">-</td>
    </tr>
    <tr class="collapse acm-notimplemented">
      <td>RestoreAddressToClassic</td>
       <td style="text-align:right">-</td>
    </tr>
    <tr class="collapse acm-notimplemented">
      <td>RestoreImageFromRecycleBin</td>
       <td style="text-align:right">-</td>
    </tr>
    <tr class="collapse acm-notimplemented">
      <td>RestoreManagedPrefixListVersion</td>
       <td style="text-align:right">-</td>
    </tr>
    <tr class="collapse acm-notimplemented">
      <td>RestoreSnapshotFromRecycleBin</td>
       <td style="text-align:right">-</td>
    </tr>
    <tr class="collapse acm-notimplemented">
      <td>RestoreSnapshotTier</td>
       <td style="text-align:right">-</td>
    </tr>
    <tr class="collapse acm-notimplemented">
      <td>RevokeClientVpnIngress</td>
       <td style="text-align:right">-</td>
    </tr>
    <tr class="collapse acm-notimplemented">
      <td>RunScheduledInstances</td>
       <td style="text-align:right">-</td>
    </tr>
    <tr class="collapse acm-notimplemented">
      <td>SearchLocalGatewayRoutes</td>
       <td style="text-align:right">-</td>
    </tr>
    <tr class="collapse acm-notimplemented">
      <td>SearchTransitGatewayMulticastGroups</td>
       <td style="text-align:right">-</td>
    </tr>
    <tr class="collapse acm-notimplemented">
      <td>SendDiagnosticInterrupt</td>
       <td style="text-align:right">-</td>
    </tr>
    <tr class="collapse acm-notimplemented">
      <td>StartNetworkInsightsAccessScopeAnalysis</td>
       <td style="text-align:right">-</td>
    </tr>
    <tr class="collapse acm-notimplemented">
      <td>StartNetworkInsightsAnalysis</td>
       <td style="text-align:right">-</td>
    </tr>
    <tr class="collapse acm-notimplemented">
      <td>StartVpcEndpointServicePrivateDnsVerification</td>
       <td style="text-align:right">-</td>
    </tr>
    <tr class="collapse acm-notimplemented">
      <td>TerminateClientVpnConnections</td>
       <td style="text-align:right">-</td>
    </tr>
    <tr class="collapse acm-notimplemented">
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
      <td>BatchDeleteImage <a href="#misc" title="covered by our integration test suite">✨</a></td>
       <td style="text-align:right">✅</td>
    </tr>
    <tr>
      <td>BatchGetImage <a href="#misc" title="covered by our integration test suite">✨</a></td>
       <td style="text-align:right">✅</td>
    </tr>
    <tr>
      <td>CreateRepository <a href="#misc" title="covered by our integration test suite">✨</a></td>
       <td style="text-align:right">✅</td>
    </tr>
    <tr>
      <td>DeleteLifecyclePolicy <a href="#misc" title="covered by our integration test suite">✨</a></td>
       <td style="text-align:right">✅</td>
    </tr>
    <tr>
      <td>DeleteRegistryPolicy</td>
       <td style="text-align:right">✅</td>
    </tr>
    <tr>
      <td>DeleteRepository <a href="#misc" title="covered by our integration test suite">✨</a></td>
       <td style="text-align:right">✅</td>
    </tr>
    <tr>
      <td>DeleteRepositoryPolicy</td>
       <td style="text-align:right">✅</td>
    </tr>
    <tr>
      <td>DescribeImageScanFindings</td>
       <td style="text-align:right">✅</td>
    </tr>
    <tr>
      <td>DescribeImages <a href="#misc" title="covered by our integration test suite">✨</a></td>
       <td style="text-align:right">✅</td>
    </tr>
    <tr>
      <td>DescribeRegistry</td>
       <td style="text-align:right">✅</td>
    </tr>
    <tr>
      <td>DescribeRepositories <a href="#misc" title="covered by our integration test suite">✨</a></td>
       <td style="text-align:right">✅</td>
    </tr>
    <tr>
      <td>GetAuthorizationToken <a href="#misc" title="covered by our integration test suite">✨</a></td>
       <td style="text-align:right">✅</td>
    </tr>
    <tr>
      <td>GetLifecyclePolicy <a href="#misc" title="covered by our integration test suite">✨</a></td>
       <td style="text-align:right">✅</td>
    </tr>
    <tr>
      <td>GetLifecyclePolicyPreview</td>
       <td style="text-align:right">✅</td>
    </tr>
    <tr>
      <td>GetRegistryPolicy</td>
       <td style="text-align:right">✅</td>
    </tr>
    <tr>
      <td>GetRepositoryPolicy</td>
       <td style="text-align:right">✅</td>
    </tr>
    <tr>
      <td>ListImages <a href="#misc" title="covered by our integration test suite">✨</a></td>
       <td style="text-align:right">✅</td>
    </tr>
    <tr>
      <td>ListTagsForResource <a href="#misc" title="covered by our integration test suite">✨</a></td>
       <td style="text-align:right">✅</td>
    </tr>
    <tr>
      <td>PutImage</td>
       <td style="text-align:right">✅</td>
    </tr>
    <tr>
      <td>PutImageScanningConfiguration</td>
       <td style="text-align:right">✅</td>
    </tr>
    <tr>
      <td>PutImageTagMutability <a href="#misc" title="covered by our integration test suite">✨</a></td>
       <td style="text-align:right">✅</td>
    </tr>
    <tr>
      <td>PutLifecyclePolicy <a href="#misc" title="covered by our integration test suite">✨</a></td>
       <td style="text-align:right">✅</td>
    </tr>
    <tr>
      <td>PutRegistryPolicy</td>
       <td style="text-align:right">✅</td>
    </tr>
    <tr>
      <td>PutReplicationConfiguration</td>
       <td style="text-align:right">✅</td>
    </tr>
    <tr>
      <td>SetRepositoryPolicy</td>
       <td style="text-align:right">✅</td>
    </tr>
    <tr>
      <td>StartImageScan</td>
       <td style="text-align:right">✅</td>
    </tr>
    <tr>
      <td>StartLifecyclePolicyPreview</td>
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
      <td><a data-toggle="collapse" href=".acm-notimplemented">Show more</a></td>
      <td style="text-align:right"></td>
    </tr>
    <tr class="collapse acm-notimplemented">
      <td>BatchCheckLayerAvailability</td>
       <td style="text-align:right">-</td>
    </tr>
    <tr class="collapse acm-notimplemented">
      <td>BatchGetRepositoryScanningConfiguration</td>
       <td style="text-align:right">-</td>
    </tr>
    <tr class="collapse acm-notimplemented">
      <td>CompleteLayerUpload</td>
       <td style="text-align:right">-</td>
    </tr>
    <tr class="collapse acm-notimplemented">
      <td>CreatePullThroughCacheRule</td>
       <td style="text-align:right">-</td>
    </tr>
    <tr class="collapse acm-notimplemented">
      <td>DeletePullThroughCacheRule</td>
       <td style="text-align:right">-</td>
    </tr>
    <tr class="collapse acm-notimplemented">
      <td>DescribeImageReplicationStatus</td>
       <td style="text-align:right">-</td>
    </tr>
    <tr class="collapse acm-notimplemented">
      <td>DescribePullThroughCacheRules</td>
       <td style="text-align:right">-</td>
    </tr>
    <tr class="collapse acm-notimplemented">
      <td>GetDownloadUrlForLayer</td>
       <td style="text-align:right">-</td>
    </tr>
    <tr class="collapse acm-notimplemented">
      <td>GetRegistryScanningConfiguration</td>
       <td style="text-align:right">-</td>
    </tr>
    <tr class="collapse acm-notimplemented">
      <td>InitiateLayerUpload</td>
       <td style="text-align:right">-</td>
    </tr>
    <tr class="collapse acm-notimplemented">
      <td>PutRegistryScanningConfiguration</td>
       <td style="text-align:right">-</td>
    </tr>
    <tr class="collapse acm-notimplemented">
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
      <td>CreateCapacityProvider</td>
       <td style="text-align:right">✅</td>
    </tr>
    <tr>
      <td>CreateCluster <a href="#misc" title="covered by our integration test suite">✨</a></td>
       <td style="text-align:right">✅</td>
    </tr>
    <tr>
      <td>CreateService <a href="#misc" title="covered by our integration test suite">✨</a></td>
       <td style="text-align:right">✅</td>
    </tr>
    <tr>
      <td>CreateTaskSet <a href="#misc" title="covered by our integration test suite">✨</a></td>
       <td style="text-align:right">✅</td>
    </tr>
    <tr>
      <td>DeleteAccountSetting</td>
       <td style="text-align:right">✅</td>
    </tr>
    <tr>
      <td>DeleteAttributes</td>
       <td style="text-align:right">✅</td>
    </tr>
    <tr>
      <td>DeleteCapacityProvider</td>
       <td style="text-align:right">✅</td>
    </tr>
    <tr>
      <td>DeleteCluster <a href="#misc" title="covered by our integration test suite">✨</a></td>
       <td style="text-align:right">✅</td>
    </tr>
    <tr>
      <td>DeleteService <a href="#misc" title="covered by our integration test suite">✨</a></td>
       <td style="text-align:right">✅</td>
    </tr>
    <tr>
      <td>DeleteTaskSet</td>
       <td style="text-align:right">✅</td>
    </tr>
    <tr>
      <td>DeregisterContainerInstance</td>
       <td style="text-align:right">✅</td>
    </tr>
    <tr>
      <td>DeregisterTaskDefinition <a href="#misc" title="covered by our integration test suite">✨</a></td>
       <td style="text-align:right">✅</td>
    </tr>
    <tr>
      <td>DescribeCapacityProviders</td>
       <td style="text-align:right">✅</td>
    </tr>
    <tr>
      <td>DescribeClusters <a href="#misc" title="covered by our integration test suite">✨</a></td>
       <td style="text-align:right">✅</td>
    </tr>
    <tr>
      <td>DescribeContainerInstances</td>
       <td style="text-align:right">✅</td>
    </tr>
    <tr>
      <td>DescribeServices <a href="#misc" title="covered by our integration test suite">✨</a></td>
       <td style="text-align:right">✅</td>
    </tr>
    <tr>
      <td>DescribeTaskDefinition <a href="#misc" title="covered by our integration test suite">✨</a></td>
       <td style="text-align:right">✅</td>
    </tr>
    <tr>
      <td>DescribeTaskSets</td>
       <td style="text-align:right">✅</td>
    </tr>
    <tr>
      <td>DescribeTasks <a href="#misc" title="covered by our integration test suite">✨</a></td>
       <td style="text-align:right">✅</td>
    </tr>
    <tr>
      <td>DiscoverPollEndpoint</td>
       <td style="text-align:right">✅</td>
    </tr>
    <tr>
      <td>ListAccountSettings</td>
       <td style="text-align:right">✅</td>
    </tr>
    <tr>
      <td>ListAttributes</td>
       <td style="text-align:right">✅</td>
    </tr>
    <tr>
      <td>ListClusters <a href="#misc" title="covered by our integration test suite">✨</a></td>
       <td style="text-align:right">✅</td>
    </tr>
    <tr>
      <td>ListContainerInstances</td>
       <td style="text-align:right">✅</td>
    </tr>
    <tr>
      <td>ListServices</td>
       <td style="text-align:right">✅</td>
    </tr>
    <tr>
      <td>ListTagsForResource</td>
       <td style="text-align:right">✅</td>
    </tr>
    <tr>
      <td>ListTaskDefinitionFamilies</td>
       <td style="text-align:right">✅</td>
    </tr>
    <tr>
      <td>ListTaskDefinitions <a href="#misc" title="covered by our integration test suite">✨</a></td>
       <td style="text-align:right">✅</td>
    </tr>
    <tr>
      <td>ListTasks <a href="#misc" title="covered by our integration test suite">✨</a></td>
       <td style="text-align:right">✅</td>
    </tr>
    <tr>
      <td>PutAccountSetting</td>
       <td style="text-align:right">✅</td>
    </tr>
    <tr>
      <td>PutAttributes</td>
       <td style="text-align:right">✅</td>
    </tr>
    <tr>
      <td>PutClusterCapacityProviders <a href="#misc" title="covered by our integration test suite">✨</a></td>
       <td style="text-align:right">✅</td>
    </tr>
    <tr>
      <td>RegisterContainerInstance</td>
       <td style="text-align:right">✅</td>
    </tr>
    <tr>
      <td>RegisterTaskDefinition <a href="#misc" title="covered by our integration test suite">✨</a></td>
       <td style="text-align:right">✅</td>
    </tr>
    <tr>
      <td>RunTask <a href="#misc" title="covered by our integration test suite">✨</a></td>
       <td style="text-align:right">✅</td>
    </tr>
    <tr>
      <td>StartTask</td>
       <td style="text-align:right">✅</td>
    </tr>
    <tr>
      <td>StopTask <a href="#misc" title="covered by our integration test suite">✨</a></td>
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
      <td>UpdateCluster <a href="#misc" title="covered by our integration test suite">✨</a></td>
       <td style="text-align:right">✅</td>
    </tr>
    <tr>
      <td>UpdateContainerInstancesState</td>
       <td style="text-align:right">✅</td>
    </tr>
    <tr>
      <td>UpdateService</td>
       <td style="text-align:right">✅</td>
    </tr>
    <tr>
      <td>UpdateServicePrimaryTaskSet</td>
       <td style="text-align:right">✅</td>
    </tr>
    <tr>
      <td>UpdateTaskSet</td>
       <td style="text-align:right">✅</td>
    </tr>
    <tr>
      <td><a data-toggle="collapse" href=".acm-notimplemented">Show more</a></td>
      <td style="text-align:right"></td>
    </tr>
    <tr class="collapse acm-notimplemented">
      <td>ExecuteCommand</td>
       <td style="text-align:right">-</td>
    </tr>
    <tr class="collapse acm-notimplemented">
      <td>PutAccountSettingDefault</td>
       <td style="text-align:right">-</td>
    </tr>
    <tr class="collapse acm-notimplemented">
      <td>SubmitAttachmentStateChanges</td>
       <td style="text-align:right">-</td>
    </tr>
    <tr class="collapse acm-notimplemented">
      <td>SubmitContainerStateChange</td>
       <td style="text-align:right">-</td>
    </tr>
    <tr class="collapse acm-notimplemented">
      <td>SubmitTaskStateChange</td>
       <td style="text-align:right">-</td>
    </tr>
    <tr class="collapse acm-notimplemented">
      <td>UpdateCapacityProvider</td>
       <td style="text-align:right">-</td>
    </tr>
    <tr class="collapse acm-notimplemented">
      <td>UpdateClusterSettings</td>
       <td style="text-align:right">-</td>
    </tr>
    <tr class="collapse acm-notimplemented">
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
      <td>CreateFileSystem <a href="#misc" title="covered by our integration test suite">✨</a></td>
       <td style="text-align:right">✅</td>
    </tr>
    <tr>
      <td>DeleteFileSystem <a href="#misc" title="covered by our integration test suite">✨</a></td>
       <td style="text-align:right">✅</td>
    </tr>
    <tr>
      <td>DescribeFileSystems <a href="#misc" title="covered by our integration test suite">✨</a></td>
       <td style="text-align:right">✅</td>
    </tr>
    <tr>
      <td><a data-toggle="collapse" href=".acm-notimplemented">Show more</a></td>
      <td style="text-align:right"></td>
    </tr>
    <tr class="collapse acm-notimplemented">
      <td>CreateAccessPoint</td>
       <td style="text-align:right">-</td>
    </tr>
    <tr class="collapse acm-notimplemented">
      <td>CreateMountTarget</td>
       <td style="text-align:right">-</td>
    </tr>
    <tr class="collapse acm-notimplemented">
      <td>CreateReplicationConfiguration</td>
       <td style="text-align:right">-</td>
    </tr>
    <tr class="collapse acm-notimplemented">
      <td>CreateTags</td>
       <td style="text-align:right">-</td>
    </tr>
    <tr class="collapse acm-notimplemented">
      <td>DeleteAccessPoint</td>
       <td style="text-align:right">-</td>
    </tr>
    <tr class="collapse acm-notimplemented">
      <td>DeleteFileSystemPolicy</td>
       <td style="text-align:right">-</td>
    </tr>
    <tr class="collapse acm-notimplemented">
      <td>DeleteMountTarget</td>
       <td style="text-align:right">-</td>
    </tr>
    <tr class="collapse acm-notimplemented">
      <td>DeleteReplicationConfiguration</td>
       <td style="text-align:right">-</td>
    </tr>
    <tr class="collapse acm-notimplemented">
      <td>DeleteTags</td>
       <td style="text-align:right">-</td>
    </tr>
    <tr class="collapse acm-notimplemented">
      <td>DescribeAccessPoints</td>
       <td style="text-align:right">-</td>
    </tr>
    <tr class="collapse acm-notimplemented">
      <td>DescribeAccountPreferences</td>
       <td style="text-align:right">-</td>
    </tr>
    <tr class="collapse acm-notimplemented">
      <td>DescribeBackupPolicy</td>
       <td style="text-align:right">-</td>
    </tr>
    <tr class="collapse acm-notimplemented">
      <td>DescribeFileSystemPolicy</td>
       <td style="text-align:right">-</td>
    </tr>
    <tr class="collapse acm-notimplemented">
      <td>DescribeLifecycleConfiguration</td>
       <td style="text-align:right">-</td>
    </tr>
    <tr class="collapse acm-notimplemented">
      <td>DescribeMountTargetSecurityGroups</td>
       <td style="text-align:right">-</td>
    </tr>
    <tr class="collapse acm-notimplemented">
      <td>DescribeMountTargets</td>
       <td style="text-align:right">-</td>
    </tr>
    <tr class="collapse acm-notimplemented">
      <td>DescribeReplicationConfigurations</td>
       <td style="text-align:right">-</td>
    </tr>
    <tr class="collapse acm-notimplemented">
      <td>DescribeTags</td>
       <td style="text-align:right">-</td>
    </tr>
    <tr class="collapse acm-notimplemented">
      <td>ListTagsForResource</td>
       <td style="text-align:right">-</td>
    </tr>
    <tr class="collapse acm-notimplemented">
      <td>ModifyMountTargetSecurityGroups</td>
       <td style="text-align:right">-</td>
    </tr>
    <tr class="collapse acm-notimplemented">
      <td>PutAccountPreferences</td>
       <td style="text-align:right">-</td>
    </tr>
    <tr class="collapse acm-notimplemented">
      <td>PutBackupPolicy</td>
       <td style="text-align:right">-</td>
    </tr>
    <tr class="collapse acm-notimplemented">
      <td>PutFileSystemPolicy</td>
       <td style="text-align:right">-</td>
    </tr>
    <tr class="collapse acm-notimplemented">
      <td>PutLifecycleConfiguration</td>
       <td style="text-align:right">-</td>
    </tr>
    <tr class="collapse acm-notimplemented">
      <td>TagResource</td>
       <td style="text-align:right">-</td>
    </tr>
    <tr class="collapse acm-notimplemented">
      <td>UntagResource</td>
       <td style="text-align:right">-</td>
    </tr>
    <tr class="collapse acm-notimplemented">
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
      <td>CreateCluster <a href="#misc" title="covered by our integration test suite">✨</a></td>
       <td style="text-align:right">✅</td>
    </tr>
    <tr>
      <td>CreateFargateProfile</td>
       <td style="text-align:right">✅</td>
    </tr>
    <tr>
      <td>CreateNodegroup</td>
       <td style="text-align:right">✅</td>
    </tr>
    <tr>
      <td>DeleteCluster <a href="#misc" title="covered by our integration test suite">✨</a></td>
       <td style="text-align:right">✅</td>
    </tr>
    <tr>
      <td>DeleteFargateProfile</td>
       <td style="text-align:right">✅</td>
    </tr>
    <tr>
      <td>DeleteNodegroup</td>
       <td style="text-align:right">✅</td>
    </tr>
    <tr>
      <td>DescribeCluster <a href="#misc" title="covered by our integration test suite">✨</a></td>
       <td style="text-align:right">✅</td>
    </tr>
    <tr>
      <td>DescribeFargateProfile</td>
       <td style="text-align:right">✅</td>
    </tr>
    <tr>
      <td>DescribeNodegroup</td>
       <td style="text-align:right">✅</td>
    </tr>
    <tr>
      <td>ListClusters</td>
       <td style="text-align:right">✅</td>
    </tr>
    <tr>
      <td>ListFargateProfiles</td>
       <td style="text-align:right">✅</td>
    </tr>
    <tr>
      <td>ListNodegroups</td>
       <td style="text-align:right">✅</td>
    </tr>
    <tr>
      <td>UpdateClusterConfig</td>
       <td style="text-align:right">✅</td>
    </tr>
    <tr>
      <td>UpdateNodegroupConfig</td>
       <td style="text-align:right">✅</td>
    </tr>
    <tr>
      <td>UpdateNodegroupVersion</td>
       <td style="text-align:right">✅</td>
    </tr>
    <tr>
      <td><a data-toggle="collapse" href=".acm-notimplemented">Show more</a></td>
      <td style="text-align:right"></td>
    </tr>
    <tr class="collapse acm-notimplemented">
      <td>AssociateEncryptionConfig</td>
       <td style="text-align:right">-</td>
    </tr>
    <tr class="collapse acm-notimplemented">
      <td>AssociateIdentityProviderConfig</td>
       <td style="text-align:right">-</td>
    </tr>
    <tr class="collapse acm-notimplemented">
      <td>CreateAddon</td>
       <td style="text-align:right">-</td>
    </tr>
    <tr class="collapse acm-notimplemented">
      <td>DeleteAddon</td>
       <td style="text-align:right">-</td>
    </tr>
    <tr class="collapse acm-notimplemented">
      <td>DeregisterCluster</td>
       <td style="text-align:right">-</td>
    </tr>
    <tr class="collapse acm-notimplemented">
      <td>DescribeAddon</td>
       <td style="text-align:right">-</td>
    </tr>
    <tr class="collapse acm-notimplemented">
      <td>DescribeAddonVersions</td>
       <td style="text-align:right">-</td>
    </tr>
    <tr class="collapse acm-notimplemented">
      <td>DescribeIdentityProviderConfig</td>
       <td style="text-align:right">-</td>
    </tr>
    <tr class="collapse acm-notimplemented">
      <td>DescribeUpdate</td>
       <td style="text-align:right">-</td>
    </tr>
    <tr class="collapse acm-notimplemented">
      <td>DisassociateIdentityProviderConfig</td>
       <td style="text-align:right">-</td>
    </tr>
    <tr class="collapse acm-notimplemented">
      <td>ListAddons</td>
       <td style="text-align:right">-</td>
    </tr>
    <tr class="collapse acm-notimplemented">
      <td>ListIdentityProviderConfigs</td>
       <td style="text-align:right">-</td>
    </tr>
    <tr class="collapse acm-notimplemented">
      <td>ListTagsForResource</td>
       <td style="text-align:right">-</td>
    </tr>
    <tr class="collapse acm-notimplemented">
      <td>ListUpdates</td>
       <td style="text-align:right">-</td>
    </tr>
    <tr class="collapse acm-notimplemented">
      <td>RegisterCluster</td>
       <td style="text-align:right">-</td>
    </tr>
    <tr class="collapse acm-notimplemented">
      <td>TagResource</td>
       <td style="text-align:right">-</td>
    </tr>
    <tr class="collapse acm-notimplemented">
      <td>UntagResource</td>
       <td style="text-align:right">-</td>
    </tr>
    <tr class="collapse acm-notimplemented">
      <td>UpdateAddon</td>
       <td style="text-align:right">-</td>
    </tr>
    <tr class="collapse acm-notimplemented">
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
      <td>AddTagsToResource</td>
       <td style="text-align:right">✅</td>
    </tr>
    <tr>
      <td>CreateCacheCluster <a href="#misc" title="covered by our integration test suite">✨</a></td>
       <td style="text-align:right">✅</td>
    </tr>
    <tr>
      <td>CreateCacheParameterGroup <a href="#misc" title="covered by our integration test suite">✨</a></td>
       <td style="text-align:right">✅</td>
    </tr>
    <tr>
      <td>CreateCacheSecurityGroup <a href="#misc" title="covered by our integration test suite">✨</a></td>
       <td style="text-align:right">✅</td>
    </tr>
    <tr>
      <td>CreateCacheSubnetGroup <a href="#misc" title="covered by our integration test suite">✨</a></td>
       <td style="text-align:right">✅</td>
    </tr>
    <tr>
      <td>CreateReplicationGroup <a href="#misc" title="covered by our integration test suite">✨</a></td>
       <td style="text-align:right">✅</td>
    </tr>
    <tr>
      <td>DeleteCacheCluster <a href="#misc" title="covered by our integration test suite">✨</a></td>
       <td style="text-align:right">✅</td>
    </tr>
    <tr>
      <td>DeleteCacheParameterGroup <a href="#misc" title="covered by our integration test suite">✨</a></td>
       <td style="text-align:right">✅</td>
    </tr>
    <tr>
      <td>DeleteCacheSecurityGroup <a href="#misc" title="covered by our integration test suite">✨</a></td>
       <td style="text-align:right">✅</td>
    </tr>
    <tr>
      <td>DeleteCacheSubnetGroup <a href="#misc" title="covered by our integration test suite">✨</a></td>
       <td style="text-align:right">✅</td>
    </tr>
    <tr>
      <td>DeleteReplicationGroup <a href="#misc" title="covered by our integration test suite">✨</a></td>
       <td style="text-align:right">✅</td>
    </tr>
    <tr>
      <td>DescribeCacheClusters <a href="#misc" title="covered by our integration test suite">✨</a></td>
       <td style="text-align:right">✅</td>
    </tr>
    <tr>
      <td>DescribeCacheParameterGroups <a href="#misc" title="covered by our integration test suite">✨</a></td>
       <td style="text-align:right">✅</td>
    </tr>
    <tr>
      <td>DescribeCacheParameters <a href="#misc" title="covered by our integration test suite">✨</a></td>
       <td style="text-align:right">✅</td>
    </tr>
    <tr>
      <td>DescribeCacheSecurityGroups <a href="#misc" title="covered by our integration test suite">✨</a></td>
       <td style="text-align:right">✅</td>
    </tr>
    <tr>
      <td>DescribeCacheSubnetGroups <a href="#misc" title="covered by our integration test suite">✨</a></td>
       <td style="text-align:right">✅</td>
    </tr>
    <tr>
      <td>DescribeReplicationGroups <a href="#misc" title="covered by our integration test suite">✨</a></td>
       <td style="text-align:right">✅</td>
    </tr>
    <tr>
      <td>ListTagsForResource</td>
       <td style="text-align:right">✅</td>
    </tr>
    <tr>
      <td>ModifyCacheCluster <a href="#misc" title="covered by our integration test suite">✨</a></td>
       <td style="text-align:right">✅</td>
    </tr>
    <tr>
      <td>ModifyCacheParameterGroup <a href="#misc" title="covered by our integration test suite">✨</a></td>
       <td style="text-align:right">✅</td>
    </tr>
    <tr>
      <td>ModifyCacheSubnetGroup <a href="#misc" title="covered by our integration test suite">✨</a></td>
       <td style="text-align:right">✅</td>
    </tr>
    <tr>
      <td>ModifyReplicationGroup <a href="#misc" title="covered by our integration test suite">✨</a></td>
       <td style="text-align:right">✅</td>
    </tr>
    <tr>
      <td>RemoveTagsFromResource</td>
       <td style="text-align:right">✅</td>
    </tr>
    <tr>
      <td><a data-toggle="collapse" href=".acm-notimplemented">Show more</a></td>
      <td style="text-align:right"></td>
    </tr>
    <tr class="collapse acm-notimplemented">
      <td>AuthorizeCacheSecurityGroupIngress</td>
       <td style="text-align:right">-</td>
    </tr>
    <tr class="collapse acm-notimplemented">
      <td>BatchApplyUpdateAction</td>
       <td style="text-align:right">-</td>
    </tr>
    <tr class="collapse acm-notimplemented">
      <td>BatchStopUpdateAction</td>
       <td style="text-align:right">-</td>
    </tr>
    <tr class="collapse acm-notimplemented">
      <td>CompleteMigration</td>
       <td style="text-align:right">-</td>
    </tr>
    <tr class="collapse acm-notimplemented">
      <td>CopySnapshot</td>
       <td style="text-align:right">-</td>
    </tr>
    <tr class="collapse acm-notimplemented">
      <td>CreateGlobalReplicationGroup</td>
       <td style="text-align:right">-</td>
    </tr>
    <tr class="collapse acm-notimplemented">
      <td>CreateSnapshot</td>
       <td style="text-align:right">-</td>
    </tr>
    <tr class="collapse acm-notimplemented">
      <td>CreateUser</td>
       <td style="text-align:right">-</td>
    </tr>
    <tr class="collapse acm-notimplemented">
      <td>CreateUserGroup</td>
       <td style="text-align:right">-</td>
    </tr>
    <tr class="collapse acm-notimplemented">
      <td>DecreaseNodeGroupsInGlobalReplicationGroup</td>
       <td style="text-align:right">-</td>
    </tr>
    <tr class="collapse acm-notimplemented">
      <td>DecreaseReplicaCount</td>
       <td style="text-align:right">-</td>
    </tr>
    <tr class="collapse acm-notimplemented">
      <td>DeleteGlobalReplicationGroup</td>
       <td style="text-align:right">-</td>
    </tr>
    <tr class="collapse acm-notimplemented">
      <td>DeleteSnapshot</td>
       <td style="text-align:right">-</td>
    </tr>
    <tr class="collapse acm-notimplemented">
      <td>DeleteUser</td>
       <td style="text-align:right">-</td>
    </tr>
    <tr class="collapse acm-notimplemented">
      <td>DeleteUserGroup</td>
       <td style="text-align:right">-</td>
    </tr>
    <tr class="collapse acm-notimplemented">
      <td>DescribeCacheEngineVersions</td>
       <td style="text-align:right">-</td>
    </tr>
    <tr class="collapse acm-notimplemented">
      <td>DescribeEngineDefaultParameters</td>
       <td style="text-align:right">-</td>
    </tr>
    <tr class="collapse acm-notimplemented">
      <td>DescribeEvents</td>
       <td style="text-align:right">-</td>
    </tr>
    <tr class="collapse acm-notimplemented">
      <td>DescribeGlobalReplicationGroups</td>
       <td style="text-align:right">-</td>
    </tr>
    <tr class="collapse acm-notimplemented">
      <td>DescribeReservedCacheNodes</td>
       <td style="text-align:right">-</td>
    </tr>
    <tr class="collapse acm-notimplemented">
      <td>DescribeReservedCacheNodesOfferings</td>
       <td style="text-align:right">-</td>
    </tr>
    <tr class="collapse acm-notimplemented">
      <td>DescribeServiceUpdates</td>
       <td style="text-align:right">-</td>
    </tr>
    <tr class="collapse acm-notimplemented">
      <td>DescribeSnapshots</td>
       <td style="text-align:right">-</td>
    </tr>
    <tr class="collapse acm-notimplemented">
      <td>DescribeUpdateActions</td>
       <td style="text-align:right">-</td>
    </tr>
    <tr class="collapse acm-notimplemented">
      <td>DescribeUserGroups</td>
       <td style="text-align:right">-</td>
    </tr>
    <tr class="collapse acm-notimplemented">
      <td>DescribeUsers</td>
       <td style="text-align:right">-</td>
    </tr>
    <tr class="collapse acm-notimplemented">
      <td>DisassociateGlobalReplicationGroup</td>
       <td style="text-align:right">-</td>
    </tr>
    <tr class="collapse acm-notimplemented">
      <td>FailoverGlobalReplicationGroup</td>
       <td style="text-align:right">-</td>
    </tr>
    <tr class="collapse acm-notimplemented">
      <td>IncreaseNodeGroupsInGlobalReplicationGroup</td>
       <td style="text-align:right">-</td>
    </tr>
    <tr class="collapse acm-notimplemented">
      <td>IncreaseReplicaCount</td>
       <td style="text-align:right">-</td>
    </tr>
    <tr class="collapse acm-notimplemented">
      <td>ListAllowedNodeTypeModifications</td>
       <td style="text-align:right">-</td>
    </tr>
    <tr class="collapse acm-notimplemented">
      <td>ModifyGlobalReplicationGroup</td>
       <td style="text-align:right">-</td>
    </tr>
    <tr class="collapse acm-notimplemented">
      <td>ModifyReplicationGroupShardConfiguration</td>
       <td style="text-align:right">-</td>
    </tr>
    <tr class="collapse acm-notimplemented">
      <td>ModifyUser</td>
       <td style="text-align:right">-</td>
    </tr>
    <tr class="collapse acm-notimplemented">
      <td>ModifyUserGroup</td>
       <td style="text-align:right">-</td>
    </tr>
    <tr class="collapse acm-notimplemented">
      <td>PurchaseReservedCacheNodesOffering</td>
       <td style="text-align:right">-</td>
    </tr>
    <tr class="collapse acm-notimplemented">
      <td>RebalanceSlotsInGlobalReplicationGroup</td>
       <td style="text-align:right">-</td>
    </tr>
    <tr class="collapse acm-notimplemented">
      <td>RebootCacheCluster</td>
       <td style="text-align:right">-</td>
    </tr>
    <tr class="collapse acm-notimplemented">
      <td>ResetCacheParameterGroup</td>
       <td style="text-align:right">-</td>
    </tr>
    <tr class="collapse acm-notimplemented">
      <td>RevokeCacheSecurityGroupIngress</td>
       <td style="text-align:right">-</td>
    </tr>
    <tr class="collapse acm-notimplemented">
      <td>StartMigration</td>
       <td style="text-align:right">-</td>
    </tr>
    <tr class="collapse acm-notimplemented">
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
      <td>CreateApplication <a href="#misc" title="covered by our integration test suite">✨</a></td>
       <td style="text-align:right">✅</td>
    </tr>
    <tr>
      <td>CreateApplicationVersion <a href="#misc" title="covered by our integration test suite">✨</a></td>
       <td style="text-align:right">✅</td>
    </tr>
    <tr>
      <td>CreateEnvironment <a href="#misc" title="covered by our integration test suite">✨</a></td>
       <td style="text-align:right">✅</td>
    </tr>
    <tr>
      <td>DeleteApplication <a href="#misc" title="covered by our integration test suite">✨</a></td>
       <td style="text-align:right">✅</td>
    </tr>
    <tr>
      <td>DeleteApplicationVersion <a href="#misc" title="covered by our integration test suite">✨</a></td>
       <td style="text-align:right">✅</td>
    </tr>
    <tr>
      <td>DeleteEnvironmentConfiguration <a href="#misc" title="covered by our integration test suite">✨</a></td>
       <td style="text-align:right">✅</td>
    </tr>
    <tr>
      <td>DescribeApplicationVersions <a href="#misc" title="covered by our integration test suite">✨</a></td>
       <td style="text-align:right">✅</td>
    </tr>
    <tr>
      <td>DescribeApplications <a href="#misc" title="covered by our integration test suite">✨</a></td>
       <td style="text-align:right">✅</td>
    </tr>
    <tr>
      <td>DescribeEnvironments <a href="#misc" title="covered by our integration test suite">✨</a></td>
       <td style="text-align:right">✅</td>
    </tr>
    <tr>
      <td>UpdateApplication <a href="#misc" title="covered by our integration test suite">✨</a></td>
       <td style="text-align:right">✅</td>
    </tr>
    <tr>
      <td>UpdateApplicationVersion <a href="#misc" title="covered by our integration test suite">✨</a></td>
       <td style="text-align:right">✅</td>
    </tr>
    <tr>
      <td>UpdateEnvironment <a href="#misc" title="covered by our integration test suite">✨</a></td>
       <td style="text-align:right">✅</td>
    </tr>
    <tr>
      <td><a data-toggle="collapse" href=".acm-notimplemented">Show more</a></td>
      <td style="text-align:right"></td>
    </tr>
    <tr class="collapse acm-notimplemented">
      <td>AbortEnvironmentUpdate</td>
       <td style="text-align:right">-</td>
    </tr>
    <tr class="collapse acm-notimplemented">
      <td>ApplyEnvironmentManagedAction</td>
       <td style="text-align:right">-</td>
    </tr>
    <tr class="collapse acm-notimplemented">
      <td>AssociateEnvironmentOperationsRole</td>
       <td style="text-align:right">-</td>
    </tr>
    <tr class="collapse acm-notimplemented">
      <td>CheckDNSAvailability</td>
       <td style="text-align:right">-</td>
    </tr>
    <tr class="collapse acm-notimplemented">
      <td>ComposeEnvironments</td>
       <td style="text-align:right">-</td>
    </tr>
    <tr class="collapse acm-notimplemented">
      <td>CreateConfigurationTemplate</td>
       <td style="text-align:right">-</td>
    </tr>
    <tr class="collapse acm-notimplemented">
      <td>CreatePlatformVersion</td>
       <td style="text-align:right">-</td>
    </tr>
    <tr class="collapse acm-notimplemented">
      <td>CreateStorageLocation</td>
       <td style="text-align:right">-</td>
    </tr>
    <tr class="collapse acm-notimplemented">
      <td>DeleteConfigurationTemplate</td>
       <td style="text-align:right">-</td>
    </tr>
    <tr class="collapse acm-notimplemented">
      <td>DeletePlatformVersion</td>
       <td style="text-align:right">-</td>
    </tr>
    <tr class="collapse acm-notimplemented">
      <td>DescribeAccountAttributes</td>
       <td style="text-align:right">-</td>
    </tr>
    <tr class="collapse acm-notimplemented">
      <td>DescribeConfigurationOptions</td>
       <td style="text-align:right">-</td>
    </tr>
    <tr class="collapse acm-notimplemented">
      <td>DescribeConfigurationSettings</td>
       <td style="text-align:right">-</td>
    </tr>
    <tr class="collapse acm-notimplemented">
      <td>DescribeEnvironmentHealth</td>
       <td style="text-align:right">-</td>
    </tr>
    <tr class="collapse acm-notimplemented">
      <td>DescribeEnvironmentManagedActionHistory</td>
       <td style="text-align:right">-</td>
    </tr>
    <tr class="collapse acm-notimplemented">
      <td>DescribeEnvironmentManagedActions</td>
       <td style="text-align:right">-</td>
    </tr>
    <tr class="collapse acm-notimplemented">
      <td>DescribeEnvironmentResources</td>
       <td style="text-align:right">-</td>
    </tr>
    <tr class="collapse acm-notimplemented">
      <td>DescribeEvents</td>
       <td style="text-align:right">-</td>
    </tr>
    <tr class="collapse acm-notimplemented">
      <td>DescribeInstancesHealth</td>
       <td style="text-align:right">-</td>
    </tr>
    <tr class="collapse acm-notimplemented">
      <td>DescribePlatformVersion</td>
       <td style="text-align:right">-</td>
    </tr>
    <tr class="collapse acm-notimplemented">
      <td>DisassociateEnvironmentOperationsRole</td>
       <td style="text-align:right">-</td>
    </tr>
    <tr class="collapse acm-notimplemented">
      <td>ListAvailableSolutionStacks</td>
       <td style="text-align:right">-</td>
    </tr>
    <tr class="collapse acm-notimplemented">
      <td>ListPlatformBranches</td>
       <td style="text-align:right">-</td>
    </tr>
    <tr class="collapse acm-notimplemented">
      <td>ListPlatformVersions</td>
       <td style="text-align:right">-</td>
    </tr>
    <tr class="collapse acm-notimplemented">
      <td>ListTagsForResource</td>
       <td style="text-align:right">-</td>
    </tr>
    <tr class="collapse acm-notimplemented">
      <td>RebuildEnvironment</td>
       <td style="text-align:right">-</td>
    </tr>
    <tr class="collapse acm-notimplemented">
      <td>RequestEnvironmentInfo</td>
       <td style="text-align:right">-</td>
    </tr>
    <tr class="collapse acm-notimplemented">
      <td>RestartAppServer</td>
       <td style="text-align:right">-</td>
    </tr>
    <tr class="collapse acm-notimplemented">
      <td>RetrieveEnvironmentInfo</td>
       <td style="text-align:right">-</td>
    </tr>
    <tr class="collapse acm-notimplemented">
      <td>SwapEnvironmentCNAMEs</td>
       <td style="text-align:right">-</td>
    </tr>
    <tr class="collapse acm-notimplemented">
      <td>TerminateEnvironment</td>
       <td style="text-align:right">-</td>
    </tr>
    <tr class="collapse acm-notimplemented">
      <td>UpdateApplicationResourceLifecycle</td>
       <td style="text-align:right">-</td>
    </tr>
    <tr class="collapse acm-notimplemented">
      <td>UpdateConfigurationTemplate</td>
       <td style="text-align:right">-</td>
    </tr>
    <tr class="collapse acm-notimplemented">
      <td>UpdateTagsForResource</td>
       <td style="text-align:right">-</td>
    </tr>
    <tr class="collapse acm-notimplemented">
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
      <td>AddTags</td>
       <td style="text-align:right">✅</td>
    </tr>
    <tr>
      <td>ApplySecurityGroupsToLoadBalancer</td>
       <td style="text-align:right">✅</td>
    </tr>
    <tr>
      <td>AttachLoadBalancerToSubnets</td>
       <td style="text-align:right">✅</td>
    </tr>
    <tr>
      <td>ConfigureHealthCheck</td>
       <td style="text-align:right">✅</td>
    </tr>
    <tr>
      <td>CreateAppCookieStickinessPolicy</td>
       <td style="text-align:right">✅</td>
    </tr>
    <tr>
      <td>CreateLBCookieStickinessPolicy</td>
       <td style="text-align:right">✅</td>
    </tr>
    <tr>
      <td>CreateLoadBalancer</td>
       <td style="text-align:right">✅</td>
    </tr>
    <tr>
      <td>CreateLoadBalancerListeners</td>
       <td style="text-align:right">✅</td>
    </tr>
    <tr>
      <td>CreateLoadBalancerPolicy</td>
       <td style="text-align:right">✅</td>
    </tr>
    <tr>
      <td>DeleteLoadBalancer</td>
       <td style="text-align:right">✅</td>
    </tr>
    <tr>
      <td>DeleteLoadBalancerListeners</td>
       <td style="text-align:right">✅</td>
    </tr>
    <tr>
      <td>DeleteLoadBalancerPolicy</td>
       <td style="text-align:right">✅</td>
    </tr>
    <tr>
      <td>DeregisterInstancesFromLoadBalancer</td>
       <td style="text-align:right">✅</td>
    </tr>
    <tr>
      <td>DescribeInstanceHealth</td>
       <td style="text-align:right">✅</td>
    </tr>
    <tr>
      <td>DescribeLoadBalancerAttributes</td>
       <td style="text-align:right">✅</td>
    </tr>
    <tr>
      <td>DescribeLoadBalancerPolicies</td>
       <td style="text-align:right">✅</td>
    </tr>
    <tr>
      <td>DescribeLoadBalancers</td>
       <td style="text-align:right">✅</td>
    </tr>
    <tr>
      <td>DescribeTags</td>
       <td style="text-align:right">✅</td>
    </tr>
    <tr>
      <td>DetachLoadBalancerFromSubnets</td>
       <td style="text-align:right">✅</td>
    </tr>
    <tr>
      <td>DisableAvailabilityZonesForLoadBalancer</td>
       <td style="text-align:right">✅</td>
    </tr>
    <tr>
      <td>EnableAvailabilityZonesForLoadBalancer</td>
       <td style="text-align:right">✅</td>
    </tr>
    <tr>
      <td>ModifyLoadBalancerAttributes</td>
       <td style="text-align:right">✅</td>
    </tr>
    <tr>
      <td>RegisterInstancesWithLoadBalancer</td>
       <td style="text-align:right">✅</td>
    </tr>
    <tr>
      <td>RemoveTags</td>
       <td style="text-align:right">✅</td>
    </tr>
    <tr>
      <td>SetLoadBalancerListenerSSLCertificate</td>
       <td style="text-align:right">✅</td>
    </tr>
    <tr>
      <td>SetLoadBalancerPoliciesForBackendServer</td>
       <td style="text-align:right">✅</td>
    </tr>
    <tr>
      <td>SetLoadBalancerPoliciesOfListener</td>
       <td style="text-align:right">✅</td>
    </tr>
    <tr>
      <td><a data-toggle="collapse" href=".acm-notimplemented">Show more</a></td>
      <td style="text-align:right"></td>
    </tr>
    <tr class="collapse acm-notimplemented">
      <td>DescribeAccountLimits</td>
       <td style="text-align:right">-</td>
    </tr>
    <tr class="collapse acm-notimplemented">
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
      <td>AddListenerCertificates</td>
       <td style="text-align:right">✅</td>
    </tr>
    <tr>
      <td>AddTags</td>
       <td style="text-align:right">✅</td>
    </tr>
    <tr>
      <td>CreateListener <a href="#misc" title="covered by our integration test suite">✨</a></td>
       <td style="text-align:right">✅</td>
    </tr>
    <tr>
      <td>CreateLoadBalancer <a href="#misc" title="covered by our integration test suite">✨</a></td>
       <td style="text-align:right">✅</td>
    </tr>
    <tr>
      <td>CreateRule <a href="#misc" title="covered by our integration test suite">✨</a></td>
       <td style="text-align:right">✅</td>
    </tr>
    <tr>
      <td>CreateTargetGroup <a href="#misc" title="covered by our integration test suite">✨</a></td>
       <td style="text-align:right">✅</td>
    </tr>
    <tr>
      <td>DeleteListener</td>
       <td style="text-align:right">✅</td>
    </tr>
    <tr>
      <td>DeleteLoadBalancer</td>
       <td style="text-align:right">✅</td>
    </tr>
    <tr>
      <td>DeleteRule</td>
       <td style="text-align:right">✅</td>
    </tr>
    <tr>
      <td>DeleteTargetGroup</td>
       <td style="text-align:right">✅</td>
    </tr>
    <tr>
      <td>DeregisterTargets</td>
       <td style="text-align:right">✅</td>
    </tr>
    <tr>
      <td>DescribeAccountLimits</td>
       <td style="text-align:right">✅</td>
    </tr>
    <tr>
      <td>DescribeListenerCertificates</td>
       <td style="text-align:right">✅</td>
    </tr>
    <tr>
      <td>DescribeListeners <a href="#misc" title="covered by our integration test suite">✨</a></td>
       <td style="text-align:right">✅</td>
    </tr>
    <tr>
      <td>DescribeLoadBalancerAttributes</td>
       <td style="text-align:right">✅</td>
    </tr>
    <tr>
      <td>DescribeLoadBalancers <a href="#misc" title="covered by our integration test suite">✨</a></td>
       <td style="text-align:right">✅</td>
    </tr>
    <tr>
      <td>DescribeRules <a href="#misc" title="covered by our integration test suite">✨</a></td>
       <td style="text-align:right">✅</td>
    </tr>
    <tr>
      <td>DescribeSSLPolicies</td>
       <td style="text-align:right">✅</td>
    </tr>
    <tr>
      <td>DescribeTags</td>
       <td style="text-align:right">✅</td>
    </tr>
    <tr>
      <td>DescribeTargetGroupAttributes</td>
       <td style="text-align:right">✅</td>
    </tr>
    <tr>
      <td>DescribeTargetGroups <a href="#misc" title="covered by our integration test suite">✨</a></td>
       <td style="text-align:right">✅</td>
    </tr>
    <tr>
      <td>DescribeTargetHealth</td>
       <td style="text-align:right">✅</td>
    </tr>
    <tr>
      <td>ModifyListener</td>
       <td style="text-align:right">✅</td>
    </tr>
    <tr>
      <td>ModifyLoadBalancerAttributes <a href="#misc" title="covered by our integration test suite">✨</a></td>
       <td style="text-align:right">✅</td>
    </tr>
    <tr>
      <td>ModifyRule</td>
       <td style="text-align:right">✅</td>
    </tr>
    <tr>
      <td>ModifyTargetGroup</td>
       <td style="text-align:right">✅</td>
    </tr>
    <tr>
      <td>ModifyTargetGroupAttributes</td>
       <td style="text-align:right">✅</td>
    </tr>
    <tr>
      <td>RegisterTargets <a href="#misc" title="covered by our integration test suite">✨</a></td>
       <td style="text-align:right">✅</td>
    </tr>
    <tr>
      <td>RemoveListenerCertificates</td>
       <td style="text-align:right">✅</td>
    </tr>
    <tr>
      <td>RemoveTags</td>
       <td style="text-align:right">✅</td>
    </tr>
    <tr>
      <td>SetIpAddressType</td>
       <td style="text-align:right">✅</td>
    </tr>
    <tr>
      <td>SetRulePriorities</td>
       <td style="text-align:right">✅</td>
    </tr>
    <tr>
      <td>SetSecurityGroups</td>
       <td style="text-align:right">✅</td>
    </tr>
    <tr>
      <td>SetSubnets</td>
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
      <td>AddInstanceFleet <a href="#misc" title="covered by our integration test suite">✨</a></td>
       <td style="text-align:right">✅</td>
    </tr>
    <tr>
      <td>AddInstanceGroups</td>
       <td style="text-align:right">✅</td>
    </tr>
    <tr>
      <td>AddJobFlowSteps</td>
       <td style="text-align:right">✅</td>
    </tr>
    <tr>
      <td>AddTags</td>
       <td style="text-align:right">✅</td>
    </tr>
    <tr>
      <td>CreateSecurityConfiguration</td>
       <td style="text-align:right">✅</td>
    </tr>
    <tr>
      <td>DeleteSecurityConfiguration</td>
       <td style="text-align:right">✅</td>
    </tr>
    <tr>
      <td>DescribeCluster <a href="#misc" title="covered by our integration test suite">✨</a></td>
       <td style="text-align:right">✅</td>
    </tr>
    <tr>
      <td>DescribeJobFlows</td>
       <td style="text-align:right">✅</td>
    </tr>
    <tr>
      <td>DescribeSecurityConfiguration</td>
       <td style="text-align:right">✅</td>
    </tr>
    <tr>
      <td>DescribeStep</td>
       <td style="text-align:right">✅</td>
    </tr>
    <tr>
      <td>GetAutoTerminationPolicy <a href="#misc" title="covered by our integration test suite">✨</a></td>
       <td style="text-align:right">✅</td>
    </tr>
    <tr>
      <td>GetBlockPublicAccessConfiguration</td>
       <td style="text-align:right">✅</td>
    </tr>
    <tr>
      <td>ListBootstrapActions <a href="#misc" title="covered by our integration test suite">✨</a></td>
       <td style="text-align:right">✅</td>
    </tr>
    <tr>
      <td>ListClusters <a href="#misc" title="covered by our integration test suite">✨</a></td>
       <td style="text-align:right">✅</td>
    </tr>
    <tr>
      <td>ListInstanceFleets <a href="#misc" title="covered by our integration test suite">✨</a></td>
       <td style="text-align:right">✅</td>
    </tr>
    <tr>
      <td>ListInstanceGroups <a href="#misc" title="covered by our integration test suite">✨</a></td>
       <td style="text-align:right">✅</td>
    </tr>
    <tr>
      <td>ListInstances</td>
       <td style="text-align:right">✅</td>
    </tr>
    <tr>
      <td>ListSteps <a href="#misc" title="covered by our integration test suite">✨</a></td>
       <td style="text-align:right">✅</td>
    </tr>
    <tr>
      <td>ModifyCluster</td>
       <td style="text-align:right">✅</td>
    </tr>
    <tr>
      <td>ModifyInstanceFleet <a href="#misc" title="covered by our integration test suite">✨</a></td>
       <td style="text-align:right">✅</td>
    </tr>
    <tr>
      <td>ModifyInstanceGroups</td>
       <td style="text-align:right">✅</td>
    </tr>
    <tr>
      <td>PutAutoScalingPolicy</td>
       <td style="text-align:right">✅</td>
    </tr>
    <tr>
      <td>PutAutoTerminationPolicy <a href="#misc" title="covered by our integration test suite">✨</a></td>
       <td style="text-align:right">✅</td>
    </tr>
    <tr>
      <td>RemoveAutoScalingPolicy</td>
       <td style="text-align:right">✅</td>
    </tr>
    <tr>
      <td>RemoveAutoTerminationPolicy <a href="#misc" title="covered by our integration test suite">✨</a></td>
       <td style="text-align:right">✅</td>
    </tr>
    <tr>
      <td>RemoveTags</td>
       <td style="text-align:right">✅</td>
    </tr>
    <tr>
      <td>RunJobFlow <a href="#misc" title="covered by our integration test suite">✨</a></td>
       <td style="text-align:right">✅</td>
    </tr>
    <tr>
      <td>SetTerminationProtection</td>
       <td style="text-align:right">✅</td>
    </tr>
    <tr>
      <td>SetVisibleToAllUsers</td>
       <td style="text-align:right">✅</td>
    </tr>
    <tr>
      <td>TerminateJobFlows <a href="#misc" title="covered by our integration test suite">✨</a></td>
       <td style="text-align:right">✅</td>
    </tr>
    <tr>
      <td><a data-toggle="collapse" href=".acm-notimplemented">Show more</a></td>
      <td style="text-align:right"></td>
    </tr>
    <tr class="collapse acm-notimplemented">
      <td>CancelSteps</td>
       <td style="text-align:right">-</td>
    </tr>
    <tr class="collapse acm-notimplemented">
      <td>CreateStudio</td>
       <td style="text-align:right">-</td>
    </tr>
    <tr class="collapse acm-notimplemented">
      <td>CreateStudioSessionMapping</td>
       <td style="text-align:right">-</td>
    </tr>
    <tr class="collapse acm-notimplemented">
      <td>DeleteStudio</td>
       <td style="text-align:right">-</td>
    </tr>
    <tr class="collapse acm-notimplemented">
      <td>DeleteStudioSessionMapping</td>
       <td style="text-align:right">-</td>
    </tr>
    <tr class="collapse acm-notimplemented">
      <td>DescribeNotebookExecution</td>
       <td style="text-align:right">-</td>
    </tr>
    <tr class="collapse acm-notimplemented">
      <td>DescribeReleaseLabel</td>
       <td style="text-align:right">-</td>
    </tr>
    <tr class="collapse acm-notimplemented">
      <td>DescribeStudio</td>
       <td style="text-align:right">-</td>
    </tr>
    <tr class="collapse acm-notimplemented">
      <td>GetManagedScalingPolicy</td>
       <td style="text-align:right">-</td>
    </tr>
    <tr class="collapse acm-notimplemented">
      <td>GetStudioSessionMapping</td>
       <td style="text-align:right">-</td>
    </tr>
    <tr class="collapse acm-notimplemented">
      <td>ListNotebookExecutions</td>
       <td style="text-align:right">-</td>
    </tr>
    <tr class="collapse acm-notimplemented">
      <td>ListReleaseLabels</td>
       <td style="text-align:right">-</td>
    </tr>
    <tr class="collapse acm-notimplemented">
      <td>ListSecurityConfigurations</td>
       <td style="text-align:right">-</td>
    </tr>
    <tr class="collapse acm-notimplemented">
      <td>ListStudioSessionMappings</td>
       <td style="text-align:right">-</td>
    </tr>
    <tr class="collapse acm-notimplemented">
      <td>ListStudios</td>
       <td style="text-align:right">-</td>
    </tr>
    <tr class="collapse acm-notimplemented">
      <td>PutBlockPublicAccessConfiguration</td>
       <td style="text-align:right">-</td>
    </tr>
    <tr class="collapse acm-notimplemented">
      <td>PutManagedScalingPolicy</td>
       <td style="text-align:right">-</td>
    </tr>
    <tr class="collapse acm-notimplemented">
      <td>RemoveManagedScalingPolicy</td>
       <td style="text-align:right">-</td>
    </tr>
    <tr class="collapse acm-notimplemented">
      <td>StartNotebookExecution</td>
       <td style="text-align:right">-</td>
    </tr>
    <tr class="collapse acm-notimplemented">
      <td>StopNotebookExecution</td>
       <td style="text-align:right">-</td>
    </tr>
    <tr class="collapse acm-notimplemented">
      <td>UpdateStudio</td>
       <td style="text-align:right">-</td>
    </tr>
    <tr class="collapse acm-notimplemented">
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
    <tr>
      <td><a data-toggle="collapse" href=".acm-notimplemented">Show more</a></td>
      <td style="text-align:right"></td>
    </tr>
    <tr class="collapse acm-notimplemented">
      <td>AcceptInboundCrossClusterSearchConnection</td>
       <td style="text-align:right">-</td>
    </tr>
    <tr class="collapse acm-notimplemented">
      <td>AssociatePackage</td>
       <td style="text-align:right">-</td>
    </tr>
    <tr class="collapse acm-notimplemented">
      <td>CancelElasticsearchServiceSoftwareUpdate</td>
       <td style="text-align:right">-</td>
    </tr>
    <tr class="collapse acm-notimplemented">
      <td>CreateOutboundCrossClusterSearchConnection</td>
       <td style="text-align:right">-</td>
    </tr>
    <tr class="collapse acm-notimplemented">
      <td>CreatePackage</td>
       <td style="text-align:right">-</td>
    </tr>
    <tr class="collapse acm-notimplemented">
      <td>DeleteElasticsearchServiceRole</td>
       <td style="text-align:right">-</td>
    </tr>
    <tr class="collapse acm-notimplemented">
      <td>DeleteInboundCrossClusterSearchConnection</td>
       <td style="text-align:right">-</td>
    </tr>
    <tr class="collapse acm-notimplemented">
      <td>DeleteOutboundCrossClusterSearchConnection</td>
       <td style="text-align:right">-</td>
    </tr>
    <tr class="collapse acm-notimplemented">
      <td>DeletePackage</td>
       <td style="text-align:right">-</td>
    </tr>
    <tr class="collapse acm-notimplemented">
      <td>DescribeDomainAutoTunes</td>
       <td style="text-align:right">-</td>
    </tr>
    <tr class="collapse acm-notimplemented">
      <td>DescribeDomainChangeProgress</td>
       <td style="text-align:right">-</td>
    </tr>
    <tr class="collapse acm-notimplemented">
      <td>DescribeElasticsearchInstanceTypeLimits</td>
       <td style="text-align:right">-</td>
    </tr>
    <tr class="collapse acm-notimplemented">
      <td>DescribeInboundCrossClusterSearchConnections</td>
       <td style="text-align:right">-</td>
    </tr>
    <tr class="collapse acm-notimplemented">
      <td>DescribeOutboundCrossClusterSearchConnections</td>
       <td style="text-align:right">-</td>
    </tr>
    <tr class="collapse acm-notimplemented">
      <td>DescribePackages</td>
       <td style="text-align:right">-</td>
    </tr>
    <tr class="collapse acm-notimplemented">
      <td>DescribeReservedElasticsearchInstanceOfferings</td>
       <td style="text-align:right">-</td>
    </tr>
    <tr class="collapse acm-notimplemented">
      <td>DescribeReservedElasticsearchInstances</td>
       <td style="text-align:right">-</td>
    </tr>
    <tr class="collapse acm-notimplemented">
      <td>DissociatePackage</td>
       <td style="text-align:right">-</td>
    </tr>
    <tr class="collapse acm-notimplemented">
      <td>GetPackageVersionHistory</td>
       <td style="text-align:right">-</td>
    </tr>
    <tr class="collapse acm-notimplemented">
      <td>GetUpgradeHistory</td>
       <td style="text-align:right">-</td>
    </tr>
    <tr class="collapse acm-notimplemented">
      <td>GetUpgradeStatus</td>
       <td style="text-align:right">-</td>
    </tr>
    <tr class="collapse acm-notimplemented">
      <td>ListDomainsForPackage</td>
       <td style="text-align:right">-</td>
    </tr>
    <tr class="collapse acm-notimplemented">
      <td>ListElasticsearchInstanceTypes</td>
       <td style="text-align:right">-</td>
    </tr>
    <tr class="collapse acm-notimplemented">
      <td>ListPackagesForDomain</td>
       <td style="text-align:right">-</td>
    </tr>
    <tr class="collapse acm-notimplemented">
      <td>PurchaseReservedElasticsearchInstanceOffering</td>
       <td style="text-align:right">-</td>
    </tr>
    <tr class="collapse acm-notimplemented">
      <td>RejectInboundCrossClusterSearchConnection</td>
       <td style="text-align:right">-</td>
    </tr>
    <tr class="collapse acm-notimplemented">
      <td>StartElasticsearchServiceSoftwareUpdate</td>
       <td style="text-align:right">-</td>
    </tr>
    <tr class="collapse acm-notimplemented">
      <td>UpdatePackage</td>
       <td style="text-align:right">-</td>
    </tr>
    <tr class="collapse acm-notimplemented">
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
    <tr>
      <td><a data-toggle="collapse" href=".acm-notimplemented">Show more</a></td>
      <td style="text-align:right"></td>
    </tr>
    <tr class="collapse acm-notimplemented">
      <td>ActivateEventSource</td>
       <td style="text-align:right">-</td>
    </tr>
    <tr class="collapse acm-notimplemented">
      <td>CreateEndpoint</td>
       <td style="text-align:right">-</td>
    </tr>
    <tr class="collapse acm-notimplemented">
      <td>CreatePartnerEventSource</td>
       <td style="text-align:right">-</td>
    </tr>
    <tr class="collapse acm-notimplemented">
      <td>DeactivateEventSource</td>
       <td style="text-align:right">-</td>
    </tr>
    <tr class="collapse acm-notimplemented">
      <td>DeauthorizeConnection</td>
       <td style="text-align:right">-</td>
    </tr>
    <tr class="collapse acm-notimplemented">
      <td>DeleteEndpoint</td>
       <td style="text-align:right">-</td>
    </tr>
    <tr class="collapse acm-notimplemented">
      <td>DeletePartnerEventSource</td>
       <td style="text-align:right">-</td>
    </tr>
    <tr class="collapse acm-notimplemented">
      <td>DescribeEndpoint</td>
       <td style="text-align:right">-</td>
    </tr>
    <tr class="collapse acm-notimplemented">
      <td>DescribeEventSource</td>
       <td style="text-align:right">-</td>
    </tr>
    <tr class="collapse acm-notimplemented">
      <td>DescribePartnerEventSource</td>
       <td style="text-align:right">-</td>
    </tr>
    <tr class="collapse acm-notimplemented">
      <td>ListEndpoints</td>
       <td style="text-align:right">-</td>
    </tr>
    <tr class="collapse acm-notimplemented">
      <td>ListEventSources</td>
       <td style="text-align:right">-</td>
    </tr>
    <tr class="collapse acm-notimplemented">
      <td>ListPartnerEventSourceAccounts</td>
       <td style="text-align:right">-</td>
    </tr>
    <tr class="collapse acm-notimplemented">
      <td>ListPartnerEventSources</td>
       <td style="text-align:right">-</td>
    </tr>
    <tr class="collapse acm-notimplemented">
      <td>PutPartnerEvents</td>
       <td style="text-align:right">-</td>
    </tr>
    <tr class="collapse acm-notimplemented">
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
    <tr>
      <td><a data-toggle="collapse" href=".acm-notimplemented">Show more</a></td>
      <td style="text-align:right"></td>
    </tr>
    <tr class="collapse acm-notimplemented">
      <td>StartDeliveryStreamEncryption</td>
       <td style="text-align:right">-</td>
    </tr>
    <tr class="collapse acm-notimplemented">
      <td>StopDeliveryStreamEncryption</td>
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
      <td>AbortMultipartUpload</td>
       <td style="text-align:right">✅</td>
    </tr>
    <tr>
      <td>AbortVaultLock</td>
       <td style="text-align:right">✅</td>
    </tr>
    <tr>
      <td>AddTagsToVault <a href="#misc" title="covered by our integration test suite">✨</a></td>
       <td style="text-align:right">✅</td>
    </tr>
    <tr>
      <td>CompleteMultipartUpload</td>
       <td style="text-align:right">✅</td>
    </tr>
    <tr>
      <td>CompleteVaultLock</td>
       <td style="text-align:right">✅</td>
    </tr>
    <tr>
      <td>CreateVault <a href="#misc" title="covered by our integration test suite">✨</a></td>
       <td style="text-align:right">✅</td>
    </tr>
    <tr>
      <td>DeleteArchive</td>
       <td style="text-align:right">✅</td>
    </tr>
    <tr>
      <td>DeleteVault <a href="#misc" title="covered by our integration test suite">✨</a></td>
       <td style="text-align:right">✅</td>
    </tr>
    <tr>
      <td>DeleteVaultAccessPolicy</td>
       <td style="text-align:right">✅</td>
    </tr>
    <tr>
      <td>DeleteVaultNotifications</td>
       <td style="text-align:right">✅</td>
    </tr>
    <tr>
      <td>DescribeJob</td>
       <td style="text-align:right">✅</td>
    </tr>
    <tr>
      <td>DescribeVault <a href="#misc" title="covered by our integration test suite">✨</a></td>
       <td style="text-align:right">✅</td>
    </tr>
    <tr>
      <td>GetDataRetrievalPolicy</td>
       <td style="text-align:right">✅</td>
    </tr>
    <tr>
      <td>GetJobOutput <a href="#misc" title="covered by our integration test suite">✨</a></td>
       <td style="text-align:right">✅</td>
    </tr>
    <tr>
      <td>GetVaultAccessPolicy <a href="#misc" title="covered by our integration test suite">✨</a></td>
       <td style="text-align:right">✅</td>
    </tr>
    <tr>
      <td>GetVaultLock</td>
       <td style="text-align:right">✅</td>
    </tr>
    <tr>
      <td>GetVaultNotifications <a href="#misc" title="covered by our integration test suite">✨</a></td>
       <td style="text-align:right">✅</td>
    </tr>
    <tr>
      <td>InitiateJob <a href="#misc" title="covered by our integration test suite">✨</a></td>
       <td style="text-align:right">✅</td>
    </tr>
    <tr>
      <td>InitiateMultipartUpload</td>
       <td style="text-align:right">✅</td>
    </tr>
    <tr>
      <td>InitiateVaultLock</td>
       <td style="text-align:right">✅</td>
    </tr>
    <tr>
      <td>ListJobs</td>
       <td style="text-align:right">✅</td>
    </tr>
    <tr>
      <td>ListMultipartUploads</td>
       <td style="text-align:right">✅</td>
    </tr>
    <tr>
      <td>ListParts</td>
       <td style="text-align:right">✅</td>
    </tr>
    <tr>
      <td>ListProvisionedCapacity</td>
       <td style="text-align:right">✅</td>
    </tr>
    <tr>
      <td>ListTagsForVault <a href="#misc" title="covered by our integration test suite">✨</a></td>
       <td style="text-align:right">✅</td>
    </tr>
    <tr>
      <td>ListVaults <a href="#misc" title="covered by our integration test suite">✨</a></td>
       <td style="text-align:right">✅</td>
    </tr>
    <tr>
      <td>PurchaseProvisionedCapacity</td>
       <td style="text-align:right">✅</td>
    </tr>
    <tr>
      <td>RemoveTagsFromVault</td>
       <td style="text-align:right">✅</td>
    </tr>
    <tr>
      <td>SetDataRetrievalPolicy</td>
       <td style="text-align:right">✅</td>
    </tr>
    <tr>
      <td>SetVaultAccessPolicy</td>
       <td style="text-align:right">✅</td>
    </tr>
    <tr>
      <td>SetVaultNotifications</td>
       <td style="text-align:right">✅</td>
    </tr>
    <tr>
      <td>UploadArchive <a href="#misc" title="covered by our integration test suite">✨</a></td>
       <td style="text-align:right">✅</td>
    </tr>
    <tr>
      <td>UploadMultipartPart</td>
       <td style="text-align:right">✅</td>
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
      <td>BatchCreatePartition</td>
       <td style="text-align:right">✅</td>
    </tr>
    <tr>
      <td>BatchDeletePartition</td>
       <td style="text-align:right">✅</td>
    </tr>
    <tr>
      <td>BatchDeleteTable</td>
       <td style="text-align:right">✅</td>
    </tr>
    <tr>
      <td>BatchGetPartition</td>
       <td style="text-align:right">✅</td>
    </tr>
    <tr>
      <td>BatchUpdatePartition</td>
       <td style="text-align:right">✅</td>
    </tr>
    <tr>
      <td>CheckSchemaVersionValidity</td>
       <td style="text-align:right">✅</td>
    </tr>
    <tr>
      <td>CreateClassifier <a href="#misc" title="covered by our integration test suite">✨</a></td>
       <td style="text-align:right">✅</td>
    </tr>
    <tr>
      <td>CreateConnection <a href="#misc" title="covered by our integration test suite">✨</a></td>
       <td style="text-align:right">✅</td>
    </tr>
    <tr>
      <td>CreateCrawler <a href="#misc" title="covered by our integration test suite">✨</a></td>
       <td style="text-align:right">✅</td>
    </tr>
    <tr>
      <td>CreateDatabase <a href="#misc" title="covered by our integration test suite">✨</a></td>
       <td style="text-align:right">✅</td>
    </tr>
    <tr>
      <td>CreateJob <a href="#misc" title="covered by our integration test suite">✨</a></td>
       <td style="text-align:right">✅</td>
    </tr>
    <tr>
      <td>CreatePartition <a href="#misc" title="covered by our integration test suite">✨</a></td>
       <td style="text-align:right">✅</td>
    </tr>
    <tr>
      <td>CreatePartitionIndex <a href="#misc" title="covered by our integration test suite">✨</a></td>
       <td style="text-align:right">✅</td>
    </tr>
    <tr>
      <td>CreateRegistry <a href="#misc" title="covered by our integration test suite">✨</a></td>
       <td style="text-align:right">✅</td>
    </tr>
    <tr>
      <td>CreateSchema <a href="#misc" title="covered by our integration test suite">✨</a></td>
       <td style="text-align:right">✅</td>
    </tr>
    <tr>
      <td>CreateSecurityConfiguration <a href="#misc" title="covered by our integration test suite">✨</a></td>
       <td style="text-align:right">✅</td>
    </tr>
    <tr>
      <td>CreateTable <a href="#misc" title="covered by our integration test suite">✨</a></td>
       <td style="text-align:right">✅</td>
    </tr>
    <tr>
      <td>CreateTrigger <a href="#misc" title="covered by our integration test suite">✨</a></td>
       <td style="text-align:right">✅</td>
    </tr>
    <tr>
      <td>CreateWorkflow <a href="#misc" title="covered by our integration test suite">✨</a></td>
       <td style="text-align:right">✅</td>
    </tr>
    <tr>
      <td>DeleteClassifier <a href="#misc" title="covered by our integration test suite">✨</a></td>
       <td style="text-align:right">✅</td>
    </tr>
    <tr>
      <td>DeleteConnection <a href="#misc" title="covered by our integration test suite">✨</a></td>
       <td style="text-align:right">✅</td>
    </tr>
    <tr>
      <td>DeleteCrawler <a href="#misc" title="covered by our integration test suite">✨</a></td>
       <td style="text-align:right">✅</td>
    </tr>
    <tr>
      <td>DeleteDatabase <a href="#misc" title="covered by our integration test suite">✨</a></td>
       <td style="text-align:right">✅</td>
    </tr>
    <tr>
      <td>DeleteJob <a href="#misc" title="covered by our integration test suite">✨</a></td>
       <td style="text-align:right">✅</td>
    </tr>
    <tr>
      <td>DeletePartition <a href="#misc" title="covered by our integration test suite">✨</a></td>
       <td style="text-align:right">✅</td>
    </tr>
    <tr>
      <td>DeletePartitionIndex <a href="#misc" title="covered by our integration test suite">✨</a></td>
       <td style="text-align:right">✅</td>
    </tr>
    <tr>
      <td>DeleteRegistry <a href="#misc" title="covered by our integration test suite">✨</a></td>
       <td style="text-align:right">✅</td>
    </tr>
    <tr>
      <td>DeleteResourcePolicy <a href="#misc" title="covered by our integration test suite">✨</a></td>
       <td style="text-align:right">✅</td>
    </tr>
    <tr>
      <td>DeleteSchema <a href="#misc" title="covered by our integration test suite">✨</a></td>
       <td style="text-align:right">✅</td>
    </tr>
    <tr>
      <td>DeleteSchemaVersions <a href="#misc" title="covered by our integration test suite">✨</a></td>
       <td style="text-align:right">✅</td>
    </tr>
    <tr>
      <td>DeleteSecurityConfiguration <a href="#misc" title="covered by our integration test suite">✨</a></td>
       <td style="text-align:right">✅</td>
    </tr>
    <tr>
      <td>DeleteTable <a href="#misc" title="covered by our integration test suite">✨</a></td>
       <td style="text-align:right">✅</td>
    </tr>
    <tr>
      <td>DeleteTrigger <a href="#misc" title="covered by our integration test suite">✨</a></td>
       <td style="text-align:right">✅</td>
    </tr>
    <tr>
      <td>DeleteWorkflow <a href="#misc" title="covered by our integration test suite">✨</a></td>
       <td style="text-align:right">✅</td>
    </tr>
    <tr>
      <td>GetCatalogImportStatus</td>
       <td style="text-align:right">✅</td>
    </tr>
    <tr>
      <td>GetClassifier <a href="#misc" title="covered by our integration test suite">✨</a></td>
       <td style="text-align:right">✅</td>
    </tr>
    <tr>
      <td>GetClassifiers <a href="#misc" title="covered by our integration test suite">✨</a></td>
       <td style="text-align:right">✅</td>
    </tr>
    <tr>
      <td>GetConnection <a href="#misc" title="covered by our integration test suite">✨</a></td>
       <td style="text-align:right">✅</td>
    </tr>
    <tr>
      <td>GetConnections <a href="#misc" title="covered by our integration test suite">✨</a></td>
       <td style="text-align:right">✅</td>
    </tr>
    <tr>
      <td>GetCrawler <a href="#misc" title="covered by our integration test suite">✨</a></td>
       <td style="text-align:right">✅</td>
    </tr>
    <tr>
      <td>GetCrawlers <a href="#misc" title="covered by our integration test suite">✨</a></td>
       <td style="text-align:right">✅</td>
    </tr>
    <tr>
      <td>GetDatabase <a href="#misc" title="covered by our integration test suite">✨</a></td>
       <td style="text-align:right">✅</td>
    </tr>
    <tr>
      <td>GetDatabases <a href="#misc" title="covered by our integration test suite">✨</a></td>
       <td style="text-align:right">✅</td>
    </tr>
    <tr>
      <td>GetJob <a href="#misc" title="covered by our integration test suite">✨</a></td>
       <td style="text-align:right">✅</td>
    </tr>
    <tr>
      <td>GetJobRun <a href="#misc" title="covered by our integration test suite">✨</a></td>
       <td style="text-align:right">✅</td>
    </tr>
    <tr>
      <td>GetJobRuns <a href="#misc" title="covered by our integration test suite">✨</a></td>
       <td style="text-align:right">✅</td>
    </tr>
    <tr>
      <td>GetJobs <a href="#misc" title="covered by our integration test suite">✨</a></td>
       <td style="text-align:right">✅</td>
    </tr>
    <tr>
      <td>GetPartition <a href="#misc" title="covered by our integration test suite">✨</a></td>
       <td style="text-align:right">✅</td>
    </tr>
    <tr>
      <td>GetPartitionIndexes <a href="#misc" title="covered by our integration test suite">✨</a></td>
       <td style="text-align:right">✅</td>
    </tr>
    <tr>
      <td>GetPartitions <a href="#misc" title="covered by our integration test suite">✨</a></td>
       <td style="text-align:right">✅</td>
    </tr>
    <tr>
      <td>GetRegistry <a href="#misc" title="covered by our integration test suite">✨</a></td>
       <td style="text-align:right">✅</td>
    </tr>
    <tr>
      <td>GetResourcePolicy <a href="#misc" title="covered by our integration test suite">✨</a></td>
       <td style="text-align:right">✅</td>
    </tr>
    <tr>
      <td>GetSchema <a href="#misc" title="covered by our integration test suite">✨</a></td>
       <td style="text-align:right">✅</td>
    </tr>
    <tr>
      <td>GetSchemaByDefinition</td>
       <td style="text-align:right">✅</td>
    </tr>
    <tr>
      <td>GetSchemaVersion <a href="#misc" title="covered by our integration test suite">✨</a></td>
       <td style="text-align:right">✅</td>
    </tr>
    <tr>
      <td>GetSchemaVersionsDiff</td>
       <td style="text-align:right">✅</td>
    </tr>
    <tr>
      <td>GetSecurityConfiguration <a href="#misc" title="covered by our integration test suite">✨</a></td>
       <td style="text-align:right">✅</td>
    </tr>
    <tr>
      <td>GetSecurityConfigurations <a href="#misc" title="covered by our integration test suite">✨</a></td>
       <td style="text-align:right">✅</td>
    </tr>
    <tr>
      <td>GetTable <a href="#misc" title="covered by our integration test suite">✨</a></td>
       <td style="text-align:right">✅</td>
    </tr>
    <tr>
      <td>GetTableVersion</td>
       <td style="text-align:right">✅</td>
    </tr>
    <tr>
      <td>GetTableVersions</td>
       <td style="text-align:right">✅</td>
    </tr>
    <tr>
      <td>GetTables <a href="#misc" title="covered by our integration test suite">✨</a></td>
       <td style="text-align:right">✅</td>
    </tr>
    <tr>
      <td>GetTags</td>
       <td style="text-align:right">✅</td>
    </tr>
    <tr>
      <td>GetTrigger <a href="#misc" title="covered by our integration test suite">✨</a></td>
       <td style="text-align:right">✅</td>
    </tr>
    <tr>
      <td>GetWorkflow <a href="#misc" title="covered by our integration test suite">✨</a></td>
       <td style="text-align:right">✅</td>
    </tr>
    <tr>
      <td>ImportCatalogToGlue</td>
       <td style="text-align:right">✅</td>
    </tr>
    <tr>
      <td>ListJobs <a href="#misc" title="covered by our integration test suite">✨</a></td>
       <td style="text-align:right">✅</td>
    </tr>
    <tr>
      <td>ListRegistries <a href="#misc" title="covered by our integration test suite">✨</a></td>
       <td style="text-align:right">✅</td>
    </tr>
    <tr>
      <td>ListSchemaVersions <a href="#misc" title="covered by our integration test suite">✨</a></td>
       <td style="text-align:right">✅</td>
    </tr>
    <tr>
      <td>ListSchemas <a href="#misc" title="covered by our integration test suite">✨</a></td>
       <td style="text-align:right">✅</td>
    </tr>
    <tr>
      <td>ListWorkflows <a href="#misc" title="covered by our integration test suite">✨</a></td>
       <td style="text-align:right">✅</td>
    </tr>
    <tr>
      <td>PutResourcePolicy <a href="#misc" title="covered by our integration test suite">✨</a></td>
       <td style="text-align:right">✅</td>
    </tr>
    <tr>
      <td>PutSchemaVersionMetadata <a href="#misc" title="covered by our integration test suite">✨</a></td>
       <td style="text-align:right">✅</td>
    </tr>
    <tr>
      <td>QuerySchemaVersionMetadata <a href="#misc" title="covered by our integration test suite">✨</a></td>
       <td style="text-align:right">✅</td>
    </tr>
    <tr>
      <td>RegisterSchemaVersion <a href="#misc" title="covered by our integration test suite">✨</a></td>
       <td style="text-align:right">✅</td>
    </tr>
    <tr>
      <td>RemoveSchemaVersionMetadata <a href="#misc" title="covered by our integration test suite">✨</a></td>
       <td style="text-align:right">✅</td>
    </tr>
    <tr>
      <td>StartCrawler <a href="#misc" title="covered by our integration test suite">✨</a></td>
       <td style="text-align:right">✅</td>
    </tr>
    <tr>
      <td>StartJobRun <a href="#misc" title="covered by our integration test suite">✨</a></td>
       <td style="text-align:right">✅</td>
    </tr>
    <tr>
      <td>StartTrigger</td>
       <td style="text-align:right">✅</td>
    </tr>
    <tr>
      <td>StopCrawler</td>
       <td style="text-align:right">✅</td>
    </tr>
    <tr>
      <td>StopTrigger</td>
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
      <td>UpdateClassifier</td>
       <td style="text-align:right">✅</td>
    </tr>
    <tr>
      <td>UpdateConnection</td>
       <td style="text-align:right">✅</td>
    </tr>
    <tr>
      <td>UpdateCrawler <a href="#misc" title="covered by our integration test suite">✨</a></td>
       <td style="text-align:right">✅</td>
    </tr>
    <tr>
      <td>UpdateDatabase <a href="#misc" title="covered by our integration test suite">✨</a></td>
       <td style="text-align:right">✅</td>
    </tr>
    <tr>
      <td>UpdateJob <a href="#misc" title="covered by our integration test suite">✨</a></td>
       <td style="text-align:right">✅</td>
    </tr>
    <tr>
      <td>UpdatePartition <a href="#misc" title="covered by our integration test suite">✨</a></td>
       <td style="text-align:right">✅</td>
    </tr>
    <tr>
      <td>UpdateRegistry <a href="#misc" title="covered by our integration test suite">✨</a></td>
       <td style="text-align:right">✅</td>
    </tr>
    <tr>
      <td>UpdateSchema <a href="#misc" title="covered by our integration test suite">✨</a></td>
       <td style="text-align:right">✅</td>
    </tr>
    <tr>
      <td>UpdateTable <a href="#misc" title="covered by our integration test suite">✨</a></td>
       <td style="text-align:right">✅</td>
    </tr>
    <tr>
      <td>UpdateTrigger <a href="#misc" title="covered by our integration test suite">✨</a></td>
       <td style="text-align:right">✅</td>
    </tr>
    <tr>
      <td>UpdateWorkflow</td>
       <td style="text-align:right">✅</td>
    </tr>
    <tr>
      <td><a data-toggle="collapse" href=".acm-notimplemented">Show more</a></td>
      <td style="text-align:right"></td>
    </tr>
    <tr class="collapse acm-notimplemented">
      <td>BatchDeleteConnection</td>
       <td style="text-align:right">-</td>
    </tr>
    <tr class="collapse acm-notimplemented">
      <td>BatchDeleteTableVersion</td>
       <td style="text-align:right">-</td>
    </tr>
    <tr class="collapse acm-notimplemented">
      <td>BatchGetBlueprints</td>
       <td style="text-align:right">-</td>
    </tr>
    <tr class="collapse acm-notimplemented">
      <td>BatchGetCrawlers</td>
       <td style="text-align:right">-</td>
    </tr>
    <tr class="collapse acm-notimplemented">
      <td>BatchGetCustomEntityTypes</td>
       <td style="text-align:right">-</td>
    </tr>
    <tr class="collapse acm-notimplemented">
      <td>BatchGetDevEndpoints</td>
       <td style="text-align:right">-</td>
    </tr>
    <tr class="collapse acm-notimplemented">
      <td>BatchGetJobs</td>
       <td style="text-align:right">-</td>
    </tr>
    <tr class="collapse acm-notimplemented">
      <td>BatchGetTriggers</td>
       <td style="text-align:right">-</td>
    </tr>
    <tr class="collapse acm-notimplemented">
      <td>BatchGetWorkflows</td>
       <td style="text-align:right">-</td>
    </tr>
    <tr class="collapse acm-notimplemented">
      <td>BatchStopJobRun</td>
       <td style="text-align:right">-</td>
    </tr>
    <tr class="collapse acm-notimplemented">
      <td>CancelMLTaskRun</td>
       <td style="text-align:right">-</td>
    </tr>
    <tr class="collapse acm-notimplemented">
      <td>CancelStatement</td>
       <td style="text-align:right">-</td>
    </tr>
    <tr class="collapse acm-notimplemented">
      <td>CreateBlueprint</td>
       <td style="text-align:right">-</td>
    </tr>
    <tr class="collapse acm-notimplemented">
      <td>CreateCustomEntityType</td>
       <td style="text-align:right">-</td>
    </tr>
    <tr class="collapse acm-notimplemented">
      <td>CreateDevEndpoint</td>
       <td style="text-align:right">-</td>
    </tr>
    <tr class="collapse acm-notimplemented">
      <td>CreateMLTransform</td>
       <td style="text-align:right">-</td>
    </tr>
    <tr class="collapse acm-notimplemented">
      <td>CreateScript</td>
       <td style="text-align:right">-</td>
    </tr>
    <tr class="collapse acm-notimplemented">
      <td>CreateSession</td>
       <td style="text-align:right">-</td>
    </tr>
    <tr class="collapse acm-notimplemented">
      <td>CreateUserDefinedFunction</td>
       <td style="text-align:right">-</td>
    </tr>
    <tr class="collapse acm-notimplemented">
      <td>DeleteBlueprint</td>
       <td style="text-align:right">-</td>
    </tr>
    <tr class="collapse acm-notimplemented">
      <td>DeleteColumnStatisticsForPartition</td>
       <td style="text-align:right">-</td>
    </tr>
    <tr class="collapse acm-notimplemented">
      <td>DeleteColumnStatisticsForTable</td>
       <td style="text-align:right">-</td>
    </tr>
    <tr class="collapse acm-notimplemented">
      <td>DeleteCustomEntityType</td>
       <td style="text-align:right">-</td>
    </tr>
    <tr class="collapse acm-notimplemented">
      <td>DeleteDevEndpoint</td>
       <td style="text-align:right">-</td>
    </tr>
    <tr class="collapse acm-notimplemented">
      <td>DeleteMLTransform</td>
       <td style="text-align:right">-</td>
    </tr>
    <tr class="collapse acm-notimplemented">
      <td>DeleteSession</td>
       <td style="text-align:right">-</td>
    </tr>
    <tr class="collapse acm-notimplemented">
      <td>DeleteTableVersion</td>
       <td style="text-align:right">-</td>
    </tr>
    <tr class="collapse acm-notimplemented">
      <td>DeleteUserDefinedFunction</td>
       <td style="text-align:right">-</td>
    </tr>
    <tr class="collapse acm-notimplemented">
      <td>GetBlueprint</td>
       <td style="text-align:right">-</td>
    </tr>
    <tr class="collapse acm-notimplemented">
      <td>GetBlueprintRun</td>
       <td style="text-align:right">-</td>
    </tr>
    <tr class="collapse acm-notimplemented">
      <td>GetBlueprintRuns</td>
       <td style="text-align:right">-</td>
    </tr>
    <tr class="collapse acm-notimplemented">
      <td>GetColumnStatisticsForPartition</td>
       <td style="text-align:right">-</td>
    </tr>
    <tr class="collapse acm-notimplemented">
      <td>GetColumnStatisticsForTable</td>
       <td style="text-align:right">-</td>
    </tr>
    <tr class="collapse acm-notimplemented">
      <td>GetCrawlerMetrics</td>
       <td style="text-align:right">-</td>
    </tr>
    <tr class="collapse acm-notimplemented">
      <td>GetCustomEntityType</td>
       <td style="text-align:right">-</td>
    </tr>
    <tr class="collapse acm-notimplemented">
      <td>GetDataCatalogEncryptionSettings</td>
       <td style="text-align:right">-</td>
    </tr>
    <tr class="collapse acm-notimplemented">
      <td>GetDataflowGraph</td>
       <td style="text-align:right">-</td>
    </tr>
    <tr class="collapse acm-notimplemented">
      <td>GetDevEndpoint</td>
       <td style="text-align:right">-</td>
    </tr>
    <tr class="collapse acm-notimplemented">
      <td>GetDevEndpoints</td>
       <td style="text-align:right">-</td>
    </tr>
    <tr class="collapse acm-notimplemented">
      <td>GetJobBookmark</td>
       <td style="text-align:right">-</td>
    </tr>
    <tr class="collapse acm-notimplemented">
      <td>GetMLTaskRun</td>
       <td style="text-align:right">-</td>
    </tr>
    <tr class="collapse acm-notimplemented">
      <td>GetMLTaskRuns</td>
       <td style="text-align:right">-</td>
    </tr>
    <tr class="collapse acm-notimplemented">
      <td>GetMLTransform</td>
       <td style="text-align:right">-</td>
    </tr>
    <tr class="collapse acm-notimplemented">
      <td>GetMLTransforms</td>
       <td style="text-align:right">-</td>
    </tr>
    <tr class="collapse acm-notimplemented">
      <td>GetMapping</td>
       <td style="text-align:right">-</td>
    </tr>
    <tr class="collapse acm-notimplemented">
      <td>GetPlan</td>
       <td style="text-align:right">-</td>
    </tr>
    <tr class="collapse acm-notimplemented">
      <td>GetResourcePolicies</td>
       <td style="text-align:right">-</td>
    </tr>
    <tr class="collapse acm-notimplemented">
      <td>GetSession</td>
       <td style="text-align:right">-</td>
    </tr>
    <tr class="collapse acm-notimplemented">
      <td>GetStatement</td>
       <td style="text-align:right">-</td>
    </tr>
    <tr class="collapse acm-notimplemented">
      <td>GetTriggers</td>
       <td style="text-align:right">-</td>
    </tr>
    <tr class="collapse acm-notimplemented">
      <td>GetUnfilteredPartitionMetadata</td>
       <td style="text-align:right">-</td>
    </tr>
    <tr class="collapse acm-notimplemented">
      <td>GetUnfilteredPartitionsMetadata</td>
       <td style="text-align:right">-</td>
    </tr>
    <tr class="collapse acm-notimplemented">
      <td>GetUnfilteredTableMetadata</td>
       <td style="text-align:right">-</td>
    </tr>
    <tr class="collapse acm-notimplemented">
      <td>GetUserDefinedFunction</td>
       <td style="text-align:right">-</td>
    </tr>
    <tr class="collapse acm-notimplemented">
      <td>GetUserDefinedFunctions</td>
       <td style="text-align:right">-</td>
    </tr>
    <tr class="collapse acm-notimplemented">
      <td>GetWorkflowRun</td>
       <td style="text-align:right">-</td>
    </tr>
    <tr class="collapse acm-notimplemented">
      <td>GetWorkflowRunProperties</td>
       <td style="text-align:right">-</td>
    </tr>
    <tr class="collapse acm-notimplemented">
      <td>GetWorkflowRuns</td>
       <td style="text-align:right">-</td>
    </tr>
    <tr class="collapse acm-notimplemented">
      <td>ListBlueprints</td>
       <td style="text-align:right">-</td>
    </tr>
    <tr class="collapse acm-notimplemented">
      <td>ListCrawlers</td>
       <td style="text-align:right">-</td>
    </tr>
    <tr class="collapse acm-notimplemented">
      <td>ListCrawls</td>
       <td style="text-align:right">-</td>
    </tr>
    <tr class="collapse acm-notimplemented">
      <td>ListCustomEntityTypes</td>
       <td style="text-align:right">-</td>
    </tr>
    <tr class="collapse acm-notimplemented">
      <td>ListDevEndpoints</td>
       <td style="text-align:right">-</td>
    </tr>
    <tr class="collapse acm-notimplemented">
      <td>ListMLTransforms</td>
       <td style="text-align:right">-</td>
    </tr>
    <tr class="collapse acm-notimplemented">
      <td>ListSessions</td>
       <td style="text-align:right">-</td>
    </tr>
    <tr class="collapse acm-notimplemented">
      <td>ListStatements</td>
       <td style="text-align:right">-</td>
    </tr>
    <tr class="collapse acm-notimplemented">
      <td>ListTriggers</td>
       <td style="text-align:right">-</td>
    </tr>
    <tr class="collapse acm-notimplemented">
      <td>PutDataCatalogEncryptionSettings</td>
       <td style="text-align:right">-</td>
    </tr>
    <tr class="collapse acm-notimplemented">
      <td>PutWorkflowRunProperties</td>
       <td style="text-align:right">-</td>
    </tr>
    <tr class="collapse acm-notimplemented">
      <td>ResetJobBookmark</td>
       <td style="text-align:right">-</td>
    </tr>
    <tr class="collapse acm-notimplemented">
      <td>ResumeWorkflowRun</td>
       <td style="text-align:right">-</td>
    </tr>
    <tr class="collapse acm-notimplemented">
      <td>RunStatement</td>
       <td style="text-align:right">-</td>
    </tr>
    <tr class="collapse acm-notimplemented">
      <td>SearchTables</td>
       <td style="text-align:right">-</td>
    </tr>
    <tr class="collapse acm-notimplemented">
      <td>StartBlueprintRun</td>
       <td style="text-align:right">-</td>
    </tr>
    <tr class="collapse acm-notimplemented">
      <td>StartCrawlerSchedule</td>
       <td style="text-align:right">-</td>
    </tr>
    <tr class="collapse acm-notimplemented">
      <td>StartExportLabelsTaskRun</td>
       <td style="text-align:right">-</td>
    </tr>
    <tr class="collapse acm-notimplemented">
      <td>StartImportLabelsTaskRun</td>
       <td style="text-align:right">-</td>
    </tr>
    <tr class="collapse acm-notimplemented">
      <td>StartMLEvaluationTaskRun</td>
       <td style="text-align:right">-</td>
    </tr>
    <tr class="collapse acm-notimplemented">
      <td>StartMLLabelingSetGenerationTaskRun</td>
       <td style="text-align:right">-</td>
    </tr>
    <tr class="collapse acm-notimplemented">
      <td>StartWorkflowRun</td>
       <td style="text-align:right">-</td>
    </tr>
    <tr class="collapse acm-notimplemented">
      <td>StopCrawlerSchedule</td>
       <td style="text-align:right">-</td>
    </tr>
    <tr class="collapse acm-notimplemented">
      <td>StopSession</td>
       <td style="text-align:right">-</td>
    </tr>
    <tr class="collapse acm-notimplemented">
      <td>StopWorkflowRun</td>
       <td style="text-align:right">-</td>
    </tr>
    <tr class="collapse acm-notimplemented">
      <td>UpdateBlueprint</td>
       <td style="text-align:right">-</td>
    </tr>
    <tr class="collapse acm-notimplemented">
      <td>UpdateColumnStatisticsForPartition</td>
       <td style="text-align:right">-</td>
    </tr>
    <tr class="collapse acm-notimplemented">
      <td>UpdateColumnStatisticsForTable</td>
       <td style="text-align:right">-</td>
    </tr>
    <tr class="collapse acm-notimplemented">
      <td>UpdateCrawlerSchedule</td>
       <td style="text-align:right">-</td>
    </tr>
    <tr class="collapse acm-notimplemented">
      <td>UpdateDevEndpoint</td>
       <td style="text-align:right">-</td>
    </tr>
    <tr class="collapse acm-notimplemented">
      <td>UpdateMLTransform</td>
       <td style="text-align:right">-</td>
    </tr>
    <tr class="collapse acm-notimplemented">
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
      <td>AddUserToGroup</td>
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
      <td>DeleteAccessKey</td>
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
      <td>GetAccountAuthorizationDetails <a href="#misc" title="covered by our integration test suite">✨</a></td>
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
      <td>ListAccessKeys</td>
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
      <td>ListGroups</td>
       <td style="text-align:right">✅</td>
    </tr>
    <tr>
      <td>ListGroupsForUser</td>
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
      <td>ListUsers</td>
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
      <td>PutRolePermissionsBoundary</td>
       <td style="text-align:right">✅</td>
    </tr>
    <tr>
      <td>PutRolePolicy <a href="#misc" title="covered by our integration test suite">✨</a></td>
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
      <td>RemoveUserFromGroup</td>
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
      <td>UpdateAssumeRolePolicy</td>
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
    <tr>
      <td><a data-toggle="collapse" href=".acm-notimplemented">Show more</a></td>
      <td style="text-align:right"></td>
    </tr>
    <tr class="collapse acm-notimplemented">
      <td>AddClientIDToOpenIDConnectProvider</td>
       <td style="text-align:right">-</td>
    </tr>
    <tr class="collapse acm-notimplemented">
      <td>ChangePassword</td>
       <td style="text-align:right">-</td>
    </tr>
    <tr class="collapse acm-notimplemented">
      <td>CreateServiceSpecificCredential</td>
       <td style="text-align:right">-</td>
    </tr>
    <tr class="collapse acm-notimplemented">
      <td>DeleteServiceSpecificCredential</td>
       <td style="text-align:right">-</td>
    </tr>
    <tr class="collapse acm-notimplemented">
      <td>DeleteUserPermissionsBoundary</td>
       <td style="text-align:right">-</td>
    </tr>
    <tr class="collapse acm-notimplemented">
      <td>GenerateOrganizationsAccessReport</td>
       <td style="text-align:right">-</td>
    </tr>
    <tr class="collapse acm-notimplemented">
      <td>GenerateServiceLastAccessedDetails</td>
       <td style="text-align:right">-</td>
    </tr>
    <tr class="collapse acm-notimplemented">
      <td>GetContextKeysForCustomPolicy</td>
       <td style="text-align:right">-</td>
    </tr>
    <tr class="collapse acm-notimplemented">
      <td>GetContextKeysForPrincipalPolicy</td>
       <td style="text-align:right">-</td>
    </tr>
    <tr class="collapse acm-notimplemented">
      <td>GetOrganizationsAccessReport</td>
       <td style="text-align:right">-</td>
    </tr>
    <tr class="collapse acm-notimplemented">
      <td>GetServiceLastAccessedDetails</td>
       <td style="text-align:right">-</td>
    </tr>
    <tr class="collapse acm-notimplemented">
      <td>GetServiceLastAccessedDetailsWithEntities</td>
       <td style="text-align:right">-</td>
    </tr>
    <tr class="collapse acm-notimplemented">
      <td>ListMFADeviceTags</td>
       <td style="text-align:right">-</td>
    </tr>
    <tr class="collapse acm-notimplemented">
      <td>ListPoliciesGrantingServiceAccess</td>
       <td style="text-align:right">-</td>
    </tr>
    <tr class="collapse acm-notimplemented">
      <td>ListSAMLProviderTags</td>
       <td style="text-align:right">-</td>
    </tr>
    <tr class="collapse acm-notimplemented">
      <td>ListServerCertificateTags</td>
       <td style="text-align:right">-</td>
    </tr>
    <tr class="collapse acm-notimplemented">
      <td>ListServiceSpecificCredentials</td>
       <td style="text-align:right">-</td>
    </tr>
    <tr class="collapse acm-notimplemented">
      <td>PutUserPermissionsBoundary</td>
       <td style="text-align:right">-</td>
    </tr>
    <tr class="collapse acm-notimplemented">
      <td>RemoveClientIDFromOpenIDConnectProvider</td>
       <td style="text-align:right">-</td>
    </tr>
    <tr class="collapse acm-notimplemented">
      <td>ResetServiceSpecificCredential</td>
       <td style="text-align:right">-</td>
    </tr>
    <tr class="collapse acm-notimplemented">
      <td>ResyncMFADevice</td>
       <td style="text-align:right">-</td>
    </tr>
    <tr class="collapse acm-notimplemented">
      <td>SetSecurityTokenServicePreferences</td>
       <td style="text-align:right">-</td>
    </tr>
    <tr class="collapse acm-notimplemented">
      <td>SimulateCustomPolicy</td>
       <td style="text-align:right">-</td>
    </tr>
    <tr class="collapse acm-notimplemented">
      <td>TagMFADevice</td>
       <td style="text-align:right">-</td>
    </tr>
    <tr class="collapse acm-notimplemented">
      <td>TagSAMLProvider</td>
       <td style="text-align:right">-</td>
    </tr>
    <tr class="collapse acm-notimplemented">
      <td>TagServerCertificate</td>
       <td style="text-align:right">-</td>
    </tr>
    <tr class="collapse acm-notimplemented">
      <td>UntagMFADevice</td>
       <td style="text-align:right">-</td>
    </tr>
    <tr class="collapse acm-notimplemented">
      <td>UntagSAMLProvider</td>
       <td style="text-align:right">-</td>
    </tr>
    <tr class="collapse acm-notimplemented">
      <td>UntagServerCertificate</td>
       <td style="text-align:right">-</td>
    </tr>
    <tr class="collapse acm-notimplemented">
      <td>UpdateServerCertificate</td>
       <td style="text-align:right">-</td>
    </tr>
    <tr class="collapse acm-notimplemented">
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
      <td>AddThingToThingGroup <a href="#misc" title="covered by our integration test suite">✨</a></td>
       <td style="text-align:right">✅</td>
    </tr>
    <tr>
      <td>AttachPolicy <a href="#misc" title="covered by our integration test suite">✨</a></td>
       <td style="text-align:right">✅</td>
    </tr>
    <tr>
      <td>AttachPrincipalPolicy</td>
       <td style="text-align:right">✅</td>
    </tr>
    <tr>
      <td>AttachThingPrincipal <a href="#misc" title="covered by our integration test suite">✨</a></td>
       <td style="text-align:right">✅</td>
    </tr>
    <tr>
      <td>CancelJob</td>
       <td style="text-align:right">✅</td>
    </tr>
    <tr>
      <td>CancelJobExecution</td>
       <td style="text-align:right">✅</td>
    </tr>
    <tr>
      <td>CreateCertificateFromCsr</td>
       <td style="text-align:right">✅</td>
    </tr>
    <tr>
      <td>CreateDomainConfiguration</td>
       <td style="text-align:right">✅</td>
    </tr>
    <tr>
      <td>CreateDynamicThingGroup <a href="#misc" title="covered by our integration test suite">✨</a></td>
       <td style="text-align:right">✅</td>
    </tr>
    <tr>
      <td>CreateJob <a href="#misc" title="covered by our integration test suite">✨</a></td>
       <td style="text-align:right">✅</td>
    </tr>
    <tr>
      <td>CreateKeysAndCertificate</td>
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
      <td>CreateThing <a href="#misc" title="covered by our integration test suite">✨</a></td>
       <td style="text-align:right">✅</td>
    </tr>
    <tr>
      <td>CreateThingGroup <a href="#misc" title="covered by our integration test suite">✨</a></td>
       <td style="text-align:right">✅</td>
    </tr>
    <tr>
      <td>CreateThingType</td>
       <td style="text-align:right">✅</td>
    </tr>
    <tr>
      <td>CreateTopicRule <a href="#misc" title="covered by our integration test suite">✨</a></td>
       <td style="text-align:right">✅</td>
    </tr>
    <tr>
      <td>CreateTopicRuleDestination <a href="#misc" title="covered by our integration test suite">✨</a></td>
       <td style="text-align:right">✅</td>
    </tr>
    <tr>
      <td>DeleteCACertificate</td>
       <td style="text-align:right">✅</td>
    </tr>
    <tr>
      <td>DeleteCertificate</td>
       <td style="text-align:right">✅</td>
    </tr>
    <tr>
      <td>DeleteDomainConfiguration</td>
       <td style="text-align:right">✅</td>
    </tr>
    <tr>
      <td>DeleteDynamicThingGroup <a href="#misc" title="covered by our integration test suite">✨</a></td>
       <td style="text-align:right">✅</td>
    </tr>
    <tr>
      <td>DeleteJob <a href="#misc" title="covered by our integration test suite">✨</a></td>
       <td style="text-align:right">✅</td>
    </tr>
    <tr>
      <td>DeleteJobExecution</td>
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
      <td>DeleteThing <a href="#misc" title="covered by our integration test suite">✨</a></td>
       <td style="text-align:right">✅</td>
    </tr>
    <tr>
      <td>DeleteThingGroup <a href="#misc" title="covered by our integration test suite">✨</a></td>
       <td style="text-align:right">✅</td>
    </tr>
    <tr>
      <td>DeleteThingType</td>
       <td style="text-align:right">✅</td>
    </tr>
    <tr>
      <td>DeleteTopicRule <a href="#misc" title="covered by our integration test suite">✨</a></td>
       <td style="text-align:right">✅</td>
    </tr>
    <tr>
      <td>DeleteTopicRuleDestination</td>
       <td style="text-align:right">✅</td>
    </tr>
    <tr>
      <td>DeprecateThingType</td>
       <td style="text-align:right">✅</td>
    </tr>
    <tr>
      <td>DescribeCACertificate</td>
       <td style="text-align:right">✅</td>
    </tr>
    <tr>
      <td>DescribeCertificate</td>
       <td style="text-align:right">✅</td>
    </tr>
    <tr>
      <td>DescribeDomainConfiguration</td>
       <td style="text-align:right">✅</td>
    </tr>
    <tr>
      <td>DescribeEndpoint <a href="#misc" title="covered by our integration test suite">✨</a></td>
       <td style="text-align:right">✅</td>
    </tr>
    <tr>
      <td>DescribeJob <a href="#misc" title="covered by our integration test suite">✨</a></td>
       <td style="text-align:right">✅</td>
    </tr>
    <tr>
      <td>DescribeJobExecution <a href="#misc" title="covered by our integration test suite">✨</a></td>
       <td style="text-align:right">✅</td>
    </tr>
    <tr>
      <td>DescribeThing <a href="#misc" title="covered by our integration test suite">✨</a></td>
       <td style="text-align:right">✅</td>
    </tr>
    <tr>
      <td>DescribeThingGroup <a href="#misc" title="covered by our integration test suite">✨</a></td>
       <td style="text-align:right">✅</td>
    </tr>
    <tr>
      <td>DescribeThingType</td>
       <td style="text-align:right">✅</td>
    </tr>
    <tr>
      <td>DetachPolicy</td>
       <td style="text-align:right">✅</td>
    </tr>
    <tr>
      <td>DetachPrincipalPolicy</td>
       <td style="text-align:right">✅</td>
    </tr>
    <tr>
      <td>DetachThingPrincipal <a href="#misc" title="covered by our integration test suite">✨</a></td>
       <td style="text-align:right">✅</td>
    </tr>
    <tr>
      <td>DisableTopicRule</td>
       <td style="text-align:right">✅</td>
    </tr>
    <tr>
      <td>EnableTopicRule</td>
       <td style="text-align:right">✅</td>
    </tr>
    <tr>
      <td>GetJobDocument</td>
       <td style="text-align:right">✅</td>
    </tr>
    <tr>
      <td>GetPolicy <a href="#misc" title="covered by our integration test suite">✨</a></td>
       <td style="text-align:right">✅</td>
    </tr>
    <tr>
      <td>GetPolicyVersion</td>
       <td style="text-align:right">✅</td>
    </tr>
    <tr>
      <td>GetRegistrationCode</td>
       <td style="text-align:right">✅</td>
    </tr>
    <tr>
      <td>GetTopicRule <a href="#misc" title="covered by our integration test suite">✨</a></td>
       <td style="text-align:right">✅</td>
    </tr>
    <tr>
      <td>GetTopicRuleDestination</td>
       <td style="text-align:right">✅</td>
    </tr>
    <tr>
      <td>ListAttachedPolicies</td>
       <td style="text-align:right">✅</td>
    </tr>
    <tr>
      <td>ListAuditMitigationActionsTasks</td>
       <td style="text-align:right">✅</td>
    </tr>
    <tr>
      <td>ListAuditTasks</td>
       <td style="text-align:right">✅</td>
    </tr>
    <tr>
      <td>ListCertificates</td>
       <td style="text-align:right">✅</td>
    </tr>
    <tr>
      <td>ListCertificatesByCA</td>
       <td style="text-align:right">✅</td>
    </tr>
    <tr>
      <td>ListDetectMitigationActionsExecutions</td>
       <td style="text-align:right">✅</td>
    </tr>
    <tr>
      <td>ListDetectMitigationActionsTasks</td>
       <td style="text-align:right">✅</td>
    </tr>
    <tr>
      <td>ListDomainConfigurations</td>
       <td style="text-align:right">✅</td>
    </tr>
    <tr>
      <td>ListJobExecutionsForJob</td>
       <td style="text-align:right">✅</td>
    </tr>
    <tr>
      <td>ListJobExecutionsForThing <a href="#misc" title="covered by our integration test suite">✨</a></td>
       <td style="text-align:right">✅</td>
    </tr>
    <tr>
      <td>ListJobs <a href="#misc" title="covered by our integration test suite">✨</a></td>
       <td style="text-align:right">✅</td>
    </tr>
    <tr>
      <td>ListMetricValues</td>
       <td style="text-align:right">✅</td>
    </tr>
    <tr>
      <td>ListPolicies <a href="#misc" title="covered by our integration test suite">✨</a></td>
       <td style="text-align:right">✅</td>
    </tr>
    <tr>
      <td>ListPolicyPrincipals</td>
       <td style="text-align:right">✅</td>
    </tr>
    <tr>
      <td>ListPolicyVersions</td>
       <td style="text-align:right">✅</td>
    </tr>
    <tr>
      <td>ListPrincipalPolicies</td>
       <td style="text-align:right">✅</td>
    </tr>
    <tr>
      <td>ListPrincipalThings</td>
       <td style="text-align:right">✅</td>
    </tr>
    <tr>
      <td>ListTagsForResource <a href="#misc" title="covered by our integration test suite">✨</a></td>
       <td style="text-align:right">✅</td>
    </tr>
    <tr>
      <td>ListThingGroups <a href="#misc" title="covered by our integration test suite">✨</a></td>
       <td style="text-align:right">✅</td>
    </tr>
    <tr>
      <td>ListThingGroupsForThing <a href="#misc" title="covered by our integration test suite">✨</a></td>
       <td style="text-align:right">✅</td>
    </tr>
    <tr>
      <td>ListThingPrincipals <a href="#misc" title="covered by our integration test suite">✨</a></td>
       <td style="text-align:right">✅</td>
    </tr>
    <tr>
      <td>ListThingTypes</td>
       <td style="text-align:right">✅</td>
    </tr>
    <tr>
      <td>ListThings <a href="#misc" title="covered by our integration test suite">✨</a></td>
       <td style="text-align:right">✅</td>
    </tr>
    <tr>
      <td>ListThingsInThingGroup <a href="#misc" title="covered by our integration test suite">✨</a></td>
       <td style="text-align:right">✅</td>
    </tr>
    <tr>
      <td>ListTopicRules <a href="#misc" title="covered by our integration test suite">✨</a></td>
       <td style="text-align:right">✅</td>
    </tr>
    <tr>
      <td>ListViolationEvents</td>
       <td style="text-align:right">✅</td>
    </tr>
    <tr>
      <td>RegisterCACertificate</td>
       <td style="text-align:right">✅</td>
    </tr>
    <tr>
      <td>RegisterCertificate <a href="#misc" title="covered by our integration test suite">✨</a></td>
       <td style="text-align:right">✅</td>
    </tr>
    <tr>
      <td>RegisterCertificateWithoutCA</td>
       <td style="text-align:right">✅</td>
    </tr>
    <tr>
      <td>RemoveThingFromThingGroup <a href="#misc" title="covered by our integration test suite">✨</a></td>
       <td style="text-align:right">✅</td>
    </tr>
    <tr>
      <td>ReplaceTopicRule</td>
       <td style="text-align:right">✅</td>
    </tr>
    <tr>
      <td>SearchIndex <a href="#misc" title="covered by our integration test suite">✨</a></td>
       <td style="text-align:right">✅</td>
    </tr>
    <tr>
      <td>SetDefaultPolicyVersion</td>
       <td style="text-align:right">✅</td>
    </tr>
    <tr>
      <td>TagResource <a href="#misc" title="covered by our integration test suite">✨</a></td>
       <td style="text-align:right">✅</td>
    </tr>
    <tr>
      <td>UpdateCACertificate</td>
       <td style="text-align:right">✅</td>
    </tr>
    <tr>
      <td>UpdateCertificate</td>
       <td style="text-align:right">✅</td>
    </tr>
    <tr>
      <td>UpdateDomainConfiguration</td>
       <td style="text-align:right">✅</td>
    </tr>
    <tr>
      <td>UpdateDynamicThingGroup <a href="#misc" title="covered by our integration test suite">✨</a></td>
       <td style="text-align:right">✅</td>
    </tr>
    <tr>
      <td>UpdateIndexingConfiguration <a href="#misc" title="covered by our integration test suite">✨</a></td>
       <td style="text-align:right">✅</td>
    </tr>
    <tr>
      <td>UpdateThing</td>
       <td style="text-align:right">✅</td>
    </tr>
    <tr>
      <td>UpdateThingGroup</td>
       <td style="text-align:right">✅</td>
    </tr>
    <tr>
      <td>UpdateThingGroupsForThing</td>
       <td style="text-align:right">✅</td>
    </tr>
    <tr>
      <td><a data-toggle="collapse" href=".acm-notimplemented">Show more</a></td>
      <td style="text-align:right"></td>
    </tr>
    <tr class="collapse acm-notimplemented">
      <td>AcceptCertificateTransfer</td>
       <td style="text-align:right">-</td>
    </tr>
    <tr class="collapse acm-notimplemented">
      <td>AddThingToBillingGroup</td>
       <td style="text-align:right">-</td>
    </tr>
    <tr class="collapse acm-notimplemented">
      <td>AssociateTargetsWithJob</td>
       <td style="text-align:right">-</td>
    </tr>
    <tr class="collapse acm-notimplemented">
      <td>AttachSecurityProfile</td>
       <td style="text-align:right">-</td>
    </tr>
    <tr class="collapse acm-notimplemented">
      <td>CancelAuditMitigationActionsTask</td>
       <td style="text-align:right">-</td>
    </tr>
    <tr class="collapse acm-notimplemented">
      <td>CancelAuditTask</td>
       <td style="text-align:right">-</td>
    </tr>
    <tr class="collapse acm-notimplemented">
      <td>CancelCertificateTransfer</td>
       <td style="text-align:right">-</td>
    </tr>
    <tr class="collapse acm-notimplemented">
      <td>CancelDetectMitigationActionsTask</td>
       <td style="text-align:right">-</td>
    </tr>
    <tr class="collapse acm-notimplemented">
      <td>ClearDefaultAuthorizer</td>
       <td style="text-align:right">-</td>
    </tr>
    <tr class="collapse acm-notimplemented">
      <td>ConfirmTopicRuleDestination</td>
       <td style="text-align:right">-</td>
    </tr>
    <tr class="collapse acm-notimplemented">
      <td>CreateAuditSuppression</td>
       <td style="text-align:right">-</td>
    </tr>
    <tr class="collapse acm-notimplemented">
      <td>CreateAuthorizer</td>
       <td style="text-align:right">-</td>
    </tr>
    <tr class="collapse acm-notimplemented">
      <td>CreateBillingGroup</td>
       <td style="text-align:right">-</td>
    </tr>
    <tr class="collapse acm-notimplemented">
      <td>CreateCustomMetric</td>
       <td style="text-align:right">-</td>
    </tr>
    <tr class="collapse acm-notimplemented">
      <td>CreateDimension</td>
       <td style="text-align:right">-</td>
    </tr>
    <tr class="collapse acm-notimplemented">
      <td>CreateFleetMetric</td>
       <td style="text-align:right">-</td>
    </tr>
    <tr class="collapse acm-notimplemented">
      <td>CreateJobTemplate</td>
       <td style="text-align:right">-</td>
    </tr>
    <tr class="collapse acm-notimplemented">
      <td>CreateMitigationAction</td>
       <td style="text-align:right">-</td>
    </tr>
    <tr class="collapse acm-notimplemented">
      <td>CreateOTAUpdate</td>
       <td style="text-align:right">-</td>
    </tr>
    <tr class="collapse acm-notimplemented">
      <td>CreateProvisioningClaim</td>
       <td style="text-align:right">-</td>
    </tr>
    <tr class="collapse acm-notimplemented">
      <td>CreateProvisioningTemplate</td>
       <td style="text-align:right">-</td>
    </tr>
    <tr class="collapse acm-notimplemented">
      <td>CreateProvisioningTemplateVersion</td>
       <td style="text-align:right">-</td>
    </tr>
    <tr class="collapse acm-notimplemented">
      <td>CreateRoleAlias</td>
       <td style="text-align:right">-</td>
    </tr>
    <tr class="collapse acm-notimplemented">
      <td>CreateScheduledAudit</td>
       <td style="text-align:right">-</td>
    </tr>
    <tr class="collapse acm-notimplemented">
      <td>CreateSecurityProfile</td>
       <td style="text-align:right">-</td>
    </tr>
    <tr class="collapse acm-notimplemented">
      <td>CreateStream</td>
       <td style="text-align:right">-</td>
    </tr>
    <tr class="collapse acm-notimplemented">
      <td>DeleteAccountAuditConfiguration</td>
       <td style="text-align:right">-</td>
    </tr>
    <tr class="collapse acm-notimplemented">
      <td>DeleteAuditSuppression</td>
       <td style="text-align:right">-</td>
    </tr>
    <tr class="collapse acm-notimplemented">
      <td>DeleteAuthorizer</td>
       <td style="text-align:right">-</td>
    </tr>
    <tr class="collapse acm-notimplemented">
      <td>DeleteBillingGroup</td>
       <td style="text-align:right">-</td>
    </tr>
    <tr class="collapse acm-notimplemented">
      <td>DeleteCustomMetric</td>
       <td style="text-align:right">-</td>
    </tr>
    <tr class="collapse acm-notimplemented">
      <td>DeleteDimension</td>
       <td style="text-align:right">-</td>
    </tr>
    <tr class="collapse acm-notimplemented">
      <td>DeleteFleetMetric</td>
       <td style="text-align:right">-</td>
    </tr>
    <tr class="collapse acm-notimplemented">
      <td>DeleteJobTemplate</td>
       <td style="text-align:right">-</td>
    </tr>
    <tr class="collapse acm-notimplemented">
      <td>DeleteMitigationAction</td>
       <td style="text-align:right">-</td>
    </tr>
    <tr class="collapse acm-notimplemented">
      <td>DeleteOTAUpdate</td>
       <td style="text-align:right">-</td>
    </tr>
    <tr class="collapse acm-notimplemented">
      <td>DeleteProvisioningTemplate</td>
       <td style="text-align:right">-</td>
    </tr>
    <tr class="collapse acm-notimplemented">
      <td>DeleteProvisioningTemplateVersion</td>
       <td style="text-align:right">-</td>
    </tr>
    <tr class="collapse acm-notimplemented">
      <td>DeleteRegistrationCode</td>
       <td style="text-align:right">-</td>
    </tr>
    <tr class="collapse acm-notimplemented">
      <td>DeleteRoleAlias</td>
       <td style="text-align:right">-</td>
    </tr>
    <tr class="collapse acm-notimplemented">
      <td>DeleteScheduledAudit</td>
       <td style="text-align:right">-</td>
    </tr>
    <tr class="collapse acm-notimplemented">
      <td>DeleteSecurityProfile</td>
       <td style="text-align:right">-</td>
    </tr>
    <tr class="collapse acm-notimplemented">
      <td>DeleteStream</td>
       <td style="text-align:right">-</td>
    </tr>
    <tr class="collapse acm-notimplemented">
      <td>DeleteV2LoggingLevel</td>
       <td style="text-align:right">-</td>
    </tr>
    <tr class="collapse acm-notimplemented">
      <td>DescribeAccountAuditConfiguration</td>
       <td style="text-align:right">-</td>
    </tr>
    <tr class="collapse acm-notimplemented">
      <td>DescribeAuditFinding</td>
       <td style="text-align:right">-</td>
    </tr>
    <tr class="collapse acm-notimplemented">
      <td>DescribeAuditMitigationActionsTask</td>
       <td style="text-align:right">-</td>
    </tr>
    <tr class="collapse acm-notimplemented">
      <td>DescribeAuditSuppression</td>
       <td style="text-align:right">-</td>
    </tr>
    <tr class="collapse acm-notimplemented">
      <td>DescribeAuditTask</td>
       <td style="text-align:right">-</td>
    </tr>
    <tr class="collapse acm-notimplemented">
      <td>DescribeAuthorizer</td>
       <td style="text-align:right">-</td>
    </tr>
    <tr class="collapse acm-notimplemented">
      <td>DescribeBillingGroup</td>
       <td style="text-align:right">-</td>
    </tr>
    <tr class="collapse acm-notimplemented">
      <td>DescribeCustomMetric</td>
       <td style="text-align:right">-</td>
    </tr>
    <tr class="collapse acm-notimplemented">
      <td>DescribeDefaultAuthorizer</td>
       <td style="text-align:right">-</td>
    </tr>
    <tr class="collapse acm-notimplemented">
      <td>DescribeDetectMitigationActionsTask</td>
       <td style="text-align:right">-</td>
    </tr>
    <tr class="collapse acm-notimplemented">
      <td>DescribeDimension</td>
       <td style="text-align:right">-</td>
    </tr>
    <tr class="collapse acm-notimplemented">
      <td>DescribeEventConfigurations</td>
       <td style="text-align:right">-</td>
    </tr>
    <tr class="collapse acm-notimplemented">
      <td>DescribeFleetMetric</td>
       <td style="text-align:right">-</td>
    </tr>
    <tr class="collapse acm-notimplemented">
      <td>DescribeIndex</td>
       <td style="text-align:right">-</td>
    </tr>
    <tr class="collapse acm-notimplemented">
      <td>DescribeJobTemplate</td>
       <td style="text-align:right">-</td>
    </tr>
    <tr class="collapse acm-notimplemented">
      <td>DescribeManagedJobTemplate</td>
       <td style="text-align:right">-</td>
    </tr>
    <tr class="collapse acm-notimplemented">
      <td>DescribeMitigationAction</td>
       <td style="text-align:right">-</td>
    </tr>
    <tr class="collapse acm-notimplemented">
      <td>DescribeProvisioningTemplate</td>
       <td style="text-align:right">-</td>
    </tr>
    <tr class="collapse acm-notimplemented">
      <td>DescribeProvisioningTemplateVersion</td>
       <td style="text-align:right">-</td>
    </tr>
    <tr class="collapse acm-notimplemented">
      <td>DescribeRoleAlias</td>
       <td style="text-align:right">-</td>
    </tr>
    <tr class="collapse acm-notimplemented">
      <td>DescribeScheduledAudit</td>
       <td style="text-align:right">-</td>
    </tr>
    <tr class="collapse acm-notimplemented">
      <td>DescribeSecurityProfile</td>
       <td style="text-align:right">-</td>
    </tr>
    <tr class="collapse acm-notimplemented">
      <td>DescribeStream</td>
       <td style="text-align:right">-</td>
    </tr>
    <tr class="collapse acm-notimplemented">
      <td>DescribeThingRegistrationTask</td>
       <td style="text-align:right">-</td>
    </tr>
    <tr class="collapse acm-notimplemented">
      <td>DetachSecurityProfile</td>
       <td style="text-align:right">-</td>
    </tr>
    <tr class="collapse acm-notimplemented">
      <td>GetBehaviorModelTrainingSummaries</td>
       <td style="text-align:right">-</td>
    </tr>
    <tr class="collapse acm-notimplemented">
      <td>GetBucketsAggregation</td>
       <td style="text-align:right">-</td>
    </tr>
    <tr class="collapse acm-notimplemented">
      <td>GetCardinality</td>
       <td style="text-align:right">-</td>
    </tr>
    <tr class="collapse acm-notimplemented">
      <td>GetEffectivePolicies</td>
       <td style="text-align:right">-</td>
    </tr>
    <tr class="collapse acm-notimplemented">
      <td>GetIndexingConfiguration</td>
       <td style="text-align:right">-</td>
    </tr>
    <tr class="collapse acm-notimplemented">
      <td>GetLoggingOptions</td>
       <td style="text-align:right">-</td>
    </tr>
    <tr class="collapse acm-notimplemented">
      <td>GetOTAUpdate</td>
       <td style="text-align:right">-</td>
    </tr>
    <tr class="collapse acm-notimplemented">
      <td>GetPercentiles</td>
       <td style="text-align:right">-</td>
    </tr>
    <tr class="collapse acm-notimplemented">
      <td>GetStatistics</td>
       <td style="text-align:right">-</td>
    </tr>
    <tr class="collapse acm-notimplemented">
      <td>GetV2LoggingOptions</td>
       <td style="text-align:right">-</td>
    </tr>
    <tr class="collapse acm-notimplemented">
      <td>ListActiveViolations</td>
       <td style="text-align:right">-</td>
    </tr>
    <tr class="collapse acm-notimplemented">
      <td>ListAuditFindings</td>
       <td style="text-align:right">-</td>
    </tr>
    <tr class="collapse acm-notimplemented">
      <td>ListAuditMitigationActionsExecutions</td>
       <td style="text-align:right">-</td>
    </tr>
    <tr class="collapse acm-notimplemented">
      <td>ListAuditSuppressions</td>
       <td style="text-align:right">-</td>
    </tr>
    <tr class="collapse acm-notimplemented">
      <td>ListAuthorizers</td>
       <td style="text-align:right">-</td>
    </tr>
    <tr class="collapse acm-notimplemented">
      <td>ListBillingGroups</td>
       <td style="text-align:right">-</td>
    </tr>
    <tr class="collapse acm-notimplemented">
      <td>ListCACertificates</td>
       <td style="text-align:right">-</td>
    </tr>
    <tr class="collapse acm-notimplemented">
      <td>ListCustomMetrics</td>
       <td style="text-align:right">-</td>
    </tr>
    <tr class="collapse acm-notimplemented">
      <td>ListDimensions</td>
       <td style="text-align:right">-</td>
    </tr>
    <tr class="collapse acm-notimplemented">
      <td>ListFleetMetrics</td>
       <td style="text-align:right">-</td>
    </tr>
    <tr class="collapse acm-notimplemented">
      <td>ListIndices</td>
       <td style="text-align:right">-</td>
    </tr>
    <tr class="collapse acm-notimplemented">
      <td>ListJobTemplates</td>
       <td style="text-align:right">-</td>
    </tr>
    <tr class="collapse acm-notimplemented">
      <td>ListManagedJobTemplates</td>
       <td style="text-align:right">-</td>
    </tr>
    <tr class="collapse acm-notimplemented">
      <td>ListMitigationActions</td>
       <td style="text-align:right">-</td>
    </tr>
    <tr class="collapse acm-notimplemented">
      <td>ListOTAUpdates</td>
       <td style="text-align:right">-</td>
    </tr>
    <tr class="collapse acm-notimplemented">
      <td>ListOutgoingCertificates</td>
       <td style="text-align:right">-</td>
    </tr>
    <tr class="collapse acm-notimplemented">
      <td>ListProvisioningTemplateVersions</td>
       <td style="text-align:right">-</td>
    </tr>
    <tr class="collapse acm-notimplemented">
      <td>ListProvisioningTemplates</td>
       <td style="text-align:right">-</td>
    </tr>
    <tr class="collapse acm-notimplemented">
      <td>ListRoleAliases</td>
       <td style="text-align:right">-</td>
    </tr>
    <tr class="collapse acm-notimplemented">
      <td>ListScheduledAudits</td>
       <td style="text-align:right">-</td>
    </tr>
    <tr class="collapse acm-notimplemented">
      <td>ListSecurityProfiles</td>
       <td style="text-align:right">-</td>
    </tr>
    <tr class="collapse acm-notimplemented">
      <td>ListSecurityProfilesForTarget</td>
       <td style="text-align:right">-</td>
    </tr>
    <tr class="collapse acm-notimplemented">
      <td>ListStreams</td>
       <td style="text-align:right">-</td>
    </tr>
    <tr class="collapse acm-notimplemented">
      <td>ListTargetsForPolicy</td>
       <td style="text-align:right">-</td>
    </tr>
    <tr class="collapse acm-notimplemented">
      <td>ListTargetsForSecurityProfile</td>
       <td style="text-align:right">-</td>
    </tr>
    <tr class="collapse acm-notimplemented">
      <td>ListThingRegistrationTaskReports</td>
       <td style="text-align:right">-</td>
    </tr>
    <tr class="collapse acm-notimplemented">
      <td>ListThingRegistrationTasks</td>
       <td style="text-align:right">-</td>
    </tr>
    <tr class="collapse acm-notimplemented">
      <td>ListThingsInBillingGroup</td>
       <td style="text-align:right">-</td>
    </tr>
    <tr class="collapse acm-notimplemented">
      <td>ListTopicRuleDestinations</td>
       <td style="text-align:right">-</td>
    </tr>
    <tr class="collapse acm-notimplemented">
      <td>ListV2LoggingLevels</td>
       <td style="text-align:right">-</td>
    </tr>
    <tr class="collapse acm-notimplemented">
      <td>PutVerificationStateOnViolation</td>
       <td style="text-align:right">-</td>
    </tr>
    <tr class="collapse acm-notimplemented">
      <td>RegisterThing</td>
       <td style="text-align:right">-</td>
    </tr>
    <tr class="collapse acm-notimplemented">
      <td>RejectCertificateTransfer</td>
       <td style="text-align:right">-</td>
    </tr>
    <tr class="collapse acm-notimplemented">
      <td>RemoveThingFromBillingGroup</td>
       <td style="text-align:right">-</td>
    </tr>
    <tr class="collapse acm-notimplemented">
      <td>SetDefaultAuthorizer</td>
       <td style="text-align:right">-</td>
    </tr>
    <tr class="collapse acm-notimplemented">
      <td>SetLoggingOptions</td>
       <td style="text-align:right">-</td>
    </tr>
    <tr class="collapse acm-notimplemented">
      <td>SetV2LoggingLevel</td>
       <td style="text-align:right">-</td>
    </tr>
    <tr class="collapse acm-notimplemented">
      <td>SetV2LoggingOptions</td>
       <td style="text-align:right">-</td>
    </tr>
    <tr class="collapse acm-notimplemented">
      <td>StartAuditMitigationActionsTask</td>
       <td style="text-align:right">-</td>
    </tr>
    <tr class="collapse acm-notimplemented">
      <td>StartDetectMitigationActionsTask</td>
       <td style="text-align:right">-</td>
    </tr>
    <tr class="collapse acm-notimplemented">
      <td>StartOnDemandAuditTask</td>
       <td style="text-align:right">-</td>
    </tr>
    <tr class="collapse acm-notimplemented">
      <td>StartThingRegistrationTask</td>
       <td style="text-align:right">-</td>
    </tr>
    <tr class="collapse acm-notimplemented">
      <td>StopThingRegistrationTask</td>
       <td style="text-align:right">-</td>
    </tr>
    <tr class="collapse acm-notimplemented">
      <td>TestAuthorization</td>
       <td style="text-align:right">-</td>
    </tr>
    <tr class="collapse acm-notimplemented">
      <td>TestInvokeAuthorizer</td>
       <td style="text-align:right">-</td>
    </tr>
    <tr class="collapse acm-notimplemented">
      <td>TransferCertificate</td>
       <td style="text-align:right">-</td>
    </tr>
    <tr class="collapse acm-notimplemented">
      <td>UntagResource</td>
       <td style="text-align:right">-</td>
    </tr>
    <tr class="collapse acm-notimplemented">
      <td>UpdateAccountAuditConfiguration</td>
       <td style="text-align:right">-</td>
    </tr>
    <tr class="collapse acm-notimplemented">
      <td>UpdateAuditSuppression</td>
       <td style="text-align:right">-</td>
    </tr>
    <tr class="collapse acm-notimplemented">
      <td>UpdateAuthorizer</td>
       <td style="text-align:right">-</td>
    </tr>
    <tr class="collapse acm-notimplemented">
      <td>UpdateBillingGroup</td>
       <td style="text-align:right">-</td>
    </tr>
    <tr class="collapse acm-notimplemented">
      <td>UpdateCustomMetric</td>
       <td style="text-align:right">-</td>
    </tr>
    <tr class="collapse acm-notimplemented">
      <td>UpdateDimension</td>
       <td style="text-align:right">-</td>
    </tr>
    <tr class="collapse acm-notimplemented">
      <td>UpdateEventConfigurations</td>
       <td style="text-align:right">-</td>
    </tr>
    <tr class="collapse acm-notimplemented">
      <td>UpdateFleetMetric</td>
       <td style="text-align:right">-</td>
    </tr>
    <tr class="collapse acm-notimplemented">
      <td>UpdateJob</td>
       <td style="text-align:right">-</td>
    </tr>
    <tr class="collapse acm-notimplemented">
      <td>UpdateMitigationAction</td>
       <td style="text-align:right">-</td>
    </tr>
    <tr class="collapse acm-notimplemented">
      <td>UpdateProvisioningTemplate</td>
       <td style="text-align:right">-</td>
    </tr>
    <tr class="collapse acm-notimplemented">
      <td>UpdateRoleAlias</td>
       <td style="text-align:right">-</td>
    </tr>
    <tr class="collapse acm-notimplemented">
      <td>UpdateScheduledAudit</td>
       <td style="text-align:right">-</td>
    </tr>
    <tr class="collapse acm-notimplemented">
      <td>UpdateSecurityProfile</td>
       <td style="text-align:right">-</td>
    </tr>
    <tr class="collapse acm-notimplemented">
      <td>UpdateStream</td>
       <td style="text-align:right">-</td>
    </tr>
    <tr class="collapse acm-notimplemented">
      <td>UpdateTopicRuleDestination</td>
       <td style="text-align:right">-</td>
    </tr>
    <tr class="collapse acm-notimplemented">
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
      <td>DeleteThingShadow</td>
       <td style="text-align:right">✅</td>
    </tr>
    <tr>
      <td>GetThingShadow <a href="#misc" title="covered by our integration test suite">✨</a></td>
       <td style="text-align:right">✅</td>
    </tr>
    <tr>
      <td>Publish <a href="#misc" title="covered by our integration test suite">✨</a></td>
       <td style="text-align:right">✅</td>
    </tr>
    <tr>
      <td>UpdateThingShadow <a href="#misc" title="covered by our integration test suite">✨</a></td>
       <td style="text-align:right">✅</td>
    </tr>
    <tr>
      <td><a data-toggle="collapse" href=".acm-notimplemented">Show more</a></td>
      <td style="text-align:right"></td>
    </tr>
    <tr class="collapse acm-notimplemented">
      <td>GetRetainedMessage</td>
       <td style="text-align:right">-</td>
    </tr>
    <tr class="collapse acm-notimplemented">
      <td>ListNamedShadowsForThing</td>
       <td style="text-align:right">-</td>
    </tr>
    <tr class="collapse acm-notimplemented">
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
      <td>CreateChannel <a href="#misc" title="covered by our integration test suite">✨</a></td>
       <td style="text-align:right">✅</td>
    </tr>
    <tr>
      <td>CreateDataset <a href="#misc" title="covered by our integration test suite">✨</a></td>
       <td style="text-align:right">✅</td>
    </tr>
    <tr>
      <td>CreateDatastore <a href="#misc" title="covered by our integration test suite">✨</a></td>
       <td style="text-align:right">✅</td>
    </tr>
    <tr>
      <td>CreatePipeline <a href="#misc" title="covered by our integration test suite">✨</a></td>
       <td style="text-align:right">✅</td>
    </tr>
    <tr>
      <td>DeleteChannel <a href="#misc" title="covered by our integration test suite">✨</a></td>
       <td style="text-align:right">✅</td>
    </tr>
    <tr>
      <td>DeleteDataset <a href="#misc" title="covered by our integration test suite">✨</a></td>
       <td style="text-align:right">✅</td>
    </tr>
    <tr>
      <td>DeleteDatastore <a href="#misc" title="covered by our integration test suite">✨</a></td>
       <td style="text-align:right">✅</td>
    </tr>
    <tr>
      <td>DeletePipeline <a href="#misc" title="covered by our integration test suite">✨</a></td>
       <td style="text-align:right">✅</td>
    </tr>
    <tr>
      <td>DescribeChannel <a href="#misc" title="covered by our integration test suite">✨</a></td>
       <td style="text-align:right">✅</td>
    </tr>
    <tr>
      <td>DescribeDataset <a href="#misc" title="covered by our integration test suite">✨</a></td>
       <td style="text-align:right">✅</td>
    </tr>
    <tr>
      <td>DescribeDatastore <a href="#misc" title="covered by our integration test suite">✨</a></td>
       <td style="text-align:right">✅</td>
    </tr>
    <tr>
      <td>DescribePipeline <a href="#misc" title="covered by our integration test suite">✨</a></td>
       <td style="text-align:right">✅</td>
    </tr>
    <tr>
      <td>ListChannels <a href="#misc" title="covered by our integration test suite">✨</a></td>
       <td style="text-align:right">✅</td>
    </tr>
    <tr>
      <td>ListDatasetContents</td>
       <td style="text-align:right">✅</td>
    </tr>
    <tr>
      <td>ListDatasets <a href="#misc" title="covered by our integration test suite">✨</a></td>
       <td style="text-align:right">✅</td>
    </tr>
    <tr>
      <td>ListDatastores <a href="#misc" title="covered by our integration test suite">✨</a></td>
       <td style="text-align:right">✅</td>
    </tr>
    <tr>
      <td>ListPipelines <a href="#misc" title="covered by our integration test suite">✨</a></td>
       <td style="text-align:right">✅</td>
    </tr>
    <tr>
      <td>SampleChannelData</td>
       <td style="text-align:right">✅</td>
    </tr>
    <tr>
      <td><a data-toggle="collapse" href=".acm-notimplemented">Show more</a></td>
      <td style="text-align:right"></td>
    </tr>
    <tr class="collapse acm-notimplemented">
      <td>BatchPutMessage</td>
       <td style="text-align:right">-</td>
    </tr>
    <tr class="collapse acm-notimplemented">
      <td>CancelPipelineReprocessing</td>
       <td style="text-align:right">-</td>
    </tr>
    <tr class="collapse acm-notimplemented">
      <td>CreateDatasetContent</td>
       <td style="text-align:right">-</td>
    </tr>
    <tr class="collapse acm-notimplemented">
      <td>DeleteDatasetContent</td>
       <td style="text-align:right">-</td>
    </tr>
    <tr class="collapse acm-notimplemented">
      <td>DescribeLoggingOptions</td>
       <td style="text-align:right">-</td>
    </tr>
    <tr class="collapse acm-notimplemented">
      <td>GetDatasetContent</td>
       <td style="text-align:right">-</td>
    </tr>
    <tr class="collapse acm-notimplemented">
      <td>ListTagsForResource</td>
       <td style="text-align:right">-</td>
    </tr>
    <tr class="collapse acm-notimplemented">
      <td>PutLoggingOptions</td>
       <td style="text-align:right">-</td>
    </tr>
    <tr class="collapse acm-notimplemented">
      <td>RunPipelineActivity</td>
       <td style="text-align:right">-</td>
    </tr>
    <tr class="collapse acm-notimplemented">
      <td>StartPipelineReprocessing</td>
       <td style="text-align:right">-</td>
    </tr>
    <tr class="collapse acm-notimplemented">
      <td>TagResource</td>
       <td style="text-align:right">-</td>
    </tr>
    <tr class="collapse acm-notimplemented">
      <td>UntagResource</td>
       <td style="text-align:right">-</td>
    </tr>
    <tr class="collapse acm-notimplemented">
      <td>UpdateChannel</td>
       <td style="text-align:right">-</td>
    </tr>
    <tr class="collapse acm-notimplemented">
      <td>UpdateDataset</td>
       <td style="text-align:right">-</td>
    </tr>
    <tr class="collapse acm-notimplemented">
      <td>UpdateDatastore</td>
       <td style="text-align:right">-</td>
    </tr>
    <tr class="collapse acm-notimplemented">
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
      <td>CreateDeviceProfile <a href="#misc" title="covered by our integration test suite">✨</a></td>
       <td style="text-align:right">✅</td>
    </tr>
    <tr>
      <td>CreateWirelessDevice <a href="#misc" title="covered by our integration test suite">✨</a></td>
       <td style="text-align:right">✅</td>
    </tr>
    <tr>
      <td>CreateWirelessGateway <a href="#misc" title="covered by our integration test suite">✨</a></td>
       <td style="text-align:right">✅</td>
    </tr>
    <tr>
      <td>DeleteDeviceProfile <a href="#misc" title="covered by our integration test suite">✨</a></td>
       <td style="text-align:right">✅</td>
    </tr>
    <tr>
      <td>DeleteWirelessDevice <a href="#misc" title="covered by our integration test suite">✨</a></td>
       <td style="text-align:right">✅</td>
    </tr>
    <tr>
      <td>DeleteWirelessGateway <a href="#misc" title="covered by our integration test suite">✨</a></td>
       <td style="text-align:right">✅</td>
    </tr>
    <tr>
      <td>GetDeviceProfile <a href="#misc" title="covered by our integration test suite">✨</a></td>
       <td style="text-align:right">✅</td>
    </tr>
    <tr>
      <td>GetWirelessDevice <a href="#misc" title="covered by our integration test suite">✨</a></td>
       <td style="text-align:right">✅</td>
    </tr>
    <tr>
      <td>GetWirelessGateway <a href="#misc" title="covered by our integration test suite">✨</a></td>
       <td style="text-align:right">✅</td>
    </tr>
    <tr>
      <td>ListDeviceProfiles <a href="#misc" title="covered by our integration test suite">✨</a></td>
       <td style="text-align:right">✅</td>
    </tr>
    <tr>
      <td>ListWirelessDevices <a href="#misc" title="covered by our integration test suite">✨</a></td>
       <td style="text-align:right">✅</td>
    </tr>
    <tr>
      <td>ListWirelessGateways <a href="#misc" title="covered by our integration test suite">✨</a></td>
       <td style="text-align:right">✅</td>
    </tr>
    <tr>
      <td>UpdateWirelessDevice</td>
       <td style="text-align:right">✅</td>
    </tr>
    <tr>
      <td>UpdateWirelessGateway</td>
       <td style="text-align:right">✅</td>
    </tr>
    <tr>
      <td><a data-toggle="collapse" href=".acm-notimplemented">Show more</a></td>
      <td style="text-align:right"></td>
    </tr>
    <tr class="collapse acm-notimplemented">
      <td>AssociateAwsAccountWithPartnerAccount</td>
       <td style="text-align:right">-</td>
    </tr>
    <tr class="collapse acm-notimplemented">
      <td>AssociateMulticastGroupWithFuotaTask</td>
       <td style="text-align:right">-</td>
    </tr>
    <tr class="collapse acm-notimplemented">
      <td>AssociateWirelessDeviceWithFuotaTask</td>
       <td style="text-align:right">-</td>
    </tr>
    <tr class="collapse acm-notimplemented">
      <td>AssociateWirelessDeviceWithMulticastGroup</td>
       <td style="text-align:right">-</td>
    </tr>
    <tr class="collapse acm-notimplemented">
      <td>AssociateWirelessDeviceWithThing</td>
       <td style="text-align:right">-</td>
    </tr>
    <tr class="collapse acm-notimplemented">
      <td>AssociateWirelessGatewayWithCertificate</td>
       <td style="text-align:right">-</td>
    </tr>
    <tr class="collapse acm-notimplemented">
      <td>AssociateWirelessGatewayWithThing</td>
       <td style="text-align:right">-</td>
    </tr>
    <tr class="collapse acm-notimplemented">
      <td>CancelMulticastGroupSession</td>
       <td style="text-align:right">-</td>
    </tr>
    <tr class="collapse acm-notimplemented">
      <td>CreateDestination</td>
       <td style="text-align:right">-</td>
    </tr>
    <tr class="collapse acm-notimplemented">
      <td>CreateFuotaTask</td>
       <td style="text-align:right">-</td>
    </tr>
    <tr class="collapse acm-notimplemented">
      <td>CreateMulticastGroup</td>
       <td style="text-align:right">-</td>
    </tr>
    <tr class="collapse acm-notimplemented">
      <td>CreateNetworkAnalyzerConfiguration</td>
       <td style="text-align:right">-</td>
    </tr>
    <tr class="collapse acm-notimplemented">
      <td>CreateServiceProfile</td>
       <td style="text-align:right">-</td>
    </tr>
    <tr class="collapse acm-notimplemented">
      <td>CreateWirelessGatewayTask</td>
       <td style="text-align:right">-</td>
    </tr>
    <tr class="collapse acm-notimplemented">
      <td>CreateWirelessGatewayTaskDefinition</td>
       <td style="text-align:right">-</td>
    </tr>
    <tr class="collapse acm-notimplemented">
      <td>DeleteDestination</td>
       <td style="text-align:right">-</td>
    </tr>
    <tr class="collapse acm-notimplemented">
      <td>DeleteFuotaTask</td>
       <td style="text-align:right">-</td>
    </tr>
    <tr class="collapse acm-notimplemented">
      <td>DeleteMulticastGroup</td>
       <td style="text-align:right">-</td>
    </tr>
    <tr class="collapse acm-notimplemented">
      <td>DeleteNetworkAnalyzerConfiguration</td>
       <td style="text-align:right">-</td>
    </tr>
    <tr class="collapse acm-notimplemented">
      <td>DeleteQueuedMessages</td>
       <td style="text-align:right">-</td>
    </tr>
    <tr class="collapse acm-notimplemented">
      <td>DeleteServiceProfile</td>
       <td style="text-align:right">-</td>
    </tr>
    <tr class="collapse acm-notimplemented">
      <td>DeleteWirelessGatewayTask</td>
       <td style="text-align:right">-</td>
    </tr>
    <tr class="collapse acm-notimplemented">
      <td>DeleteWirelessGatewayTaskDefinition</td>
       <td style="text-align:right">-</td>
    </tr>
    <tr class="collapse acm-notimplemented">
      <td>DisassociateAwsAccountFromPartnerAccount</td>
       <td style="text-align:right">-</td>
    </tr>
    <tr class="collapse acm-notimplemented">
      <td>DisassociateMulticastGroupFromFuotaTask</td>
       <td style="text-align:right">-</td>
    </tr>
    <tr class="collapse acm-notimplemented">
      <td>DisassociateWirelessDeviceFromFuotaTask</td>
       <td style="text-align:right">-</td>
    </tr>
    <tr class="collapse acm-notimplemented">
      <td>DisassociateWirelessDeviceFromMulticastGroup</td>
       <td style="text-align:right">-</td>
    </tr>
    <tr class="collapse acm-notimplemented">
      <td>DisassociateWirelessDeviceFromThing</td>
       <td style="text-align:right">-</td>
    </tr>
    <tr class="collapse acm-notimplemented">
      <td>DisassociateWirelessGatewayFromCertificate</td>
       <td style="text-align:right">-</td>
    </tr>
    <tr class="collapse acm-notimplemented">
      <td>DisassociateWirelessGatewayFromThing</td>
       <td style="text-align:right">-</td>
    </tr>
    <tr class="collapse acm-notimplemented">
      <td>GetDestination</td>
       <td style="text-align:right">-</td>
    </tr>
    <tr class="collapse acm-notimplemented">
      <td>GetEventConfigurationByResourceTypes</td>
       <td style="text-align:right">-</td>
    </tr>
    <tr class="collapse acm-notimplemented">
      <td>GetFuotaTask</td>
       <td style="text-align:right">-</td>
    </tr>
    <tr class="collapse acm-notimplemented">
      <td>GetLogLevelsByResourceTypes</td>
       <td style="text-align:right">-</td>
    </tr>
    <tr class="collapse acm-notimplemented">
      <td>GetMulticastGroup</td>
       <td style="text-align:right">-</td>
    </tr>
    <tr class="collapse acm-notimplemented">
      <td>GetMulticastGroupSession</td>
       <td style="text-align:right">-</td>
    </tr>
    <tr class="collapse acm-notimplemented">
      <td>GetNetworkAnalyzerConfiguration</td>
       <td style="text-align:right">-</td>
    </tr>
    <tr class="collapse acm-notimplemented">
      <td>GetPartnerAccount</td>
       <td style="text-align:right">-</td>
    </tr>
    <tr class="collapse acm-notimplemented">
      <td>GetResourceEventConfiguration</td>
       <td style="text-align:right">-</td>
    </tr>
    <tr class="collapse acm-notimplemented">
      <td>GetResourceLogLevel</td>
       <td style="text-align:right">-</td>
    </tr>
    <tr class="collapse acm-notimplemented">
      <td>GetServiceEndpoint</td>
       <td style="text-align:right">-</td>
    </tr>
    <tr class="collapse acm-notimplemented">
      <td>GetServiceProfile</td>
       <td style="text-align:right">-</td>
    </tr>
    <tr class="collapse acm-notimplemented">
      <td>GetWirelessDeviceStatistics</td>
       <td style="text-align:right">-</td>
    </tr>
    <tr class="collapse acm-notimplemented">
      <td>GetWirelessGatewayCertificate</td>
       <td style="text-align:right">-</td>
    </tr>
    <tr class="collapse acm-notimplemented">
      <td>GetWirelessGatewayFirmwareInformation</td>
       <td style="text-align:right">-</td>
    </tr>
    <tr class="collapse acm-notimplemented">
      <td>GetWirelessGatewayStatistics</td>
       <td style="text-align:right">-</td>
    </tr>
    <tr class="collapse acm-notimplemented">
      <td>GetWirelessGatewayTask</td>
       <td style="text-align:right">-</td>
    </tr>
    <tr class="collapse acm-notimplemented">
      <td>GetWirelessGatewayTaskDefinition</td>
       <td style="text-align:right">-</td>
    </tr>
    <tr class="collapse acm-notimplemented">
      <td>ListDestinations</td>
       <td style="text-align:right">-</td>
    </tr>
    <tr class="collapse acm-notimplemented">
      <td>ListEventConfigurations</td>
       <td style="text-align:right">-</td>
    </tr>
    <tr class="collapse acm-notimplemented">
      <td>ListFuotaTasks</td>
       <td style="text-align:right">-</td>
    </tr>
    <tr class="collapse acm-notimplemented">
      <td>ListMulticastGroups</td>
       <td style="text-align:right">-</td>
    </tr>
    <tr class="collapse acm-notimplemented">
      <td>ListMulticastGroupsByFuotaTask</td>
       <td style="text-align:right">-</td>
    </tr>
    <tr class="collapse acm-notimplemented">
      <td>ListNetworkAnalyzerConfigurations</td>
       <td style="text-align:right">-</td>
    </tr>
    <tr class="collapse acm-notimplemented">
      <td>ListPartnerAccounts</td>
       <td style="text-align:right">-</td>
    </tr>
    <tr class="collapse acm-notimplemented">
      <td>ListQueuedMessages</td>
       <td style="text-align:right">-</td>
    </tr>
    <tr class="collapse acm-notimplemented">
      <td>ListServiceProfiles</td>
       <td style="text-align:right">-</td>
    </tr>
    <tr class="collapse acm-notimplemented">
      <td>ListTagsForResource</td>
       <td style="text-align:right">-</td>
    </tr>
    <tr class="collapse acm-notimplemented">
      <td>ListWirelessGatewayTaskDefinitions</td>
       <td style="text-align:right">-</td>
    </tr>
    <tr class="collapse acm-notimplemented">
      <td>PutResourceLogLevel</td>
       <td style="text-align:right">-</td>
    </tr>
    <tr class="collapse acm-notimplemented">
      <td>ResetAllResourceLogLevels</td>
       <td style="text-align:right">-</td>
    </tr>
    <tr class="collapse acm-notimplemented">
      <td>ResetResourceLogLevel</td>
       <td style="text-align:right">-</td>
    </tr>
    <tr class="collapse acm-notimplemented">
      <td>SendDataToMulticastGroup</td>
       <td style="text-align:right">-</td>
    </tr>
    <tr class="collapse acm-notimplemented">
      <td>SendDataToWirelessDevice</td>
       <td style="text-align:right">-</td>
    </tr>
    <tr class="collapse acm-notimplemented">
      <td>StartBulkAssociateWirelessDeviceWithMulticastGroup</td>
       <td style="text-align:right">-</td>
    </tr>
    <tr class="collapse acm-notimplemented">
      <td>StartBulkDisassociateWirelessDeviceFromMulticastGroup</td>
       <td style="text-align:right">-</td>
    </tr>
    <tr class="collapse acm-notimplemented">
      <td>StartFuotaTask</td>
       <td style="text-align:right">-</td>
    </tr>
    <tr class="collapse acm-notimplemented">
      <td>StartMulticastGroupSession</td>
       <td style="text-align:right">-</td>
    </tr>
    <tr class="collapse acm-notimplemented">
      <td>TagResource</td>
       <td style="text-align:right">-</td>
    </tr>
    <tr class="collapse acm-notimplemented">
      <td>TestWirelessDevice</td>
       <td style="text-align:right">-</td>
    </tr>
    <tr class="collapse acm-notimplemented">
      <td>UntagResource</td>
       <td style="text-align:right">-</td>
    </tr>
    <tr class="collapse acm-notimplemented">
      <td>UpdateDestination</td>
       <td style="text-align:right">-</td>
    </tr>
    <tr class="collapse acm-notimplemented">
      <td>UpdateEventConfigurationByResourceTypes</td>
       <td style="text-align:right">-</td>
    </tr>
    <tr class="collapse acm-notimplemented">
      <td>UpdateFuotaTask</td>
       <td style="text-align:right">-</td>
    </tr>
    <tr class="collapse acm-notimplemented">
      <td>UpdateLogLevelsByResourceTypes</td>
       <td style="text-align:right">-</td>
    </tr>
    <tr class="collapse acm-notimplemented">
      <td>UpdateMulticastGroup</td>
       <td style="text-align:right">-</td>
    </tr>
    <tr class="collapse acm-notimplemented">
      <td>UpdateNetworkAnalyzerConfiguration</td>
       <td style="text-align:right">-</td>
    </tr>
    <tr class="collapse acm-notimplemented">
      <td>UpdatePartnerAccount</td>
       <td style="text-align:right">-</td>
    </tr>
    <tr class="collapse acm-notimplemented">
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
      <td>CreateCluster <a href="#misc" title="covered by our integration test suite">✨</a></td>
       <td style="text-align:right">✅</td>
    </tr>
    <tr>
      <td>CreateConfiguration <a href="#misc" title="covered by our integration test suite">✨</a></td>
       <td style="text-align:right">✅</td>
    </tr>
    <tr>
      <td>DeleteCluster <a href="#misc" title="covered by our integration test suite">✨</a></td>
       <td style="text-align:right">✅</td>
    </tr>
    <tr>
      <td>DeleteConfiguration <a href="#misc" title="covered by our integration test suite">✨</a></td>
       <td style="text-align:right">✅</td>
    </tr>
    <tr>
      <td>DescribeCluster <a href="#misc" title="covered by our integration test suite">✨</a></td>
       <td style="text-align:right">✅</td>
    </tr>
    <tr>
      <td>DescribeClusterOperation</td>
       <td style="text-align:right">✅</td>
    </tr>
    <tr>
      <td>DescribeConfiguration <a href="#misc" title="covered by our integration test suite">✨</a></td>
       <td style="text-align:right">✅</td>
    </tr>
    <tr>
      <td>DescribeConfigurationRevision <a href="#misc" title="covered by our integration test suite">✨</a></td>
       <td style="text-align:right">✅</td>
    </tr>
    <tr>
      <td>GetBootstrapBrokers <a href="#misc" title="covered by our integration test suite">✨</a></td>
       <td style="text-align:right">✅</td>
    </tr>
    <tr>
      <td>ListClusters <a href="#misc" title="covered by our integration test suite">✨</a></td>
       <td style="text-align:right">✅</td>
    </tr>
    <tr>
      <td>ListConfigurationRevisions <a href="#misc" title="covered by our integration test suite">✨</a></td>
       <td style="text-align:right">✅</td>
    </tr>
    <tr>
      <td>ListConfigurations <a href="#misc" title="covered by our integration test suite">✨</a></td>
       <td style="text-align:right">✅</td>
    </tr>
    <tr>
      <td>ListNodes <a href="#misc" title="covered by our integration test suite">✨</a></td>
       <td style="text-align:right">✅</td>
    </tr>
    <tr>
      <td>UpdateClusterConfiguration</td>
       <td style="text-align:right">✅</td>
    </tr>
    <tr>
      <td>UpdateClusterKafkaVersion</td>
       <td style="text-align:right">✅</td>
    </tr>
    <tr>
      <td>UpdateConfiguration <a href="#misc" title="covered by our integration test suite">✨</a></td>
       <td style="text-align:right">✅</td>
    </tr>
    <tr>
      <td><a data-toggle="collapse" href=".acm-notimplemented">Show more</a></td>
      <td style="text-align:right"></td>
    </tr>
    <tr class="collapse acm-notimplemented">
      <td>BatchAssociateScramSecret</td>
       <td style="text-align:right">-</td>
    </tr>
    <tr class="collapse acm-notimplemented">
      <td>BatchDisassociateScramSecret</td>
       <td style="text-align:right">-</td>
    </tr>
    <tr class="collapse acm-notimplemented">
      <td>CreateClusterV2</td>
       <td style="text-align:right">-</td>
    </tr>
    <tr class="collapse acm-notimplemented">
      <td>DescribeClusterV2</td>
       <td style="text-align:right">-</td>
    </tr>
    <tr class="collapse acm-notimplemented">
      <td>GetCompatibleKafkaVersions</td>
       <td style="text-align:right">-</td>
    </tr>
    <tr class="collapse acm-notimplemented">
      <td>ListClusterOperations</td>
       <td style="text-align:right">-</td>
    </tr>
    <tr class="collapse acm-notimplemented">
      <td>ListClustersV2</td>
       <td style="text-align:right">-</td>
    </tr>
    <tr class="collapse acm-notimplemented">
      <td>ListKafkaVersions</td>
       <td style="text-align:right">-</td>
    </tr>
    <tr class="collapse acm-notimplemented">
      <td>ListScramSecrets</td>
       <td style="text-align:right">-</td>
    </tr>
    <tr class="collapse acm-notimplemented">
      <td>ListTagsForResource</td>
       <td style="text-align:right">-</td>
    </tr>
    <tr class="collapse acm-notimplemented">
      <td>RebootBroker</td>
       <td style="text-align:right">-</td>
    </tr>
    <tr class="collapse acm-notimplemented">
      <td>TagResource</td>
       <td style="text-align:right">-</td>
    </tr>
    <tr class="collapse acm-notimplemented">
      <td>UntagResource</td>
       <td style="text-align:right">-</td>
    </tr>
    <tr class="collapse acm-notimplemented">
      <td>UpdateBrokerCount</td>
       <td style="text-align:right">-</td>
    </tr>
    <tr class="collapse acm-notimplemented">
      <td>UpdateBrokerStorage</td>
       <td style="text-align:right">-</td>
    </tr>
    <tr class="collapse acm-notimplemented">
      <td>UpdateBrokerType</td>
       <td style="text-align:right">-</td>
    </tr>
    <tr class="collapse acm-notimplemented">
      <td>UpdateConnectivity</td>
       <td style="text-align:right">-</td>
    </tr>
    <tr class="collapse acm-notimplemented">
      <td>UpdateMonitoring</td>
       <td style="text-align:right">-</td>
    </tr>
    <tr class="collapse acm-notimplemented">
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
      <td>AddTagsToStream</td>
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
      <td>ListTagsForStream</td>
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
      <td>AddApplicationInputProcessingConfiguration <a href="#misc" title="covered by our integration test suite">✨</a></td>
       <td style="text-align:right">✅</td>
    </tr>
    <tr>
      <td>AddApplicationOutput <a href="#misc" title="covered by our integration test suite">✨</a></td>
       <td style="text-align:right">✅</td>
    </tr>
    <tr>
      <td>CreateApplication <a href="#misc" title="covered by our integration test suite">✨</a></td>
       <td style="text-align:right">✅</td>
    </tr>
    <tr>
      <td>DeleteApplication <a href="#misc" title="covered by our integration test suite">✨</a></td>
       <td style="text-align:right">✅</td>
    </tr>
    <tr>
      <td>DeleteApplicationInputProcessingConfiguration <a href="#misc" title="covered by our integration test suite">✨</a></td>
       <td style="text-align:right">✅</td>
    </tr>
    <tr>
      <td>DescribeApplication <a href="#misc" title="covered by our integration test suite">✨</a></td>
       <td style="text-align:right">✅</td>
    </tr>
    <tr>
      <td>ListApplications <a href="#misc" title="covered by our integration test suite">✨</a></td>
       <td style="text-align:right">✅</td>
    </tr>
    <tr>
      <td>ListTagsForResource <a href="#misc" title="covered by our integration test suite">✨</a></td>
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
      <td>UpdateApplication <a href="#misc" title="covered by our integration test suite">✨</a></td>
       <td style="text-align:right">✅</td>
    </tr>
    <tr>
      <td><a data-toggle="collapse" href=".acm-notimplemented">Show more</a></td>
      <td style="text-align:right"></td>
    </tr>
    <tr class="collapse acm-notimplemented">
      <td>AddApplicationCloudWatchLoggingOption</td>
       <td style="text-align:right">-</td>
    </tr>
    <tr class="collapse acm-notimplemented">
      <td>AddApplicationInput</td>
       <td style="text-align:right">-</td>
    </tr>
    <tr class="collapse acm-notimplemented">
      <td>AddApplicationReferenceDataSource</td>
       <td style="text-align:right">-</td>
    </tr>
    <tr class="collapse acm-notimplemented">
      <td>DeleteApplicationCloudWatchLoggingOption</td>
       <td style="text-align:right">-</td>
    </tr>
    <tr class="collapse acm-notimplemented">
      <td>DeleteApplicationOutput</td>
       <td style="text-align:right">-</td>
    </tr>
    <tr class="collapse acm-notimplemented">
      <td>DeleteApplicationReferenceDataSource</td>
       <td style="text-align:right">-</td>
    </tr>
    <tr class="collapse acm-notimplemented">
      <td>DiscoverInputSchema</td>
       <td style="text-align:right">-</td>
    </tr>
    <tr class="collapse acm-notimplemented">
      <td>StartApplication</td>
       <td style="text-align:right">-</td>
    </tr>
    <tr class="collapse acm-notimplemented">
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
      <td>AddApplicationInputProcessingConfiguration <a href="#misc" title="covered by our integration test suite">✨</a></td>
       <td style="text-align:right">✅</td>
    </tr>
    <tr>
      <td>AddApplicationOutput <a href="#misc" title="covered by our integration test suite">✨</a></td>
       <td style="text-align:right">✅</td>
    </tr>
    <tr>
      <td>CreateApplication <a href="#misc" title="covered by our integration test suite">✨</a></td>
       <td style="text-align:right">✅</td>
    </tr>
    <tr>
      <td>DeleteApplication <a href="#misc" title="covered by our integration test suite">✨</a></td>
       <td style="text-align:right">✅</td>
    </tr>
    <tr>
      <td>DeleteApplicationInputProcessingConfiguration <a href="#misc" title="covered by our integration test suite">✨</a></td>
       <td style="text-align:right">✅</td>
    </tr>
    <tr>
      <td>DescribeApplication <a href="#misc" title="covered by our integration test suite">✨</a></td>
       <td style="text-align:right">✅</td>
    </tr>
    <tr>
      <td>ListApplications <a href="#misc" title="covered by our integration test suite">✨</a></td>
       <td style="text-align:right">✅</td>
    </tr>
    <tr>
      <td>ListTagsForResource <a href="#misc" title="covered by our integration test suite">✨</a></td>
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
      <td>UpdateApplication <a href="#misc" title="covered by our integration test suite">✨</a></td>
       <td style="text-align:right">✅</td>
    </tr>
    <tr>
      <td><a data-toggle="collapse" href=".acm-notimplemented">Show more</a></td>
      <td style="text-align:right"></td>
    </tr>
    <tr class="collapse acm-notimplemented">
      <td>AddApplicationCloudWatchLoggingOption</td>
       <td style="text-align:right">-</td>
    </tr>
    <tr class="collapse acm-notimplemented">
      <td>AddApplicationInput</td>
       <td style="text-align:right">-</td>
    </tr>
    <tr class="collapse acm-notimplemented">
      <td>AddApplicationReferenceDataSource</td>
       <td style="text-align:right">-</td>
    </tr>
    <tr class="collapse acm-notimplemented">
      <td>AddApplicationVpcConfiguration</td>
       <td style="text-align:right">-</td>
    </tr>
    <tr class="collapse acm-notimplemented">
      <td>CreateApplicationPresignedUrl</td>
       <td style="text-align:right">-</td>
    </tr>
    <tr class="collapse acm-notimplemented">
      <td>CreateApplicationSnapshot</td>
       <td style="text-align:right">-</td>
    </tr>
    <tr class="collapse acm-notimplemented">
      <td>DeleteApplicationCloudWatchLoggingOption</td>
       <td style="text-align:right">-</td>
    </tr>
    <tr class="collapse acm-notimplemented">
      <td>DeleteApplicationOutput</td>
       <td style="text-align:right">-</td>
    </tr>
    <tr class="collapse acm-notimplemented">
      <td>DeleteApplicationReferenceDataSource</td>
       <td style="text-align:right">-</td>
    </tr>
    <tr class="collapse acm-notimplemented">
      <td>DeleteApplicationSnapshot</td>
       <td style="text-align:right">-</td>
    </tr>
    <tr class="collapse acm-notimplemented">
      <td>DeleteApplicationVpcConfiguration</td>
       <td style="text-align:right">-</td>
    </tr>
    <tr class="collapse acm-notimplemented">
      <td>DescribeApplicationSnapshot</td>
       <td style="text-align:right">-</td>
    </tr>
    <tr class="collapse acm-notimplemented">
      <td>DescribeApplicationVersion</td>
       <td style="text-align:right">-</td>
    </tr>
    <tr class="collapse acm-notimplemented">
      <td>DiscoverInputSchema</td>
       <td style="text-align:right">-</td>
    </tr>
    <tr class="collapse acm-notimplemented">
      <td>ListApplicationSnapshots</td>
       <td style="text-align:right">-</td>
    </tr>
    <tr class="collapse acm-notimplemented">
      <td>ListApplicationVersions</td>
       <td style="text-align:right">-</td>
    </tr>
    <tr class="collapse acm-notimplemented">
      <td>RollbackApplication</td>
       <td style="text-align:right">-</td>
    </tr>
    <tr class="collapse acm-notimplemented">
      <td>StartApplication</td>
       <td style="text-align:right">-</td>
    </tr>
    <tr class="collapse acm-notimplemented">
      <td>StopApplication</td>
       <td style="text-align:right">-</td>
    </tr>
    <tr class="collapse acm-notimplemented">
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
      <td>CancelKeyDeletion</td>
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
      <td>EnableKeyRotation</td>
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
      <td>GenerateDataKeyWithoutPlaintext</td>
       <td style="text-align:right">✅</td>
    </tr>
    <tr>
      <td>GenerateRandom</td>
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
      <td>ListKeyPolicies</td>
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
      <td>ListRetirableGrants</td>
       <td style="text-align:right">✅</td>
    </tr>
    <tr>
      <td>PutKeyPolicy</td>
       <td style="text-align:right">✅</td>
    </tr>
    <tr>
      <td>ReEncrypt</td>
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
      <td>UpdateKeyDescription</td>
       <td style="text-align:right">✅</td>
    </tr>
    <tr>
      <td><a data-toggle="collapse" href=".acm-notimplemented">Show more</a></td>
      <td style="text-align:right"></td>
    </tr>
    <tr class="collapse acm-notimplemented">
      <td>ConnectCustomKeyStore</td>
       <td style="text-align:right">-</td>
    </tr>
    <tr class="collapse acm-notimplemented">
      <td>CreateCustomKeyStore</td>
       <td style="text-align:right">-</td>
    </tr>
    <tr class="collapse acm-notimplemented">
      <td>DeleteCustomKeyStore</td>
       <td style="text-align:right">-</td>
    </tr>
    <tr class="collapse acm-notimplemented">
      <td>DeleteImportedKeyMaterial</td>
       <td style="text-align:right">-</td>
    </tr>
    <tr class="collapse acm-notimplemented">
      <td>DescribeCustomKeyStores</td>
       <td style="text-align:right">-</td>
    </tr>
    <tr class="collapse acm-notimplemented">
      <td>DisconnectCustomKeyStore</td>
       <td style="text-align:right">-</td>
    </tr>
    <tr class="collapse acm-notimplemented">
      <td>GenerateMac</td>
       <td style="text-align:right">-</td>
    </tr>
    <tr class="collapse acm-notimplemented">
      <td>ReplicateKey</td>
       <td style="text-align:right">-</td>
    </tr>
    <tr class="collapse acm-notimplemented">
      <td>UpdateCustomKeyStore</td>
       <td style="text-align:right">-</td>
    </tr>
    <tr class="collapse acm-notimplemented">
      <td>UpdatePrimaryRegion</td>
       <td style="text-align:right">-</td>
    </tr>
    <tr class="collapse acm-notimplemented">
      <td>Verify</td>
       <td style="text-align:right">-</td>
    </tr>
    <tr class="collapse acm-notimplemented">
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
      <td>DeregisterResource</td>
       <td style="text-align:right">✅</td>
    </tr>
    <tr>
      <td>DescribeResource</td>
       <td style="text-align:right">✅</td>
    </tr>
    <tr>
      <td>GetDataLakeSettings</td>
       <td style="text-align:right">✅</td>
    </tr>
    <tr>
      <td>GrantPermissions <a href="#misc" title="covered by our integration test suite">✨</a></td>
       <td style="text-align:right">✅</td>
    </tr>
    <tr>
      <td>ListPermissions <a href="#misc" title="covered by our integration test suite">✨</a></td>
       <td style="text-align:right">✅</td>
    </tr>
    <tr>
      <td>ListResources</td>
       <td style="text-align:right">✅</td>
    </tr>
    <tr>
      <td>PutDataLakeSettings</td>
       <td style="text-align:right">✅</td>
    </tr>
    <tr>
      <td>RegisterResource</td>
       <td style="text-align:right">✅</td>
    </tr>
    <tr>
      <td>RevokePermissions</td>
       <td style="text-align:right">✅</td>
    </tr>
    <tr>
      <td><a data-toggle="collapse" href=".acm-notimplemented">Show more</a></td>
      <td style="text-align:right"></td>
    </tr>
    <tr class="collapse acm-notimplemented">
      <td>AddLFTagsToResource</td>
       <td style="text-align:right">-</td>
    </tr>
    <tr class="collapse acm-notimplemented">
      <td>BatchGrantPermissions</td>
       <td style="text-align:right">-</td>
    </tr>
    <tr class="collapse acm-notimplemented">
      <td>BatchRevokePermissions</td>
       <td style="text-align:right">-</td>
    </tr>
    <tr class="collapse acm-notimplemented">
      <td>CancelTransaction</td>
       <td style="text-align:right">-</td>
    </tr>
    <tr class="collapse acm-notimplemented">
      <td>CommitTransaction</td>
       <td style="text-align:right">-</td>
    </tr>
    <tr class="collapse acm-notimplemented">
      <td>CreateDataCellsFilter</td>
       <td style="text-align:right">-</td>
    </tr>
    <tr class="collapse acm-notimplemented">
      <td>CreateLFTag</td>
       <td style="text-align:right">-</td>
    </tr>
    <tr class="collapse acm-notimplemented">
      <td>DeleteDataCellsFilter</td>
       <td style="text-align:right">-</td>
    </tr>
    <tr class="collapse acm-notimplemented">
      <td>DeleteLFTag</td>
       <td style="text-align:right">-</td>
    </tr>
    <tr class="collapse acm-notimplemented">
      <td>DeleteObjectsOnCancel</td>
       <td style="text-align:right">-</td>
    </tr>
    <tr class="collapse acm-notimplemented">
      <td>DescribeTransaction</td>
       <td style="text-align:right">-</td>
    </tr>
    <tr class="collapse acm-notimplemented">
      <td>ExtendTransaction</td>
       <td style="text-align:right">-</td>
    </tr>
    <tr class="collapse acm-notimplemented">
      <td>GetEffectivePermissionsForPath</td>
       <td style="text-align:right">-</td>
    </tr>
    <tr class="collapse acm-notimplemented">
      <td>GetLFTag</td>
       <td style="text-align:right">-</td>
    </tr>
    <tr class="collapse acm-notimplemented">
      <td>GetQueryState</td>
       <td style="text-align:right">-</td>
    </tr>
    <tr class="collapse acm-notimplemented">
      <td>GetQueryStatistics</td>
       <td style="text-align:right">-</td>
    </tr>
    <tr class="collapse acm-notimplemented">
      <td>GetResourceLFTags</td>
       <td style="text-align:right">-</td>
    </tr>
    <tr class="collapse acm-notimplemented">
      <td>GetTableObjects</td>
       <td style="text-align:right">-</td>
    </tr>
    <tr class="collapse acm-notimplemented">
      <td>GetTemporaryGluePartitionCredentials</td>
       <td style="text-align:right">-</td>
    </tr>
    <tr class="collapse acm-notimplemented">
      <td>GetTemporaryGlueTableCredentials</td>
       <td style="text-align:right">-</td>
    </tr>
    <tr class="collapse acm-notimplemented">
      <td>GetWorkUnitResults</td>
       <td style="text-align:right">-</td>
    </tr>
    <tr class="collapse acm-notimplemented">
      <td>GetWorkUnits</td>
       <td style="text-align:right">-</td>
    </tr>
    <tr class="collapse acm-notimplemented">
      <td>ListDataCellsFilter</td>
       <td style="text-align:right">-</td>
    </tr>
    <tr class="collapse acm-notimplemented">
      <td>ListLFTags</td>
       <td style="text-align:right">-</td>
    </tr>
    <tr class="collapse acm-notimplemented">
      <td>ListTableStorageOptimizers</td>
       <td style="text-align:right">-</td>
    </tr>
    <tr class="collapse acm-notimplemented">
      <td>ListTransactions</td>
       <td style="text-align:right">-</td>
    </tr>
    <tr class="collapse acm-notimplemented">
      <td>RemoveLFTagsFromResource</td>
       <td style="text-align:right">-</td>
    </tr>
    <tr class="collapse acm-notimplemented">
      <td>SearchDatabasesByLFTags</td>
       <td style="text-align:right">-</td>
    </tr>
    <tr class="collapse acm-notimplemented">
      <td>SearchTablesByLFTags</td>
       <td style="text-align:right">-</td>
    </tr>
    <tr class="collapse acm-notimplemented">
      <td>StartQueryPlanning</td>
       <td style="text-align:right">-</td>
    </tr>
    <tr class="collapse acm-notimplemented">
      <td>StartTransaction</td>
       <td style="text-align:right">-</td>
    </tr>
    <tr class="collapse acm-notimplemented">
      <td>UpdateLFTag</td>
       <td style="text-align:right">-</td>
    </tr>
    <tr class="collapse acm-notimplemented">
      <td>UpdateResource</td>
       <td style="text-align:right">-</td>
    </tr>
    <tr class="collapse acm-notimplemented">
      <td>UpdateTableObjects</td>
       <td style="text-align:right">-</td>
    </tr>
    <tr class="collapse acm-notimplemented">
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
      <td>AddLayerVersionPermission</td>
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
      <td>DeleteAlias</td>
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
      <td>DeleteFunctionCodeSigningConfig <a href="#misc" title="covered by our integration test suite">✨</a></td>
       <td style="text-align:right">✅</td>
    </tr>
    <tr>
      <td>DeleteFunctionConcurrency <a href="#misc" title="covered by our integration test suite">✨</a></td>
       <td style="text-align:right">✅</td>
    </tr>
    <tr>
      <td>DeleteFunctionEventInvokeConfig <a href="#misc" title="covered by our integration test suite">✨</a></td>
       <td style="text-align:right">✅</td>
    </tr>
    <tr>
      <td>DeleteLayerVersion <a href="#misc" title="covered by our integration test suite">✨</a></td>
       <td style="text-align:right">✅</td>
    </tr>
    <tr>
      <td>GetAlias</td>
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
      <td>GetFunctionCodeSigningConfig <a href="#misc" title="covered by our integration test suite">✨</a></td>
       <td style="text-align:right">✅</td>
    </tr>
    <tr>
      <td>GetFunctionConcurrency <a href="#misc" title="covered by our integration test suite">✨</a></td>
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
      <td>GetLayerVersion <a href="#misc" title="covered by our integration test suite">✨</a></td>
       <td style="text-align:right">✅</td>
    </tr>
    <tr>
      <td>GetLayerVersionByArn</td>
       <td style="text-align:right">✅</td>
    </tr>
    <tr>
      <td>GetLayerVersionPolicy</td>
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
      <td>ListLayerVersions <a href="#misc" title="covered by our integration test suite">✨</a></td>
       <td style="text-align:right">✅</td>
    </tr>
    <tr>
      <td>ListLayers <a href="#misc" title="covered by our integration test suite">✨</a></td>
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
      <td>PublishLayerVersion <a href="#misc" title="covered by our integration test suite">✨</a></td>
       <td style="text-align:right">✅</td>
    </tr>
    <tr>
      <td>PublishVersion</td>
       <td style="text-align:right">✅</td>
    </tr>
    <tr>
      <td>PutFunctionCodeSigningConfig <a href="#misc" title="covered by our integration test suite">✨</a></td>
       <td style="text-align:right">✅</td>
    </tr>
    <tr>
      <td>PutFunctionConcurrency <a href="#misc" title="covered by our integration test suite">✨</a></td>
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
      <td>UpdateCodeSigningConfig <a href="#misc" title="covered by our integration test suite">✨</a></td>
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
      <td>UpdateFunctionEventInvokeConfig <a href="#misc" title="covered by our integration test suite">✨</a></td>
       <td style="text-align:right">✅</td>
    </tr>
    <tr>
      <td><a data-toggle="collapse" href=".acm-notimplemented">Show more</a></td>
      <td style="text-align:right"></td>
    </tr>
    <tr class="collapse acm-notimplemented">
      <td>CreateFunctionUrlConfig</td>
       <td style="text-align:right">-</td>
    </tr>
    <tr class="collapse acm-notimplemented">
      <td>DeleteFunctionUrlConfig</td>
       <td style="text-align:right">-</td>
    </tr>
    <tr class="collapse acm-notimplemented">
      <td>DeleteProvisionedConcurrencyConfig</td>
       <td style="text-align:right">-</td>
    </tr>
    <tr class="collapse acm-notimplemented">
      <td>GetAccountSettings</td>
       <td style="text-align:right">-</td>
    </tr>
    <tr class="collapse acm-notimplemented">
      <td>GetFunctionUrlConfig</td>
       <td style="text-align:right">-</td>
    </tr>
    <tr class="collapse acm-notimplemented">
      <td>GetProvisionedConcurrencyConfig</td>
       <td style="text-align:right">-</td>
    </tr>
    <tr class="collapse acm-notimplemented">
      <td>InvokeAsync</td>
       <td style="text-align:right">-</td>
    </tr>
    <tr class="collapse acm-notimplemented">
      <td>ListFunctionEventInvokeConfigs</td>
       <td style="text-align:right">-</td>
    </tr>
    <tr class="collapse acm-notimplemented">
      <td>ListFunctionUrlConfigs</td>
       <td style="text-align:right">-</td>
    </tr>
    <tr class="collapse acm-notimplemented">
      <td>ListFunctionsByCodeSigningConfig</td>
       <td style="text-align:right">-</td>
    </tr>
    <tr class="collapse acm-notimplemented">
      <td>ListProvisionedConcurrencyConfigs</td>
       <td style="text-align:right">-</td>
    </tr>
    <tr class="collapse acm-notimplemented">
      <td>PutProvisionedConcurrencyConfig</td>
       <td style="text-align:right">-</td>
    </tr>
    <tr class="collapse acm-notimplemented">
      <td>RemoveLayerVersionPermission</td>
       <td style="text-align:right">-</td>
    </tr>
    <tr class="collapse acm-notimplemented">
      <td>UpdateFunctionUrlConfig</td>
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
    <tr>
      <td><a data-toggle="collapse" href=".acm-notimplemented">Show more</a></td>
      <td style="text-align:right"></td>
    </tr>
    <tr class="collapse acm-notimplemented">
      <td>AssociateKmsKey</td>
       <td style="text-align:right">-</td>
    </tr>
    <tr class="collapse acm-notimplemented">
      <td>CancelExportTask</td>
       <td style="text-align:right">-</td>
    </tr>
    <tr class="collapse acm-notimplemented">
      <td>DeleteDestination</td>
       <td style="text-align:right">-</td>
    </tr>
    <tr class="collapse acm-notimplemented">
      <td>DeleteQueryDefinition</td>
       <td style="text-align:right">-</td>
    </tr>
    <tr class="collapse acm-notimplemented">
      <td>DescribeDestinations</td>
       <td style="text-align:right">-</td>
    </tr>
    <tr class="collapse acm-notimplemented">
      <td>DescribeExportTasks</td>
       <td style="text-align:right">-</td>
    </tr>
    <tr class="collapse acm-notimplemented">
      <td>DescribeQueries</td>
       <td style="text-align:right">-</td>
    </tr>
    <tr class="collapse acm-notimplemented">
      <td>DescribeQueryDefinitions</td>
       <td style="text-align:right">-</td>
    </tr>
    <tr class="collapse acm-notimplemented">
      <td>DisassociateKmsKey</td>
       <td style="text-align:right">-</td>
    </tr>
    <tr class="collapse acm-notimplemented">
      <td>GetLogGroupFields</td>
       <td style="text-align:right">-</td>
    </tr>
    <tr class="collapse acm-notimplemented">
      <td>GetLogRecord</td>
       <td style="text-align:right">-</td>
    </tr>
    <tr class="collapse acm-notimplemented">
      <td>GetQueryResults</td>
       <td style="text-align:right">-</td>
    </tr>
    <tr class="collapse acm-notimplemented">
      <td>PutDestination</td>
       <td style="text-align:right">-</td>
    </tr>
    <tr class="collapse acm-notimplemented">
      <td>PutDestinationPolicy</td>
       <td style="text-align:right">-</td>
    </tr>
    <tr class="collapse acm-notimplemented">
      <td>PutQueryDefinition</td>
       <td style="text-align:right">-</td>
    </tr>
    <tr class="collapse acm-notimplemented">
      <td>StopQuery</td>
       <td style="text-align:right">-</td>
    </tr>
    <tr class="collapse acm-notimplemented">
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
      <td>CreateContainer <a href="#misc" title="covered by our integration test suite">✨</a></td>
       <td style="text-align:right">✅</td>
    </tr>
    <tr>
      <td>DeleteContainer <a href="#misc" title="covered by our integration test suite">✨</a></td>
       <td style="text-align:right">✅</td>
    </tr>
    <tr>
      <td>DescribeContainer <a href="#misc" title="covered by our integration test suite">✨</a></td>
       <td style="text-align:right">✅</td>
    </tr>
    <tr>
      <td>ListContainers <a href="#misc" title="covered by our integration test suite">✨</a></td>
       <td style="text-align:right">✅</td>
    </tr>
    <tr>
      <td><a data-toggle="collapse" href=".acm-notimplemented">Show more</a></td>
      <td style="text-align:right"></td>
    </tr>
    <tr class="collapse acm-notimplemented">
      <td>DeleteContainerPolicy</td>
       <td style="text-align:right">-</td>
    </tr>
    <tr class="collapse acm-notimplemented">
      <td>DeleteCorsPolicy</td>
       <td style="text-align:right">-</td>
    </tr>
    <tr class="collapse acm-notimplemented">
      <td>DeleteLifecyclePolicy</td>
       <td style="text-align:right">-</td>
    </tr>
    <tr class="collapse acm-notimplemented">
      <td>DeleteMetricPolicy</td>
       <td style="text-align:right">-</td>
    </tr>
    <tr class="collapse acm-notimplemented">
      <td>GetContainerPolicy</td>
       <td style="text-align:right">-</td>
    </tr>
    <tr class="collapse acm-notimplemented">
      <td>GetCorsPolicy</td>
       <td style="text-align:right">-</td>
    </tr>
    <tr class="collapse acm-notimplemented">
      <td>GetLifecyclePolicy</td>
       <td style="text-align:right">-</td>
    </tr>
    <tr class="collapse acm-notimplemented">
      <td>GetMetricPolicy</td>
       <td style="text-align:right">-</td>
    </tr>
    <tr class="collapse acm-notimplemented">
      <td>ListTagsForResource</td>
       <td style="text-align:right">-</td>
    </tr>
    <tr class="collapse acm-notimplemented">
      <td>PutContainerPolicy</td>
       <td style="text-align:right">-</td>
    </tr>
    <tr class="collapse acm-notimplemented">
      <td>PutCorsPolicy</td>
       <td style="text-align:right">-</td>
    </tr>
    <tr class="collapse acm-notimplemented">
      <td>PutLifecyclePolicy</td>
       <td style="text-align:right">-</td>
    </tr>
    <tr class="collapse acm-notimplemented">
      <td>PutMetricPolicy</td>
       <td style="text-align:right">-</td>
    </tr>
    <tr class="collapse acm-notimplemented">
      <td>StartAccessLogging</td>
       <td style="text-align:right">-</td>
    </tr>
    <tr class="collapse acm-notimplemented">
      <td>StopAccessLogging</td>
       <td style="text-align:right">-</td>
    </tr>
    <tr class="collapse acm-notimplemented">
      <td>TagResource</td>
       <td style="text-align:right">-</td>
    </tr>
    <tr class="collapse acm-notimplemented">
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
      <td>DeleteObject <a href="#misc" title="covered by our integration test suite">✨</a></td>
       <td style="text-align:right">✅</td>
    </tr>
    <tr>
      <td>DescribeObject <a href="#misc" title="covered by our integration test suite">✨</a></td>
       <td style="text-align:right">✅</td>
    </tr>
    <tr>
      <td>GetObject <a href="#misc" title="covered by our integration test suite">✨</a></td>
       <td style="text-align:right">✅</td>
    </tr>
    <tr>
      <td>PutObject <a href="#misc" title="covered by our integration test suite">✨</a></td>
       <td style="text-align:right">✅</td>
    </tr>
    <tr>
      <td><a data-toggle="collapse" href=".acm-notimplemented">Show more</a></td>
      <td style="text-align:right"></td>
    </tr>
    <tr class="collapse acm-notimplemented">
      <td>ListItems</td>
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
      <td>CreateEnvironment</td>
       <td style="text-align:right">✅</td>
    </tr>
    <tr>
      <td>DeleteEnvironment</td>
       <td style="text-align:right">✅</td>
    </tr>
    <tr>
      <td>GetEnvironment</td>
       <td style="text-align:right">✅</td>
    </tr>
    <tr>
      <td>ListEnvironments <a href="#misc" title="covered by our integration test suite">✨</a></td>
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
      <td>UpdateEnvironment</td>
       <td style="text-align:right">✅</td>
    </tr>
    <tr>
      <td><a data-toggle="collapse" href=".acm-notimplemented">Show more</a></td>
      <td style="text-align:right"></td>
    </tr>
    <tr class="collapse acm-notimplemented">
      <td>CreateCliToken</td>
       <td style="text-align:right">-</td>
    </tr>
    <tr class="collapse acm-notimplemented">
      <td>CreateWebLoginToken</td>
       <td style="text-align:right">-</td>
    </tr>
    <tr class="collapse acm-notimplemented">
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
      <td>AddTagsToResource</td>
       <td style="text-align:right">✅</td>
    </tr>
    <tr>
      <td>CopyDBClusterSnapshot</td>
       <td style="text-align:right">✅</td>
    </tr>
    <tr>
      <td>CreateDBCluster</td>
       <td style="text-align:right">✅</td>
    </tr>
    <tr>
      <td>CreateDBClusterEndpoint</td>
       <td style="text-align:right">✅</td>
    </tr>
    <tr>
      <td>CreateDBClusterParameterGroup</td>
       <td style="text-align:right">✅</td>
    </tr>
    <tr>
      <td>CreateDBClusterSnapshot</td>
       <td style="text-align:right">✅</td>
    </tr>
    <tr>
      <td>CreateDBInstance</td>
       <td style="text-align:right">✅</td>
    </tr>
    <tr>
      <td>CreateDBParameterGroup</td>
       <td style="text-align:right">✅</td>
    </tr>
    <tr>
      <td>CreateDBSubnetGroup</td>
       <td style="text-align:right">✅</td>
    </tr>
    <tr>
      <td>CreateEventSubscription</td>
       <td style="text-align:right">✅</td>
    </tr>
    <tr>
      <td>DeleteDBCluster</td>
       <td style="text-align:right">✅</td>
    </tr>
    <tr>
      <td>DeleteDBClusterEndpoint</td>
       <td style="text-align:right">✅</td>
    </tr>
    <tr>
      <td>DeleteDBClusterParameterGroup</td>
       <td style="text-align:right">✅</td>
    </tr>
    <tr>
      <td>DeleteDBClusterSnapshot</td>
       <td style="text-align:right">✅</td>
    </tr>
    <tr>
      <td>DeleteDBInstance</td>
       <td style="text-align:right">✅</td>
    </tr>
    <tr>
      <td>DeleteDBParameterGroup</td>
       <td style="text-align:right">✅</td>
    </tr>
    <tr>
      <td>DeleteDBSubnetGroup</td>
       <td style="text-align:right">✅</td>
    </tr>
    <tr>
      <td>DeleteEventSubscription</td>
       <td style="text-align:right">✅</td>
    </tr>
    <tr>
      <td>DescribeDBClusterEndpoints</td>
       <td style="text-align:right">✅</td>
    </tr>
    <tr>
      <td>DescribeDBClusterParameterGroups</td>
       <td style="text-align:right">✅</td>
    </tr>
    <tr>
      <td>DescribeDBClusterParameters</td>
       <td style="text-align:right">✅</td>
    </tr>
    <tr>
      <td>DescribeDBClusterSnapshots</td>
       <td style="text-align:right">✅</td>
    </tr>
    <tr>
      <td>DescribeDBClusters</td>
       <td style="text-align:right">✅</td>
    </tr>
    <tr>
      <td>DescribeDBEngineVersions</td>
       <td style="text-align:right">✅</td>
    </tr>
    <tr>
      <td>DescribeDBInstances</td>
       <td style="text-align:right">✅</td>
    </tr>
    <tr>
      <td>DescribeDBParameterGroups</td>
       <td style="text-align:right">✅</td>
    </tr>
    <tr>
      <td>DescribeDBParameters</td>
       <td style="text-align:right">✅</td>
    </tr>
    <tr>
      <td>DescribeDBSubnetGroups</td>
       <td style="text-align:right">✅</td>
    </tr>
    <tr>
      <td>DescribeEventSubscriptions</td>
       <td style="text-align:right">✅</td>
    </tr>
    <tr>
      <td>DescribeGlobalClusters</td>
       <td style="text-align:right">✅</td>
    </tr>
    <tr>
      <td>ListTagsForResource</td>
       <td style="text-align:right">✅</td>
    </tr>
    <tr>
      <td>ModifyDBCluster</td>
       <td style="text-align:right">✅</td>
    </tr>
    <tr>
      <td>ModifyDBClusterEndpoint</td>
       <td style="text-align:right">✅</td>
    </tr>
    <tr>
      <td>ModifyDBClusterParameterGroup</td>
       <td style="text-align:right">✅</td>
    </tr>
    <tr>
      <td>ModifyDBInstance</td>
       <td style="text-align:right">✅</td>
    </tr>
    <tr>
      <td>ModifyDBParameterGroup</td>
       <td style="text-align:right">✅</td>
    </tr>
    <tr>
      <td>ModifyDBSubnetGroup</td>
       <td style="text-align:right">✅</td>
    </tr>
    <tr>
      <td>RebootDBInstance</td>
       <td style="text-align:right">✅</td>
    </tr>
    <tr>
      <td>RemoveTagsFromResource</td>
       <td style="text-align:right">✅</td>
    </tr>
    <tr>
      <td>ResetDBClusterParameterGroup</td>
       <td style="text-align:right">✅</td>
    </tr>
    <tr>
      <td>RestoreDBClusterFromSnapshot</td>
       <td style="text-align:right">✅</td>
    </tr>
    <tr>
      <td>StartDBCluster</td>
       <td style="text-align:right">✅</td>
    </tr>
    <tr>
      <td>StopDBCluster</td>
       <td style="text-align:right">✅</td>
    </tr>
    <tr>
      <td><a data-toggle="collapse" href=".acm-notimplemented">Show more</a></td>
      <td style="text-align:right"></td>
    </tr>
    <tr class="collapse acm-notimplemented">
      <td>AddRoleToDBCluster</td>
       <td style="text-align:right">-</td>
    </tr>
    <tr class="collapse acm-notimplemented">
      <td>AddSourceIdentifierToSubscription</td>
       <td style="text-align:right">-</td>
    </tr>
    <tr class="collapse acm-notimplemented">
      <td>ApplyPendingMaintenanceAction</td>
       <td style="text-align:right">-</td>
    </tr>
    <tr class="collapse acm-notimplemented">
      <td>CopyDBClusterParameterGroup</td>
       <td style="text-align:right">-</td>
    </tr>
    <tr class="collapse acm-notimplemented">
      <td>CopyDBParameterGroup</td>
       <td style="text-align:right">-</td>
    </tr>
    <tr class="collapse acm-notimplemented">
      <td>CreateGlobalCluster</td>
       <td style="text-align:right">-</td>
    </tr>
    <tr class="collapse acm-notimplemented">
      <td>DeleteGlobalCluster</td>
       <td style="text-align:right">-</td>
    </tr>
    <tr class="collapse acm-notimplemented">
      <td>DescribeDBClusterSnapshotAttributes</td>
       <td style="text-align:right">-</td>
    </tr>
    <tr class="collapse acm-notimplemented">
      <td>DescribeEngineDefaultClusterParameters</td>
       <td style="text-align:right">-</td>
    </tr>
    <tr class="collapse acm-notimplemented">
      <td>DescribeEngineDefaultParameters</td>
       <td style="text-align:right">-</td>
    </tr>
    <tr class="collapse acm-notimplemented">
      <td>DescribeEventCategories</td>
       <td style="text-align:right">-</td>
    </tr>
    <tr class="collapse acm-notimplemented">
      <td>DescribeEvents</td>
       <td style="text-align:right">-</td>
    </tr>
    <tr class="collapse acm-notimplemented">
      <td>DescribeOrderableDBInstanceOptions</td>
       <td style="text-align:right">-</td>
    </tr>
    <tr class="collapse acm-notimplemented">
      <td>DescribePendingMaintenanceActions</td>
       <td style="text-align:right">-</td>
    </tr>
    <tr class="collapse acm-notimplemented">
      <td>DescribeValidDBInstanceModifications</td>
       <td style="text-align:right">-</td>
    </tr>
    <tr class="collapse acm-notimplemented">
      <td>FailoverDBCluster</td>
       <td style="text-align:right">-</td>
    </tr>
    <tr class="collapse acm-notimplemented">
      <td>FailoverGlobalCluster</td>
       <td style="text-align:right">-</td>
    </tr>
    <tr class="collapse acm-notimplemented">
      <td>ModifyDBClusterSnapshotAttribute</td>
       <td style="text-align:right">-</td>
    </tr>
    <tr class="collapse acm-notimplemented">
      <td>ModifyEventSubscription</td>
       <td style="text-align:right">-</td>
    </tr>
    <tr class="collapse acm-notimplemented">
      <td>ModifyGlobalCluster</td>
       <td style="text-align:right">-</td>
    </tr>
    <tr class="collapse acm-notimplemented">
      <td>PromoteReadReplicaDBCluster</td>
       <td style="text-align:right">-</td>
    </tr>
    <tr class="collapse acm-notimplemented">
      <td>RemoveFromGlobalCluster</td>
       <td style="text-align:right">-</td>
    </tr>
    <tr class="collapse acm-notimplemented">
      <td>RemoveRoleFromDBCluster</td>
       <td style="text-align:right">-</td>
    </tr>
    <tr class="collapse acm-notimplemented">
      <td>RemoveSourceIdentifierFromSubscription</td>
       <td style="text-align:right">-</td>
    </tr>
    <tr class="collapse acm-notimplemented">
      <td>ResetDBParameterGroup</td>
       <td style="text-align:right">-</td>
    </tr>
    <tr class="collapse acm-notimplemented">
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
    <tr>
      <td><a data-toggle="collapse" href=".acm-notimplemented">Show more</a></td>
      <td style="text-align:right"></td>
    </tr>
    <tr class="collapse acm-notimplemented">
      <td>AcceptInboundConnection</td>
       <td style="text-align:right">-</td>
    </tr>
    <tr class="collapse acm-notimplemented">
      <td>AssociatePackage</td>
       <td style="text-align:right">-</td>
    </tr>
    <tr class="collapse acm-notimplemented">
      <td>CancelServiceSoftwareUpdate</td>
       <td style="text-align:right">-</td>
    </tr>
    <tr class="collapse acm-notimplemented">
      <td>CreateOutboundConnection</td>
       <td style="text-align:right">-</td>
    </tr>
    <tr class="collapse acm-notimplemented">
      <td>CreatePackage</td>
       <td style="text-align:right">-</td>
    </tr>
    <tr class="collapse acm-notimplemented">
      <td>DeleteInboundConnection</td>
       <td style="text-align:right">-</td>
    </tr>
    <tr class="collapse acm-notimplemented">
      <td>DeleteOutboundConnection</td>
       <td style="text-align:right">-</td>
    </tr>
    <tr class="collapse acm-notimplemented">
      <td>DeletePackage</td>
       <td style="text-align:right">-</td>
    </tr>
    <tr class="collapse acm-notimplemented">
      <td>DescribeDomainAutoTunes</td>
       <td style="text-align:right">-</td>
    </tr>
    <tr class="collapse acm-notimplemented">
      <td>DescribeDomainChangeProgress</td>
       <td style="text-align:right">-</td>
    </tr>
    <tr class="collapse acm-notimplemented">
      <td>DescribeInboundConnections</td>
       <td style="text-align:right">-</td>
    </tr>
    <tr class="collapse acm-notimplemented">
      <td>DescribeInstanceTypeLimits</td>
       <td style="text-align:right">-</td>
    </tr>
    <tr class="collapse acm-notimplemented">
      <td>DescribeOutboundConnections</td>
       <td style="text-align:right">-</td>
    </tr>
    <tr class="collapse acm-notimplemented">
      <td>DescribePackages</td>
       <td style="text-align:right">-</td>
    </tr>
    <tr class="collapse acm-notimplemented">
      <td>DescribeReservedInstanceOfferings</td>
       <td style="text-align:right">-</td>
    </tr>
    <tr class="collapse acm-notimplemented">
      <td>DescribeReservedInstances</td>
       <td style="text-align:right">-</td>
    </tr>
    <tr class="collapse acm-notimplemented">
      <td>DissociatePackage</td>
       <td style="text-align:right">-</td>
    </tr>
    <tr class="collapse acm-notimplemented">
      <td>GetPackageVersionHistory</td>
       <td style="text-align:right">-</td>
    </tr>
    <tr class="collapse acm-notimplemented">
      <td>GetUpgradeHistory</td>
       <td style="text-align:right">-</td>
    </tr>
    <tr class="collapse acm-notimplemented">
      <td>GetUpgradeStatus</td>
       <td style="text-align:right">-</td>
    </tr>
    <tr class="collapse acm-notimplemented">
      <td>ListDomainsForPackage</td>
       <td style="text-align:right">-</td>
    </tr>
    <tr class="collapse acm-notimplemented">
      <td>ListInstanceTypeDetails</td>
       <td style="text-align:right">-</td>
    </tr>
    <tr class="collapse acm-notimplemented">
      <td>ListPackagesForDomain</td>
       <td style="text-align:right">-</td>
    </tr>
    <tr class="collapse acm-notimplemented">
      <td>PurchaseReservedInstanceOffering</td>
       <td style="text-align:right">-</td>
    </tr>
    <tr class="collapse acm-notimplemented">
      <td>RejectInboundConnection</td>
       <td style="text-align:right">-</td>
    </tr>
    <tr class="collapse acm-notimplemented">
      <td>StartServiceSoftwareUpdate</td>
       <td style="text-align:right">-</td>
    </tr>
    <tr class="collapse acm-notimplemented">
      <td>UpdatePackage</td>
       <td style="text-align:right">-</td>
    </tr>
    <tr class="collapse acm-notimplemented">
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
      <td>AttachPolicy</td>
       <td style="text-align:right">✅</td>
    </tr>
    <tr>
      <td>CloseAccount</td>
       <td style="text-align:right">✅</td>
    </tr>
    <tr>
      <td>CreateAccount <a href="#misc" title="covered by our integration test suite">✨</a></td>
       <td style="text-align:right">✅</td>
    </tr>
    <tr>
      <td>CreateOrganization <a href="#misc" title="covered by our integration test suite">✨</a></td>
       <td style="text-align:right">✅</td>
    </tr>
    <tr>
      <td>CreateOrganizationalUnit</td>
       <td style="text-align:right">✅</td>
    </tr>
    <tr>
      <td>CreatePolicy</td>
       <td style="text-align:right">✅</td>
    </tr>
    <tr>
      <td>DeleteOrganization <a href="#misc" title="covered by our integration test suite">✨</a></td>
       <td style="text-align:right">✅</td>
    </tr>
    <tr>
      <td>DeletePolicy</td>
       <td style="text-align:right">✅</td>
    </tr>
    <tr>
      <td>DeregisterDelegatedAdministrator</td>
       <td style="text-align:right">✅</td>
    </tr>
    <tr>
      <td>DescribeAccount <a href="#misc" title="covered by our integration test suite">✨</a></td>
       <td style="text-align:right">✅</td>
    </tr>
    <tr>
      <td>DescribeCreateAccountStatus</td>
       <td style="text-align:right">✅</td>
    </tr>
    <tr>
      <td>DescribeOrganization <a href="#misc" title="covered by our integration test suite">✨</a></td>
       <td style="text-align:right">✅</td>
    </tr>
    <tr>
      <td>DescribeOrganizationalUnit</td>
       <td style="text-align:right">✅</td>
    </tr>
    <tr>
      <td>DescribePolicy</td>
       <td style="text-align:right">✅</td>
    </tr>
    <tr>
      <td>DetachPolicy</td>
       <td style="text-align:right">✅</td>
    </tr>
    <tr>
      <td>DisableAWSServiceAccess</td>
       <td style="text-align:right">✅</td>
    </tr>
    <tr>
      <td>DisablePolicyType</td>
       <td style="text-align:right">✅</td>
    </tr>
    <tr>
      <td>EnableAWSServiceAccess</td>
       <td style="text-align:right">✅</td>
    </tr>
    <tr>
      <td>EnablePolicyType</td>
       <td style="text-align:right">✅</td>
    </tr>
    <tr>
      <td>ListAWSServiceAccessForOrganization</td>
       <td style="text-align:right">✅</td>
    </tr>
    <tr>
      <td>ListAccounts</td>
       <td style="text-align:right">✅</td>
    </tr>
    <tr>
      <td>ListAccountsForParent</td>
       <td style="text-align:right">✅</td>
    </tr>
    <tr>
      <td>ListChildren</td>
       <td style="text-align:right">✅</td>
    </tr>
    <tr>
      <td>ListCreateAccountStatus</td>
       <td style="text-align:right">✅</td>
    </tr>
    <tr>
      <td>ListDelegatedAdministrators</td>
       <td style="text-align:right">✅</td>
    </tr>
    <tr>
      <td>ListDelegatedServicesForAccount</td>
       <td style="text-align:right">✅</td>
    </tr>
    <tr>
      <td>ListOrganizationalUnitsForParent</td>
       <td style="text-align:right">✅</td>
    </tr>
    <tr>
      <td>ListParents</td>
       <td style="text-align:right">✅</td>
    </tr>
    <tr>
      <td>ListPolicies</td>
       <td style="text-align:right">✅</td>
    </tr>
    <tr>
      <td>ListPoliciesForTarget</td>
       <td style="text-align:right">✅</td>
    </tr>
    <tr>
      <td>ListRoots</td>
       <td style="text-align:right">✅</td>
    </tr>
    <tr>
      <td>ListTagsForResource</td>
       <td style="text-align:right">✅</td>
    </tr>
    <tr>
      <td>ListTargetsForPolicy</td>
       <td style="text-align:right">✅</td>
    </tr>
    <tr>
      <td>MoveAccount</td>
       <td style="text-align:right">✅</td>
    </tr>
    <tr>
      <td>RegisterDelegatedAdministrator</td>
       <td style="text-align:right">✅</td>
    </tr>
    <tr>
      <td>RemoveAccountFromOrganization</td>
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
      <td>UpdateOrganizationalUnit</td>
       <td style="text-align:right">✅</td>
    </tr>
    <tr>
      <td>UpdatePolicy</td>
       <td style="text-align:right">✅</td>
    </tr>
    <tr>
      <td><a data-toggle="collapse" href=".acm-notimplemented">Show more</a></td>
      <td style="text-align:right"></td>
    </tr>
    <tr class="collapse acm-notimplemented">
      <td>AcceptHandshake</td>
       <td style="text-align:right">-</td>
    </tr>
    <tr class="collapse acm-notimplemented">
      <td>CancelHandshake</td>
       <td style="text-align:right">-</td>
    </tr>
    <tr class="collapse acm-notimplemented">
      <td>CreateGovCloudAccount</td>
       <td style="text-align:right">-</td>
    </tr>
    <tr class="collapse acm-notimplemented">
      <td>DeclineHandshake</td>
       <td style="text-align:right">-</td>
    </tr>
    <tr class="collapse acm-notimplemented">
      <td>DeleteOrganizationalUnit</td>
       <td style="text-align:right">-</td>
    </tr>
    <tr class="collapse acm-notimplemented">
      <td>DescribeEffectivePolicy</td>
       <td style="text-align:right">-</td>
    </tr>
    <tr class="collapse acm-notimplemented">
      <td>DescribeHandshake</td>
       <td style="text-align:right">-</td>
    </tr>
    <tr class="collapse acm-notimplemented">
      <td>EnableAllFeatures</td>
       <td style="text-align:right">-</td>
    </tr>
    <tr class="collapse acm-notimplemented">
      <td>InviteAccountToOrganization</td>
       <td style="text-align:right">-</td>
    </tr>
    <tr class="collapse acm-notimplemented">
      <td>LeaveOrganization</td>
       <td style="text-align:right">-</td>
    </tr>
    <tr class="collapse acm-notimplemented">
      <td>ListHandshakesForAccount</td>
       <td style="text-align:right">-</td>
    </tr>
    <tr class="collapse acm-notimplemented">
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
      <td>CreateLedger <a href="#misc" title="covered by our integration test suite">✨</a></td>
       <td style="text-align:right">✅</td>
    </tr>
    <tr>
      <td>DeleteLedger <a href="#misc" title="covered by our integration test suite">✨</a></td>
       <td style="text-align:right">✅</td>
    </tr>
    <tr>
      <td>DescribeJournalKinesisStream</td>
       <td style="text-align:right">✅</td>
    </tr>
    <tr>
      <td>DescribeJournalS3Export</td>
       <td style="text-align:right">✅</td>
    </tr>
    <tr>
      <td>DescribeLedger <a href="#misc" title="covered by our integration test suite">✨</a></td>
       <td style="text-align:right">✅</td>
    </tr>
    <tr>
      <td>ExportJournalToS3</td>
       <td style="text-align:right">✅</td>
    </tr>
    <tr>
      <td>ListLedgers <a href="#misc" title="covered by our integration test suite">✨</a></td>
       <td style="text-align:right">✅</td>
    </tr>
    <tr>
      <td>ListTagsForResource <a href="#misc" title="covered by our integration test suite">✨</a></td>
       <td style="text-align:right">✅</td>
    </tr>
    <tr>
      <td>StreamJournalToKinesis <a href="#misc" title="covered by our integration test suite">✨</a></td>
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
      <td>UpdateLedger <a href="#misc" title="covered by our integration test suite">✨</a></td>
       <td style="text-align:right">✅</td>
    </tr>
    <tr>
      <td><a data-toggle="collapse" href=".acm-notimplemented">Show more</a></td>
      <td style="text-align:right"></td>
    </tr>
    <tr class="collapse acm-notimplemented">
      <td>CancelJournalKinesisStream</td>
       <td style="text-align:right">-</td>
    </tr>
    <tr class="collapse acm-notimplemented">
      <td>GetBlock</td>
       <td style="text-align:right">-</td>
    </tr>
    <tr class="collapse acm-notimplemented">
      <td>GetDigest</td>
       <td style="text-align:right">-</td>
    </tr>
    <tr class="collapse acm-notimplemented">
      <td>GetRevision</td>
       <td style="text-align:right">-</td>
    </tr>
    <tr class="collapse acm-notimplemented">
      <td>ListJournalKinesisStreamsForLedger</td>
       <td style="text-align:right">-</td>
    </tr>
    <tr class="collapse acm-notimplemented">
      <td>ListJournalS3Exports</td>
       <td style="text-align:right">-</td>
    </tr>
    <tr class="collapse acm-notimplemented">
      <td>ListJournalS3ExportsForLedger</td>
       <td style="text-align:right">-</td>
    </tr>
    <tr class="collapse acm-notimplemented">
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
      <td>SendCommand <a href="#misc" title="covered by our integration test suite">✨</a></td>
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
      <td>AddTagsToResource <a href="#misc" title="covered by our integration test suite">✨</a></td>
       <td style="text-align:right">✅</td>
    </tr>
    <tr>
      <td>AuthorizeDBSecurityGroupIngress</td>
       <td style="text-align:right">✅</td>
    </tr>
    <tr>
      <td>CancelExportTask</td>
       <td style="text-align:right">✅</td>
    </tr>
    <tr>
      <td>CopyDBClusterSnapshot</td>
       <td style="text-align:right">✅</td>
    </tr>
    <tr>
      <td>CopyDBSnapshot</td>
       <td style="text-align:right">✅</td>
    </tr>
    <tr>
      <td>CreateDBCluster <a href="#misc" title="covered by our integration test suite">✨</a></td>
       <td style="text-align:right">✅</td>
    </tr>
    <tr>
      <td>CreateDBClusterEndpoint <a href="#misc" title="covered by our integration test suite">✨</a></td>
       <td style="text-align:right">✅</td>
    </tr>
    <tr>
      <td>CreateDBClusterParameterGroup <a href="#misc" title="covered by our integration test suite">✨</a></td>
       <td style="text-align:right">✅</td>
    </tr>
    <tr>
      <td>CreateDBClusterSnapshot <a href="#misc" title="covered by our integration test suite">✨</a></td>
       <td style="text-align:right">✅</td>
    </tr>
    <tr>
      <td>CreateDBInstance <a href="#misc" title="covered by our integration test suite">✨</a></td>
       <td style="text-align:right">✅</td>
    </tr>
    <tr>
      <td>CreateDBInstanceReadReplica</td>
       <td style="text-align:right">✅</td>
    </tr>
    <tr>
      <td>CreateDBParameterGroup <a href="#misc" title="covered by our integration test suite">✨</a></td>
       <td style="text-align:right">✅</td>
    </tr>
    <tr>
      <td>CreateDBProxy <a href="#misc" title="covered by our integration test suite">✨</a></td>
       <td style="text-align:right">✅</td>
    </tr>
    <tr>
      <td>CreateDBSecurityGroup</td>
       <td style="text-align:right">✅</td>
    </tr>
    <tr>
      <td>CreateDBSnapshot <a href="#misc" title="covered by our integration test suite">✨</a></td>
       <td style="text-align:right">✅</td>
    </tr>
    <tr>
      <td>CreateDBSubnetGroup <a href="#misc" title="covered by our integration test suite">✨</a></td>
       <td style="text-align:right">✅</td>
    </tr>
    <tr>
      <td>CreateEventSubscription</td>
       <td style="text-align:right">✅</td>
    </tr>
    <tr>
      <td>CreateOptionGroup</td>
       <td style="text-align:right">✅</td>
    </tr>
    <tr>
      <td>DeleteDBCluster <a href="#misc" title="covered by our integration test suite">✨</a></td>
       <td style="text-align:right">✅</td>
    </tr>
    <tr>
      <td>DeleteDBClusterEndpoint <a href="#misc" title="covered by our integration test suite">✨</a></td>
       <td style="text-align:right">✅</td>
    </tr>
    <tr>
      <td>DeleteDBClusterParameterGroup <a href="#misc" title="covered by our integration test suite">✨</a></td>
       <td style="text-align:right">✅</td>
    </tr>
    <tr>
      <td>DeleteDBClusterSnapshot <a href="#misc" title="covered by our integration test suite">✨</a></td>
       <td style="text-align:right">✅</td>
    </tr>
    <tr>
      <td>DeleteDBInstance <a href="#misc" title="covered by our integration test suite">✨</a></td>
       <td style="text-align:right">✅</td>
    </tr>
    <tr>
      <td>DeleteDBParameterGroup <a href="#misc" title="covered by our integration test suite">✨</a></td>
       <td style="text-align:right">✅</td>
    </tr>
    <tr>
      <td>DeleteDBProxy <a href="#misc" title="covered by our integration test suite">✨</a></td>
       <td style="text-align:right">✅</td>
    </tr>
    <tr>
      <td>DeleteDBSecurityGroup</td>
       <td style="text-align:right">✅</td>
    </tr>
    <tr>
      <td>DeleteDBSnapshot</td>
       <td style="text-align:right">✅</td>
    </tr>
    <tr>
      <td>DeleteDBSubnetGroup <a href="#misc" title="covered by our integration test suite">✨</a></td>
       <td style="text-align:right">✅</td>
    </tr>
    <tr>
      <td>DeleteEventSubscription</td>
       <td style="text-align:right">✅</td>
    </tr>
    <tr>
      <td>DeleteOptionGroup</td>
       <td style="text-align:right">✅</td>
    </tr>
    <tr>
      <td>DeregisterDBProxyTargets <a href="#misc" title="covered by our integration test suite">✨</a></td>
       <td style="text-align:right">✅</td>
    </tr>
    <tr>
      <td>DescribeCertificates</td>
       <td style="text-align:right">✅</td>
    </tr>
    <tr>
      <td>DescribeDBClusterEndpoints <a href="#misc" title="covered by our integration test suite">✨</a></td>
       <td style="text-align:right">✅</td>
    </tr>
    <tr>
      <td>DescribeDBClusterParameterGroups <a href="#misc" title="covered by our integration test suite">✨</a></td>
       <td style="text-align:right">✅</td>
    </tr>
    <tr>
      <td>DescribeDBClusterParameters <a href="#misc" title="covered by our integration test suite">✨</a></td>
       <td style="text-align:right">✅</td>
    </tr>
    <tr>
      <td>DescribeDBClusterSnapshots <a href="#misc" title="covered by our integration test suite">✨</a></td>
       <td style="text-align:right">✅</td>
    </tr>
    <tr>
      <td>DescribeDBClusters <a href="#misc" title="covered by our integration test suite">✨</a></td>
       <td style="text-align:right">✅</td>
    </tr>
    <tr>
      <td>DescribeDBEngineVersions <a href="#misc" title="covered by our integration test suite">✨</a></td>
       <td style="text-align:right">✅</td>
    </tr>
    <tr>
      <td>DescribeDBInstances <a href="#misc" title="covered by our integration test suite">✨</a></td>
       <td style="text-align:right">✅</td>
    </tr>
    <tr>
      <td>DescribeDBParameterGroups <a href="#misc" title="covered by our integration test suite">✨</a></td>
       <td style="text-align:right">✅</td>
    </tr>
    <tr>
      <td>DescribeDBParameters <a href="#misc" title="covered by our integration test suite">✨</a></td>
       <td style="text-align:right">✅</td>
    </tr>
    <tr>
      <td>DescribeDBProxies <a href="#misc" title="covered by our integration test suite">✨</a></td>
       <td style="text-align:right">✅</td>
    </tr>
    <tr>
      <td>DescribeDBProxyTargets <a href="#misc" title="covered by our integration test suite">✨</a></td>
       <td style="text-align:right">✅</td>
    </tr>
    <tr>
      <td>DescribeDBSecurityGroups</td>
       <td style="text-align:right">✅</td>
    </tr>
    <tr>
      <td>DescribeDBSnapshots <a href="#misc" title="covered by our integration test suite">✨</a></td>
       <td style="text-align:right">✅</td>
    </tr>
    <tr>
      <td>DescribeDBSubnetGroups <a href="#misc" title="covered by our integration test suite">✨</a></td>
       <td style="text-align:right">✅</td>
    </tr>
    <tr>
      <td>DescribeEventSubscriptions</td>
       <td style="text-align:right">✅</td>
    </tr>
    <tr>
      <td>DescribeExportTasks</td>
       <td style="text-align:right">✅</td>
    </tr>
    <tr>
      <td>DescribeGlobalClusters</td>
       <td style="text-align:right">✅</td>
    </tr>
    <tr>
      <td>DescribeOptionGroupOptions</td>
       <td style="text-align:right">✅</td>
    </tr>
    <tr>
      <td>DescribeOptionGroups</td>
       <td style="text-align:right">✅</td>
    </tr>
    <tr>
      <td>ListTagsForResource <a href="#misc" title="covered by our integration test suite">✨</a></td>
       <td style="text-align:right">✅</td>
    </tr>
    <tr>
      <td>ModifyCertificates</td>
       <td style="text-align:right">✅</td>
    </tr>
    <tr>
      <td>ModifyCurrentDBClusterCapacity</td>
       <td style="text-align:right">✅</td>
    </tr>
    <tr>
      <td>ModifyDBCluster <a href="#misc" title="covered by our integration test suite">✨</a></td>
       <td style="text-align:right">✅</td>
    </tr>
    <tr>
      <td>ModifyDBClusterEndpoint <a href="#misc" title="covered by our integration test suite">✨</a></td>
       <td style="text-align:right">✅</td>
    </tr>
    <tr>
      <td>ModifyDBClusterParameterGroup <a href="#misc" title="covered by our integration test suite">✨</a></td>
       <td style="text-align:right">✅</td>
    </tr>
    <tr>
      <td>ModifyDBInstance <a href="#misc" title="covered by our integration test suite">✨</a></td>
       <td style="text-align:right">✅</td>
    </tr>
    <tr>
      <td>ModifyDBParameterGroup <a href="#misc" title="covered by our integration test suite">✨</a></td>
       <td style="text-align:right">✅</td>
    </tr>
    <tr>
      <td>ModifyDBSubnetGroup</td>
       <td style="text-align:right">✅</td>
    </tr>
    <tr>
      <td>ModifyOptionGroup</td>
       <td style="text-align:right">✅</td>
    </tr>
    <tr>
      <td>RebootDBInstance</td>
       <td style="text-align:right">✅</td>
    </tr>
    <tr>
      <td>RegisterDBProxyTargets <a href="#misc" title="covered by our integration test suite">✨</a></td>
       <td style="text-align:right">✅</td>
    </tr>
    <tr>
      <td>RemoveTagsFromResource <a href="#misc" title="covered by our integration test suite">✨</a></td>
       <td style="text-align:right">✅</td>
    </tr>
    <tr>
      <td>ResetDBClusterParameterGroup</td>
       <td style="text-align:right">✅</td>
    </tr>
    <tr>
      <td>RestoreDBClusterFromSnapshot <a href="#misc" title="covered by our integration test suite">✨</a></td>
       <td style="text-align:right">✅</td>
    </tr>
    <tr>
      <td>RestoreDBInstanceFromDBSnapshot <a href="#misc" title="covered by our integration test suite">✨</a></td>
       <td style="text-align:right">✅</td>
    </tr>
    <tr>
      <td>StartDBCluster</td>
       <td style="text-align:right">✅</td>
    </tr>
    <tr>
      <td>StartDBInstance</td>
       <td style="text-align:right">✅</td>
    </tr>
    <tr>
      <td>StartExportTask</td>
       <td style="text-align:right">✅</td>
    </tr>
    <tr>
      <td>StopDBCluster</td>
       <td style="text-align:right">✅</td>
    </tr>
    <tr>
      <td>StopDBInstance</td>
       <td style="text-align:right">✅</td>
    </tr>
    <tr>
      <td><a data-toggle="collapse" href=".acm-notimplemented">Show more</a></td>
      <td style="text-align:right"></td>
    </tr>
    <tr class="collapse acm-notimplemented">
      <td>AddRoleToDBCluster</td>
       <td style="text-align:right">-</td>
    </tr>
    <tr class="collapse acm-notimplemented">
      <td>AddRoleToDBInstance</td>
       <td style="text-align:right">-</td>
    </tr>
    <tr class="collapse acm-notimplemented">
      <td>AddSourceIdentifierToSubscription</td>
       <td style="text-align:right">-</td>
    </tr>
    <tr class="collapse acm-notimplemented">
      <td>ApplyPendingMaintenanceAction</td>
       <td style="text-align:right">-</td>
    </tr>
    <tr class="collapse acm-notimplemented">
      <td>BacktrackDBCluster</td>
       <td style="text-align:right">-</td>
    </tr>
    <tr class="collapse acm-notimplemented">
      <td>CopyDBClusterParameterGroup</td>
       <td style="text-align:right">-</td>
    </tr>
    <tr class="collapse acm-notimplemented">
      <td>CopyDBParameterGroup</td>
       <td style="text-align:right">-</td>
    </tr>
    <tr class="collapse acm-notimplemented">
      <td>CopyOptionGroup</td>
       <td style="text-align:right">-</td>
    </tr>
    <tr class="collapse acm-notimplemented">
      <td>CreateCustomDBEngineVersion</td>
       <td style="text-align:right">-</td>
    </tr>
    <tr class="collapse acm-notimplemented">
      <td>CreateDBProxyEndpoint</td>
       <td style="text-align:right">-</td>
    </tr>
    <tr class="collapse acm-notimplemented">
      <td>CreateGlobalCluster</td>
       <td style="text-align:right">-</td>
    </tr>
    <tr class="collapse acm-notimplemented">
      <td>DeleteCustomDBEngineVersion</td>
       <td style="text-align:right">-</td>
    </tr>
    <tr class="collapse acm-notimplemented">
      <td>DeleteDBInstanceAutomatedBackup</td>
       <td style="text-align:right">-</td>
    </tr>
    <tr class="collapse acm-notimplemented">
      <td>DeleteDBProxyEndpoint</td>
       <td style="text-align:right">-</td>
    </tr>
    <tr class="collapse acm-notimplemented">
      <td>DeleteGlobalCluster</td>
       <td style="text-align:right">-</td>
    </tr>
    <tr class="collapse acm-notimplemented">
      <td>DescribeAccountAttributes</td>
       <td style="text-align:right">-</td>
    </tr>
    <tr class="collapse acm-notimplemented">
      <td>DescribeDBClusterBacktracks</td>
       <td style="text-align:right">-</td>
    </tr>
    <tr class="collapse acm-notimplemented">
      <td>DescribeDBClusterSnapshotAttributes</td>
       <td style="text-align:right">-</td>
    </tr>
    <tr class="collapse acm-notimplemented">
      <td>DescribeDBInstanceAutomatedBackups</td>
       <td style="text-align:right">-</td>
    </tr>
    <tr class="collapse acm-notimplemented">
      <td>DescribeDBLogFiles</td>
       <td style="text-align:right">-</td>
    </tr>
    <tr class="collapse acm-notimplemented">
      <td>DescribeDBProxyEndpoints</td>
       <td style="text-align:right">-</td>
    </tr>
    <tr class="collapse acm-notimplemented">
      <td>DescribeDBProxyTargetGroups</td>
       <td style="text-align:right">-</td>
    </tr>
    <tr class="collapse acm-notimplemented">
      <td>DescribeDBSnapshotAttributes</td>
       <td style="text-align:right">-</td>
    </tr>
    <tr class="collapse acm-notimplemented">
      <td>DescribeEngineDefaultClusterParameters</td>
       <td style="text-align:right">-</td>
    </tr>
    <tr class="collapse acm-notimplemented">
      <td>DescribeEngineDefaultParameters</td>
       <td style="text-align:right">-</td>
    </tr>
    <tr class="collapse acm-notimplemented">
      <td>DescribeEventCategories</td>
       <td style="text-align:right">-</td>
    </tr>
    <tr class="collapse acm-notimplemented">
      <td>DescribeEvents</td>
       <td style="text-align:right">-</td>
    </tr>
    <tr class="collapse acm-notimplemented">
      <td>DescribeOrderableDBInstanceOptions</td>
       <td style="text-align:right">-</td>
    </tr>
    <tr class="collapse acm-notimplemented">
      <td>DescribePendingMaintenanceActions</td>
       <td style="text-align:right">-</td>
    </tr>
    <tr class="collapse acm-notimplemented">
      <td>DescribeReservedDBInstances</td>
       <td style="text-align:right">-</td>
    </tr>
    <tr class="collapse acm-notimplemented">
      <td>DescribeReservedDBInstancesOfferings</td>
       <td style="text-align:right">-</td>
    </tr>
    <tr class="collapse acm-notimplemented">
      <td>DescribeSourceRegions</td>
       <td style="text-align:right">-</td>
    </tr>
    <tr class="collapse acm-notimplemented">
      <td>DescribeValidDBInstanceModifications</td>
       <td style="text-align:right">-</td>
    </tr>
    <tr class="collapse acm-notimplemented">
      <td>DownloadDBLogFilePortion</td>
       <td style="text-align:right">-</td>
    </tr>
    <tr class="collapse acm-notimplemented">
      <td>FailoverDBCluster</td>
       <td style="text-align:right">-</td>
    </tr>
    <tr class="collapse acm-notimplemented">
      <td>FailoverGlobalCluster</td>
       <td style="text-align:right">-</td>
    </tr>
    <tr class="collapse acm-notimplemented">
      <td>ModifyCustomDBEngineVersion</td>
       <td style="text-align:right">-</td>
    </tr>
    <tr class="collapse acm-notimplemented">
      <td>ModifyDBClusterSnapshotAttribute</td>
       <td style="text-align:right">-</td>
    </tr>
    <tr class="collapse acm-notimplemented">
      <td>ModifyDBProxy</td>
       <td style="text-align:right">-</td>
    </tr>
    <tr class="collapse acm-notimplemented">
      <td>ModifyDBProxyEndpoint</td>
       <td style="text-align:right">-</td>
    </tr>
    <tr class="collapse acm-notimplemented">
      <td>ModifyDBProxyTargetGroup</td>
       <td style="text-align:right">-</td>
    </tr>
    <tr class="collapse acm-notimplemented">
      <td>ModifyDBSnapshot</td>
       <td style="text-align:right">-</td>
    </tr>
    <tr class="collapse acm-notimplemented">
      <td>ModifyDBSnapshotAttribute</td>
       <td style="text-align:right">-</td>
    </tr>
    <tr class="collapse acm-notimplemented">
      <td>ModifyEventSubscription</td>
       <td style="text-align:right">-</td>
    </tr>
    <tr class="collapse acm-notimplemented">
      <td>ModifyGlobalCluster</td>
       <td style="text-align:right">-</td>
    </tr>
    <tr class="collapse acm-notimplemented">
      <td>PromoteReadReplica</td>
       <td style="text-align:right">-</td>
    </tr>
    <tr class="collapse acm-notimplemented">
      <td>PromoteReadReplicaDBCluster</td>
       <td style="text-align:right">-</td>
    </tr>
    <tr class="collapse acm-notimplemented">
      <td>PurchaseReservedDBInstancesOffering</td>
       <td style="text-align:right">-</td>
    </tr>
    <tr class="collapse acm-notimplemented">
      <td>RebootDBCluster</td>
       <td style="text-align:right">-</td>
    </tr>
    <tr class="collapse acm-notimplemented">
      <td>RemoveFromGlobalCluster</td>
       <td style="text-align:right">-</td>
    </tr>
    <tr class="collapse acm-notimplemented">
      <td>RemoveRoleFromDBCluster</td>
       <td style="text-align:right">-</td>
    </tr>
    <tr class="collapse acm-notimplemented">
      <td>RemoveRoleFromDBInstance</td>
       <td style="text-align:right">-</td>
    </tr>
    <tr class="collapse acm-notimplemented">
      <td>RemoveSourceIdentifierFromSubscription</td>
       <td style="text-align:right">-</td>
    </tr>
    <tr class="collapse acm-notimplemented">
      <td>ResetDBParameterGroup</td>
       <td style="text-align:right">-</td>
    </tr>
    <tr class="collapse acm-notimplemented">
      <td>RestoreDBClusterFromS3</td>
       <td style="text-align:right">-</td>
    </tr>
    <tr class="collapse acm-notimplemented">
      <td>RestoreDBClusterToPointInTime</td>
       <td style="text-align:right">-</td>
    </tr>
    <tr class="collapse acm-notimplemented">
      <td>RestoreDBInstanceFromS3</td>
       <td style="text-align:right">-</td>
    </tr>
    <tr class="collapse acm-notimplemented">
      <td>RestoreDBInstanceToPointInTime</td>
       <td style="text-align:right">-</td>
    </tr>
    <tr class="collapse acm-notimplemented">
      <td>RevokeDBSecurityGroupIngress</td>
       <td style="text-align:right">-</td>
    </tr>
    <tr class="collapse acm-notimplemented">
      <td>StartActivityStream</td>
       <td style="text-align:right">-</td>
    </tr>
    <tr class="collapse acm-notimplemented">
      <td>StartDBInstanceAutomatedBackupsReplication</td>
       <td style="text-align:right">-</td>
    </tr>
    <tr class="collapse acm-notimplemented">
      <td>StopActivityStream</td>
       <td style="text-align:right">-</td>
    </tr>
    <tr class="collapse acm-notimplemented">
      <td>StopDBInstanceAutomatedBackupsReplication</td>
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
      <td>BeginTransaction <a href="#misc" title="covered by our integration test suite">✨</a></td>
       <td style="text-align:right">✅</td>
    </tr>
    <tr>
      <td>CommitTransaction <a href="#misc" title="covered by our integration test suite">✨</a></td>
       <td style="text-align:right">✅</td>
    </tr>
    <tr>
      <td>ExecuteSql <a href="#misc" title="covered by our integration test suite">✨</a></td>
       <td style="text-align:right">✅</td>
    </tr>
    <tr>
      <td>ExecuteStatement <a href="#misc" title="covered by our integration test suite">✨</a></td>
       <td style="text-align:right">✅</td>
    </tr>
    <tr>
      <td><a data-toggle="collapse" href=".acm-notimplemented">Show more</a></td>
      <td style="text-align:right"></td>
    </tr>
    <tr class="collapse acm-notimplemented">
      <td>BatchExecuteStatement</td>
       <td style="text-align:right">-</td>
    </tr>
    <tr class="collapse acm-notimplemented">
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
      <td>AuthorizeClusterSecurityGroupIngress</td>
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
      <td>CreateClusterSecurityGroup</td>
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
      <td>DescribeClusterParameters <a href="#misc" title="covered by our integration test suite">✨</a></td>
       <td style="text-align:right">✅</td>
    </tr>
    <tr>
      <td>DescribeClusterSecurityGroups</td>
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
      <td>DescribeDefaultClusterParameters <a href="#misc" title="covered by our integration test suite">✨</a></td>
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
    <tr>
      <td><a data-toggle="collapse" href=".acm-notimplemented">Show more</a></td>
      <td style="text-align:right"></td>
    </tr>
    <tr class="collapse acm-notimplemented">
      <td>AcceptReservedNodeExchange</td>
       <td style="text-align:right">-</td>
    </tr>
    <tr class="collapse acm-notimplemented">
      <td>AddPartner</td>
       <td style="text-align:right">-</td>
    </tr>
    <tr class="collapse acm-notimplemented">
      <td>AssociateDataShareConsumer</td>
       <td style="text-align:right">-</td>
    </tr>
    <tr class="collapse acm-notimplemented">
      <td>AuthorizeDataShare</td>
       <td style="text-align:right">-</td>
    </tr>
    <tr class="collapse acm-notimplemented">
      <td>AuthorizeEndpointAccess</td>
       <td style="text-align:right">-</td>
    </tr>
    <tr class="collapse acm-notimplemented">
      <td>AuthorizeSnapshotAccess</td>
       <td style="text-align:right">-</td>
    </tr>
    <tr class="collapse acm-notimplemented">
      <td>BatchDeleteClusterSnapshots</td>
       <td style="text-align:right">-</td>
    </tr>
    <tr class="collapse acm-notimplemented">
      <td>BatchModifyClusterSnapshots</td>
       <td style="text-align:right">-</td>
    </tr>
    <tr class="collapse acm-notimplemented">
      <td>CancelResize</td>
       <td style="text-align:right">-</td>
    </tr>
    <tr class="collapse acm-notimplemented">
      <td>CopyClusterSnapshot</td>
       <td style="text-align:right">-</td>
    </tr>
    <tr class="collapse acm-notimplemented">
      <td>CreateAuthenticationProfile</td>
       <td style="text-align:right">-</td>
    </tr>
    <tr class="collapse acm-notimplemented">
      <td>CreateEndpointAccess</td>
       <td style="text-align:right">-</td>
    </tr>
    <tr class="collapse acm-notimplemented">
      <td>CreateEventSubscription</td>
       <td style="text-align:right">-</td>
    </tr>
    <tr class="collapse acm-notimplemented">
      <td>CreateHsmClientCertificate</td>
       <td style="text-align:right">-</td>
    </tr>
    <tr class="collapse acm-notimplemented">
      <td>CreateHsmConfiguration</td>
       <td style="text-align:right">-</td>
    </tr>
    <tr class="collapse acm-notimplemented">
      <td>CreateScheduledAction</td>
       <td style="text-align:right">-</td>
    </tr>
    <tr class="collapse acm-notimplemented">
      <td>CreateSnapshotSchedule</td>
       <td style="text-align:right">-</td>
    </tr>
    <tr class="collapse acm-notimplemented">
      <td>CreateUsageLimit</td>
       <td style="text-align:right">-</td>
    </tr>
    <tr class="collapse acm-notimplemented">
      <td>DeauthorizeDataShare</td>
       <td style="text-align:right">-</td>
    </tr>
    <tr class="collapse acm-notimplemented">
      <td>DeleteAuthenticationProfile</td>
       <td style="text-align:right">-</td>
    </tr>
    <tr class="collapse acm-notimplemented">
      <td>DeleteEndpointAccess</td>
       <td style="text-align:right">-</td>
    </tr>
    <tr class="collapse acm-notimplemented">
      <td>DeleteEventSubscription</td>
       <td style="text-align:right">-</td>
    </tr>
    <tr class="collapse acm-notimplemented">
      <td>DeleteHsmClientCertificate</td>
       <td style="text-align:right">-</td>
    </tr>
    <tr class="collapse acm-notimplemented">
      <td>DeleteHsmConfiguration</td>
       <td style="text-align:right">-</td>
    </tr>
    <tr class="collapse acm-notimplemented">
      <td>DeletePartner</td>
       <td style="text-align:right">-</td>
    </tr>
    <tr class="collapse acm-notimplemented">
      <td>DeleteScheduledAction</td>
       <td style="text-align:right">-</td>
    </tr>
    <tr class="collapse acm-notimplemented">
      <td>DeleteSnapshotSchedule</td>
       <td style="text-align:right">-</td>
    </tr>
    <tr class="collapse acm-notimplemented">
      <td>DeleteUsageLimit</td>
       <td style="text-align:right">-</td>
    </tr>
    <tr class="collapse acm-notimplemented">
      <td>DescribeAccountAttributes</td>
       <td style="text-align:right">-</td>
    </tr>
    <tr class="collapse acm-notimplemented">
      <td>DescribeAuthenticationProfiles</td>
       <td style="text-align:right">-</td>
    </tr>
    <tr class="collapse acm-notimplemented">
      <td>DescribeClusterDbRevisions</td>
       <td style="text-align:right">-</td>
    </tr>
    <tr class="collapse acm-notimplemented">
      <td>DescribeClusterTracks</td>
       <td style="text-align:right">-</td>
    </tr>
    <tr class="collapse acm-notimplemented">
      <td>DescribeClusterVersions</td>
       <td style="text-align:right">-</td>
    </tr>
    <tr class="collapse acm-notimplemented">
      <td>DescribeDataShares</td>
       <td style="text-align:right">-</td>
    </tr>
    <tr class="collapse acm-notimplemented">
      <td>DescribeDataSharesForConsumer</td>
       <td style="text-align:right">-</td>
    </tr>
    <tr class="collapse acm-notimplemented">
      <td>DescribeDataSharesForProducer</td>
       <td style="text-align:right">-</td>
    </tr>
    <tr class="collapse acm-notimplemented">
      <td>DescribeEndpointAccess</td>
       <td style="text-align:right">-</td>
    </tr>
    <tr class="collapse acm-notimplemented">
      <td>DescribeEndpointAuthorization</td>
       <td style="text-align:right">-</td>
    </tr>
    <tr class="collapse acm-notimplemented">
      <td>DescribeEventCategories</td>
       <td style="text-align:right">-</td>
    </tr>
    <tr class="collapse acm-notimplemented">
      <td>DescribeEventSubscriptions</td>
       <td style="text-align:right">-</td>
    </tr>
    <tr class="collapse acm-notimplemented">
      <td>DescribeEvents</td>
       <td style="text-align:right">-</td>
    </tr>
    <tr class="collapse acm-notimplemented">
      <td>DescribeHsmClientCertificates</td>
       <td style="text-align:right">-</td>
    </tr>
    <tr class="collapse acm-notimplemented">
      <td>DescribeHsmConfigurations</td>
       <td style="text-align:right">-</td>
    </tr>
    <tr class="collapse acm-notimplemented">
      <td>DescribeLoggingStatus</td>
       <td style="text-align:right">-</td>
    </tr>
    <tr class="collapse acm-notimplemented">
      <td>DescribeNodeConfigurationOptions</td>
       <td style="text-align:right">-</td>
    </tr>
    <tr class="collapse acm-notimplemented">
      <td>DescribeOrderableClusterOptions</td>
       <td style="text-align:right">-</td>
    </tr>
    <tr class="collapse acm-notimplemented">
      <td>DescribePartners</td>
       <td style="text-align:right">-</td>
    </tr>
    <tr class="collapse acm-notimplemented">
      <td>DescribeReservedNodeExchangeStatus</td>
       <td style="text-align:right">-</td>
    </tr>
    <tr class="collapse acm-notimplemented">
      <td>DescribeReservedNodeOfferings</td>
       <td style="text-align:right">-</td>
    </tr>
    <tr class="collapse acm-notimplemented">
      <td>DescribeReservedNodes</td>
       <td style="text-align:right">-</td>
    </tr>
    <tr class="collapse acm-notimplemented">
      <td>DescribeResize</td>
       <td style="text-align:right">-</td>
    </tr>
    <tr class="collapse acm-notimplemented">
      <td>DescribeScheduledActions</td>
       <td style="text-align:right">-</td>
    </tr>
    <tr class="collapse acm-notimplemented">
      <td>DescribeSnapshotSchedules</td>
       <td style="text-align:right">-</td>
    </tr>
    <tr class="collapse acm-notimplemented">
      <td>DescribeStorage</td>
       <td style="text-align:right">-</td>
    </tr>
    <tr class="collapse acm-notimplemented">
      <td>DescribeTableRestoreStatus</td>
       <td style="text-align:right">-</td>
    </tr>
    <tr class="collapse acm-notimplemented">
      <td>DescribeUsageLimits</td>
       <td style="text-align:right">-</td>
    </tr>
    <tr class="collapse acm-notimplemented">
      <td>DisableLogging</td>
       <td style="text-align:right">-</td>
    </tr>
    <tr class="collapse acm-notimplemented">
      <td>DisassociateDataShareConsumer</td>
       <td style="text-align:right">-</td>
    </tr>
    <tr class="collapse acm-notimplemented">
      <td>EnableLogging</td>
       <td style="text-align:right">-</td>
    </tr>
    <tr class="collapse acm-notimplemented">
      <td>GetClusterCredentialsWithIAM</td>
       <td style="text-align:right">-</td>
    </tr>
    <tr class="collapse acm-notimplemented">
      <td>GetReservedNodeExchangeConfigurationOptions</td>
       <td style="text-align:right">-</td>
    </tr>
    <tr class="collapse acm-notimplemented">
      <td>GetReservedNodeExchangeOfferings</td>
       <td style="text-align:right">-</td>
    </tr>
    <tr class="collapse acm-notimplemented">
      <td>ModifyAquaConfiguration</td>
       <td style="text-align:right">-</td>
    </tr>
    <tr class="collapse acm-notimplemented">
      <td>ModifyAuthenticationProfile</td>
       <td style="text-align:right">-</td>
    </tr>
    <tr class="collapse acm-notimplemented">
      <td>ModifyClusterDbRevision</td>
       <td style="text-align:right">-</td>
    </tr>
    <tr class="collapse acm-notimplemented">
      <td>ModifyClusterIamRoles</td>
       <td style="text-align:right">-</td>
    </tr>
    <tr class="collapse acm-notimplemented">
      <td>ModifyClusterMaintenance</td>
       <td style="text-align:right">-</td>
    </tr>
    <tr class="collapse acm-notimplemented">
      <td>ModifyClusterParameterGroup</td>
       <td style="text-align:right">-</td>
    </tr>
    <tr class="collapse acm-notimplemented">
      <td>ModifyClusterSnapshot</td>
       <td style="text-align:right">-</td>
    </tr>
    <tr class="collapse acm-notimplemented">
      <td>ModifyClusterSnapshotSchedule</td>
       <td style="text-align:right">-</td>
    </tr>
    <tr class="collapse acm-notimplemented">
      <td>ModifyClusterSubnetGroup</td>
       <td style="text-align:right">-</td>
    </tr>
    <tr class="collapse acm-notimplemented">
      <td>ModifyEndpointAccess</td>
       <td style="text-align:right">-</td>
    </tr>
    <tr class="collapse acm-notimplemented">
      <td>ModifyEventSubscription</td>
       <td style="text-align:right">-</td>
    </tr>
    <tr class="collapse acm-notimplemented">
      <td>ModifyScheduledAction</td>
       <td style="text-align:right">-</td>
    </tr>
    <tr class="collapse acm-notimplemented">
      <td>ModifySnapshotSchedule</td>
       <td style="text-align:right">-</td>
    </tr>
    <tr class="collapse acm-notimplemented">
      <td>ModifyUsageLimit</td>
       <td style="text-align:right">-</td>
    </tr>
    <tr class="collapse acm-notimplemented">
      <td>PurchaseReservedNodeOffering</td>
       <td style="text-align:right">-</td>
    </tr>
    <tr class="collapse acm-notimplemented">
      <td>RebootCluster</td>
       <td style="text-align:right">-</td>
    </tr>
    <tr class="collapse acm-notimplemented">
      <td>RejectDataShare</td>
       <td style="text-align:right">-</td>
    </tr>
    <tr class="collapse acm-notimplemented">
      <td>ResetClusterParameterGroup</td>
       <td style="text-align:right">-</td>
    </tr>
    <tr class="collapse acm-notimplemented">
      <td>ResizeCluster</td>
       <td style="text-align:right">-</td>
    </tr>
    <tr class="collapse acm-notimplemented">
      <td>RestoreTableFromClusterSnapshot</td>
       <td style="text-align:right">-</td>
    </tr>
    <tr class="collapse acm-notimplemented">
      <td>RevokeClusterSecurityGroupIngress</td>
       <td style="text-align:right">-</td>
    </tr>
    <tr class="collapse acm-notimplemented">
      <td>RevokeEndpointAccess</td>
       <td style="text-align:right">-</td>
    </tr>
    <tr class="collapse acm-notimplemented">
      <td>RevokeSnapshotAccess</td>
       <td style="text-align:right">-</td>
    </tr>
    <tr class="collapse acm-notimplemented">
      <td>RotateEncryptionKey</td>
       <td style="text-align:right">-</td>
    </tr>
    <tr class="collapse acm-notimplemented">
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
      <td>DescribeStatement <a href="#misc" title="covered by our integration test suite">✨</a></td>
       <td style="text-align:right">✅</td>
    </tr>
    <tr>
      <td>DescribeTable <a href="#misc" title="covered by our integration test suite">✨</a></td>
       <td style="text-align:right">✅</td>
    </tr>
    <tr>
      <td>ExecuteStatement <a href="#misc" title="covered by our integration test suite">✨</a></td>
       <td style="text-align:right">✅</td>
    </tr>
    <tr>
      <td>GetStatementResult <a href="#misc" title="covered by our integration test suite">✨</a></td>
       <td style="text-align:right">✅</td>
    </tr>
    <tr>
      <td>ListDatabases <a href="#misc" title="covered by our integration test suite">✨</a></td>
       <td style="text-align:right">✅</td>
    </tr>
    <tr>
      <td><a data-toggle="collapse" href=".acm-notimplemented">Show more</a></td>
      <td style="text-align:right"></td>
    </tr>
    <tr class="collapse acm-notimplemented">
      <td>BatchExecuteStatement</td>
       <td style="text-align:right">-</td>
    </tr>
    <tr class="collapse acm-notimplemented">
      <td>CancelStatement</td>
       <td style="text-align:right">-</td>
    </tr>
    <tr class="collapse acm-notimplemented">
      <td>ListSchemas</td>
       <td style="text-align:right">-</td>
    </tr>
    <tr class="collapse acm-notimplemented">
      <td>ListStatements</td>
       <td style="text-align:right">-</td>
    </tr>
    <tr class="collapse acm-notimplemented">
      <td>ListTables</td>
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
      <td>GetTags</td>
       <td style="text-align:right">✅</td>
    </tr>
    <tr>
      <td>GroupResources</td>
       <td style="text-align:right">✅</td>
    </tr>
    <tr>
      <td>ListGroupResources</td>
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
      <td>SearchResources</td>
       <td style="text-align:right">✅</td>
    </tr>
    <tr>
      <td>UngroupResources</td>
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
    <tr>
      <td><a data-toggle="collapse" href=".acm-notimplemented">Show more</a></td>
      <td style="text-align:right"></td>
    </tr>
    <tr class="collapse acm-notimplemented">
      <td>Tag</td>
       <td style="text-align:right">-</td>
    </tr>
    <tr class="collapse acm-notimplemented">
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
    <tr>
      <td><a data-toggle="collapse" href=".acm-notimplemented">Show more</a></td>
      <td style="text-align:right"></td>
    </tr>
    <tr class="collapse acm-notimplemented">
      <td>DescribeReportCreation</td>
       <td style="text-align:right">-</td>
    </tr>
    <tr class="collapse acm-notimplemented">
      <td>GetComplianceSummary</td>
       <td style="text-align:right">-</td>
    </tr>
    <tr class="collapse acm-notimplemented">
      <td>StartReportCreation</td>
       <td style="text-align:right">-</td>
    </tr>
    <tr class="collapse acm-notimplemented">
      <td>TagResources</td>
       <td style="text-align:right">-</td>
    </tr>
    <tr class="collapse acm-notimplemented">
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
      <td>ActivateKeySigningKey</td>
       <td style="text-align:right">✅</td>
    </tr>
    <tr>
      <td>AssociateVPCWithHostedZone <a href="#misc" title="covered by our integration test suite">✨</a></td>
       <td style="text-align:right">✅</td>
    </tr>
    <tr>
      <td>ChangeCidrCollection</td>
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
      <td>CreateCidrCollection</td>
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
      <td>CreateKeySigningKey</td>
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
      <td>CreateTrafficPolicy</td>
       <td style="text-align:right">✅</td>
    </tr>
    <tr>
      <td>CreateTrafficPolicyInstance</td>
       <td style="text-align:right">✅</td>
    </tr>
    <tr>
      <td>CreateTrafficPolicyVersion</td>
       <td style="text-align:right">✅</td>
    </tr>
    <tr>
      <td>CreateVPCAssociationAuthorization</td>
       <td style="text-align:right">✅</td>
    </tr>
    <tr>
      <td>DeactivateKeySigningKey</td>
       <td style="text-align:right">✅</td>
    </tr>
    <tr>
      <td>DeleteCidrCollection</td>
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
      <td>DeleteKeySigningKey</td>
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
      <td>DeleteTrafficPolicy</td>
       <td style="text-align:right">✅</td>
    </tr>
    <tr>
      <td>DeleteTrafficPolicyInstance</td>
       <td style="text-align:right">✅</td>
    </tr>
    <tr>
      <td>DeleteVPCAssociationAuthorization</td>
       <td style="text-align:right">✅</td>
    </tr>
    <tr>
      <td>DisableHostedZoneDNSSEC</td>
       <td style="text-align:right">✅</td>
    </tr>
    <tr>
      <td>DisassociateVPCFromHostedZone <a href="#misc" title="covered by our integration test suite">✨</a></td>
       <td style="text-align:right">✅</td>
    </tr>
    <tr>
      <td>EnableHostedZoneDNSSEC</td>
       <td style="text-align:right">✅</td>
    </tr>
    <tr>
      <td>GetAccountLimit</td>
       <td style="text-align:right">✅</td>
    </tr>
    <tr>
      <td>GetChange <a href="#misc" title="covered by our integration test suite">✨</a></td>
       <td style="text-align:right">✅</td>
    </tr>
    <tr>
      <td>GetCheckerIpRanges</td>
       <td style="text-align:right">✅</td>
    </tr>
    <tr>
      <td>GetDNSSEC</td>
       <td style="text-align:right">✅</td>
    </tr>
    <tr>
      <td>GetGeoLocation</td>
       <td style="text-align:right">✅</td>
    </tr>
    <tr>
      <td>GetHealthCheck <a href="#misc" title="covered by our integration test suite">✨</a></td>
       <td style="text-align:right">✅</td>
    </tr>
    <tr>
      <td>GetHealthCheckCount</td>
       <td style="text-align:right">✅</td>
    </tr>
    <tr>
      <td>GetHealthCheckLastFailureReason</td>
       <td style="text-align:right">✅</td>
    </tr>
    <tr>
      <td>GetHealthCheckStatus</td>
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
      <td>GetHostedZoneLimit</td>
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
      <td>GetReusableDelegationSetLimit</td>
       <td style="text-align:right">✅</td>
    </tr>
    <tr>
      <td>GetTrafficPolicy</td>
       <td style="text-align:right">✅</td>
    </tr>
    <tr>
      <td>GetTrafficPolicyInstance</td>
       <td style="text-align:right">✅</td>
    </tr>
    <tr>
      <td>GetTrafficPolicyInstanceCount</td>
       <td style="text-align:right">✅</td>
    </tr>
    <tr>
      <td>ListCidrBlocks</td>
       <td style="text-align:right">✅</td>
    </tr>
    <tr>
      <td>ListCidrCollections</td>
       <td style="text-align:right">✅</td>
    </tr>
    <tr>
      <td>ListCidrLocations</td>
       <td style="text-align:right">✅</td>
    </tr>
    <tr>
      <td>ListGeoLocations</td>
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
      <td>ListTagsForResources</td>
       <td style="text-align:right">✅</td>
    </tr>
    <tr>
      <td>ListTrafficPolicies</td>
       <td style="text-align:right">✅</td>
    </tr>
    <tr>
      <td>ListTrafficPolicyInstances</td>
       <td style="text-align:right">✅</td>
    </tr>
    <tr>
      <td>ListTrafficPolicyInstancesByHostedZone</td>
       <td style="text-align:right">✅</td>
    </tr>
    <tr>
      <td>ListTrafficPolicyInstancesByPolicy</td>
       <td style="text-align:right">✅</td>
    </tr>
    <tr>
      <td>ListTrafficPolicyVersions</td>
       <td style="text-align:right">✅</td>
    </tr>
    <tr>
      <td>ListVPCAssociationAuthorizations</td>
       <td style="text-align:right">✅</td>
    </tr>
    <tr>
      <td>TestDNSAnswer</td>
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
    <tr>
      <td>UpdateTrafficPolicyComment</td>
       <td style="text-align:right">✅</td>
    </tr>
    <tr>
      <td>UpdateTrafficPolicyInstance</td>
       <td style="text-align:right">✅</td>
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
      <td>AssociateResolverRule</td>
       <td style="text-align:right">✅</td>
    </tr>
    <tr>
      <td>CreateResolverEndpoint <a href="#misc" title="covered by our integration test suite">✨</a></td>
       <td style="text-align:right">✅</td>
    </tr>
    <tr>
      <td>CreateResolverRule</td>
       <td style="text-align:right">✅</td>
    </tr>
    <tr>
      <td>DeleteResolverEndpoint</td>
       <td style="text-align:right">✅</td>
    </tr>
    <tr>
      <td>DeleteResolverRule</td>
       <td style="text-align:right">✅</td>
    </tr>
    <tr>
      <td>DisassociateResolverRule</td>
       <td style="text-align:right">✅</td>
    </tr>
    <tr>
      <td>GetResolverEndpoint</td>
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
      <td>ListResolverEndpointIpAddresses</td>
       <td style="text-align:right">✅</td>
    </tr>
    <tr>
      <td>ListResolverEndpoints</td>
       <td style="text-align:right">✅</td>
    </tr>
    <tr>
      <td>ListResolverRuleAssociations</td>
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
      <td>UpdateResolverEndpoint</td>
       <td style="text-align:right">✅</td>
    </tr>
    <tr>
      <td><a data-toggle="collapse" href=".acm-notimplemented">Show more</a></td>
      <td style="text-align:right"></td>
    </tr>
    <tr class="collapse acm-notimplemented">
      <td>AssociateFirewallRuleGroup</td>
       <td style="text-align:right">-</td>
    </tr>
    <tr class="collapse acm-notimplemented">
      <td>AssociateResolverEndpointIpAddress</td>
       <td style="text-align:right">-</td>
    </tr>
    <tr class="collapse acm-notimplemented">
      <td>AssociateResolverQueryLogConfig</td>
       <td style="text-align:right">-</td>
    </tr>
    <tr class="collapse acm-notimplemented">
      <td>CreateFirewallDomainList</td>
       <td style="text-align:right">-</td>
    </tr>
    <tr class="collapse acm-notimplemented">
      <td>CreateFirewallRule</td>
       <td style="text-align:right">-</td>
    </tr>
    <tr class="collapse acm-notimplemented">
      <td>CreateFirewallRuleGroup</td>
       <td style="text-align:right">-</td>
    </tr>
    <tr class="collapse acm-notimplemented">
      <td>CreateResolverQueryLogConfig</td>
       <td style="text-align:right">-</td>
    </tr>
    <tr class="collapse acm-notimplemented">
      <td>DeleteFirewallDomainList</td>
       <td style="text-align:right">-</td>
    </tr>
    <tr class="collapse acm-notimplemented">
      <td>DeleteFirewallRule</td>
       <td style="text-align:right">-</td>
    </tr>
    <tr class="collapse acm-notimplemented">
      <td>DeleteFirewallRuleGroup</td>
       <td style="text-align:right">-</td>
    </tr>
    <tr class="collapse acm-notimplemented">
      <td>DeleteResolverQueryLogConfig</td>
       <td style="text-align:right">-</td>
    </tr>
    <tr class="collapse acm-notimplemented">
      <td>DisassociateFirewallRuleGroup</td>
       <td style="text-align:right">-</td>
    </tr>
    <tr class="collapse acm-notimplemented">
      <td>DisassociateResolverEndpointIpAddress</td>
       <td style="text-align:right">-</td>
    </tr>
    <tr class="collapse acm-notimplemented">
      <td>DisassociateResolverQueryLogConfig</td>
       <td style="text-align:right">-</td>
    </tr>
    <tr class="collapse acm-notimplemented">
      <td>GetFirewallConfig</td>
       <td style="text-align:right">-</td>
    </tr>
    <tr class="collapse acm-notimplemented">
      <td>GetFirewallDomainList</td>
       <td style="text-align:right">-</td>
    </tr>
    <tr class="collapse acm-notimplemented">
      <td>GetFirewallRuleGroup</td>
       <td style="text-align:right">-</td>
    </tr>
    <tr class="collapse acm-notimplemented">
      <td>GetFirewallRuleGroupAssociation</td>
       <td style="text-align:right">-</td>
    </tr>
    <tr class="collapse acm-notimplemented">
      <td>GetFirewallRuleGroupPolicy</td>
       <td style="text-align:right">-</td>
    </tr>
    <tr class="collapse acm-notimplemented">
      <td>GetResolverConfig</td>
       <td style="text-align:right">-</td>
    </tr>
    <tr class="collapse acm-notimplemented">
      <td>GetResolverDnssecConfig</td>
       <td style="text-align:right">-</td>
    </tr>
    <tr class="collapse acm-notimplemented">
      <td>GetResolverQueryLogConfig</td>
       <td style="text-align:right">-</td>
    </tr>
    <tr class="collapse acm-notimplemented">
      <td>GetResolverQueryLogConfigAssociation</td>
       <td style="text-align:right">-</td>
    </tr>
    <tr class="collapse acm-notimplemented">
      <td>GetResolverQueryLogConfigPolicy</td>
       <td style="text-align:right">-</td>
    </tr>
    <tr class="collapse acm-notimplemented">
      <td>GetResolverRulePolicy</td>
       <td style="text-align:right">-</td>
    </tr>
    <tr class="collapse acm-notimplemented">
      <td>ImportFirewallDomains</td>
       <td style="text-align:right">-</td>
    </tr>
    <tr class="collapse acm-notimplemented">
      <td>ListFirewallConfigs</td>
       <td style="text-align:right">-</td>
    </tr>
    <tr class="collapse acm-notimplemented">
      <td>ListFirewallDomainLists</td>
       <td style="text-align:right">-</td>
    </tr>
    <tr class="collapse acm-notimplemented">
      <td>ListFirewallDomains</td>
       <td style="text-align:right">-</td>
    </tr>
    <tr class="collapse acm-notimplemented">
      <td>ListFirewallRuleGroupAssociations</td>
       <td style="text-align:right">-</td>
    </tr>
    <tr class="collapse acm-notimplemented">
      <td>ListFirewallRuleGroups</td>
       <td style="text-align:right">-</td>
    </tr>
    <tr class="collapse acm-notimplemented">
      <td>ListFirewallRules</td>
       <td style="text-align:right">-</td>
    </tr>
    <tr class="collapse acm-notimplemented">
      <td>ListResolverConfigs</td>
       <td style="text-align:right">-</td>
    </tr>
    <tr class="collapse acm-notimplemented">
      <td>ListResolverDnssecConfigs</td>
       <td style="text-align:right">-</td>
    </tr>
    <tr class="collapse acm-notimplemented">
      <td>ListResolverQueryLogConfigAssociations</td>
       <td style="text-align:right">-</td>
    </tr>
    <tr class="collapse acm-notimplemented">
      <td>ListResolverQueryLogConfigs</td>
       <td style="text-align:right">-</td>
    </tr>
    <tr class="collapse acm-notimplemented">
      <td>PutFirewallRuleGroupPolicy</td>
       <td style="text-align:right">-</td>
    </tr>
    <tr class="collapse acm-notimplemented">
      <td>PutResolverQueryLogConfigPolicy</td>
       <td style="text-align:right">-</td>
    </tr>
    <tr class="collapse acm-notimplemented">
      <td>PutResolverRulePolicy</td>
       <td style="text-align:right">-</td>
    </tr>
    <tr class="collapse acm-notimplemented">
      <td>UpdateFirewallConfig</td>
       <td style="text-align:right">-</td>
    </tr>
    <tr class="collapse acm-notimplemented">
      <td>UpdateFirewallDomains</td>
       <td style="text-align:right">-</td>
    </tr>
    <tr class="collapse acm-notimplemented">
      <td>UpdateFirewallRule</td>
       <td style="text-align:right">-</td>
    </tr>
    <tr class="collapse acm-notimplemented">
      <td>UpdateFirewallRuleGroupAssociation</td>
       <td style="text-align:right">-</td>
    </tr>
    <tr class="collapse acm-notimplemented">
      <td>UpdateResolverConfig</td>
       <td style="text-align:right">-</td>
    </tr>
    <tr class="collapse acm-notimplemented">
      <td>UpdateResolverDnssecConfig</td>
       <td style="text-align:right">-</td>
    </tr>
    <tr class="collapse acm-notimplemented">
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
      <td>DeleteBucketWebsite</td>
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
      <td>GetObjectAcl <a href="#misc" title="covered by our integration test suite">✨</a></td>
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
      <td>ListParts</td>
       <td style="text-align:right">✅</td>
    </tr>
    <tr>
      <td>PutBucketAccelerateConfiguration</td>
       <td style="text-align:right">✅</td>
    </tr>
    <tr>
      <td>PutBucketAcl</td>
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
      <td>CreateAccessPointForObjectLambda</td>
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
      <td>CreateMultiRegionAccessPoint</td>
       <td style="text-align:right">✅</td>
    </tr>
    <tr>
      <td>DeleteAccessPoint</td>
       <td style="text-align:right">✅</td>
    </tr>
    <tr>
      <td>DeleteAccessPointForObjectLambda</td>
       <td style="text-align:right">✅</td>
    </tr>
    <tr>
      <td>DeleteAccessPointPolicy</td>
       <td style="text-align:right">✅</td>
    </tr>
    <tr>
      <td>DeleteAccessPointPolicyForObjectLambda</td>
       <td style="text-align:right">✅</td>
    </tr>
    <tr>
      <td>DeleteBucket</td>
       <td style="text-align:right">✅</td>
    </tr>
    <tr>
      <td>DeleteBucketLifecycleConfiguration</td>
       <td style="text-align:right">✅</td>
    </tr>
    <tr>
      <td>DeleteBucketPolicy</td>
       <td style="text-align:right">✅</td>
    </tr>
    <tr>
      <td>DeleteBucketTagging</td>
       <td style="text-align:right">✅</td>
    </tr>
    <tr>
      <td>DeleteJobTagging</td>
       <td style="text-align:right">✅</td>
    </tr>
    <tr>
      <td>DeleteMultiRegionAccessPoint</td>
       <td style="text-align:right">✅</td>
    </tr>
    <tr>
      <td>DeletePublicAccessBlock <a href="#misc" title="covered by our integration test suite">✨</a></td>
       <td style="text-align:right">✅</td>
    </tr>
    <tr>
      <td>DeleteStorageLensConfiguration</td>
       <td style="text-align:right">✅</td>
    </tr>
    <tr>
      <td>DeleteStorageLensConfigurationTagging</td>
       <td style="text-align:right">✅</td>
    </tr>
    <tr>
      <td>DescribeJob</td>
       <td style="text-align:right">✅</td>
    </tr>
    <tr>
      <td>DescribeMultiRegionAccessPointOperation</td>
       <td style="text-align:right">✅</td>
    </tr>
    <tr>
      <td>GetAccessPoint</td>
       <td style="text-align:right">✅</td>
    </tr>
    <tr>
      <td>GetAccessPointConfigurationForObjectLambda</td>
       <td style="text-align:right">✅</td>
    </tr>
    <tr>
      <td>GetAccessPointForObjectLambda</td>
       <td style="text-align:right">✅</td>
    </tr>
    <tr>
      <td>GetAccessPointPolicy</td>
       <td style="text-align:right">✅</td>
    </tr>
    <tr>
      <td>GetAccessPointPolicyForObjectLambda</td>
       <td style="text-align:right">✅</td>
    </tr>
    <tr>
      <td>GetAccessPointPolicyStatus</td>
       <td style="text-align:right">✅</td>
    </tr>
    <tr>
      <td>GetAccessPointPolicyStatusForObjectLambda</td>
       <td style="text-align:right">✅</td>
    </tr>
    <tr>
      <td>GetBucket</td>
       <td style="text-align:right">✅</td>
    </tr>
    <tr>
      <td>GetBucketLifecycleConfiguration</td>
       <td style="text-align:right">✅</td>
    </tr>
    <tr>
      <td>GetBucketPolicy</td>
       <td style="text-align:right">✅</td>
    </tr>
    <tr>
      <td>GetBucketTagging</td>
       <td style="text-align:right">✅</td>
    </tr>
    <tr>
      <td>GetJobTagging</td>
       <td style="text-align:right">✅</td>
    </tr>
    <tr>
      <td>GetMultiRegionAccessPoint</td>
       <td style="text-align:right">✅</td>
    </tr>
    <tr>
      <td>GetMultiRegionAccessPointPolicy</td>
       <td style="text-align:right">✅</td>
    </tr>
    <tr>
      <td>GetMultiRegionAccessPointPolicyStatus</td>
       <td style="text-align:right">✅</td>
    </tr>
    <tr>
      <td>GetPublicAccessBlock <a href="#misc" title="covered by our integration test suite">✨</a></td>
       <td style="text-align:right">✅</td>
    </tr>
    <tr>
      <td>GetStorageLensConfiguration</td>
       <td style="text-align:right">✅</td>
    </tr>
    <tr>
      <td>GetStorageLensConfigurationTagging</td>
       <td style="text-align:right">✅</td>
    </tr>
    <tr>
      <td>ListAccessPoints</td>
       <td style="text-align:right">✅</td>
    </tr>
    <tr>
      <td>ListAccessPointsForObjectLambda</td>
       <td style="text-align:right">✅</td>
    </tr>
    <tr>
      <td>ListJobs</td>
       <td style="text-align:right">✅</td>
    </tr>
    <tr>
      <td>ListMultiRegionAccessPoints</td>
       <td style="text-align:right">✅</td>
    </tr>
    <tr>
      <td>ListRegionalBuckets</td>
       <td style="text-align:right">✅</td>
    </tr>
    <tr>
      <td>ListStorageLensConfigurations</td>
       <td style="text-align:right">✅</td>
    </tr>
    <tr>
      <td>PutAccessPointConfigurationForObjectLambda</td>
       <td style="text-align:right">✅</td>
    </tr>
    <tr>
      <td>PutAccessPointPolicy</td>
       <td style="text-align:right">✅</td>
    </tr>
    <tr>
      <td>PutAccessPointPolicyForObjectLambda</td>
       <td style="text-align:right">✅</td>
    </tr>
    <tr>
      <td>PutBucketLifecycleConfiguration</td>
       <td style="text-align:right">✅</td>
    </tr>
    <tr>
      <td>PutBucketPolicy</td>
       <td style="text-align:right">✅</td>
    </tr>
    <tr>
      <td>PutBucketTagging</td>
       <td style="text-align:right">✅</td>
    </tr>
    <tr>
      <td>PutJobTagging</td>
       <td style="text-align:right">✅</td>
    </tr>
    <tr>
      <td>PutMultiRegionAccessPointPolicy</td>
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
    <tr>
      <td>PutStorageLensConfigurationTagging</td>
       <td style="text-align:right">✅</td>
    </tr>
    <tr>
      <td>UpdateJobPriority</td>
       <td style="text-align:right">✅</td>
    </tr>
    <tr>
      <td>UpdateJobStatus</td>
       <td style="text-align:right">✅</td>
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
      <td>AddTags</td>
       <td style="text-align:right">✅</td>
    </tr>
    <tr>
      <td>AssociateTrialComponent</td>
       <td style="text-align:right">✅</td>
    </tr>
    <tr>
      <td>CreateEndpoint</td>
       <td style="text-align:right">✅</td>
    </tr>
    <tr>
      <td>CreateEndpointConfig</td>
       <td style="text-align:right">✅</td>
    </tr>
    <tr>
      <td>CreateExperiment</td>
       <td style="text-align:right">✅</td>
    </tr>
    <tr>
      <td>CreateModel <a href="#misc" title="covered by our integration test suite">✨</a></td>
       <td style="text-align:right">✅</td>
    </tr>
    <tr>
      <td>CreateNotebookInstance</td>
       <td style="text-align:right">✅</td>
    </tr>
    <tr>
      <td>CreateNotebookInstanceLifecycleConfig</td>
       <td style="text-align:right">✅</td>
    </tr>
    <tr>
      <td>CreateProcessingJob</td>
       <td style="text-align:right">✅</td>
    </tr>
    <tr>
      <td>CreateTrainingJob</td>
       <td style="text-align:right">✅</td>
    </tr>
    <tr>
      <td>CreateTrial</td>
       <td style="text-align:right">✅</td>
    </tr>
    <tr>
      <td>CreateTrialComponent</td>
       <td style="text-align:right">✅</td>
    </tr>
    <tr>
      <td>DeleteEndpoint</td>
       <td style="text-align:right">✅</td>
    </tr>
    <tr>
      <td>DeleteEndpointConfig</td>
       <td style="text-align:right">✅</td>
    </tr>
    <tr>
      <td>DeleteExperiment</td>
       <td style="text-align:right">✅</td>
    </tr>
    <tr>
      <td>DeleteModel</td>
       <td style="text-align:right">✅</td>
    </tr>
    <tr>
      <td>DeleteNotebookInstance</td>
       <td style="text-align:right">✅</td>
    </tr>
    <tr>
      <td>DeleteNotebookInstanceLifecycleConfig</td>
       <td style="text-align:right">✅</td>
    </tr>
    <tr>
      <td>DeleteTags</td>
       <td style="text-align:right">✅</td>
    </tr>
    <tr>
      <td>DeleteTrial</td>
       <td style="text-align:right">✅</td>
    </tr>
    <tr>
      <td>DeleteTrialComponent</td>
       <td style="text-align:right">✅</td>
    </tr>
    <tr>
      <td>DescribeEndpoint</td>
       <td style="text-align:right">✅</td>
    </tr>
    <tr>
      <td>DescribeEndpointConfig</td>
       <td style="text-align:right">✅</td>
    </tr>
    <tr>
      <td>DescribeExperiment</td>
       <td style="text-align:right">✅</td>
    </tr>
    <tr>
      <td>DescribeModel <a href="#misc" title="covered by our integration test suite">✨</a></td>
       <td style="text-align:right">✅</td>
    </tr>
    <tr>
      <td>DescribeNotebookInstance</td>
       <td style="text-align:right">✅</td>
    </tr>
    <tr>
      <td>DescribeNotebookInstanceLifecycleConfig</td>
       <td style="text-align:right">✅</td>
    </tr>
    <tr>
      <td>DescribeProcessingJob</td>
       <td style="text-align:right">✅</td>
    </tr>
    <tr>
      <td>DescribeTrainingJob</td>
       <td style="text-align:right">✅</td>
    </tr>
    <tr>
      <td>DescribeTrial</td>
       <td style="text-align:right">✅</td>
    </tr>
    <tr>
      <td>DescribeTrialComponent</td>
       <td style="text-align:right">✅</td>
    </tr>
    <tr>
      <td>DisassociateTrialComponent</td>
       <td style="text-align:right">✅</td>
    </tr>
    <tr>
      <td>ListAssociations</td>
       <td style="text-align:right">✅</td>
    </tr>
    <tr>
      <td>ListExperiments</td>
       <td style="text-align:right">✅</td>
    </tr>
    <tr>
      <td>ListModels</td>
       <td style="text-align:right">✅</td>
    </tr>
    <tr>
      <td>ListProcessingJobs</td>
       <td style="text-align:right">✅</td>
    </tr>
    <tr>
      <td>ListTags</td>
       <td style="text-align:right">✅</td>
    </tr>
    <tr>
      <td>ListTrainingJobs</td>
       <td style="text-align:right">✅</td>
    </tr>
    <tr>
      <td>ListTrialComponents</td>
       <td style="text-align:right">✅</td>
    </tr>
    <tr>
      <td>ListTrials</td>
       <td style="text-align:right">✅</td>
    </tr>
    <tr>
      <td>Search</td>
       <td style="text-align:right">✅</td>
    </tr>
    <tr>
      <td>StartNotebookInstance</td>
       <td style="text-align:right">✅</td>
    </tr>
    <tr>
      <td>StopNotebookInstance</td>
       <td style="text-align:right">✅</td>
    </tr>
    <tr>
      <td>UpdateEndpointWeightsAndCapacities</td>
       <td style="text-align:right">✅</td>
    </tr>
    <tr>
      <td><a data-toggle="collapse" href=".acm-notimplemented">Show more</a></td>
      <td style="text-align:right"></td>
    </tr>
    <tr class="collapse acm-notimplemented">
      <td>AddAssociation</td>
       <td style="text-align:right">-</td>
    </tr>
    <tr class="collapse acm-notimplemented">
      <td>BatchDescribeModelPackage</td>
       <td style="text-align:right">-</td>
    </tr>
    <tr class="collapse acm-notimplemented">
      <td>CreateAction</td>
       <td style="text-align:right">-</td>
    </tr>
    <tr class="collapse acm-notimplemented">
      <td>CreateAlgorithm</td>
       <td style="text-align:right">-</td>
    </tr>
    <tr class="collapse acm-notimplemented">
      <td>CreateApp</td>
       <td style="text-align:right">-</td>
    </tr>
    <tr class="collapse acm-notimplemented">
      <td>CreateAppImageConfig</td>
       <td style="text-align:right">-</td>
    </tr>
    <tr class="collapse acm-notimplemented">
      <td>CreateArtifact</td>
       <td style="text-align:right">-</td>
    </tr>
    <tr class="collapse acm-notimplemented">
      <td>CreateAutoMLJob</td>
       <td style="text-align:right">-</td>
    </tr>
    <tr class="collapse acm-notimplemented">
      <td>CreateCodeRepository</td>
       <td style="text-align:right">-</td>
    </tr>
    <tr class="collapse acm-notimplemented">
      <td>CreateCompilationJob</td>
       <td style="text-align:right">-</td>
    </tr>
    <tr class="collapse acm-notimplemented">
      <td>CreateContext</td>
       <td style="text-align:right">-</td>
    </tr>
    <tr class="collapse acm-notimplemented">
      <td>CreateDataQualityJobDefinition</td>
       <td style="text-align:right">-</td>
    </tr>
    <tr class="collapse acm-notimplemented">
      <td>CreateDeviceFleet</td>
       <td style="text-align:right">-</td>
    </tr>
    <tr class="collapse acm-notimplemented">
      <td>CreateDomain</td>
       <td style="text-align:right">-</td>
    </tr>
    <tr class="collapse acm-notimplemented">
      <td>CreateEdgePackagingJob</td>
       <td style="text-align:right">-</td>
    </tr>
    <tr class="collapse acm-notimplemented">
      <td>CreateFeatureGroup</td>
       <td style="text-align:right">-</td>
    </tr>
    <tr class="collapse acm-notimplemented">
      <td>CreateFlowDefinition</td>
       <td style="text-align:right">-</td>
    </tr>
    <tr class="collapse acm-notimplemented">
      <td>CreateHumanTaskUi</td>
       <td style="text-align:right">-</td>
    </tr>
    <tr class="collapse acm-notimplemented">
      <td>CreateHyperParameterTuningJob</td>
       <td style="text-align:right">-</td>
    </tr>
    <tr class="collapse acm-notimplemented">
      <td>CreateImage</td>
       <td style="text-align:right">-</td>
    </tr>
    <tr class="collapse acm-notimplemented">
      <td>CreateImageVersion</td>
       <td style="text-align:right">-</td>
    </tr>
    <tr class="collapse acm-notimplemented">
      <td>CreateInferenceRecommendationsJob</td>
       <td style="text-align:right">-</td>
    </tr>
    <tr class="collapse acm-notimplemented">
      <td>CreateLabelingJob</td>
       <td style="text-align:right">-</td>
    </tr>
    <tr class="collapse acm-notimplemented">
      <td>CreateModelBiasJobDefinition</td>
       <td style="text-align:right">-</td>
    </tr>
    <tr class="collapse acm-notimplemented">
      <td>CreateModelExplainabilityJobDefinition</td>
       <td style="text-align:right">-</td>
    </tr>
    <tr class="collapse acm-notimplemented">
      <td>CreateModelPackage</td>
       <td style="text-align:right">-</td>
    </tr>
    <tr class="collapse acm-notimplemented">
      <td>CreateModelPackageGroup</td>
       <td style="text-align:right">-</td>
    </tr>
    <tr class="collapse acm-notimplemented">
      <td>CreateModelQualityJobDefinition</td>
       <td style="text-align:right">-</td>
    </tr>
    <tr class="collapse acm-notimplemented">
      <td>CreateMonitoringSchedule</td>
       <td style="text-align:right">-</td>
    </tr>
    <tr class="collapse acm-notimplemented">
      <td>CreatePipeline</td>
       <td style="text-align:right">-</td>
    </tr>
    <tr class="collapse acm-notimplemented">
      <td>CreatePresignedDomainUrl</td>
       <td style="text-align:right">-</td>
    </tr>
    <tr class="collapse acm-notimplemented">
      <td>CreatePresignedNotebookInstanceUrl</td>
       <td style="text-align:right">-</td>
    </tr>
    <tr class="collapse acm-notimplemented">
      <td>CreateProject</td>
       <td style="text-align:right">-</td>
    </tr>
    <tr class="collapse acm-notimplemented">
      <td>CreateStudioLifecycleConfig</td>
       <td style="text-align:right">-</td>
    </tr>
    <tr class="collapse acm-notimplemented">
      <td>CreateTransformJob</td>
       <td style="text-align:right">-</td>
    </tr>
    <tr class="collapse acm-notimplemented">
      <td>CreateUserProfile</td>
       <td style="text-align:right">-</td>
    </tr>
    <tr class="collapse acm-notimplemented">
      <td>CreateWorkforce</td>
       <td style="text-align:right">-</td>
    </tr>
    <tr class="collapse acm-notimplemented">
      <td>CreateWorkteam</td>
       <td style="text-align:right">-</td>
    </tr>
    <tr class="collapse acm-notimplemented">
      <td>DeleteAction</td>
       <td style="text-align:right">-</td>
    </tr>
    <tr class="collapse acm-notimplemented">
      <td>DeleteAlgorithm</td>
       <td style="text-align:right">-</td>
    </tr>
    <tr class="collapse acm-notimplemented">
      <td>DeleteApp</td>
       <td style="text-align:right">-</td>
    </tr>
    <tr class="collapse acm-notimplemented">
      <td>DeleteAppImageConfig</td>
       <td style="text-align:right">-</td>
    </tr>
    <tr class="collapse acm-notimplemented">
      <td>DeleteArtifact</td>
       <td style="text-align:right">-</td>
    </tr>
    <tr class="collapse acm-notimplemented">
      <td>DeleteAssociation</td>
       <td style="text-align:right">-</td>
    </tr>
    <tr class="collapse acm-notimplemented">
      <td>DeleteCodeRepository</td>
       <td style="text-align:right">-</td>
    </tr>
    <tr class="collapse acm-notimplemented">
      <td>DeleteContext</td>
       <td style="text-align:right">-</td>
    </tr>
    <tr class="collapse acm-notimplemented">
      <td>DeleteDataQualityJobDefinition</td>
       <td style="text-align:right">-</td>
    </tr>
    <tr class="collapse acm-notimplemented">
      <td>DeleteDeviceFleet</td>
       <td style="text-align:right">-</td>
    </tr>
    <tr class="collapse acm-notimplemented">
      <td>DeleteDomain</td>
       <td style="text-align:right">-</td>
    </tr>
    <tr class="collapse acm-notimplemented">
      <td>DeleteFeatureGroup</td>
       <td style="text-align:right">-</td>
    </tr>
    <tr class="collapse acm-notimplemented">
      <td>DeleteFlowDefinition</td>
       <td style="text-align:right">-</td>
    </tr>
    <tr class="collapse acm-notimplemented">
      <td>DeleteHumanTaskUi</td>
       <td style="text-align:right">-</td>
    </tr>
    <tr class="collapse acm-notimplemented">
      <td>DeleteImage</td>
       <td style="text-align:right">-</td>
    </tr>
    <tr class="collapse acm-notimplemented">
      <td>DeleteImageVersion</td>
       <td style="text-align:right">-</td>
    </tr>
    <tr class="collapse acm-notimplemented">
      <td>DeleteModelBiasJobDefinition</td>
       <td style="text-align:right">-</td>
    </tr>
    <tr class="collapse acm-notimplemented">
      <td>DeleteModelExplainabilityJobDefinition</td>
       <td style="text-align:right">-</td>
    </tr>
    <tr class="collapse acm-notimplemented">
      <td>DeleteModelPackage</td>
       <td style="text-align:right">-</td>
    </tr>
    <tr class="collapse acm-notimplemented">
      <td>DeleteModelPackageGroup</td>
       <td style="text-align:right">-</td>
    </tr>
    <tr class="collapse acm-notimplemented">
      <td>DeleteModelPackageGroupPolicy</td>
       <td style="text-align:right">-</td>
    </tr>
    <tr class="collapse acm-notimplemented">
      <td>DeleteModelQualityJobDefinition</td>
       <td style="text-align:right">-</td>
    </tr>
    <tr class="collapse acm-notimplemented">
      <td>DeleteMonitoringSchedule</td>
       <td style="text-align:right">-</td>
    </tr>
    <tr class="collapse acm-notimplemented">
      <td>DeletePipeline</td>
       <td style="text-align:right">-</td>
    </tr>
    <tr class="collapse acm-notimplemented">
      <td>DeleteProject</td>
       <td style="text-align:right">-</td>
    </tr>
    <tr class="collapse acm-notimplemented">
      <td>DeleteStudioLifecycleConfig</td>
       <td style="text-align:right">-</td>
    </tr>
    <tr class="collapse acm-notimplemented">
      <td>DeleteUserProfile</td>
       <td style="text-align:right">-</td>
    </tr>
    <tr class="collapse acm-notimplemented">
      <td>DeleteWorkforce</td>
       <td style="text-align:right">-</td>
    </tr>
    <tr class="collapse acm-notimplemented">
      <td>DeleteWorkteam</td>
       <td style="text-align:right">-</td>
    </tr>
    <tr class="collapse acm-notimplemented">
      <td>DeregisterDevices</td>
       <td style="text-align:right">-</td>
    </tr>
    <tr class="collapse acm-notimplemented">
      <td>DescribeAction</td>
       <td style="text-align:right">-</td>
    </tr>
    <tr class="collapse acm-notimplemented">
      <td>DescribeAlgorithm</td>
       <td style="text-align:right">-</td>
    </tr>
    <tr class="collapse acm-notimplemented">
      <td>DescribeApp</td>
       <td style="text-align:right">-</td>
    </tr>
    <tr class="collapse acm-notimplemented">
      <td>DescribeAppImageConfig</td>
       <td style="text-align:right">-</td>
    </tr>
    <tr class="collapse acm-notimplemented">
      <td>DescribeArtifact</td>
       <td style="text-align:right">-</td>
    </tr>
    <tr class="collapse acm-notimplemented">
      <td>DescribeAutoMLJob</td>
       <td style="text-align:right">-</td>
    </tr>
    <tr class="collapse acm-notimplemented">
      <td>DescribeCodeRepository</td>
       <td style="text-align:right">-</td>
    </tr>
    <tr class="collapse acm-notimplemented">
      <td>DescribeCompilationJob</td>
       <td style="text-align:right">-</td>
    </tr>
    <tr class="collapse acm-notimplemented">
      <td>DescribeContext</td>
       <td style="text-align:right">-</td>
    </tr>
    <tr class="collapse acm-notimplemented">
      <td>DescribeDataQualityJobDefinition</td>
       <td style="text-align:right">-</td>
    </tr>
    <tr class="collapse acm-notimplemented">
      <td>DescribeDevice</td>
       <td style="text-align:right">-</td>
    </tr>
    <tr class="collapse acm-notimplemented">
      <td>DescribeDeviceFleet</td>
       <td style="text-align:right">-</td>
    </tr>
    <tr class="collapse acm-notimplemented">
      <td>DescribeDomain</td>
       <td style="text-align:right">-</td>
    </tr>
    <tr class="collapse acm-notimplemented">
      <td>DescribeEdgePackagingJob</td>
       <td style="text-align:right">-</td>
    </tr>
    <tr class="collapse acm-notimplemented">
      <td>DescribeFeatureGroup</td>
       <td style="text-align:right">-</td>
    </tr>
    <tr class="collapse acm-notimplemented">
      <td>DescribeFeatureMetadata</td>
       <td style="text-align:right">-</td>
    </tr>
    <tr class="collapse acm-notimplemented">
      <td>DescribeFlowDefinition</td>
       <td style="text-align:right">-</td>
    </tr>
    <tr class="collapse acm-notimplemented">
      <td>DescribeHumanTaskUi</td>
       <td style="text-align:right">-</td>
    </tr>
    <tr class="collapse acm-notimplemented">
      <td>DescribeHyperParameterTuningJob</td>
       <td style="text-align:right">-</td>
    </tr>
    <tr class="collapse acm-notimplemented">
      <td>DescribeImage</td>
       <td style="text-align:right">-</td>
    </tr>
    <tr class="collapse acm-notimplemented">
      <td>DescribeImageVersion</td>
       <td style="text-align:right">-</td>
    </tr>
    <tr class="collapse acm-notimplemented">
      <td>DescribeInferenceRecommendationsJob</td>
       <td style="text-align:right">-</td>
    </tr>
    <tr class="collapse acm-notimplemented">
      <td>DescribeLabelingJob</td>
       <td style="text-align:right">-</td>
    </tr>
    <tr class="collapse acm-notimplemented">
      <td>DescribeLineageGroup</td>
       <td style="text-align:right">-</td>
    </tr>
    <tr class="collapse acm-notimplemented">
      <td>DescribeModelBiasJobDefinition</td>
       <td style="text-align:right">-</td>
    </tr>
    <tr class="collapse acm-notimplemented">
      <td>DescribeModelExplainabilityJobDefinition</td>
       <td style="text-align:right">-</td>
    </tr>
    <tr class="collapse acm-notimplemented">
      <td>DescribeModelPackage</td>
       <td style="text-align:right">-</td>
    </tr>
    <tr class="collapse acm-notimplemented">
      <td>DescribeModelPackageGroup</td>
       <td style="text-align:right">-</td>
    </tr>
    <tr class="collapse acm-notimplemented">
      <td>DescribeModelQualityJobDefinition</td>
       <td style="text-align:right">-</td>
    </tr>
    <tr class="collapse acm-notimplemented">
      <td>DescribeMonitoringSchedule</td>
       <td style="text-align:right">-</td>
    </tr>
    <tr class="collapse acm-notimplemented">
      <td>DescribePipeline</td>
       <td style="text-align:right">-</td>
    </tr>
    <tr class="collapse acm-notimplemented">
      <td>DescribePipelineDefinitionForExecution</td>
       <td style="text-align:right">-</td>
    </tr>
    <tr class="collapse acm-notimplemented">
      <td>DescribePipelineExecution</td>
       <td style="text-align:right">-</td>
    </tr>
    <tr class="collapse acm-notimplemented">
      <td>DescribeProject</td>
       <td style="text-align:right">-</td>
    </tr>
    <tr class="collapse acm-notimplemented">
      <td>DescribeStudioLifecycleConfig</td>
       <td style="text-align:right">-</td>
    </tr>
    <tr class="collapse acm-notimplemented">
      <td>DescribeSubscribedWorkteam</td>
       <td style="text-align:right">-</td>
    </tr>
    <tr class="collapse acm-notimplemented">
      <td>DescribeTransformJob</td>
       <td style="text-align:right">-</td>
    </tr>
    <tr class="collapse acm-notimplemented">
      <td>DescribeUserProfile</td>
       <td style="text-align:right">-</td>
    </tr>
    <tr class="collapse acm-notimplemented">
      <td>DescribeWorkforce</td>
       <td style="text-align:right">-</td>
    </tr>
    <tr class="collapse acm-notimplemented">
      <td>DescribeWorkteam</td>
       <td style="text-align:right">-</td>
    </tr>
    <tr class="collapse acm-notimplemented">
      <td>DisableSagemakerServicecatalogPortfolio</td>
       <td style="text-align:right">-</td>
    </tr>
    <tr class="collapse acm-notimplemented">
      <td>EnableSagemakerServicecatalogPortfolio</td>
       <td style="text-align:right">-</td>
    </tr>
    <tr class="collapse acm-notimplemented">
      <td>GetDeviceFleetReport</td>
       <td style="text-align:right">-</td>
    </tr>
    <tr class="collapse acm-notimplemented">
      <td>GetLineageGroupPolicy</td>
       <td style="text-align:right">-</td>
    </tr>
    <tr class="collapse acm-notimplemented">
      <td>GetModelPackageGroupPolicy</td>
       <td style="text-align:right">-</td>
    </tr>
    <tr class="collapse acm-notimplemented">
      <td>GetSagemakerServicecatalogPortfolioStatus</td>
       <td style="text-align:right">-</td>
    </tr>
    <tr class="collapse acm-notimplemented">
      <td>GetSearchSuggestions</td>
       <td style="text-align:right">-</td>
    </tr>
    <tr class="collapse acm-notimplemented">
      <td>ListActions</td>
       <td style="text-align:right">-</td>
    </tr>
    <tr class="collapse acm-notimplemented">
      <td>ListAlgorithms</td>
       <td style="text-align:right">-</td>
    </tr>
    <tr class="collapse acm-notimplemented">
      <td>ListAppImageConfigs</td>
       <td style="text-align:right">-</td>
    </tr>
    <tr class="collapse acm-notimplemented">
      <td>ListApps</td>
       <td style="text-align:right">-</td>
    </tr>
    <tr class="collapse acm-notimplemented">
      <td>ListArtifacts</td>
       <td style="text-align:right">-</td>
    </tr>
    <tr class="collapse acm-notimplemented">
      <td>ListAutoMLJobs</td>
       <td style="text-align:right">-</td>
    </tr>
    <tr class="collapse acm-notimplemented">
      <td>ListCandidatesForAutoMLJob</td>
       <td style="text-align:right">-</td>
    </tr>
    <tr class="collapse acm-notimplemented">
      <td>ListCodeRepositories</td>
       <td style="text-align:right">-</td>
    </tr>
    <tr class="collapse acm-notimplemented">
      <td>ListCompilationJobs</td>
       <td style="text-align:right">-</td>
    </tr>
    <tr class="collapse acm-notimplemented">
      <td>ListContexts</td>
       <td style="text-align:right">-</td>
    </tr>
    <tr class="collapse acm-notimplemented">
      <td>ListDataQualityJobDefinitions</td>
       <td style="text-align:right">-</td>
    </tr>
    <tr class="collapse acm-notimplemented">
      <td>ListDeviceFleets</td>
       <td style="text-align:right">-</td>
    </tr>
    <tr class="collapse acm-notimplemented">
      <td>ListDevices</td>
       <td style="text-align:right">-</td>
    </tr>
    <tr class="collapse acm-notimplemented">
      <td>ListDomains</td>
       <td style="text-align:right">-</td>
    </tr>
    <tr class="collapse acm-notimplemented">
      <td>ListEdgePackagingJobs</td>
       <td style="text-align:right">-</td>
    </tr>
    <tr class="collapse acm-notimplemented">
      <td>ListEndpointConfigs</td>
       <td style="text-align:right">-</td>
    </tr>
    <tr class="collapse acm-notimplemented">
      <td>ListEndpoints</td>
       <td style="text-align:right">-</td>
    </tr>
    <tr class="collapse acm-notimplemented">
      <td>ListFeatureGroups</td>
       <td style="text-align:right">-</td>
    </tr>
    <tr class="collapse acm-notimplemented">
      <td>ListFlowDefinitions</td>
       <td style="text-align:right">-</td>
    </tr>
    <tr class="collapse acm-notimplemented">
      <td>ListHumanTaskUis</td>
       <td style="text-align:right">-</td>
    </tr>
    <tr class="collapse acm-notimplemented">
      <td>ListHyperParameterTuningJobs</td>
       <td style="text-align:right">-</td>
    </tr>
    <tr class="collapse acm-notimplemented">
      <td>ListImageVersions</td>
       <td style="text-align:right">-</td>
    </tr>
    <tr class="collapse acm-notimplemented">
      <td>ListImages</td>
       <td style="text-align:right">-</td>
    </tr>
    <tr class="collapse acm-notimplemented">
      <td>ListInferenceRecommendationsJobs</td>
       <td style="text-align:right">-</td>
    </tr>
    <tr class="collapse acm-notimplemented">
      <td>ListLabelingJobs</td>
       <td style="text-align:right">-</td>
    </tr>
    <tr class="collapse acm-notimplemented">
      <td>ListLabelingJobsForWorkteam</td>
       <td style="text-align:right">-</td>
    </tr>
    <tr class="collapse acm-notimplemented">
      <td>ListLineageGroups</td>
       <td style="text-align:right">-</td>
    </tr>
    <tr class="collapse acm-notimplemented">
      <td>ListModelBiasJobDefinitions</td>
       <td style="text-align:right">-</td>
    </tr>
    <tr class="collapse acm-notimplemented">
      <td>ListModelExplainabilityJobDefinitions</td>
       <td style="text-align:right">-</td>
    </tr>
    <tr class="collapse acm-notimplemented">
      <td>ListModelMetadata</td>
       <td style="text-align:right">-</td>
    </tr>
    <tr class="collapse acm-notimplemented">
      <td>ListModelPackageGroups</td>
       <td style="text-align:right">-</td>
    </tr>
    <tr class="collapse acm-notimplemented">
      <td>ListModelPackages</td>
       <td style="text-align:right">-</td>
    </tr>
    <tr class="collapse acm-notimplemented">
      <td>ListModelQualityJobDefinitions</td>
       <td style="text-align:right">-</td>
    </tr>
    <tr class="collapse acm-notimplemented">
      <td>ListMonitoringExecutions</td>
       <td style="text-align:right">-</td>
    </tr>
    <tr class="collapse acm-notimplemented">
      <td>ListMonitoringSchedules</td>
       <td style="text-align:right">-</td>
    </tr>
    <tr class="collapse acm-notimplemented">
      <td>ListNotebookInstanceLifecycleConfigs</td>
       <td style="text-align:right">-</td>
    </tr>
    <tr class="collapse acm-notimplemented">
      <td>ListNotebookInstances</td>
       <td style="text-align:right">-</td>
    </tr>
    <tr class="collapse acm-notimplemented">
      <td>ListPipelineExecutionSteps</td>
       <td style="text-align:right">-</td>
    </tr>
    <tr class="collapse acm-notimplemented">
      <td>ListPipelineExecutions</td>
       <td style="text-align:right">-</td>
    </tr>
    <tr class="collapse acm-notimplemented">
      <td>ListPipelineParametersForExecution</td>
       <td style="text-align:right">-</td>
    </tr>
    <tr class="collapse acm-notimplemented">
      <td>ListPipelines</td>
       <td style="text-align:right">-</td>
    </tr>
    <tr class="collapse acm-notimplemented">
      <td>ListProjects</td>
       <td style="text-align:right">-</td>
    </tr>
    <tr class="collapse acm-notimplemented">
      <td>ListStudioLifecycleConfigs</td>
       <td style="text-align:right">-</td>
    </tr>
    <tr class="collapse acm-notimplemented">
      <td>ListSubscribedWorkteams</td>
       <td style="text-align:right">-</td>
    </tr>
    <tr class="collapse acm-notimplemented">
      <td>ListTrainingJobsForHyperParameterTuningJob</td>
       <td style="text-align:right">-</td>
    </tr>
    <tr class="collapse acm-notimplemented">
      <td>ListTransformJobs</td>
       <td style="text-align:right">-</td>
    </tr>
    <tr class="collapse acm-notimplemented">
      <td>ListUserProfiles</td>
       <td style="text-align:right">-</td>
    </tr>
    <tr class="collapse acm-notimplemented">
      <td>ListWorkforces</td>
       <td style="text-align:right">-</td>
    </tr>
    <tr class="collapse acm-notimplemented">
      <td>ListWorkteams</td>
       <td style="text-align:right">-</td>
    </tr>
    <tr class="collapse acm-notimplemented">
      <td>PutModelPackageGroupPolicy</td>
       <td style="text-align:right">-</td>
    </tr>
    <tr class="collapse acm-notimplemented">
      <td>QueryLineage</td>
       <td style="text-align:right">-</td>
    </tr>
    <tr class="collapse acm-notimplemented">
      <td>RegisterDevices</td>
       <td style="text-align:right">-</td>
    </tr>
    <tr class="collapse acm-notimplemented">
      <td>RenderUiTemplate</td>
       <td style="text-align:right">-</td>
    </tr>
    <tr class="collapse acm-notimplemented">
      <td>RetryPipelineExecution</td>
       <td style="text-align:right">-</td>
    </tr>
    <tr class="collapse acm-notimplemented">
      <td>SendPipelineExecutionStepFailure</td>
       <td style="text-align:right">-</td>
    </tr>
    <tr class="collapse acm-notimplemented">
      <td>SendPipelineExecutionStepSuccess</td>
       <td style="text-align:right">-</td>
    </tr>
    <tr class="collapse acm-notimplemented">
      <td>StartMonitoringSchedule</td>
       <td style="text-align:right">-</td>
    </tr>
    <tr class="collapse acm-notimplemented">
      <td>StartPipelineExecution</td>
       <td style="text-align:right">-</td>
    </tr>
    <tr class="collapse acm-notimplemented">
      <td>StopAutoMLJob</td>
       <td style="text-align:right">-</td>
    </tr>
    <tr class="collapse acm-notimplemented">
      <td>StopCompilationJob</td>
       <td style="text-align:right">-</td>
    </tr>
    <tr class="collapse acm-notimplemented">
      <td>StopEdgePackagingJob</td>
       <td style="text-align:right">-</td>
    </tr>
    <tr class="collapse acm-notimplemented">
      <td>StopHyperParameterTuningJob</td>
       <td style="text-align:right">-</td>
    </tr>
    <tr class="collapse acm-notimplemented">
      <td>StopInferenceRecommendationsJob</td>
       <td style="text-align:right">-</td>
    </tr>
    <tr class="collapse acm-notimplemented">
      <td>StopLabelingJob</td>
       <td style="text-align:right">-</td>
    </tr>
    <tr class="collapse acm-notimplemented">
      <td>StopMonitoringSchedule</td>
       <td style="text-align:right">-</td>
    </tr>
    <tr class="collapse acm-notimplemented">
      <td>StopPipelineExecution</td>
       <td style="text-align:right">-</td>
    </tr>
    <tr class="collapse acm-notimplemented">
      <td>StopProcessingJob</td>
       <td style="text-align:right">-</td>
    </tr>
    <tr class="collapse acm-notimplemented">
      <td>StopTrainingJob</td>
       <td style="text-align:right">-</td>
    </tr>
    <tr class="collapse acm-notimplemented">
      <td>StopTransformJob</td>
       <td style="text-align:right">-</td>
    </tr>
    <tr class="collapse acm-notimplemented">
      <td>UpdateAction</td>
       <td style="text-align:right">-</td>
    </tr>
    <tr class="collapse acm-notimplemented">
      <td>UpdateAppImageConfig</td>
       <td style="text-align:right">-</td>
    </tr>
    <tr class="collapse acm-notimplemented">
      <td>UpdateArtifact</td>
       <td style="text-align:right">-</td>
    </tr>
    <tr class="collapse acm-notimplemented">
      <td>UpdateCodeRepository</td>
       <td style="text-align:right">-</td>
    </tr>
    <tr class="collapse acm-notimplemented">
      <td>UpdateContext</td>
       <td style="text-align:right">-</td>
    </tr>
    <tr class="collapse acm-notimplemented">
      <td>UpdateDeviceFleet</td>
       <td style="text-align:right">-</td>
    </tr>
    <tr class="collapse acm-notimplemented">
      <td>UpdateDevices</td>
       <td style="text-align:right">-</td>
    </tr>
    <tr class="collapse acm-notimplemented">
      <td>UpdateDomain</td>
       <td style="text-align:right">-</td>
    </tr>
    <tr class="collapse acm-notimplemented">
      <td>UpdateEndpoint</td>
       <td style="text-align:right">-</td>
    </tr>
    <tr class="collapse acm-notimplemented">
      <td>UpdateExperiment</td>
       <td style="text-align:right">-</td>
    </tr>
    <tr class="collapse acm-notimplemented">
      <td>UpdateFeatureGroup</td>
       <td style="text-align:right">-</td>
    </tr>
    <tr class="collapse acm-notimplemented">
      <td>UpdateFeatureMetadata</td>
       <td style="text-align:right">-</td>
    </tr>
    <tr class="collapse acm-notimplemented">
      <td>UpdateImage</td>
       <td style="text-align:right">-</td>
    </tr>
    <tr class="collapse acm-notimplemented">
      <td>UpdateModelPackage</td>
       <td style="text-align:right">-</td>
    </tr>
    <tr class="collapse acm-notimplemented">
      <td>UpdateMonitoringSchedule</td>
       <td style="text-align:right">-</td>
    </tr>
    <tr class="collapse acm-notimplemented">
      <td>UpdateNotebookInstance</td>
       <td style="text-align:right">-</td>
    </tr>
    <tr class="collapse acm-notimplemented">
      <td>UpdateNotebookInstanceLifecycleConfig</td>
       <td style="text-align:right">-</td>
    </tr>
    <tr class="collapse acm-notimplemented">
      <td>UpdatePipeline</td>
       <td style="text-align:right">-</td>
    </tr>
    <tr class="collapse acm-notimplemented">
      <td>UpdatePipelineExecution</td>
       <td style="text-align:right">-</td>
    </tr>
    <tr class="collapse acm-notimplemented">
      <td>UpdateProject</td>
       <td style="text-align:right">-</td>
    </tr>
    <tr class="collapse acm-notimplemented">
      <td>UpdateTrainingJob</td>
       <td style="text-align:right">-</td>
    </tr>
    <tr class="collapse acm-notimplemented">
      <td>UpdateTrial</td>
       <td style="text-align:right">-</td>
    </tr>
    <tr class="collapse acm-notimplemented">
      <td>UpdateTrialComponent</td>
       <td style="text-align:right">-</td>
    </tr>
    <tr class="collapse acm-notimplemented">
      <td>UpdateUserProfile</td>
       <td style="text-align:right">-</td>
    </tr>
    <tr class="collapse acm-notimplemented">
      <td>UpdateWorkforce</td>
       <td style="text-align:right">-</td>
    </tr>
    <tr class="collapse acm-notimplemented">
      <td>UpdateWorkteam</td>
       <td style="text-align:right">-</td>
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
    <tr>
      <td><a data-toggle="collapse" href=".acm-notimplemented">Show more</a></td>
      <td style="text-align:right"></td>
    </tr>
    <tr class="collapse acm-notimplemented">
      <td>CancelRotateSecret</td>
       <td style="text-align:right">-</td>
    </tr>
    <tr class="collapse acm-notimplemented">
      <td>RemoveRegionsFromReplication</td>
       <td style="text-align:right">-</td>
    </tr>
    <tr class="collapse acm-notimplemented">
      <td>ReplicateSecretToRegions</td>
       <td style="text-align:right">-</td>
    </tr>
    <tr class="collapse acm-notimplemented">
      <td>StopReplicationToReplica</td>
       <td style="text-align:right">-</td>
    </tr>
    <tr class="collapse acm-notimplemented">
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
      <td>CreateApplication <a href="#misc" title="covered by our integration test suite">✨</a></td>
       <td style="text-align:right">✅</td>
    </tr>
    <tr>
      <td>CreateApplicationVersion <a href="#misc" title="covered by our integration test suite">✨</a></td>
       <td style="text-align:right">✅</td>
    </tr>
    <tr>
      <td>CreateCloudFormationChangeSet <a href="#misc" title="covered by our integration test suite">✨</a></td>
       <td style="text-align:right">✅</td>
    </tr>
    <tr>
      <td>CreateCloudFormationTemplate <a href="#misc" title="covered by our integration test suite">✨</a></td>
       <td style="text-align:right">✅</td>
    </tr>
    <tr>
      <td>DeleteApplication <a href="#misc" title="covered by our integration test suite">✨</a></td>
       <td style="text-align:right">✅</td>
    </tr>
    <tr>
      <td>GetCloudFormationTemplate <a href="#misc" title="covered by our integration test suite">✨</a></td>
       <td style="text-align:right">✅</td>
    </tr>
    <tr>
      <td>ListApplicationVersions <a href="#misc" title="covered by our integration test suite">✨</a></td>
       <td style="text-align:right">✅</td>
    </tr>
    <tr>
      <td>ListApplications <a href="#misc" title="covered by our integration test suite">✨</a></td>
       <td style="text-align:right">✅</td>
    </tr>
    <tr>
      <td><a data-toggle="collapse" href=".acm-notimplemented">Show more</a></td>
      <td style="text-align:right"></td>
    </tr>
    <tr class="collapse acm-notimplemented">
      <td>GetApplication</td>
       <td style="text-align:right">-</td>
    </tr>
    <tr class="collapse acm-notimplemented">
      <td>GetApplicationPolicy</td>
       <td style="text-align:right">-</td>
    </tr>
    <tr class="collapse acm-notimplemented">
      <td>ListApplicationDependencies</td>
       <td style="text-align:right">-</td>
    </tr>
    <tr class="collapse acm-notimplemented">
      <td>PutApplicationPolicy</td>
       <td style="text-align:right">-</td>
    </tr>
    <tr class="collapse acm-notimplemented">
      <td>UnshareApplication</td>
       <td style="text-align:right">-</td>
    </tr>
    <tr class="collapse acm-notimplemented">
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
      <td>CreateHttpNamespace <a href="#misc" title="covered by our integration test suite">✨</a></td>
       <td style="text-align:right">✅</td>
    </tr>
    <tr>
      <td>CreatePrivateDnsNamespace <a href="#misc" title="covered by our integration test suite">✨</a></td>
       <td style="text-align:right">✅</td>
    </tr>
    <tr>
      <td>CreatePublicDnsNamespace <a href="#misc" title="covered by our integration test suite">✨</a></td>
       <td style="text-align:right">✅</td>
    </tr>
    <tr>
      <td>CreateService <a href="#misc" title="covered by our integration test suite">✨</a></td>
       <td style="text-align:right">✅</td>
    </tr>
    <tr>
      <td>DeleteNamespace <a href="#misc" title="covered by our integration test suite">✨</a></td>
       <td style="text-align:right">✅</td>
    </tr>
    <tr>
      <td>DeleteService <a href="#misc" title="covered by our integration test suite">✨</a></td>
       <td style="text-align:right">✅</td>
    </tr>
    <tr>
      <td>DeregisterInstance <a href="#misc" title="covered by our integration test suite">✨</a></td>
       <td style="text-align:right">✅</td>
    </tr>
    <tr>
      <td>GetInstance <a href="#misc" title="covered by our integration test suite">✨</a></td>
       <td style="text-align:right">✅</td>
    </tr>
    <tr>
      <td>GetNamespace <a href="#misc" title="covered by our integration test suite">✨</a></td>
       <td style="text-align:right">✅</td>
    </tr>
    <tr>
      <td>GetOperation <a href="#misc" title="covered by our integration test suite">✨</a></td>
       <td style="text-align:right">✅</td>
    </tr>
    <tr>
      <td>GetService <a href="#misc" title="covered by our integration test suite">✨</a></td>
       <td style="text-align:right">✅</td>
    </tr>
    <tr>
      <td>ListInstances <a href="#misc" title="covered by our integration test suite">✨</a></td>
       <td style="text-align:right">✅</td>
    </tr>
    <tr>
      <td>ListNamespaces <a href="#misc" title="covered by our integration test suite">✨</a></td>
       <td style="text-align:right">✅</td>
    </tr>
    <tr>
      <td>ListServices <a href="#misc" title="covered by our integration test suite">✨</a></td>
       <td style="text-align:right">✅</td>
    </tr>
    <tr>
      <td>ListTagsForResource <a href="#misc" title="covered by our integration test suite">✨</a></td>
       <td style="text-align:right">✅</td>
    </tr>
    <tr>
      <td>RegisterInstance <a href="#misc" title="covered by our integration test suite">✨</a></td>
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
      <td>UpdateService <a href="#misc" title="covered by our integration test suite">✨</a></td>
       <td style="text-align:right">✅</td>
    </tr>
    <tr>
      <td><a data-toggle="collapse" href=".acm-notimplemented">Show more</a></td>
      <td style="text-align:right"></td>
    </tr>
    <tr class="collapse acm-notimplemented">
      <td>DiscoverInstances</td>
       <td style="text-align:right">-</td>
    </tr>
    <tr class="collapse acm-notimplemented">
      <td>GetInstancesHealthStatus</td>
       <td style="text-align:right">-</td>
    </tr>
    <tr class="collapse acm-notimplemented">
      <td>ListOperations</td>
       <td style="text-align:right">-</td>
    </tr>
    <tr class="collapse acm-notimplemented">
      <td>UpdateHttpNamespace</td>
       <td style="text-align:right">-</td>
    </tr>
    <tr class="collapse acm-notimplemented">
      <td>UpdateInstanceCustomHealthStatus</td>
       <td style="text-align:right">-</td>
    </tr>
    <tr class="collapse acm-notimplemented">
      <td>UpdatePrivateDnsNamespace</td>
       <td style="text-align:right">-</td>
    </tr>
    <tr class="collapse acm-notimplemented">
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
      <td>DeleteReceiptRule <a href="#misc" title="covered by our integration test suite">✨</a></td>
       <td style="text-align:right">✅</td>
    </tr>
    <tr>
      <td>DeleteReceiptRuleSet <a href="#misc" title="covered by our integration test suite">✨</a></td>
       <td style="text-align:right">✅</td>
    </tr>
    <tr>
      <td>DeleteTemplate <a href="#misc" title="covered by our integration test suite">✨</a></td>
       <td style="text-align:right">✅</td>
    </tr>
    <tr>
      <td>DescribeActiveReceiptRuleSet <a href="#misc" title="covered by our integration test suite">✨</a></td>
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
      <td>ListReceiptRuleSets <a href="#misc" title="covered by our integration test suite">✨</a></td>
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
      <td>SetActiveReceiptRuleSet <a href="#misc" title="covered by our integration test suite">✨</a></td>
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
    <tr>
      <td><a data-toggle="collapse" href=".acm-notimplemented">Show more</a></td>
      <td style="text-align:right"></td>
    </tr>
    <tr class="collapse acm-notimplemented">
      <td>CloneReceiptRuleSet</td>
       <td style="text-align:right">-</td>
    </tr>
    <tr class="collapse acm-notimplemented">
      <td>CreateConfigurationSetTrackingOptions</td>
       <td style="text-align:right">-</td>
    </tr>
    <tr class="collapse acm-notimplemented">
      <td>CreateCustomVerificationEmailTemplate</td>
       <td style="text-align:right">-</td>
    </tr>
    <tr class="collapse acm-notimplemented">
      <td>CreateReceiptFilter</td>
       <td style="text-align:right">-</td>
    </tr>
    <tr class="collapse acm-notimplemented">
      <td>DeleteConfigurationSet</td>
       <td style="text-align:right">-</td>
    </tr>
    <tr class="collapse acm-notimplemented">
      <td>DeleteConfigurationSetEventDestination</td>
       <td style="text-align:right">-</td>
    </tr>
    <tr class="collapse acm-notimplemented">
      <td>DeleteConfigurationSetTrackingOptions</td>
       <td style="text-align:right">-</td>
    </tr>
    <tr class="collapse acm-notimplemented">
      <td>DeleteCustomVerificationEmailTemplate</td>
       <td style="text-align:right">-</td>
    </tr>
    <tr class="collapse acm-notimplemented">
      <td>DeleteIdentityPolicy</td>
       <td style="text-align:right">-</td>
    </tr>
    <tr class="collapse acm-notimplemented">
      <td>DeleteReceiptFilter</td>
       <td style="text-align:right">-</td>
    </tr>
    <tr class="collapse acm-notimplemented">
      <td>DeleteVerifiedEmailAddress</td>
       <td style="text-align:right">-</td>
    </tr>
    <tr class="collapse acm-notimplemented">
      <td>DescribeConfigurationSet</td>
       <td style="text-align:right">-</td>
    </tr>
    <tr class="collapse acm-notimplemented">
      <td>GetAccountSendingEnabled</td>
       <td style="text-align:right">-</td>
    </tr>
    <tr class="collapse acm-notimplemented">
      <td>GetCustomVerificationEmailTemplate</td>
       <td style="text-align:right">-</td>
    </tr>
    <tr class="collapse acm-notimplemented">
      <td>GetIdentityDkimAttributes</td>
       <td style="text-align:right">-</td>
    </tr>
    <tr class="collapse acm-notimplemented">
      <td>GetIdentityPolicies</td>
       <td style="text-align:right">-</td>
    </tr>
    <tr class="collapse acm-notimplemented">
      <td>ListConfigurationSets</td>
       <td style="text-align:right">-</td>
    </tr>
    <tr class="collapse acm-notimplemented">
      <td>ListCustomVerificationEmailTemplates</td>
       <td style="text-align:right">-</td>
    </tr>
    <tr class="collapse acm-notimplemented">
      <td>ListIdentityPolicies</td>
       <td style="text-align:right">-</td>
    </tr>
    <tr class="collapse acm-notimplemented">
      <td>ListReceiptFilters</td>
       <td style="text-align:right">-</td>
    </tr>
    <tr class="collapse acm-notimplemented">
      <td>PutConfigurationSetDeliveryOptions</td>
       <td style="text-align:right">-</td>
    </tr>
    <tr class="collapse acm-notimplemented">
      <td>PutIdentityPolicy</td>
       <td style="text-align:right">-</td>
    </tr>
    <tr class="collapse acm-notimplemented">
      <td>ReorderReceiptRuleSet</td>
       <td style="text-align:right">-</td>
    </tr>
    <tr class="collapse acm-notimplemented">
      <td>SendBounce</td>
       <td style="text-align:right">-</td>
    </tr>
    <tr class="collapse acm-notimplemented">
      <td>SendCustomVerificationEmail</td>
       <td style="text-align:right">-</td>
    </tr>
    <tr class="collapse acm-notimplemented">
      <td>SetIdentityDkimEnabled</td>
       <td style="text-align:right">-</td>
    </tr>
    <tr class="collapse acm-notimplemented">
      <td>SetIdentityHeadersInNotificationsEnabled</td>
       <td style="text-align:right">-</td>
    </tr>
    <tr class="collapse acm-notimplemented">
      <td>SetReceiptRulePosition</td>
       <td style="text-align:right">-</td>
    </tr>
    <tr class="collapse acm-notimplemented">
      <td>UpdateAccountSendingEnabled</td>
       <td style="text-align:right">-</td>
    </tr>
    <tr class="collapse acm-notimplemented">
      <td>UpdateConfigurationSetEventDestination</td>
       <td style="text-align:right">-</td>
    </tr>
    <tr class="collapse acm-notimplemented">
      <td>UpdateConfigurationSetReputationMetricsEnabled</td>
       <td style="text-align:right">-</td>
    </tr>
    <tr class="collapse acm-notimplemented">
      <td>UpdateConfigurationSetSendingEnabled</td>
       <td style="text-align:right">-</td>
    </tr>
    <tr class="collapse acm-notimplemented">
      <td>UpdateConfigurationSetTrackingOptions</td>
       <td style="text-align:right">-</td>
    </tr>
    <tr class="collapse acm-notimplemented">
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
      <td>CreateEmailIdentity <a href="#misc" title="covered by our integration test suite">✨</a></td>
       <td style="text-align:right">✅</td>
    </tr>
    <tr>
      <td>CreateEmailTemplate <a href="#misc" title="covered by our integration test suite">✨</a></td>
       <td style="text-align:right">✅</td>
    </tr>
    <tr>
      <td>DeleteEmailIdentity <a href="#misc" title="covered by our integration test suite">✨</a></td>
       <td style="text-align:right">✅</td>
    </tr>
    <tr>
      <td>DeleteEmailTemplate</td>
       <td style="text-align:right">✅</td>
    </tr>
    <tr>
      <td>GetDomainStatisticsReport</td>
       <td style="text-align:right">✅</td>
    </tr>
    <tr>
      <td>GetEmailIdentity <a href="#misc" title="covered by our integration test suite">✨</a></td>
       <td style="text-align:right">✅</td>
    </tr>
    <tr>
      <td>ListDomainDeliverabilityCampaigns</td>
       <td style="text-align:right">✅</td>
    </tr>
    <tr>
      <td>ListEmailIdentities <a href="#misc" title="covered by our integration test suite">✨</a></td>
       <td style="text-align:right">✅</td>
    </tr>
    <tr>
      <td>ListEmailTemplates</td>
       <td style="text-align:right">✅</td>
    </tr>
    <tr>
      <td>ListSuppressedDestinations</td>
       <td style="text-align:right">✅</td>
    </tr>
    <tr>
      <td>PutEmailIdentityDkimSigningAttributes</td>
       <td style="text-align:right">✅</td>
    </tr>
    <tr>
      <td>SendBulkEmail <a href="#misc" title="covered by our integration test suite">✨</a></td>
       <td style="text-align:right">✅</td>
    </tr>
    <tr>
      <td>SendEmail <a href="#misc" title="covered by our integration test suite">✨</a></td>
       <td style="text-align:right">✅</td>
    </tr>
    <tr>
      <td><a data-toggle="collapse" href=".acm-notimplemented">Show more</a></td>
      <td style="text-align:right"></td>
    </tr>
    <tr class="collapse acm-notimplemented">
      <td>CreateConfigurationSet</td>
       <td style="text-align:right">-</td>
    </tr>
    <tr class="collapse acm-notimplemented">
      <td>CreateConfigurationSetEventDestination</td>
       <td style="text-align:right">-</td>
    </tr>
    <tr class="collapse acm-notimplemented">
      <td>CreateContact</td>
       <td style="text-align:right">-</td>
    </tr>
    <tr class="collapse acm-notimplemented">
      <td>CreateContactList</td>
       <td style="text-align:right">-</td>
    </tr>
    <tr class="collapse acm-notimplemented">
      <td>CreateCustomVerificationEmailTemplate</td>
       <td style="text-align:right">-</td>
    </tr>
    <tr class="collapse acm-notimplemented">
      <td>CreateDedicatedIpPool</td>
       <td style="text-align:right">-</td>
    </tr>
    <tr class="collapse acm-notimplemented">
      <td>CreateDeliverabilityTestReport</td>
       <td style="text-align:right">-</td>
    </tr>
    <tr class="collapse acm-notimplemented">
      <td>CreateEmailIdentityPolicy</td>
       <td style="text-align:right">-</td>
    </tr>
    <tr class="collapse acm-notimplemented">
      <td>CreateImportJob</td>
       <td style="text-align:right">-</td>
    </tr>
    <tr class="collapse acm-notimplemented">
      <td>DeleteConfigurationSet</td>
       <td style="text-align:right">-</td>
    </tr>
    <tr class="collapse acm-notimplemented">
      <td>DeleteConfigurationSetEventDestination</td>
       <td style="text-align:right">-</td>
    </tr>
    <tr class="collapse acm-notimplemented">
      <td>DeleteContact</td>
       <td style="text-align:right">-</td>
    </tr>
    <tr class="collapse acm-notimplemented">
      <td>DeleteContactList</td>
       <td style="text-align:right">-</td>
    </tr>
    <tr class="collapse acm-notimplemented">
      <td>DeleteCustomVerificationEmailTemplate</td>
       <td style="text-align:right">-</td>
    </tr>
    <tr class="collapse acm-notimplemented">
      <td>DeleteDedicatedIpPool</td>
       <td style="text-align:right">-</td>
    </tr>
    <tr class="collapse acm-notimplemented">
      <td>DeleteEmailIdentityPolicy</td>
       <td style="text-align:right">-</td>
    </tr>
    <tr class="collapse acm-notimplemented">
      <td>DeleteSuppressedDestination</td>
       <td style="text-align:right">-</td>
    </tr>
    <tr class="collapse acm-notimplemented">
      <td>GetAccount</td>
       <td style="text-align:right">-</td>
    </tr>
    <tr class="collapse acm-notimplemented">
      <td>GetBlacklistReports</td>
       <td style="text-align:right">-</td>
    </tr>
    <tr class="collapse acm-notimplemented">
      <td>GetConfigurationSet</td>
       <td style="text-align:right">-</td>
    </tr>
    <tr class="collapse acm-notimplemented">
      <td>GetConfigurationSetEventDestinations</td>
       <td style="text-align:right">-</td>
    </tr>
    <tr class="collapse acm-notimplemented">
      <td>GetContact</td>
       <td style="text-align:right">-</td>
    </tr>
    <tr class="collapse acm-notimplemented">
      <td>GetContactList</td>
       <td style="text-align:right">-</td>
    </tr>
    <tr class="collapse acm-notimplemented">
      <td>GetCustomVerificationEmailTemplate</td>
       <td style="text-align:right">-</td>
    </tr>
    <tr class="collapse acm-notimplemented">
      <td>GetDedicatedIp</td>
       <td style="text-align:right">-</td>
    </tr>
    <tr class="collapse acm-notimplemented">
      <td>GetDedicatedIps</td>
       <td style="text-align:right">-</td>
    </tr>
    <tr class="collapse acm-notimplemented">
      <td>GetDeliverabilityDashboardOptions</td>
       <td style="text-align:right">-</td>
    </tr>
    <tr class="collapse acm-notimplemented">
      <td>GetDeliverabilityTestReport</td>
       <td style="text-align:right">-</td>
    </tr>
    <tr class="collapse acm-notimplemented">
      <td>GetDomainDeliverabilityCampaign</td>
       <td style="text-align:right">-</td>
    </tr>
    <tr class="collapse acm-notimplemented">
      <td>GetEmailIdentityPolicies</td>
       <td style="text-align:right">-</td>
    </tr>
    <tr class="collapse acm-notimplemented">
      <td>GetEmailTemplate</td>
       <td style="text-align:right">-</td>
    </tr>
    <tr class="collapse acm-notimplemented">
      <td>GetImportJob</td>
       <td style="text-align:right">-</td>
    </tr>
    <tr class="collapse acm-notimplemented">
      <td>GetSuppressedDestination</td>
       <td style="text-align:right">-</td>
    </tr>
    <tr class="collapse acm-notimplemented">
      <td>ListConfigurationSets</td>
       <td style="text-align:right">-</td>
    </tr>
    <tr class="collapse acm-notimplemented">
      <td>ListContactLists</td>
       <td style="text-align:right">-</td>
    </tr>
    <tr class="collapse acm-notimplemented">
      <td>ListContacts</td>
       <td style="text-align:right">-</td>
    </tr>
    <tr class="collapse acm-notimplemented">
      <td>ListCustomVerificationEmailTemplates</td>
       <td style="text-align:right">-</td>
    </tr>
    <tr class="collapse acm-notimplemented">
      <td>ListDedicatedIpPools</td>
       <td style="text-align:right">-</td>
    </tr>
    <tr class="collapse acm-notimplemented">
      <td>ListDeliverabilityTestReports</td>
       <td style="text-align:right">-</td>
    </tr>
    <tr class="collapse acm-notimplemented">
      <td>ListImportJobs</td>
       <td style="text-align:right">-</td>
    </tr>
    <tr class="collapse acm-notimplemented">
      <td>ListTagsForResource</td>
       <td style="text-align:right">-</td>
    </tr>
    <tr class="collapse acm-notimplemented">
      <td>PutAccountDedicatedIpWarmupAttributes</td>
       <td style="text-align:right">-</td>
    </tr>
    <tr class="collapse acm-notimplemented">
      <td>PutAccountDetails</td>
       <td style="text-align:right">-</td>
    </tr>
    <tr class="collapse acm-notimplemented">
      <td>PutAccountSendingAttributes</td>
       <td style="text-align:right">-</td>
    </tr>
    <tr class="collapse acm-notimplemented">
      <td>PutAccountSuppressionAttributes</td>
       <td style="text-align:right">-</td>
    </tr>
    <tr class="collapse acm-notimplemented">
      <td>PutConfigurationSetDeliveryOptions</td>
       <td style="text-align:right">-</td>
    </tr>
    <tr class="collapse acm-notimplemented">
      <td>PutConfigurationSetReputationOptions</td>
       <td style="text-align:right">-</td>
    </tr>
    <tr class="collapse acm-notimplemented">
      <td>PutConfigurationSetSendingOptions</td>
       <td style="text-align:right">-</td>
    </tr>
    <tr class="collapse acm-notimplemented">
      <td>PutConfigurationSetSuppressionOptions</td>
       <td style="text-align:right">-</td>
    </tr>
    <tr class="collapse acm-notimplemented">
      <td>PutConfigurationSetTrackingOptions</td>
       <td style="text-align:right">-</td>
    </tr>
    <tr class="collapse acm-notimplemented">
      <td>PutDedicatedIpInPool</td>
       <td style="text-align:right">-</td>
    </tr>
    <tr class="collapse acm-notimplemented">
      <td>PutDedicatedIpWarmupAttributes</td>
       <td style="text-align:right">-</td>
    </tr>
    <tr class="collapse acm-notimplemented">
      <td>PutDeliverabilityDashboardOption</td>
       <td style="text-align:right">-</td>
    </tr>
    <tr class="collapse acm-notimplemented">
      <td>PutEmailIdentityConfigurationSetAttributes</td>
       <td style="text-align:right">-</td>
    </tr>
    <tr class="collapse acm-notimplemented">
      <td>PutEmailIdentityDkimAttributes</td>
       <td style="text-align:right">-</td>
    </tr>
    <tr class="collapse acm-notimplemented">
      <td>PutEmailIdentityFeedbackAttributes</td>
       <td style="text-align:right">-</td>
    </tr>
    <tr class="collapse acm-notimplemented">
      <td>PutEmailIdentityMailFromAttributes</td>
       <td style="text-align:right">-</td>
    </tr>
    <tr class="collapse acm-notimplemented">
      <td>PutSuppressedDestination</td>
       <td style="text-align:right">-</td>
    </tr>
    <tr class="collapse acm-notimplemented">
      <td>SendCustomVerificationEmail</td>
       <td style="text-align:right">-</td>
    </tr>
    <tr class="collapse acm-notimplemented">
      <td>TagResource</td>
       <td style="text-align:right">-</td>
    </tr>
    <tr class="collapse acm-notimplemented">
      <td>TestRenderEmailTemplate</td>
       <td style="text-align:right">-</td>
    </tr>
    <tr class="collapse acm-notimplemented">
      <td>UntagResource</td>
       <td style="text-align:right">-</td>
    </tr>
    <tr class="collapse acm-notimplemented">
      <td>UpdateConfigurationSetEventDestination</td>
       <td style="text-align:right">-</td>
    </tr>
    <tr class="collapse acm-notimplemented">
      <td>UpdateContact</td>
       <td style="text-align:right">-</td>
    </tr>
    <tr class="collapse acm-notimplemented">
      <td>UpdateContactList</td>
       <td style="text-align:right">-</td>
    </tr>
    <tr class="collapse acm-notimplemented">
      <td>UpdateCustomVerificationEmailTemplate</td>
       <td style="text-align:right">-</td>
    </tr>
    <tr class="collapse acm-notimplemented">
      <td>UpdateEmailIdentityPolicy</td>
       <td style="text-align:right">-</td>
    </tr>
    <tr class="collapse acm-notimplemented">
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
      <td>ListEndpointsByPlatformApplication</td>
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
    <tr>
      <td><a data-toggle="collapse" href=".acm-notimplemented">Show more</a></td>
      <td style="text-align:right"></td>
    </tr>
    <tr class="collapse acm-notimplemented">
      <td>CreateSMSSandboxPhoneNumber</td>
       <td style="text-align:right">-</td>
    </tr>
    <tr class="collapse acm-notimplemented">
      <td>DeleteSMSSandboxPhoneNumber</td>
       <td style="text-align:right">-</td>
    </tr>
    <tr class="collapse acm-notimplemented">
      <td>GetSMSSandboxAccountStatus</td>
       <td style="text-align:right">-</td>
    </tr>
    <tr class="collapse acm-notimplemented">
      <td>ListOriginationNumbers</td>
       <td style="text-align:right">-</td>
    </tr>
    <tr class="collapse acm-notimplemented">
      <td>ListSMSSandboxPhoneNumbers</td>
       <td style="text-align:right">-</td>
    </tr>
    <tr class="collapse acm-notimplemented">
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
      <td>CancelCommand <a href="#misc" title="covered by our integration test suite">✨</a></td>
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
      <td>DescribeInstanceInformation <a href="#misc" title="covered by our integration test suite">✨</a></td>
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
      <td>ListCommandInvocations</td>
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
    <tr>
      <td><a data-toggle="collapse" href=".acm-notimplemented">Show more</a></td>
      <td style="text-align:right"></td>
    </tr>
    <tr class="collapse acm-notimplemented">
      <td>AssociateOpsItemRelatedItem</td>
       <td style="text-align:right">-</td>
    </tr>
    <tr class="collapse acm-notimplemented">
      <td>CancelMaintenanceWindowExecution</td>
       <td style="text-align:right">-</td>
    </tr>
    <tr class="collapse acm-notimplemented">
      <td>CreateActivation</td>
       <td style="text-align:right">-</td>
    </tr>
    <tr class="collapse acm-notimplemented">
      <td>CreateAssociation</td>
       <td style="text-align:right">-</td>
    </tr>
    <tr class="collapse acm-notimplemented">
      <td>CreateAssociationBatch</td>
       <td style="text-align:right">-</td>
    </tr>
    <tr class="collapse acm-notimplemented">
      <td>CreateOpsItem</td>
       <td style="text-align:right">-</td>
    </tr>
    <tr class="collapse acm-notimplemented">
      <td>CreateOpsMetadata</td>
       <td style="text-align:right">-</td>
    </tr>
    <tr class="collapse acm-notimplemented">
      <td>CreatePatchBaseline</td>
       <td style="text-align:right">-</td>
    </tr>
    <tr class="collapse acm-notimplemented">
      <td>CreateResourceDataSync</td>
       <td style="text-align:right">-</td>
    </tr>
    <tr class="collapse acm-notimplemented">
      <td>DeleteActivation</td>
       <td style="text-align:right">-</td>
    </tr>
    <tr class="collapse acm-notimplemented">
      <td>DeleteAssociation</td>
       <td style="text-align:right">-</td>
    </tr>
    <tr class="collapse acm-notimplemented">
      <td>DeleteInventory</td>
       <td style="text-align:right">-</td>
    </tr>
    <tr class="collapse acm-notimplemented">
      <td>DeleteOpsMetadata</td>
       <td style="text-align:right">-</td>
    </tr>
    <tr class="collapse acm-notimplemented">
      <td>DeletePatchBaseline</td>
       <td style="text-align:right">-</td>
    </tr>
    <tr class="collapse acm-notimplemented">
      <td>DeleteResourceDataSync</td>
       <td style="text-align:right">-</td>
    </tr>
    <tr class="collapse acm-notimplemented">
      <td>DeregisterManagedInstance</td>
       <td style="text-align:right">-</td>
    </tr>
    <tr class="collapse acm-notimplemented">
      <td>DeregisterPatchBaselineForPatchGroup</td>
       <td style="text-align:right">-</td>
    </tr>
    <tr class="collapse acm-notimplemented">
      <td>DeregisterTargetFromMaintenanceWindow</td>
       <td style="text-align:right">-</td>
    </tr>
    <tr class="collapse acm-notimplemented">
      <td>DeregisterTaskFromMaintenanceWindow</td>
       <td style="text-align:right">-</td>
    </tr>
    <tr class="collapse acm-notimplemented">
      <td>DescribeActivations</td>
       <td style="text-align:right">-</td>
    </tr>
    <tr class="collapse acm-notimplemented">
      <td>DescribeAssociation</td>
       <td style="text-align:right">-</td>
    </tr>
    <tr class="collapse acm-notimplemented">
      <td>DescribeAssociationExecutionTargets</td>
       <td style="text-align:right">-</td>
    </tr>
    <tr class="collapse acm-notimplemented">
      <td>DescribeAssociationExecutions</td>
       <td style="text-align:right">-</td>
    </tr>
    <tr class="collapse acm-notimplemented">
      <td>DescribeAutomationExecutions</td>
       <td style="text-align:right">-</td>
    </tr>
    <tr class="collapse acm-notimplemented">
      <td>DescribeAutomationStepExecutions</td>
       <td style="text-align:right">-</td>
    </tr>
    <tr class="collapse acm-notimplemented">
      <td>DescribeAvailablePatches</td>
       <td style="text-align:right">-</td>
    </tr>
    <tr class="collapse acm-notimplemented">
      <td>DescribeEffectiveInstanceAssociations</td>
       <td style="text-align:right">-</td>
    </tr>
    <tr class="collapse acm-notimplemented">
      <td>DescribeEffectivePatchesForPatchBaseline</td>
       <td style="text-align:right">-</td>
    </tr>
    <tr class="collapse acm-notimplemented">
      <td>DescribeInstanceAssociationsStatus</td>
       <td style="text-align:right">-</td>
    </tr>
    <tr class="collapse acm-notimplemented">
      <td>DescribeInstancePatchStates</td>
       <td style="text-align:right">-</td>
    </tr>
    <tr class="collapse acm-notimplemented">
      <td>DescribeInstancePatchStatesForPatchGroup</td>
       <td style="text-align:right">-</td>
    </tr>
    <tr class="collapse acm-notimplemented">
      <td>DescribeInstancePatches</td>
       <td style="text-align:right">-</td>
    </tr>
    <tr class="collapse acm-notimplemented">
      <td>DescribeInventoryDeletions</td>
       <td style="text-align:right">-</td>
    </tr>
    <tr class="collapse acm-notimplemented">
      <td>DescribeMaintenanceWindowExecutionTaskInvocations</td>
       <td style="text-align:right">-</td>
    </tr>
    <tr class="collapse acm-notimplemented">
      <td>DescribeMaintenanceWindowExecutionTasks</td>
       <td style="text-align:right">-</td>
    </tr>
    <tr class="collapse acm-notimplemented">
      <td>DescribeMaintenanceWindowExecutions</td>
       <td style="text-align:right">-</td>
    </tr>
    <tr class="collapse acm-notimplemented">
      <td>DescribeMaintenanceWindowSchedule</td>
       <td style="text-align:right">-</td>
    </tr>
    <tr class="collapse acm-notimplemented">
      <td>DescribeMaintenanceWindowTargets</td>
       <td style="text-align:right">-</td>
    </tr>
    <tr class="collapse acm-notimplemented">
      <td>DescribeMaintenanceWindowTasks</td>
       <td style="text-align:right">-</td>
    </tr>
    <tr class="collapse acm-notimplemented">
      <td>DescribeMaintenanceWindowsForTarget</td>
       <td style="text-align:right">-</td>
    </tr>
    <tr class="collapse acm-notimplemented">
      <td>DescribeOpsItems</td>
       <td style="text-align:right">-</td>
    </tr>
    <tr class="collapse acm-notimplemented">
      <td>DescribePatchBaselines</td>
       <td style="text-align:right">-</td>
    </tr>
    <tr class="collapse acm-notimplemented">
      <td>DescribePatchGroupState</td>
       <td style="text-align:right">-</td>
    </tr>
    <tr class="collapse acm-notimplemented">
      <td>DescribePatchGroups</td>
       <td style="text-align:right">-</td>
    </tr>
    <tr class="collapse acm-notimplemented">
      <td>DescribePatchProperties</td>
       <td style="text-align:right">-</td>
    </tr>
    <tr class="collapse acm-notimplemented">
      <td>DescribeSessions</td>
       <td style="text-align:right">-</td>
    </tr>
    <tr class="collapse acm-notimplemented">
      <td>DisassociateOpsItemRelatedItem</td>
       <td style="text-align:right">-</td>
    </tr>
    <tr class="collapse acm-notimplemented">
      <td>GetAutomationExecution</td>
       <td style="text-align:right">-</td>
    </tr>
    <tr class="collapse acm-notimplemented">
      <td>GetCalendarState</td>
       <td style="text-align:right">-</td>
    </tr>
    <tr class="collapse acm-notimplemented">
      <td>GetConnectionStatus</td>
       <td style="text-align:right">-</td>
    </tr>
    <tr class="collapse acm-notimplemented">
      <td>GetDefaultPatchBaseline</td>
       <td style="text-align:right">-</td>
    </tr>
    <tr class="collapse acm-notimplemented">
      <td>GetDeployablePatchSnapshotForInstance</td>
       <td style="text-align:right">-</td>
    </tr>
    <tr class="collapse acm-notimplemented">
      <td>GetInventory</td>
       <td style="text-align:right">-</td>
    </tr>
    <tr class="collapse acm-notimplemented">
      <td>GetInventorySchema</td>
       <td style="text-align:right">-</td>
    </tr>
    <tr class="collapse acm-notimplemented">
      <td>GetMaintenanceWindowExecution</td>
       <td style="text-align:right">-</td>
    </tr>
    <tr class="collapse acm-notimplemented">
      <td>GetMaintenanceWindowExecutionTask</td>
       <td style="text-align:right">-</td>
    </tr>
    <tr class="collapse acm-notimplemented">
      <td>GetMaintenanceWindowExecutionTaskInvocation</td>
       <td style="text-align:right">-</td>
    </tr>
    <tr class="collapse acm-notimplemented">
      <td>GetMaintenanceWindowTask</td>
       <td style="text-align:right">-</td>
    </tr>
    <tr class="collapse acm-notimplemented">
      <td>GetOpsItem</td>
       <td style="text-align:right">-</td>
    </tr>
    <tr class="collapse acm-notimplemented">
      <td>GetOpsMetadata</td>
       <td style="text-align:right">-</td>
    </tr>
    <tr class="collapse acm-notimplemented">
      <td>GetOpsSummary</td>
       <td style="text-align:right">-</td>
    </tr>
    <tr class="collapse acm-notimplemented">
      <td>GetPatchBaseline</td>
       <td style="text-align:right">-</td>
    </tr>
    <tr class="collapse acm-notimplemented">
      <td>GetPatchBaselineForPatchGroup</td>
       <td style="text-align:right">-</td>
    </tr>
    <tr class="collapse acm-notimplemented">
      <td>GetServiceSetting</td>
       <td style="text-align:right">-</td>
    </tr>
    <tr class="collapse acm-notimplemented">
      <td>ListAssociationVersions</td>
       <td style="text-align:right">-</td>
    </tr>
    <tr class="collapse acm-notimplemented">
      <td>ListAssociations</td>
       <td style="text-align:right">-</td>
    </tr>
    <tr class="collapse acm-notimplemented">
      <td>ListComplianceItems</td>
       <td style="text-align:right">-</td>
    </tr>
    <tr class="collapse acm-notimplemented">
      <td>ListComplianceSummaries</td>
       <td style="text-align:right">-</td>
    </tr>
    <tr class="collapse acm-notimplemented">
      <td>ListDocumentMetadataHistory</td>
       <td style="text-align:right">-</td>
    </tr>
    <tr class="collapse acm-notimplemented">
      <td>ListDocumentVersions</td>
       <td style="text-align:right">-</td>
    </tr>
    <tr class="collapse acm-notimplemented">
      <td>ListInventoryEntries</td>
       <td style="text-align:right">-</td>
    </tr>
    <tr class="collapse acm-notimplemented">
      <td>ListOpsItemEvents</td>
       <td style="text-align:right">-</td>
    </tr>
    <tr class="collapse acm-notimplemented">
      <td>ListOpsItemRelatedItems</td>
       <td style="text-align:right">-</td>
    </tr>
    <tr class="collapse acm-notimplemented">
      <td>ListOpsMetadata</td>
       <td style="text-align:right">-</td>
    </tr>
    <tr class="collapse acm-notimplemented">
      <td>ListResourceComplianceSummaries</td>
       <td style="text-align:right">-</td>
    </tr>
    <tr class="collapse acm-notimplemented">
      <td>ListResourceDataSync</td>
       <td style="text-align:right">-</td>
    </tr>
    <tr class="collapse acm-notimplemented">
      <td>PutComplianceItems</td>
       <td style="text-align:right">-</td>
    </tr>
    <tr class="collapse acm-notimplemented">
      <td>PutInventory</td>
       <td style="text-align:right">-</td>
    </tr>
    <tr class="collapse acm-notimplemented">
      <td>RegisterDefaultPatchBaseline</td>
       <td style="text-align:right">-</td>
    </tr>
    <tr class="collapse acm-notimplemented">
      <td>RegisterPatchBaselineForPatchGroup</td>
       <td style="text-align:right">-</td>
    </tr>
    <tr class="collapse acm-notimplemented">
      <td>RegisterTargetWithMaintenanceWindow</td>
       <td style="text-align:right">-</td>
    </tr>
    <tr class="collapse acm-notimplemented">
      <td>RegisterTaskWithMaintenanceWindow</td>
       <td style="text-align:right">-</td>
    </tr>
    <tr class="collapse acm-notimplemented">
      <td>ResetServiceSetting</td>
       <td style="text-align:right">-</td>
    </tr>
    <tr class="collapse acm-notimplemented">
      <td>ResumeSession</td>
       <td style="text-align:right">-</td>
    </tr>
    <tr class="collapse acm-notimplemented">
      <td>SendAutomationSignal</td>
       <td style="text-align:right">-</td>
    </tr>
    <tr class="collapse acm-notimplemented">
      <td>StartAssociationsOnce</td>
       <td style="text-align:right">-</td>
    </tr>
    <tr class="collapse acm-notimplemented">
      <td>StartAutomationExecution</td>
       <td style="text-align:right">-</td>
    </tr>
    <tr class="collapse acm-notimplemented">
      <td>StartChangeRequestExecution</td>
       <td style="text-align:right">-</td>
    </tr>
    <tr class="collapse acm-notimplemented">
      <td>StartSession</td>
       <td style="text-align:right">-</td>
    </tr>
    <tr class="collapse acm-notimplemented">
      <td>StopAutomationExecution</td>
       <td style="text-align:right">-</td>
    </tr>
    <tr class="collapse acm-notimplemented">
      <td>TerminateSession</td>
       <td style="text-align:right">-</td>
    </tr>
    <tr class="collapse acm-notimplemented">
      <td>UnlabelParameterVersion</td>
       <td style="text-align:right">-</td>
    </tr>
    <tr class="collapse acm-notimplemented">
      <td>UpdateAssociation</td>
       <td style="text-align:right">-</td>
    </tr>
    <tr class="collapse acm-notimplemented">
      <td>UpdateAssociationStatus</td>
       <td style="text-align:right">-</td>
    </tr>
    <tr class="collapse acm-notimplemented">
      <td>UpdateDocumentMetadata</td>
       <td style="text-align:right">-</td>
    </tr>
    <tr class="collapse acm-notimplemented">
      <td>UpdateMaintenanceWindow</td>
       <td style="text-align:right">-</td>
    </tr>
    <tr class="collapse acm-notimplemented">
      <td>UpdateMaintenanceWindowTarget</td>
       <td style="text-align:right">-</td>
    </tr>
    <tr class="collapse acm-notimplemented">
      <td>UpdateMaintenanceWindowTask</td>
       <td style="text-align:right">-</td>
    </tr>
    <tr class="collapse acm-notimplemented">
      <td>UpdateManagedInstanceRole</td>
       <td style="text-align:right">-</td>
    </tr>
    <tr class="collapse acm-notimplemented">
      <td>UpdateOpsItem</td>
       <td style="text-align:right">-</td>
    </tr>
    <tr class="collapse acm-notimplemented">
      <td>UpdateOpsMetadata</td>
       <td style="text-align:right">-</td>
    </tr>
    <tr class="collapse acm-notimplemented">
      <td>UpdatePatchBaseline</td>
       <td style="text-align:right">-</td>
    </tr>
    <tr class="collapse acm-notimplemented">
      <td>UpdateResourceDataSync</td>
       <td style="text-align:right">-</td>
    </tr>
    <tr class="collapse acm-notimplemented">
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
      <td>ListActivities <a href="#misc" title="covered by our integration test suite">✨</a></td>
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
    <tr>
      <td><a data-toggle="collapse" href=".acm-notimplemented">Show more</a></td>
      <td style="text-align:right"></td>
    </tr>
    <tr class="collapse acm-notimplemented">
      <td>StartSyncExecution</td>
       <td style="text-align:right">-</td>
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
    <tr>
      <td><a data-toggle="collapse" href=".acm-notimplemented">Show more</a></td>
      <td style="text-align:right"></td>
    </tr>
    <tr class="collapse acm-notimplemented">
      <td>DecodeAuthorizationMessage</td>
       <td style="text-align:right">-</td>
    </tr>
    <tr class="collapse acm-notimplemented">
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
    <tr>
      <td><a data-toggle="collapse" href=".acm-notimplemented">Show more</a></td>
      <td style="text-align:right"></td>
    </tr>
    <tr class="collapse acm-notimplemented">
      <td>AddAttachmentsToSet</td>
       <td style="text-align:right">-</td>
    </tr>
    <tr class="collapse acm-notimplemented">
      <td>AddCommunicationToCase</td>
       <td style="text-align:right">-</td>
    </tr>
    <tr class="collapse acm-notimplemented">
      <td>DescribeAttachment</td>
       <td style="text-align:right">-</td>
    </tr>
    <tr class="collapse acm-notimplemented">
      <td>DescribeCommunications</td>
       <td style="text-align:right">-</td>
    </tr>
    <tr class="collapse acm-notimplemented">
      <td>DescribeServices</td>
       <td style="text-align:right">-</td>
    </tr>
    <tr class="collapse acm-notimplemented">
      <td>DescribeSeverityLevels</td>
       <td style="text-align:right">-</td>
    </tr>
    <tr class="collapse acm-notimplemented">
      <td>DescribeTrustedAdvisorCheckRefreshStatuses</td>
       <td style="text-align:right">-</td>
    </tr>
    <tr class="collapse acm-notimplemented">
      <td>DescribeTrustedAdvisorCheckResult</td>
       <td style="text-align:right">-</td>
    </tr>
    <tr class="collapse acm-notimplemented">
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
    <tr>
      <td><a data-toggle="collapse" href=".acm-notimplemented">Show more</a></td>
      <td style="text-align:right"></td>
    </tr>
    <tr class="collapse acm-notimplemented">
      <td>CountClosedWorkflowExecutions</td>
       <td style="text-align:right">-</td>
    </tr>
    <tr class="collapse acm-notimplemented">
      <td>CountOpenWorkflowExecutions</td>
       <td style="text-align:right">-</td>
    </tr>
    <tr class="collapse acm-notimplemented">
      <td>ListTagsForResource</td>
       <td style="text-align:right">-</td>
    </tr>
    <tr class="collapse acm-notimplemented">
      <td>RequestCancelWorkflowExecution</td>
       <td style="text-align:right">-</td>
    </tr>
    <tr class="collapse acm-notimplemented">
      <td>RespondActivityTaskCanceled</td>
       <td style="text-align:right">-</td>
    </tr>
    <tr class="collapse acm-notimplemented">
      <td>TagResource</td>
       <td style="text-align:right">-</td>
    </tr>
    <tr class="collapse acm-notimplemented">
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
      <td>Query <a href="#misc" title="covered by our integration test suite">✨</a></td>
       <td style="text-align:right">✅</td>
    </tr>
    <tr>
      <td><a data-toggle="collapse" href=".acm-notimplemented">Show more</a></td>
      <td style="text-align:right"></td>
    </tr>
    <tr class="collapse acm-notimplemented">
      <td>CancelQuery</td>
       <td style="text-align:right">-</td>
    </tr>
    <tr class="collapse acm-notimplemented">
      <td>CreateScheduledQuery</td>
       <td style="text-align:right">-</td>
    </tr>
    <tr class="collapse acm-notimplemented">
      <td>DeleteScheduledQuery</td>
       <td style="text-align:right">-</td>
    </tr>
    <tr class="collapse acm-notimplemented">
      <td>DescribeEndpoints</td>
       <td style="text-align:right">-</td>
    </tr>
    <tr class="collapse acm-notimplemented">
      <td>DescribeScheduledQuery</td>
       <td style="text-align:right">-</td>
    </tr>
    <tr class="collapse acm-notimplemented">
      <td>ExecuteScheduledQuery</td>
       <td style="text-align:right">-</td>
    </tr>
    <tr class="collapse acm-notimplemented">
      <td>ListScheduledQueries</td>
       <td style="text-align:right">-</td>
    </tr>
    <tr class="collapse acm-notimplemented">
      <td>ListTagsForResource</td>
       <td style="text-align:right">-</td>
    </tr>
    <tr class="collapse acm-notimplemented">
      <td>PrepareQuery</td>
       <td style="text-align:right">-</td>
    </tr>
    <tr class="collapse acm-notimplemented">
      <td>TagResource</td>
       <td style="text-align:right">-</td>
    </tr>
    <tr class="collapse acm-notimplemented">
      <td>UntagResource</td>
       <td style="text-align:right">-</td>
    </tr>
    <tr class="collapse acm-notimplemented">
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
      <td>CreateDatabase <a href="#misc" title="covered by our integration test suite">✨</a></td>
       <td style="text-align:right">✅</td>
    </tr>
    <tr>
      <td>CreateTable <a href="#misc" title="covered by our integration test suite">✨</a></td>
       <td style="text-align:right">✅</td>
    </tr>
    <tr>
      <td>DeleteDatabase <a href="#misc" title="covered by our integration test suite">✨</a></td>
       <td style="text-align:right">✅</td>
    </tr>
    <tr>
      <td>DeleteTable <a href="#misc" title="covered by our integration test suite">✨</a></td>
       <td style="text-align:right">✅</td>
    </tr>
    <tr>
      <td>DescribeDatabase <a href="#misc" title="covered by our integration test suite">✨</a></td>
       <td style="text-align:right">✅</td>
    </tr>
    <tr>
      <td>DescribeTable <a href="#misc" title="covered by our integration test suite">✨</a></td>
       <td style="text-align:right">✅</td>
    </tr>
    <tr>
      <td>ListDatabases <a href="#misc" title="covered by our integration test suite">✨</a></td>
       <td style="text-align:right">✅</td>
    </tr>
    <tr>
      <td>ListTables <a href="#misc" title="covered by our integration test suite">✨</a></td>
       <td style="text-align:right">✅</td>
    </tr>
    <tr>
      <td>WriteRecords <a href="#misc" title="covered by our integration test suite">✨</a></td>
       <td style="text-align:right">✅</td>
    </tr>
    <tr>
      <td><a data-toggle="collapse" href=".acm-notimplemented">Show more</a></td>
      <td style="text-align:right"></td>
    </tr>
    <tr class="collapse acm-notimplemented">
      <td>DescribeEndpoints</td>
       <td style="text-align:right">-</td>
    </tr>
    <tr class="collapse acm-notimplemented">
      <td>ListTagsForResource</td>
       <td style="text-align:right">-</td>
    </tr>
    <tr class="collapse acm-notimplemented">
      <td>TagResource</td>
       <td style="text-align:right">-</td>
    </tr>
    <tr class="collapse acm-notimplemented">
      <td>UntagResource</td>
       <td style="text-align:right">-</td>
    </tr>
    <tr class="collapse acm-notimplemented">
      <td>UpdateDatabase</td>
       <td style="text-align:right">-</td>
    </tr>
    <tr class="collapse acm-notimplemented">
      <td>UpdateTable</td>
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
      <td>CreateServer <a href="#misc" title="covered by our integration test suite">✨</a></td>
       <td style="text-align:right">✅</td>
    </tr>
    <tr>
      <td>CreateUser <a href="#misc" title="covered by our integration test suite">✨</a></td>
       <td style="text-align:right">✅</td>
    </tr>
    <tr>
      <td>DeleteServer <a href="#misc" title="covered by our integration test suite">✨</a></td>
       <td style="text-align:right">✅</td>
    </tr>
    <tr>
      <td>DeleteSshPublicKey <a href="#misc" title="covered by our integration test suite">✨</a></td>
       <td style="text-align:right">✅</td>
    </tr>
    <tr>
      <td>DeleteUser <a href="#misc" title="covered by our integration test suite">✨</a></td>
       <td style="text-align:right">✅</td>
    </tr>
    <tr>
      <td>DescribeServer <a href="#misc" title="covered by our integration test suite">✨</a></td>
       <td style="text-align:right">✅</td>
    </tr>
    <tr>
      <td>DescribeUser <a href="#misc" title="covered by our integration test suite">✨</a></td>
       <td style="text-align:right">✅</td>
    </tr>
    <tr>
      <td>ImportSshPublicKey <a href="#misc" title="covered by our integration test suite">✨</a></td>
       <td style="text-align:right">✅</td>
    </tr>
    <tr>
      <td>ListServers</td>
       <td style="text-align:right">✅</td>
    </tr>
    <tr>
      <td>ListUsers <a href="#misc" title="covered by our integration test suite">✨</a></td>
       <td style="text-align:right">✅</td>
    </tr>
    <tr>
      <td>UpdateUser <a href="#misc" title="covered by our integration test suite">✨</a></td>
       <td style="text-align:right">✅</td>
    </tr>
    <tr>
      <td><a data-toggle="collapse" href=".acm-notimplemented">Show more</a></td>
      <td style="text-align:right"></td>
    </tr>
    <tr class="collapse acm-notimplemented">
      <td>CreateAccess</td>
       <td style="text-align:right">-</td>
    </tr>
    <tr class="collapse acm-notimplemented">
      <td>CreateWorkflow</td>
       <td style="text-align:right">-</td>
    </tr>
    <tr class="collapse acm-notimplemented">
      <td>DeleteAccess</td>
       <td style="text-align:right">-</td>
    </tr>
    <tr class="collapse acm-notimplemented">
      <td>DeleteWorkflow</td>
       <td style="text-align:right">-</td>
    </tr>
    <tr class="collapse acm-notimplemented">
      <td>DescribeAccess</td>
       <td style="text-align:right">-</td>
    </tr>
    <tr class="collapse acm-notimplemented">
      <td>DescribeExecution</td>
       <td style="text-align:right">-</td>
    </tr>
    <tr class="collapse acm-notimplemented">
      <td>DescribeSecurityPolicy</td>
       <td style="text-align:right">-</td>
    </tr>
    <tr class="collapse acm-notimplemented">
      <td>DescribeWorkflow</td>
       <td style="text-align:right">-</td>
    </tr>
    <tr class="collapse acm-notimplemented">
      <td>ListAccesses</td>
       <td style="text-align:right">-</td>
    </tr>
    <tr class="collapse acm-notimplemented">
      <td>ListExecutions</td>
       <td style="text-align:right">-</td>
    </tr>
    <tr class="collapse acm-notimplemented">
      <td>ListSecurityPolicies</td>
       <td style="text-align:right">-</td>
    </tr>
    <tr class="collapse acm-notimplemented">
      <td>ListTagsForResource</td>
       <td style="text-align:right">-</td>
    </tr>
    <tr class="collapse acm-notimplemented">
      <td>ListWorkflows</td>
       <td style="text-align:right">-</td>
    </tr>
    <tr class="collapse acm-notimplemented">
      <td>SendWorkflowStepState</td>
       <td style="text-align:right">-</td>
    </tr>
    <tr class="collapse acm-notimplemented">
      <td>StartServer</td>
       <td style="text-align:right">-</td>
    </tr>
    <tr class="collapse acm-notimplemented">
      <td>StopServer</td>
       <td style="text-align:right">-</td>
    </tr>
    <tr class="collapse acm-notimplemented">
      <td>TagResource</td>
       <td style="text-align:right">-</td>
    </tr>
    <tr class="collapse acm-notimplemented">
      <td>TestIdentityProvider</td>
       <td style="text-align:right">-</td>
    </tr>
    <tr class="collapse acm-notimplemented">
      <td>UntagResource</td>
       <td style="text-align:right">-</td>
    </tr>
    <tr class="collapse acm-notimplemented">
      <td>UpdateAccess</td>
       <td style="text-align:right">-</td>
    </tr>
    <tr class="collapse acm-notimplemented">
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
      <td>BatchGetTraces</td>
       <td style="text-align:right">✅</td>
    </tr>
    <tr>
      <td>CreateGroup</td>
       <td style="text-align:right">✅</td>
    </tr>
    <tr>
      <td>CreateSamplingRule <a href="#misc" title="covered by our integration test suite">✨</a></td>
       <td style="text-align:right">✅</td>
    </tr>
    <tr>
      <td>DeleteGroup</td>
       <td style="text-align:right">✅</td>
    </tr>
    <tr>
      <td>DeleteSamplingRule <a href="#misc" title="covered by our integration test suite">✨</a></td>
       <td style="text-align:right">✅</td>
    </tr>
    <tr>
      <td>GetEncryptionConfig</td>
       <td style="text-align:right">✅</td>
    </tr>
    <tr>
      <td>GetGroup</td>
       <td style="text-align:right">✅</td>
    </tr>
    <tr>
      <td>GetGroups</td>
       <td style="text-align:right">✅</td>
    </tr>
    <tr>
      <td>GetInsight</td>
       <td style="text-align:right">✅</td>
    </tr>
    <tr>
      <td>GetInsightEvents</td>
       <td style="text-align:right">✅</td>
    </tr>
    <tr>
      <td>GetInsightImpactGraph</td>
       <td style="text-align:right">✅</td>
    </tr>
    <tr>
      <td>GetInsightSummaries</td>
       <td style="text-align:right">✅</td>
    </tr>
    <tr>
      <td>GetSamplingRules <a href="#misc" title="covered by our integration test suite">✨</a></td>
       <td style="text-align:right">✅</td>
    </tr>
    <tr>
      <td>GetSamplingStatisticSummaries</td>
       <td style="text-align:right">✅</td>
    </tr>
    <tr>
      <td>GetSamplingTargets</td>
       <td style="text-align:right">✅</td>
    </tr>
    <tr>
      <td>GetServiceGraph</td>
       <td style="text-align:right">✅</td>
    </tr>
    <tr>
      <td>GetTimeSeriesServiceStatistics</td>
       <td style="text-align:right">✅</td>
    </tr>
    <tr>
      <td>GetTraceGraph</td>
       <td style="text-align:right">✅</td>
    </tr>
    <tr>
      <td>GetTraceSummaries <a href="#misc" title="covered by our integration test suite">✨</a></td>
       <td style="text-align:right">✅</td>
    </tr>
    <tr>
      <td>ListTagsForResource</td>
       <td style="text-align:right">✅</td>
    </tr>
    <tr>
      <td>PutEncryptionConfig</td>
       <td style="text-align:right">✅</td>
    </tr>
    <tr>
      <td>PutTelemetryRecords <a href="#misc" title="covered by our integration test suite">✨</a></td>
       <td style="text-align:right">✅</td>
    </tr>
    <tr>
      <td>PutTraceSegments <a href="#misc" title="covered by our integration test suite">✨</a></td>
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
      <td>UpdateGroup</td>
       <td style="text-align:right">✅</td>
    </tr>
    <tr>
      <td>UpdateSamplingRule <a href="#misc" title="covered by our integration test suite">✨</a></td>
       <td style="text-align:right">✅</td>
    </tr>
 </tbody>
</table>



## Misc ##

Endpoints marked with ✨ are covered by our integration test suite.

</div>