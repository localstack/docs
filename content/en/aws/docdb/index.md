---
title: "DocumentDB (DocDB)"
linkTitle: "DocumentDB (DocDB)"
categories: ["LocalStack Pro"]
description: >
DocumentDB (DocDB)
---

LocalStack supports a basic version of [Amazon DocumentDB](https://aws.amazon.com/documentdb/) for
testing.

When loading the DocumentDB service, LocalStack will create a MongoDB container to handle DocumentDB
storage.
By default, a master user named 'test' will be instantiated without a password.
LocalStack starts a MongoDB server in a separate Docker container and adds port-mapping so that it
can be accessed from the host machine.
To find such a free port, LocalStack will select an available port on the machine, that means there
is no pre-defined port range.

The database currently uses the default configuration of the
latest [MongoDB Docker image](https://hub.docker.com/_/mongo). It automatically creates a database
named `test` if nothing else is defined.
The `mongosh` client may be used to log in to and interact with the instance.

{{< alert title="Note" >}}
Because LocalStack utilizes a MongoDB container to provide DocumentDB storage, LocalStack may not
have feature parity with Amazon DocumentDB. The database engine may support additional features that
Amazon DocumentDB does not and vice versa.
{{< /alert >}}

## Getting started

To create a new DocumentDB cluster we use the `create-db-cluster` command as follows:

{{< command >}}
$ awslocal docdb create-db-cluster --db-cluster-identifier test-docdb-cluster --engine docdb

{
"DBCluster": {
"DBClusterIdentifier": "test-docdb-cluster",
"DBClusterParameterGroup": "default.docdb",
"Status": "available",
"Endpoint": "localhost:39045",
"MultiAZ": false,
"Engine": "docdb",
"Port": 39045,
"MasterUsername": "test",
"DBClusterMembers": [],
"VpcSecurityGroups": [
{
"VpcSecurityGroupId": "sg-a30edea1f7da6ff90",
"Status": "active"
}
],
"StorageEncrypted": false,
"DBClusterArn": "arn:aws:rds:us-east-1:000000000000:cluster:test-docdb-cluster"
}
}
{{< /command >}}

If we break down the previous command, we can identify:

- `docdb`: The command related to Amazon DocumentDB, the managed document database service provided
  by AWS.
- `create-db-cluster`: The AWS CLI command to create an Amazon DocumentDB cluster.
- `--db-cluster-identifier test-docdb-cluster`: Specifies the unique identifier for the DocumentDB
  cluster. In this case, it is set to `test-docdb-cluster`. You can customize this identifier to a
  name of your choice.
- `--engine docdb`: Specifies the database engine. Here, it is set to `docdb`, indicating the use of
  Amazon DocumentDB.

Notice in the `DBClusterMembers` field of the cluster description that there are no other databases
created.
To create a new database, we can use the `create-db-instance` command, like in this example:

{{< command >}}
$ awslocal docdb create-db-instance --db-instance-identifier test-company
--db-instance-class db.r5.large --engine docdb --db-cluster-identifier test-docdb-cluster
{
"DBInstance": {
"DBInstanceIdentifier": "test-docdb-instance",
"DBInstanceClass": "db.r5.large",
"Engine": "docdb",
"DBInstanceStatus": "creating",
"Endpoint": {
"Address": "localhost",
"Port": 50761
},
"InstanceCreateTime": "2022-10-28T04:27:35.917000+00:00",
"PreferredBackupWindow": "03:50-04:20",
"BackupRetentionPeriod": 1,
"VpcSecurityGroups": [],
"AvailabilityZone": "us-east-1a",
"PreferredMaintenanceWindow": "wed:06:38-wed:07:08",
"EngineVersion": "12.34",
"AutoMinorVersionUpgrade": false,
"PubliclyAccessible": false,
"StatusInfos": [],
"DBClusterIdentifier": "test-docdb-cluster",
"StorageEncrypted": false,
"DbiResourceId": "db-M5ENSHXFPU6XHZ4G4ZEI5QIO2U",
"CopyTagsToSnapshot": false,
"DBInstanceArn": "arn:aws:rds:us-east-1:000000000000:db:test-docdb-instance",
"EnabledCloudwatchLogsExports": []
}
}
{{< /command >}}

Some noticeable fields: 

- `--db-instance-identifier test-company`: Represents the unique identifier of the newly created database
- `--db-instance-class db.r5.large`: Is the instance type or class for the Amazon DocumentDB instance. It determines the compute 
and memory capacity allocated to the instance. `db.r5.large` refers to a specific instance type in the R5 family.
The R5 instance family is optimized for memory-intensive workloads and offers a good balance of compute and memory resources.
You can find out more about instance classes in the [AWS documentation](https://docs.aws.amazon.com/AmazonRDS/latest/UserGuide/Concepts.DBInstanceClass.html).

To obtain detailed information about the cluster, we use the `describe-db-cluster` command:
{{< command >}}
$ awslocal docdb describe-db-clusters --db-cluster-identifier test-docdb-cluster
{
"DBClusters": [
{
"DBClusterIdentifier": "test-docdb-cluster",
"DBClusterParameterGroup": "default.docdb",
"Status": "available",
"Endpoint": "localhost:39045",
"MultiAZ": false,
"Engine": "docdb",
"Port": 39045,
"MasterUsername": "test",
"DBClusterMembers": [
{
"DBInstanceIdentifier": "test-company",
"IsClusterWriter": true,
"DBClusterParameterGroupStatus": "in-sync",
"PromotionTier": 1
}
],
"VpcSecurityGroups": [
{
"VpcSecurityGroupId": "sg-a30edea1f7da6ff90",
"Status": "active"
}
],
"StorageEncrypted": false,
"DBClusterArn": "arn:aws:rds:us-east-1:000000000000:cluster:test-docdb-cluster"
}
]
}
{{< /command >}}

Interacting with the databases is done using `mongosh`, which is an official command-line shell and interactive MongoDB shell provided by MongoDB.
It is designed to provide a modern and enhanced user experience for interacting with MongoDB databases.

{{< command >}}

$ mongosh mongodb://localhost:39045
Current Mongosh Log ID:	64a70b795697bcd4865e1b9a
Connecting to:		mongodb://localhost:39045/?directConnection=true&serverSelectionTimeoutMS=2000&appName=mongosh+1.10.1
Using MongoDB:		6.0.7
Using Mongosh:		1.10.1

For mongosh info see: https://docs.mongodb.com/mongodb-shell/

------

test>

{{< /command >}}

This command will default to accessing the `test` database that was created with the cluster.
To work with a specific database, the command is:

{{< command >}}
$ mongosh mongodb://localhost:39045/company
Current Mongosh Log ID:	64a70bb163a42b40c3498816
Connecting to:		mongodb://localhost:39045/company?directConnection=true&serverSelectionTimeoutMS=2000&appName=mongosh+1.10.1
Using MongoDB:		6.0.7
Using Mongosh:		1.10.1

For mongosh info see: https://docs.mongodb.com/mongodb-shell/

------

company>

{{< /command >}}

From here on we can manipulate collections using [the JavaScript methods provided](https://www.mongodb.com/docs/manual/reference/method/) by `mongosh`:

{{< command >}}

company> db.createCollection("employees")
{ ok: 1 }
company> db.createCollection("customers")
{ ok: 1 }
company> show collections
customers
employees
company> exit

{{< /command >}}

For more information on how to use MongoDB with `mongosh` please refer to the [MongoDB documentation](https://www.mongodb.com/docs/).

