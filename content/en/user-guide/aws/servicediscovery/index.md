---
title: "Service Discovery"
linkTitle: "Service Discovery"
description: >
  Get started with Service Discovery on LocalStack
tags: ["Pro image"]
---

## Introduction

Service Discovery simplifies the management and discovery of services by locating and connecting to the components and resources that make up their applications.
Service Discovery allows for a centralized mechanism for dynamically registering, tracking, and resolving service instances, allowing seamless communication between services.
Service discovery uses Cloud Map API actions to manage HTTP and DNS namespaces for services, enabling automatic registration and discovery of services running in the cluster.

LocalStack allows you to use the Service Discovery APIs in your local environment to monitor and manage your services across various environments and network topologies.
The supported APIs are available on our [API coverage page]({{< ref "coverage_servicediscovery" >}}), which provides information on the extent of Service Discovery's integration with LocalStack.

## Getting Started

This guide is designed for users new to Service Discovery and assumes basic knowledge of the AWS CLI and our [`awslocal`](https://github.com/localstack/awscli-local) wrapper script.

Start your LocalStack container using your preferred method.
We will demonstrate how to create an ECS service containing a Fargate task that uses Service Discovery with the AWS CLI.

### Create a Cloud Map service discovery namespace

To set up a private Cloud Map service discovery namespace, you can utilize the [`CreatePrivateDnsNamespace`](https://docs.aws.amazon.com/cloud-map/latest/api/API_CreatePrivateDnsNamespace.html) API.
This API allows you to define a custom name for your namespace and specify the VPC ID where your services will be locatedBefore proceeding, make sure to create the required VPC.

To create the private Cloud Map service discovery namespace, execute the following command:

{{< command >}}
$ awslocal servicediscovery create-private-dns-namespace \
      --name tutorial \
      --vpc <vpc-id>
{{< /command >}}

Ensure that you replace `<vpc-id>` with the actual ID of the VPC you intend to use for the namespace.
Upon running this command, you will receive an output containing an `OperationId`.
This identifier can be used to check the status of the operation.

To verify the status of the operation, execute the following command:

{{< command >}}
$ awslocal servicediscovery get-operation \
      --operation-id <operation-id>
{{< /command >}}

The output will consist of a `NAMESPACE` ID, which you will need to create a service within the namespace.

### Create a Cloud Map service

After creating the private Cloud Map service discovery namespace, you can proceed to create a service within that namespace using the [`CreateService`](https://docs.aws.amazon.com/cloud-map/latest/api/API_CreateService.html) API
This service represents a specific component or resource in your application.

To create a service within the namespace, execute the following command:

{{< command >}}
$ awslocal servicediscovery create-service \
      --name myapplication \
      --dns-config "NamespaceId="<Namespace-ID>",DnsRecords=[{Type="A",TTL="300"}]" \
      --health-check-custom-config FailureThreshold=1
{{< /command >}}

Upon successful execution, the output will provide you with the Service ID and the Amazon Resource Name (ARN) of the newly created service.
These identifiers will be useful for further operations or integrations.

### Create an ECS cluster

To integrate the service you created earlier with an ECS (Elastic Container Service) service, you can follow the steps below.

Start by creating an ECS cluster using the [`CreateCluster`](https://docs.aws.amazon.com/AmazonECS/latest/APIReference/API_CreateCluster.html) API.
Execute the following command:

{{< command >}}
$ awslocal ecs create-cluster \
      --cluster-name tutorial
{{< /command >}}

### Register a task definition

Next, you will register a task definition that's compatible with Fargate.
Create a file named `fargate-task.json` and add the following content:

```json
{
    "family": "tutorial-task-def",
        "networkMode": "awsvpc",
        "containerDefinitions": [
            {
                "name": "sample-app",
                "image": "httpd:2.4",
                "portMappings": [
                    {
                        "containerPort": 80,
                        "hostPort": 80,
                        "protocol": "tcp"
                    }
                ],
                "essential": true,
                "entryPoint": [
                    "sh",
                    "-c"
                ],
                "command": [
                    "/bin/sh",
                    "-c",
                    "echo '<html> <head> <title>Amazon ECS Sample App</title> <style>body {margin-top: 40px; background-color: #333;} </style> </head><body> <div style=color:white;text-align:center> <h1>Amazon ECS Sample App</h1> <h2>Congratulations!</h2> <p>Your application is now running on a container in Amazon ECS.</p> </div></body></html>' >  /usr/local/apache2/htdocs/index.html && httpd-foreground"
                ]
            }
        ],
        "requiresCompatibilities": [
            "FARGATE"
        ],
        "cpu": "256",
        "memory": "512"
}
```

Register the task definition using the [`RegisterTaskDefinition`](https://docs.aws.amazon.com/AmazonECS/latest/APIReference/API_RegisterTaskDefinition.html) API.
Execute the following command:

{{< command >}}
$ awslocal ecs register-task-definition \
      --cli-input-json file://fargate-task.json
{{< /command >}}

### Create an ECS service

To create an ECS service, you will need to retrieve the `securityGroups` and `subnets` associated with the VPC used to create the Cloud Map namespace.
You can obtain this information by using the [`DescribeVpcs`](https://docs.aws.amazon.com/vpc/latest/APIReference/API_DescribeVpcs.html) API.
Execute the following command to retrieve the details of all VPCs:

{{< command >}}
$ awslocal ec2 describe-vpcs
{{< /command >}}

The output will include a list of VPCs.
Locate the VPC that was used to create the Cloud Map namespace and make a note of its `VpcId` value.

Next, execute the following commands to retrieve the `securityGroups` and `subnets` associated with the VPC:

{{< command >}}
$ awslocal ec2 describe-security-groups --filters Name=vpc-id,Values=vpc-<ID> --query 'SecurityGroups[*].[GroupId, GroupName]' --output text

$ awslocal ec2 describe-subnets --filters Name=vpc-id,Values=vpc-<ID> --query 'Subnets[*].[SubnetId, CidrBlock]' --output text
{{< /command >}}

Replace `<VpcId>` with the actual VpcId value of the VPC you identified earlier.
Make a note of the `GroupId` and `SubnetId` values.

Create a new file named `ecs-service-discovery.json` and add the following content to it:

```json
{
    "cluster": "tutorial",
    "serviceName": "ecs-service-discovery",
    "taskDefinition": "tutorial-task-def",
    "serviceRegistries": [
       {
          "registryArn": <ARN_OF_THE_SERVICE_DISCOVERY>
       }
    ],
    "launchType": "FARGATE",
    "platformVersion": "LATEST",
    "networkConfiguration": {
       "awsvpcConfiguration": {
          "assignPublicIp": "ENABLED",
          "securityGroups": [ "sg-*" ], // Add the security group IDs here
          "subnets": [ "subnet-*" ] // Add the subnet IDs here
       }
    },
    "desiredCount": 1
}
```

Create your ECS service using the [`CreateService`](https://docs.aws.amazon.com/AmazonECS/latest/APIReference/API_CreateService.html) API.
Execute the following command:

{{< command >}}
$ awslocal ecs create-service \
      --cli-input-json file://ecs-service-discovery.json
{{< /command >}}

### Verify the service

You can use the Service Discovery service ID to verify that the service was created successfully.
Execute the following command:

{{< command >}}
$ awslocal servicediscovery list-instances \
       --service-id <service-id>
{{< /command >}}

The output will consist of the resource ID, and you can further use the [`DiscoverInstances`](https://docs.aws.amazon.com/cloud-map/latest/api/API_DiscoverInstances.html) API.
This API allows you to query the DNS records associated with the service and perform various operations.

To explore the DNS records of your service and perform other operations, refer to the [AWS CLI documentation](https://docs.aws.amazon.com/cli/latest/reference/servicediscovery/index.html) for comprehensive instructions and examples.

### Using filters

Filters can be used to narrow down the results of a list operation.
Filters are supported for the following operations:

- [`list-namespaces`](https://docs.aws.amazon.com/cli/latest/reference/servicediscovery/list-namespaces.html)
- [`list-services`](https://docs.aws.amazon.com/cli/latest/reference/ecs/list-services.html)
- [`discover-instances`](https://docs.aws.amazon.com/cli/latest/reference/servicediscovery/discover-instances.html)

Using `list-namespaces` you can filter for the parameters `TYPE`, `NAME`, `HTTP_NAME`.
Using `list-services` it is only possible to filter for `NAMESPACE_ID`.
Both `list-services` and `list-namespaces` support `EQ` (default condition if not specified) and `BEGINS_WITH` as conditions.
Both conditions and only support a single value to match by.
The following examples demonstrate how to use filters with these operations:

{{< command >}}
$ awslocal servicediscovery list-namespaces \
    --filters "Name=HTTP_NAME,Values=['example-namespace'],Condition=EQ"
{{< /command >}}

{{< command >}}
$ awslocal servicediscovery list-services \
    --filters "Name=NAMESPACE_ID,Values=['id_to_match']"
{{< /command >}}

The command `discover-instance` supports parameters and optional parameters as filter criteria.
Conditions in parameters must match return values, while if one ore more conditions in optional parameters match, the subset is returned, if no conditions in optional parameters match, all unfiltered results are returned.

This command will only return instances where the parameter `env` is equal to `fuu`:
{{< command >}}
$ awslocal servicediscovery discover-instances \
    --namespace-name example-namespace \
    --service-name example-service \
    --query-parameters "env"="fuu"
{{< /command >}}

This command instead will return all instances where the optional parameter `env` is equal to `bar`, but if no instances match, all instances are returned:
{{< command >}}
$ awslocal servicediscovery discover-instances \
    --namespace-name example-namespace \
    --service-name example-service \
    --optional-parameters "env"="bar"
{{< /command >}}
