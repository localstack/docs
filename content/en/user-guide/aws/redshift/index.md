---
title: "Redshift"
linkTitle: "Redshift"
description: Get started with Redshift on LocalStack
tags: ["Pro image"]
---

## Introduction

RedShift is a cloud-based data warehouse solution which allows end users to aggregate huge volumes of data and parallel processing of data.
RedShift is fully managed by AWS and serves as a petabyte-scale service which allows users to create visualization reports and critically analyze collected data.
The query results can be saved to an S3 Data Lake while additional analytics can be provided by Athena or SageMaker.

LocalStack allows you to use the RedShift APIs in your local environment to analyze structured and semi-structured data across local data warehouses and data lakes.
The supported APIs are available on our [API coverage page](https://docs.localstack.cloud/references/coverage/coverage_redshift/), which provides information on the extent of RedShift's integration with LocalStack.

## Getting started

This guide is designed for users new to RedShift and assumes basic knowledge of the AWS CLI and our [`awslocal`](https://github.com/localstack/awscli-local) wrapper script.

Start your LocalStack container using your preferred method.
We will demonstrate how to create a RedShift cluster and database while using a Glue Crawler to populate the metadata store with the schema of the RedShift database tables using the AWS CLI.

### Define the variables

First, we will define the variables we will use throughout this guide.
Export the following variables in your shell:

```bash
REDSHIFT_CLUSTER_IDENTIFIER="redshiftcluster"
REDSHIFT_SCHEMA_NAME="public"
REDSHIFT_DATABASE_NAME="db1"
REDSHIFT_TABLE_NAME="sales"
REDSHIFT_USERNAME="crawlertestredshiftusername"
REDSHIFT_PASSWORD="crawlertestredshiftpassword"
GLUE_DATABASE_NAME="gluedb"
GLUE_CONNECTION_NAME="glueconnection"
GLUE_CRAWLER_NAME="gluecrawler"
```

The above variables will be used to create a RedShift cluster, database, table, and user.
You will also create a Glue database, connection, and crawler to populate the Glue Data Catalog with the schema of the RedShift database tables.

### Create a RedShift cluster and database

You can create a RedShift cluster using the [`CreateCluster`](https://docs.aws.amazon.com/redshift/latest/APIReference/API_CreateCluster.html) API.
The following command will create a RedShift cluster with the variables defined above:

{{< command >}}
$ awslocal redshift create-cluster \
      --cluster-identifier $REDSHIFT_CLUSTER_IDENTIFIER \
      --db-name $REDSHIFT_DATABASE_NAME \
      --master-username $REDSHIFT_USERNAME \
      --master-user-password $REDSHIFT_PASSWORD \
      --node-type n1
{{< / command >}}

You can fetch the status of the cluster using the [`DescribeClusters`](https://docs.aws.amazon.com/redshift/latest/APIReference/API_DescribeClusters.html) API.
Run the following command to extract the URL of the cluster:

{{< command >}}
$ REDSHIFT_URL=$(awslocal redshift describe-clusters \
      --cluster-identifier $REDSHIFT_CLUSTER_IDENTIFIER | jq -r '(.Clusters[0].Endpoint.Address) + ":" + (.Clusters[0].Endpoint.Port|tostring)')
{{< / command >}}

### Create a Glue database, connection, and crawler

You can create a Glue database using the [`CreateDatabase`](https://docs.aws.amazon.com/glue/latest/webapi/API_CreateDatabase.html) API.
The following command will create a Glue database:

{{< command >}}
$ awslocal glue create-database \
      --database-input "{\"Name\": \"$GLUE_DATABASE_NAME\"}"
{{< / command >}}

You can create a connection to the RedShift cluster using the [`CreateConnection`](https://docs.aws.amazon.com/glue/latest/webapi/API_CreateConnection.html) API.
The following command will create a Glue connection with the RedShift cluster:

{{< command >}}
$ awslocal glue create-connection \
      --connection-input "{\"Name\":\"$GLUE_CONNECTION_NAME\", \"ConnectionType\": \"JDBC\", \"ConnectionProperties\": {\"USERNAME\": \"$REDSHIFT_USERNAME\", \"PASSWORD\": \"$REDSHIFT_PASSWORD\", \"JDBC_CONNECTION_URL\": \"jdbc:redshift://$REDSHIFT_URL/$REDSHIFT_DATABASE_NAME\"}}"
{{< / command >}}

Finally, you can create a Glue crawler using the [`CreateCrawler`](https://docs.aws.amazon.com/glue/latest/webapi/API_CreateCrawler.html) API.
The following command will create a Glue crawler:

{{< command >}}
$ awslocal glue create-crawler \
      --name $GLUE_CRAWLER_NAME \
      --database-name $GLUE_DATABASE_NAME \
      --targets "{\"JdbcTargets\": [{\"ConnectionName\": \"$GLUE_CONNECTION_NAME\", \"Path\": \"$REDSHIFT_DATABASE_NAME/%/$REDSHIFT_TABLE_NAME\"}]}" \
      --role r1
{{< / command >}}

### Create table in RedShift

You can create a table in RedShift using the [`CreateTable`](https://docs.aws.amazon.com/redshift/latest/dg/r_CREATE_TABLE_NEW.html) API.
The following command will create a table in RedShift:

{{< command >}}
$ REDSHIFT_STATEMENT_ID=$(awslocal redshift-data execute-statement \
      --cluster-identifier $REDSHIFT_CLUSTER_IDENTIFIER \
      --database $REDSHIFT_DATABASE_NAME \
      --sql \
  "create table $REDSHIFT_TABLE_NAME(salesid integer not null, listid integer not null, sellerid integer not null, buyerid integer not null, eventid integer not null, dateid smallint not null, qtysold smallint not null, pricepaid decimal(8,2), commission decimal(8,2), saletime timestamp)" | jq -r .Id)
{{< / command >}}

You can check the status of the statement using the [`DescribeStatement`](https://docs.aws.amazon.com/redshift-data/latest/APIReference/API_DescribeStatement.html) API.
The following command will check the status of the statement:

{{< command >}}
$ wait "awslocal redshift-data describe-statement \
      --id $REDSHIFT_STATEMENT_ID" ".Status" "FINISHED"
{{< / command >}}

### Run the crawler

You can run the crawler using the [`StartCrawler`](https://docs.aws.amazon.com/glue/latest/webapi/API_StartCrawler.html) API.
The following command will run the crawler:

{{< command >}}
$ awslocal glue start-crawler \
      --name $GLUE_CRAWLER_NAME
{{< / command >}}

You can wait for the crawler to finish using the [`GetCrawler`](https://docs.aws.amazon.com/glue/latest/webapi/API_GetCrawler.html) API.
The following command will wait for the crawler to finish:

{{< command >}}
$ wait "awslocal glue get-crawler \
      --name $GLUE_CRAWLER_NAME" ".Crawler.State" "READY"
{{< / command >}}

You can finally retrieve the schema of the table using the [`GetTable`](https://docs.aws.amazon.com/glue/latest/webapi/API_GetTable.html) API.
The following command will retrieve the schema of the table:

{{< command >}}
$ awslocal glue get-table \
      --database-name $GLUE_DATABASE_NAME \
      --name "${REDSHIFT_DATABASE_NAME}_${REDSHIFT_SCHEMA_NAME}_${REDSHIFT_TABLE_NAME}"
{{< / command >}}
