---
title: "Bedrock"
linkTitle: "Bedrock"
description: Use foundation models running on your device with LocalStack!
tags: ["Enterprise plan"]
---

## Introduction

Bedrock is a fully managed service provided by Amazon Web Services (AWS) that makes foundation models from various LLM providers accessible via an API.
LocalStack allows you to use the Bedrock APIs to test and develop AI-powered applications in your local environment.
The supported APIs are available on our [API Coverage Page](https://docs.localstack.cloud/references/coverage/coverage_bedrock/), which provides information on the extent of Bedrock's integration with LocalStack.

## Getting started

This guide is designed for users new to AWS Bedrock and assumes basic knowledge of the AWS CLI and our `awslocal` wrapper script.

Start your LocalStack container using your preferred method with or without pre-warming the Bedrock engine.
We will demonstrate how to use Bedrock by following these steps:

1. Listing available foundation models
2. Invoking a model for inference
3. Using the conversation API
4. Using batch processing

### Pre-warming the Bedrock engine

The startup of the Bedrock engine can take some time.
Per default, we only start it once you send a request to one of the `bedrock-runtime` APIs.
However, if you want to start the engine when localstack starts to avoid long wait times on your first request you can set the flag `BEDROCK_PREWARM`.

### List available foundation models

You can view all available foundation models using the [`ListFoundationModels`](https://docs.aws.amazon.com/bedrock/latest/APIReference/API_ListFoundationModels.html) API.
This will show you which models are available on AWS Bedrock.
{{< callout "note">}}
The actual model that will be used for emulation will differ from the ones defined in this list.
You can define the used model with `DEFAULT_BEDROCK_MODEL`
{{< / callout >}}

Run the following command:

{{< command >}}
$ awslocal bedrock list-foundation-models
{{< / command >}}

### Invoke a model

You can use the [`InvokeModel`](https://docs.aws.amazon.com/bedrock/latest/APIReference/API_runtime_InvokeModel.html) API to send requests to a specific model.
In this example, we selected the Llama 3 model to process a simple prompt.
However, the actual model will be defined by the `DEFAULT_BEDROCK_MODEL` environment variable.

Run the following command:

{{< command >}}
$ awslocal bedrock-runtime invoke-model \
    --model-id "meta.llama3-8b-instruct-v1:0" \
    --body '{
        "prompt": "<|begin_of_text|><|start_header_id|>user<|end_header_id|>\nSay Hello!\n<|eot_id|>\n<|start_header_id|>assistant<|end_header_id|>",
        "max_gen_len": 2,
        "temperature": 0.9
    }' --cli-binary-format raw-in-base64-out outfile.txt
{{< / command >}}

The output will be available in the `outfile.txt`.

### Use the conversation API

Bedrock provides a higher-level conversation API that makes it easier to maintain context in a chat-like interaction using the [`Converse`](https://docs.aws.amazon.com/bedrock/latest/APIReference/API_runtime_Converse.html) API.
You can specify both system prompts and user messages.

Run the following command:

{{< command >}}
$ awslocal bedrock-runtime converse \
    --model-id "meta.llama3-8b-instruct-v1:0" \
    --messages '[{
        "role": "user",
        "content": [{
            "text": "Say Hello!"
        }]
    }]' \
    --system '[{
        "text": "You'\''re a chatbot that can only say '\''Hello!'\''"
    }]'
{{< / command >}}

### Model Invocation Batch Processing

Bedrock offers the feature to handle large batches of model invocation requests defined in S3 buckets using the [`CreateModelInvocationJob`](https://docs.aws.amazon.com/bedrock/latest/APIReference/API_CreateModelInvocationJob.html) API.

First, you need to create a `JSONL` file that contains all your prompts:

{{< command >}}
$ cat batch_input.jsonl
{"prompt": "Tell me a quick fact about Vienna.", "max_tokens": 50, "temperature": 0.5}
{"prompt": "Tell me a quick fact about Zurich.", "max_tokens": 50, "temperature": 0.5}
{"prompt": "Tell me a quick fact about Las Vegas.", "max_tokens": 50, "temperature": 0.5}
{{< / command >}}

Then, you need to define buckets for the input as well as the output and upload the file in the input bucket:

{{< command >}}
$ awslocal s3 mb s3://in-bucket
make_bucket: in-bucket

$ awslocal s3 cp batch_input.jsonl s3://in-bucket
upload: ./batch_input.jsonl to s3://in-bucket/batch_input.jsonl

$ awslocal s3 mb s3://out-bucket
make_bucket: out-bucket
{{< / command >}}

Afterwards you can run the invocation job like this:

{{< command >}}
$ awslocal bedrock create-model-invocation-job \
  --job-name "my-batch-job" \
  --model-id "mistral.mistral-small-2402-v1:0" \
  --role-arn "arn:aws:iam::123456789012:role/MyBatchInferenceRole" \
  --input-data-config '{"s3InputDataConfig": {"s3Uri": "s3://in-bucket"}}' \
  --output-data-config '{"s3OutputDataConfig": {"s3Uri": "s3://out-bucket"}}'
{
    "jobArn": "arn:aws:bedrock:us-east-1:000000000000:model-invocation-job/12345678"
}
{{< / command >}}

The results will be at the S3 URL `s3://out-bucket/12345678/batch_input.jsonl.out`

## Available models

LocalStack's Bedrock emulation supports models from the [Ollama Models library](https://ollama.com/search).

To use a model, retrieve its ID from Ollama and set `DEFAULT_BEDROCK_MODEL` to that ID.
LocalStack will pull the model from Ollama and use it for emulation.

For example, to use the Mistral model, set the environment variable while starting LocalStack:

{{< command >}}
$ DEFAULT_BEDROCK_MODEL=mistral localstack start
{{< / command >}}

## Troubleshooting

Users of Docker Desktop on macOS or Windows might run into the issue of Bedrock becoming unresponsive after some usage.
A common reason for that is insufficient storage or memory space in the Docker Desktop VM.
To resolve this issue you can increase those amounts directly in Docker Desktop or clean up unused artifacts with the Docker CLI like this

{{< command >}}
$ docker system prune
{{< / command >}}

You could also try to use a model with lower requirements.
To achieve that you can search for models in the [Ollama Models library](https://ollama.com/search) with a low parameter count or smaller size.

## Limitations

* At this point, we have only tested text-based models in LocalStack.
Other models available with Ollama might also work, but are not officially supported by the Bedrock implementation.
* Currently, GPU models are not supported by the LocalStack Bedrock implementation.
