---
title: "CodeCommit"
linkTitle: "CodeCommit"
categories: ["LocalStack Pro"]
description: >
  Get started with AWS CodeCommit on LocalStack
aliases:
  - /aws/codecommit/
---

LocalStack Pro contains basic support for CodeCommit code repositories. The CodeCommit API can be used to create Git repositories, clone these repos to local folders, push commits with changes, etc.

A simple example has been added in [this Github repository](https://github.com/localstack/localstack-pro-samples/tree/master/codecommit-git-repo). The sample creates an Git repository via the AWS CodeCommit API locally, commits and pushes a test file to the repository, and then checks out the file in a fresh clone of the repository.

Please note that CodeCommit is a fairly large API and currently not all methods are supported yet, but we are actively extending the implementation on an ongoing basis.
