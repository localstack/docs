---
title: "Athena"
linkTitle: "Athena"
categories: ["LocalStack Pro"]
description: >
  Get started with AWS Athena on LocalStack
aliases:
  - /aws/athena/
---

LocalStack Pro ships with built-in support for [Athena](https://aws.amazon.com/athena), Amazon's serverless data warehouse and analytics platform.
Athena uses [Presto](https://prestodb.github.io)/[Trino](https://trino.io) under the covers, and your Athena instance will be automatically configured with a Hive metastore that connects seamlessly to the LocalStack S3 API.
That is, you can easily connect your local S3 buckets and query data directly from S3 via the powerful Athena query API.

## Basic Query Execution

The following commands illustrate how to use Athena from the command line (assuming you have [`awslocal`](https://github.com/localstack/awscli-local) installed):

{{< command >}}
$ awslocal athena start-query-execution --query-string 'SELECT 1, 2, 3'
{
    "QueryExecutionId": "c9f453ad"
}
$ awslocal athena list-query-executions
{
    "QueryExecutionIds": [
        "c9f453ad"
    ]
}
$ awslocal athena get-query-results --query-execution-id c9f453ad
{
    "ResultSet": {
        "Rows": [
            {
                "Data": [
                    { "VarCharValue": "_col0" },
                    { "VarCharValue": "_col1" },
                    { "VarCharValue": "_col2" }
                ]
            }, {
                "Data": [
                    { "VarCharValue": "1" },
                    { "VarCharValue": "2" },
                    { "VarCharValue": "3" }
                ]
            }
        ],
        "ResultSetMetadata": {
            "ColumnInfo": [
                {
                    "Name": "_col0", "Type": "integer"
                }, {
                    "Name": "_col1", "Type": "integer"
                }, {
                    "Name": "_col2", "Type": "integer"
                }
            ]
        }
    },
    "UpdateCount": 0
}
{{< / command >}}

{{< alert title="Note" >}}
In order to use the Athena API, some additional dependencies have to be fetched from the network (including Presto, Hive, and other tools). These dependencies are automatically fetched when you start up the service, so please make sure you're on a decent internet connection when using Athena for the first time.
{{< /alert >}}

## Delta Lake Tables

LocalStack Athena supports [Delta Lake](https://delta.io), an open-source storage framework that extends Parquet data files with a file-based transaction log for ACID transactions and scalable metadata handling.

To illustrate this feature, we take a sample published in the [AWS blog](https://aws.amazon.com/blogs/big-data/crawl-delta-lake-tables-using-aws-glue-crawlers).

The Delta Lake files used in this sample are available in a public S3 bucket under `s3://aws-bigdata-blog/artifacts/delta-lake-crawler/sample_delta_table`.
For your convenience, we have prepared the test files in a downloadable ZIP file [here](https://localstack-assets.s3.amazonaws.com/aws-sample-athena-delta-lake.zip).
We start by downloading and extracting this ZIP file:

{{< command >}}
$ mkdir /tmp/delta-lake-sample; cd /tmp/delta-lake-sample
$ wget https://localstack-assets.s3.amazonaws.com/aws-sample-athena-delta-lake.zip
$ unzip aws-sample-athena-delta-lake.zip; rm aws-sample-athena-delta-lake.zip
{{< / command >}}

We can then create an S3 bucket in LocalStack using the [`awslocal`](https://github.com/localstack/awscli-local) command line, and upload the files to the bucket:
{{< command >}}
$ awslocal s3 mb s3://test
$ awslocal s3 sync /tmp/delta-lake-sample s3://test
{{< / command >}}

Next, we create the table definitions in Athena:
{{< command >}}
$ awslocal athena start-query-execution \
    --query-string "CREATE EXTERNAL TABLE test (product_id string, product_name string, \
    price bigint, currency string, category string, updated_at double) \
    LOCATION 's3://test/' TBLPROPERTIES ('table_type'='DELTA')"
{{< / command >}}

Please note that this query may take some time to finish executing. You can observe the output in the LocalStack container (ideally with `DEBUG=1` enabled) to follow the steps of the query execution.

Finally, we can now run a `SELECT` query to extract data from the Delta Lake table we've just created:
{{< command >}}
$ queryId=$(awslocal athena start-query-execution --query-string "SELECT * from deltalake.default.test" | jq -r .QueryExecutionId)
$ awslocal athena get-query-results --query-execution-id $queryId
{{< / command >}}

The query should yield a result similar to the output below:
```
...
    "Rows": [
        {
            "Data": [
                { "VarCharValue": "product_id" },
                { "VarCharValue": "product_name" },
                { "VarCharValue": "price" },
                { "VarCharValue": "currency" },
                { "VarCharValue": "category" },
                { "VarCharValue": "updated_at" }
            ]
        },
        {
            "Data": [
                { "VarCharValue": "00005" },
                { "VarCharValue": "USB charger" },
                { "VarCharValue": "50" },
                { "VarCharValue": "INR" },
                { "VarCharValue": "Electronics" },
                { "VarCharValue": "1653462374.9975588" }
            ]
        },
        ...
...
```

{{< alert title="Note" >}}
The `SELECT` statement above currently requires us to prefix the database/table name with `deltalake.` - this will be further improved in a future iteration, for better parity with AWS.
{{< /alert >}}

## Iceberg Tables

The LocalStack Athena implementation also supports [Iceberg tables](https://docs.aws.amazon.com/athena/latest/ug/querying-iceberg-creating-tables.html) - more details and samples will be provided here soon.
