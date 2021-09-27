docs.localstack.cloud
=====================

Repository for docs.localstack.cloud


get started
-----------

### clone repo

clone the repoitory and init submodules recursively (`themes/docsy` is a submodule that again has submodules for vendored assets like fontawesome).

    git clone --recurse-submodules --depth 1 git@github.com:localstack/docs.git

or

    git clone git@github.com:localstack/docs.git
    cd docs
    git submodule update --init --recursive
    
### install hugo

[install hugo](https://gohugo.io/getting-started/installing/https://gohugo.io/getting-started/installing/). Make sure to install the _extended version_.


### run locally

    npm install
    hugo server

or run in developer mode with automatic reload

    hugo server --watch=true --disableFastRender -D
