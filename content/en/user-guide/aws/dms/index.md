---
title: "Database Migration Service (DMS)"
linkTitle: "Database Migration Service (DMS)"
description: Get started with Database Migration Service (DMS) on LocalStack
tags: ["Enterprise plan"]
---

## Introduction

AWS Database Migration Service provides migration solution from databases, data warehouses, and other type of data stores (e.g. S3, SAP). 
The migration can be homogeneous (source and target have the same type), but often times is heterogeneous as it supports migration from various sources to various targets (self-hosted and AWS services).

LocalStack only supports selected use cases for DMS at the moment. 
The supported APIs are available on our [API coverage page](https://docs.localstack.cloud/references/coverage/coverage_dms/), which provides information on the extent of DMS integration with LocalStack.

{{< callout "note">}}
DMS is in a preview state, supporting only [selected use cases](#supported-use-cases). 
It is only available as part of the **LocalStack Enterprise** plan, and you need to set the env `ENABLE_DMS=1` in order to activate it. 
If you'd like to try it out, please [contact us](https://www.localstack.cloud/demo) to request access.
{{< /callout >}}

## Getting started

You can run a DMS sample showcasing MariaDB source and Kinesis target from our [GitHub repository](https://github.com/localstack-samples/sample-dms-kinesis-rds-mariadb/).

* The sample is using CDK to setup the infrastructure.
* It setups two databases: one external MariaDB (starting in a docker container) and one RDS MariaDB.
* It creates two `cdc` replication tasks, with different table mappings, that will run against the RDS database,
* and two `full-load` replication tasks with different table mappings, running against the hosted (containerized) MariaDB.

To follow the sample, simply clone the repository:

```sh
git clone https://github.com/localstack-samples/sample-dms-kinesis-rds-mariadb.git
```

Next, start LocalStack (there is a docker-compose included, setting the `ENABLE_DMS=1` flag):

```sh
export LOCALSTACK_AUTH_TOKEN=<your-auth-token> # this must be a enterprise license token
docker-compose up
```

Now you can install the dependencies, deploy the resources, and run the tests:

```sh
# install dependencies
make install
# deploys cdk stack with all required resources (replication instances, tasks, endpoints)
make deploy
# starts the tasks
make run
```

You will then see some log output, indicating the status of the ongoing replication:

```sh
************
STARTING FULL LOAD FLOW
************
db endpoint: localhost:3306

	Cleaning tables
	Creating tables
	Inserting data

	Added the following authors
[{'first_name': 'John', 'last_name': 'Doe'}]

	Added the following accounts
[{'account_balance': Decimal('1500.00'), 'name': 'Alice'}]

	Added the following novels
[{'author_id': 1, 'title': 'The Great Adventure'},
 {'author_id': 1, 'title': 'Journey to the Stars'}]

****Full Task 1****


	Starting Full load task 1 a%
Replication Task arn:aws:dms:us-east-1:000000000000:task:FQWFF7YIZ4VGQHBIXCLI9FJTUUS17NSECIM0UR7 status: starting
Waiting for task status stopped
task='arn:aws:dms:us-east-1:000000000000:task:FQWFF7YIZ4VGQHBIXCLI9FJTUUS17NSECIM0UR7' status='starting'
task='arn:aws:dms:us-east-1:000000000000:task:FQWFF7YIZ4VGQHBIXCLI9FJTUUS17NSECIM0UR7' status='stopped'

	Kinesis events

fetching Kinesis event
Received: 6 events
[{'control': {},
  'metadata': {'operation': 'drop-table',
               'partition-key-type': 'task-id',
               'partition-key-value': 'FQWFF7YIZ4VGQHBIXCLI9FJTUUS17NSECIM0UR7',
               'record-type': 'control',
               'schema-name': 'dms_sample',
               'table-name': 'accounts',
               'timestamp': '2024-05-23T19:17:33.126Z'},
  'partition_key': 'FQWFF7YIZ4VGQHBIXCLI9FJTUUS17NSECIM0UR7.dms_sample.accounts'},
 {'control': {},
  'metadata': {'operation': 'drop-table',
               'partition-key-type': 'task-id',
               'partition-key-value': 'FQWFF7YIZ4VGQHBIXCLI9FJTUUS17NSECIM0UR7',
               'record-type': 'control',
               'schema-name': 'dms_sample',
               'table-name': 'authors',
               'timestamp': '2024-05-23T19:17:33.128Z'},
...
...
...
```


## Supported Use Cases

DMS is in a preview state on LocalStack and only supports some selected use cases:

| Source             | Target      | Migration Types |
| -                  | -           | -               | 
| MariaDB (external) | Kinesis     | full-load, cdc  |
| MySQL (external)   | Kinesis     | full-load, cdc  |
| RDS MariaDB        | Kinesis     | full-load, cdc  |
| RDS MySQL          | Kinesis     | full-load, cdc  |


## Current Limitations

For RDS MariaDB and RDS MySQL it is not yet possible to set custom db-parameters. 
In order to make those databases work with `cdc` migration for DMS, some default db-parameters are changed upon start if the `ENABLE_DMS=1` flag is set:

```sh
binlog_checksum=NONE
binlog_row_image=FULL
binlog_format=ROW
server_id=1
log_bin=mysqld-bin
```


### Enum Values for CDC data events

To support Enum values for CDC data events, you need to enable the database setting `BINLOG_ROW_METADATA=FULL`

### Migration Type

A replication task on LocalStack does currently only support `full-load` (migrate existing data) or `cdc` (replicate data changes only). 
On AWS there is also a combination for those, which is not yet implemented on LocalStack.

### ReplicationTaskSettings

The `ReplicationTaskSettings` for a [replication task](https://docs.aws.amazon.com/dms/latest/userguide/CHAP_Tasks.CustomizingTasks.TaskSettings.html) only considers `BeforeImageSettings`, `FullLoadSettings.CommitRate` and `FullLoadSettings.TargetTablePrepMode`


### Other Limitations

- [DMS Serverless](https://docs.aws.amazon.com/dms/latest/userguide/CHAP_Serverless.html) is not yet supported
- [Data Validation](https://docs.aws.amazon.com/dms/latest/userguide/CHAP_Validating.html#CHAP_Validating.TaskStatistics) is not supported
- [Reload](https://docs.aws.amazon.com/dms/latest/userguide/CHAP_Tasks.ReloadTables.html) of tables is not supported
- [Task Logs](https://docs.aws.amazon.com/dms/latest/userguide/CHAP_Monitoring.html#CHAP_Monitoring.ManagingLogs), specifically CloudWatch, and CloudTrail are not supported (table statistics are supported)
- [Time Travel](https://docs.aws.amazon.com/dms/latest/userguide/CHAP_Tasks.CustomizingTasks.TaskSettings.TimeTravel.html) is not supported
- [Target Metadata Settings](https://docs.aws.amazon.com/dms/latest/userguide/CHAP_Tasks.CustomizingTasks.TaskSettings.TargetMetadata.html): `ParallelLoadThreads` is not supported
- [Transformation](https://docs.aws.amazon.com/dms/latest/userguide/CHAP_Tasks.CustomizingTasks.TableMapping.SelectionTransformation.Transformations.html): `"rule-type": "transformation"` is not supported
- [AWS DMS Schema Conversion Tool](https://docs.aws.amazon.com/dms/latest/userguide/CHAP_SchemaConversion.html) is not supported
- [AWS DMS Fleet Advisor](https://docs.aws.amazon.com/dms/latest/userguide/CHAP_FleetAdvisor.html) is not supported
