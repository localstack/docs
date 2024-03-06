---
title: "Managed Workflows for Apache Airflow (MWAA)"
linkTitle: "Managed Workflows for Apache Airflow (MWAA)"
description: >
    Get started with Managed Workflows for Apache Airflow (MWAA) on LocalStack
tags: ["Pro image"]
---

## Introduction

Managed Workflows for Apache Airflow (MWAA) is a fully managed service by AWS that simplifies the deployment, management, and scaling of Apache Airflow workflows in the cloud.
MWAA leverages the familiar Airflow features and integrations while integrating with S3, Glue, Redshift, Lambda, and other AWS services to build data pipelines and orchestrate data processing workflows in the cloud.

LocalStack allows you to use the MWAA APIs in your local environment to allow the setup and operation of data pipelines.
The supported APIs are available on our [API coverage page](https://docs.localstack.cloud/references/coverage/coverage_mwaa/), which provides information on the extent of MWAA's integration with LocalStack.

## Getting started

This guide is designed for users new to Managed Workflows for Apache Airflow and assumes basic knowledge of the AWS CLI and our [`awslocal`](https://github.com/localstack/awscli-local) wrapper script.

Start your LocalStack container using your preferred method.
We will demonstrate how to create an Airflow environment and access the Airflow UI.

### Create a S3 bucket

Create a S3 bucket that will be used for Airflow resources.
Run the following command to create a bucket using the [`mb`](https://docs.aws.amazon.com/cli/latest/reference/s3/mb.html) command.


{{< command >}}
$ awslocal s3 mb s3://my-mwaa-bucket
{{< /command >}}

### Create an Airflow environment

You can now create an Airflow environment, using the [`CreateEnvironment`](https://docs.aws.amazon.com/mwaa/latest/API/API_CreateEnvironment.html) API.
Run the following command, by specifying the bucket ARN we created earlier:

{{< command >}}
$ awslocal mwaa create-environment --dag-s3-path /dags \
        --execution-role-arn arn:aws:iam::000000000000:role/airflow-role \
        --network-configuration {} \
        --source-bucket-arn arn:aws:s3:::my-mwaa-bucket \
        --airflow-version 2.2.2 \
        --airflow-configuration-options agent.code=007,agent.name=bond \
        --name my-mwaa-env
{{< /command >}}

### Access the Airflow UI

LocalStack will create the Airflow environment and print the Airflow UI URL and access credentials in the logs:

```bash
2022-11-30T17:58:36.533 DEBUG --- [functhread13] l.services.mwaa.provider   : Airflow available at http://localhost.localstack.cloud:4510 with username=localstack and password=localstack
```

## Airflow versions

LocalStack supports the following versions of Apache Airflow:

- `1.10.12` (deprecated)
- `2.0.2` (deprecated)
- `2.2.2` (deprecated)
- `2.4.3`
- `2.5.1`
- `2.6.3`
- `2.7.2` (default)

## Airflow configuration options

To configure Airflow environments effectively, you can utilize the `AirflowConfigurationOptions` argument.
These options are transformed into corresponding environment variables and passed to Airflow.
For instance:

-   `agent.code`:`007` is transformed into `AIRFLOW__AGENT__CODE:007`.
-   `agent.name`:`bond` is transformed into `AIRFLOW__AGENT__NAME:bond`.

This transformation process ensures that your configuration settings are easily applied within the Airflow environment.

## Adding or updating DAGs

When it comes to adding or updating DAGs in Airflow, the process is simple and efficient.
Just upload your DAGs to the designated S3 bucket path, configured by the `DagS3Path` argument.

Follow this example command to upload a sample DAG named `sample_dag.py` to your S3 bucket named `my-mwaa-bucket`:

{{< command >}} 
$ awslocal s3 cp sample_dag.py s3://my-mwaa-bucket/dags 
{{< /command >}}

## Installing custom plugins

You can extend the capabilities of Airflow by incorporating custom plugins, which introduce new operators, interfaces, or hooks.
LocalStack seamlessly supports plugins packaged according to [AWS specifications](https://docs.aws.amazon.com/mwaa/latest/userguide/configuring-dag-import-plugins.html#configuring-dag-plugins-test-create).

To integrate your custom plugins into the MWAA environment, upload the packaged `plugins.zip` file to the designated S3 bucket path:

{{< command >}}
$ awslocal s3 cp plugins.zip s3://my-mwaa-bucket/plugins.zip
{{< /command >}}

## Installing Python dependencies

LocalStack streamlines the process of installing Python dependencies for Apache Airflow within your environments.
To get started, create a `requirements.txt` file that lists the required dependencies.
For example:

```txt
boto3==1.17.54
boto==2.49.0
botocore==1.20.54
```

Once you have your `requirements.txt` file ready, upload it to the designated S3 bucket, configured for use by the MWAA environment.
Make sure to upload the file to `/requirements.txt` in the bucket:

{{< command >}}
$ awslocal s3 cp requirements.txt s3://my-mwaa-bucket/requirements.txt
{{< /command >}}

After the upload, the environment will be automatically updated, and your Apache Airflow setup will be equipped with the new dependencies.
It is important to note that, unlike [AWS](https://docs.aws.amazon.com/mwaa/latest/userguide/connections-packages.html), LocalStack does not install any provider packages by default.
Therefore, you must follow the above steps to install any required provider packages.

## Connections

When incorporating connections to other AWS services within your DAGs, it is crucial to specify either the internal Docker IP address of the LocalStack container or utilize `host.docker.internal`.
LocalStack currently does not use the credentials and region from `aws_conn_id`.
This information must be explicitly passed in operators, hooks, and sensors.
