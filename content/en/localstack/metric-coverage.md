---
title: "LocalStack Metric Coverage"
linkTitle: "LocalStack Metric Coverage"
weight: 100
description: >
  Overview of the implemented AWS APIs and integration test coverage in LocalStack
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
<td><a data-toggle="collapse" href=".acm-notimplemented">Show missing</a></td>
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


## Misc ##

Endpoints marked with ✨ are covered by our integration test suite.


</div>