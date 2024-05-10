---
title: "Chaos Engineering: Route53 Failover with FIS"
linkTitle: "Chaos Engineering: Route53 Failover with FIS"
weight: 9
description: >
  Integrate FIS with Route 53 to create a resilient, self-repairing infrastructure, which manages traffic effectively during simulated disruptions.
type: tutorials
teaser: ""
services:
- fis
- agw
- ddb
- lmb
- r53
platform:
- Java
deployment:
- awscli
tags:
- BASH
- FIS
- Route53
- API Gateway
- DynamoDB
- Lambda
pro: true
leadimage: "route-53-failover.png"
---

> TODO

## Introduction

LocalStack allows you to integrate & test [Fault Injection Simulator (FIS)](https://docs.localstack.cloud/user-guide/aws/fis/) with [Route53](https://docs.localstack.cloud/user-guide/aws/route53/) to automatically divert users to 
a healthy secondary zone if the primary region fails, ensuring system availability and responsiveness. Route53's health checks and
traffic redirection enhance architecture resilience and ensure service continuity during regional outages, crucial for uninterrupted
user experiences.

{{< callout "note">}}
Route53 Failover with FIS is currently available as part of the **LocalStack Enterprise** plan. If you'd like to try it out,
please [contact us](https://www.localstack.cloud/demo) to request access.
{{< /callout >}}

## Getting started

This tutorial is designed for users new to the Route53 and FIS services. In this example, there's an active-primary and
passive-standby configuration. Route53 routes traffic to the primary region, which processes product-related requests through
API Gateway and Lambda functions, with data stored in DynamoDB. If the primary region fails, Route53 redirects to the standby
region, maintained in sync by a replication Lambda function.

For this particular example, we'll be using a [sample application repository](https://github.com/localstack-samples/samples-chaos-engineering/tree/main/route53-failover). Clone the repository, and follow the
instructions below to get started.

### Prerequisites

The general prerequisites for this guide are:

- LocalStack Pro with [LocalStack Auth Token]({{<ref "getting-started/auth-token">}})
- [AWS CLI]({{<ref "user-guide/integrations/aws-cli">}}) with the [`awslocal` wrapper]({{<ref "user-guide/integrations/aws-cli#localstack-aws-cli-awslocal">}})
- [Docker](https://docs.docker.com/get-docker/) and [Docker Compose](https://docs.docker.com/compose/install/)
- [Python-3](https://www.python.org/downloads/)
- `dig`

Start LocalStack by using the `docker-compose.yml` file from the repository. Ensure to set your Auth Token as an environment variable
during this process.

{{< command >}}
$ LOCALSTACK_AUTH_TOKEN=<YOUR_LOCALSTACK_AUTH_TOKEN>
$ docker compose up
{{< /command >}}

### Application Architecture

The following diagram shows the architecture that this application builds and deploys:

{{< figure src="route53-failover-1.png" width="800">}}

### Creating the resources

To begin, deploy the same services in both `us-west-1` and `us-east-1` regions. The resources specified in the `init-resources.sh`
file will be created when the LocalStack container starts, using Initialization Hooks and the `awslocal` CLI tool.

The objective is to have a backup system in case of a regional outage in the primary availability zone (`us-west-1`). We'll focus
on this region to examine the existing resilience mechanisms.

{{< figure src="route53-failover-2.png" width="800">}}

-   The primary API Gateway includes a health check endpoint that returns a 200 HTTP status code, serving as a basic check for its availability.
-   Data synchronization across regions can be achieved with AWS-native tools like DynamoDB Streams and AWS Lambda. Here, any changes to the
primary table trigger a Lambda function, replicating these changes to a secondary table. This configuration is essential for high availability
and disaster recovery.

### Configuring a Route53 hosted zone

Let's begin by setting up a hosted zone in Route53 named `hello-localstack.com` and retrieved the hosted zone ID:

{{< command >}}
$ HOSTED_ZONE_NAME=hello-localstack.com
$ HOSTED_ZONE_ID=$(awslocal route53 create-hosted-zone --name $HOSTED_ZONE_NAME --caller-reference foo | jq -r .HostedZone.Id)
{{< /command >}}

Then, define the health check ID for the API Gateway available in the `us-west-1` region:

{{< command >}}
$ HEALTH_CHECK_ID=$(
awslocal route53 create-health-check \
--caller-reference foobar \
--health-check-config '{
    "FullyQualifiedDomainName": "12345.execute-api.localhost.localstack.cloud",
    "Port": 4566,
    "ResourcePath": "/dev/healthcheck",
    "Type": "HTTP",
    "RequestInterval": 10
}' | jq -r .HealthCheck.Id
)
{{< /command >}}

This command creates a Route 53 health check for an HTTP endpoint (`12345.execute-api.localhost.localstack.cloud:4566/dev/healthcheck`) 
with a 10-second request interval and captures the health check's ID. The caller reference identifier in AWS resource creation or updates
prevents accidental duplication if requests are repeated.

To update DNS records in the specified Route53 hosted zone (`$HOSTED_ZONE_ID`), add two CNAME records: `12345.$HOSTED_ZONE_NAME` 
pointing to `12345.execute-api.localhost.localstack.cloud`, and `67890.$HOSTED_ZONE_NAME` pointing to `67890.execute-api.localhost.localstack.cloud`.
Set a TTL (Time to Live) of 60 seconds for these records.

{{< command >}}
$ awslocal route53 change-resource-record-sets \
--hosted-zone $HOSTED_ZONE_ID \
--change-batch '{
    "Changes": [
    {
        "Action": "CREATE",
        "ResourceRecordSet": {
            "Name": "12345.'$HOSTED_ZONE_NAME'",
            "Type": "CNAME",
            "TTL": 60,
            "ResourceRecords": [
                {"Value": "12345.execute-api.localhost.localstack.cloud"}
            ]
        }
    },
    {
        "Action": "CREATE",
        "ResourceRecordSet": {
            "Name": "67890.'$HOSTED_ZONE_NAME'",
            "Type": "CNAME",
            "TTL": 60,
            "ResourceRecords": [
                {"Value": "67890.execute-api.localhost.localstack.cloud"}
            ]
        }
    }
    ]
}'
{{< /command >}}

Finally, we'll update the DNS records in the Route53 hosted zone identified by **`$HOSTED_ZONE_ID`**. We're adding two CNAME records
for the subdomain `test.$HOSTED_ZONE_NAME`. The first record points to `12345.$HOSTED_ZONE_NAME` and is linked with the earlier created
health check, designated as the primary failover target. The second record points to `67890.$HOSTED_ZONE_NAME` and is set as the secondary
failover target.

{{< command >}}
$ awslocal route53 change-resource-record-sets \
--hosted-zone-id $HOSTED_ZONE_ID \
--change-batch '{
    "Changes": [
    {
        "Action": "CREATE",
        "ResourceRecordSet": {
            "Name": "test.'$HOSTED_ZONE_NAME'",
            "Type": "CNAME",
            "SetIdentifier": "12345",
            "AliasTarget": {
                "HostedZoneId": "'$HOSTED_ZONE_ID'",
                "DNSName": "12345.'$HOSTED_ZONE_NAME'",
                "EvaluateTargetHealth": true
            },
            "HealthCheckId": "'$HEALTH_CHECK_ID'",
            "Failover": "PRIMARY"
        }
    },
    {
        "Action": "CREATE",
        "ResourceRecordSet": {
            "Name": "test.'$HOSTED_ZONE_NAME'",
            "Type": "CNAME",
            "SetIdentifier": "67890",
            "AliasTarget": {
                "HostedZoneId": "'$HOSTED_ZONE_ID'",
                "DNSName": "67890.'$HOSTED_ZONE_NAME'",
                "EvaluateTargetHealth": true
            },
            "Failover": "SECONDARY"
        }
    }
]
}'
{{< /command >}}

This setup represents the basic failover configuration where traffic is redirected to different endpoints based on their health check
status. To confirm that the CNAME record for `test.hello-localstack.com` points to `12345.execute-api.localhost.localstack.cloud`, 
you can use the following `dig` command:

{{< command >}}
$ dig @localhost test.hello-localstack.com CNAME
<disable-copy>                                        
.....
;; QUESTION SECTION:
;test.hello-localstack.com.	IN	CNAME

;; ANSWER SECTION:
test.hello-localstack.com. 300	IN	CNAME	12345.execute-api.localhost.localstack.cloud.
.....
</disable-copy>
{{< /command >}}

### Creating a controlled outage

Our setup is now complete and ready for testing. To mimic a regional outage in the `us-west-1` region, we'll conduct an experiment that
halts all service invocations in this region, including the health check function. Once the primary region becomes non-functional,
Route 53's health checks will fail. This failure will activate the failover policy, redirecting traffic to the corresponding services
in the secondary region, thus maintaining service continuity.

{{< command >}}
$ cat region-outage-experiment.json
<disable-copy>
{
    "description": "template for internal server error for few regions i.e. us-west-1",
    "actions": {
        "regionUnavailable-us-west-1": {
            "actionId": "localstack:generic:api-error",
            "parameters": {
                "region": "us-west-1",
                "errorCode": "503"
            }
        }
    },
    "stopConditions": [],
    "roleArn": "arn:aws:iam:000000000000:role/ExperimentRole"
}
</disable-copy>               
{{< /command >}}

This Fault Injection Simulator (FIS) experiment template is set up to mimic a `Service Unavailable` (503 error) in the `us-west-1` region.
To create the experiment template, use the following command:

{{< command >}}
$ awslocal fis create-experiment-template --cli-input-json file://region-outage-experiment.json
{{< /command >}}

Once the template is created, start the experiment using its ID:

{{< command >}}
$ awslocal fis start-experiment --experiment-template-id <EXPERIMENT_TEMPLATE_ID>
<disable-copy>
{
    "experiment": {
    "id": "651b5196-b244-4a8b-8ab6-d7b9e13998a0",
    "experimentTemplateId": "d3a1a31b-c52e-49ec-8387-8f5eb75a11df",
    "roleArn": "arn:aws:iam:000000000000:role/ExperimentRole",
    "state": {
        "status": "running"
    },
    "actions": {
        "regionUnavailable-us-east-1": {
        "actionId": "localstack:generic:api-error",
        "parameters": {
            "region": "us-west-1",
            "errorCode": "503"
            }
        }
    },
    "stopConditions": [],
    "creationTime": 1699902569.439826,
    "startTime": 1699902569.439826
    }
}
</disable-copy>
{{< /command >}}

Replace `<EXPERIMENT_TEMPLATE_ID>` with the ID of the experiment template created in the previous step. When the experiment is active,
Route 53's health checks will detect the failure and redirect traffic to the standby region as per the failover setup. Confirm this redirection with:

{{< command >}}
$ dig @localhost test.hello-localstack.com CNAME
<disable-copy>                                        
.....
;; QUESTION SECTION:
;test.hello-localstack.com.	IN	CNAME

;; ANSWER SECTION:
test.hello-localstack.com. 300	IN	CNAME	67890.execute-api.localhost.localstack.cloud.
.....
</disable-copy>
{{< /command >}}

This indicates that the hosted zone name now points to the secondary API Gateway, and `us-east-1` services are in use.

A Python script can simulate backend handling of this switch:

```python
import dns.resolver
import requests

# Set the Route53 DNS resolver to use
dns_resolver_ip = '127.0.0.1'

# Domain to resolve
domain_to_resolve = 'test.hello-localstack.com'

# Resolve the CNAME record using the specified DNS server
resolver = dns.resolver.Resolver(configure=False)
resolver.nameservers = [dns_resolver_ip]

try:
    cname_record = resolver.query(domain_to_resolve, rdtype=dns.rdatatype.CNAME)
    resolved_domain = str(cname_record[0].target)

    # Construct the full URL with the resolved domain
    resolved_url = f'http://{resolved_domain}:4566/dev/productApi?id=prod-1088'

    # Make an HTTP request to the resolved URL
    response = requests.get(resolved_url)

    # Print the response
    print(response.text)

except dns.resolver.NXDOMAIN:
    print(f"CNAME record not found for {domain_to_resolve}")

except Exception as e:
    print(f"Error: {e}")
```

Running the script will resolve the CNAME record for 'test.hello-localstack.com', make an HTTP request to the resolved URL, and print the response, which fetches a Product object from DynamoDB in the `us-east-1` region.

{{< command >}}
$ python3 dns-resolver.py
<disable-copy>
s{"price":"29.99","name":"Super Widget","description":"A versatile widget that can be used for a variety of purposes.
Durable, reliable, and affordable.","id":"prod-1088"}
</disable-copy>
{{< /command >}}

The LocalStack logs will confirm which API Gateway was called based on the resolved domain.

```bash
2023-11-07T11:59:28.292 DEBUG --- [   asgi_gw_9] l.s.l.i.version_manager    : > {resource: /productApi,path: /productApi,httpMethod: GET,headers: {Host=67890.execute-api.localhost.localstack.cloud:4566,
User-Agent=python-requests/2.31.0, accept-encoding=gzip, deflate, accept=*/*, Connection=keep-alive, x-localstack-tgt-api=apigateway .... 
```
