---
title: "Glue"
linkTitle: "Glue"
categories: ["LocalStack Pro"]
description: >
  Get started with Amazon Glue on LocalStack
aliases:
  - /aws/glue/
---

The Glue API in LocalStack Pro allows you to run ETL (Extract-Transform-Load) jobs locally, maintaining table metadata in the local Glue data catalog, and using the Spark ecosystem (PySpark/Scala) to run data processing workflows.

{{< alert >}}**Note**:
In order to run Glue jobs, some additional dependencies have to be fetched from the network, including a Docker image of apprx. 1.5GB which includes Spark, Presto, Hive and other tools. These dependencies are automatically fetched when you start up the service, so please make sure you're on a decent internet connection when pulling the dependencies for the first time.
{{< /alert >}}

## Creating Databases and Table Metadata

The commands below illustrate the creation of some very basic entries (databases, tables) in the Glue data catalog:
{{< command >}}
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
{{< / command >}}

## Running Scripts with Scala and PySpark

Assuming we would like to deploy a simple PySpark script `job.py` in the local folder, we can first copy the script to an S3 bucket:
{{< command >}}
$ awslocal s3 mb s3://glue-test
$ awslocal s3 cp job.py s3://glue-test/job.py
{{< / command >}}

Next, we can create a job definition:
{{< command >}}
$ awslocal glue create-job --name job1 --role r1 \
  --command '{"Name": "pythonshell", "ScriptLocation": "s3://glue-test/job.py"}'
{{< / command >}}
... and finally start the job:
{{< command >}}
$ awslocal glue start-job-run --job-name job1
{
    "JobRunId": "733b76d0"
}
{{< / command >}}
The returned `JobRunId` can be used to query the status job the job execution, until it becomes `SUCCEEDED`:
{{< command >}}
$ awslocal glue get-job-run --job-name job1 --run-id 733b76d0
{
    "JobRun": {
        "Id": "733b76d0",
        "Attempt": 1,
        "JobRunState": "SUCCEEDED"
    }
}
{{< / command >}}

