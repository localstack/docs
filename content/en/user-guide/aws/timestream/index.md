---
title: "Timestream"
linkTitle: "Timestream"
description: >
  Get started with Timestream on LocalStack
tags: ["Pro image"]
---

## Introduction

LocalStack contains basic support for Timestream time series databases, including these operations:

* Creating databases
* Creating tables
* Writing records to tables
* Querying timeseries data from tables

The supported APIs are available on our API Coverage Page ([Timestream-Query](https://docs.localstack.cloud/references/coverage/coverage_timestream-query/)/[Timestream-Write](https://docs.localstack.cloud/references/coverage/coverage_timestream-write/)), which provides information on the extent of Timestream integration with LocalStack.

## Getting Started

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

## Limitations

LocalStack's Timestream implementation is under active development and only supports a limited set of operations, please refer to the API Coverage pages for an up-to-date list of implemented and tested functions within [Timestream-Query](https://docs.localstack.cloud/references/coverage/coverage_timestream-query/) and [Timestream-Write](https://docs.localstack.cloud/references/coverage/coverage_timestream-write/).

If you have a usecase that uses Timestream but doesn't work with our implementation yet, we encourage you to [get in touch](https://localstack.cloud/contact/), so we can streamline any operations you rely on.