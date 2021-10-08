---
title: "Relational Database Service (RDS)"
linkTitle: "Relational Database Service (RDS)"
categories: ["LocalStack Pro"]
description: >
  Relational Database Service (RDS)
---

LocalStack supports a basic version of [RDS](https://aws.amazon.com/rds/) for testing. Currently, it is possible to spin up PostgreSQL databases on the local machine; support for MySQL and other DB engines is under development and coming soon.

The local RDS service also supports the [RDS Data API](https://docs.aws.amazon.com/AmazonRDS/latest/AuroraUserGuide/data-api.html), which allows executing data queries over a JSON/REST interface. Below is a simple example that illustrates (1) creation of an RDS database, (2) creation of a SecretsManager secret with the DB password, and (3) running a simple `SELECT 123` query via the RDS Data API.
{{< command >}}
$ awslocal rds create-db-instance --db-instance-identifier db1 --db-instance-class c1 --engine postgres
...
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
