---
title: "ACM Option #2 (AWS Certificate Manager) Coverage"
linkTitle: "ACM Option #2 Coverage"
weight: 100
description: >
  Overview of ACM (AWS Certificate Manager) coverage in LocalStack
hide_readingtime: true
---


## Available Operations #

11 out of 15 operations available in LocalStack

<div id="service"><div class="card w-75">
            <div class="card-header" id="header_AddTagsToCertificate">
                <button class="btn btn-link btn-block collapsed" data-toggle="collapse" data-target="#AddTagsToCertificate" aria-controls="AddTagsToCertificate">
                <div class="container">
                <div class="row">
                    <div class="col-md text-left">
                     <h5>AddTagsToCertificate</h5>
                    </div>
                    <div class="col">Community
                    </div>
                     <div class="col text-right"><a title="Tested externally">♻</a>
                    </div>
                </div>
                </div>
                </button>
            </div>
            <div id="AddTagsToCertificate" class="collapse" aria-labelledby="header_AddTagsToCertificate" data-parent="#service">
            <div class="card-body">
            <div class="container">
                <div class="row">
                    <div class="col-sm">
                     <b>Parameters tested:</b> <ul>
  <li>CertificateArn</li>
  <li>Tags</li>
</ul>
                    </div>
                    <div class="col-sm">
                    <b>Exceptions tested:</b> <ul>
  <li>ResourceNotFoundException</li>
  <li>ValidationException</li>
  <li>TooManyTagsException</li>
</ul>
                    </div>
                </div>
                </div>
            </div>
            </div>
        </div>
        <div class="card w-75">
            <div class="card-header" id="header_DeleteCertificate">
                <button class="btn btn-link btn-block collapsed" data-toggle="collapse" data-target="#DeleteCertificate" aria-controls="DeleteCertificate">
                <div class="container">
                <div class="row">
                    <div class="col-md text-left">
                     <h5>DeleteCertificate</h5>
                    </div>
                    <div class="col">Community
                    </div>
                     <div class="col text-right"><a title="AWS validated">☁✅</a>
                    </div>
                </div>
                </div>
                </button>
            </div>
            <div id="DeleteCertificate" class="collapse" aria-labelledby="header_DeleteCertificate" data-parent="#service">
            <div class="card-body">
            <div class="container">
                <div class="row">
                    <div class="col-sm">
                     <b>Parameters tested:</b> <ul>
  <li>CertificateArn</li>
</ul>
                    </div>
                    <div class="col-sm">
                    <b>Exceptions tested:</b> <ul>
  <li>ResourceNotFoundException</li>
</ul>
                    </div>
                </div>
                </div>
            </div>
            </div>
        </div>
        <div class="card w-75">
            <div class="card-header" id="header_DescribeCertificate">
                <button class="btn btn-link btn-block collapsed" data-toggle="collapse" data-target="#DescribeCertificate" aria-controls="DescribeCertificate">
                <div class="container">
                <div class="row">
                    <div class="col-md text-left">
                     <h5>DescribeCertificate</h5>
                    </div>
                    <div class="col">Community
                    </div>
                     <div class="col text-right"><a title="AWS validated">☁✅</a>
                    </div>
                </div>
                </div>
                </button>
            </div>
            <div id="DescribeCertificate" class="collapse" aria-labelledby="header_DescribeCertificate" data-parent="#service">
            <div class="card-body">
            <div class="container">
                <div class="row">
                    <div class="col-sm">
                     <b>Parameters tested:</b> <ul>
  <li>CertificateArn</li>
</ul>
                    </div>
                    <div class="col-sm">
                    <b>Exceptions tested:</b> <ul>
  <li>ResourceNotFoundException</li>
</ul>
                    </div>
                </div>
                </div>
            </div>
            </div>
        </div>
        <div class="card w-75">
            <div class="card-header" id="header_ExportCertificate">
                <button class="btn btn-link btn-block collapsed" data-toggle="collapse" data-target="#ExportCertificate" aria-controls="ExportCertificate">
                <div class="container">
                <div class="row">
                    <div class="col-md text-left">
                     <h5>ExportCertificate</h5>
                    </div>
                    <div class="col">Community
                    </div>
                     <div class="col text-right"><a title="Tested externally">♻</a>
                    </div>
                </div>
                </div>
                </button>
            </div>
            <div id="ExportCertificate" class="collapse" aria-labelledby="header_ExportCertificate" data-parent="#service">
            <div class="card-body">
            <div class="container">
                <div class="row">
                    <div class="col-sm">
                     <b>Parameters tested:</b> <ul>
  <li>CertificateArn</li>
  <li>Passphrase</li>
