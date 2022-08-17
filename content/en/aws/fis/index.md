---
title: "FIS"
linkTitle: "FIS"
categories: ["LocalStack Pro"]
description: >
  Fault Injection Simulator (FIS)
---

Basic support for the Fault Injection Simulator (FIS) service is included in LocalStack Pro. The local FIS API allows you to introduce faults to other services - in order to check how your setup behaves when parts of it stop working.
The full list of such possible fault introductions - called "actions" - available in AWS is [here](https://docs.aws.amazon.com/fis/latest/userguide/fis-actions-reference.html).

In general, calls to FIS contain the following information:

1. What kind of fault to introduce - "action".
2. What kind of resources to affect - "target".
3. (sometimes) Duration of the interruption. After the specified amount of time FIS is supposed to revert systems to their original state or to stop introducing faults.

FIS actions come in roughly two types:

1. A single-time event, e.g., `aws:ec2:stop-instances` FIS action is a `stop-instances` command sent to target EC2 instances. Results of some of these single-time events can be automatically reverted after a specified period of time, e.g., by sending `start-instances` command to the affected instances.
2. Generation of API errors in response to a specified percentage of API calls. E.g. aws:fis:inject-api-unavailable-error. Currently AWS only supports this for EC2 API calls.

# Most notable current FIS limitations in LocalStack
1. Only a subset of FIS actions available in AWS are currently supported in LocalStack (unsupported actions generate an error). The set of supported actions is extended on an ongoing basis, and new actions can easily be added on demand.
2. Only single-time events are supported. The continuous generation of API errors in reponse to some API calls is in the works.
3. LocalStack doesn't support target selection mechanism used by AWS. See [selection mode documentation for more info](https://docs.aws.amazon.com/fis/latest/userguide/targets.html#target-selection-mode)
4. LocalStack ignores [roleArns](https://docs.aws.amazon.com/fis/latest/APIReference/API_ExperimentTemplate.html#fis-Type-ExperimentTemplate-roleArn). In AWS FIS performs actions under permissions granted to given roleArns.
