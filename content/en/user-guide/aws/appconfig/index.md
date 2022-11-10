---
title: "AppConfig"
linkTitle: "AppConfig"
categories: ["LocalStack Pro"]
description: Get started with AWS AppConfig
---

AWS AppConfig offers centralized management of configuration data and the ability to create, manage, and deploy configuration changes separately. It allows you to avoid deploying the service repeatedly for smaller changes, enables controlled deployments to applications and includes built-in validation checks & monitoring. With AppConfig, the configuration management is safe and secure, with automated monitoring and validation alongside roll-back capabilities. 

LocalStack provides AppConfig support via our Pro offering. You can use the AppConfig API to configure and set up an application, create an AppConfig environment, build a configuration profile, and detail your deployment strategy. The supported APIs are available over our [feature coverage page]({{< ref "feature-coverage" >}}).

## Getting started

In this getting started guide, you'll learn how to make a basic usage of AppConfig over LocalStack. This guide is intended for users who wish to get more acquainted with AppConfig, and assumes you have basic knowledge of the AWS CLI (and our [`awslocal`](https://github.com/localstack/awscli-local) wrapper script). First, start your LocalStack instance using your preferred method, then run the following commands:

1. Create an AWS AppConfig application via the `awslocal` CLI:
   {{< command >}}
   $ awslocal appconfig create-application \
        --name <APPLICATION_NAME> \
        --description <APPLICATION_DESCRIPTION>
   {{< /command >}}
   In AppConfig, an application is a folder/directory that contains the configuration data for your specific application. The output of this command will be the application ID, which you will need for the next step:
   {{< command >}}
   {
        "Id": "<APPLICATION_ID>",
        "Name": "<APPLICATION_NAME>",
        "Description": "<APPLICATION_DESCRIPTION>",
   }
   {{< /command >}}

2. Create an AppConfig environment using the `create-environment` command:
   {{< command >}}
   $ awslocal appconfig create-environment \
        --application-id <APPLICATION_ID> \
        --name <ENVIRONMENT_NAME> \
        --description <ENVIRONMENT_DESCRIPTION>
   {{< /command >}}
   An environment consists of the deployment group of your AppConfig applications. The output of this command will be the environment ID, which you will need for the next step:
   {{< command >}}
   {
        "ApplicationId": "<APPLICATION_ID>",
        "Id": "<ENVIRONMENT_ID>",
        "Name": "<ENVIRONMENT_NAME>",
        "Description": "<ENVIRONMENT_DESCRIPTION>",
        "State": "READY_FOR_DEPLOYMENT"
   }
   {{< /command >}}

3. Create an AppConfig feature flag configuration profile using the `create-configuration-profile` command:
   {{< command >}}
   $ awslocal appconfig create-configuration-profile \
        --application-id <APPLICATION_ID> \
        --name <CONFIGURATION_PROFILE_NAME> \
        --location-uri hosted \
        --type AWS.AppConfig.FeatureFlags
   {{< /command >}}
   You can further create your feature flag configuration data in JSON format by conforming to the `AWS.AppConfig.FeatureFlags` JSON schema. Follow the [schema documentation](https://docs.aws.amazon.com/appconfig/latest/userguide/appconfig-creating-configuration-and-profile.html#appconfig-type-reference-feature-flags) to use the `create-hosted-configuration-version` command to save your feature flag configuration data to AppConfig:
   {{< command >}}
   $ awslocal appconfig create-hosted-configuration-version \
        --application-id <APPLICATION_ID> \
        --configuration-profile-id <CONFIGURATION_PROFILE_ID> \
        --content-type "application/json" \
        --content <FEATURE_FLAG_CONFIGURATION_DATA_FILE>
   {{< /command >}}

4. Create an AppConfig deployment strategy using the `create-deployment-strategy` command:
   {{< command >}}
   $ awslocal appconfig create-deployment-strategy \
        --name <DEPLOYMENT_STRATEGY_NAME> \
        --description <DEPLOYMENT_STRATEGY_DESCRIPTION> \
        --deployment-duration-in-minutes <DEPLOYMENT_DURATION_IN_MINUTES> \
        --growth-factor <GROWTH_FACTOR> \
   {{< /command >}}

   For more information on deployment strategies, see the [AppConfig documentation](https://docs.aws.amazon.com/appconfig/latest/userguide/appconfig-creating-deployment-strategy.html). The above command will return the following information:
   {{< command >}}
   {
        "Id": "<DEPLOYMENT_STRATEGY_ID>",
        "Name": "<DEPLOYMENT_STRATEGY_NAME>",
        "Description": "<DEPLOYMENT_STRATEGY_DESCRIPTION>",
        "DeploymentDurationInMinutes": <DEPLOYMENT_DURATION_IN_MINUTES>,
        "GrowthFactor": <GROWTH_FACTOR>,
   }
   {{< /command >}}

5. Deploy the configuration using the `start-deployment` command:
   {{< command >}}
   $ awslocal appconfig start-deployment \
        --application-id <APPLICATION_ID> \
        --environment-id <ENVIRONMENT_ID> \
        --deployment-strategy-id <DEPLOYMENT_STRATEGY_ID> \
        --configuration-profile-id <CONFIGURATION_PROFILE_ID> \
        --configuration-version <CONFIGURATION_VERSION>
        --description <DEPLOYMENT_DESCRIPTION>
   {{< /command >}}

Navigate to the [AppConfig extensions](https://docs.aws.amazon.com/appconfig/latest/userguide/working-with-appconfig-extensions.html) and [services that integrate with AppConfig](https://docs.aws.amazon.com/appconfig/latest/userguide/appconfig-integration.html) over the official documentation to learn more about how to inject logic in your configuration, and use AppConfig with other AWS services respectively.
