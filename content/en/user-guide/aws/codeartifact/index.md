---
title: CodeArtifact
linkTitle: CodeArtifact
description: >
  Get started with CodeArtifact on LocalStack
tags: ["Pro image"]
---

## Introduction

CodeArtifact is a fully managed artifact repository service that makes it easy to securely store, publish, and share software packages used in your development process.

On AWS, CodeArtifact supports popular package formats such as Maven, npm, Python (pip), NuGet, etc.
You can configure it to work with public repositories or use it to store your private packages.

LocalStack provides mocking support for several CodeArtifact API operations.
You can find supported operations on the [API coverage page]({{< ref "coverage_codeartifact" >}}).
It also has full support to create and use NPM repositories.

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
$ awslocal codeartifact describe-repository --domain demo-domain \
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

### External Connections and Upstream Repositories

Repositories can be associated with external connections using [AssociateExternalConnection](https://docs.aws.amazon.com/codeartifact/latest/APIReference/API_AssociateExternalConnection.html) and [DisassociateExternalConnection](https://docs.aws.amazon.com/codeartifact/latest/APIReference/API_DisassociateExternalConnection.html).

{{< command >}}
$ awslocal codeartifact associate-external-connection --domain demo-domain \
    --repository demo-repo \
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

{{< callout "note">}}
Please note, a repository can have one or more upstream repositories, or an external connection.
{{< /callout >}}

## Using CodeArtifact with npm

### Configuring npm with the login command

Use the `awslocal codeartifact login` command to fetch credentials for use with npm.

{{< command >}}
$ awslocal codeartifact login --tool npm --domain demo-domain --repository demo-repo
{{< /command >}}

This command makes the following changes to your `~/.npmrc` file:

- Adds an authorization token after fetching it from CodeArtifact using your AWS credentials.
- Sets the npm registry to the repository specified by the `--repository` option.
- **For npm 6 and lower:** Adds `"always-auth=true"` so the authorization token is sent for every npm command.

The default authorization period after calling login is 12 hours, and login must be called to periodically refresh the token.
For more information about the authorization token created with the login command, see [Tokens created with the login command](https://docs.aws.amazon.com/codeartifact/latest/ug/tokens-authentication.html#auth-token-login).

### Configuring npm manually

You can configure npm with your CodeArtifact repository without the `awslocal codeartifact login` command by manually updating the npm configuration.

#### To configure npm without using the login command

1. In a command line, fetch a CodeArtifact authorization token and store it in an environment variable.
  npm will use this token to authenticate with your CodeArtifact repository.

{{< command >}}
$ export CODEARTIFACT_AUTH_TOKEN=$(awslocal codeartifact get-authorization-token --domain demo-domain --query authorizationToken --output text)
{{< /command >}}

2. Get your CodeArtifact repository's endpoint by running the following command.
  Your repository endpoint is used to point npm to your repository to install or publish packages.

{{< command >}}
$ awslocal codeartifact get-repository-endpoint --domain demo-domain --repository demo-repo --format npm
{{< /command >}}

The following URL is an example repository endpoint.

```text
http://demo-domain-000000000000.d.codeartifact.eu-central-1.localhost.localstack.cloud/npm/demo-repo/
```

3. Use the `npm config set` command to set the registry to your CodeArtifact repository.
  Replace the URL with the repository endpoint URL from the previous step.

{{< command >}}
$ npm config set registry http://demo-domain-000000000000.d.codeartifact.eu-central-1.localhost.localstack.cloud/npm/demo-repo/
{{< /command >}}

4. Use the `npm config set` command to add your authorization token to your npm configuration.

{{< command >}}
$ npm config set //demo-domain-000000000000.d.codeartifact.eu-central-1.localhost.localstack.cloud/:_authToken=${CODEARTIFACT_AUTH_TOKEN}
{{< /command >}}

**For npm 6 or lower:** To make npm always pass the auth token to CodeArtifact, even for GET requests, set the always-auth configuration variable with npm config set.

{{< command >}}
$ npm config set //demo-domain-000000000000.d.codeartifact.eu-central-1.localhost.localstack.cloud/:always-auth=true
{{< /command >}}

#### Example npm configuration file (`.npmrc`)

The following is an example `.npmrc` file after following the preceding instructions to set the CodeArtifact registry endpoint, add an authentication token, and configure `always-auth`.

```text
registry=http://demo-domain-000000000000.d.codeartifact.eu-central-1.localhost.localstack.cloud/npm/demo-repo/
//demo-domain-000000000000.d.codeartifact.eu-central-1.localhost.localstack.cloud/:_authToken=eyJ2ZX...
//demo-domain-000000000000.d.codeartifact.eu-central-1.localhost.localstack.cloud/:always-auth=true
```

## Current Limitations

LocalStack does not support the following features yet:

- Domain owners are ignored
- Copying package versions is not supported yet
- Domain and repository permission policies are not supported yet
- Package groups are not supported yet
- Only supports the `npm` format
