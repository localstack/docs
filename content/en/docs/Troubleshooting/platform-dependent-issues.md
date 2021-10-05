---
title: "Platform-dependent Issues"
weight: 50
description: >
  Known limitations of LocalStack and its services
---

## Covered Topics

* [Apple M1 known issues and ways to solve them](#apple-m1-known-issues-and-ways-to-solve-them)

## Apple M1 known issues and ways to solve them

{{% alert title="Aarch64 Support" color="info" %}}
LocalStack team and community are working hard to bring M1 support to LocalStack images
{{% /alert %}}

Currently, LocalStack images do not fully support `aarch64`, including
Apple M1 silicon.

However, this does not mean you can not run LocalStack on M1 machines. Folow the
next workaround tip to get LocalStack up and running on your M1.

{{% alert title="Note on JVM Lambda" color="warning" %}}
You need to use the `local` lambfda executor for JVM Lambda functions
{{% /alert %}}

To be on a safer side, you can enable "Rosetta" on your preferred Terminal. This
way you'll be installing packages for `x86_64` platform.

![Rosetta](../m1-trouble-1.png)

What we will be doing now is installing Java and Python executables using
Homebrew, it should automativally resolve packages to proper architecture versions.

```shell
# Install Homebrew
/bin/bash -c "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/HEAD/install.sh)"

# Install java11 and follow instructions
brew install java11

# Install jenv and follow instructions
brew install jenv

# Add Java11 to jenv and use it globally
jenv add /Library/Java/JavaVirtualMachines/openjdk-11.jdk/Contents/Home/
jenv global 11

# Install pyenv and follow instructions
brew install pyenv

# Install python 3.8.10 and enable it globally
pyenv install 3.8.10
pyenv global 3.8.10
```

Then clone LocalStack to your machine, run `make install` and then `make start`.
