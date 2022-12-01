---
title: "Systems Manager (SSM)"
linkTitle: "Systems Manager (SSM)"
categories: ["LocalStack Pro"]
description: Get started with AWS Systems Manager (SSM) on LocalStack
aliases:
  - /aws/systems-manager/
---

Systems Manager can be used in conjunction with the [EC2 Docker backend]({{< ref "../elastic-compute-cloud/index.md" >}}) to run operational tasks on the Dockerised instances.

The following table highlights some differences between LocalStack SSM and AWS SSM.

| LocalStack | AWS |
|------------|-----|
| Instances are automatically registered with SSM | Instances are manually registered using [`CreateActivation`](https://docs.aws.amazon.com/systems-manager/latest/APIReference/API_CreateActivation.html) |
| Uses Docker exec to perform operations | Uses [Amazon SSM Agent](https://github.com/aws/amazon-ssm-agent) |
| Instance IDs are prefixed with `i-` | Instance IDs are prefixed with `mi-` |

Following operations are currently supported:

| Operation | Notes |
|:----------|:------|
| DescribeInstanceInformation | List all registered instances |
| SendCommand | Currently only `AWS-RunShellScript` document is supported |
| ListCommandInvocations | List all invocations |
| GetCommandInvocation | Details of an invocation including standard output and standard error contents |

### Examples

{{< command >}}
$ awslocal ssm send-command --document-name "AWS-RunShellScript" \
    --document-version "1" \
    --instance-ids i-04df0c15 \
    --parameters "commands='cat ./uptime',workingDirectory=/proc"
{
    "Command": {
        "CommandId": "e53e67c3-a8f2-419e-87e4-e596880797e8",
        "DocumentName": "AWS-RunShellScript",
        "DocumentVersion": "1",
        "InstanceIds": [
            "i-04df0c15"
        ],
        "Status": "InProgress"
    }
}

$ awslocal ssm get-command-invocation \
    --command-id a0105ed1-0a4d-423b-9a64-9a49828f5391 \
    --instance-id i-04df0c15
{
    "CommandId": "a0105ed1-0a4d-423b-9a64-9a49828f5391",
    "InstanceId": "i-04df0c15",
    "DocumentName": "AWS-RunShellScript",
    "DocumentVersion": "1",
    "Status": "Success",
    "StandardOutputContent": "1066081.29 510156.74\n",
    "StandardErrorContent": ""
}
{{< /command >}}

### Limitations

- Only `AWS-RunShellScript` is supported for Dockerised instances.
- If the command returns a non-zero code, the standard output and standard error streams are not captured and will be empty.
- Shell constructs like job controls (`&&`, `||`), redirection (`>`) etc. are not supported.
