---
title: "Athena"
linkTitle: "Athena"
date: 2021-09-28
weight: 5
categories: ["LocalStack Pro"]
description: >
  Athena
---
LocalStack Pro ships with built-in support for [Athena](https://aws.amazon.com/athena), Amazon's serverless data warehouse and analytics platform. Athena uses [Presto](https://prestodb.github.io/) under the covers, and your Athena instance will be automatically configured with a Hive metastore that connects seamlessly to the LocalStack S3 API. That is, you can easily connect your local S3 buckets and query data directly from S3 via the powerful Athena query API.

The following commands illustrate how to use Athena from the command line (assuming you have [`awslocal`](https://github.com/localstack/awscli-local) installed):
```bash
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
        "Rows": [{
            "Data": [
                { "VarCharValue": "1" },
                { "VarCharValue": "2" },
                { "VarCharValue": "3" }
            ]
        }],
        "ResultSetMetadata": { "ColumnInfo": [] }
    },
    "UpdateCount": 0
}
```

{{< alert >}}**Note**:
In order to use the Athena API, some additional dependencies have to be fetched from the network, including a Docker image of apprx. 1.2GB which includes Presto, Hive and other tools. These dependencies are automatically fetched when you start up the service, so please make sure you're on a decent internet connection when pulling the dependencies for the first time.
{{< /alert >}}
