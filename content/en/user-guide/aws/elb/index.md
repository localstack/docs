---
title: "Elastic Load Balancing (ELB)"
linkTitle: "Elastic Load Balancing (ELB)"
description: Get started with Elastic Load Balancing (ELB) on LocalStack
tags: ["Pro image"]
---

## Introduction

Elastic Load Balancing (ELB) is a service that allows users to distribute incoming traffic across multiple targets, such as EC2 instances, containers, IP addresses, and lambda functions and automatically scales its request handling capacity in response to incoming traffic. It also monitors the health of its registered targets and ensures that it routes traffic only to healthy targets. You can check [the official AWS documentation](https://docs.aws.amazon.com/elasticloadbalancing/latest/userguide/what-is-load-balancing.html) to understand the basic terms and concepts used in the ELB.

Localstack allows you to use the Elastic Load Balancing APIs in your local environment to create, edit, and view load balancers, target groups, listeners, and rules. The supported APIs are available on our [API coverage page](https://docs.localstack.cloud/references/coverage/coverage_elbv2/), which provides information on the extent of ELB's integration with LocalStack.

## Getting started

This guide is designed for users new to Elastic Load Balancing and assumes basic knowledge of the AWS CLI and our [`awslocal`](https://github.com/localstack/awscli-local) wrapper script.

Start your LocalStack container using your preferred method. We will demonstrate how to create an Application Load Balancer, along with its target group, listener, and rule, and forward requests to an IP target.

### Start a target server

Launch an HTTP server which will serve as the target for our load balancer.

{{< command >}}
$ docker run --rm -itd -p 5678:80 ealen/echo-server
{{< /command >}}

### Create a load balancer

To specify the subnet and VPC in which the load balancer will be created, you can use the [`DescribeSubnets`](https://docs.aws.amazon.com/elasticloadbalancing/latest/APIReference/API_DescribeSubnets.html) API to retrieve the subnet ID and VPC ID. In this example, we will use the subnet and VPC in the `us-east-1f` availability zone.

{{< command >}}
$ subnet_info=$(awslocal ec2 describe-subnets --filters Name=availability-zone,Values=us-east-1f \
    | jq -r '.Subnets[] | select(.AvailabilityZone == "us-east-1f") | {SubnetId: .SubnetId, VpcId: .VpcId}')

$ subnet_id=$(echo $subnet_info | jq -r '.SubnetId')

$ vpc_id=$(echo $subnet_info | jq -r '.VpcId')
{{< /command >}}

To create a load balancer, you can use the [`CreateLoadBalancer`](https://docs.aws.amazon.com/elasticloadbalancing/latest/APIReference/API_CreateLoadBalancer.html) API. The following command creates an Application Load Balancer named `example-lb`:

{{< command >}}
$ loadBalancer=$(awslocal elbv2 create-load-balancer --name example-lb \
    --subnets $subnet_id | jq -r '.LoadBalancers[]|.LoadBalancerArn')
{{< /command >}}

### Create a target group

To create a target group, you can use the [`CreateTargetGroup`](https://docs.aws.amazon.com/elasticloadbalancing/latest/APIReference/API_CreateTargetGroup.html) API. The following command creates a target group named `example-target-group`:

{{< command >}}
$ targetGroup=$(awslocal elbv2 create-target-group --name example-target-group \
    --protocol HTTP --target-type ip --port 80 --vpc-id $vpc_id \
    | jq -r '.TargetGroups[].TargetGroupArn')
{{< /command >}}

### Register a target

To register a target, you can use the [`RegisterTargets`](https://docs.aws.amazon.com/elasticloadbalancing/latest/APIReference/API_RegisterTargets.html) API. The following command registers the target with the target group created in the previous step:

{{< command >}}
$ awslocal elbv2 register-targets --targets Id=127.0.0.1,Port=5678,AvailabilityZone=all \
    --target-group-arn $targetGroup
{{< /command >}}

{{< callout >}}
Note that in some cases the `targets` parameter `Id` can be the `Gateway` address of the docker container.
You can find the gateway address by running `docker inspect <container_id>`.
{{< /callout >}}

### Create a listener and a rule

We create a for the load balancer using the [`CreateListener`](https://docs.aws.amazon.com/elasticloadbalancing/latest/APIReference/API_CreateListener.html) API. The following command creates a listener for the load balancer created in the previous step:

{{< command >}}
$ listenerArn=$(awslocal elbv2 create-listener \
        --default-actions '{"Type":"forward","TargetGroupArn":"'$targetGroup'","ForwardConfig":{"TargetGroups":[{"TargetGroupArn":"'$targetGroup'","Weight":11}]}}' \
        --load-balancer-arn $loadBalancer | jq -r '.Listeners[]|.ListenerArn')
{{< /command >}}

To create a rule for the listener, you can use the [`CreateRule`](https://docs.aws.amazon.com/elasticloadbalancing/latest/APIReference/API_CreateRule.html) API. The following command creates a rule for the listener created above:

{{< command >}}
$ listenerRule=$(awslocal elbv2 create-rule \
        --conditions Field=path-pattern,Values=/ \
        --priority 1 \
        --actions '{"Type":"forward","TargetGroupArn":"'$targetGroup'","ForwardConfig":{"TargetGroups":[{"TargetGroupArn":"'$targetGroup'","Weight":11}]}}' \
        --listener-arn $listenerArn \
    | jq -r '.Rules[].RuleArn')
{{< /command >}}

### Send a request to the load balancer

Finally, you can issue an HTTP request to the `DNSName` parameter of `CreateLoadBalancer` operation, and `Port` parameter of `CreateListener` command with the following command:

{{< command >}}
$ curl example-lb.elb.localhost.localstack.cloud:4566
{{< /command >}}

The following output will be retrieved:

```bash
{
  "host": {
    "hostname": "example-lb.elb.localhost.localstack.cloud",
    "ip": "::ffff:172.17.0.1",
    "ips": []
  },
  "http": {
    "method": "GET",
    "baseUrl": "",
    "originalUrl": "/",
    "protocol": "http"
  },
  "request": {
    "params": {
      "0": "/"
    },
    "query": {},
    "cookies": {},
    "body": {},
    "headers": {
      "accept-encoding": "identity",
      "host": "example-lb.elb.localhost.localstack.cloud:4566",
      "user-agent": "curl/7.88.1",
      "accept": "*/*"
    }
  },
  "environment": {
    "PATH": "/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin",
    "HOSTNAME": "bee08b83d633",
    "TERM": "xterm",
    "NODE_VERSION": "18.17.1",
    "YARN_VERSION": "1.22.19",
    "HOME": "/root"
  }
}
```

## Examples

The following code snippets and sample applications provide practical examples of how to use ELB in LocalStack for various use cases:

- [Setting up Elastic Load Balancing (ELB) Application Load Balancers using LocalStack, deployed via the Serverless framework](https://docs.localstack.cloud/tutorials/elb-load-balancing/)

## Current Limitations

- The Application Load Balancer currently supports only the `forward` and `redirect` action types.
- When opting for Route53 CNAMEs to direct requests towards the ALBs, it's important to remember that explicit configuration of the `Host` header to match the resource record might be necessary while making calls.
