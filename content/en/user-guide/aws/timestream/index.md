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
$ awslocal timestream-query query --query-string "SELECT CREATE_TIME_SERIES(time, measure_value::double) as cpu FROM testDB.timeStreamTable WHERE measure_name='cpu'"
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

## Date / Time Functions

LocalStack supports the following functions for querying Timestream data:

| Function | Description                                                         | Data type |
|----------|---------------------------------------------------------------------|-----------|
| ago (interval)      | Returns the value corresponding to current_timestamp `interval`.    | timestamp |
| bin (timestamp, interval)     | Returns a rounded value down to a multiple of given bin `interval`. | timestamp |
| parse_duration (string) | Returns an `interval` equivalent parsed out of the input string. | interval |
| from_iso8601_date (string) | Parses the ISO 8601 date string into internal Timestamp format for UTC 00:00:00 of the specified date. | timestamp |
| from_iso8601_timestamp (string) | Parses the ISO 8601 timestamp into internal timestamp format. | timestamp |
