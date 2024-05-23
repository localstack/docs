---
title: "Database Migration Service (DMS)"
linkTitle: "Database Migration Service (DMS)"
description: Get started with Database Migration Service (DMS) on LocalStack

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

**TODO** - maybe only link to the sample that we will port to localstack-samples?


## Limitations

For RDS MariaDB and RDS MySQL it is not yet possible to set custom db-parameters. 
In order to make those databases work with `cdc` migration for DMS, some default db-parameters are changed upon start if the `ENABLE_DMS=1` flag is set:

```sh
binlog_checksum=NONE
binlog_row_image=FULL
binlog_format=ROW
server_id=1
log_bin=mysqld-bin
```

### Supported Use Cases

| Source             | Target      | Migration Types |
| -                  | -           | -               | 
| MariaDB (external) | Kinesis     | full-load, cdc  |
| MySQL (external)   | Kinesis     | full-load, cdc  |
| RDS MariaDB        | Kinesis     | full-load, cdc  |
| RDS MySQL          | Kinesis     | full-load, cdc  |



### Enum Values for CDC data events

To support Enum values for CDC data events, you need to enable the database setting `BINLOG_ROW_METADATA=FULL`

### Migration Type

A replication task on LocalStack does currently only support `full-load` (migrate existing data) or `cdc` (replicate data changes only). 
On AWS there is also a combination for those, which is not yet implemented on LocalStack.

### ReplicationTaskSettings

The `ReplicationTaskSettings` for a [replication task](https://docs.aws.amazon.com/dms/latest/userguide/CHAP_Tasks.CustomizingTasks.TaskSettings.html) only considers `BeforeImageSettings`, `FullLoadSettings.CommitRate` and `FullLoadSettings.TargetTablePrepMode`

### Persistence

Persistence on LocalStack for DMS is not supported.


### Unsupported Features or Settings

- [DMS Serverless](https://docs.aws.amazon.com/dms/latest/userguide/CHAP_Serverless.html) is not yet supported
- [Data Validation](https://docs.aws.amazon.com/dms/latest/userguide/CHAP_Validating.html#CHAP_Validating.TaskStatistics) is not supported
- [Reload](https://docs.aws.amazon.com/dms/latest/userguide/CHAP_Tasks.ReloadTables.html) of tables is not supported
- [Task Logs](https://docs.aws.amazon.com/dms/latest/userguide/CHAP_Monitoring.html#CHAP_Monitoring.ManagingLogs), specifically CloudWatch, and CloudTrail are not supported (table statistics are supported)
- [Time Travel](https://docs.aws.amazon.com/dms/latest/userguide/CHAP_Tasks.CustomizingTasks.TaskSettings.TimeTravel.html) is not supported
- [Target Metadata Settings](https://docs.aws.amazon.com/dms/latest/userguide/CHAP_Tasks.CustomizingTasks.TaskSettings.TargetMetadata.html): `ParallelLoadThreads` is not supported
- [Transformation](https://docs.aws.amazon.com/dms/latest/userguide/CHAP_Tasks.CustomizingTasks.TableMapping.SelectionTransformation.Transformations.html): `"rule-type": "transformation"` is not supported
- [AWS DMS Schema Conversion Tool](https://docs.aws.amazon.com/dms/latest/userguide/CHAP_SchemaConversion.html) is not supported
- [AWS DMS Fleet Advisor](https://docs.aws.amazon.com/dms/latest/userguide/CHAP_FleetAdvisor.html) is not supported
