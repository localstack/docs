---
title: "Elastic MapReduce (EMR)"
linkTitle: "Elastic MapReduce (EMR)"
categories: ["LocalStack Pro"]
description: >
  Get started with Elastic MapReduce (EMR) on LocalStack
aliases:
  - /aws/elastic-mapreduce/
---

## Introduction

Amazon EMR (Elastic MapReduce) is a fully managed big data processing service that allows developers to effortlessly create, deploy, and manage big data applications. EMR supports various big data processing frameworks, including Hadoop MapReduce, Apache Spark, Apache Hive, and Apache Pig. Developers can leverage these frameworks and their rich ecosystem of tools and libraries to perform complex data transformations, machine learning tasks, and real-time data processing.

LocalStack Pro supports EMR and allows developers to run data analytics workloads locally. EMR utilizes various tools in the [Hadoop](https://hadoop.apache.org/) and [Spark](https://spark.apache.org) ecosystem, and your EMR instance is automatically configured to connect seamlessly to LocalStack's S3 API. LocalStack also supports EMR Serverless to create applications and job runs, to run your Spark/PySpark jobs locally.

The supported APIs are available on our [API coverage page](https://docs.localstack.cloud/references/coverage/coverage_emr/), which provides information on the extent of EMR's integration with LocalStack.

{{< alert title="Note">}}
To utilize the EMR API, certain additional dependencies need to be downloaded from the network. This includes a Docker image of approximately 1.5 GB, which incorporates essential tools like Presto, Hive, and others. These dependencies are fetched automatically during service startup. Therefore, it's important to ensure a reliable internet connection when retrieving the dependencies for the first time.
{{< /alert >}}

## Getting started

This guide is designed for users new to emr and assumes basic knowledge of the AWS CLI and our [`awslocal`](https://github.com/localstack/awscli-local) wrapper script.

Start your LocalStack container using your preferred method. We will create a virtual EMR cluster using the AWS CLI. To create an EMR cluster, run the following command:

{{< command >}}
$ awslocal emr create-cluster \
          --release-label emr-5.9.0 \
          --instance-groups InstanceGroupType=MASTER,InstanceCount=1,InstanceType=m4.large InstanceGroupType=CORE,InstanceCount=1,InstanceType=m4.large
{{< / command >}}

The command above will spin up one more more Docker containers on your local machine that can be used to run analytics workloads using Spark, Hadoop, Pig, and other tools.

You will see a response similar to the following:

```sh
{
    "ClusterId": "j-A2KF3EKLAOWRI"
}
```

You can also specify startup commands using the `--steps=...` command line argument to the `CreateCluster` API.

## Examples

The following code snippets and sample applications provide practical examples of how to use EMR in LocalStack for various use cases:

- [Running data analytics jobs using EMR](https://github.com/localstack/localstack-pro-samples/tree/master/sample-archive/emr-hadoop-spark-jobs)
- [Running EMR Serverless Jobs with Java](https://github.com/localstack/localstack-pro-samples/tree/master/emr-serverless-sample)
