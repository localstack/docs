---
title: "Auth Token"
linkTitle: "Auth Token"
weight: 25
description: >
  The personal auth token is used to authenticate a user in a workspace and is used to access advanced features in the LocalStack emulator.
cascade:
  type: docs
---

The auth token is a personal token that is used to authenticate a user outside the webapp, especially when using the LocalStack emulator.
The auth token is used to retrieve a user's license and to unlock advanced functionality. The auth token replaces the (now legacy) developer API keys.

The auth token does not change (unless rotated by the user) also when a license is assigned or removed.

## Setting the Auth Token
The auth token needs to be set as an environment variable in the user's dev environment.
The token itself, as well as detailed instruction on how to set it, can be found on the <a href=https://app.localstack.cloud/workspace/auth-token>Auth Token</a> page under the 'Workspace' menu.


## Rotating the Auth Token
Your personal auth token gives you full access to the associated workspace and LocalStack license.
Auth tokens should be treated as secrets and never be shared or checked into source control management systems (SCMs) like for example git.

If you suspect your personal auth token to be compromised, or if it becomes known to a third party, you should reset it immediately.
By resetting a token, the previous token will stop working immediately and can no longer be used to access a license or workspace.
Previous tokens cannot be restored.

To rotate the auth token, select the 'Reset Auth Token' action from the <a href=https://app.localstack.cloud/workspace/auth-token>Auth Token<a/> page.