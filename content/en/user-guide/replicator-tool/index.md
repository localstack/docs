---
title: "Replicator Tool"
date: 2024-09-26T11:03:46-05:00
draft: true

description: >
  Internals of LocalStack replicator tool
aliases:
  - /localstack/replicator-tool/
  - /references/replicator-tool/
tags: ["Pro image"]
---

## Introduction

The new replicator tool enables seamless copying of real AWS resources into LocalStack, allowing you to recreate your cloud environment locally. By extracting and replicating AWS configurations, services, and data, this tool ensures an accurate reflection of your cloud setup within LocalStack. Whether for development, testing, or troubleshooting, this tool provides a quick and efficient way to mirror live resources in an emulated environment, enabling you to work locally with the same infrastructure you'd deploy on AWS.

## Usage 
To use the replicator tool, follow these steps: (Add steps here)

## Coverage 
The tool is capable of replicating the following resources into LocalStack.


{{< localstack_replicator_table >}}
