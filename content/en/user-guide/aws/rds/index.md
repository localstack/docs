---
title: "Relational Database Service (RDS)"
linkTitle: "Relational Database Service (RDS)"
categories: ["LocalStack Pro"]
description: >
  Get started with Relational Database Service (RDS) on LocalStack
aliases:
  - /aws/rds/
---

LocalStack supports a basic version of the [Relational Database Service (RDS)](https://aws.amazon.com/rds/) for testing.

## Supported DB engines

Currently, it is possible to spin up PostgreSQL, MySQL, and MSSQL (SQL Server) databases on the local machine.

{{< alert title="Note" >}}
In order to use MSSQL databases, you need to explicitly accept the [Microsoft SQL Server End-User Licensing Agreement (EULA)](https://hub.docker.com/_/microsoft-mssql-server) by setting `MSSQL_ACCEPT_EULA=Y` in the LocalStack container environment.
{{< /alert >}}

### Postgres versions

When creating an RDS DB cluster or instance with `postgres`/`aurora-postgresql` DB engine and a specific `EngineVersion`, LocalStack will install and provision the respective Postgres version on demand.

Currently, versions 11, 12, and 13 can be chosen - when selecting a major version outside of this range, the default version 11 is used as fallback.

Please be aware that the minor version cannot be freely selected - the latest available version will be installed in the docker environment.

In order to disable installation of custom versions, you may configure the environment variable `RDS_PG_CUSTOM_VERSIONS=0`, in which case always the default Postgres version 11 will be used.


{{< alert title="Note" >}}
The `describe-db-cluster` and `describe-db-instances` calls will still return the `engine-version` as it was defined for the creation, but the actual installed postgres engine could be different. This is important, e.g., when using a terraform configuration, as it should not detect changes in that case.
{{< /alert >}}

## End-to-end example (Postgres)

The local RDS service also supports the [RDS Data API](https://docs.aws.amazon.com/AmazonRDS/latest/AuroraUserGuide/data-api.html), which allows executing data queries against RDS clusters over a JSON/REST interface. Below is a simple example that illustrates (1) creation of an RDS cluster, (2) creation of a SecretsManager secret with the DB password, and (3) running a simple `SELECT 123` query via the RDS Data API.
{{< command >}}
$ awslocal rds create-db-cluster --db-cluster-identifier db1 --engine aurora-postgresql --database-name test
{
    "DBCluster": {
        ...
        "Endpoint": "localhost:4510",
        "Port": 4510,  # may vary
        "DBClusterArn": "arn:aws:rds:us-east-1:000000000000:cluster:db1",
        ...
    }
}


$ awslocal secretsmanager create-secret --name dbpass --secret-string test
{
    "ARN": "arn:aws:secretsmanager:eu-central-1:1234567890:secret:dbpass-cfnAX",
    "Name": "dbpass",
    "VersionId": "fffa1f4a-2381-4a2b-a977-4869d59a16c0"
}

$ awslocal rds-data execute-statement --database test --resource-arn arn:aws:rds:us-east-1:000000000000:cluster:db1 --secret-arn arn:aws:secretsmanager:eu-central-1:1234567890:secret:dbpass-cfnAX --include-result-metadata --sql 'SELECT 123'
{
    "columnMetadata": [
        {
            "arrayBaseColumnType": 0,
            "isAutoIncrement": false,
            "isCaseSensitive": false,
            "isCurrency": false,
            "isSigned": true,
            "label": "?column?",
            "name": "?column?",
            "nullable": 0,
            "precision": 10,
            "scale": 0,
            "schemaName": "",
            "tableName": "",
            "type": 4,
            "typeName": "int4"
        }
    ],
    "numberOfRecordsUpdated": 0,
    "records": [
        [
            {
                "longValue": 123
            }
        ]
    ]
}

{{< / command >}}

You can also use other clients like `psql` to interact with the database. The hostname and port of your created instance can be found in the output from above or by running `awslocal rds describe-db-instances`.

{{< command >}}
$ psql -d test -U test -p 4513 -h localhost -W
Password: <enter "test">
{{< / command >}}

## Default usernames and passwords

Please consider the following notes regarding default usernames/passwords and database names:
- The default for `master-username` and `db-name` is "test". The default `master-user-password` is "test" - except for MSSQL DBs, which uses "Test123!" as the default master password.
- You can use any `master-username`, except "postgres", for creating a new RDS instance. The user will automatically be created.
- The user "postgres" is special, and it is not possible to create a new RDS instance with this user name.
- Do not use `db-name` "postgres" as it is already in use by LocalStack.
