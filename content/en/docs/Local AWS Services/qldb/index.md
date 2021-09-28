---
title: "Quantum Ledger Database (QLDB)"
linkTitle: "Quantum Ledger Database (QLDB)"
date: 2021-09-28
weight: 5
categories: ["LocalStack Pro"]
description: >
  Quantum Ledger Database (QLDB)
---

The Quantum Ledger Database (QLDB) API supports queries over cryptographically verifiable data, stored in a journal of immutable transaction events. LocalStack allows to create local ledgers and journals, to perform `CREATE TABLE` statements, to insert data via `INSERT` statements, and to query data via `SELECT` statements.

QLDB uses the [Amazon ION data format](https://amzn.github.io/ion-docs), a data serialization format that represents a superset of JSON, with a number of additional features.

A simple QLDB example running on LocalStack is provided in [this Github repository](https://github.com/localstack/localstack-pro-samples/tree/master/qldb-ledger-queries). The sample consists of two simple scenarios: (1) to create and list tables via the `pyqldb` Python library, and (2) to insert data into two tables and perform a `JOIN` query that combines data from the two tables. The sample output is posted below:

```
Scenario 1: create and list tables in ledger
-----------
Creating new test ledger in QLDB API: ledger-test-1
Creating two test tables in ledger
Retrieved list of tables in ledger ledger-test-1: ['foobar1', 'foobar2']
-----------
Scenario 2: create ledger tables and run join query
-----------
Creating two test tables in ledger - "Vehicle" and "VehicleRegistration"
Running a query that joins data from the two tables
Query result: [{'Vehicle': {'id': 'v1'}}, {'Vehicle': {'id': 'v2'}}, {'Vehicle': {'id': 'v3'}}]
```
