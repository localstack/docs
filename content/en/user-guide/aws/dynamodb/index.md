---
title: DynamoDB
linkTitle: DynamoDB
description: Get started with Amazon DynamoDB on LocalStack
---

DynamoDB on LocalStack is powered by [DynamoDB Local](https://docs.aws.amazon.com/amazondynamodb/latest/developerguide/DynamoDBLocal.html).

## Global tables

LocalStack has support for global tables (version 2019).
These are tables belonging to the same account and replicated across different regions.

Following example illustrates the use of global tables:

{{< command >}}
# Create a table
$ awslocal dynamodb create-table \
    --table-name global01 \
    --key-schema AttributeName=id,KeyType=HASH \
    --attribute-definitions AttributeName=id,AttributeType=S \
    --billing-mode PAY_PER_REQUEST \
    --region ap-south-1
{{< /command >}}

{{< command >}}
# Create replicas
$ awslocal dynamodb update-table \
    --table-name global01 \
    --replica-updates '[{"Create": {"RegionName": "eu-central-1"}}, {"Create": {"RegionName": "us-west-1"}}]' \
    --region ap-south-1
{{< /command >}}

{{< command >}}
# Table can be operated on in all replicated regions
$ awslocal dynamodb list-tables --region eu-central-1
{
    "TableNames": [
        "global01"
    ]
}

$ awslocal dynamodb put-item --table-name global01 --item '{"id":{"S":"foo"}} --region eu-central-1

$ awslocal dynamodb describe-table --table-name global01 --query 'Table.ItemCount' --region ap-south-1
1
{{< /command >}}

{{< alert title="Warning" color="warning">}}
When describing global tables, the current table is treated as a replica.
This is a known bug <https://github.com/localstack/localstack/issues/7426>.
{{< /alert >}}

{{< command >}}
$ awslocal dynamodb describe-table --table-name global01 --query 'Table.Replicas' --region us-west-1
[
    {
        "RegionName": "ap-south-1",
        "ReplicaStatus": "ACTIVE"
    },
    {
        "RegionName": "eu-central-1",
        "ReplicaStatus": "ACTIVE"
    },
    {
        "RegionName": "us-west-1",
        "ReplicaStatus": "ACTIVE"
    }
]
{{< /command >}}

{{< alert title="Warning" color="warning">}}
It is currently not possible to remove the original table region from the replication set.
Deleting the original table will also remove all the replicas.
{{< /alert >}}

{{< alert title="Warning" color="warning">}}
DynamoDB Streams are only supported for original tables and not for replicated tables.
Please see <https://github.com/localstack/localstack/issues/7405> for more information.
{{< /alert >}}

{{< alert title="Warning" color="warning">}}
Batch operations (`BatchWriteItem`, `BatchGetItem`, etc.) are currently not supported on replicated tables.
{{< /alert >}}

<!--
## SSE specifications

## Kinesis streams
-->
