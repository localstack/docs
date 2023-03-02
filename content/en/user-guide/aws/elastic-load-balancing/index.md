---
title: "Elastic Load Balancing"
linkTitle: "Elastic Load Balancing"
categories: ["LocalStack Pro"]
description: Get started with Elastic Load Balancing (ELB) on LocalStack
aliases:
  - /aws/elastic-load-balancing/
---


LocalStack Pro supports Elastic Load Balancing operations for both version 1 and 2.

Application load balancers also support request forwarding to IP address and Lambda targets.


### IP Targets

This example illustrates a load balancer configured for an IP target.

Start an HTTP server which will serve as the target of our load balancer.

{{< command >}}
$ docker run --rm -itd -p 5678:80 ealen/echo-server
{{< /command >}}

Create the load balancer, target group and register the target, which is the above Docker container in this case.

{{< command >}}
$ subnet=$(awslocal ec2 describe-subnets --filters Name=availability-zone,Values=us-east-1f | jq -r '.Subnets[].SubnetId')

$ loadBalancer=$(awslocal elbv2 create-load-balancer --name example-lb --subnets $subnet \
    | jq -r '.LoadBalancers[]|.LoadBalancerArn')

$ targetGroup=$(awslocal elbv2 create-target-group --name example-target-group --protocol HTTP --target-type ip \
    | jq -r '.TargetGroups[].TargetGroupArn')

$ awslocal elbv2 register-targets --targets Id=127.0.0.1,Port=5678,AvailabilityZone=all --target-group-arn $targetGroup
{{< /command >}}

Create a listener and a rule so that incoming requests are forwarded to the target.

{{< command >}}
$ listenerArn=$(awslocal elbv2 create-listener \
        --default-actions '{"Type":"forward","TargetGroupArn":"'$targetGroup'","ForwardConfig":{"TargetGroups":[{"TargetGroupArn":"'$targetGroup'","Weight":11}]}}' \
        --load-balancer-arn $loadBalancer | jq -r '.Listeners[]|.ListenerArn')

$ listenerRule=$(awslocal elbv2 create-rule \
        --conditions Field=path-pattern,Values=/ \
        --priority 1 \
        --actions '{"Type":"forward","TargetGroupArn":"'$targetGroup'","ForwardConfig":{"TargetGroups":[{"TargetGroupArn":"'$targetGroup'","Weight":11}]}}' \
        --listener-arn $listenerArn \
    | jq -r '.Rules[].RuleArn')
{{< /command >}}

Finally, we issue an HTTP request to the `DNSName` parameter of `CreateLoadBalancer` operation, and `Port` parameter of `CreateListener` command.
In the above example, these parameters are filtered using `jq`.

{{< command >}}
$ curl example-lb.elb.localhost.localstack.cloud:4566
{"host":{"hostname":"..."},"http":{"method":"GET","baseUrl":"","originalUrl":"/","protocol":"http"},...}}
{{< /command >}}

### Limitations

The Aplication Load Balancer currently supports only the `forward` and `redirect` action types.
