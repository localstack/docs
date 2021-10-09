---
title: "Kinesis"
categories: ["LocalStack Community"]
description: >
  Explaining the different Kinesis providers and how to configure the service.
---

AWS Kinesis is a fully managed data streaming service, which enables your application to ingest, buffer, and process data in real-time. 
Kinesis is shipped with the LocalStack Community version and is [extensively supported]({{< ref "feature-coverage.md" >}}).

## Quickstart

Trying to run the example applications from the [official AWS developer guide](https://docs.aws.amazon.com/streams/latest/dev/examples.html) against LocalStack is a great place to start.
Assuming you have `awslocal` installed you can also try out the following commands:

{{< command >}}
$ awslocal kinesis create-stream --stream-name samplestream --shard-count  1
{{< /command >}}

{{< command >}}
$ awslocal kinesis list-streams 
{
    "StreamNames": [
        "samplestream"
    ]
}
{{< /command >}}

{{< command >}}
$ awslocal kinesis put-record --stream-name samplestream --data '{"symbol":"TEST","sampleno":42}' --partition-key test1 
{
    "ShardId": "shardId-000000000001",
    "SequenceNumber": "49622467803485029265018102167378141645049970239670845458",
    "EncryptionType": "NONE"
}
{{< / command >}}

## Kinesis backend providers

LocalStack supports two third-party providers for Kinesis:
* [kinesis-mock](https://github.com/etspaceman/kinesis-mock)
* [kinesalite](https://github.com/mhart/kinesalite)

By default `kinesis-mock` is used.
Your desired provider can be set with the environment variable `KINESIS_PROVIDER`.
For instance, if you wish to use `kinesalite` you'd pass the environment variable as `KINESIS_PROVIDER=kinesalite`.
While both providers are supported, we recommend working with `kinesis-mock`, as it is more actively maintained.
Moreover, the [Cloud Pods]({{< ref "cloud-pods" >}}) feature provides support **only** for `kinesis-mock`. 

## Configuration


Regardless of which provider you're working with, Kinesis can be further configured with the following environment variables:

| Variable | Description |
| -------- | ----------- |
| `KINESIS_ERROR_PROBABILITY` | Decimal value between `0.0` (default) and `1.0`. Typically, it is difficult to know beforehand whether your application can handle the throughput and whether it can deal with backpressure. By setting this environment variable the application will randomly inject `ProvisionedThroughputException`. While this won't tell you whether your application can handle sufficient throughput, it does help you to test whether your application can handle exceptions gracefully. |
| `KINESIS_SHARD_LIMIT` | Integer value (default: `100`) or `Infinity` (to disable). This variable can help you to test whether your application adheres to the allocated shard limit. This behavior can only be disabled by explicitly setting the environment variable as `KINESIS_SHARD_LIMIT=Infinity` |
| `KINESIS_LATENCY` | Integer value of milliseconds (default: `500`) or `0` (to disable). Especially important for testing latency-critical applications. Since latency cannot be tested with the local Kinesis service, you can use this variable to introduce artificial latency into your AWS calls. This behavior can only be disabled by explicitly setting the environment variable as `KINESIS_LATENCY=0`. |
| `KINESIS_INITIALIZE_STREAMS` | A comma-delimited string of stream names, its corresponding shard count and an optional region to initialize during startup. If the region is not provided, the default region is used. For instance, `KINESIS_INITIALIZE_STREAMS=my-first-stream:1,my-other-stream:2:us-west-2,my-last-stream:1` **Important**: Only supported by `kinesis-mock` |
