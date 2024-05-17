---
title: "Cloud Custodian"
linkTitle: "Cloud Custodian"
description: >
  Use Cloud Custodian with LocalStack
---

## Introduction

Cloud Custodian is an open-source rules engine and cloud management tool designed to help organizations maintain security and compliance across their cloud environments. Cloud Custodian's YAML DSL allows definition of rules to filter and tag resources, and then apply actions to those resources. 

Cloud Custodian can be used to manage local AWS resources in LocalStack, resembling the live AWS environment, allowing you to test and validate your security policies locally. You can use Cloud Custodian with LocalStack by just specifying the Cloud Custodian package to use the LocalStack profile configured with your AWS CLI.

## Getting started

This guide is designed for users who are new to Cloud Custodian and assumes basic knowledge of the AWS CLI and our [`awslocal`](https://github.com/localstack/awscli-local) wrapper script.

Start your LocalStack container using your preferred method. We will demonstrate how you can spin up an EC2 instance and tag it with the key `Custodian`, and then use Cloud Custodian to stop the instance.

### Install Cloud Custodian

To install Cloud Custodian, run the following command:

{{< command >}}
$ pip install c7n
{{< / command >}}

After installing Cloud Custodian, you can configure a [custom LocalStack profile](http://docs.localstack.cloud/user-guide/integrations/aws-cli/#configuring-a-custom-profile) in your AWS CLI configuration file.

### Create an EC2 instance

You can create an EC2 instance using the `awslocal` wrapper script. You can use the [`RunInstances`](https://docs.aws.amazon.com/AWSEC2/latest/APIReference/API_RunInstances.html) API to create an EC2 instance. The following example creates an EC2 instance with the tag `Custodian` (any value):

{{< command >}}
$ awslocal ec2 run-instances \
    --image-id ami-ff0fea8310f3 \
    --count 1 \
    --instance-type t3.nano \
    --tag-specifications "ResourceType=instance,Tags=[{Key=Custodian,Value=AnyValue}]"
{{< / command >}}

You can navigate to the LocalStack logs to verify that the EC2 instance was created successfully:

```bash
2023-10-16T15:27:35.479  INFO --- [   asgi_gw_0] l.u.container_networking   : Determined main container network: bridge
2023-10-16T15:27:35.504  INFO --- [   asgi_gw_0] l.u.container_networking   : Determined main container target IP: 172.17.0.2
2023-10-16T15:27:36.154  INFO --- [   asgi_gw_0] l.s.ec2.vmmanager.docker   : Instance i-d87f1ab75e95ab0d2 will be accessible via SSH at: 127.0.0.1:22, 172.17.0.3:22
2023-10-16T15:27:36.155  INFO --- [   asgi_gw_0] l.s.ec2.vmmanager.docker   : Instance i-d87f1ab75e95ab0d2 port mappings (container -> host): {'22/tcp': 22}
2023-10-16T15:27:36.218  INFO --- [   asgi_gw_0] localstack.request.aws     : AWS ec2.RunInstances => 200
```

### Create a Cloud Custodian policy

You can now create a Cloud Custodian policy to stop the EC2 instances with the tag `Custodian`. Create a file named `custodian.yml` and add the following content:

```yaml
policies:
  - name: my-first-policy
    resource: aws.ec2
    filters:
      - "tag:Custodian": present
    actions:
      - stop
```

The above policy specifies the following:

- `name`: The name of the policy.
- `resource`: The AWS resource to apply the policy to.
- `filters`: The filters to apply to the resource. In this case, the filter is `tag:Custodian` and the value is `present`.
- `actions`: The actions to apply to the resource. In this case, the action is `stop`.

### Run the Cloud Custodian policy

You can now run the Cloud Custodian policy using the following command:

{{< command >}}
$ custodian run \
    --output-dir=. custodian.yml \
    --profile localstack
{{< / command >}}

{{< callout "tip" >}}
Alternatively, you can also set the `AWS_PROFILE=localstack` environment variable, in which case the `--profile localstack` parameter can be omitted in the commands above.
{{< /callout >}}

You should see the following output:

```sh
2023-10-16 21:06:13,853: custodian.policy:INFO policy:my-first-policy resource:aws.ec2 region:us-east-1 count:1 time:0.20
2023-10-16 21:06:13,961: custodian.policy:INFO policy:my-first-policy action:stop resources:1 execution_time:0.10
```

You can then navigate to the LocalStack logs to verify that the EC2 instance was stopped successfully:

```bash
2023-10-16T15:36:13.583  INFO --- [   asgi_gw_0] localstack.request.aws     : AWS sts.GetCallerIdentity => 200
2023-10-16T15:36:13.851  INFO --- [   asgi_gw_1] localstack.request.aws     : AWS ec2.DescribeInstances => 200
2023-10-16T15:36:13.960  INFO --- [   asgi_gw_0] localstack.request.aws     : AWS ec2.StopInstances => 200
```

### Create CloudWatch metrics for Cloud Custodian

Cloud Custodian creates CloudWatch metrics for each policy. These metrics show how many resources met the filters, the time taken to gather and filter those resources, and the time required to perform actions.

Certain filters and actions might produce their own metrics. To activate metric output, you must set the `metrics` flag running Cloud Custodian.

{{< command >}}
$ custodian run -s . \
    --metrics aws custodian.yml \
    --profile localstack
{{< / command >}}

You can access the CloudWatch metrics in the [LocalStack Web Application](https://app.localstack.cloud/inst/default/resources/cloudwatch).

## Further reading

- [Example Policies](https://cloudcustodian.io/docs/aws/examples/index.html) for practical examples of specific policies for individual AWS modules.
- [Cloud Custodian documentation](https://cloudcustodian.io/docs/quickstart/index.html) to learn more about Cloud Custodian.
- [Integrations](https://cloudcustodian.io/docs/aws/topics/index.html) with Config, Security Hub, Systems Manager, and X-Ray.
- [Monitoring the environment](https://cloudcustodian.io/docs/aws/usage.html) by generating CloudWatch metrics.
