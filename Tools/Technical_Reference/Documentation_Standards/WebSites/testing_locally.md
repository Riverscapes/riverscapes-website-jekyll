---
title: Testing Sites Locally
---

It's always a good idea to verify changes locally before pushing them to GitHub. This avoids potentially breaking a site, or having to a push simply to visualize your work (only to realize a minor typo and then stage-commit-push a second time). To do this you need to run Jekyll locally on your computer and then point your browser at your localhost. Unfortunately Jekyll is coded in Ruby which can be tricky to install on Windows. Follow these one-time set-up instructions then at the bottom, the new command for running a Jekyll site from your computer:

### Check if Ruby is installed

1. [Open a DOS command Window](https://www.isunshare.com/windows-10/4-ways-to-open-command-prompt-in-windows-10.html) (press the Windows key and then type `cmd` and hit enter)
1. Type the command `ruby --version` to check if you have Ruby installed and which version you might be running.
1. If you get "command not found" because Ruby is not installed then proceed to the next section. 
1. We need a Ruby version that's equal to or newer than 2.1.0 so reinstall Ruby if you have an older version.

### Install Ruby (if necessary)

1. Download the [Ruby installer](https://rubyinstaller.org/downloads). You want: Ruby+devkit 2.6.4 (exact number doesn't matter. Just choose the greatest Ruby+Devkit version)
1. Run the installer and choose all the default choices.
1. When the command line choice comes up choose **Base installation**

```
   1 - MSYS2 base installation        <------ choose this one: (1)
   2 - MSYS2 system update (optional)
   3 - MSYS2 and MINGW development toolchain
```
At the second prompt just hit ENTER to get out.

Now go back to **Step 1: Check Version of Ruby**. There's no point in proceeding if you're running an old version or the installation failed.

### Install Bundler

Back at the DOS command window, type the following command:

```
gem install bundler
```

### Site-level (Do this for every site you want to serve locally)

1. Open a DOS command window in the `/docs` folder of the site you want to serve.
1. Run the following command to install all the necessary components needed for the current site:

```
bundler install
```

### Serving a site locally

With the one-time steps above complete, you're good to go. You shouldn't have to run bundler install again and can just run the following command every time you want to serve a site:

```
bundle exec jekyll serve
```
