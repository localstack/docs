---
title: "C++"
categories: []
description: >
  How to use the C++ AWS SDK with LocalStack.
---

## Overview

The [AWS SDK for C++](https://docs.aws.amazon.com/sdk-for-cpp), like other AWS SDKs, lets you set the endpoint when creating resource clients,
which is the preferred way of integrating the C++ SDK with LocalStack.

## Example

Consider the following example, which creates an SQS queue, sends a message to it, then receives the same message via the SDK:

```cpp
#include <iostream>
#include <aws/core/Aws.h>
#include <aws/core/utils/logging/LogLevel.h>
#include <aws/sqs/SQSClient.h>
#include <aws/sqs/model/CreateQueueRequest.h>
#include <aws/sqs/model/SendMessageRequest.h>
#include <aws/sqs/model/ReceiveMessageRequest.h>
#include <aws/sqs/model/DeleteMessageRequest.h>

using namespace Aws;

int main()
{
    // initialize AWS SDK
    SDKOptions options;
    options.loggingOptions.logLevel = Utils::Logging::LogLevel::Debug;
    InitAPI(options);

    // create SQS client with local endpoint configuration
    Aws::Client::ClientConfiguration clientConfig;
    clientConfig.endpointOverride = "http://localhost:4566";
    SQS::SQSClient client = SQS::SQSClient(clientConfig);

    // create queue
    std::cout << "Creating queue ..." << std::endl;
    Aws::SQS::Model::CreateQueueRequest cqReq;
    cqReq.SetQueueName("test-queue");
    auto cqRes = client.CreateQueue(cqReq);
    auto queueUrl = cqRes.GetResult().GetQueueUrl();

    // send message
    std::cout << "Sending message ..." << std::endl;
    Aws::SQS::Model::SendMessageRequest smReq;
    smReq.SetQueueUrl(queueUrl);
    smReq.SetMessageBody("test message 123");
    client.SendMessage(smReq);

    // receive message
    std::cout << "Receiving message ..." << std::endl;
    Aws::SQS::Model::ReceiveMessageRequest rmReq;
    rmReq.SetQueueUrl(queueUrl);
    auto rmRes = client.ReceiveMessage(rmReq);
    const auto& messages = rmRes.GetResult().GetMessages();
    std::cout << "Received " << messages.size() << " messages from queue " << queueUrl << std::endl;

    // print message
    const auto& message = messages[0];
    std::cout << "Received message:" << std::endl;
    std::cout << "  MessageId: " << message.GetMessageId() << std::endl;
    std::cout << "  ReceiptHandle: " << message.GetReceiptHandle() << std::endl;
    std::cout << "  Body: " << message.GetBody() << std::endl;

    // delete message
    std::cout << "Deleting message ..." << std::endl;
    Aws::SQS::Model::DeleteMessageRequest dmReq;
    dmReq.SetQueueUrl(queueUrl);
    dmReq.SetReceiptHandle(message.GetReceiptHandle());
    auto dmRes = client.DeleteMessage(dmReq);
    std::cout << "Delete message success result: " << dmRes.IsSuccess() << std::endl;

    // shut down the SDK
    ShutdownAPI(options);
    return 0;
}
```

Once compiled, we'll see the following output when running the application:

```sh
Creating queue ...
Sending message ...
Receiving message ...
Received 1 messages from queue http://localhost:4566/000000000000/test-queue
Received message:
  MessageId: 4731b327-49b2-4410-a8da-2c479e7bde04
  ReceiptHandle: ZTQ1M2Q1ZjYtMjBkZS00ODQxLTlkYzQtMjBlMGQ4MDNkODVkIGFybjphd3M6c3FzOnVzLWVhc3QtMTowMDAwMDAwMDAwMDA6dGVzdC1xdWV1ZSA0NzMxYjMyNy00OWIyLTQ0MTAtYThkYS0yYzQ3OWU3YmRlMDQgMTY3ODIxMjExMS42ODk1NTE=
  Body: test message 123
Deleting message ...
Delete message success result: 1
```

## Resources

* [AWS SDK for C++](https://docs.aws.amazon.com/sdk-for-cpp)
* [Getting Started Guide](https://docs.aws.amazon.com/sdk-for-cpp/v1/developer-guide/getting-started.html)
