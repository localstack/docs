---
title: "Route 53"
linkTitle: "Route 53"
date: 2021-09-28
weight: 5
categories: ["LocalStack Pro"]
description: >
  Route 53
---

The Route53 API in LocalStack Pro allows you to create hosted zones and to manage DNS entries (e.g., A records) which can then be queried via the built-in DNS server.

The example below illustrates the creation of a hosted zone `example.com`, registration of an A record named `test.example.com` that points to `1.2.3.4`, and finally querying the DNS record by using the `dig` command against the DNS server running on `localhost` (inside the LocalStack container, on port `53`):
```
$ zone_id=$(awslocal route53 create-hosted-zone --name example.com --caller-reference r1 | jq -r '.HostedZone.Id')
$ awslocal route53 change-resource-record-sets --hosted-zone-id $zone_id --change-batch 'Changes=[{Action=CREATE,ResourceRecordSet={Name=test.example.com,Type=A,ResourceRecords=[{Value=1.2.3.4}]}}]'
$ dig @localhost test.example.com
...
;; ANSWER SECTION:
test.example.com.	300	IN	A	1.2.3.4
```

**Note**: Using the built-in DNS capabilities requires privileged access for the LocalStack container (please also refer to the `DNS_ADDRESS` configuration variable).
