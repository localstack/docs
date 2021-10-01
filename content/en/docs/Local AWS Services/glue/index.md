---
title: "Glue"
linkTitle: "Glue"
categories: ["LocalStack Pro"]
description: >
  Glue
---

The Glue API in LocalStack Pro allows you to run ETL (Extract-Transform-Load) jobs locally, maintaining table metadata in the local Glue data catalog, and using the Spark ecosystem (PySpark/Scala) to run data processing workflows.

{{< alert >}}**Note**:
In order to run Glue jobs, some additional dependencies have to be fetched from the network, including a Docker image of apprx. 1.5GB which includes Spark, Presto, Hive and other tools. These dependencies are automatically fetched when you start up the service, so please make sure you're on a decent internet connection when pulling the dependencies for the first time.
{{< /alert >}}

## Creating Databases and Table Metadata

The commands below illustrate the creation of some very basic entries (databases, tables) in the Glue data catalog:
```
$ awslocal glue create-database --database-input '{"Name":"db1"}'
$ awslocal glue create-table --database db1 --table-input '{"Name":"table1"}'
$ awslocal glue get-tables --database db1
{
    "TableList": [
        {
            "Name": "table1",
            "DatabaseName": "db1"
        }
    ]
}
```

## Running Scripts with Scala and PySpark

Assuming we would like to deploy a simple PySpark script `job.py` in the local folder, we can first copy the script to an S3 bucket:
```
$ awslocal s3 mb s3://glue-test
$ awslocal s3 cp job.py s3://glue-test/job.py
```

Next, we can create a job definition:
```
$ awslocal glue create-job --name job1 --role r1 \
  --command '{"Name": "pythonshell", "ScriptLocation": "s3://glue-test/job.py"}'
```
... and finally start the job:
```
$ awslocal glue start-job-run --job-name job1
{
    "JobRunId": "733b76d0"
}
```
The returned `JobRunId` can be used to query the status job the job execution, until it becomes `SUCCEEDED`:
```
$ awslocal glue get-job-run --job-name job1 --run-id 733b76d0
{
    "JobRun": {
        "Id": "733b76d0",
        "Attempt": 1,
        "JobRunState": "SUCCEEDED"
    }
}
```

For a more detailed example illustrating how to run a local Glue PySpark job, please refer to this [sample repository](https://github.com/localstack/localstack-pro-samples/tree/master/glue-etl-jobs).

## Importing Athena Tables into Glue Data Catalog

The Glue data catalog is integrated with Athena, and the database/table definitions can be imported via the `import-catalog-to-glue` API.

Assume you are running the following Athena queries to create databases and table definitions:
```
CREATE DATABASE db2
CREATE EXTERNAL TABLE db2.table1 (a1 Date, a2 STRING, a3 INT) LOCATION 's3://test/table1'
CREATE EXTERNAL TABLE db2.table2 (a1 Date, a2 STRING, a3 INT) LOCATION 's3://test/table2'
```

Then this command will import these DB/table definitions into the Glue data catalog:
```
$ awslocal glue import-catalog-to-glue
```

... and finally they will be available in Glue:
```
$ awslocal glue get-databases
{
    "DatabaseList": [
        ...
        {
            "Name": "db2",
            "Description": "Database db2 imported from Athena",
            "TargetDatabase": {
                "CatalogId": "000000000000",
                "DatabaseName": "db2"
            }
        }
    ]
}
$ awslocal glue get-tables --database-name db2
{
    "TableList": [
        {
            "Name": "table1",
            "DatabaseName": "db2",
            "Description": "Table db2.table1 imported from Athena",
            "CreateTime": ...
        },
        {
            "Name": "table2",
            "DatabaseName": "db2",
            "Description": "Table db2.table2 imported from Athena",
            "CreateTime": ...
        }
    ]
}
```

## Further Reading

The AWS Glue API is a fairly comprehensive service - more details can be found in the official [AWS Glue Developer Guide](https://docs.aws.amazon.com/glue/latest/dg/what-is-glue.html).

## Current Limitations

Support for crawlers and triggers is currently limited - the basic API endpoints are implemented, but starting a crawler process is currently still under development (more details coming soon).
