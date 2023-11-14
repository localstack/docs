---
title: "Route53 Failover with FIS"
linkTitle: "Route53 Failover with FIS"
weight: 1
description: Leveraging Route 53 with AWS FIS to architect a robust, self-healing infrastructure that ensures seamless failover and traffic management in response to simulated disruptions.
---

## Introduction

Harnessing Route53's health checks and automated traffic redirection not only fortifies your architecture but also 
ensures continuity of service during regional outages. This approach embodies resilience, automatically rerouting users
to a healthy secondary zone if the primary region falters, thereby upholding system availability and responsiveness.
It's a strategic safeguard, integral for maintaining seamless user experiences under adverse conditions.


## Getting started

This guide is designed for users new to the Route53 and FIS services and assumes basic knowledge of the AWS CLI and our
[`awslocal`](https://github.com/localstack/awscli-local) wrapper script. To read extensively about the FIS service, please
refer to the dedicated [documentation page](https://docs.localstack.cloud/user-guide/aws/fis/) and [here](https://docs.localstack.cloud/user-guide/aws/route53/) for Route53.

In this example we have an AWS-based architecture with an active-primary and passive-standby setup. Route53 
directs traffic to the primary region, which handles product-related requests via API Gateway and Lambda functions, 
with data stored in a DynamoDB. In case of primary region failure, Route53 switches to the standby region, which 
is kept in sync through a replication Lambda function. We can better visualize it with the diagram:

{{< figure src="route53-failover-1.png" >}}


Start LocalStack using the `docker-compose.yml` file from the repository and make sure you provide your API key as an environment
variable:

{{< command >}}
$ LOCALSTACK_API_KEY=<YOUR_LOCALSTACK_API_KEY>
$ docker compose up
{{< /command >}}


## Creating the resources 

In order to get started, we need to deploy the same set of services in both regions, `us-west-1` and `us-east-1`. The resources 
defined in the `init-resources.sh` file will be created at the start of the LocalStack container, using `initialization hooks` 
and the `awslocal` CLI tool.

Our goal is to ensure that our system has a backup in case there’s a regional outage for the primary availability zone 
(`us-west-1`). Let's zoom in on that region and check the resilience mechanisms that are already in place:

{{< figure src="route53-failover-2.png" >}}

- The primary API Gateway has a health check endpoint that only returns a 200 HTTP status code, just to make sure it’s still there.
- Synchronizing data across different regions can be done through AWS-native solutions like DynamoDB Streams and AWS Lambda, where changes 
to the primary table trigger a Lambda function that replicates the changes to the secondary table. This setup is critical 
for achieving high availability and disaster recovery objectives.


## Configuring Route53

Let’s get started. First, we need to define a hosted zone for Route53, let’s call it “hello-localstack.com”:

```bash
$ HOSTED_ZONE_NAME=hello-localstack.com
```

We’re going to retrieve the hosted zone ID, based on its name:

```bash
$ HOSTED_ZONE_ID=$(awslocal route53 create-hosted-zone --name $HOSTED_ZONE_NAME --caller-reference foo | jq -r .HostedZone.Id)
```

And let’s also define the health check ID for the `us-west-1` API Gateway:

```bash
$ HEALTH_CHECK_ID=$(awslocal route53 create-health-check --caller-reference foobar --health-check-config '{
    "FullyQualifiedDomainName": "12345.execute-api.localhost.localstack.cloud",
    "Port": 4566,
    "ResourcePath": "/dev/healthcheck",
    "Type": "HTTP",
    "RequestInterval": 10
}' | jq -r .HealthCheck.Id)
```

This command is pretty self-explanatory, it creates a local Route 53 health check for an HTTP endpoint 
(**`12345.execute-api.localhost.localstack.cloud:4566/dev/healthcheck`**) with a request interval of 10 seconds, and 
retrieves the ID of the HealthCheck JSON object that is returned. When creating or updating AWS resources, the caller reference 
identifier helps prevent accidental duplication of resources in case the request is submitted multiple times.

We want to update the DNS records in the Route53 hosted zone specified by **`$HOSTED_ZONE_ID`**. It adds two new CNAME 
records: one for `12345.$HOSTED_ZONE_NAME` pointing to `12345.execute-api.localhost.localstack.cloud` and another 
for `67890.$HOSTED_ZONE_NAME` pointing to `67890.execute-api.localhost.localstack.cloud`. The TTL (Time to Live) 
for these records is set to 60 seconds:

```bash
$ awslocal route53 change-resource-record-sets --hosted-zone $HOSTED_ZONE_ID --change-batch '{
                                             "Changes": [
                                                 {
                                                     "Action": "CREATE",
                                                     "ResourceRecordSet": {
                                                         "Name": "12345.'$HOSTED_ZONE_NAME'",
                                                         "Type": "CNAME",
                                                         "TTL": 60,
                                                         "ResourceRecords": [{"Value": "12345.execute-api.localhost.localstack.cloud"}]
                                                     }
                                                 },
                                                 {
                                                     "Action": "CREATE",
                                                     "ResourceRecordSet": {
                                                         "Name": "67890.'$HOSTED_ZONE_NAME'",
                                                         "Type": "CNAME",
                                                         "TTL": 60,
                                                         "ResourceRecords": [{"Value": "67890.execute-api.localhost.localstack.cloud"}]
                                                     }
                                                 }
                                             ]}'
```

Lastly, we can update the DNS records in Route53 hosted zone specified by **`$HOSTED_ZONE_ID`**. We’re creating two 
CNAME records for the subdomain `test.$HOSTED_ZONE_NAME`. The first record has the alias target set to
`12345.$HOSTED_ZONE_NAME` and is associated with the health check we previously created, marked as the primary 
(failover) target. The second record has the alias target set to `67890.$HOSTED_ZONE_NAME` and is marked as the secondary 
failover target:

```bash
$ awslocal route53 change-resource-record-sets --hosted-zone-id $HOSTED_ZONE_ID --change-batch '{
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
                                             ]}'
```

This has been the minimum failover configuration where traffic is directed to different endpoints based on health 
check status. Now we can verify that the CNAME record of **`test.hello-localstack.com`** points 
to **`[12345.execute-api.localhost.localstack.cloud](http://12345.execute-api.localhost.localstack.cloud)`** , by using 
the following `dig` command:

```bash
$ dig @localhost test.hello-localstack.com CNAME
                                             
.....
;; QUESTION SECTION:
;test.hello-localstack.com.	IN	CNAME

;; ANSWER SECTION:
test.hello-localstack.com. 300	IN	CNAME	12345.execute-api.localhost.localstack.cloud.
 .....
```

## Controlled outage

Our setup is ready to go. Now it’s time for a little chaos.

To simulate a regional outage for the `us-west-1` region, we create an
experiment that completely stops the invocation of services in this region, including the healthcheck function. 
With the primary region non-operational, Route 53 health checks would fail, triggering the predefined failover 
policy to redirect traffic to the equivalent services in the secondary region, ensuring continuity of service.

```bash
$ cat region-outage-experiment.json 
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
}⏎                                             
```

This FIS experiment template is designed to simulate an `Service Unavailable` error (503 error code) in the "us-west-1" region.
Let's create the experiment template:

```bash
$ awslocal fis create-experiment-template --cli-input-json file://region-outage-experiment.json
```

After the creation of the experiment template, we can use its ID to start the experiment.

```bash
awslocal fis start-experiment --experiment-template-id 6cd0d0e2-b48d-4337-9eec-6e740764c2cc
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
```

Once the experiment is started Route 53 will detect the failure through its health check mechanism and,
according to the failover configuration, will automatically reroute the traffic to the standby region.
We can verify that using the `dig` command:

```bash
$ dig @localhost test.hello-localstack.com CNAME
                                             
.....
;; QUESTION SECTION:
;test.hello-localstack.com.	IN	CNAME

;; ANSWER SECTION:
test.hello-localstack.com. 300	IN	CNAME	67890.execute-api.localhost.localstack.cloud.
 .....

```
Now our hosted zone name is pointing to the secondary API Gateway endpoint, meaning services in `us-east-1` will be used.

With a very simple Python script we can emulate a backend handling of this switch:

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

This script resolves a CNAME record for 'test.hello-localstack.com' using a specified local DNS server, constructs a 
URL with the resolved domain, makes an HTTP GET request to that URL, and prints the response or error encountered.

If we run it, the Product object with the specified ID will be retrieved using the `us-east-1` DynamoDB:

```bash
$ python3 dns-resolver.py

{"price":"29.99","name":"Super Widget","description":"A versatile widget that can be used for a variety of purposes.
 Durable, reliable, and affordable.","id":"prod-1088"}

```

And if we check the LocalStack logs, they will clearly indicate which API Gateway has been called, based on the resolved
domain:

```bash
2023-11-07T11:59:28.292 DEBUG --- [   asgi_gw_9] l.s.l.i.version_manager    : > {resource: /productApi,path: /productApi,httpMethod: GET,headers: {Host=67890.execute-api.localhost.localstack.cloud:4566,
 User-Agent=python-requests/2.31.0, accept-encoding=gzip, deflate, accept=*/*, Connection=keep-alive, x-localstack-tgt-api=apigateway ....
 
```





