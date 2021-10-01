---
title: "Elastic MapReduce (EMR)"
linkTitle: "Elastic MapReduce (EMR)"
categories: ["LocalStack Pro"]
description: >
  Elastic MapReduce (EMR)
---

LocalStack Pro allows running data analytics workloads locally via the [EMR](https://aws.amazon.com/emr) API. EMR utilizes various tools in the [Hadoop](https://hadoop.apache.org/) and [Spark](https://spark.apache.org) ecosystem, and your EMR instance is automatically configured to connect seamlessly to the LocalStack S3 API.

To create a virtual EMR cluster locally from the command line (assuming you have [`awslocal`](https://github.com/localstack/awscli-local) installed):
```
$ awslocal emr create-cluster --release-label emr-5.9.0 --instance-groups InstanceGroupType=MASTER,InstanceCount=1,InstanceType=m4.large InstanceGroupType=CORE,InstanceCount=1,InstanceType=m4.large
{
    "ClusterId": "j-A2KF3EKLAOWRI"
}
```

The commmand above will spin up one more more Docker containers on your local machine that can be used to run analytics workloads using Spark, Hadoop, Pig, and other tools.

Note that you can also specify startup commands using the `--steps=...` command line argument to the `create-cluster` command. A simple demo project with more details can be found in [this Github repository](https://github.com/localstack/localstack-pro-samples/tree/master/emr-hadoop-spark-jobs).

{{< alert >}}**Note**:
In order to use the EMR API, some additional dependencies have to be fetched from the network, including a Docker image of apprx. 1.5GB which includes Presto, Hive and other tools. These dependencies are automatically fetched when you start up the service, so please make sure you're on a decent internet connection when pulling the dependencies for the first time.
{{< /alert >}}
