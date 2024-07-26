---
title: "K8s Operator"
linkTitle: "K8s Operator"
weight: 2
description: Custom K8s operator that offers LocalStack emulator as a native resource in Kubernetes environments.
tags: ["Enterprise plan"]
---

## Introduction

LocalStack K8s operator is a custom Kubernetes operator that offers LocalStack emulator as a native resource in Kubernetes environments.
The operator is designed to simplify the deployment and management of LocalStack in Kubernetes clusters.

## Installation

To install the K8s operator, run the following commands:

{{< command >}}
$ kubectl apply -f https://raw.githubusercontent.com/localstack/localstack-k8s-operator/v0.2.0/release/crds.yaml
$ kubectl apply -f https://raw.githubusercontent.com/localstack/localstack-k8s-operator/v0.2.0/release/controller.yaml
{{< / command >}}

You can then deploy a LocalStack instance by storing the following file content as `localstack.yml` and applying it against the cluster via `kubectl apply -f localstack.yml`.

```bash
apiVersion: api.localstack.cloud/v1alpha1
kind: LocalStack
metadata:
  name: env-0
  namespace: default
spec:
  image: localstack/localstack-pro:3.5.0
  debug: trace

  authToken: "<my-auth-token>" # Set your LocalStack auth token here
  autoLoadPods: ["<my-cloudpod>"] # Set your Cloud Pods to automatically load them here (optional)

  dnsProvider: coredns
  dnsConfigName: coredns
  dnsConfigNamespace: kube-system
```

## API Reference

### Resource Types

- [LocalStack](#localstack)
- [LocalStackList](#localstacklist)

#### Hooks

_Appears in:_
- [LocalStackSpec](#localstackspec)

| Field | Description |
| --- | --- |
| `readyConfigName` _string_ |  |
| `bootConfigName` _string_ |  |
| `shutdownConfigName` _string_ |  |
| `startConfigName` _string_ |  |

Use as described in the [Initialization Hooks](https://docs.localstack.cloud/references/init-hooks/) reference.

#### LocalStack

LocalStack is the Schema for the `localstacks` API

_Appears in:_
- [LocalStackList](#localstacklist)

| Field | Description |
| --- | --- |
| `apiVersion` _string_ | `api.localstack.cloud/v1alpha1`
| `kind` _string_ | `LocalStack`
| `kind` _string_ | Kind is a string value representing the REST resource this object represents.<br /><br />Servers may infer this from the endpoint the client submits requests to.<br /><br />Cannot be updated.<br /><br />In CamelCase.<br /><br />More info: https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#types-kinds |
| `apiVersion` _string_ | APIVersion defines the versioned schema of this representation of an object.<br /><br />Servers should convert recognized schemas to the latest internal value, and<br /><br />may reject unrecognized values.<br /><br />More info: https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#resources |
| `metadata` _[ObjectMeta](https://kubernetes.io/docs/reference/generated/kubernetes-api/v/#objectmeta-v1-meta)_ | Refer to Kubernetes API documentation for fields of `metadata`. |
| `spec` _[LocalStackSpec](#localstackspec)_ |  |
| `status` _[LocalStackStatus](#localstackstatus)_ |  |

#### LocalStackList

LocalStackList contains a list of LocalStack

| Field | Description |
| --- | --- |
| `apiVersion` _string_ | `api.localstack.cloud/v1alpha1`
| `kind` _string_ | `LocalStackList`
| `kind` _string_ | Kind is a string value representing the REST resource this object represents.<br /><br />Servers may infer this from the endpoint the client submits requests to.<br /><br />Cannot be updated.<br /><br />In CamelCase.<br /><br />More info: https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#types-kinds |
| `apiVersion` _string_ | APIVersion defines the versioned schema of this representation of an object.<br /><br />Servers should convert recognized schemas to the latest internal value, and<br /><br />may reject unrecognized values.<br /><br />More info: https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#resources |
| `metadata` _[ListMeta](https://kubernetes.io/docs/reference/generated/kubernetes-api/v/#listmeta-v1-meta)_ | Refer to Kubernetes API documentation for fields of `metadata`. |
| `items` _[LocalStack](#localstack) array_ |  |

#### LocalStackSpec

LocalStackSpec defines the desired state of LocalStack

_Appears in:_
- [LocalStack](#localstack)

| Field | Description |
| --- | --- |
| `dnsProvider` _string_ |  |
| `dnsConfigName` _string_ |  |
| `dnsConfigNamespace` _string_ |  |
| `debug` _string_ |  |
| `autoLoadPods` _string array_ |  |
| `authToken` _string_ |  |
| `hooks` _[Hooks](#hooks)_ |  |
| `image` _string_ | Validate docker inage name (with optional tag and registry address) |
| `resources` _[ResourceRequirements](https://kubernetes.io/docs/reference/generated/kubernetes-api/v/#resourcerequirements-v1-core)_ |  |
| `readiness_probe` _[Probe](https://kubernetes.io/docs/reference/generated/kubernetes-api/v/#probe-v1-core)_ |  |
| `liveness_probe` _[Probe](https://kubernetes.io/docs/reference/generated/kubernetes-api/v/#probe-v1-core)_ |  |
| `envFrom` _[EnvFromSource](https://kubernetes.io/docs/reference/generated/kubernetes-api/v/#envfromsource-v1-core) array_ |  |
| `env` _[EnvVar](https://kubernetes.io/docs/reference/generated/kubernetes-api/v/#envvar-v1-core) array_ |  |
| `dnsPolicy` _[DNSPolicy](https://kubernetes.io/docs/reference/generated/kubernetes-api/v/#dnspolicy-v1-core)_ |  |

#### LocalStackStatus

LocalStackStatus defines the observed state of LocalStack

_Appears in:_
- [LocalStack](#localstack)

| Field | Description |
| --- | --- |
| `ready` _boolean_ |  |
| `ip` _string_ |  |
| `dns` _string_ |  |

#### PodSpec

_Appears in:_
- [LocalStackSpec](#localstackspec)

| Field | Description |
| --- | --- |
| `image` _string_ | Validate docker inage name (with optional tag and registry address) |
| `resources` _[ResourceRequirements](https://kubernetes.io/docs/reference/generated/kubernetes-api/v/#resourcerequirements-v1-core)_ |  |
| `readiness_probe` _[Probe](https://kubernetes.io/docs/reference/generated/kubernetes-api/v/#probe-v1-core)_ |  |
| `liveness_probe` _[Probe](https://kubernetes.io/docs/reference/generated/kubernetes-api/v/#probe-v1-core)_ |  |
| `envFrom` _[EnvFromSource](https://kubernetes.io/docs/reference/generated/kubernetes-api/v/#envfromsource-v1-core) array_ |  |
| `env` _[EnvVar](https://kubernetes.io/docs/reference/generated/kubernetes-api/v/#envvar-v1-core) array_ |  |
| `dnsPolicy` _[DNSPolicy](https://kubernetes.io/docs/reference/generated/kubernetes-api/v/#dnspolicy-v1-core)_ |  |
