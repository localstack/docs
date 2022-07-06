---
title: "Metric Coverage"
linkTitle: "Metric Coverge"
weight: 1
description: >
  Overview of the implemented AWS APIs and their level of parity with the AWS cloud
---  

**__Disclaimer__**: naive calculation of test coverage - if operation is called at least once, it is considered as 'covered'.


## acm ##


| Operation             | Implemented | Tested |
|-----------------------|-------------|--------|
| AddTagsToCertificate  | ✅          | ✅     |
| DeleteCertificate     | ✅          | ❌     |
