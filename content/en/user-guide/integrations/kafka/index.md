---
title: "Self-managed Kafka cluster"
linkTitle: "Self-managed Kafka cluster"
description: >
  Using LocalStack Lambda with a self-managed Kafka cluster
---

LocalStack Pro supports [AWS Managed Streaming for Kafka (MSK)]({{< ref "user-guide/aws/msk" >}}) and you can create Kafka clusters directly through the MSK API that will run in LocalStack.
In some cases, you may want to run your own self-managed Kafka cluster and integrate it with your applications, like triggering Lambdas from a Kafka stream running in your own cluster.
The Lambda integration with self-managed Kafka clusters is also a LocalStack Pro feature.

## Running self-managed Kafka

You can find the [example Docker Compose](docker-compose.yml) file which contains a single-noded ZooKeeper and a Kafka cluster and a simple LocalStack setup as well as [Kowl](https://github.com/cloudhut/kowl), an Apache Kafka Web UI.

1. Run Docker Compose:

{{< command >}}
$ docker-compose up -d
{{< / command >}}

2. Create the Lambda function:

{{< command >}}
$ awslocal lambda create-function \
    --function-name fun1 \
    --handler lambda.handler \
    --runtime python3.8 \
    --role arn:aws:iam::000000000000:role/lambda-role \
    --zip-file fileb://lambda.zip
{
    "FunctionName": "fun1",
    "FunctionArn": "arn:aws:lambda:us-east-1:000000000000:function:fun1",
    "Runtime": "python3.8",
    "Role": "arn:aws:iam::000000000000:role/lambda-role",
    "Handler": "lambda.handler",
    "CodeSize": 294,
    "Description": "",
    "Timeout": 3,
    "LastModified": "2021-05-19T02:01:06.617+0000",
    "CodeSha256": "/GPsiNXaq4tBA4QpxPCwgpeVfP7j+1tTH6zdkJ3jiU4=",
    "Version": "$LATEST",
    "VpcConfig": {},
    "TracingConfig": {
        "Mode": "PassThrough"
    },
    "RevisionId": "d85469d2-8558-4d75-bc0e-5926f373e12c",
    "State": "Active",
    "LastUpdateStatus": "Successful",
    "PackageType": "Zip"
}
{{< / command >}}

3. Create an example secret:

{{< command >}}
$ awslocal secretsmanager create-secret --name localstack
{
    "ARN": "arn:aws:secretsmanager:us-east-1:000000000000:secret:localstack-TDIuI",
    "Name": "localstack",
    "VersionId": "32bbb8e2-46ee-4322-b3d5-b6459d54513b"
}
{{< / command >}}

4. Create an example Kafka topic:

{{< command >}}
$ docker exec -ti kafka kafka-topics --zookeeper zookeeper:2181 --create --replication-factor 1 --partitions 1 --topic t1
Created topic t1.
{{< / command >}}

5. Create the event source mapping to your local kafka cluster:

{{< command >}}
$ awslocal lambda create-event-source-mapping \
    --topics t1 \
    --source-access-configuration Type=SASL_SCRAM_512_AUTH,URI=arn:aws:secretsmanager:us-east-1:000000000000:secret:localstack-TDIuI \
    --function-name arn:aws:lambda:us-east-1:000000000000:function:fun1 \
    --self-managed-event-source '{"Endpoints":{"KAFKA_BOOTSTRAP_SERVERS":["localhost:9092"]}}'
{
    "UUID": "4a2b0ea6-960c-4847-8684-465876dd6dbd",
    "BatchSize": 100,
    "FunctionArn": "arn:aws:lambda:us-east-1:000000000000:function:fun1",
    "LastModified": "2021-05-19T04:02:49+02:00",
    "LastProcessingResult": "OK",
    "State": "Enabled",
    "StateTransitionReason": "User action",
    "Topics": [
        "t1"
    ],
    "SourceAccessConfigurations": [
        {
            "Type": "SASL_SCRAM_512_AUTH",
            "URI": "arn:aws:secretsmanager:us-east-1:000000000000:secret:localstack-TDIuI"
        }
    ],
    "SelfManagedEventSource": {
        "Endpoints": {
            "KAFKA_BOOTSTRAP_SERVERS": [
                "localhost:9092"
            ]
        }
    }
}
{{< / command >}}

6. Additionally visit `http://localhost:8080` for Kowl's UI.
