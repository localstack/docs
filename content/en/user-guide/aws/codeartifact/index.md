---
title: CodeArtifact
linkTitle: CodeArtifact
description: >
  Get started with CodeArtifact on LocalStack
tags: ["Pro image"]
---

## Introduction

CodeArtifact is a fully managed artifact repository service that makes it easy to securely store, publish, and share software packages used in your development process.

On AWS, CodeArtifact supports common package formats such as Maven, npm, Python (pip), and NuGet. You can configure it to work with public repositories or use it to store your private packages.

LocalStack provides mocking support for several CodeArtifact API operations.
You can find supported operations on the [API coverage page]({{< ref "coverage_codeartifact" >}}).

## Getting Started

This guide will help you create a domain, repository, and manage package publishing workflows using the `awslocal` CLI.

Basic knowledge of the AWS CLI and the [`awslocal`](https://github.com/localstack/awscli-local) wrapper is expected.

Start LocalStack using your preferred method.

### Domains

Domains are the top-level containers for repositories in CodeArtifact.

Create a domain with the [CreateDomain](https://docs.aws.amazon.com/codeartifact/latest/APIReference/API_CreateDomain.html) operation:

{{< command >}}
$ awslocal codeartifact create-domain --domain demo-domain
{{< /command >}}

The following output is displayed:
```json
{
    "domain": {
        "name": "demo-domain",
        "owner": "000000000000",
        "arn": "arn:aws:codeartifact:eu-central-1:000000000000:domain/demo-domain",
        "status": "Active",
        "createdTime": "2025-05-20T11:30:52.073202+02:00",
        "repositoryCount": 0,
        "assetSizeBytes": 0
    }
}
```

You can use [DescribeDomain](https://docs.aws.amazon.com/codeartifact/latest/APIReference/API_DescribeDomain.html), [UpdateDomain](https://docs.aws.amazon.com/codeartifact/latest/APIReference/API_UpdateDomain.html), and [DeleteDomain](https://docs.aws.amazon.com/codeartifact/latest/APIReference/API_DeleteDomain.html) for domain management.

{{< command >}}
$ awslocal codeartifact describe-domain --domain demo-domain
{{< /command >}}

The following output is displayed:
```json
{
    "domain": {
        "name": "demo-domain",
        "owner": "000000000000",
        "arn": "arn:aws:codeartifact:eu-central-1:000000000000:domain/demo-domain",
        "status": "Active",
        "createdTime": "2025-05-20T11:30:52.073202+02:00",
        "repositoryCount": 0,
        "assetSizeBytes": 0
    }
}
```

You can list all domains using [ListDomains](https://docs.aws.amazon.com/codeartifact/latest/APIReference/API_ListDomains.html).

{{< command >}}
$ awslocal codeartifact list-domains
{{< /command >}}

The following output is displayed:
```json
{
    "domains": [
        {
            "name": "demo-domain",
            "owner": "000000000000",
            "arn": "arn:aws:codeartifact:eu-central-1:000000000000:domain/demo-domain",
            "status": "Active",
            "createdTime": "2025-05-20T11:30:52.073202+02:00"
        }
    ]
}
```

### Repositories

Repositories store packages and are associated with a domain.

Create a repository using [CreateRepository](https://docs.aws.amazon.com/codeartifact/latest/APIReference/API_CreateRepository.html):

{{< command >}}
$ awslocal codeartifact create-repository --domain demo-domain \
    --repository demo-repo
{{< /command >}}

The following output is displayed:
```json
{
    "repository": {
        "name": "demo-repo",
        "administratorAccount": "000000000000",
        "domainName": "demo-domain",
        "domainOwner": "000000000000",
        "arn": "arn:aws:codeartifact:eu-central-1:000000000000:repository/demo-domain/demo-repo",
        "upstreams": [],
        "externalConnections": [],
        "createdTime": "2025-05-20T11:34:27.712367+02:00"
    }
}
```

You can use [DescribeRepository](https://docs.aws.amazon.com/codeartifact/latest/APIReference/API_DescribeRepository.html), [UpdateRepository](https://docs.aws.amazon.com/codeartifact/latest/APIReference/API_UpdateRepository.html), and [DeleteRepository](https://docs.aws.amazon.com/codeartifact/latest/APIReference/API_DeleteRepository.html) to manage repositories.

{{< command >}}
$ awslocal codeartifact describe-repository --domain demo-domain --repository demo-repo
{{< /command >}}

The following output is displayed:
```json
{
    "repository": {
        "name": "demo-repo",
        "administratorAccount": "000000000000",
        "domainName": "demo-domain",
        "domainOwner": "000000000000",
        "arn": "arn:aws:codeartifact:eu-central-1:000000000000:repository/demo-domain/demo-repo",
        "upstreams": [],
        "externalConnections": [],
        "createdTime": "2025-05-20T11:34:27.712367+02:00"
    }
}
```

Use [ListRepositories](https://docs.aws.amazon.com/codeartifact/latest/APIReference/API_ListRepositories.html) to view all of the repositories.

{{< command >}}
$ awslocal codeartifact list-repositories
{{< /command >}}

The following output is displayed:
```json
{
    "repositories": [
        {
            "name": "demo-repo",
            "administratorAccount": "000000000000",
            "domainName": "demo-domain",
            "domainOwner": "000000000000",
            "arn": "arn:aws:codeartifact:eu-central-1:000000000000:repository/demo-domain/demo-repo",
            "createdTime": "2025-05-20T11:34:27.712367+02:00"
        }
    ]
}
```

Otherwise, list repositories in a specific domain using [ListRepositoriesInDomain](https://docs.aws.amazon.com/codeartifact/latest/APIReference/API_ListRepositoriesInDomain.html):

{{< command >}}
$ awslocal codeartifact list-repositories-in-domain --domain demo-domain
{{< /command >}}

The following output is displayed:
```json
{
    "repositories": [
        {
            "name": "demo-repo",
            "administratorAccount": "000000000000",
            "domainName": "demo-domain",
            "domainOwner": "000000000000",
            "arn": "arn:aws:codeartifact:eu-central-1:000000000000:repository/demo-domain/demo-repo",
            "createdTime": "2025-05-20T11:34:27.712367+02:00"
        }
    ]
}
```

### External connections and upstream repositories

Repositories can be associated with external connections using [AssociateExternalConnection](https://docs.aws.amazon.com/codeartifact/latest/APIReference/API_AssociateExternalConnection.html) and [DisassociateExternalConnection](https://docs.aws.amazon.com/codeartifact/latest/APIReference/API_DisassociateExternalConnection.html).

{{< command >}}
$ awslocal codeartifact associate-external-connection --domain demo-domain --repository demo-repo \
    --external-connection "public:npmjs"
{{< /command >}}

The following output is displayed:
```json
{
    "repository": {
        "name": "demo-repo",
        "administratorAccount": "000000000000",
        "domainName": "demo-domain",
        "domainOwner": "000000000000",
        "arn": "arn:aws:codeartifact:eu-central-1:000000000000:repository/demo-domain/demo-repo",
        "upstreams": [],
        "externalConnections": [
            {
                "externalConnectionName": "public:npmjs",
                "packageFormat": "npm",
                "status": "AVAILABLE"
            }
        ],
        "createdTime": "2025-05-20T14:03:27.539994+02:00"
    }
}
```

Alternatively, repositories can be configured with upstream repositories using the `upstreams` property of [CreateRepository](https://docs.aws.amazon.com/codeartifact/latest/APIReference/API_CreateRepository.html) and [UpdateRepository](https://docs.aws.amazon.com/codeartifact/latest/APIReference/API_UpdateRepository.html).

{{< command >}}
$ awslocal codeartifact create-repository --domain demo-domain \
    --repository demo-repo2 \
    --upstreams repositoryName=demo-repo
{{< /command >}}

The following output is displayed:
```json
{
    "repository": {
        "name": "demo-repo2",
        "administratorAccount": "000000000000",
        "domainName": "demo-domain",
        "domainOwner": "000000000000",
        "arn": "arn:aws:codeartifact:eu-central-1:000000000000:repository/demo-domain/demo-repo2",
        "upstreams": [
            {
                "repositoryName": "demo-repo"
            }
        ],
        "externalConnections": [],
        "createdTime": "2025-05-20T14:07:56.741333+02:00"
    }
}
```

Please note, a repository can have one or more upstream repositories, or an external connection.

## Limitations

LocalStack doesn't support the following features yet:

- Domain and repository permission policies
- Packages and package groups handlers
- Retrieving repository endpoints
