---
title: "Step Functions"
linkTitle: "Step Functions"
description: >
    Get started with Step Functions on LocalStack
---

Step Functions is a serverless workflow engine that integrates with AWS Lambda and other AWS services. Step Functions allows you to define workflows using Amazon States Language, a JSON-based structured language, to provide the necessary configurations and run the workflow. Step Functions allow you to define standard workflows and express workflows for long-running and high-volume event processing.

LocalStack supports Step Functions via the Community offering, allowing you to use the Step Functions APIs in your local environment to create, execute, update, and delete state machines locally. The supported APIs are available on our [API coverage page](https://docs.localstack.cloud/references/coverage/coverage_stepfunctions/), which provides information on the extent of Step Function's integration with LocalStack.

## Getting started

This guide is designed for users new to Step Functions and assumes basic knowledge of the AWS CLI and our [`awslocal`](https://github.com/localstack/awscli-local) wrapper script.

Start your LocalStack container using your preferred method. We will demonstrate how you can create a state machine, execute it, and check the status of the execution.

### Create a state machine

You can create a state machine using the [`CreateStateMachine`](https://docs.aws.amazon.com/step-functions/latest/apireference/API_CreateStateMachine.html) API. The API requires the name of the state machine, the state machine definition, and the role ARN that the state machine will assume to call AWS services. Run the following command to create a state machine:

{{< command >}}
$ awslocal stepfunctions create-state-machine \
     --name "WaitMachine" \
     --definition '{
        "StartAt": "WaitExecution",
        "States": {
            "WaitExecution": {
            "Type": "Wait",
            "Seconds": 10,
            "End": true
            }
        }
     }' \
     --role-arn "arn:aws:iam::000000000000:role/stepfunctions-role"
{{< /command >}}

The output of the above command is the ARN of the state machine:

```json
{
     "stateMachineArn": "arn:aws:states:<AWS_REGION>:000000000000:stateMachine:WaitMachine",
     "creationDate": "<DATE>"
}
```

You can list the state machines using the [`ListStateMachines`](https://docs.aws.amazon.com/step-functions/latest/apireference/API_ListStateMachines.html) API. Run the following command to list the state machines:

{{< command >}}
$ awslocal stepfunctions list-state-machines
{{< /command >}}

The output of the above command is a list of state machines:

```json
{
	"stateMachines": [{
		"stateMachineArn": "arn:aws:states:us-east-1:000000000000:stateMachine:WaitMachine",
		"name": "WaitMachine",
		"type": "STANDARD",
		"creationDate": "<DATE>"
	}]
}
```

### Execute the state machine

You can execute the state machine using the [`StartExecution`](https://docs.aws.amazon.com/step-functions/latest/apireference/API_StartExecution.html) API. The API requires the state machine's ARN and the state machine's input. Run the following command to execute the state machine:

{{< command >}}
$ awslocal stepfunctions start-execution \
     --state-machine-arn "arn:aws:states:us-east-1:000000000000:stateMachine:WaitMachine"
{{< /command >}}

The output of the above command is the execution ARN:

```json
{
     "executionArn": "arn:aws:states:us-east-1:000000000000:execution:WaitMachine:<ID>",
     "startDate": "<DATE>"
}
```

To check the status of the execution, you can use the [`DescribeExecution`](https://docs.aws.amazon.com/step-functions/latest/apireference/API_DescribeExecution.html) API. Run the following command to describe the execution:

{{< command >}}
$ awslocal stepfunctions describe-execution \
     --execution-arn "arn:aws:states:us-east-1:000000000000:execution:WaitMachine:<ID>"
{{< /command >}}

The output of the above command is the execution status:

```json
{
     "executionArn": "arn:aws:states:us-east-1:000000000000:execution:WaitMachine:32174130-4587-4314-ad63-86c6242523b2",
     "stateMachineArn": "arn:aws:states:us-east-1:000000000000:stateMachine:WaitMachine",
     ...
     }
}
```

### Update and delete the state machine

You can update the state machine definition using the [`UpdateStateMachine`](https://docs.aws.amazon.com/step-functions/latest/apireference/API_UpdateStateMachine.html) API. The API requires the ARN of the state machine and the new state machine definition. Run the following command to update the state machine definition:

{{< command >}}
$ awslocal stepfunctions update-state-machine \
     --state-machine-arn "arn:aws:states:us-east-1:000000000000:stateMachine:WaitMachine" \
     --definition file://path/to/your/statemachine.json
     --role-arn "arn:aws:iam::000000000000:role/stepfunctions-role"
{{< /command >}}

You can delete the state machine using the [`DeleteStateMachine`](https://docs.aws.amazon.com/step-functions/latest/apireference/API_DeleteStateMachine.html) API. Run the following command to delete the state machine:

{{< command >}}
$ awslocal stepfunctions delete-state-machine \
     --state-machine-arn "arn:aws:states:us-east-1:000000000000:stateMachine:WaitMachine"
{{< /command >}}

## Resource Browser

The LocalStack Web Application provides a Resource Browser for managing Step Functions state machines. You can access the Resource Browser by opening the LocalStack Web Application in your browser, navigating to the **Resources** section, and then clicking on **Step Functions** under the **App Integration** section.

<img src="stepfunctions-resource-browser.png" alt="Step Functions Resource Browser" title="Step Functions Resource Browser" width="900" />

The Resource Browser allows you to perform the following actions:

- **View State Machines**: View a list of all state machines you have created locally.
- **View Executions and Flow Chart**: View a list of all executions for a given state machine and the flow chart for each execution. You can also check the Execution Status, Timestamp, and Type for each execution.

## Examples

The following code snippets and sample applications provide practical examples of how to use Step Functions in LocalStack for various use cases:

- [Loan Broker application with AWS Step Functions, DynamoDB, Lambda, SQS, and SNS](https://github.com/localstack/loan-broker-stepfunctions-lambda-app)
- [Integrating Step Functions with local Lambda functions on LocalStack](https://github.com/localstack/localstack-pro-samples/tree/master/stepfunctions-lambda)
