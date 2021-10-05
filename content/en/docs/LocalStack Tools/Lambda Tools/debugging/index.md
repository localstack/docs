---
title: "Remote debugging"
weight: 5
categories: ["LocalStack Community"]
description: >
  Attach a debugger to your Lambda functions from your IDE.
---

Using a debugger with Lambda functions used to be a really difficult task.
LocalStack changes that with the same local code mounting functionality that also helps you to [iterate quickly over your function code]({{< ref "hot-deploy" >}}).

Currently, this guide covers the remote debugging for Python Lambda functions and [Visual Studio Code](https://code.visualstudio.com/) as an IDE. 
More examples and tooling support for local Lambda debugging (including support for other IDEs like PyCharm, IntelliJ, etc.) is coming soon - stay tuned!

For a simple working example of this feature, you can refer to [our samples repository](https://github.com/localstack/localstack-pro-samples/tree/master/lambda-mounting-and-debugging).
There, the necessary code fragments for enabling debugging are already present.

### Starting up LocalStack

First, make sure that LocalStack is started with the following configuration (see the [Configuration docs]({{< ref "configuration#lambda" >}}) for more information):
```sh
LAMBDA_REMOTE_DOCKER=0 \
    LAMBDA_DOCKER_FLAGS='-p 19891:19891' \
    DEBUG=1 localstack start
```

### Preparing your code

For providing the debug server, we use [`debugpy`](https://github.com/microsoft/debugpy) inside the Lambda function code. 
In general, you just need the following code fragment inside your handler code:
```python
import debugpy
debugpy.listen(19891)
debugpy.wait_for_client()  # blocks execution until client is attached
```
For extra convenience, you can use the `wait_for_debug_client` function from our example.
It implements the above-mentioned start of the debug server and also adds an automatic cancellation of the wait task if the debug client (i.e. VSCode) doesn't connect.
```python
def wait_for_debug_client(timeout=15):
    """Utility function to enable debugging with Visual Studio Code"""
    import time, threading
    import sys, glob
    sys.path.append(glob.glob(".venv/lib/python*/site-packages")[0])
    import debugpy

    debugpy.listen(("0.0.0.0", 19891))
    class T(threading.Thread):
        daemon = True
        def run(self):
            time.sleep(timeout)
            print("Canceling debug wait task ...")
            debugpy.wait_for_client.cancel()
    T().start()
    print("Waiting for client to attach debugger ...")
    debugpy.wait_for_client()
```

### Creating the Lambda function

To create the Lambda function, you just need to take care of two things:
1. Deploy the function via an S3 Bucket. You need to use the magic variable `__local__` as the bucket name.
2. Set the S3 key to the path of the directory your lambda function resides in.
   The handler is then referenced by the filename of your lambda code and the function in that code that should be invoked.

So, in our [example](https://github.com/localstack/localstack-pro-samples/tree/master/lambda-mounting-and-debugging), this would be:

```sh
awslocal lambda create-function --function-name my-cool-local-function \
    --code S3Bucket="__local__",S3Key="$(pwd)/" \         
    --handler handler.handler \
    --runtime python3.8 \
    --role cool-stacklifter
```

We can quickly verify that it works by invoking it with a simple payload:

```sh
awslocal lambda invoke --function-name my-cool-local-function --payload '{"message": "Hello from LocalStack!"}' output.txt 
```

### Attaching your IDE

For attaching the debug server from Visual Studio Code, you need to add a run configuration.

```json
{
    "version": "0.2.0",
    "configurations": [
        {
            "name": "Python: Remote Attach",
            "type": "python",
            "request": "attach",
            "connect": {
                "host": "localhost",
                "port": 19891
            },
            "pathMappings": [
                {
                    "localRoot": "${workspaceFolder}",
                    "remoteRoot": "."
                }
            ]
        }
    ]
}
```

With our function from above you have about 15 seconds (the timeout is configurable) to switch to Visual Studio Code and run the preconfigured remote debugger.
Make sure to set a breakpoint in the Lambda handler code first, which can then later be inspected.

The screenshot below shows the triggered breakpoint with our `'Hello from LocalStack!'` in the variable inspection view:

![Visual Studio Code debugging](vscode-debugging.png)

### Limitations

Due to the ports used by the debugger, you can currently only debug one Lambda at a time.
Multiple concurrent invocations will not work.