# LocalStack Docs

Repository for [docs.localstack.cloud](https://docs.localstack.cloud).


## Getting Started

### Basics

LocalStack Docs is using the following technology stack:
- [Hugo](https://gohugo.io) to generate the static site.
- [Docsy](https://docsy.dev) as a theme for Hugo.
- [GitHub Pages](https://pages.github.com/) to automatically deploy every commit on the `main` branch of this repository on [docs.localstack.cloud](https://docs.localstack.cloud).


### Clone the repo

Clone this repository and initialize the Git submodules recursively (`themes/docsy` is a submodule that again has submodules for vendored assets like fontawesome).

    git clone --recurse-submodules --depth 1 git@github.com:localstack/docs.git

This performs a shallow clone, which leads to only the main branch being configured for your remote.
To be able to pull/push from/to all branches, please run:

    git config remote.origin.fetch "+refs/heads/*:refs/remotes/origin/*" && git fetch

or:

    git clone git@github.com:localstack/docs.git
    cd docs
    git submodule update --init --recursive


### Install Hugo

LocalStack Docs is based on the [Hugo static site generator](https://gohugo.io).

In order to contribute to LocalStack Docs, you need to [install Hugo](https://gohugo.io/getting-started/installing) in order to verify your changes. Make sure to install the _extended_ version of Hugo.
You also need to make sure that `go` is installed in order to run hugo scripts. 


### Run locally

Once you have Hugo installed, you can start your local server with the following command:

    hugo serve

or run in developer mode with automatic reload:

    hugo serve --watch=true --disableFastRender -D

Once the server is started, the locally served Docs are available at http://localhost:1313.


### Writing content

The whole site is generated with Hugo, a powerful static-site generator.

You can find an extensive documentation on how to use Hugo [in their docs](https://gohugo.io/documentation/), however most of the content is written in plain Markdown.

Make sure to follow the best practices below when contributing content.

#### Updating developer hub applications
While contributing to the developer hub applications page i.e. editing `data/developerhub/applications.json` file, make sure to run the `create-applications.js` script in the `scripts` folder to create new application pages.

Example usage in the project root:

    node scripts/create-applications.js


## Best Practices

Please follow these best practices when writing documentation in this repository:
- **Stick to markdown** wherever possible.
- **One sentence per line:** Use one line for each sentence in markdown.
  Unless you add a backslash at the end of the line or add two new-lines, there won't be linebreak in the rendered text.
- **Commands:** Use the `command` shortcode for all one-line commands (also when their output is presented).
  Do not use it for bash scripts with comments.
  You can find a more detailed description here: https://github.com/localstack/docs/pull/55.
  If needed, you can also [highlight a specific line](https://gohugo.io/content-management/syntax-highlighting/#highlighting-in-code-fences).
- **Internal links:** Use the [`ref` or `relref` shortcode](https://gohugo.io/content-management/cross-references/#use-ref-and-relref) when creating non-external links (but still use the markdown native image linking, ref doesn't work there).
  You can either use `ref` or `relref`, the point is to have compile time internal-link checks (which works for both).
- **Code snippets:** For snippets, make sure you indicate the programming/markup language so that proper syntax highlighting is used.
  Use `bash` only for Bash scripts, and use `text` for shell outputs or command examples.
  The full list of the supported languages [here](https://gohugo.io/content-management/syntax-highlighting/).
  If needed, you can also [highlight a specific line](https://gohugo.io/content-management/syntax-highlighting/#highlighting-in-code-fences) in the snippet.
- **Images:** If you want to use images in your post, create a new [leaf bundle directory](https://github.com/gohugoio/hugo/issues/1240) and put the image and the post (named `index.md`) in there (you can find examples in the docs already, f.e. the cognito service docs).
  Then you can use the usual markdown syntax with a relative path (f.e.: `![Alternative_Text](file_next_to_post.png)`).
  If you want to resize the image, use the `figure` or `img` shortcode, for example: `{{< img src="cockpit-init-check.png" class="img-fluid shadow rounded" width="150px" >}}`
- **Callouts:** Use these to make content stand out.
  The `callout` shortcode supports `note` (default), `tip` and `warning` levels.
  Use it like so:
  ```
  {{< callout "warning" >}}
  This will make your computer halt and catch fire!
  {{< /callout >}}
  ```


## Troubleshooting

This section covers common issues when working with LocalStack Docs:

### Missing shortcodes

Example error:
```
Start building sites …
hugo v0.88.1-5BC54738+extended linux/amd64 BuildDate=2021-09-04T09:39:19Z VendorInfo=gohugoio
Error: Error building site: "/home/localstack/Repos/docs-test/content/en/get-started/_index.md:57:1": failed to extract shortcode: template for shortcode "alert" not found
Built in 45 ms
```

1. Make sure to correctly clone and initialize the git submodules of this repo. For details see the section "[Clone the repo](#clone-the-repo)" above.
2. Delete the Hugo Module cache using `hugo mod clean` or `make clean`.
