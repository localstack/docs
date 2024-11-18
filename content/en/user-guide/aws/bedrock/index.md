---
title: "Bedrock"
linkTitle: "Bedrock"
description: Use foundation models running on your device with LocalStack!
tags: ["Enterprise image"]
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

## Limitations

* LocalStack Bedrock currently only officially supports text-based models.
* Currently, GPU models are not supported by the LocalStack Bedrock implementation.
