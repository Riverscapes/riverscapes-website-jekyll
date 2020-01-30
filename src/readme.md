This folder contains helper scripts that generate or manipulate content
within the riverscapes-website Jekyll site.

The first script, citations.py, calls the Zotero API and writes the
list of citations within a Zotero "group" library and writes them to
the publications.md file within this repository.

To run this script you need to create a file called .env in the src
folder of this repo. There is a file called .env_TEMPLATE that you
can copy and use as a starting point. Then populate the .env file
with the Zotero Library ID (this is part numeric slug within the URL
of the library when viewing it in Zotero online) and your user API key
that can be found (or generated within your settings page within Zotero
online.

Then run the citations.py script providing the path to where the 
citations should be written. Typically its up one level from the src
folder in a file called publications.md

You can optionally provide a boiler plate file that contains markdown
that will be injected into the output file before the list of citations.