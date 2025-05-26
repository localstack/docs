---
title: "Managed Blockchain (AMB)"
linkTitle: "Managed Blockchain (AMB)"
description: >
  Get started with Managed Blockchain (AMB) on LocalStack
tags: ["Pro image"]
---

Managed Blockchain (AMB) is a managed service that enables the creation and management of blockchain networks, such as Hyperledger Fabric, Bitcoin, Polygon and Ethereum.
Blockchain enables the development of applications in which multiple entities can conduct transactions and exchange data securely and transparently, eliminating the requirement for a central, trusted authority.

LocalStack allows you to use the AMB APIs to develop and deploy decentralized applications in your local environment.
The supported APIs are available on our [API Coverage Page]({{< ref "coverage_managedblockchain" >}}), which provides information on the extent of AMB integration with LocalStack.

## Getting started

This guide is designed for users new to AMB and assumes basic knowledge of the AWS CLI and our [`awslocal`](https://github.com/localstack/awscli-local) wrapper script.

Start your LocalStack container using your preferred method.
We will demonstrate how to create a blockchain network, a node, and a proposal.

### Create a blockchain network

You can create a blockchain network using the [`CreateNetwork`](https://docs.aws.amazon.com/managed-blockchain/latest/APIReference/API_CreateNetwork.html) API.
Run the following command to create a network named `OurBlockchainNet` which uses the Hyperledger Fabric with the following configuration:

{{< command >}}
$ awslocal managedblockchain create-network \
    --cli-input-json '{
        "Name": "OurBlockchainNet",
        "Description": "OurBlockchainNetDesc",
        "Framework": "HYPERLEDGER_FABRIC",
        "FrameworkVersion": "1.2",
        "FrameworkConfiguration": {
            "Fabric": {
            "Edition": "STARTER"
            }
        },
        "VotingPolicy": {
            "ApprovalThresholdPolicy": {
            "ThresholdPercentage": 50,
            "ProposalDurationInHours": 24,
            "ThresholdComparator": "GREATER_THAN"
            }
        },
        "MemberConfiguration": {
            "Name": "org1",
            "Description": "Org1 first member of network",
            "FrameworkConfiguration": {
            "Fabric": {
                "AdminUsername": "MyAdminUser",
                "AdminPassword": "Password123"
            }
            },
            "LogPublishingConfiguration": {
            "Fabric": {
                "CaLogs": {
                "Cloudwatch": {
                    "Enabled": true
                }
                }
            }
            }
        }
        }'
<disable-copy>
{
    "NetworkId": "n-X24AF1AK2GC6MDW11HYW5I5DQC",
    "MemberId": "m-6VWBWHP2Y15F7TQ2DS093RTCW2"
}
</disable-copy>
{{< / command >}}

Copy the `NetworkId` and `MemberId` values from the output of the above command, as we will need them in the next step.

### Create a node

You can create a node using the [`CreateNode`](https://docs.aws.amazon.com/managed-blockchain/latest/APIReference/API_CreateNode.html) API.
Run the following command to create a node with the following configuration:

{{< command >}}
$ awslocal managedblockchain create-node \
    --node-configuration '{
    "InstanceType": "bc.t3.small",
    "AvailabilityZone": "us-east-1a",
    "LogPublishingConfiguration": {
        "Fabric": {
        "ChaincodeLogs": {
            "Cloudwatch": {
            "Enabled": true
            }
        },
        "PeerLogs": {
            "Cloudwatch": {
            "Enabled": true
            }
        }
        }
    }
    }' \
    --network-id n-X24AF1AK2GC6MDW11HYW5I5DQC \
    --member-id m-6VWBWHP2Y15F7TQ2DS093RTCW2
<disable-copy>
{
    "NodeId": "nd-77K8AI0O5BEQD1IW4L8OGKMXV7"
}
</disable-copy>
{{< / command >}}

Replace the `NetworkId` and `MemberId` values in the above command with the values you copied in the previous step.

### Create a proposal

You can create a proposal using the [`CreateProposal`](https://docs.aws.amazon.com/managed-blockchain/latest/APIReference/API_CreateProposal.html) API.
Run the following command to create a proposal with the following configuration:

{{< command >}}
$ awslocal managedblockchain create-proposal \
    --actions "Invitations=[{Principal=000000000000}]" \
    --network-id n-X24AF1AK2GC6MDW11HYW5I5DQC \
    --member-id m-6VWBWHP2Y15F7TQ2DS093RTCW2
<disable-copy>
{
    "ProposalId": "p-NK0PSLDPETJQX01Q4OLBRHP8CZ"
}
</disable-copy>
{{< / command >}}

Replace the `NetworkId` and `MemberId` values in the above command with the values you copied in the previous step.
