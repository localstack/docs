---
title: "Elastic Load Balancing"
linkTitle: "Elastic Load Balancing"
categories: ["LocalStack Pro"]
description: Elastic Load Balancing
---


## Pro

LocalStack Pro supports Elastic Load Balancing operations for both version 1 and 2.

Application load balancers also support request forwarding to IP address and Lambda targets.


### IP Targets

This example illustrates a load balancer configured for an IP target.

Start an HTTP server which will serve as the target of our load balancer.

{{< command >}}
$ docker run -itd -p 5678:5678 docker.io/hashicorp/http-echo:latest -text 'hello from the IP target'
{{< /command >}}

Create the load balancer, target group and register the target, which is the above Docker container in this case.

{{< command >}}
$ awslocal ec2 describe-subnets --filters Name=availability-zone,Values=us-east-1f \
    | jq .Subnets[].SubnetId
"subnet-22d4f64a"

$ awslocal elbv2 create-load-balancer --name example-lb --subnets subnet-22d4f64a \
    | jq '.LoadBalancers[]|.LoadBalancerArn,.DNSName'
"arn:aws:elasticloadbalancing:us-east-1:112233445566:loadbalancer/app/example-lb/50dc6c495c0c9188"
"example-lb.elb.localhost.localstack.cloud"

$ awslocal elbv2 create-target-group --name example-target-group --protocol HTTP --target-type ip \
    | jq .TargetGroups[].TargetGroupArn
"arn:aws:elasticloadbalancing:us-east-1:112233445566:targetgroup/example-target-group/50dc6c495c0c9188"

$ awslocal elbv2 register-targets \
        --targets Id=127.0.0.1,Port=5678,AvailabilityZone=all \
        --target-group-arn arn:aws:elasticloadbalancing:us-east-1:112233445566:targetgroup/example-target-group/50dc6c495c0c9188
{{< /command >}}

Create a listener and a rule so that incoming requests are forwarded to the target.

{{< command >}}
$ awslocal elbv2 create-listener \
        --default-actions '{"Type":"forward","TargetGroupArn":"arn:aws:elasticloadbalancing:us-east-1:112233445566:targetgroup/example-target-group/50dc6c495c0c9188","ForwardConfig":{"TargetGroups":[{"TargetGroupArn":"arn:aws:elasticloadbalancing:us-east-1:112233445566:targetgroup/example-target-group/50dc6c495c0c9188","Weight":11}]}}' \
        --load-balancer-arn arn:aws:elasticloadbalancing:us-east-1:112233445566:loadbalancer/app/example-lb/50dc6c495c0c9188 \
    | jq '.Listeners[]|.ListenerArn,.Port'
"arn:aws:elasticloadbalancing:us-east-1:112233445566:listener/app/example/50dc6c495c0c9188/4566140160361637296"
4566

$ awslocal elbv2 create-rule \
        --conditions Field=path-pattern,Values=/ \
        --priority 1 \
        --actions '{"Type":"forward","TargetGroupArn":"arn:aws:elasticloadbalancing:us-east-1:112233445566:targetgroup/example-target-group/50dc6c495c0c9188","ForwardConfig":{"TargetGroups":[{"TargetGroupArn":"arn:aws:elasticloadbalancing:us-east-1:112233445566:targetgroup/example-target-group/50dc6c495c0c9188","Weight":11}]}}' \
        --listener-arn arn:aws:elasticloadbalancing:us-east-1:112233445566:listener/app/example/50dc6c495c0c9188/4566140160361637296 \
    | jq .Rules[].RuleArn
"arn:aws:elasticloadbalancing:us-east-1:112233445566:listener-rule/app/example/50dc6c495c0c9188/4566140160361637296/60d9790dd44c69e5"
{{< /command >}}

Finally, issue HTTP request to the `DNSName` parameter of `CreateLoadBalancer` operation, and `Port` parameter of `CreateListener` command.
In the above example, these parameter are filtered using `jq`.

{{< command >}}
$ curl example-lb.elb.localhost.localstack.cloud:4566
hello from the IP target
{{< /command >}}
