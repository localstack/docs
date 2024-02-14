---
title: "Step Functions"
linkTitle: "Step Functions"
description: >
    Get started with Step Functions on LocalStack
---


{{< alert title="Note" >}}
A new [StepFunctions]({{< ref "user-guide/aws/lambda" >}}) implementation is now active by default since LocalStack&nbsp;3.0 (Docker `latest` since 2023-09-11).

If you experience any issues please open an issue on GitHub.
You can revert to the old behavior in the meantime by setting `PROVIDER_OVERRIDE_STEPFUNCTIONS=legacy`
{{</alert>}}

Step Functions is a serverless workflow engine that enables the orchestrating of multiple AWS services. It provides a JSON-based structured language called Amazon States Language (ASL) which allows to specify how to manage a sequence of tasks and actions that compose the application's workflow. Thus making it easier to build and maintain complex and distributed applications. Step Functions allows for the definition of both standard and express workflows for long-running and high-volume event processing.

LocalStack supports Step Functions via the Community offering, allowing you to use the Step Functions APIs in your local environment to create, execute, update, and delete state machines locally. The supported APIs are available on our [API coverage page](https://docs.localstack.cloud/references/coverage/coverage_stepfunctions/), which provides information on the extent of Step Function's integration with LocalStack.

## Getting started

This guide is designed for users new to Step Functions and assumes basic knowledge of the AWS CLI and our [`awslocal`](https://github.com/localstack/awscli-local) wrapper script.

Start your LocalStack container using your preferred method. We will demonstrate how you can create a state machine, execute it, and check the status of the execution.

### Create a state machine

You can create a state machine using the [`CreateStateMachine`](https://docs.aws.amazon.com/step-functions/latest/apireference/API_CreateStateMachine.html) API. The API requires the name of the state machine, the state machine definition, and the role ARN that the state machine will assume to call AWS services. Run the following command to create a state machine:

{{< command >}}
$ awslocal stepfunctions create-state-machine \
    --name "CreateAndListBuckets" \
    --definition '{
        "Comment": "Create bucket and list buckets",
        "StartAt": "CreateBucket",
            "States": {
            "CreateBucket": {
                "Type": "Task",
                "Resource": "arn:aws:states:::aws-sdk:s3:createBucket",
                "Parameters": {
                    "Bucket": "new-sfn-bucket"
                },
                "Next": "ListBuckets"
            },
            "ListBuckets": {
                "Type": "Task",
                "Resource": "arn:aws:states:::aws-sdk:s3:listBuckets",
                "End": true
            }
        }
    }' \
    --role-arn "arn:aws:iam::000000000000:role/stepfunctions-role"
{{< /command >}}

The output of the above command is the ARN of the state machine:

```json
{
    "stateMachineArn": "arn:aws:states:<AWS_REGION>:000000000000:stateMachine:CreateAndListBuckets",
    "creationDate": "<DATE>"
}
```

You can retrieve the details of a state machine using the [`DescribeStateMachine`](https://docs.aws.amazon.com/step-functions/latest/apireference/API_DescribeStateMachine.html) API. Run the following command to describe the state machine:

{{< command >}}
$ awslocal stepfunctions describe-state-machine --state-machine-arn "arn:aws:states:us-east-1:000000000000:stateMachine:CreateAndListBuckets"
{{< /command >}}

The output of the above command is the execution ARN:
```json
{
    "stateMachineArn": "arn:aws:states:<REGION>:000000000000:stateMachine:CreateAndListBuckets",
    "name": "CreateAndListBuckets",
    "status": "ACTIVE",
    "definition": "{\n            \"Comment\": \"Create bucket and list buckets\",\n            \"StartAt\": \"CreateBucket\",\n            \"States\": {\n                \"CreateBucket\": {\n                    \"Type\": \"Task\",\n                    \"Resource\": \"arn:aws:states:::aws-sdk:s3:createBucket\",\n                    \"Parameters\": {\n                        \"BucketName\": \"new-sfn-demo-bucket\"\n                    },\n                    \"Next\": \"ListBuckets\"\n                },\n                \"ListBuckets\": {\n                    \"Type\": \"Task\",\n                    \"Resource\": \"arn:aws:states:::aws-sdk:s3:listBuckets\",\n                    \"End\": true\n                }\n            }\n        }",
    "roleArn": "arn:aws:iam::000000000000:role/stepfunctions-role",
    "type": "STANDARD",
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
    "stateMachines": [
        {
            "stateMachineArn": "arn:aws:states:<REGION>:000000000000:stateMachine:CreateAndListBuckets",
            "name": "CreateAndListBuckets",
            "type": "STANDARD",
            "creationDate": "<DATE>"
        }
    ]
}
```

### Execute the state machine

You can execute the state machine using the [`StartExecution`](https://docs.aws.amazon.com/step-functions/latest/apireference/API_StartExecution.html) API. The API requires the state machine's ARN and the state machine's input. Run the following command to execute the state machine:

{{< command >}}
$ awslocal stepfunctions start-execution \
    --state-machine-arn "arn:aws:states:us-east-1:000000000000:stateMachine:CreateAndListBuckets"
{{< /command >}}

The output of the above command is the execution ARN:
```json
{
    "executionArn": "arn:aws:states:<REGION>:000000000000:execution:CreateAndListBuckets:<ID>",
    "startDate": "<DATE>"
}
```

### Check the execution status
To check the status of the execution, you can use the [`DescribeExecution`](https://docs.aws.amazon.com/step-functions/latest/apireference/API_DescribeExecution.html) API. Run the following command to describe the execution:

{{< command >}}
$ awslocal stepfunctions describe-execution \
        --execution-arn "arn:aws:states:<REGION>:000000000000:execution:CreateAndListBuckets:<ID>"
{{< /command >}}

The output of the above command is the execution status:

```json
{
    "executionArn": "arn:aws:states:<REGION>:000000000000:execution:CreateAndListBuckets:<ID>",
    "stateMachineArn": "arn:aws:states:<REGION>:000000000000:stateMachine:CreateAndListBuckets",
    "name": "<EXECUTION-NAME",
    "status": "SUCCEEDED",
    "startDate": "<DATE>",
    "stopDate": "<DATE>",
    "input": "{}",
    "inputDetails": {"included": true},
    "output": "{\"Buckets\":[{\"Name\":\"new-sfn-bucket\",\"CreationDate\":\"<DATE\"}],\"Owner\":{\"DisplayName\":\"webfile\",\"ID\":\"<ID>\"}}",
    "outputDetails": {"included": true}
}
```

### Update and delete the state machine

You can update the state machine definition using the [`UpdateStateMachine`](https://docs.aws.amazon.com/step-functions/latest/apireference/API_UpdateStateMachine.html) API. The API requires the ARN of the state machine and the new state machine definition. Run the following command to update the state machine definition:

{{< command >}}
$ awslocal stepfunctions update-state-machine \
     --state-machine-arn "arn:aws:states:us-east-1:000000000000:stateMachine:CreateAndListBuckets" \
     --definition file://path/to/your/statemachine.json \
     --role-arn "arn:aws:iam::000000000000:role/stepfunctions-role"
{{< /command >}}

You can delete the state machine using the [`DeleteStateMachine`](https://docs.aws.amazon.com/step-functions/latest/apireference/API_DeleteStateMachine.html) API. Run the following command to delete the state machine:

{{< command >}}
$ awslocal stepfunctions delete-state-machine \
     --state-machine-arn "arn:aws:states:us-east-1:000000000000:stateMachine:CreateAndListBuckets"
{{< /command >}}

## Resource Browser

The LocalStack Web Application provides a Resource Browser for managing Step Functions state machines. You can access the Resource Browser by opening the LocalStack Web Application in your browser, navigating to the **Resources** section, and then clicking on **Step Functions** under the **App Integration** section.

<img src="stepfunctions-resource-browser.png" alt="Step Functions Resource Browser" title="Step Functions Resource Browser" width="900" />

The Resource Browser allows you to perform the following actions:

- **View State Machines**: View a list of all state machines you have created locally.
- **View Executions and Flow Chart**: View a list of all executions for a given state machine and the flow chart for each execution. You can also check the Execution Status, Timestamp, and Type for each execution.

## Supported services and operations

Step Functions integrates with AWS services, allowing you to invoke API actions for each service within your workflow. LocalStack's Step Functions emulation supports the following AWS services:

| Supported service integrations | Service                 | Request Response | Run a Job (.sync) | Run a Job (.sync2) | Wait for Callback (.waitForTaskToken) |
|--------------------------------|-------------------------|:---:             |:---:              |:---:               |:---:                                  |
| Optimized integrations         | Lambda                  | &#10003;         |                   |                    | &#10003;                              |
|                                | DynamoDB                | &#10003;         |                   |                    |                                       |
|                                | Amazon SNS              | &#10003;         |                   |                    | &#10003;                              |
|                                | Amazon SQS              | &#10003;         |                   |                    | &#10003;                              |
|                                | API Gateway             | &#10003;         |                   |                    | &#10003;                              |
|                                | Amazon EventBridge      | &#10003;         |                   |                    | &#10003;                              |
|                                | AWS Step Functions      | &#10003;         | &#10003;          | &#10003;           | &#10003;                              |
| AWS SDK integrations           | All LocalStack services | &#10003;         |                   |                    | &#10003;                              |

## Examples

The following code snippets and sample applications provide practical examples of how to use Step Functions in LocalStack for various use cases:

- [Loan Broker application with AWS Step Functions, DynamoDB, Lambda, SQS, and SNS](https://github.com/localstack/loan-broker-stepfunctions-lambda-app)
- [Integrating Step Functions with local Lambda functions on LocalStack](https://github.com/localstack/localstack-pro-samples/tree/master/stepfunctions-lambda)
