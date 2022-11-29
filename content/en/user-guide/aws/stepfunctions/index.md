---
title: "Step Functions"
linkTitle: "Step Functions"
categories: ["LocalStack Community"]
description: Get started with AWS Step Functions on LocalStack
aliases:
  - /aws/stepfunctions/
---

Amazon Web Services (AWS) Step Functions is a serverless workflow engine that integrates with AWS Lambda and other AWS services. It allows us to define workflows using Amazon States Language, a JSON-based structured language, to provide the necessary configurations and run the workflow. Step Functions allow you to define standard workflows and express workflows for long-running workflows and high-volume event processing, respectively.

LocalStack provides Step Functions support via the Community offering. You can use the Step Functions API to create, execute, update, and delete state machines. The supported APIs are available over our [feature coverage page]({{< ref "feature-coverage" >}}).

## Getting started

In this getting started guide, you'll learn how to make basic usage of Step Functions in LocalStack. This guide is intended for users who wish to get more acquainted with Step Functions, and assumes you have basic knowledge of the AWS CLI (and our [`awslocal`](https://github.com/localstack/awscli-local) wrapper script). First, start your LocalStack instance using your preferred method, then run the following commands:

1. Create a state machine using the `create-state-machine` command and specify the name of the state machine, the state machine definition, and the role ARN that the state machine will assume to call AWS services:
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
   In the above example, we have created a state machine named `WaitMachine`, with a single state, `WaitExecution`, which waits for 10 seconds before completing the execution. The role ARN is used to grant the state machine access to other AWS services, and you can create an IAM role within LocalStack as well. The output of the above command is the ARN of the state machine:
   ```json
   {
    "stateMachineArn": "arn:aws:states:<AWS_REGION>:000000000000:stateMachine:WaitMachine",
    "creationDate": "<DATE>"
   }
   ```

2. You can list the state machines in your account by running the following command:
   {{< command >}}
   $ awslocal stepfunctions list-state-machines
   {{< /command >}}
   The output of the above command is a list of state machines:
   ```json
   {
    "stateMachines": [
        {
        "stateMachineArn": "arn:aws:states:<AWS_REGION>:000000000000:stateMachine:WaitMachine",
        "name": "WaitMachine",
        "type": "STANDARD",
        "creationDate": "<DATE>"
        }
    ]
   }
   ```

3. You can retrieve the state machine using the ARN returned in the first step, via the `list-state-machines` command:
   {{< command >}}
   $ awslocal stepfunctions describe-state-machine --state-machine-arn "arn:aws:states:<AWS_REGION>:000000000000:stateMachine:WaitExecution"
   {{< /command >}}
   The output of the above command is the state machine definition:
   ```json
   {
        "stateMachineArn": "arn:aws:states:us-east-1:000000000000:stateMachine:WaitMachine",
        "name": "WaitMachine",
        "status": "ACTIVE",
        "definition": "{\n        \"StartAt\": \"WaitExecution\",\n        \"States\": {\n            \"WaitExecution\": {\n            \"Type\": \"Wait\",\n            \"Seconds\": 10,\n            \"End\": true\n            }\n        }\n        }",
        "roleArn": "arn:aws:iam::000000000000:role/stepfunctions-role",
        "type": "STANDARD",
        "creationDate": "<DATE>"
        "loggingConfiguration": {
            "level": "OFF",
            "includeExecutionData": false
        }
   }
   ```

4. You can next execute the state machine using the `start-execution` command:
   {{< command >}}
   $ awslocal stepfunctions start-execution \
        --state-machine-arn "arn:aws:states:<REGION>:000000000000:stateMachine:WaitMachine"
   {{< /command >}}
   The output of the above command is the execution ARN:
   ```json
   {
        "executionArn": "arn:aws:states:us-east-1:000000000000:execution:WaitMachine:<ID>",
        "startDate": "<DATE>"
   }
   ```

5. To check the status of the execution, you can use the `describe-execution` command:
   {{< command >}}
   $ awslocal stepfunctions describe-execution \
        --execution-arn "arn:aws:states:us-east-1:000000000000:execution:WaitMachine:<ID>"
   {{< /command >}}
   The output of the above command is the execution status:
   ```json
   {
        "executionArn": "arn:aws:states:us-east-1:000000000000:execution:WaitMachine:32174130-4587-4314-ad63-86c6242523b2",
        "stateMachineArn": "arn:aws:states:us-east-1:000000000000:stateMachine:WaitMachine",
        "name": "<NAME>",
        "status": "SUCCEEDED",
        "startDate": "<START_DATE>",
        "stopDate": "<STOP_DATE>",
        "input": "{}",
        "inputDetails": {
            "included": true
        },
        "output": "{}",
        "outputDetails": {
            "included": true
        }
   }
   ```

6. To update the state machine definition, you can use the `update-state-machine` command:
   {{< command >}}
   $ awslocal stepfunctions update-state-machine \
        --state-machine-arn "arn:aws:states:<REGION>:000000000000:stateMachine:WaitMachine" \
        --definition file://path/to/your/statemachine.json
        --role-arn "arn:aws:iam::000000000000:role/stepfunctions-role"
   {{< /command >}}

7. To delete the state machine, you can use the `delete-state-machine` command:
   {{< command >}}
   $ awslocal stepfunctions delete-state-machine \
        --state-machine-arn "arn:aws:states:<REGION>:000000000000:stateMachine:WaitMachine"
   {{< /command >}}

For an extensive list of supported Step Functions APIs, please refer to the [official AWS documentation](https://docs.aws.amazon.com/step-functions/latest/dg/welcome.html), and the [CLI reference](https://docs.aws.amazon.com/cli/latest/reference/stepfunctions/index.html).

## Using LocalStack Pro

LocalStack Pro users can access our [LocalStack App's](https://app.localstack.cloud) web user interface to work with Step Functions and other AWS services. It is a convenient way to work with Step Functions and allows you to check the executions and flowcharts in a fashion similar to the AWS console. While using the LocalStack App, ensure you have the LocalStack instance running. You can also navigate across previous events and executions and view the state machine statuses.
