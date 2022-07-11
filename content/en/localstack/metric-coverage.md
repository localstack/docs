---
title: "LocalStack Metric Coverage"
linkTitle: "LocalStack Metric Coverage"
weight: 100
description: >
  Overview of the implemented AWS APIs and integration test coverage in LocalStack
---

<div class="coverage-report">

## acm ##

| Operation                              | Implemented |
| -------------------------------------- | ----------: |
| AddTagsToCertificate                   | ✅         |
| DeleteCertificate [✨](#misc "covered by our integration test suite")                    | ✅         |
| DescribeCertificate [✨](#misc "covered by our integration test suite")                  | ✅         |
| ExportCertificate                      | ✅         |
| GetCertificate                         | ✅         |
| ImportCertificate [✨](#misc "covered by our integration test suite")                    | ✅         |
| ListCertificates [✨](#misc "covered by our integration test suite")                     | ✅         |
| ListTagsForCertificate [✨](#misc "covered by our integration test suite")               | ✅         |
| RemoveTagsFromCertificate              | ✅         |
| RequestCertificate [✨](#misc "covered by our integration test suite")                   | ✅         |
| ResendValidationEmail                  | ✅         |
| {{< details "Coming soon" >}}
* GetAccountConfiguration
* PutAccountConfiguration
* RenewCertificate
* UpdateCertificateOptions
{{< /details >}} | |


<!-- {{< details "Coming soon" >}}
| Operation                              | Implemented |
| -------------------------------------- | ----------: |
| GetAccountConfiguration                | -         |
| PutAccountConfiguration                | -         |
| RenewCertificate                       | -         |
| UpdateCertificateOptions                       | -         |

{{< /details >}} -->

## Misc ##

Endpoints marked with ✨ are covered by our integration test suite.

</div>