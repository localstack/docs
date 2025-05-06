---
title: "Step Functions"
linkTitle: "Step Functions"
description: >
    Get started with Step Functions on LocalStack
---

## Introduction

Step Functions is a serverless workflow engine that enables the orchestrating of multiple AWS services.
It provides a JSON-based structured language called Amazon States Language (ASL) which allows to specify how to manage a sequence of tasks and actions that compose the application's workflow.
Thus making it easier to build and maintain complex and distributed applications.

LocalStack allows you to use the Step Functions APIs in your local environment to create, execute, update, and delete state machines locally.
The supported APIs are available on our [API coverage page](https://docs.localstack.cloud/references/coverage/coverage_stepfunctions/), which provides information on the extent of Step Function's integration with LocalStack.

## Getting started

This guide is designed for users new to Step Functions and assumes basic knowledge of the AWS CLI and our [`awslocal`](https://github.com/localstack/awscli-local) wrapper script.

Start your LocalStack container using your preferred method.
We will demonstrate how you can create a state machine, execute it, and check the status of the execution.

### Create a state machine

You can create a state machine using the [`CreateStateMachine`](https://docs.aws.amazon.com/step-functions/latest/apireference/API_CreateStateMachine.html) API.
The API requires the name of the state machine, the state machine definition, and the role ARN that the state machine will assume to call AWS services.
Run the following command to create a state machine:

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
    "stateMachineArn": "arn:aws:states:us-east-1:000000000000:stateMachine:CreateAndListBuckets",
    "creationDate": 1714643996.18017
}
```

### Execute the state machine

You can execute the state machine using the [`StartExecution`](https://docs.aws.amazon.com/step-functions/latest/apireference/API_StartExecution.html) API.
The API requires the state machine's ARN and the state machine's input.
Run the following command to execute the state machine:

{{< command >}}
$ awslocal stepfunctions start-execution \
    --state-machine-arn "arn:aws:states:us-east-1:000000000000:stateMachine:CreateAndListBuckets"
{{< /command >}}

The output of the above command is the execution ARN:

```json
{
    "executionArn": "arn:aws:states:us-east-1:000000000000:execution:CreateAndListBuckets:bf7d2138-e96f-42d1-b1f9-41f0c1c7bc3e",
    "startDate": 1714644089.748442
}
```

### Check the execution status

To check the status of the execution, you can use the [`DescribeExecution`](https://docs.aws.amazon.com/step-functions/latest/apireference/API_DescribeExecution.html) API.
Run the following command to describe the execution:

{{< command >}}
$ awslocal stepfunctions describe-execution \
        --execution-arn "arn:aws:states:us-east-1:000000000000:execution:CreateAndListBuckets:bf7d2138-e96f-42d1-b1f9-41f0c1c7bc3e"
{{< /command >}}

Replace the `execution-arn` with the ARN of the execution you want to describe.

The output of the above command is the execution status:

```json
{
    "executionArn": "arn:aws:states:us-east-1:000000000000:execution:CreateAndListBuckets:bf7d2138-e96f-42d1-b1f9-41f0c1c7bc3e",
    "stateMachineArn": "arn:aws:states:us-east-1:000000000000:stateMachine:CreateAndListBuckets",
    "name": "bf7d2138-e96f-42d1-b1f9-41f0c1c7bc3e",
    "status": "SUCCEEDED",
    "startDate": 1714644089.748442,
    "stopDate": 1714644089.907964,
    "input": "{}",
    "inputDetails": {
        "included": true
    },
    "output": "{\"Buckets\":[{\"Name\":\"cdk-hnb659fds-assets-000000000000-us-east-1\",\"CreationDate\":\"2024-05-02T09:53:54+00:00\"},{\"Name\":\"new-sfn-bucket\",\"CreationDate\":\"2024-05-02T10:01:29+00:00\"}],\"Owner\":{\"DisplayName\":\"webfile\",\"Id\":\"75aa57f09aa0c8caeab4f8c24e99d10f8e7faeebf76c078efc7c6caea54ba06a\"}}",
    "outputDetails": {
        "included": true
    }
}
```

## Supported services and operations

Step Functions integrates with AWS services, allowing you to invoke API actions for each service within your workflow.
LocalStack's Step Functions emulation supports the following AWS services:

| Supported service integrations | Service                 | Request Response | Run a Job (.sync) | Run a Job (.sync2) | Wait for Callback (.waitForTaskToken) |
|--------------------------------|-------------------------|:---:             |:---:              |:---:               |:---:                                  |
| Optimized integrations         | Lambda                  | &#10003;         |                   |                    | &#10003;                              |
|                                | DynamoDB                | &#10003;         |                   |                    |                                       |
|                                | Amazon ECS/AWS Fargate  | &#10003;         | &#10003;          |                    | &#10003;                              |
|                                | Amazon SNS              | &#10003;         |                   |                    | &#10003;                              |
|                                | Amazon SQS              | &#10003;         |                   |                    | &#10003;                              |
|                                | API Gateway             | &#10003;         |                   |                    | &#10003;                              |
|                                | Amazon EventBridge      | &#10003;         |                   |                    | &#10003;                              |
|                                | AWS Glue                | &#10003;         | &#10003;          |                    |                                       |
|                                | AWS Step Functions      | &#10003;         | &#10003;          | &#10003;           | &#10003;                              |
|          | AWS Batch            | &#10003;         | &#10003;          |                    |                                   |
| AWS SDK integrations           | All LocalStack services | &#10003;         |                   |                    | &#10003;                              |

## Mocked Service Integrations

Mocked service integrations allow you to test AWS Step Functions without calling LocalStack's emulated AWS services.
Instead, Task states return predefined outputs from a mock configuration file.
The key components are:

- **Mocked service integrations**: Task states that return predefined responses instead of invoking local AWS services.
- **Mocked responses**: Static payloads associated with mocked Task states.
- **Test cases**: State machine executions using mocked responses.
- **Mock configuration file**: JSON file that defines test cases, mocked states, and their response payloads.

During execution, each Task state defined in the mock file returns its corresponding mocked response.
States not listed continue to invoke their real emulated services, allowing a mix of mocked and live interactions.

You can provide one or more mocked payloads per Task state.
The Supported patterns include `.sync`, `.sync2`, and `.waitForTaskToken`.
Both success and failure scenarios can be simulated.

### Compatibility with AWS Step Functions Local

LocalStack can also serve as a drop-in replacement for [AWS Step Functions Local testing with mocked service integrations](https://docs.aws.amazon.com/step-functions/latest/dg/sfn-local-test-sm-exec.html).
It supports test cases with mocked Task states and maintains compatibility with existing Step Functions Local configurations.
This functionality is extended in LocalStack by providing access to the latest Step Functions features such as [JSONata and Variables](https://blog.localstack.cloud/aws-step-functions-made-easy/), as well as the ability to enable both mocked and emulated service interactions emulated by LocalStack.

{{< callout >}}
LocalStack does not validate response formats.
Ensure the payload structure in the mocked responses matches what the real service expects.
{{< /callout >}}

### Identify a State Machine for Mocked Integrations

Mocked service integrations apply to specific state machine definitions.  
The first step is to select the state machine where mocked responses will be used.  

In this example, the state machine with the name `LambdaSQSIntegration` state machine will be used with the following definition:

```json
{
  "Comment": "This state machine is called: LambdaSQSIntegration",
  "QueryLanguage": "JSONata",
  "StartAt": "LambdaState",
  "States": {
    "LambdaState": {
      "Type": "Task",
      "Resource": "arn:aws:states:::lambda:invoke",
      "Arguments": {
        "FunctionName": "GreetingsFunction",
        "Payload": {
          "fullname": "{% $states.input.name & ' ' & $states.input.surname %}"
        }
      },
      "Retry": [
        {
          "ErrorEquals": [ "States.ALL" ],
          "IntervalSeconds": 2,
          "MaxAttempts": 4,
          "BackoffRate": 2
        }
      ],
      "Assign": {
        "greeting": "{% $states.result.Payload.greeting %}"
      },
      "Next": "SQSState"
    },
    "SQSState": {
      "Type": "Task",
      "Resource": "arn:aws:states:::sqs:sendMessage",
      "Arguments": {
        "QueueUrl": "http://sqs.us-east-1.localhost.localstack.cloud:4566/000000000000/localstack-queue",
        "MessageBody": "{% $greeting %}"
      },
      "End": true
    }
  }
}
```

### Define Mock Integrations in a Configuration File

Mock integrations are defined in a JSON file with two top-level section:

- **StateMachines** – Maps each state machine to its test cases, specifying which states use which mocked responses.
- **MockedResponses** – Defines reusable mock payloads identified by `ResponseID`, which test cases refer to.

#### `StateMachines`

This section specifies the Step Functions state machines to mock and their test cases.  
Each test case maps state names to response IDs defined in `MockedResponses`.

```json
"StateMachines": {
  "<StateMachineName>": {
    "TestCases": {
      "<TestCaseName>": {
        "<StateName>": "<ResponseID>",
        ...
      }
    }
  }
}
```

In the example above:

- `StateMachineName`: Must match the exact name used during creation in LocalStack.
- `TestCases`: Named scenarios that define mocked behavior for individual states.

Each test case maps Task states to mock responses that define expected behavior.  
At runtime, if a test case is selected, the state uses the mock response if defined; otherwise, it calls the emulated service.

Here is a full example of the `StateMachines` section:

```json
"LambdaSQSIntegration": {
  "TestCases": {
    "LambdaRetryCase": {
      "LambdaState": "MockedLambdaStateRetry",
      "SQSState":   "MockedSQSStateSuccess"
    }
  }
}
```

#### `MockedResponses`

This section defines mocked responses for Task states.  
Each `ResponseID` contains one or more step keys and either a `Return` or `Throw`.

```json
"MockedResponses": {
  "<ResponseID>": {
    "<step-key>": { "Return": ... },
    "<step-key>": { "Throw": ... }
  }
}
```

In the example above:

- `ResponseID`: Unique identifier referenced in test cases.
- `step-key`: Indicates the attempt (e.g., `"0"` for first try, `"1-2"` for a range).
- `Return`: Simulates success with a response payload.
- `Throw`: Simulates failure with `Error` and `Cause`.

{{< callout >}}
Each entry must have **either** `Return` or `Throw`, but cannot have both.
{{< /callout >}}

Here is a full example of the `MockedResponses` section:

```json
"MockedLambdaStateRetry": {
  "0": {
    "Throw": {
      "Error": "Lambda.ServiceException",
      "Cause": "An internal service error occurred."
    }
  },
  "1-2": {
    "Throw": {
      "Error": "Lambda.TooManyRequestsException",
      "Cause": "Invocation rate limit exceeded."
    }
  },
  "3": {
    "Return": {
      "StatusCode": 200,
      "Payload": {
        "greeting": "Hello John Smith, you’re now testing mocked integrations with LocalStack!"
      }
    }
  }
}
```

The `MockConfigFile.json` below is used to test the `LambdaSQSIntegration` state machine defined earlier.

```json
{
  "StateMachines":{
    "LambdaSQSIntegration":{
      "TestCases":{
        "BaseCase":{
          "LambdaState":"MockedLambdaStateSuccess",
          "SQSState":"MockedSQSStateSuccess"
        },
        "LambdaRetryCase":{
          "LambdaState":"MockedLambdaStateRetry",
          "SQSState":"MockedSQSStateSuccess"
        },
        "HybridCase":{
          "LambdaState":"MockedLambdaSuccess"
        }
      }
    }
  },
  "MockedResponses":{
    "MockedLambdaStateSuccess":{
      "0":{
        "Return":{
          "StatusCode":200,
          "Payload":{
            "greeting":"Hello John Smith, you’re now testing mocked integrations with LocalStack!"
          }
        }
      }
    },
    "MockedSQSStateSuccess":{
      "0":{
        "Return":{
          "MD5OfMessageBody":"3661896f-1287-45a3-8f89-53bd7b25a9a6",
          "MessageId":"7c9ef661-c455-4779-a9c2-278531e231c2"
        }
      }
    },
    "MockedLambdaStateRetry":{
      "0":{
        "Throw":{
          "Error":"Lambda.ServiceException",
          "Cause":"An internal service error occurred."
        }
      },
      "1-2":{
        "Throw":{
          "Error":"Lambda.TooManyRequestsException",
          "Cause":"Invocation rate limit exceeded."
        }
      },
      "3":{
        "Return":{
          "StatusCode":200,
          "Payload":{
            "greeting":"Hello John Smith, you’re now testing mocked integrations with LocalStack!"
          }
        }
      }
    }
  }
}
```

### Provide the Mock Configuration to LocalStack

Set the `SFN_MOCK_CONFIG` configuration variable to the path of the mock configuration file.  
When running LocalStack in Docker, mount the file and pass the variable as shown below:

{{< tabpane >}}
{{< tab header="LocalStack CLI" lang="shell" >}}
LOCALSTACK_SFN_MOCK_CONFIG=/tmp/MockConfigFile.json \
localstack start --volume /path/to/MockConfigFile.json:/tmp/MockConfigFile.json
{{< /tab >}}
{{< tab header="Docker Compose" lang="yaml" >}}
services:
  localstack:
    container_name: "${LOCALSTACK_DOCKER_NAME:-localstack-main}"
    image: localstack/localstack
    ports:
      - "127.0.0.1:4566:4566"            # LocalStack Gateway
      - "127.0.0.1:4510-4559:4510-4559"  # external services port range
    environment:
      # LocalStack configuration: https://docs.localstack.cloud/references/configuration/
      - DEBUG=${DEBUG:-0}
      - SFN_MOCK_CONFIG=/tmp/MockConfigFile.json
    volumes:
      - "${LOCALSTACK_VOLUME_DIR:-./volume}:/var/lib/localstack"
      - "/var/run/docker.sock:/var/run/docker.sock"
      - "./MockConfigFile.json:/tmp/MockConfigFile.json"
{{< /tab >}}
{{< /tabpane >}}

### Run Test Cases with Mocked Integrations

Create the state machine to match the name defined in the mock configuration file.  
In this example, create the `LambdaSQSIntegration` state machine using:

{{< command >}}
$ awslocal stepfunctions create-state-machine \
    --definition file://LambdaSQSIntegration.json \
    --name "LambdaSQSIntegration" \
    --role-arn "arn:aws:iam::000000000000:role/service-role/testrole"
{{< /command >}}

After the state machine is created and named correctly, test cases from the mock configuration file can be run using the [`StartExecution`](https://docs.aws.amazon.com/step-functions/latest/apireference/API_StartExecution.html) API.

To execute a test case, append the test case name to the state machine ARN using `#`.
This tells LocalStack to apply the mocked responses from the configuration file.
For example, run the `BaseCase` test case:

{{< command >}}
$ awslocal stepfunctions start-execution \
    --state-machine arn:aws:states:us-east-1:000000000000:stateMachine:LambdaSQSIntegration#BaseCase \
    --input '{"name": "John", "surname": "smith"}' \
    --name "MockExecutionBaseCase"
{{< /command >}}

During execution, any state mapped in the mock config will use the predefined response.  
States without mock entries invoke the actual emulated service as usual.

You can inspect the execution using the [`DescribeExecution`](https://docs.aws.amazon.com/step-functions/latest/apireference/API_DescribeExecution.html) API:

{{< command >}}
$ awslocal stepfunctions describe-execution \
    --execution-arn "arn:aws:states:us-east-1:000000000000:execution:LambdaSQSIntegration:MockExecutionBaseCase"
{{< /command >}}

The sample output shows the execution details, including the state machine ARN, execution ARN, status, start and stop dates, input, and output:

```json
{
    "executionArn": "arn:aws:states:us-east-1:000000000000:execution:LambdaSQSIntegration:MockExecutionBaseCase",
    "stateMachineArn": "arn:aws:states:us-east-1:000000000000:stateMachine:LambdaSQSIntegration",
    "name": "MockExecutionBaseCase",
    "status": "SUCCEEDED",
    "startDate": "...",
    "stopDate": "...",
    "input": "{\"name\":\"John\",\"surname\":\"smith\"}",
    "inputDetails": {
        "included": true
    },
    "output": "{\"MessageId\":\"7c9ef661-c455-4779-a9c2-278531e231c2\",\"MD5OfMessageBody\":\"3661896f-1287-45a3-8f89-53bd7b25a9a6\"}",
    "outputDetails": {
        "included": true
    }
}
```

You can also use the [`GetExecutionHistory`](https://docs.aws.amazon.com/step-functions/latest/apireference/API_GetExecutionHistory.html) API to retrieve the execution history, including the events and their details.

{{< command >}}
$ awslocal stepfunctions get-execution-history \
    --execution-arn "arn:aws:states:us-east-1:000000000000:execution:LambdaSQSIntegration:MockExecutionBaseCase"
{{< /command >}}

This will return the full execution history, including entries that indicate how the mocked responses were applied to the Lambda and SQS states.

```json
...
{
    "timestamp": "...",
    "type": "TaskSucceeded",
    "id": 5,
    "previousEventId": 4,
    "taskSucceededEventDetails": {
        "resourceType": "lambda",
        "resource": "invoke",
        "output": "{\"StatusCode\": 200, \"Payload\": {\"greeting\": \"Hello John Smith, you\\u2019re now testing mocked integrations with LocalStack!\"}}",
        "outputDetails": {
            "truncated": false
        }
    }
}
...
{
    "timestamp": "...",
    "type": "TaskSucceeded",
    "id": 10,
    "previousEventId": 9,
    "taskSucceededEventDetails": {
        "resourceType": "sqs",
        "resource": "sendMessage",
        "output": "{\"MessageId\": \"7c9ef661-c455-4779-a9c2-278531e231c2\", \"MD5OfMessageBody\": \"3661896f-1287-45a3-8f89-53bd7b25a9a6\"}",
        "outputDetails": {
            "truncated": false
        }
    }
}
...
```

## Resource Browser

The LocalStack Web Application provides a Resource Browser for managing Step Functions state machines.
You can access the Resource Browser by opening the LocalStack Web Application in your browser, navigating to the **Resource Browser** section, and then clicking on **Step Functions** under the **App Integration** section.

<img src="stepfunctions-resource-browser.png" alt="Step Functions Resource Browser" title="Step Functions Resource Browser" width="900" />
<br>
<br>

The Resource Browser allows you to perform the following actions:

- **Create state machine**: Create a new state machine by clicking on the **Create state machine** button and providing the required information.
- **View state machine details**: Click on a state machine to view its details, including the state executions, definition details, such as the schema and flowchart, and the state machine's ARN.
- **Start execution**: Start a new execution of the state machine by clicking on the **Start Execution** button and providing the input data.
- **Delete state machine**: Delete a state machine by selecting it and clicking on the **Actions** button followed by **Remove Selected** button.

## Examples

The following code snippets and sample applications provide practical examples of how to use Step Functions in LocalStack for various use cases:

- [Loan Broker application with AWS Step Functions, DynamoDB, Lambda, SQS, and SNS](https://github.com/localstack/loan-broker-stepfunctions-lambda-app)
- [Integrating Step Functions with local Lambda functions on LocalStack](https://github.com/localstack/localstack-pro-samples/tree/master/stepfunctions-lambda)
