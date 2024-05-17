---
title: "Pulumi"
linkTitle: "Pulumi"
description: >
  Use the Pulumi Infrastructure as Code framework with LocalStack
---

## Introduction

Pulumi's SDK for infrastructure-as-code allows you to create, deploy, and manage AWS containers, serverless functions, and other infrastructure using popular programming languages. It supports a range of cloud providers, including AWS, Azure, Google Cloud, and Kubernetes.

LocalStack can integrate with Pulumi through the Pulumi configuration environment. There are two main methods to configure Pulumi for use with LocalStack:

- Using the `pulumilocal` wrapper script which automatically configures service endpoints.
- Manually setting up the service endpoints in your Pulumi configuration, which requires ongoing maintenance.

This guide will show you how to set up local AWS resources using both the `pulumilocal` wrapper and manual configuration.

## `pulumilocal` wrapper script

`pulumilocal` is a wrapper for the `pulumi` command line interface, facilitating the use of Pulumi with LocalStack. When executing deployment commands like `pulumilocal ["up", "destroy", "preview", "cancel"]`, the script configures the Pulumi settings for LocalStack and runs the specified Pulumi command.

The endpoints are set to point to the LocalStack API (`http://localhost:4566`). This setup simplifies the deployment of Pulumi stacks against LocalStack.

### Configure the Local Backend

Optionally, you can set environment variables to store state locally, avoiding cloud storage.

{{< command >}}
$ export PULUMI_CONFIG_PASSPHRASE=lsdevtest
$ export PULUMI_BACKEND_URL=file://`pwd`/myproj
{{< / command >}}