</ul>
                    </div>
                    <div class="col-sm">
                    <b>Exceptions tested:</b> <ul>
  <li>ResourceNotFoundException</li>
</ul>
                    </div>
                </div>
                </div>
            </div>
            </div>
        </div>
        <div class="card w-75">
            <div class="card-header" id="header_GetCertificate">
                <button class="btn btn-link btn-block collapsed" data-toggle="collapse" data-target="#GetCertificate" aria-controls="GetCertificate">
                <div class="container">
                <div class="row">
                    <div class="col-md text-left">
                     <h5>GetCertificate</h5>
                    </div>
                    <div class="col">Community
                    </div>
                     <div class="col text-right"><a title="Tested externally">♻</a>
                    </div>
                </div>
                </div>
                </button>
            </div>
            <div id="GetCertificate" class="collapse" aria-labelledby="header_GetCertificate" data-parent="#service">
            <div class="card-body">
            <div class="container">
                <div class="row">
                    <div class="col-sm">
                     <b>Parameters tested:</b> <ul>
  <li>CertificateArn</li>
</ul>
                    </div>
                    <div class="col-sm">
                    <b>Exceptions tested:</b> <ul>
  <li>ResourceNotFoundException</li>
</ul>
                    </div>
                </div>
                </div>
            </div>
            </div>
        </div>
        <div class="card w-75">
            <div class="card-header" id="header_ImportCertificate">
                <button class="btn btn-link btn-block collapsed" data-toggle="collapse" data-target="#ImportCertificate" aria-controls="ImportCertificate">
                <div class="container">
                <div class="row">
                    <div class="col-md text-left">
                     <h5>ImportCertificate</h5>
                    </div>
                    <div class="col">Community
                    </div>
                     <div class="col text-right"><a title="Tested internally">✅</a>
                    </div>
                </div>
                </div>
                </button>
            </div>
            <div id="ImportCertificate" class="collapse" aria-labelledby="header_ImportCertificate" data-parent="#service">
            <div class="card-body">
            <div class="container">
                <div class="row">
                    <div class="col-sm">
                     <b>Parameters tested:</b> <ul>
  <li>Certificate</li>
  <li>PrivateKey</li>
  <li>CertificateChain</li>
  <li>Tags</li>
</ul>
                    </div>
                    <div class="col-sm">
                    <b>Exceptions tested:</b> <ul>
  <li>ValidationException</li>
</ul>
                    </div>
                </div>
                </div>
            </div>
            </div>
        </div>
        <div class="card w-75">
            <div class="card-header" id="header_ListCertificates">
                <button class="btn btn-link btn-block collapsed" data-toggle="collapse" data-target="#ListCertificates" aria-controls="ListCertificates">
                <div class="container">
                <div class="row">
                    <div class="col-md text-left">
                     <h5>ListCertificates</h5>
                    </div>
                    <div class="col">Community
                    </div>
                     <div class="col text-right"><a title="Tested internally">✅</a>
                    </div>
                </div>
                </div>
                </button>
            </div>
            <div id="ListCertificates" class="collapse" aria-labelledby="header_ListCertificates" data-parent="#service">
            <div class="card-body">
            <div class="container">
                <div class="row">
                    <div class="col-sm">
                     <b>Parameters tested:</b> <ul>
  <li>CertificateStatuses</li>
</ul>
                    </div>
                    <div class="col-sm">
                    <b>Exceptions tested:</b> <ul>
  <li>AccessDeniedException</li>
</ul>
                    </div>
                </div>
                </div>
            </div>
            </div>
        </div>
        <div class="card w-75">
            <div class="card-header" id="header_ListTagsForCertificate">
                <button class="btn btn-link btn-block collapsed" data-toggle="collapse" data-target="#ListTagsForCertificate" aria-controls="ListTagsForCertificate">
                <div class="container">
                <div class="row">
                    <div class="col-md text-left">
                     <h5>ListTagsForCertificate</h5>
                    </div>
                    <div class="col">Community
                    </div>
                     <div class="col text-right"><a title="AWS validated">☁✅</a>
                    </div>
                </div>
                </div>
                </button>
            </div>
            <div id="ListTagsForCertificate" class="collapse" aria-labelledby="header_ListTagsForCertificate" data-parent="#service">
            <div class="card-body">
            <div class="container">
                <div class="row">
                    <div class="col-sm">
                     <b>Parameters tested:</b> <ul>
  <li>CertificateArn</li>
