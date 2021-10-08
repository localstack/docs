docs.localstack.cloud
=====================

Repository for docs.localstack.cloud


get started
-----------

### clone repo

clone the repoitory and init submodules recursively (`themes/docsy` is a submodule that again has submodules for vendored assets like fontawesome).

    git clone --recurse-submodules --depth 1 git@github.com:localstack/docs.git

this performs a shallow clone, which leads to only the main branch being configured for your remote.
To be able to pull/push from/to all branches, please run:

    git config remote.origin.fetch "+refs/heads/*:refs/remotes/origin/*" && git fetch

or

    git clone git@github.com:localstack/docs.git
    cd docs
    git submodule update --init --recursive

### install hugo

[install hugo](https://gohugo.io/getting-started/installing). Make sure to install the _extended version_.


### run locally

    npm install
    hugo server

or run in developer mode with automatic reload

    hugo server --watch=true --disableFastRender -D

alternatively:

    npm run dev



## Best Practices

Please follow these best practices when writing documentation here:
- Use the custom `command` shortcode for all one-liner commands (also when their output is presented). Do not use it for bash scripts with comments. You can find a more detailed description here: https://github.com/localstack/docs/pull/55
- Use the [`ref` or `relref` shortcode](https://gohugo.io/content-management/cross-references/#use-ref-and-relref) when creating non-external links (but still use the markdown native image linking, ref doesn't work there).
  You can either use `ref` or `relref`, the point is to have compile time internal-link checks (which works for both).
- Stick to markdown if possible.
- Use one line for each sentence in markdown.
  If you don't add a backslash at the end of the line or add two new-lines, there won't be linebreak in the rendered text.
- For snippets, define the correct syntax highlighting.
  Here's a list of the supported languages:
  https://gohugo.io/content-management/syntax-highlighting/
- If you want to hightlight a specific line, there's a feature for that: https://gohugo.io/content-management/syntax-highlighting/#highlighting-in-code-fences
  - This is also supported by the `command` shortcode!
- Handling images can be a bit tedious with Hugo.
  If you want to use images in your post, create a new [leaf bundle directory](https://github.com/gohugoio/hugo/issues/1240) and put the image and the post (named `index.md`) in there (you can find examples in the docs already, f.e. the cognito service docs).

  Then you can use the usual markdown syntax with a relative path (f.e.:
  `![Alternative_Text](file_next_to_post.png)`).

  If you want to resize the image, use the `figure` shortcode.

PS.: Feel free to add more best practices here (also give us a heads-up in [#sig-docs](https://localstack-cloud.slack.com/archives/C02FZH6UB2A)).
