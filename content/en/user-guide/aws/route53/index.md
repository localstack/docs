---
title: "Route 53"
linkTitle: Route53
categories: ["LocalStack Pro", "DNS"]
description: >
  Get started with Amazon Route 53 on LocalStack
aliases:
  - /aws/route53/
---

The Route53 API in LocalStack Pro allows you to create hosted zones and to manage DNS entries (e.g., A records) which can then be queried via the built-in DNS server.

The example below illustrates the creation of a hosted zone `example.com`, registration of an A record named `test.example.com` that points to `1.2.3.4`, and finally querying the DNS record by using the `dig` command against the DNS server running on `localhost` (inside the LocalStack container, on port `53`):
{{< command >}}
$ zone_id=$(awslocal route53 create-hosted-zone --name example.com --caller-reference r1 | jq -r '.HostedZone.Id')
$ awslocal route53 change-resource-record-sets --hosted-zone-id $zone_id --change-batch 'Changes=[{Action=CREATE,ResourceRecordSet={Name=test.example.com,Type=A,ResourceRecords=[{Value=1.2.3.4}]}}]'
$ dig @localhost test.example.com
...
;; ANSWER SECTION:
test.example.com.	300	IN	A	1.2.3.4
{{< / command >}}

{{< alert >}}
**Note**: Using the built-in DNS capabilities requires privileged access for the LocalStack container (please also refer to the `DNS_ADDRESS` configuration variable).
{{< /alert >}}

## Customizing internal endpoint resolution

The DNS name `localhost.localstack.cloud` (and any subdomains like `mybucket.s3.localhost.localstack.cloud`) is used internally in LocalStack to route requests, e.g., between a Lambda container and the LocalStack APIs.

Customizing the internal LocalStack DNS name is not a common requirement - it should work out of the box for most use cases. However, in some cases you may want to customize the external resolution of this DNS name, for example if your LocalStack instance is running on a separate Docker network than your application code, or even on a different machine.

Assume we'd like to have all `*.localhost.localstack.cloud` subdomains resolve to the address `5.6.7.8` (i.e., if this is the IP where your LocalStack instance is accessible) when querying the built-in DNS server. We can utilize Route53 to that effect:
{{< command >}}
$ zone_id=$(awslocal route53 create-hosted-zone --name localhost.localstack.cloud --caller-reference r1 | jq -r .HostedZone.Id)
$ awslocal route53 change-resource-record-sets --hosted-zone-id $zone_id --change-batch '{"Changes":[{"Action":"CREATE","ResourceRecordSet":{"Name":"localhost.localstack.cloud","Type":"A","ResourceRecords":[{"Value":"5.6.7.8"}]}},{"Action":"CREATE","ResourceRecordSet":{"Name":"*.localhost.localstack.cloud","Type":"A","ResourceRecords":[{"Value":"5.6.7.8"}]}}]}'
$ dig @127.0.0.1 bucket1.s3.localhost.localstack.cloud
...
;; ANSWER SECTION:
localhost.localstack.cloud. 300	IN	A	5.6.7.8
$ dig @127.0.0.1 localhost.localstack.cloud
...
;; ANSWER SECTION:
localhost.localstack.cloud. 300	IN	A	5.6.7.8
{{< / command >}}
