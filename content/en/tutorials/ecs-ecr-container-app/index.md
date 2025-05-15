---
title: "Deploying containers on Elastic Container Service (ECS) clusters using Elastic Container Registry (ECR) and AWS Fargate, with LocalStack"
linkTitle: "Deploying containers on Elastic Container Service (ECS) clusters using Elastic Container Registry (ECR) and AWS Fargate, with LocalStack"
weight: 6
description: >
  Set up an NGINX web server via Elastic Container Service (ECS) and Elastic Container Registry (ECR) to serve a static website using LocalStack. Learn how you can use CloudFormation templates to declaratively define, create, and deploy your architecture locally with LocalStack's `awslocal` CLI.
type: tutorials
teaser: ""
services:
- ecs
- ecr
platform:
- Shell
deployment:
- awscli
tags:
- BASH
- ECS
- ECR
- Fargate
- CloudFormation
- NGINX
pro: true
leadimage: "ecs-ecr-container-app-featured-image.png"
---

[Amazon Elastic Container Service (ECS)](https://aws.amazon.com/ecs/) is a fully-managed container orchestration service that simplifies the deployment, management, and scaling of Docker containers on AWS.
With support for two [launch types](https://docs.aws.amazon.com/AmazonECS/latest/developerguide/launch_types.html), EC2 and Fargate, ECS allows you to run containers on your cluster of EC2 instances or have AWS manage your underlying infrastructure with Fargate.
The Fargate launch type provides a serverless-like experience for running containers, allowing you to focus on your applications instead of infrastructure.

[Amazon Elastic Container Registry (ECR)](https://aws.amazon.com/ecr/) is a fully-managed service that allows you to store, manage, and deploy Docker container images.
It is tightly integrated with other AWS services such as ECS, EKS, and Lambda, enabling you to quickly deploy your container images to these services.
With ECR, you can version, tag, and manage your container images’ lifecycles independently of your applications, making it easy to maintain and deploy your containers.

ECS tasks can pull container images from ECR repositories and are customizable using task definitions to specify settings such as CPU and memory limits, environment variables, and networking configurations. [LocalStack Pro](https://localstack.cloud/) allows creating ECR registries, repositories, and ECS clusters and tasks on your local machine.
This tutorial will showcase using LocalStack to set up an NGINX web server to serve a static website using CloudFormation templates in a local AWS environment.

## Prerequisites

- [LocalStack Pro](https://localstack.cloud/pricing/)
- [awslocal]({{< ref "aws-cli#localstack-aws-cli-awslocal" >}})
- [Docker](https://docker.io/)
- [curl](https://curl.se/download.html)

## Creating the Docker image

To start setting up an NGINX web server on an ECS cluster, we need to create a Docker image that can be pushed to an ECR repository.
We'll begin by creating a `Dockerfile` that defines the configuration for our NGINX web server.

```dockerfile
FROM nginx

ENV foo=bar
```

The `Dockerfile` uses the official `nginx` image from Docker Hub, which allows us to serve the default index page.
Before building our Docker image, we need to start LocalStack and create an ECR repository to push our Docker image.
To start LocalStack with the `LOCALSTACK_AUTH_TOKEN` environment variable, run the following command:

{{< command >}}
$ LOCALSTACK_AUTH_TOKEN=<your-auth-token> localstack start -d
{{< / command >}}

Next, we will create an ECR repository to push our Docker image.
We will use the `awslocal` CLI to create the repository.

{{< command >}}
$ awslocal ecr create-repository --repository-name sample-ecr-repo
{{< / command >}}

The output of this command will contain the `repositoryUri` value that we'll need in the next step:

```json
{
    "repository": {
        "repositoryArn": "arn:aws:ecr:us-east-1:000000000000:repository/sample-ecr-repo",
        "registryId": "000000000000",
        "repositoryName": "sample-ecr-repo",
        "repositoryUri": "localhost.localstack.cloud:4510/sample-ecr-repo",
        "createdAt": "<TIMESTAMP>",
        "imageTagMutability": "MUTABLE",
        "imageScanningConfiguration": {
            "scanOnPush": false
        },
        "encryptionConfiguration": {
            "encryptionType": "AES256"
        }
    }
}
```

Copy the `repositoryUri` value from the output and replace `<REPOSITORY_URI>` in the following command:

{{< command >}}
$ docker build -t <REPOSITORY_URI> .
{{< / command >}}

This command will build the Docker image for our NGINX web server.
After the build is complete, we'll push the Docker image to the ECR repository we created earlier using the following command:

{{< command >}}
$ docker push <REPOSITORY_URI>
{{< / command >}}

After a few seconds, the Docker image will be pushed to the local ECR repository.
We can now create an ECS cluster and deploy our NGINX web server.

## Creating the local ECS infrastructure

LocalStack enables the deployment of ECS task definitions, services, and tasks, allowing us to deploy our ECR containers via the ECS Fargate launch type, which uses the local Docker engine to deploy containers locally.
To create the necessary ECS infrastructure on our local machine before deploying our NGINX web server, we will use a CloudFormation template.

You can create a new file named `ecs.infra.yml` inside a new `templates` directory, using a [publicly available CloudFormation template as a starting point](https://github.com/aws-cloudformation/aws-cloudformation-templates/blob/main/ECS/FargateLaunchType/services/public-service.yaml).
To begin, we'll add the `Mappings` section and configure the subnet mask values, which define the range of internal IP addresses that can be assigned.

```yaml
AWSTemplateFormatVersion: '2010-09-09'
Description: A stack for deploying containerized applications in AWS Fargate.
             This stack runs containers in a public VPC subnet, and includes a
             public facing load balancer to register the services in.
Mappings:
  SubnetConfig:
    VPC:
      CIDR: '10.0.0.0/16'
    PublicOne:
      CIDR: '10.0.2.0/24'
    PublicTwo:
      CIDR: '10.0.3.0/24'
```

Let us now declaratively create the VPC, subnets, ECS cluster, and more:

```yaml
Resources:
  VPC:
    Type: AWS::EC2::VPC
    Properties:
      EnableDnsSupport: true
      EnableDnsHostnames: true
      CidrBlock: !FindInMap ['SubnetConfig', 'VPC', 'CIDR']

  PublicSubnetOne:
    Type: AWS::EC2::Subnet
    Properties:
      AvailabilityZone: us-east-1a
      VpcId: !Ref 'VPC'
      CidrBlock: !FindInMap ['SubnetConfig', 'PublicOne', 'CIDR']
      MapPublicIpOnLaunch: true
  PublicSubnetTwo:
    Type: AWS::EC2::Subnet
    Properties:
      AvailabilityZone: us-east-1b
      VpcId: !Ref 'VPC'
      CidrBlock: !FindInMap ['SubnetConfig', 'PublicTwo', 'CIDR']
      MapPublicIpOnLaunch: true

  InternetGateway:
    Type: AWS::EC2::InternetGateway
  GatewayAttachment:
    Type: AWS::EC2::VPCGatewayAttachment
    Properties:
      VpcId: !Ref 'VPC'
      InternetGatewayId: !Ref 'InternetGateway'
  PublicRouteTable:
    Type: AWS::EC2::RouteTable
    Properties:
      VpcId: !Ref 'VPC'
  PublicRoute:
    Type: AWS::EC2::Route
    DependsOn: GatewayAttachment
    Properties:
      RouteTableId: !Ref 'PublicRouteTable'
      DestinationCidrBlock: '0.0.0.0/0'
      GatewayId: !Ref 'InternetGateway'
  PublicSubnetOneRouteTableAssociation:
    Type: AWS::EC2::SubnetRouteTableAssociation
    Properties:
      SubnetId: !Ref PublicSubnetOne
      RouteTableId: !Ref PublicRouteTable
  PublicSubnetTwoRouteTableAssociation:
    Type: AWS::EC2::SubnetRouteTableAssociation
    Properties:
      SubnetId: !Ref PublicSubnetTwo
      RouteTableId: !Ref PublicRouteTable

  ECSCluster:
    Type: AWS::ECS::Cluster

  FargateContainerSecurityGroup:
    Type: AWS::EC2::SecurityGroup
    Properties:
      GroupDescription: Access to the Fargate containers
      VpcId: !Ref 'VPC'

  EcsSecurityGroupIngressFromPublicALB:
    Type: AWS::EC2::SecurityGroupIngress
    Properties:
      Description: Ingress from the public ALB
      GroupId: !Ref 'FargateContainerSecurityGroup'
      IpProtocol: -1
      SourceSecurityGroupId: !Ref 'PublicLoadBalancerSG'

  EcsSecurityGroupIngressFromSelf:
    Type: AWS::EC2::SecurityGroupIngress
    Properties:
      Description: Ingress from other containers in the same security group
      GroupId: !Ref 'FargateContainerSecurityGroup'
      IpProtocol: -1
      SourceSecurityGroupId: !Ref 'FargateContainerSecurityGroup'

  PublicLoadBalancerSG:
    Type: AWS::EC2::SecurityGroup
    Properties:
      GroupDescription: Access to the public facing load balancer
      VpcId: !Ref 'VPC'
      SecurityGroupIngress:
          # Allow access to ALB from anywhere on the internet
          - CidrIp: 0.0.0.0/0
            IpProtocol: -1
            FromPort: 9000
            ToPort: 9010

  PublicLoadBalancer:
    Type: AWS::ElasticLoadBalancingV2::LoadBalancer
    Properties:
      Scheme: internet-facing
      LoadBalancerAttributes:
      - Key: idle_timeout.timeout_seconds
        Value: '30'
      Subnets:
        - !Ref PublicSubnetOne
        - !Ref PublicSubnetTwo
      SecurityGroups: [!Ref 'PublicLoadBalancerSG']

  DummyTargetGroupPublic:
    Type: AWS::ElasticLoadBalancingV2::TargetGroup
    Properties:
      HealthCheckIntervalSeconds: 6
      HealthCheckPath: /
      HealthCheckProtocol: HTTP
      HealthCheckTimeoutSeconds: 5
      HealthyThresholdCount: 2
      Name: !Join ['-', [!Ref 'AWS::StackName', 'drop-1']]
      Port: 80
      Protocol: HTTP
      UnhealthyThresholdCount: 2
      VpcId: !Ref 'VPC'
  PublicLoadBalancerListener:
    Type: AWS::ElasticLoadBalancingV2::Listener
    DependsOn:
      - PublicLoadBalancer
    Properties:
      DefaultActions:
        - TargetGroupArn: !Ref 'DummyTargetGroupPublic'
          Type: 'forward'
      LoadBalancerArn: !Ref 'PublicLoadBalancer'
      Port: 80
      Protocol: HTTP

  ECSRole:
    Type: AWS::IAM::Role
    Properties:
      AssumeRolePolicyDocument:
        Statement:
        - Effect: Allow
          Principal:
            Service: [ecs.amazonaws.com]
          Action: ['sts:AssumeRole']
      Path: /
      Policies:
      - PolicyName: ecs-service
        PolicyDocument:
          Statement:
          - Effect: Allow
            Action:
              - 'ec2:AttachNetworkInterface'
              - 'ec2:CreateNetworkInterface'
              - 'ec2:CreateNetworkInterfacePermission'
              - 'ec2:DeleteNetworkInterface'
              - 'ec2:DeleteNetworkInterfacePermission'
              - 'ec2:Describe*'
              - 'ec2:DetachNetworkInterface'
              - 'elasticloadbalancing:DeregisterInstancesFromLoadBalancer'
              - 'elasticloadbalancing:DeregisterTargets'
              - 'elasticloadbalancing:Describe*'
              - 'elasticloadbalancing:RegisterInstancesWithLoadBalancer'
              - 'elasticloadbalancing:RegisterTargets'
            Resource: '*'

  ECSTaskExecutionRole:
    Type: AWS::IAM::Role
    Properties:
      AssumeRolePolicyDocument:
        Statement:
        - Effect: Allow
          Principal:
            Service: [ecs-tasks.amazonaws.com]
          Action: ['sts:AssumeRole']
      Path: /
      Policies:
        - PolicyName: AmazonECSTaskExecutionRolePolicy
          PolicyDocument:
            Statement:
            - Effect: Allow
              Action:
                - 'ecr:GetAuthorizationToken'
                - 'ecr:BatchCheckLayerAvailability'
                - 'ecr:GetDownloadUrlForLayer'
                - 'ecr:BatchGetImage'
                - 'logs:CreateLogStream'
                - 'logs:PutLogEvents'
              Resource: '*'
```

So far, we have set up the VPC where the containers will be networked and created networking resources for the public subnets.
We have also added a security group for the container running in Fargate and an IAM role that authorizes ECS to manage resources in the VPC.

Next, we can configure the outputs generated by the CloudFormation template.
These outputs are values generated during the creation of the CloudFormation stack and can be used by other resources or scripts in your application.

To export the values as CloudFormation outputs, we can add the following to the end of our `ecs.infra.yml` file:

```yaml
Outputs:
  ClusterName:
    Description: The name of the ECS cluster
    Value: !Ref 'ECSCluster'
    Export:
      Name: !Join [ ':', [ !Ref 'AWS::StackName', 'ClusterName' ] ]
  ExternalUrl:
    Description: The url of the external load balancer
    Value: !Join ['', ['http://', !GetAtt 'PublicLoadBalancer.DNSName']]
    Export:
      Name: !Join [ ':', [ !Ref 'AWS::StackName', 'ExternalUrl' ] ]
  ECSRole:
    Description: The ARN of the ECS role
    Value: !GetAtt 'ECSRole.Arn'
    Export:
      Name: !Join [ ':', [ !Ref 'AWS::StackName', 'ECSRole' ] ]
  ECSTaskExecutionRole:
    Description: The ARN of the ECS role
    Value: !GetAtt 'ECSTaskExecutionRole.Arn'
    Export:
      Name: !Join [ ':', [ !Ref 'AWS::StackName', 'ECSTaskExecutionRole' ] ]
  PublicListener:
    Description: The ARN of the public load balancer's Listener
    Value: !Ref PublicLoadBalancerListener
    Export:
      Name: !Join [ ':', [ !Ref 'AWS::StackName', 'PublicListener' ] ]
  VPCId:
    Description: The ID of the VPC that this stack is deployed in
    Value: !Ref 'VPC'
    Export:
      Name: !Join [ ':', [ !Ref 'AWS::StackName', 'VPCId' ] ]
  PublicSubnetOne:
    Description: Public subnet one
    Value: !Ref 'PublicSubnetOne'
    Export:
      Name: !Join [ ':', [ !Ref 'AWS::StackName', 'PublicSubnetOne' ] ]
  PublicSubnetTwo:
    Description: Public subnet two
    Value: !Ref 'PublicSubnetTwo'
    Export:
      Name: !Join [ ':', [ !Ref 'AWS::StackName', 'PublicSubnetTwo' ] ]
  FargateContainerSecurityGroup:
    Description: A security group used to allow Fargate containers to receive traffic
    Value: !Ref 'FargateContainerSecurityGroup'
    Export:
      Name: !Join [ ':', [ !Ref 'AWS::StackName', 'FargateContainerSecurityGroup' ] ]
```

To deploy the CloudFormation template we created earlier, use the following command:

{{< command >}}
$ awslocal cloudformation create-stack --stack-name infra --template-body file://templates/ecs.infra.yml
{{< /command >}}

Wait until the stack status changes to `CREATE_COMPLETE` by running the following command:

{{< command >}}
$ awslocal cloudformation wait stack-create-complete --stack-name infra
{{< /command >}}

You can also check your deployed stack on the LocalStack Web Application by navigating to the [CloudFormation resource browser](https://app.localstack.cloud/resources/cloudformation/stacks).
With the ECS infrastructure now in place, we can proceed to deploy our NGINX web server.

## Deploying the ECS service

To deploy the ECS service, we'll use another CloudFormation template.
You can create a new file named `ecs.sample.yml` in the `templates` directory, based on the [publicly available CloudFormation template](https://github.com/awslabs/aws-cloudformation-templates/blob/master/aws/services/ECS/FargateLaunchType/services/public-service.yml).
This template will deploy the ECS service on AWS Fargate and expose it via a public load balancer.

Before we proceed, let's declare the parameters for the CloudFormation template:

```yaml
AWSTemplateFormatVersion: '2010-09-09'
Description: Deploy a service on AWS Fargate, hosted in a public subnet, and accessible via a public load balancer.
Parameters:
  StackName:
    Type: String
    Default: infra
    Description: The name of the parent Fargate networking stack that you created. Necessary
                 to locate and reference resources created by that stack.
  ServiceName:
    Type: String
    Default: nginx
    Description: A name for the service
  ImageUrl:
    Type: String
    Default: nginx
    Description: The url of a docker image that contains the application process that
                 will handle the traffic for this service
  ContainerPort:
    Type: Number
    Default: 80
    Description: What port number the application inside the docker container is binding to
  HostPort:
    Type: Number
    Default: 45139
    Description: What port number the application on the host is binding to
  ContainerCpu:
    Type: Number
    Default: 256
    Description: How much CPU to give the container. 1024 is 1 CPU
  ContainerMemory:
    Type: Number
    Default: 512
    Description: How much memory in megabytes to give the container
  Path:
    Type: String
    Default: "*"
    Description: A path on the public load balancer that this service
                 should be connected to. Use * to send all load balancer
                 traffic to this service.
  Priority:
    Type: Number
    Default: 1
    Description: The priority for the routing rule added to the load balancer.
                 This only applies if your have multiple services which have been
                 assigned to different paths on the load balancer.
  DesiredCount:
    Type: Number
    Default: 2
    Description: How many copies of the service task to run
  Role:
    Type: String
    Default: ""
    Description: (Optional) An IAM role to give the service's containers if the code within needs to
                 access other AWS resources like S3 buckets, DynamoDB tables, etc

Conditions:
  HasCustomRole: !Not [ !Equals [!Ref 'Role', ''] ]
```

Next, we can define the resources, which includes our task, service, target group, and load balancer rule:

```yaml
Resources:
  TaskDefinition:
    Type: AWS::ECS::TaskDefinition
    Properties:
      Family: !Ref ServiceName
      Cpu: !Ref ContainerCpu
      Memory: !Ref ContainerMemory
      NetworkMode: awsvpc
      RequiresCompatibilities:
        - FARGATE
      ExecutionRoleArn:
        Fn::ImportValue:
          !Join [':', [!Ref 'StackName', 'ECSTaskExecutionRole']]
      TaskRoleArn:
        Fn::If:
          - HasCustomRole
          - !Ref Role
          - !Ref AWS::NoValue
      ContainerDefinitions:
        - Name: !Ref ServiceName
          Cpu: !Ref ContainerCpu
          Memory: !Ref ContainerMemory
          Image: !Ref ImageUrl
          PortMappings:
            - ContainerPort: !Ref ContainerPort
              HostPort: !Ref HostPort

  Service:
    Type: AWS::ECS::Service
    DependsOn: LoadBalancerRule
    Properties:
      ServiceName: !Ref 'ServiceName'
      Cluster:
        Fn::ImportValue:
          !Join [':', [!Ref 'StackName', 'ClusterName']]
      LaunchType: FARGATE
      DeploymentConfiguration:
        MaximumPercent: 200
        MinimumHealthyPercent: 75
      DesiredCount: !Ref 'DesiredCount'
      NetworkConfiguration:
        AwsvpcConfiguration:
          AssignPublicIp: ENABLED
          SecurityGroups:
            - Fn::ImportValue:
                !Join [':', [!Ref 'StackName', 'FargateContainerSecurityGroup']]
          Subnets:
            - Fn::ImportValue:
                !Join [':', [!Ref 'StackName', 'PublicSubnetOne']]
            - Fn::ImportValue:
                !Join [':', [!Ref 'StackName', 'PublicSubnetTwo']]
      TaskDefinition: !Ref 'TaskDefinition'
      LoadBalancers:
        - ContainerName: !Ref 'ServiceName'
          ContainerPort: !Ref 'ContainerPort'
          TargetGroupArn: !Ref 'TargetGroup'

  TargetGroup:
    Type: AWS::ElasticLoadBalancingV2::TargetGroup
    Properties:
      HealthCheckIntervalSeconds: 6
      HealthCheckPath: /
      HealthCheckProtocol: HTTP
      HealthCheckTimeoutSeconds: 5
      HealthyThresholdCount: 2
      TargetType: ip
      Name: !Ref 'ServiceName'
      Port: !Ref 'ContainerPort'
      Protocol: HTTP
      UnhealthyThresholdCount: 2
      VpcId:
        Fn::ImportValue:
          !Join [':', [!Ref 'StackName', 'VPCId']]

  LoadBalancerRule:
    Type: AWS::ElasticLoadBalancingV2::ListenerRule
    Properties:
      Actions:
        - TargetGroupArn: !Ref 'TargetGroup'
          Type: 'forward'
      Conditions:
        - Field: path-pattern
          Values: [!Ref 'Path']
      ListenerArn:
        Fn::ImportValue:
          !Join [':', [!Ref 'StackName', 'PublicListener']]
      Priority: !Ref 'Priority'
```

Next, let's deploy the CloudFormation template by running the following command:

{{< command >}}
$ awslocal cloudformation create-stack --stack-name ecs --template-body file://templates/ecs.sample.yml --parameters ParameterKey=ImageUrl,ParameterValue=<REPOSITORY_URI>
{{< /command >}}

Replace `<REPOSITORY_URI>` with the URI of the Docker image that you want to deploy.
Wait for the stack to be created by running the following command:

{{< command >}}
$ awslocal cloudformation wait stack-create-complete --stack-name ecs
{{< /command >}}

Now that the ECS service has been deployed successfully, let's access the application endpoint.
First, let's list all the ECS clusters we have deployed in our local environment by running the following command to retrieve the cluster ARN:

{{< command >}}
$ awslocal ecs list-clusters | jq -r '.clusterArns[0]'
{{< /command >}}

Save the output of the above command as `CLUSTER_ARN`, as we will use it to list the tasks running in the cluster.
Next, run the following command to list the task ARN:

{{< command >}}
$ awslocal ecs list-tasks --cluster <CLUSTER_ARN> | jq -r '.taskArns[0]'
{{< /command >}}

Save the task ARN as `TASK_ARN`.
Let us now list the port number on which the application is running.
Run the following command:

{{< command >}}
$ awslocal ecs describe-tasks --cluster <CLUSTER_ARN> --tasks <TASK_ARN> | jq -r '.tasks[0].containers[0].networkBindings[0].hostPort'
{{< /command >}}

Earlier, we configured the application to run on port `45139`, in our `HostPort` parameter.
Let us now access the application endpoint.
Run the following command to get the public IP address of the host:

{{< command >}}
$ curl localhost:45139
{{< /command >}}

Alternatively, in the address bar of your web browser, you can navigate to [`localhost:45139`](https://localhost:45139/).
You should see the default index page of the NGINX web server.

## Conclusion

In this tutorial, we have demonstrated how to deploy a containerized service locally using Amazon ECS, ECR, and LocalStack.
We have also shown how you can use CloudFormation templates with the awslocal CLI to deploy your local AWS infrastructure.

With LocalStack, you can easily mount code from your host filesystem into the ECS container, allowing for a quicker debugging loop that doesn't require rebuilding and redeploying the task's Docker image for each change.

To try out this tutorial for yourself, you can find the code in our LocalStack Pro samples on [LocalStack Pro samples](https://github.com/localstack/localstack-pro-samples/tree/master/ecs-ecr-container-app) over GitHub, including a `Makefile` to execute each step of the process.
