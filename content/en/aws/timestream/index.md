---
title: "Timestream"
linkTitle: "Timestream"
categories: ["LocalStack Pro"]
description: >
  Timestream
---

LocalStack Pro contains basic support for Timestream time series databases, including these operations:
* Creating databases
* Creating tables
* Writing records to tables
* Querying timeseries data from tables

## Simple Usage Example

The following example illustrates the basic operations, using the [`awslocal`](https://github.com/localstack/awscli-local) command line.

First, we create a test database and table:

{{< command >}}
$ awslocal timestream-write create-database --database-name testDB
$ awslocal timestream-write create-table --database-name testDB --table-name testTable
{{</ command >}}

We can then add a few records with a timestamp, measure name, and value to the table:

{{< command >}}
$ awslocal timestream-write write-records --database-name testDB --table-name testTable --records '[{"MeasureName":"cpu","MeasureValue":"60","TimeUnit":"SECONDS","Time":"1636986409"}]'
$ awslocal timestream-write write-records --database-name testDB --table-name testTable --records '[{"MeasureName":"cpu","MeasureValue":"80","TimeUnit":"SECONDS","Time":"1636986412"}]'
$ awslocal timestream-write write-records --database-name testDB --table-name testTable --records '[{"MeasureName":"cpu","MeasureValue":"70","TimeUnit":"SECONDS","Time":"1636986414"}]'
{{</ command >}}

Finally, we can run a query to retrieve the timeseries data (or aggregate values) from the table:
{{< command >}}
$ awslocal timestream-query query --query-string "SELECT CREATE_TIME_SERIES(time, measure_value::double) as cpu FROM timeStreamDB.timeStreamTable WHERE measure_name='cpu'"
{
  "Rows": [{
    "Data": [{
      "TimeSeriesValue": [{
        "Time": "2021-11-15T14:26:49",
        "Value": {
            "ScalarValue": 60
        }
    },
...
{{</ command >}}