For a more detailed example illustrating how to run a local Glue PySpark job, please refer to this [sample repository](https://github.com/localstack/localstack-pro-samples/tree/master/glue-etl-jobs).

## Importing Athena Tables into Glue Data Catalog

The Glue data catalog is integrated with Athena, and the database/table definitions can be imported via the `import-catalog-to-glue` API.

Assume you are running the following Athena queries to create databases and table definitions:
```sql
CREATE DATABASE db2
CREATE EXTERNAL TABLE db2.table1 (a1 Date, a2 STRING, a3 INT) LOCATION 's3://test/table1'
CREATE EXTERNAL TABLE db2.table2 (a1 Date, a2 STRING, a3 INT) LOCATION 's3://test/table2'
```

Then this command will import these DB/table definitions into the Glue data catalog:
{{< command >}}
$ awslocal glue import-catalog-to-glue
{{< / command >}}

... and finally they will be available in Glue:
{{< command >}}
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
{{< / command >}}

## Crawlers

Glue crawlers allow extracting metadata from structured data sources. 

LocalStack Glue currently supports S3 targets (configurable via `S3Targets`), as well as JDBC targets (configurable via `JdbcTargets`). Support for other target types is in our pipeline and will be added soon. 

### S3 Crawler Example

The example below illustrates crawling tables and partition metadata from S3 buckets.

First, we create an S3 bucket with a couple of items:
{{< command >}}
$ awslocal s3 mb s3://test
$ printf "1, 2, 3, 4\n5, 6, 7, 8" > /tmp/file.csv
$ awslocal s3 cp /tmp/file.csv s3://test/table1/year=2021/month=Jan/day=1/file.csv
$ awslocal s3 cp /tmp/file.csv s3://test/table1/year=2021/month=Jan/day=2/file.csv
$ awslocal s3 cp /tmp/file.csv s3://test/table1/year=2021/month=Feb/day=1/file.csv
$ awslocal s3 cp /tmp/file.csv s3://test/table1/year=2021/month=Feb/day=2/file.csv
{{< / command >}}

Then we can create and trigger the crawler:
{{< command >}}
$ awslocal glue create-database --database-input '{"Name":"db1"}'
$ awslocal glue create-crawler --name c1 --database-name db1 --role r1 --targets '{"S3Targets": [{"Path": "s3://test/table1"}]}'
$ awslocal glue start-crawler --name c1
{{< / command >}}

Finally, we can query the table and partitions metadata that has been created by the crawler:
{{< command >}}
$ awslocal glue get-tables --database-name db1
{
    "TableList": [{
        "Name": "table1",
        "DatabaseName": "db1",
        "PartitionKeys": [ ... ]
...
$ awslocal glue get-partitions --database-name db1 --table-name table1
{
    "Partitions": [{
        "Values": ["2021", "Jan", "1"],
        "DatabaseName": "db1",
        "TableName": "table1",
...
{{< / command >}}

### JDBC Crawler Example

When using JDBC crawlers, you can point your crawler towards a Redshift database created in LocalStack.

Below is a rough outline of the steps required to get the integration for the JDBC crawler working. We can first create the local Redshift cluster via:
{{< command >}}
$ awslocal redshift create-cluster --cluster-identifier c1 --node-type dc1.large --master-username test --master-user-password test --db-name db1
...
    "Endpoint": {
        "Address": "localhost.localstack.cloud",
        "Port": 4510
    },
...
{{< / command >}}

Then we can use any JDBC or Postgres client to create a table `mytable1` in the Redshift database, and fill the table with some data.

Next, we're creating the Glue database, the JDBC connection, as well as the crawler:
{{< command >}}
$ awslocal glue create-database --database-input '{"Name":"gluedb1"}'
$ awslocal glue create-connection --connection-input \
    {"Name":"conn1","ConnectionType":"JDBC","ConnectionProperties":{"USERNAME":"test","PASSWORD":"test","JDBC_CONNECTION_URL":"jdbc:redshift://localhost.localstack.cloud:4510/db1"}}'
$ awslocal glue create-crawler --name c1 --database-name gluedb1 --role r1 --targets '{"JdbcTargets":[{"ConnectionName":"conn1","Path":"db1/%/mytable1"}]}'
$ awslocal glue start-crawler --name c1
...
$ awslocal glue get-crawler --name c1
...
    "State": "RUNNING",
...
$ awslocal glue get-crawler --name c1
...
    "State": "READY",
...
{{< / command >}}

Once the crawler has finished running and is back in `READY` state, the Glue table within the `gluedb1` DB should have been populated and can be queried via the API.

## Schema Registry

The Glue Schema Registry allows you to centrally discover, control, and evolve data stream schemas.
With the Schema Registry, you can manage and enforce schemas and schema compatibilities in your streaming applications.
It integrates nicely with [Managed Streaming for Kafka (MSK)](../managed-streaming-for-kafka).

{{< alert >}}**Note**:
Currently, LocalStack supports the AVRO dataformat for the Glue Schema Registry. Support for other dataformats will be added in the future.
{{< /alert >}}

{{< command >}}
$ awslocal glue create-registry --registry-name demo-registry
{
    "RegistryArn": "arn:aws:glue:us-east-1:000000000000:file-registry/demo-registry",
    "RegistryName": "demo-registry"
}
$ awslocal glue create-schema --schema-name demo-schema --registry-id RegistryName=demo-registry --data-format AVRO --compatibility FORWARD \
  --schema-definition '{"type":"record","namespace":"Demo","name":"Person","fields":[{"name":"Name","type":"string"}]}'
{
    "RegistryName": "demo-registry",
    "RegistryArn": "arn:aws:glue:us-east-1:000000000000:file-registry/demo-registry",
    "SchemaName": "demo-schema",
    "SchemaArn": "arn:aws:glue:us-east-1:000000000000:schema/demo-registry/demo-schema",
    "DataFormat": "AVRO",
    "Compatibility": "FORWARD",
    "SchemaCheckpoint": 1,
    "LatestSchemaVersion": 1,
    "NextSchemaVersion": 2,
    "SchemaStatus": "AVAILABLE",
    "SchemaVersionId": "546d3220-6ab8-452c-bb28-0f1f075f90dd",
    "SchemaVersionStatus": "AVAILABLE"
}
$ awslocal glue register-schema-version --schema-id SchemaName=demo-schema,RegistryName=demo-registry \
  --schema-definition '{"type":"record","namespace":"Demo","name":"Person","fields":[{"name":"Name","type":"string"}, {"name":"Address","type":"string"}]}'
{
    "SchemaVersionId": "ee38732b-b299-430d-a88b-4c429d9e1208",
    "VersionNumber": 2,
    "Status": "AVAILABLE"
}
{{< / command >}}

You can find a more advanced sample in our [localstack-pro-samples repository on GitHub](https://github.com/localstack/localstack-pro-samples/tree/master/glue-msk-schema-registry), which showcases the integration with AWS MSK and automatic schema registrations (including schema rejections based on the compatibilities).


## Further Reading

The AWS Glue API is a fairly comprehensive service - more details can be found in the official [AWS Glue Developer Guide](https://docs.aws.amazon.com/glue/latest/dg/what-is-glue.html).

## Current Limitations

Support for triggers is currently limited - the basic API endpoints are implemented, but triggers are currently still under development (more details coming soon).
