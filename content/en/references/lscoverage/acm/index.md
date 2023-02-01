---
title: "ACM (AWS Certificate Manager) Coverage"
linkTitle: "ACM Coverage"
weight: 100
description: >
  Overview of ACM (AWS Certificate Manager) coverage in LocalStack
hide_readingtime: true
---


## Available Operations #

11 out of 15 operations available in LocalStack

<table>
  <thead>
    <tr>
      <th>Operation</th>
      <th style="text-align:right">Pro only</th>
      <th style="text-align:right">aws-validated</th>
    </tr>
  </thead>
  <tbody>
  <tr>
      <td><a href="#addtagstocertificate">AddTagsToCertificate</a></td>
      <td style="text-align:right">⭐</td>
      <td style="text-align:right">✅</td>
    </tr>
    <tr>
      <td><a href="#deletecertificate">DeleteCertificate</a></td>
      <td style="text-align:right"></td>
      <td style="text-align:right">✅</td>
    </tr>
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