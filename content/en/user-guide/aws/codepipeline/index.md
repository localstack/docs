---
title: CodePipeline
linkTitle: CodePipeline
description: >
  Get started with CodePipeline on LocalStack
tags: ["Pro image"]
---

## Introduction

CodePipeline is a continuous integration/continuous delivery (CI/CD) service offered by AWS.
CodePipeline can be used to create automated pipelines that handle the build, test and deployment of software.

LocalStack comes with a bespoke execution engine that can be used to create, manage and execute pipelines.
It supports a variety of actions that integrate with S3, CodeBuild, CodeConnections and more.
The available operations can be found on the [API coverage](https://docs.localstack.cloud/references/coverage/coverage_codepipeline/) page.

## Getting started

In this guide, we will create a simple pipeline that fetches an object from an S3 bucket and uploads it to a different S3 bucket.
It is for users that are new to CodePipeline and have a basic knowledge of the AWS CLI and the [`awslocal`](https://github.com/localstack/awscli-local) wrapper.

Start LocalStack using your preferred method.

### Create prerequisite buckets

Begin by creating the S3 buckets that will serve as the source and target.

{{< command >}}
$ awslocal s3 mb s3://source-bucket
$ awslocal s3 mb s3://target-bucket
{{< / command >}}

It is important to note the CodePipeline requires source S3 buckets to have versioning enabled.
This can be done using the S3 [PutBucketVersioning](https://docs.aws.amazon.com/AmazonS3/latest/API/API_PutBucketVersioning.html) operation.

{{< command >}}
$ awslocal s3api put-bucket-versioning \
    --bucket source-bucket \
    --versioning-configuration Status=Enabled
{{< /command >}}

Now create a placeholder file that will flow through the pipeline and upload it to the source bucket.

{{< command >}}
$ echo "Hello LocalStack!" > file
{{< /command >}}

{{< command >}}
$ awslocal s3 cp file s3://source-bucket
<disable-copy>
upload: ./file to s3://source-bucket/file
</disable-copy>
{{< /command >}}

Pipelines also require an artifact store, which is also an S3 bucket that is used as intermediate storage.

{{< command >}}
$ awslocal s3 mb s3://artifact-store-bucket
{{< / command >}}

### Configure IAM

Depending on the specifics of the declaration, CodePipeline pipelines need access other AWS services.
In this case we want our pipeline to retrieve and upload files to S3.
This requires a properly configured IAM role that our pipeline can assume.

Create the role and make note of the role ARN:

```json
# role.json
{
    "Version": "2012-10-17",
    "Statement": [
        {
            "Effect": "Allow",
            "Principal": {
                "Service": "codepipeline.amazonaws.com"
            },
            "Action": "sts:AssumeRole"
        }
    ]
}
```

{{< command >}}
$ awslocal iam create-role --role-name role --assume-role-policy-document file://role.json | jq .Role.Arn
<disable-copy>
"arn:aws:iam::000000000000:role/role"
</disable-copy>
{{< /command >}}

Now add a permissions policy to this role that permits read and write access to S3.

```json
# policy.json
{
    "Version": "2012-10-17",
    "Statement": [
        {
            "Effect": "Allow",
            "Action": [
                "s3:*"
            ],
            "Resource": "*"
        }
    ]
}
```

The permissions in the above example policy are relatively broad.
You might want to use a more focused policy for better security on production systems.

{{< command >}}
$ awslocal iam put-role-policy --role-name role --policy-name policy --policy-document file://policy.json
{{< /command >}}

### Create pipeline

Now we can turn our attention to the pipeline declaration.

A pipeline declaration is used to define the structure of actions and stages to be performed.
The following pipeline defines two stages with one action each.
There is a source action which retrieves a file from an S3 bucket and marks it as the output.
The output is placed in the intermediate bucket until it is picked up by the action in the second stage.
This is a deploy action which uploads the file to the target bucket.

Pay special attention to `roleArn`, `artifactStore.location` as well as `S3Bucket`, `S3ObjectKey`, and `BucketName`.
These correspond to the resources we created earlier.

```json {hl_lines=[6,9,26,27,52]}
# declaration.json
{
    "name": "pipeline",
    "executionMode": "SUPERSEDED",
    "pipelineType": "V1",
    "roleArn": "arn:aws:iam::000000000000:role/role",
    "artifactStore": {
        "type": "S3",
        "location": "artifact-store-bucket"
    },
    "version": 1,
    "stages": [
        {
            "name": "stage1",
            "actions": [
                {
                    "name": "action1",
                    "actionTypeId": {
                        "category": "Source",
                        "owner": "AWS",
                        "provider": "S3",
                        "version": "1"
                    },
                    "runOrder": 1,
                    "configuration": {
                        "S3Bucket": "source-bucket",
                        "S3ObjectKey": "file",
                        "PollForSourceChanges": "false"
                    },
                    "outputArtifacts": [
                        {
                            "name": "intermediate-file"
                        }
                    ],
                    "inputArtifacts": []
                }
            ]
        },
        {
            "name": "stage2",
            "actions": [
                {
                    "name": "action1",
                    "actionTypeId": {
                        "category": "Deploy",
                        "owner": "AWS",
                        "provider": "S3",
                        "version": "1"
                    },
                    "runOrder": 1,
                    "configuration": {
                        "BucketName": "target-bucket",
                        "Extract": "false",
                        "ObjectKey": "output-file"
                    },
                    "inputArtifacts": [
                        {
                            "name": "intermediate-file"
                        }
                    ],
                    "outputArtifacts": []
                }
            ]
        }
    ]
}
```

Create the pipeline using the following command:

{{< command >}}
$ awslocal codepipeline create-pipeline --pipeline file://./declaration.json
{{< /command >}}

### Verify pipeline execution

A 'pipeline execution' is an instance of a pipeline in running or finished state.

The [CreatePipeline](https://docs.aws.amazon.com/codepipeline/latest/APIReference/API_CreatePipeline.html) operation we ran earlier started a pipeline execution.
This can be confirmed using:

{{< command >}}
$ awslocal codepipeline list-pipeline-executions --pipeline-name pipeline
<disable-copy>
{
    "pipelineExecutionSummaries": [
        {
            "pipelineExecutionId": "37e8eb2e-0ed9-447a-a016-8dbbd796bfe7",
            "status": "Succeeded",
            "startTime": 1745486647.138571,
            "lastUpdateTime": 1745486648.290341,
            "trigger": {
                "triggerType": "CreatePipeline"
            },
            "executionMode": "SUPERSEDED"
        }
    ]
}
</disable-copy>
{{< /command >}}

Note the `trigger.triggerType` field specifies what initiated the pipeline execution.
Currently in LocalStack, only two triggers are implemented: `CreatePipeline` and `StartPipelineExecution`.

The above pipeline execution was successful.
This means that we can retrieve the `output-file` object from the `target-bucket` S3 bucket.

{{< command >}}
$ awslocal s3 cp s3://target-bucket/output-file output-file
<disable-copy>
download: s3://target-bucket/output-file to ./output-file
</disable-copy>
{{< /command >}}

To verify that it is the same file as the original input:

{{< command >}}
$ cat output-file
<disable-copy>
Hello LocalStack!
</disable-copy>
{{< /command >}}

### Examine action executions

Using the [ListActionExecutions](https://docs.aws.amazon.com/codepipeline/latest/APIReference/API_ListPipelineExecutions.html), detailed information about each action execution such as inputs and outputs can be retrieved.
This is useful when debugging the pipeline.

{{< command >}}
$ awslocal codepipeline list-action-executions --pipeline-name pipeline
<disable-copy>
{
    "actionExecutionDetails": [
        {
            "pipelineExecutionId": "37e8eb2e-0ed9-447a-a016-8dbbd796bfe7",
            "actionExecutionId": "e38716df-645e-43ce-9597-104735c7f92c",
            "pipelineVersion": 1,
            "stageName": "stage2",
            "actionName": "action1",
            "startTime": 1745486647.269867,
            "lastUpdateTime": 1745486647.289813,
            "status": "Succeeded",
            "input": {
                "actionTypeId": {
                    "category": "Deploy",
                    "owner": "AWS",
                    "provider": "S3",
                    "version": "1"
                },
                "configuration": {
                    "BucketName": "target-bucket",
                    "Extract": "false",
                    "ObjectKey": "output-file"
                },
                "resolvedConfiguration": {
                    "BucketName": "target-bucket",
                    "Extract": "false",
                    "ObjectKey": "output-file"
                },
                "region": "eu-central-1",
                "inputArtifacts": [
                    {
                        "name": "intermediate-file",
                        "s3location": {
                            "bucket": "artifact-store-bucket",
                            "key": "pipeline/intermediate-file/01410aa4.zip"
                        }
                    }
                ]
            },
            "output": {
                "outputArtifacts": [],
                "executionResult": {
                    "externalExecutionId": "bcff0781",
                    "externalExecutionSummary": "Deployment Succeeded"
                },
                "outputVariables": {}
            }
        },
        {
            "pipelineExecutionId": "37e8eb2e-0ed9-447a-a016-8dbbd796bfe7",
            "actionExecutionId": "ae99095a-1d43-46ee-8a48-c72b6d60021e",
            "pipelineVersion": 1,
            "stageName": "stage1",
            "actionName": "action1",
            ...
</disable-copy>
{{< /command >}}

{{< callout >}}
LocalStack does not use the same logic to generate external execution IDs as AWS so there may be minor discrepancies.
Same is true for status and error messages produced by actions.
{{< /callout >}}

## Pipelines

The operations [CreatePipeline](https://docs.aws.amazon.com/codepipeline/latest/APIReference/API_CreatePipeline.html), [GetPipeline](https://docs.aws.amazon.com/codepipeline/latest/APIReference/API_GetPipeline.html), [UpdatePipeline](https://docs.aws.amazon.com/codepipeline/latest/APIReference/API_UpdatePipeline.html), [ListPipelines](https://docs.aws.amazon.com/codepipeline/latest/APIReference/API_ListPipelines.html), [DeletePipeline](https://docs.aws.amazon.com/codepipeline/latest/APIReference/API_DeletePipeline.html) are used to manage pipeline declarations.

LocalStack supports emulation for V1 pipelines.
V2 pipelines are only created as mocks.

{{< callout "tip" >}}
Emulation for V2 pipelines is not supported.
Make sure that the pipeline type is explicitly set in the declaration.
{{< /callout >}}

Pipeline executions can be managed with [StartPipelineExecution](https://docs.aws.amazon.com/codepipeline/latest/APIReference/API_StartPipelineExecution.html), [GetPipelineExecution](https://docs.aws.amazon.com/codepipeline/latest/APIReference/API_GetPipelineExecution.html), [ListPipelineExecutions](https://docs.aws.amazon.com/codepipeline/latest/APIReference/API_ListPipelineExecutions.html) and [StopPipelineExecutions](https://docs.aws.amazon.com/codepipeline/latest/APIReference/API_StopPipelineExecution.html).

When stopping pipeline executions with StopPipelineExecution, the stop and abandon method is not supported.
Setting the `abandon` flag will have no impact.
This is because LocalStack uses threads as the underlying mechanism to simulate pipelines, and threads can not be cleanly preempted.

Action executions can be inspected using the [ListActionExecutions](https://docs.aws.amazon.com/codepipeline/latest/APIReference/API_ListPipelineExecutions.html) operation.

### Tagging pipelines

Pipelines resources can be [tagged](https://docs.aws.amazon.com/codepipeline/latest/userguide/pipelines-tag.html) using the [TagResource](https://docs.aws.amazon.com/codepipeline/latest/APIReference/API_TagResource.html), [UntagResource](https://docs.aws.amazon.com/codepipeline/latest/APIReference/API_UntagResource.html) and [ListTagsForResource](https://docs.aws.amazon.com/codepipeline/latest/APIReference/API_ListTagsForResource.html) operations.

{{< command >}}
$ awslocal codepipeline tag-resource \
    --resource-arn arn:aws:codepipeline:eu-central-1:000000000000:pipeline \
    --tags key=purpose,value=tutorial

$ awslocal codepipeline list-tags-for-resource \
    --resource-arn arn:aws:codepipeline:eu-central-1:000000000000:pipeline
{
    "tags": [
        {
            "key": "purpose",
            "value": "tutorial"
        }
    ]
}

$ awslocal codepipeline untag-resource \
    --resource-arn arn:aws:codepipeline:eu-central-1:000000000000:pipeline \
    --tag-keys purpose
{{< /command >}}

## Variables

CodePipeline on LocalStack supports [variables](https://docs.aws.amazon.com/codepipeline/latest/userguide/reference-variables.html) which allow dynamic configuration of pipeline actions.

Actions produce output variables which can be referenced in the configuration of subsequent actions.
Make note that only when the action defines a namespace, its output variables are availabe to downstream actions.

{{< callout "tip" >}}
If an action does not use a namespace, its output variables are not available to downstream actions.
{{< /callout >}}

CodePipeline's variable placeholder syntax is as follows:

```text
#{namespace.variable}
```

As with AWS, LocalStack only makes the `codepipeline.PipelineExecutionId` variable available by default in a pipeline.

## Actions

You can use [`runOrder`](https://docs.aws.amazon.com/codepipeline/latest/userguide/action-requirements.html#action.runOrder) to control parallel or sequential order of execution of actions.

The supported actions in LocalStack CodePipeline are listed below.
Using an unsupported action will make the pipeline fail.
If you would like support for more actions, please [raise a feature request](https://github.com/localstack/localstack/issues/new/choose).

### CodeBuild Source and Test

The [CodeBuild Source and Test](https://docs.aws.amazon.com/codepipeline/latest/userguide/action-reference-CodeBuild.html) action can be used to start a CodeBuild container and run the given buildspec.

### CodeConnections Source

The [CodeConnections Source](https://docs.aws.amazon.com/codepipeline/latest/userguide/action-reference-CodestarConnectionSource.html) action is used to specify a VCS repo as the input to the pipeline.

LocalStack supports integration only with [GitHub](https://github.com/) at this time.
Please set the environment configuration option `CODEPIPELINE_GH_TOKEN` with the GitHub Personal Access Token to be able to fetch private repositories.

### S3 Deploy

The [S3 Deploy](https://docs.aws.amazon.com/codepipeline/latest/userguide/action-reference-S3Deploy.html) action is used to upload artifacts to a given S3 bucket as the output of the pipeline.

### S3 Source

The [S3 Source](https://docs.aws.amazon.com/codepipeline/latest/userguide/action-reference-S3.html) action is used to specify an S3 bucket object as input to the pipeline.

## Limitations

- Emulation for [V2 pipeline types](https://docs.aws.amazon.com/codepipeline/latest/userguide/pipeline-types-planning.html) is not supported.
  They will be created as mocks only.
- [Rollbacks and stage retries](https://docs.aws.amazon.com/codepipeline/latest/userguide/pipelines-stages.html) are not available.
- [Triggers](https://docs.aws.amazon.com/codepipeline/latest/userguide/pipelines-triggers.html) are not implemented.
  Pipelines are executed only when [CreatePipeline](https://docs.aws.amazon.com/codepipeline/latest/APIReference/API_CreatePipeline.html) and [StartPipelineExecution](https://docs.aws.amazon.com/codepipeline/latest/APIReference/API_StartPipelineExecution.html) are invoked.
- [Execution mode behaviours](https://docs.aws.amazon.com/codepipeline/latest/userguide/concepts-how-it-works.html#concepts-how-it-works-executions) are not implemented.
  Parallel pipeline executions will not lead to stage locks and waits.
- [Stage transition controls](https://docs.aws.amazon.com/codepipeline/latest/userguide/transitions.html) are not implemented.
- [Manual approval action](https://docs.aws.amazon.com/codepipeline/latest/userguide/approvals-action-add.html) and [PutApprovalResult](https://docs.aws.amazon.com/codepipeline/latest/APIReference/API_PutApprovalResult.html) operation is not available.
