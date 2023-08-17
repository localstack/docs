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

Currently, it is possible to spin up PostgreSQL, MariaDB, MySQL, and MSSQL (SQL Server) databases on the local machine.

{{< alert title="Note" >}}
Some configuration of the RDS clusters and instances have currently only CRUD functionality. E.g., the `storage-encrypted` flag is returned as it is set, but there is no support for actual storage encryption yet. 
{{< /alert >}}

### Postgres Engine

When creating an RDS DB cluster or instance with `postgres`/`aurora-postgresql` DB engine and a specific `EngineVersion`, LocalStack will install and provision the respective Postgres version on demand.

Currently, major versions between 10 and 15 can be chosen - when selecting a major version outside of this range, the default version 11 is used as fallback.

Please be aware that the minor version cannot be freely selected - the latest available version will be installed in the docker environment.

In order to disable installation of custom versions, you may configure the environment variable `RDS_PG_CUSTOM_VERSIONS=0`, in which case always the default Postgres version 11 will be used.


{{< alert title="Note" >}}
The `describe-db-cluster` and `describe-db-instances` calls will still return the `engine-version` as it was defined for the creation, but the actual installed postgres engine could be different. This is important, e.g., when using a terraform configuration, as it should not detect changes in that case.
{{< /alert >}}

DB instances and DB cluster with Postgres engine support the creation and restoring of snapshots.

### MariaDB Engine

MariaDB will be installed as OS package in LocalStack. Currently, it is not possible to freely select a specific version. 

Snapshots are currently not supported for MariaDB.

### MySQL Engine

By default, a MariaDB installation is used when requesting a MySQL engine type. 

If you wish to use a real MySQL version, you can do so by setting the environment variable `RDS_MYSQL_DOCKER=1`. With this feature enabled, MySQL community server will be started in a new Docker container when requesting the MySQL engine. The `engine-version` will be used as the tag for the image, meaning you can freely select the desired MySQL version that is listed on the [official MySQL Docker Hub](https://hub.docker.com/_/mysql).

In case you want to use a special image, you can also set the environment variable `MYSQL_IMAGE=<my-image:tag>`.

{{< alert title="Note" >}}
Please be aware that MySQL images for `arm64` are only available for newer versions. Please check the [MySQL Docker Hub repository](https://hub.docker.com/_/mysql) for details on the availability.
{{< /alert >}}

Please note that the `MasterUserPassword` defined for the database cluster/instance will be used as the `MYSQL_ROOT_PASSWORD` environment for user `root` in the MySQL container. The user for `MasterUserName` will use the same password, and will have full access to the defined database.

DB Snapshots are currently not supported for MySQL.

### MSSQL Engine

{{< alert title="Note" >}}
In order to use MSSQL databases, you need to explicitly accept the [Microsoft SQL Server End-User Licensing Agreement (EULA)](https://hub.docker.com/_/microsoft-mssql-server) by setting `MSSQL_ACCEPT_EULA=Y` in the LocalStack container environment.

Please note that MSSQL does not yet have official support for `arm64`. 
{{< /alert >}}

For the MSSQL engine, the database server is started in a new docker container using the `latest` image.

DB Snapshots are currently not supported for MSSQL.

## End-to-end example (Postgres)

The local RDS service also supports the [RDS Data API](https://docs.aws.amazon.com/AmazonRDS/latest/AuroraUserGuide/data-api.html), which allows executing data queries against RDS clusters over a JSON/REST interface. 

Below is a simple example that illustrates (1) creation of an RDS cluster, (2) creation of a SecretsManager secret with the DB password, and (3) running a simple `SELECT 123` query via the RDS Data API.


{{< command >}}
$ awslocal rds create-db-cluster --db-cluster-identifier db1 --engine aurora-postgresql --database-name test --master-username myuser --master-user-password mypassword
{
    "DBCluster": {
        ...
        "Endpoint": "localhost:4510",
        "Port": 4510,  # may vary
        "DBClusterArn": "arn:aws:rds:us-east-1:000000000000:cluster:db1",
        ...
    }
}

$ cat << 'EOF' > mycreds.json
{
    "engine": "aurora-postgresql", 
    "username": "myuser",
    "password": "mypassword",
    "host": "localhost",
    "dbname": "test",
    "port": "4510"
}
EOF

$ awslocal secretsmanager create-secret \
    --name dbpass \
    --secret-string file://mycreds.json
{
    "ARN": "arn:aws:secretsmanager:us-east-1:000000000000:secret:dbpass-cfnAX",
    "Name": "dbpass",
    "VersionId": "fffa1f4a-2381-4a2b-a977-4869d59a16c0"
}

$ awslocal rds-data execute-statement --database test --resource-arn arn:aws:rds:us-east-1:000000000000:cluster:db1 --secret-arn arn:aws:secretsmanager:us-east-1:000000000000:secret:dbpass-cfnAX --include-result-metadata --sql 'SELECT 123'
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

## IAM Authentication Support

IAM auth token can be used to connect to RDS. This feature is currently only supported for Postgres in LocalStack.

{{< alert title="Note" >}}
Please be aware that the IAM authentication is not verified at this point, which means that any DB user that is granted the role `rds_iam` will receive a valid token and will be able to connect to the database.
{{< /alert >}}

### Using IAM example

The following example showcases the IAM authentication flow for RDS Postgres:

* create a DB instance, and retrieve the host and port for the instance
* connect to the DB using the master username and password. Then create a new user and grant it the role `rds_iam`:
   * `CREATE USER <username> WITH LOGIN`
   * `GRANT rds_iam TO <username>`
* generate a token for the `<username>` via the `generate-db-auth-token` command
* connect to the DB with the user you have a created and the token generated in the previous step as password

{{< command >}}
$ MASTER_USER=hello
$ MASTER_PW='MyPassw0rd!'
$ DB_NAME=test

$ awslocal rds create-db-instance --master-username $MASTER_USER --master-user-password $MASTER_PW --db-instance-identifier mydb --engine postgres --db-name $DB_NAME --enable-iam-database-authentication --db-instance-class db.t3.small

$ PORT=$(awslocal rds describe-db-instances --db-instance-identifier mydb | jq -r ".DBInstances[0].Endpoint.Port")
$ HOST=$(awslocal rds describe-db-instances --db-instance-identifier mydb | jq -r ".DBInstances[0].Endpoint.Address")

$ PGPASSWORD=$MASTER_PW psql -d $DB_NAME -U $MASTER_USER -p $PORT -h $HOST -w -c 'CREATE USER myiam WITH LOGIN'

$ PGPASSWORD=$MASTER_PW psql -d $DB_NAME -U $MASTER_USER -p $PORT -h $HOST -w -c 'GRANT rds_iam TO myiam'

$ TOKEN=$(awslocal rds generate-db-auth-token --username myiam --hostname $HOST --port $PORT)

$ PGPASSWORD=$TOKEN psql -d $DB_NAME -U myiam -w -p $PORT -h $HOST
{{< / command >}}

## Global Database Support

LocalStack supports [Aurora Global Database](https://docs.aws.amazon.com/AmazonRDS/latest/AuroraUserGuide/aurora-global-database.html), with some limitations:

* When creating a global database, there will only be one local database created. 
All clusters and instances that belong to the global database will point to the same endpoint. 

* Consequently, clusters that have been removed from a global database cannot be used as a standalone-cluster, like on AWS.

* Persistence for global databases is currently not supported.
