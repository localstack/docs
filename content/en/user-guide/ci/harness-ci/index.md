---
title: "Harness CI"
tags: ["continuous-integration", "ci", "continuous-delivery", "testing"]
weight: 8
description: >
  Use LocalStack in [Harness CI](https://harness.io/products/continuous-integration)
---

Harness CI allows you to create software pipelines that will enable you to check out your code, build the software, run your tests, and validate every code change. In this guide, we will take a look at how you can integrate LocalStack in Harness CI pipelines for testing and delivering cloud-native applications.

## Setting up your Harness CI pipeline

Harness CI pipelines implements [Service Dependency](https://docs.harness.io/article/vo4sjbd09g-configure-service-dependency-step-settings) to make a detached service accessible to all steps in a stage. Service dependencies can run workflows for integration testing or Docker-in-Docker (`dind`) services. LocalStack can be run as a Service Dependency in a Harness CI pipeline. The pipeline can be either setup in the user-interface, or [configured using YAML](#yaml-configuration).

To get started, create a new pipeline in Harness CI:

- Click **Add Stage**.
- Click **Build** and set a name for the stage.
- Optionally configure the repository you are looking to be cloned and click on **Set Up Stage**.
- Select **Cloud** in the **Infrastructure** tab.
- Click **Add Service Dependency** in the **Execution** tab.
- In the **Configure Service Dependency** dialogue box, enter `localstack` as the name of the service dependency.
- Click **Container Registry** field and select **Docker Hub** connector.
- Enter the desired LocalStack Docker image in the **Image** field.
- Select **Optional Configuration** to add an environment variable named **LOCALSTACK_API_KEY** to have an CI key configured.
- Click on **Apply Changes**.

## YAML configuration

Instead of a visual workflow, you can use a YAML-based workflow by switching to **YAML** in the Pipeline Studio. As an example, it will pull the LocalStack Docker image and check if the LocalStack service is up and running:

```yaml
stages:
    - stage:
        name: my_stage
        type: CI
        spec:
          serviceDependencies:
            - identifier: localstack
              name: localstack
              type: Service
              spec:
                connectorRef: my_connector
                image: localstack/localstack
          execution:
            steps:
              - step:
                  type: Run
                  name: localstack health
                  identifier: localstack_health
                  spec:
                    connectorRef: docker_hub
                    image: curlimages/curl:7.83.1
                    shell: Sh
                    command: until curl --fail --silent --max-time 1 http://localstack:4566/_localstack/health; do sleep 2; done
```

To run the pipeline, click **Save** and then **Run Pipeline**. You will be able to see LocalStack Service Dependency logs that verify that the LocalStack Container is healthy and running.

## Configuring a CI key

You can easily enable LocalStack Pro by using the `localstack/localstack-pro` image and adding your CI key
by selecting **Optional Configuration** to add an environment variable named **LOCALSTACK_API_KEY** to have an CI key configured. Here is an example:

```yaml
serviceDependencies:
  - identifier: localstack
    name: localstack
    type: Service
    spec:
      connectorRef: my_connector
      image: localstack/localstack-pro
      envVariables:
        LOCALSTACK_API_KEY: <+secrets.getValue("localstack-ci-key")>
```
