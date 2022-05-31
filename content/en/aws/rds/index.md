---
title: "Relational Database Service (RDS)"
linkTitle: "Relational Database Service (RDS)"
categories: ["LocalStack Pro"]
description: >
  Relational Database Service (RDS)
---

LocalStack supports a basic version of [RDS](https://aws.amazon.com/rds/) for testing. Currently, it is possible to spin up PostgreSQL, MySQL, and MSSQL (SQL Server) databases on the local machine.

{{< alert title="Note" >}}
In order to use MSSQL databases, you need to explicitly accept the [Microsoft SQL Server End-User Licensing Agreement (EULA)](https://hub.docker.com/_/microsoft-mssql-server) by setting `MSSQL_ACCEPT_EULA=Y` in the LocalStack container environment.
{{< /alert >}}

The local RDS service also supports the [RDS Data API](https://docs.aws.amazon.com/AmazonRDS/latest/AuroraUserGuide/data-api.html), which allows executing data queries over a JSON/REST interface. Below is a simple example that illustrates (1) creation of an RDS database, (2) creation of a SecretsManager secret with the DB password, and (3) running a simple `SELECT 123` query via the RDS Data API.
{{< command >}}
$ awslocal rds create-db-instance --db-instance-identifier db1 --db-instance-class c1 --engine postgres
{
    "DBInstance": {
        ...
        "Endpoint": {
            "Address": "localhost",
            "Port": 4513  # may vary
        }
        ...
    }
    ...
}

$ awslocal secretsmanager create-secret --name dbpass --secret-string test
{
    "ARN": "arn:aws:secretsmanager:eu-central-1:1234567890:secret:dbpass-cfnAX",
    "Name": "dbpass",
    "VersionId": "fffa1f4a-2381-4a2b-a977-4869d59a16c0"
}

$ awslocal rds-data execute-statement --database test --resource-arn arn:aws:rds:eu-central-1:000000000000:db:db1 --secret-arn arn:aws:secretsmanager:eu-central-1:1234567890:secret:dbpass-cfnAX --sql 'SELECT 123'
{
    "columnMetadata": [{
        "name": "?column?",
        "type": 23
    }],
    "records": [[
        { "doubleValue": 123 }
    ]]
}
{{< / command >}}

You can also use other clients like `psql` to interact with the database. The hostname and port of your created instance can be found in the output from above or by running `awslocal rds describe-db-instances`.

{{< command >}}
$ psql -d test -U test -p 4513 -h localhost -W
Password: <enter "test">
{{< / command >}}

{{< alert title="Notes" >}}
- The default for `master-username`, `master-user-password` and `db-name` is `"test"` - except for MSSQL DBs, where the default `master-user-password` is `"Test123!"`
- You can use any `master-username`, except `"postgres"`, for creating a new RDS instance. The user will automatically be created.
- The user `"postgres"` is special, and it is not possible to create a new RDS instance with this user name.
- Do not use `db-name` `"postgres"` as it is already in use by LocalStack.
{{< /alert >}}
