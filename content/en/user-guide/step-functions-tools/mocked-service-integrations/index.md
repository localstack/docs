---
title: "Mocked Service Integrations"
weight: 2
description: >
  Attach a debugger to your Lambda functions from within your IDE
aliases:
  - /tools/step-functions-tools/mocked-service-integrations/
  - /user-guide/tools/step-functions-tools/mocked-service-integrations/
---

# Introduction

Mocked service integrations eliminate the need to deploy or invoke real AWS services during Step Functions testing.
Instead, each Task state returns a predefined output supplied through a mock configuration file.
The file lists one or more test cases per state machine, with a set of mocked responses mapped to individual states.
When a state machine is executed in mock mode, the runtime simply samples the specified responses, substituting them for calls to the actual integrated resources.
States without a corresponding mock entry continue to invoke their real services, allowing selective mixing of mocked and live interactions within the same execution.

The following definitions clarify key concepts used throughout this section:
- Mocked service integrations – Task states that are instructed to return predefined data instead of making live AWS calls.
- Mocked responses – The static payloads supplied to those Task states.
- Test cases – Individual state-machine runs that are executed with mocked service integrations enabled.
- Mock configuration file – A JSON document that declares the test cases, their mocked integrations, and the response data used for each state.

## Mocking service integrations

When mocked service integrations are enabled for specific Task states, one or more response payloads can be declared for each state.
During execution, the LocalStack runtime returns these payloads instead of calling the live AWS service.
Any Task state—using patterns such as .sync, .sync2, or .waitForTaskToken—can be mocked, and both success or failure scenarios can be reproduced.
Payload correctness is not validated by the tool, so it is up to the developer to supply responses that match the service’s expected structure.

### 1. Identify a State Machine to Configure with Mocked Integrations

