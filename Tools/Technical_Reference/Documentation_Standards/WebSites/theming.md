---
title: Theming a Tool Web Site
weight: 6
---

We have developed a single theme that controls the look and feel of sites related to riverscapes. It's the theme that's applied to this site. If you have a Riverscapes site that doesn't look like this page or is missing page elements used on this site, then you need to follow the instructions below.

These instructions describe how to apply this theme to both a new site, or update the theme for an existing site. The steps are manual and somewhat fiddly. Remember to review your changes in git before commiting them. You can always [run Jekyll locally](jekyll_toolbox.html#running-jekyll-locally) to ensure that your changes have not broken the site.

## Before You Start

You are going to need a copy of the Riverscapes **[riverscapes-jekyll-theme](https://github.com/Riverscapes/riverscapes-jekyll-theme)** repo. You can either use the green `Clone or Download` button on the [repo's GitHub web page](https://github.com/Riverscapes/riverscapes-jekyll-theme), or you can use git to clone down the repo. Regardless, make sure that you have the **latest version**. This theme will change from time to time.

Now you are ready to apply the theme to your site. Choose the section below that applies to you. If your site has never had the Riverscapes theme applied to it before, then choose [Theming a New Site](#theming-a-new-web-site). If your site has some past version of the Theme applied, or you're unsure if it's up to date, then jump to the [Updating a Site That's Already Themed](#updating-a-site-thats-already-themed) section.


# Theming a New Web Site

These instructions assume that you have already [created your GitHub web site]({{ site.baseurl }}/Technical_Reference/Documentation_Standards/WebSites/#creating-a-web-site).

If you are unsure about any of these instructions then you can there is a [sample site available that can be used as a template](https://github.com/Riverscapes/riverscapes-jekyll-theme/tree/master/docs). Simply copy the contents of this docs folder into your repo and start from there.

1. Create a file in your docs folder called `_config.yml` and cut and paste the [site configuration](https://raw.githubusercontent.com/Riverscapes/riverscapes-jekyll-theme/master/docs/_config.yml) into it.
1. Edit the `_config.yml` file and change the following:
    1. Change the title to the name of your tool
    1. Change the description.
    1. Change the URL to where your site is served.
1. Create a file in your docs folder called `Gemfile` and cut and paste the [ruby gem configuration](https://raw.githubusercontent.com/Riverscapes/riverscapes-jekyll-theme/master/docs/_config.yml) into it.
1. Create a file called `.gitignore` and cut and paste the [git ignore contents](https://raw.githubusercontent.com/Riverscapes/riverscapes-jekyll-theme/master/docs/.gitignore).
1. Create a folder called `assets`.
1. Inside the assets folder create a folder called `images`. Put all the images for your site in here.
1. Commit the changes to your repo on the master branch and then push.

# Advanced Theming Topics

## Sidebar

You can add content to the left side of every page in a site by creating a file called `sidebar.html` inside a folder called `_includes` inside your docs folder. i.e. at the path (`/docs/_includes/sidebar.html`). Inside this file you can write any HTML you want and it will get injected into every page of the site underneath the site navigation panel.

## Custom CSS

You can extend the styling of a site by creating a file called `custom.css` at the location `/docs/assets/css`. The riverscapes theme already includes the following web libraries that you can use in your customizations:

* [Foundation](https://foundation.zurb.com/)
* [Font Awesome 4.7](https://fontawesome.com/v4.7.0/) (note the version number)


## Updating your favicon

Favicons are little graphics that web browsers display on the browser tab beside the site title:

![favicon](/assets/images/favicon_demo.png)

Favicons used to be simple. Things have gotten more complicated, what with all the various devices and resolutions on which people could be viewing your site. Here's how you generate your own:

1. Find a nice sized copy of your logo that is square. A high quality image is most important, but also try to avoid images greater than 500 pixels across to avoid image distortion.
1. Go to a service like <http://www.favicon-generator.org> and upload your icon. It will generate lots images in various sizes. Use all 27 of these files in the folder to overwrite the files in `assets/images/favicons`. Make a comit and push to master. 
