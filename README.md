This repo contains the main Riverscapes web site.


## Working locally

To get the latest theme:

```
bundle update
```

To autobuild and serve the site locally

```
bundle exec jekyll serve
```

### Folder layout

Some special folders:

* `_site`: You may or may not see this. It is the compiled site on your local and should be ".gitignored".
* `assets`: this is where images, fonts, javascript and compiled CSS lives. Don't ever change CSS code here since it gets overwritten.
* `src`: helper scripts to generate or manipulate content within the site.

Some special files:

* `_config.yml` This is the configuration for your site. it tells Jekyll what the site name is, what flavour of markdown to use and what the default template is.
