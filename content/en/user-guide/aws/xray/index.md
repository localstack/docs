---
title: "X-Ray"
linkTitle: "X-Ray"
description: Get started with X-Ray on LocalStack
tags: ["Pro image"]
---

## Introduction

[X-Ray](https://docs.aws.amazon.com/xray/latest/devguide/aws-xray.html) is a distributed tracing service that
helps to understand cross-service interactions and facilitates debugging of performance bottlenecks. Instrumented applications generate trace data by recording trace segments with information about the work tasks of an
application, such as timestamps, tasks names, or metadata. X-Ray supports different ways of [instrumenting your application](https://docs.aws.amazon.com/xray/latest/devguide/xray-instrumenting-your-app.html) including
the [AWS X-Ray SDK](https://docs.aws.amazon.com/xray/latest/devguide/xray-instrumenting-your-app.html#xray-instrumenting-xray-sdk) and
the [AWS Distro for OpenTelemetry (ADOT)](https://docs.aws.amazon.com/xray/latest/devguide/xray-instrumenting-your-app.html#xray-instrumenting-opentel).
[X-Ray daemon](https://docs.aws.amazon.com/xray/latest/devguide/xray-daemon.html) is an application that gathers
raw trace segment data from the X-Ray SDK and relays it to the AWS X-Ray API.
The X-Ray API can then be used to retrieve traces originating from different application components.

LocalStack allows
you to use the X-Ray APIs to send and retrieve trace segments in your local environment.
The supported APIs are available on our [API Coverage Page](https://docs.localstack.cloud/references/coverage/coverage_xray/),
which provides information on the extent of X-Ray integration with LocalStack.

## Getting started

This guide is designed for users new to X-Ray and assumes basic
knowledge of the AWS CLI and our `awslocal` wrapper script.

Start your LocalStack container using your preferred method. We will demonstrate how you can create a minimal [trace segment](https://docs.aws.amazon.com/xray/latest/devguide/xray-api-segmentdocuments.html#api-segmentdocuments-fields)
and manually send it to the X-Ray API. Notice that this trace ingestion typically happens in the background, for example by the X-Ray SDK and X-Ray daemon.

 [PutTraceSegments](https://docs.aws.amazon.com/xray/latest/api/API_PutTraceSegments.html).

### Sending trace segments

You can generates a unique trace ID and constructs a JSON document with trace information. It then sends this trace segment to the AWS X-Ray API using the    [PutTraceSegments](https://docs.aws.amazon.com/xray/latest/api/API_PutTraceSegments.html) API. Run the following commands in your terminal:

{{< command >}}
$ START_TIME=$(date +%s)
$ HEX_TIME=$(printf '%x\n' $START_TIME)
$ GUID=$(dd if=/dev/random bs=12 count=1 2>/dev/null | od -An -tx1 | tr -d ' \t\n')
$ TRACE_ID="1-$HEX_TIME-$GUID"
$ END_TIME=$(($START_TIME+3))
$ DOC=$(cat <<EOF
{"trace_id": "$TRACE_ID", "id": "6226467e3f845502", "start_time": $START_TIME.37518, "end_time": $END_TIME.4042, "name": "test.elasticbeanstalk.com"}
EOF
)
$ echo "Sending trace segment to X-Ray API: $DOC"
$ awslocal xray put-trace-segments --trace-segment-documents "$DOC"
<disable-copy>
Sending trace segment to X-Ray API: {"trace_id": "1-6501ee11-056ec85fafff21f648e2d3ae", "id": "6226467e3f845502", "start_time": 1694625297.37518, "end_time": 1694625300.4042, "name": "test.elasticbeanstalk.com"}
{
"UnprocessedTraceSegments": []
}
</disable-copy>
{{< /command >}}

### Retrieve trace summaries

You can now retrieve the trace summaries from the last 10 minutes using the [GetTraceSummaries](https://docs.aws.amazon.com/xray/latest/api/API_GetTraceSummaries.html) API. Run the following commands in your terminal:

{{< command >}}
$ EPOCH=$(date +%s)
$ awslocal xray get-trace-summaries --start-time $(($EPOCH-600)) --end-time $(($EPOCH))
<disable-copy>
{
    "TraceSummaries": [
        {
            "Id": "1-6501ee11-056ec85fafff21f648e2d3ae",
            "Duration": 3,
            "ResponseTime": 1,
            "HasFault": false,
            "HasError": false,
            "HasThrottle": false,
            "Http": {},
            "Annotations": {},
            "Users": [],
            "ServiceIds": []
        }
    ],
    "TracesProcessedCount": 1,
    "ApproximateTime": 1694625413.0
}
</disable-copy>
{{< /command >}}

### Retrieve full trace

You can retrieve the full trace by providing the `TRACE_ID` using the [BatchGetTraces](https://docs.aws.amazon.com/xray/latest/api/API_BatchGetTraces.html) API. Run the following commands in your terminal (use the same terminal as for the first command):

{{< command >}}
$ awslocal xray batch-get-traces --trace-ids $TRACE_ID
<disable-copy>
{
    "Traces": [
        {
            "Id": "1-6501ee11-056ec85fafff21f648e2d3ae",
            "Duration": 3,
            "Segments": [
                {
                    "Id": "6226467e3f845502",
                    "Document": "{\"trace_id\": \"1-6501ee11-056ec85fafff21f648e2d3ae\", \"id\": \"6226467e3f845502\", \"start_time\": 1694625297.37518, \"end_time\": 1694625300.4042, \"name\": \"test.elasticbeanstalk.com\"}"
                }
            ]
        }
    ],
    "UnprocessedTraceIds": []
}
</disable-copy>
{{< /command >}}

## Examples

The following code snippets and sample applications provide practical examples of how to use X-Ray in LocalStack:

- [Lambda X-Ray](https://github.com/localstack/localstack-pro-samples/tree/master/lambda-xray) shows how to instrument Lambda functions for X-Ray using Powertools and the X-Ray SDK.

## Current Limitations

LocalStack supports collecting trace segments but currently does not correlate multiple trace segments with the same
`trace_id` into a single aggregated trace.