Mocked service integrations are bound to specific state machine definitions.
Therefore, the first step is to choose the state machine where mocked responses will be applied.
LocalStack supports the latest AWS Step Functions features, including [JSONata expressions and Variables](https://blog.localstack.cloud/aws-step-functions-made-easy/).
In this example, the state machine LambdaSQSIntegration will be used with the following definition:

```json
{
  "Comment":"This state machine is called: LambdaSQSIntegration",
  "QueryLanguage":"JSONata",
  "StartAt":"LambdaState",
  "States":{
    "LambdaState":{
      "Type":"Task",
      "Resource":"arn:aws:states:::lambda:invoke",
      "Arguments":{
        "FunctionName":"GreetingsFunction",
        "Payload":{
          "fullname":"{% $states.input.name & ' ' & $states.input.surname %}"
        }
      },
      "Retry":[
        {
          "ErrorEquals":[ "States.ALL" ],
          "IntervalSeconds":2,
          "MaxAttempts": 4,
          "BackoffRate":2
        }
      ],
      "Assign":{
        "greeting":"{% $states.result.Payload.greeting %}"
      },
      "Next":"SQSState"
    },
    "SQSState":{
      "Type":"Task",
      "Resource":"arn:aws:states:::sqs:sendMessage",
      "Arguments":{
        "QueueUrl":"http://sqs.us-east-1.localhost.localstack.cloud:4566/000000000000/localstack-queue",
        "MessageBody":"{% $greeting %}"
      },
      "End":true
    }
  }
}
```

### 2. Define mock integrations in a configuration file

Mock integrations are declared in a single mock configuration file written in JSON.
The file must conform to the RawMockConfig schema shown above and is organised into two top-level sections:

- StateMachines - maps each state machine name to the test scenarios that will run against it.
- MockedResponses - holds the reusable response sets that the test scenarios reference.


#### 2.1 StateMachines
The StateMachines section defines which Step Functions state machines will use mocked service integrations and how their test cases are configured.
Each entry under StateMachines corresponds to a specific state machine and contains one or more named test cases that specify how the states within that machine should behave during execution.

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

- StateMachineName – The exact name of the Step Functions state machine.
This must match the name used when the state machine is created in LocalStack.
- TestCases – A set of named test scenarios.
Each test case maps one or more state names to a predefined ResponseID from the MockedResponses section.

Each test case defines the expected behavior of specific Task states by assigning them to mock response sets.
When the test case is selected at runtime, these bindings determine whether the state uses a mocked response or proceeds with a real service invocation (if no mock is provided).

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

#### 2.2 MockedResponses
The MockedResponses section defines reusable response sets that simulate the behavior of specific Task states during test execution.
Each response set is identified by a unique ResponseID, which is then referenced in one or more test cases under the StateMachines section.

```json
"MockedResponses": {
  "<ResponseID>": {
    "<step-key>": { "Return": ... },
    "<step-key>": { "Throw": ... }
  }
}
```

- ResponseID – A unique identifier for a set of mocked responses.
These IDs are used in test cases to associate a state with its corresponding mocked behavior.
- step-key – Defines which execution attempt the response applies to.
It can be:
 - A single integer, e.g., "0" – applied on the first attempt.
 - A range of integers, e.g., "1-5" – applied to multiple attempts.
- Steps are evaluated in sequential order, allowing simulation of retries or failures followed by success.
 - Return – Defines a successful response payload to be returned by the state instead of invoking the actual integrated service.
 - Throw – Defines an error response with required fields Error and Cause, simulating a failure.
 - Each response entry must contain exactly one of Return or Throw.
 Including both or neither will result in an invalid configuration.

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

The MockConfigFile.json shown below targets the previously defined LambdaSQSIntegration state machine for testing:

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

### 3. Provide the Mock Configuration to LocalStack

The `SFN_MOCK_CONFIG` environment variable specifies the path to the mock-configuration file.
When starting LocalStack in Docker, set this variable and mount the configuration file, e.g., MockConfigFile.json—as shown in the following examples.
{{< tabpane >}}
{{< tab header="LocalStack CLI" lang="shell" >}}
LOCALSTACK_SFN_MOCK_CONFIG=/tmp/MockConfigFile.json \
localstack start --volume /path/to/MockConfigFile.json:/tmp/MockConfigFile.json
{{< /tab >}}
{{< tab header="Docker Compose" lang="yaml" >}}
services:
  localstack:
    container_name: "${LOCALSTACK_DOCKER_NAME:-localstack-main}"
    image: localstack/localstack-pro
    ports:
      - "127.0.0.1:4566:4566"            # LocalStack Gateway
      - "127.0.0.1:4510-4559:4510-4559"  # external services port range
      - "127.0.0.1:443:443"              # LocalStack HTTPS Gateway (Pro)
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


### 4. Run Tests Cases with Mocked Integrations

#### 4.1 Create the State Machine
The first step is to create the state machine for testing.
The name of the state machine must match the name defined in the mock configuration file.
Continuing from the example introduced earlier in this article, the state machine named LambdaSQSIntegration can be created with the following command:

{{< command >}}
$ awslocal stepfunctions create-state-machine \
    --definition file://LambdaSQSIntegration.json \
    --name "LambdaSQSIntegration" \
    --role-arn "arn:aws:iam::000000000000:role/service-role/testrole"
{{< /command >}}


#### 4.2 Start the Mock Test
Once the state machine is created and correctly named, test cases defined in the mock configuration file can be executed using the StartExecution or StartSyncExecution API.
To specify a test case, append the test case name to the state machine ARN using the # symbol.
For example, to run the BaseCase test case for the `LambdaSQSIntegration` state machine:

{{< command >}}
$ awslocal stepfunctions start-execution \
    --state-machine arn:aws:states:ca-central-1:000000000000:stateMachine:LambdaSQSIntegration#BaseCase \
    --input '{"name": "John", "surname": "smith"}' \
    --name "MockExecutionBaseCase"
{{< /command >}}
During execution, the state machine uses the mocked responses defined in the mock configuration file for each state.
If no mocked response is specified for a given state, the associated service integration will be invoked as normal.

#### 4.3 Inspect the Execution
After a mock test case is initiated, the state machine execution behaves like a standard execution and can be monitored using API actions such as `GetExecutionHistory` and `DescribeExecution`.
Continuing from the previous example, the execution can be described with the following command:
{{< command >}}
$ awslocal stepfunctions describe-execution \
    --execution-arn "arn:aws:states:ca-central-1:000000000000:execution:LambdaSQSIntegration:MockExecutionBaseCase"
{{< /command >}}
The response will include the output defined in the mock configuration file for `SQSState`, in this case corresponding to `MockedSQSStateSuccess`.

```json
{
    "executionArn": "arn:aws:states:ca-central-1:000000000000:execution:LambdaSQSIntegration:MockExecutionBaseCase",
    "stateMachineArn": "arn:aws:states:ca-central-1:000000000000:stateMachine:LambdaSQSIntegration",
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

The execution history can also be retrieved using the following command:
{{< command >}}
$ awslocal stepfunctions get-execution-history \
    --execution-arn "arn:aws:states:ca-central-1:000000000000:execution:LambdaSQSIntegration:MockExecutionBaseCase"
{{< /command >}}

This returns the full execution history, including entries that indicate how the mocked responses were applied to the Lambda and SQS states.
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
