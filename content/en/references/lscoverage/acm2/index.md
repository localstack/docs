---
title: "ACM 2 (AWS Certificate Manager) Coverage"
linkTitle: "ACM 2 Coverage"
weight: 100
description: >
  Overview of ACM (AWS Certificate Manager) coverage in LocalStack
hide_readingtime: true
---


## Available Operations #

11 out of 15 operations available in LocalStack

<div id="service">
  <div class="card">
    <div class="card-header" id="header_addtagstocertificate">
      <h2 class="mb-0">
        <button class="btn btn-link" data-toggle="collapse" data-target="#addtagstocertificate" aria-expanded="true" aria-controls="addtagstocertificate">
          AddTagsToCertificate <a title="only available in Pro">⭐</a>
        </button>
      </h2>
    </div>
    <div id="addtagstocertificate" class="collapse show" aria-labelledby="header_addtagstocertificate" data-parent="#service">
      <div class="card-body">
       <h5>Pro only</h5>
       <b>Parameters tested:</b>
        <ul> 
        <li> CertificateArn </li>
        </ul>
       <b>Exceptions tested:</b>
        <ul> 
        <li> ResourceNotFoundException </li>
        </ul>
      </div>
    </div>
  </div>
  <div class="card">
    <div class="card-header" id="headingTwo">
      <h5 class="mb-0">
        <button class="btn btn-link collapsed" data-toggle="collapse" data-target="#collapseTwo" aria-expanded="false" aria-controls="collapseTwo">
          Collapsible Group Item #2
        </button>
      </h5>
    </div>
    <div id="collapseTwo" class="collapse" aria-labelledby="headingTwo" data-parent="#service">
      <div class="card-body">
        Anim pariatur cliche reprehenderit, enim eiusmod high life accusamus terry richardson ad squid. 3 wolf moon officia aute, non cupidatat skateboard dolor brunch. Food truck quinoa nesciunt laborum eiusmod. Brunch 3 wolf moon tempor, sunt aliqua put a bird on it squid single-origin coffee nulla assumenda shoreditch et. Nihil anim keffiyeh helvetica, craft beer labore wes anderson cred nesciunt sapiente ea proident. Ad vegan excepteur butcher vice lomo. Leggings occaecat craft beer farm-to-table, raw denim aesthetic synth nesciunt you probably haven't heard of them accusamus labore sustainable VHS.
      </div>
    </div>
  </div>
  <div class="card">
    <div class="card-header" id="headingThree">
      <h5 class="mb-0">
        <button class="btn btn-link collapsed" data-toggle="collapse" data-target="#collapseThree" aria-expanded="false" aria-controls="collapseThree">
          Collapsible Group Item #3
        </button>
      </h5>
    </div>
    <div id="collapseThree" class="collapse" aria-labelledby="headingThree" data-parent="#service">
      <div class="card-body">
        Anim pariatur cliche reprehenderit, enim eiusmod high life accusamus terry richardson ad squid. 3 wolf moon officia aute, non cupidatat skateboard dolor brunch. Food truck quinoa nesciunt laborum eiusmod. Brunch 3 wolf moon tempor, sunt aliqua put a bird on it squid single-origin coffee nulla assumenda shoreditch et. Nihil anim keffiyeh helvetica, craft beer labore wes anderson cred nesciunt sapiente ea proident. Ad vegan excepteur butcher vice lomo. Leggings occaecat craft beer farm-to-table, raw denim aesthetic synth nesciunt you probably haven't heard of them accusamus labore sustainable VHS.
      </div>
    </div>
  </div>
</div>
<table id="service-table">
  <thead>
    <tr>
      <th>Operation</th>
      <th style="text-align:right">Pro only</th>
      <th style="text-align:right">aws-validated</th>
    </tr>
  </thead>
  <tbody>
  <tr>
      <td><a role="button" data-toggle="collapse" data-target="#acm-addtagstocertificate" aria-expanded="false" aria-controls="acm-addtagstocertificate">AddTagsToCertificate</a></td>
      <td style="text-align:right">⭐</td>
      <td style="text-align:right">✅</td>
    </tr>
      <tbody class="collapse" id="acm-addtagstocertificate" aria-labelledby="acm-addtagstocertificate" data-parent="#service-table">
      <tr >
      <td style="text-align:right">-</td>
      <td>CertificateArn</td>
       <td style="text-align:right">-</td>
       </tr>
             <tr >
      <td style="text-align:right">-</td>
      <td>TagList</td>
       <td style="text-align:right">-</td>
       </tr>
       </tbody>
    <tr>
      <td><a role="button" data-toggle="collapse" data-target="#acm-deletecertificate" aria-expanded="false" aria-controls="acm-deletecertificate">DeleteCertificate</a></td>
      <td style="text-align:right"></td>
      <td style="text-align:right">✅</td>
    </tr>
    <tbody class="collapse" id="acm-deletecertificate" aria-labelledby="acm-deletecertificate" data-parent="#service-table">
      <tr >
      <td style="text-align:right">-</td>
      <td>CertificateArn</td>
       <td style="text-align:right">-</td>
       </tr>
             <tr >
      <td style="text-align:right">-</td>
      <td>TagList</td>
       <td style="text-align:right">-</td>
       </tr>
       </tbody>
    <tr>
      <td><a href="#describecertificate">DescribeCertificate</a></td>
      <td style="text-align:right"></td>
      <td style="text-align:right"></td>
    </tr>
    <tr>
      <td><a href="#exportcertificate">ExportCertificate</a></td>
       <td style="text-align:right">⭐</td>
       <td style="text-align:right"></td>
    </tr>
    <tr>
      <td><a href="#getcertificate">GetCertificate</a></td>
       <td style="text-align:right"></td>
       <td style="text-align:right"></td>
    </tr>
    <tr>
      <td><a href="#importcertificate">ImportCertificate</a></td>
       <td style="text-align:right"></td>
       <td style="text-align:right">✅</td>
    </tr>
    <tr>
      <td><a href="#listcertificates">ListCertificates</a></td>
       <td style="text-align:right"></td>
       <td style="text-align:right">✅</td>
    </tr>
    <tr>
      <td><a href="#listtagsforcertificate">ListTagsForCertificate</a></td>
       <td style="text-align:right"></td>
       <td style="text-align:right">✅</td>
    </tr>
    <tr>
      <td><a href="#removetagsfromcertificate">RemoveTagsFromCertificate</a></td>
       <td style="text-align:right"></td>
       <td style="text-align:right">✅</td>
    </tr>
    <tr>
      <td><a href="#requestcertificate">RequestCertificate</a></td>
       <td style="text-align:right"></td>
       <td style="text-align:right">✅</td>
    </tr>
    <tr>
      <td><a href="#resendvalidationemail">ResendValidationEmail</a></td>
       <td style="text-align:right"></td>
       <td style="text-align:right">✅</td>
    </tr>
  </tbody>
 </table>


### AddTagsToCertificate ###

**Tested without parameters only**

**Exceptions tested**
* ResourceNotFoundException

### DeleteCertificate ###

**Parameters tested:**
* CertificateArn

**Exceptions tested:**
* ResourceNotFoundException


### DescribeCertificate ###



## Not yet implemented operations #

* GetAccountConfiguration
* PutAccountConfiguration
* RenewCertificate
* UpdateCertificateOptions