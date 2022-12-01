---
title: "LocalStack Limitations"
weight: 50
description: >
  Known limitations of LocalStack and its services
---

This page describes known limitations of LocalStack and its services, either due to missing implementations or due to third-party integrations.

## Implementation Limitations

Limitations that exist due to missing features in LocalStack.

<!--
TODO:
Move these limitations into the appropriate service page
-->

### Lambda Functions

Only the local executor with locally launched LocalStack can be used together with JVM Lambda Functions.

## Integration Limitations

Limitations that may occur because of third party integrations behavior.

### CDK

#### Stacks with validated certificates

By default, stacks with validated certificates may not be deployed using the `local` lambda executor.
This originates from the way how CDK ensures the certificate is ready - it creates a single-file lambda function with a single dependency on `aws-sdk` which is usually preinstalled and available globally in lambda runtime.
When this lambda is executed locally from the `/tmp` folder, the package can not be discovered by Node due to the way how Node package resolution works.

### DNS Rebind Protection

For certain LocalStack features it is necessary that the DNS resolves to the local network.
For example, LocalStack is using virtual-host based addressing for S3, ElasticSearch, and OpenSearch by default.
S3 buckets can be reached via `<bucket-name>.s3.<region>.localhost.localstack.cloud` and OpenSearch clusters which are created by LocalStack can be reached via `<domain-name>.<region>.opensearch.localhost.localstack.cloud`.
This is handled correctly if you [configured your system's DNS for the transparent execution mode of LocalStack Pro]({{< ref "dns-server#system-dns-configuration" >}}).

However, if you rely on your local network's DNS, your router / DNS server might block those requests due to the DNS Rebind Protection.
This feature is enabled by default in pfSense, OPNSense, OpenWRT, AVM FritzBox, and potentially also other devices.
Some of the vendors might allow upstream responses in the 127.0.0.0/8 range (like OpenWRT).

You can check if your DNS setup works correctly by resolving a subdomain of `localhost.localstack.cloud`:
{{< command "hl_lines=16">}}
$ dig test.localhost.localstack.cloud

; <<>> DiG 9.16.8-Ubuntu <<>> test.localhost.localstack.cloud
;; global options: +cmd
;; Got answer:
;; ->>HEADER<<- opcode: QUERY, status: NOERROR, id: 45150
;; flags: qr rd ra; QUERY: 1, ANSWER: 2, AUTHORITY: 0, ADDITIONAL: 1

;; OPT PSEUDOSECTION:
; EDNS: version: 0, flags:; udp: 65494
;; QUESTION SECTION:
;test.localhost.localstack.cloud. IN	A

;; ANSWER SECTION:
test.localhost.localstack.cloud. 10786 IN CNAME	localhost.localstack.cloud.
localhost.localstack.cloud. 389	IN	A	127.0.0.1

;; Query time: 16 msec
;; SERVER: 127.0.0.53#53(127.0.0.53)
;; WHEN: Fr Jän 14 11:23:12 CET 2022
;; MSG SIZE  rcvd: 90
{{< /command >}}
If the the DNS resolves the subdomain to your localhost (127.0.0.1), your setup is working.
If not, please check the configuration of your router / DNS if the Rebind Protection is active or [enable the LocalStack DNS on your system]({{< ref "dns-server#system-dns-configuration" >}}).
