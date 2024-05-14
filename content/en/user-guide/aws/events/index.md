---
title: "EventBridge"
linkTitle: "EventBridge"
description: >
  Get started with EventBridge on LocalStack
aliases:
- /user-guide/aws/eventbridge/
---

## Introduction

EventBridge provides a centralized mechanism to discover and communicate events across various AWS services and applications. EventBridge allows you to register, track, and resolve events, which indicates a change in the environment and then applies a rule to route the event to a target. EventBridge rules are tied to an Event Bus to manage event-driven workflows. You can use either identity-based or resource-based policies to control access to EventBridge resources, where the former can be attached to IAM users, groups, and roles, and the latter can be attached to specific AWS resources.

LocalStack allows you to use the EventBridge APIs in your local environment to create rules that route events to a target. The supported APIs are available on our [API coverage page](https://docs.localstack.cloud/references/coverage/coverage_events/), which provides information on the extent of EventBridge's integration with LocalStack. For information on EventBridge Pipes, please refer to the [EventBridge Pipes]({{< ref "user-guide/aws/pipes" >}}) section.

## Getting Started

This guide is designed for users new to EventBridge and assumes basic knowledge of the AWS CLI and our [`awslocal`](https://github.com/localstack/awscli-local) wrapper script.

Start your LocalStack container using your preferred method. We will demonstrate creating an EventBridge rule to run a Lambda function on a schedule.

### Create a Lambda Function

To create a new Lambda function, create a new file called `index.js` with the following code:

```js
'use strict';

exports.handler = (event, context, callback) => {
    console.log('LogScheduledEvent');
    console.log('Received event:', JSON.stringify(event, null, 2));
    callback(null, 'Finished');
};
```

Run the following command to create a new Lambda function using the [`CreateFunction`](https://docs.aws.amazon.com/cli/latest/reference/lambda/create-function.html) API:

{{< command >}}
$ zip function.zip index.js

$ awslocal lambda create-function \
    --function-name events-example \
    --runtime nodejs16.x \
    --zip-file fileb://function.zip \
    --handler index.handler \
    --role arn:aws:iam::000000000000:role/cool-stacklifter
{{< /command >}}

The output will consist of the `FunctionArn`, which you will need to add the Lambda function to the EventBridge target.

### Create an EventBridge Rule

Run the following command to create a new EventBridge rule using the [`PutRule`](https://docs.aws.amazon.com/cli/latest/reference/events/put-rule.html) API:

{{< command >}}
$ awslocal events put-rule \
    --name my-scheduled-rule \
    --schedule-expression 'rate(2 minutes)'
{{< /command >}}

In the above command, we have specified a schedule expression of `rate(2 minutes)`, which will run the rule every two minutes. It means that the Lambda function will be invoked every two minutes.

Next, grant the EventBridge service principal (`events.amazonaws.com`) permission to run the rule, using the [`AddPermission`](https://docs.aws.amazon.com/cli/latest/reference/events/add-permission.html) API:

{{< command >}}
$ awslocal lambda add-permission \
    --function-name events-example \
    --statement-id my-scheduled-event \
    --action 'lambda:InvokeFunction' \
    --principal events.amazonaws.com \
    --source-arn arn:aws:events:us-east-1:000000000000:rule/my-scheduled-rule
{{< /command >}}

### Add the Lambda Function as a Target

Create a file named `targets.json` with the following content:

```json
[
    {
      "Id": "1", 
      "Arn": "arn:aws:lambda:us-east-1:000000000000:function:events-example"
    }
]
```

Finally, add the Lambda function as a target to the EventBridge rule using the [`PutTargets`](https://docs.aws.amazon.com/cli/latest/reference/events/put-targets.html) API:

{{< command >}}
$ awslocal events put-targets \
    --rule my-scheduled-rule \
    --targets file://targets.json
{{< /command >}}

### Verify the Lambda invocation

You can verify the Lambda invocation by checking the CloudWatch logs. However, wait at least 2 minutes after running the last command before checking the logs.

Run the following command to list the CloudWatch log groups:

{{< command >}}
$ awslocal logs describe-log-groups
{{< /command >}}

The output will contain the log group name, which you can use to list the log streams:

{{< command >}}
$ awslocal logs describe-log-streams \
    --log-group-name /aws/lambda/events-example
{{< /command >}}

Alternatively, you can fetch LocalStack logs to verify the Lambda invocation:

{{< command >}}
$ localstack logs
...
2023-07-17T09:37:52.028  INFO --- [   asgi_gw_0] localstack.request.aws     : AWS lambda.Invoke => 202
2023-07-17T09:37:52.106  INFO --- [   asgi_gw_0] localstack.request.http    : POST /_localstack_lambda/97e08ac50c18930f131d9dd9744b8df4/invocations/ecb744d0-b3f2-400f-9e49-c85cf12b1e00/logs => 202
2023-07-17T09:37:52.114  INFO --- [   asgi_gw_0] localstack.request.http    : POST /_localstack_lambda/97e08ac50c18930f131d9dd9744b8df4/invocations/ecb744d0-b3f2-400f-9e49-c85cf12b1e00/response => 202
...
{{< /command >}}

## Supported target types

{{< callout >}}
LocalStack now supports a new event rule engine for [EventBridge event patterns](https://docs.aws.amazon.com/eventbridge/latest/userguide/eb-event-patterns.html).
You can [configure]({{< ref "configuration" >}}) `EVENT_RULE_ENGINE=java` (preview) to use the AWS [event-ruler](https://github.com/aws/event-ruler), which offers better parity.
{{< /callout >}}

At this time LocalStack supports the following [target types](https://docs.aws.amazon.com/eventbridge/latest/userguide/eb-targets.html#eb-console-targets) for EventBridge rules:

- Lambda function
- SNS Topic
- SQS queue
- StepFunctions StateMachine
- Firehose
- Event bus
- API destination
- Kinesis
- CloudWatch log group


## Resource Browser

The LocalStack Web Application provides a Resource Browser for managing EventBridge Buses. You can access the Resource Browser by opening the LocalStack Web Application in your browser, navigating to the **Resources** section, and then clicking on **EventBridge** under the **App Integration** section.

The Resource Browser allows you to perform the following actions:

- **View the Event Buses**: You can view the list of EventBridge Buses running locally, alongside their Amazon Resource Names (ARNs) and Policies.
- **Create Event Rule**: You can create a new Event Rule by specifying **Name**, **Description**, **Event Pattern**, **Schedule Expressions**, **State**, **Role ARN**, and **Tags**.
- **Trigger Event**: You can trigger an Event by specifying the **Entries** and **Endpoint Id**. While creating an Entry, you must specify **Source**, **Event Bus Name**, **Detail**, **Resources**, **Detail Type**, and **Trace Header**.
- **Remove Selected**: You can remove the selected EventBridge Bus.
