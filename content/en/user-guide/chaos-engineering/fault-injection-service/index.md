---
title: "AWS Fault Injection Service"
linkTitle: "AWS Fault Injection Service"
description: Use Fault Injection Service to simulate faults in your infrastructure and test its fault tolerance
tags: ["Ultimate"]
---

The [Fault Injection Service (FIS)](https://aws.amazon.com/fis/) is a fully managed service by AWS designed to help you improve the resilience of your applications by simulating real-world outages and operational issues.
This service allows you to conduct controlled experiments on your AWS infrastructure, injecting faults and observing how your system responds under various conditions.

By using the Fault Injection Service, you can identify weaknesses, test recovery procedures, and ensure that your applications can withstand unexpected disruptions.
This proactive approach to reliability engineering enables you to enhance system robustness, minimize downtime, and maintain a high level of service availability for your users.

{{< callout "tip" >}}
For more information, please refer to the [FIS service docs]({{< ref "user-guide/aws/fis" >}}).
{{< /callout >}}

Some of the most important concepts associated with a FIS experiment are:

**1.
Experiment Templates**: Experiment templates define the actions, targets, and any stop conditions for your experiment.
They serve as blueprints for conducting fault injection experiments, allowing you to specify what resources are targeted, what faults are injected, and under what conditions the experiment should automatically stop.

**2.
Actions**: Actions are the specific fault injection operations that the experiment performs on the target resources.
These can be injecting latency or throttling to API requests, completely blocking access to instances, etc.
Actions define the type of fault, parameters for the fault injection, and the targets affected.

**3.
Targets**: Targets are the AWS resources on which the experiment actions will be applied.
To make things even more fine-grained, a specific operation of the service can be targeted.

**4.
Stop Conditions**: Stop conditions are criteria that, when met, will automatically stop the experiment.

**5.
IAM Roles and Permissions**: To run experiments, AWS FIS requires specific IAM roles and permissions.
These are necessary for AWS FIS to perform actions on your behalf, like injecting faults into your resources.

**6.
Experiment Execution**: When you start an experiment, AWS FIS executes the actions defined in the experiment template against the specified targets, adhering to any defined stop conditions.
The execution process is logged, and detailed information about the experiment's progress and outcome is provided.
