---
title: "Python"
weight: 1
description: Use the LocalStack SDK for Python
---

## Introduction

You can use the LocalStack SDK for Python to develop Python applications that interact with the LocalStack platform and internal developer endpoints.
The SDK extends the REST API, offering an object-oriented interface for easier use.

The LocalStack SDK for Python supports these features:

- Save, list, load, and delete Cloud Pods.
- Manage fault configurations for the Chaos API.
- Automatically reset service states.
- List SQS queue messages without causing side effects.
- Retrieve and delete sent SES messages.

{{< callout >}}
This SDK is still in a preview phase, and will be subject to fast and breaking changes.
{{< /callout >}}

## Installation

Install the latest `localstack-sdk-python` release via pip:

{{< command >}}
$ pip install --upgrade localstack-sdk-python
{{< / command >}}

## Basic Concepts

LocalStack SDK for Python organizes functionality into specific modules like `aws`, `state`, `pods`, and `chaos`.
For example, the `aws` module allows developers to initialize clients for various AWS services.
Using the SDK in Python is straightforward: developers can import the relevant modules and initialize specific clients (e.g., `AWSClient`, `StateClient`, `PodsClient`, `ChaosClient`) to perform actions on local AWS services.

### AWS endpoints

#### SQS

The following code snippet shows how to set up an SQS client, create a queue, send messages, and retrieve them to test local SQS interactions using LocalStack.

```python
import json
import boto3
import localstack.sdk.aws

# Initialize LocalStack AWS client
client = localstack.sdk.aws.AWSClient()

# Set up SQS client using the LocalStack AWS client configuration
sqs_client = boto3.client(
    "sqs",
    endpoint_url=client.configuration.host,
    region_name="us-east-1",
    aws_access_key_id="test",
    aws_secret_access_key="test",
)

# Create an SQS queue
queue_name = "test-queue"
sqs_client.create_queue(QueueName=queue_name)
queue_url = sqs_client.get_queue_url(QueueName=queue_name)["QueueUrl"]

# Send messages to the queue
for i in range(5):
    sqs_client.send_message(
        QueueUrl=queue_url,
        MessageBody=json.dumps(
            {"event": f"event-{i}", "message": f"message-{i}"}
        ),
    )

# Retrieve messages from the queue
response = sqs_client.receive_message(
    QueueUrl=queue_url,
    MaxNumberOfMessages=5
)

# Print each message body
messages = response.get("Messages", [])
for msg in messages:
    print("Message Body:", msg.get("Body"))
```

The following output is displayed:

```bash
Message Body: {"event": "event-0", "message": "message-0"}
Message Body: {"event": "event-1", "message": "message-1"}
Message Body: {"event": "event-2", "message": "message-2"}
Message Body: {"event": "event-3", "message": "message-3"}
Message Body: {"event": "event-4", "message": "message-4"}
```

#### SES

The following code snippet verifies an email address, sends a raw email, retrieves the message ID, and discards all SES messages afterward.

```python
import boto3
import localstack.sdk.aws

client = localstack.sdk.aws.AWSClient()

# Initialize SES client
ses_client = boto3.client(
    "ses",
    endpoint_url=client.configuration.host,
    region_name="us-east-1",
    aws_access_key_id="test",
    aws_secret_access_key="test",
)

# Verify email address
email = "user@example.com"
ses_client.verify_email_address(EmailAddress=email)

# Send a raw email
raw_message_data = f"From: {email}\nTo: recipient@example.com\nSubject: test\n\nThis is the message body.\n\n"
ses_client.send_raw_email(RawMessage={"Data": raw_message_data})

# Get and print SES message IDs
messages = client.get_ses_messages()
for msg in messages:
    print("Message ID:", msg.id)

# Discard all SES messages
client.discard_ses_messages()
```

The following output is displayed:

```bash
Message ID: khqzljuixhpnpejl-mnlhgajk-ebch-zfxq-orit-qgexxjlrkipo-ywgvwr
```

### State Management

LocalStack provides various features for managing local state, including Cloud Pods, which allow for saving, loading, and deleting cloud states.

### Cloud Pods

Cloud Pods is a feature that enables storing and managing snapshots of the current state.
This code snippet shows listing available pods, saving a new pod, loading it, and then deleting it.
You need to set your `LOCALSTACK_AUTH_TOKEN` in your terminal session before running the snippet.

```python
from localstack.sdk.pods import PodsClient

POD_NAME = "ls-cloud-pod"
client = PodsClient()

# List all pods
pods = client.list_pods()
print("Pods:", pods)

# Save Cloud Pod
client.save_pod(pod_name=POD_NAME)
print(f"Pod '{POD_NAME}' saved.")

# Load Cloud Pod
client.load_pod(pod_name=POD_NAME)
print(f"Pod '{POD_NAME}' loaded.")

# Delete Cloud Pod
client.delete_pod(pod_name=POD_NAME)
print(f"Pod '{POD_NAME}' deleted.")
```

The following output is displayed:

```bash
Pods: cloudpods=[PodListCloudpodsInner(max_version=1, pod_name='check-pod', last_change=None)]
Pod 'ls-cloud-pod' saved.
Pod 'ls-cloud-pod' loaded.
Pod 'ls-cloud-pod' deleted.
```

### State Reset

The following example demonstrates how to reset the current cloud state using LocalStack’s `StateClient`.

```python
import boto3
from localstack.sdk.state import StateClient

# Initialize StateClient and SQS client
client = StateClient()
sqs_client = boto3.client(
    "sqs",
    endpoint_url=client.configuration.host,
    region_name="us-east-1",
    aws_access_key_id="test",
    aws_secret_access_key="test",
)

# Create SQS queue
sqs_client.create_queue(QueueName="test-queue")
url = sqs_client.get_queue_url(QueueName="test-queue")["QueueUrl"]
print("Queue URL before reset:", url)

# Reset state
client.reset_state()
print("State reset.")

# Try to retrieve the queue URL after state reset
try:
    sqs_client.get_queue_url(QueueName="test-queue")
except Exception as exc:
    error_code = exc.response["Error"]["Code"]
    print("Error after state reset:", error_code)
```

The following output is displayed:

```bash
Queue URL before reset: http://sqs.us-east-1.localhost.localstack.cloud:4566/000000000000/test-queue
State reset.
Error after state reset: AWS.SimpleQueueService.NonExistentQueue
```

### Chaos API

LocalStack’s Chaos API enables fault injection to simulate issues in AWS services.
This example shows how to add a fault rule for the S3 service, retrieve and display the rule, and finally delete it to return to normal operations.

```python
import localstack.sdk.chaos
from localstack.sdk.models import FaultRule

# Initialize ChaosClient
client = localstack.sdk.chaos.ChaosClient()

# Add a fault rule for S3
rule = FaultRule(region="us-east-1", service="s3")
rules = client.add_fault_rules(fault_rules=[rule])
print("Added S3 rule:", [(r.region, r.service) for r in rules])

# Retrieve and display current fault rules
rules = client.get_fault_rules()
print("Current rules:", [(r.region, r.service) for r in rules])

# Delete the S3 fault rule
rules = client.delete_fault_rules(fault_rules=[rule])
print("Rules after deleting S3 rule:", [(r.region, r.service) for r in rules])
```

The following output is displayed:

```bash
Added S3 rule: [('us-east-1', 's3')]
Current rules: [('us-east-1', 's3')]
Rules after deleting S3 rule: []
```