</ul>
                    </div>
                    <div class="col-sm">
                    <b>Exceptions tested:</b> <ul>
  <li>ResourceNotFoundException</li>
</ul>
                    </div>
                </div>
                </div>
            </div>
            </div>
        </div>
        <div class="card w-75">
            <div class="card-header" id="header_RemoveTagsFromCertificate">
                <button class="btn btn-link btn-block collapsed" data-toggle="collapse" data-target="#RemoveTagsFromCertificate" aria-controls="RemoveTagsFromCertificate">
                <div class="container">
                <div class="row">
                    <div class="col-md text-left">
                     <h5>RemoveTagsFromCertificate</h5>
                    </div>
                    <div class="col">Community
                    </div>
                     <div class="col text-right"><a title="Tested externally">♻</a>
                    </div>
                </div>
                </div>
                </button>
            </div>
            <div id="RemoveTagsFromCertificate" class="collapse" aria-labelledby="header_RemoveTagsFromCertificate" data-parent="#service">
            <div class="card-body">
            <div class="container">
                <div class="row">
                    <div class="col-sm">
                     <b>Parameters tested:</b> <ul>
  <li>CertificateArn</li>
  <li>Tags</li>
</ul>
                    </div>
                    <div class="col-sm">
                    <b>Exceptions tested:</b> <ul>
  <li>ResourceNotFoundException</li>
  <li>ValidationException</li>
</ul>
                    </div>
                </div>
                </div>
            </div>
            </div>
        </div>
        <div class="card w-75">
            <div class="card-header" id="header_RequestCertificate">
                <button class="btn btn-link btn-block collapsed" data-toggle="collapse" data-target="#RequestCertificate" aria-controls="RequestCertificate">
                <div class="container">
                <div class="row">
                    <div class="col-md text-left">
                     <h5>RequestCertificate</h5>
                    </div>
                    <div class="col">Community
                    </div>
                     <div class="col text-right"><a title="Tested internally">✅</a>
                    </div>
                </div>
                </div>
                </button>
            </div>
            <div id="RequestCertificate" class="collapse" aria-labelledby="header_RequestCertificate" data-parent="#service">
            <div class="card-body">
            <div class="container">
                <div class="row">
                    <div class="col-sm">
                     <b>Parameters tested:</b> <ul>
  <li>DomainName</li>
  <li>ValidationMethod</li>
  <li>IdempotencyToken</li>
  <li>Tags</li>
  <li>SubjectAlternativeNames</li>
  <li>DomainValidationOptions</li>
</ul>
                    </div>
                    <div class="col-sm">
                    <b>Exceptions tested:</b> <ul>
  <li>ValidationException</li>
</ul>
                    </div>
                </div>
                </div>
            </div>
            </div>
        </div>
        <div class="card w-75">
            <div class="card-header" id="header_ResendValidationEmail">
                <button class="btn btn-link btn-block collapsed" data-toggle="collapse" data-target="#ResendValidationEmail" aria-controls="ResendValidationEmail">
                <div class="container">
                <div class="row">
                    <div class="col-md text-left">
                     <h5>ResendValidationEmail</h5>
                    </div>
                    <div class="col">Community
                    </div>
                     <div class="col text-right"><a title="Tested externally">♻</a>
                    </div>
                </div>
                </div>
                </button>
            </div>
            <div id="ResendValidationEmail" class="collapse" aria-labelledby="header_ResendValidationEmail" data-parent="#service">
            <div class="card-body">
            <div class="container">
                <div class="row">
                    <div class="col-sm">
                     <b>Parameters tested:</b> <ul>
  <li>CertificateArn</li>
  <li>Domain</li>
  <li>ValidationDomain</li>
</ul>
                    </div>
                    <div class="col-sm">
                    <b>Exceptions tested:</b> <ul>
  <li>InvalidDomainValidationOptionsException</li>
  <li>ResourceNotFoundException</li>
</ul>
                    </div>
                </div>
                </div>
            </div>
            </div>
        </div>
<br/>

        



## Not yet implemented operations #

* GetAccountConfiguration
* PutAccountConfiguration
* RenewCertificate
* UpdateCertificateOptions