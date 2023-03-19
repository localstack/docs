---
title: "Deploying containers on Elastic Container Service (ECS) clusters using Elastic Container Registry (ECR) and AWS Fargate, with LocalStack"
linkTitle: "Deploying containers on Elastic Container Service (ECS) clusters using Elastic Container Registry (ECR) and AWS Fargate, with LocalStack"
weight: 6
description: >
  Set up an NGINX web server via Elastic Container Service (ECS) and Elastic Container Registry (ECR) to serve a static website using LocalStack. Learn how you can use CloudFormation templates to declaratively define, create, and deploy your architecture locally with LocalStack's `awslocal` CLI.
type: tutorials
---

[Amazon Elastic Container Service (ECS)](https://aws.amazon.com/ecs/) is a fully-managed container orchestration service that allows you to run and manage Docker containers on AWS. With ECS, you can deploy, manage, and scale containerized applications quickly and efficiently, which includes microservices, batch processing jobs, and web applications. ECS supports two [launch types](https://docs.aws.amazon.com/AmazonECS/latest/developerguide/launch_types.html): EC2 and Fargate. With the EC2 launch type, you can run containers on a cluster of EC2 instances you manage. With Fargate, AWS manages the underlying infrastructure, and you only need to worry about the container. Fargate launch type provides a serverless-like experience for running containers, allowing you to focus on your applications rather than infrastructure.

[Amazon Elastic Container Registry (ECR)](https://aws.amazon.com/ecr/) allows users to push their software packaged inside containers into an AWS-managed registry. Using ECR, you can version, tag, and manage your image lifecycles independently of your application. ECR is tightly integrated with other AWS services, such as ECS, EKS, and Lambda, and allows you to deploy your container image to these services. We can configure our ECS tasks to pull container images from ECR repositories. You can also use ECS task definitions to specify container settings such as CPU and memory limits, environment variables, and networking configuration, thus enabling you to focus on building and deploying your containerized applications with ease.

[LocalStack Pro](https://localstack.cloud/) supports the creation of ECR registries and repositories, as well as ECS clusters and tasks on your local machine. In this tutorial, we will demonstrate how to use it to set up an NGINX web server to serve a static website by deploying CloudFormation templates on a local AWS environment provisioned by LocalStack.

## Prerequisites

-   [LocalStack Pro](https://localstack.cloud/pricing/)  to emulate the AWS services (SNS, SQS, SES, etc) locally
    -   Don’t worry, if you don’t have a subscription yet, you can just get a trial license for free.
-   [awslocal](https://docs.localstack.cloud/integrations/aws-cli/#localstack-aws-cli-awslocal)
-   [Docker](https://docker.io/)
-   [`cURL`](https://curl.se/download.html)

## Creating the Docker image

To start setting up an NGINX web server on an ECS cluster, we will first create the Docker image, which can be further pushed to an ECR repository. Let us start by creating a `Dockerfile` for our NGINX web server. The `Dockerfile` will be used to build the Docker image for our NGINX web server.

```dockerfile
FROM nginx

ENV foo=bar
```

The `Dockerfile` uses the official `nginx` image from Docker Hub, enabling us to serve the default index page. Before building our Docker image, we will start LocalStack and create an ECR repository to push our Docker image. Start LocalStack with the `LOCALSTACK_API_KEY` environment variable to use your LocalStack Pro API key.

```bash
$ LOCALSTACK_API_KEY=<your-api-key> localstack start -d
```

Next, we will create an ECR repository to push our Docker image. We will use the `awslocal` CLI to create the repository.

```bash
awslocal ecr create-repository --repository-name <REPOSITORY_NAME>
```

Define a `REPSITORY_NAME` for your ECR repository and replace it in the above command. The output of the above command will be similar to the following:

```json
{
    "repository": {
        "repositoryArn": "arn:aws:ecr:us-east-1:000000000000:repository/<REPOSITORY_NAME>",
        "registryId": "000000000000",
        "repositoryName": "<REPOSITORY_NAME>",
        "repositoryUri": "localhost.localstack.cloud:4510/<REPOSITORY_NAME>",
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

Copy the `repositoryUri` value from the above output and replace the `REPOSITORY_URI` value in the following command.

```bash
$ docker build -t <REPOSITORY_URI> .
```

The above command will build the Docker image for our NGINX web server. Next, we will push the Docker image to the ECR repository we created earlier.

```bash
$ docker push <REPOSITORY_URI>
```

The Docker image will take a few seconds to be pushed to the local ECR repository. Once the Docker image is pushed to the ECR repository, we will create an ECS cluster and deploy our NGINX web server.

## Creating the local ECS infrastructure

LocalStack supports ECS task definitions, services, and tasks. It allows deploying our ECR containers via the ECS Fargate launch type, which utilizes the local Docker engine to deploy containers locally. Before deploying our NGINX web server, we will create the required ECS infrastructure on our local machine using a CloudFormation template. Based on a [publically available CloudFormation template](https://github.com/awslabs/aws-cloudformation-templates/blob/master/aws/services/ECS/FargateLaunchType/clusters/public-vpc.yml), you can create a new file named `ecs.infra.yml` inside a new `templates` directory.

Let us start by adding the `Mappings`, and configuring the subnet masks' hard values. These masks define the range of internal IP addresses that can be assigned. We will configure two subnets that cover the ranges from `10.0.0.0` to `10.0.255.255`.

```yaml
AWSTemplateFormatVersion: '2010-09-09'
Description: A stack for deploying containerized applications in AWS Fargate.
             This stack runs containers in a public VPC subnet, and includes a
             public facing load balancer to register the services in.
Mappings:
  SubnetConfig:
    VPC:
      CIDR: '10.0.1.0/16'
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
  GatewayAttachement:
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
    DependsOn: GatewayAttachement
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

Above, we have set up the VPC in which containers will be networked and created networking resources for the public subnets. Going further, we added a security group for the container running in Fargate and an IAM role that authorizes ECS to manage resources in the VPC.

We can now configure the outputs generated by the CloudFormation template:

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

Let us now deploy the above CloudFormation template. We can do this by running the following command:

```bash
$ awslocal cloudformation create-stack --stack-name <STACK_NAME> --template-body file://templates/ecs.infra.yml
```

Configure the `<STACK_NAME>` with the name of your choice. You can check wait until the stack status is `CREATE_COMPLETE` by running the following command:

```bash
awslocal cloudformation wait stack-create-complete --stack-name <STACK_NAME>
```

You can check out your deployed stack on the LocalStack Web Application by navigating to the [CloudFormation resource browser](https://app.localstack.cloud/resources/cloudformation/stacks). Let us now go ahead and deploy the ECS service.

## Deploying the ECS service

To deploy the ECS service, we will use another CloudFormation template. Create another file named `ecs.sample.yml` in the `templates` directory, based on the [publically available CloudFormation template](https://github.com/awslabs/aws-cloudformation-templates/blob/master/aws/services/ECS/FargateLaunchType/services/public-service.yml). This template will deploy the ECS service on AWS Fargate and expose it via a public load balancer.

Let us first declare the parameters for the CloudFormation template:

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

Let us now deploy the above CloudFormation template. We can do this by running the following command:

```bash
$ awslocal cloudformation create-stack --stack-name <STACK_NAME> --template-body file://templates/ecs.sample.yml --parameters ParameterKey=ImageUrl,ParameterValue=<REPOSITORY_URI>
```

To verify that the ECS service is deployed successfully, you can check the status of the stack by running the following command:

```bash
$ awslocal cloudformation wait stack-create-complete --stack-name <STACK_NAME>
```

We have the ECS service deployed successfully. Let us now go ahead and access the application endpoint. Before doing that, let us list all the ECS clusters we have deployed in our local environment. Run the following command to list the cluster ARN:

```bash
$ awslocal ecs list-clusters | jq -r '.clusterArns[0]'
```

Save the output of the above command as `CLUSTER_ARN`, as we will use it to list all the tasks running in the cluster. Run the following command to list the task ARN:

```bash
$ awslocal ecs list-tasks --cluster <CLUSTER_ARN> | jq -r '.taskArns[0]'
```

Save the task ARN as `TASK_ARN`. Let us list the port number on which the application is running. Run the following command:

```bash
$ awslocal ecs describe-tasks --cluster <CLUSTER_ARN> --tasks <TASK_ARN> | jq -r '.tasks[0].containers[0].networkBindings[0].hostPort'
```

Earlier, we configured the application to run on port `45139`, in our `HostPort` parameter. Let us now access the application endpoint. Run the following command to get the public IP address of the host:

```bash
$ curl localhost:45139 
```

Alternatively, in the address bar, you can navigate to your web browser and enter [`localhost:45139`](https://localhost:45139/). You should see the default index page of the NGINX web server.

## Conclusion

In conclusion, this tutorial showcases deploying a containerized service locally using Amazon ECS, ECR, and LocalStack. We have also showcased how you can deploy your local AWS infrastructure using CloudFormation templates with the `awslocal` CLI. With LocalStack, you can also mount code from your host filesystem into the ECS container to enable a quick debugging loop where you can test changes without having to build and redeploy the task’s Docker image each time.

The code for this tutorial can be found in our [LocalStack Pro samples](https://github.com/localstack/localstack-pro-samples/tree/master/ecs-ecr-container-app) over GitHub, including a `Makefile` to execute it step-by-step.
