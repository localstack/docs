---
title: "Chaos Engineering"
linkTitle: "Chaos Engineering"
weight: 11
description: >
  Chaos Engineering with LocalStack enables you to build resilient systems early on in the development phase.
cascade:
  type: docs
---

## Introduction

Chaos engineering via LocalStack is a method to enhance system resilience by deliberately introducing controlled disruptions.
This technique takes different forms depending on the team:

- Software developers focus on application behavior and error response
- Architects concentrate on the strength of system design
- Operations teams investigate the dependability of infrastructure setup.

Integrating chaos tests early in the development process helps identify and mitigate potential flaws, leading to systems that are more robust under stress and can withstand turbulent conditions.
Chaos engineering in LocalStack encompasses the following features:

- **Application behavior and error management** through Fault Injection Service (FIS) experiments.
- **Robust architecture** tested via failover scenarios using the Chaos API.
- **Consistent infrastructure setup** under challenging conditions like outages, examined through automated provisioning processes.

The best way to understand concepts is through practice, so dive into our [chaos engineering tutorials]({{< ref "tutorials" >}}).