{{< callout >}}
For further options please consult the official documentation on available  [environment variables](https://www.pulumi.com/docs/cli/environment-variables/) and [local backend](https://www.pulumi.com/docs/concepts/state/#local-filesystem).
{{< /callout  >}}

### Install the `pulumilocal` wrapper script

You can install the `pulumilocal` wrapper script by running the following command:

{{< command >}}
$ pip install pulumi-local
{{< / command >}}

You can now use the `pulumilocal` command to interact with your Pulumi project.

{{< command >}}
$ pulumilocal --help
<disable-copy>
Pulumi - Modern Infrastructure as Code
...
<disable-copy>
{{< / command >}}

### Create a new Pulumi project

To start a new project, use these commands:

{{< command >}}
$ mkdir myproj
$ pulumilocal new aws-typescript -y -s lsdev --cwd myproj
{{< / command >}}

{{< callout "tip" >}}
The `--cwd` option is unnecessary if you're already in the project directory.
{{< /callout >}}

### Deploy the Pulumi stack

Create and select the `lsdev` stack with:

{{< command >}}
$ pulumilocal stack select -c lsdev --cwd myproj
{{< / command >}}

If you've just run the `new typescript` command, the stack is already selected. Deploy it with:

{{< command >}}
$ pulumilocal up --cwd myproj
{{< / command >}}

### Configuration

| Environment Variable  | Default value     | Description                                                   |
|-----------------------|-------------------|---------------------------------------------------------------|
| `AWS_ENDPOINT_URL`    | - | Target LocalStack instance hostname and port                   |
| `LOCALSTACK_HOSTNAME`   | `localhost`         | *(Deprecated)* Target host for connecting to LocalStack        |
| `EDGE_PORT`             | `4566`              | *(Deprecated)* Target port for connecting to LocalStack        |
| `PULUMI_CMD`            | `pulumi`            | Name of the executable Pulumi command on the system PATH       |

## Manual configuration

Alternatively, you can manually configure local service endpoints and credentials. The following section will provide detailed steps for this manual configuration, assuming you have [Pulumi](https://www.pulumi.com/docs/install/) installed.

### Create a new Pulumi stack

Start a new project with:

{{< command >}}
$ mkdir quickstart && cd quickstart
$ pulumi new aws-typescript
{{< / command >}}

We use the default configuration values:

```plaintext
This command will walk you through creating a new Pulumi project.

Enter a value or leave blank to accept the (default), and press <ENTER>.
Press ^C at any time to quit.

project name: (quickstart) 
project description: (A minimal AWS TypeScript Pulumi program) 
Created project 'quickstart'

Please enter your desired stack name.
To create a stack in an organization, use the format <org-name>/<stack-name> (e.g. `acmecorp/dev`).
stack name: (dev) 
Created stack 'dev'

aws:region: The AWS region to deploy into: (us-east-1) 
Saved config

Installing dependencies...
```

This will create the following directory structure.

{{< command >}}
$ tree -L 1
.
├── index.ts
├── node_modules
├── package.json
├── package-lock.json
├── Pulumi.dev.yaml
├── Pulumi.yaml
└── tsconfig.json
{{< / command >}}

### Configure the stack

Modify your stack configuration in `Pulumi.dev.yaml` to include endpoints for AWS services pointing to `http://localhost:4566`. However, these endpoints may change depending on the AWS plugin version you are using.

```yaml
config:
  aws:accessKey: test
  aws:s3UsePathStyle: "true"
  aws:secretKey: test
  aws:skipCredentialsValidation: "true"
  aws:skipRequestingAccountId: "true"
  aws:endpoints:
    - accessanalyzer: http://localhost:4566
    - account: http://localhost:4566
    - acm: http://localhost:4566
    - acmpca: http://localhost:4566
    - amg: http://localhost:4566
    - amp: http://localhost:4566
    - amplify: http://localhost:4566
    - apigateway: http://localhost:4566
    - apigatewayv2: http://localhost:4566
    - appautoscaling: http://localhost:4566
    - appconfig: http://localhost:4566
    - appfabric: http://localhost:4566
    - appflow: http://localhost:4566
    - appintegrations: http://localhost:4566
    - appintegrationsservice: http://localhost:4566
    - applicationautoscaling: http://localhost:4566
    - applicationinsights: http://localhost:4566
    - appmesh: http://localhost:4566
    - appregistry: http://localhost:4566
    - apprunner: http://localhost:4566
    - appstream: http://localhost:4566
    - appsync: http://localhost:4566
    - athena: http://localhost:4566
    - auditmanager: http://localhost:4566
    - autoscaling: http://localhost:4566
    - autoscalingplans: http://localhost:4566
    - backup: http://localhost:4566
    - batch: http://localhost:4566
    - beanstalk: http://localhost:4566
    - bedrock: http://localhost:4566
    - bedrockagent: http://localhost:4566
    - budgets: http://localhost:4566
    - ce: http://localhost:4566
    - chime: http://localhost:4566
    - chimesdkmediapipelines: http://localhost:4566
    - chimesdkvoice: http://localhost:4566
    - cleanrooms: http://localhost:4566
    - cloud9: http://localhost:4566
    - cloudcontrol: http://localhost:4566
    - cloudcontrolapi: http://localhost:4566
    - cloudformation: http://localhost:4566
    - cloudfront: http://localhost:4566
    - cloudfrontkeyvaluestore: http://localhost:4566
    - cloudhsm: http://localhost:4566
    - cloudhsmv2: http://localhost:4566
    - cloudsearch: http://localhost:4566
    - cloudtrail: http://localhost:4566
    - cloudwatch: http://localhost:4566
    - cloudwatchevents: http://localhost:4566
    - cloudwatchevidently: http://localhost:4566
    - cloudwatchlog: http://localhost:4566
    - cloudwatchlogs: http://localhost:4566
    - cloudwatchobservabilityaccessmanager: http://localhost:4566
    - cloudwatchrum: http://localhost:4566
    - codeartifact: http://localhost:4566
    - codebuild: http://localhost:4566
    - codecatalyst: http://localhost:4566
    - codecommit: http://localhost:4566
    - codedeploy: http://localhost:4566
    - codeguruprofiler: http://localhost:4566
    - codegurureviewer: http://localhost:4566
    - codepipeline: http://localhost:4566
    - codestarconnections: http://localhost:4566
    - codestarnotifications: http://localhost:4566
    - cognitoidentity: http://localhost:4566
    - cognitoidentityprovider: http://localhost:4566
    - cognitoidp: http://localhost:4566
    - comprehend: http://localhost:4566
    - computeoptimizer: http://localhost:4566
    - config: http://localhost:4566
    - configservice: http://localhost:4566
    - connect: http://localhost:4566
    - connectcases: http://localhost:4566
    - controltower: http://localhost:4566
    - costandusagereportservice: http://localhost:4566
    - costexplorer: http://localhost:4566
    - costoptimizationhub: http://localhost:4566
    - cur: http://localhost:4566
    - customerprofiles: http://localhost:4566
    - databasemigration: http://localhost:4566
    - databasemigrationservice: http://localhost:4566
    - dataexchange: http://localhost:4566
    - datapipeline: http://localhost:4566
    - datasync: http://localhost:4566
    - dax: http://localhost:4566
    - deploy: http://localhost:4566
    - detective: http://localhost:4566
    - devicefarm: http://localhost:4566
    - directconnect: http://localhost:4566
    - directoryservice: http://localhost:4566
    - dlm: http://localhost:4566
    - dms: http://localhost:4566
    - docdb: http://localhost:4566
    - docdbelastic: http://localhost:4566
    - ds: http://localhost:4566
    - dynamodb: http://localhost:4566
    - ec2: http://localhost:4566
    - ecr: http://localhost:4566
    - ecrpublic: http://localhost:4566
    - ecs: http://localhost:4566
    - efs: http://localhost:4566
    - eks: http://localhost:4566
    - elasticache: http://localhost:4566
    - elasticbeanstalk: http://localhost:4566
    - elasticloadbalancing: http://localhost:4566
    - elasticloadbalancingv2: http://localhost:4566
    - elasticsearch: http://localhost:4566
    - elasticsearchservice: http://localhost:4566
    - elastictranscoder: http://localhost:4566
    - elb: http://localhost:4566
    - elbv2: http://localhost:4566
    - emr: http://localhost:4566
    - emrcontainers: http://localhost:4566
    - emrserverless: http://localhost:4566
    - es: http://localhost:4566
    - eventbridge: http://localhost:4566
    - events: http://localhost:4566
    - evidently: http://localhost:4566
    - finspace: http://localhost:4566
    - firehose: http://localhost:4566
    - fis: http://localhost:4566
    - fms: http://localhost:4566
    - fsx: http://localhost:4566
    - gamelift: http://localhost:4566
    - glacier: http://localhost:4566
    - globalaccelerator: http://localhost:4566
    - glue: http://localhost:4566
    - grafana: http://localhost:4566
    - greengrass: http://localhost:4566
    - groundstation: http://localhost:4566
    - guardduty: http://localhost:4566
    - healthlake: http://localhost:4566
    - iam: http://localhost:4566
    - identitystore: http://localhost:4566
    - imagebuilder: http://localhost:4566
    - inspector: http://localhost:4566
    - inspector2: http://localhost:4566
    - inspectorv2: http://localhost:4566
    - internetmonitor: http://localhost:4566
    - iot: http://localhost:4566
    - iotanalytics: http://localhost:4566
    - iotevents: http://localhost:4566
    - ivs: http://localhost:4566
    - ivschat: http://localhost:4566
    - kafka: http://localhost:4566
    - kafkaconnect: http://localhost:4566
    - kendra: http://localhost:4566
    - keyspaces: http://localhost:4566
    - kinesis: http://localhost:4566
    - kinesisanalytics: http://localhost:4566
    - kinesisanalyticsv2: http://localhost:4566
    - kinesisvideo: http://localhost:4566
    - kms: http://localhost:4566
    - lakeformation: http://localhost:4566
    - lambda: http://localhost:4566
    - launchwizard: http://localhost:4566
    - lex: http://localhost:4566
    - lexmodelbuilding: http://localhost:4566
    - lexmodelbuildingservice: http://localhost:4566
    - lexmodels: http://localhost:4566
    - lexmodelsv2: http://localhost:4566
    - lexv2models: http://localhost:4566
    - licensemanager: http://localhost:4566
    - lightsail: http://localhost:4566
    - location: http://localhost:4566
    - locationservice: http://localhost:4566
    - logs: http://localhost:4566
    - lookoutmetrics: http://localhost:4566
    - m2: http://localhost:4566
    - macie2: http://localhost:4566
    - managedgrafana: http://localhost:4566
    - mediaconnect: http://localhost:4566
    - mediaconvert: http://localhost:4566
    - medialive: http://localhost:4566
    - mediapackage: http://localhost:4566
    - mediapackagev2: http://localhost:4566
    - mediastore: http://localhost:4566
    - memorydb: http://localhost:4566
    - mq: http://localhost:4566
    - msk: http://localhost:4566
    - mwaa: http://localhost:4566
    - neptune: http://localhost:4566
    - networkfirewall: http://localhost:4566
    - networkmanager: http://localhost:4566
    - oam: http://localhost:4566
    - opensearch: http://localhost:4566
    - opensearchingestion: http://localhost:4566
    - opensearchserverless: http://localhost:4566
    - opensearchservice: http://localhost:4566
    - opsworks: http://localhost:4566
    - organizations: http://localhost:4566
    - osis: http://localhost:4566
    - outposts: http://localhost:4566
    - pcaconnectorad: http://localhost:4566
    - pinpoint: http://localhost:4566
    - pipes: http://localhost:4566
    - polly: http://localhost:4566
    - pricing: http://localhost:4566
    - prometheus: http://localhost:4566
    - prometheusservice: http://localhost:4566
    - qbusiness: http://localhost:4566
    - qldb: http://localhost:4566
    - quicksight: http://localhost:4566
    - ram: http://localhost:4566
    - rbin: http://localhost:4566
    - rds: http://localhost:4566
    - recyclebin: http://localhost:4566
    - redshift: http://localhost:4566
    - redshiftdata: http://localhost:4566
    - redshiftdataapiservice: http://localhost:4566
    - redshiftserverless: http://localhost:4566
    - rekognition: http://localhost:4566
    - resourceexplorer2: http://localhost:4566
    - resourcegroups: http://localhost:4566
    - resourcegroupstagging: http://localhost:4566
    - resourcegroupstaggingapi: http://localhost:4566
    - rolesanywhere: http://localhost:4566
    - route53: http://localhost:4566
    - route53domains: http://localhost:4566
    - route53recoverycontrolconfig: http://localhost:4566
    - route53recoveryreadiness: http://localhost:4566
    - route53resolver: http://localhost:4566
    - rum: http://localhost:4566
    - s3: http://localhost:4566
    - s3api: http://localhost:4566
    - s3control: http://localhost:4566
    - s3outposts: http://localhost:4566
    - sagemaker: http://localhost:4566
    - scheduler: http://localhost:4566
    - schemas: http://localhost:4566
    - sdb: http://localhost:4566
    - secretsmanager: http://localhost:4566
    - securityhub: http://localhost:4566
    - securitylake: http://localhost:4566
    - serverlessapplicationrepository: http://localhost:4566
    - serverlessapprepo: http://localhost:4566
    - serverlessrepo: http://localhost:4566
    - servicecatalog: http://localhost:4566
    - servicecatalogappregistry: http://localhost:4566
    - servicediscovery: http://localhost:4566
    - servicequotas: http://localhost:4566
    - ses: http://localhost:4566
    - sesv2: http://localhost:4566
    - sfn: http://localhost:4566
    - shield: http://localhost:4566
    - signer: http://localhost:4566
    - simpledb: http://localhost:4566
    - sns: http://localhost:4566
    - sqs: http://localhost:4566
    - ssm: http://localhost:4566
    - ssmcontacts: http://localhost:4566
    - ssmincidents: http://localhost:4566
    - ssmsap: http://localhost:4566
    - sso: http://localhost:4566
    - ssoadmin: http://localhost:4566
    - stepfunctions: http://localhost:4566
    - storagegateway: http://localhost:4566
    - sts: http://localhost:4566
    - swf: http://localhost:4566
    - synthetics: http://localhost:4566
    - timestreamwrite: http://localhost:4566
    - transcribe: http://localhost:4566
    - transcribeservice: http://localhost:4566
    - transfer: http://localhost:4566
    - verifiedpermissions: http://localhost:4566
    - vpclattice: http://localhost:4566
    - waf: http://localhost:4566
    - wafregional: http://localhost:4566
    - wafv2: http://localhost:4566
    - wellarchitected: http://localhost:4566
    - worklink: http://localhost:4566
    - workspaces: http://localhost:4566
    - xray: http://localhost:4566
```

### Deploy the stack to LocalStack

To deploy, ensure the S3 service is included in your configuration, start LocalStack, and run:

{{< command >}}
$ pulumi up
{{< / command >}}

After the update, check the S3 buckets with:

{{< command >}}
$ awslocal s3 ls
{{< / command >}}

You should see output similar to:

```bash
2021-09-30 11:50:59 my-bucket-6c21027
```
