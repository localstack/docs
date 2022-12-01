---
title: "Managed Workflows for Apache Airflow (MWAA)"
categories: ["LocalStack Pro"]
description: Amazon Managed Workflows for Apache Airflow
---

LocalStack supports Managed Workflows for Apache Airflow, which allow setup and operation of data pipelines.

## Creating and accessing environments

First create an S3 bucket which will be used for all the MWAA resources.

```
$ awslocal s3 mb s3://my-mwaa-bucket
```

Next create the environment with the bucket ARN as follows:

```
$ awslocal mwaa create-environment --dag-s3-path /dags \
        --execution-role-arn r1 \
        --network-configuration {} \
        --source-bucket-arn arn:aws:s3:::my-mwaa-bucket \
        --airflow-version 2.2.2 \
        --airflow-configuration-options agent.code=007,agent.name=bond \
        --name my-mwaa-env
```

LocalStack will create the environment and print the Airflow UI URL and access credentials in the logs:

```
2022-11-30T17:58:36.533 DEBUG --- [functhread13] l.services.mwaa.provider   : Airflow available at http://localhost.localstack.cloud:4510 with username=localstack and password=localstack
```

Like production AWS, LocalStack supports all three versions of Apache Airflow: `1.10.12,` `2.0.2` and `2.2.2`.
By default, `2.2.2` is used.

## Airflow configuration options

Configuration options can be passed to Airflow environments using the `AirflowConfigurationOptions` argument.

Options are transformed as follows and then passed to Airflow as environment variables.

- `agent.code`:`007` → `AIRFLOW__AGENT__CODE:007`
- `agent.name`:`bond` → `AIRFLOW__AGENT__NAME:bond`

## Adding or updating DAGs

To add DAGs to Airflow, upload them to the S3 bucket at the path configured by the `DagS3Path` argument.

```
$ awslocal s3 cp sample_dag.py s3://my-mwaa-bucket/dags
```

## Installing custom plugins

You can install custom plugins to leverage Airflow operators, interfaces or hooks.

LocalStack supports plugins packaged as per AWS specifications as described [here](https://docs.aws.amazon.com/mwaa/latest/userguide/configuring-dag-import-plugins.html#configuring-dag-plugins-test-create).

The plugins should be uploaded to S3 bucket configured for the MWAA environment at the `/plugins.zip` path, like so:

```
$ awslocal s3 cp plugins.zip s3://my-mwaa-bucket/plugins.zip
```

## Installing Python dependencies

LocalStack makes it possible to install Python dependencies for Apache Airflow in your environments.

First, create a `requirements.txt` file:

```
boto3==1.17.54
boto==2.49.0
botocore==1.20.54
```

Next, upload the file to the S3 bucket configured for use by the MWAA environment.
The file must be uploaded to `/requirements.txt`:

```
$ awslocal s3 cp requirements.txt s3://my-mwaa-bucket/requirements.txt
```

The environment will be updated and will be ready for use with new dependencies.
