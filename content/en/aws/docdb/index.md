---
title: "Document DB (DocDB)"
linkTitle: "Document DB (DocDB)"
categories: ["LocalStack Pro"]
description: >
  Document DB (DocDB)
---

LocalStack supports a basic version of [Amazon DocumentDB](https://aws.amazon.com/documentdb/) for testing.

When loading the DocumentDB service, LocalStack will create a MongoDB container to handle DocumentDB interactions. If not specified explicitly, this instance will listen on a port in the 33000-34000 port range and will instantiate a master user named 'test' without a password. The `mongosh` client may be used to log in to and interact with the instance.

{{< alert title="Note" >}}
Because LocalStack utilizes a MongoDB container to provide a DocumentDB simulation, the database engine may support additional features that Amazon DocumentDB does not.
{{< /alert >}}

## Example

{{< command >}}
$ awslocal docdb create-db-cluster --db-cluster-identifier 'test-docdb-cluster' --engine 'docdb'
{
    "DBCluster": {
        "DBClusterIdentifier": "test-docdb-cluster",
        "DBClusterParameterGroup": "default.docdb",
        "Status": "creating",
        "Endpoint": "localhost:33101",
        "MultiAZ": false,
        "Engine": "docdb",
        "Port": 33101,
        "MasterUsername": "test",
        "StorageEncrypted": false,
        "DBClusterArn": "arn:aws:rds:us-east-1:000000000000:cluster:test-docdb-cluster"
    }
}


$ awslocal docdb create-db-instance --db-instance-identifier 'test-docdb-instance' --db-instance-class 'db.r5.large' --engine 'docdb' --db-cluster-identifier 'test-docdb-cluster'
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

{{< / command >}}

Using the `describe-db-clusters` command, it's possible to create a connection string to use with `mongosh` to connect to the LocalStack DocumentDB cluster.

{{< command >}}
$ awslocal docdb describe-db-clusters --db-cluster-identifier 'test-docdb-cluster'
{
    "DBClusters": [
        {
            "DBClusterIdentifier": "test-docdb-cluster",
            "DBClusterParameterGroup": "default.docdb",
            "Status": "error",
            "Endpoint": "localhost:33101",
            "MultiAZ": false,
            "Engine": "docdb",
            "Port": 33101,
            "MasterUsername": "test",
            "StorageEncrypted": false,
            "DBClusterArn": "arn:aws:rds:us-east-1:000000000000:cluster:test-docdb-cluster"
        }
    ]
}


$ mongosh 'mongodb://127.0.0.1:33101'
Current Mongosh Log ID:	635b5bef8281e9775b1deb95
Connecting to:		mongodb://127.0.0.1:33101/?directConnection=true&serverSelectionTimeoutMS=2000&appName=mongosh+1.6.0
Using MongoDB:		6.0.2
Using Mongosh:		1.6.0

For mongosh info see: https://docs.mongodb.com/mongodb-shell/

...

{{< / command >}}
