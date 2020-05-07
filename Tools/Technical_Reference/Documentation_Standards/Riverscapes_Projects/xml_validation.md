---
title: XML Validation
---

Riverscapes relies heavily on several different [Extensible Markup Language](https://en.wikipedia.org/wiki/XML) (XML) files. They are used to define the individual projects, the data warehouses that store these projects and also how projects are displayed in [RAVE](http://rave.riverscapes.xyz/).

Each of these types of XML have a different set of rules that define the tag names, attributes and how these are laid out in the file. These rules are defined in a [XSD schema file](https://en.wikipedia.org/wiki/XML_schema) that is available online.

Whenever a person is writing an XML file by hand, or writing code to do so it is absolutely vital that they validate that the XML produced fully validates with the XSD schema file. In other words, XML files should be validated against the XSD file to check for errors and omissions. This process will check that all tag names are valid, that the required tags are present and that the nesting of all the tags meets the rules.

There are lots of tools available for validating XML. Indeed, most modern Integrated Development Environments (IDE) software can perform this task. And there are even online tools for doing it, although they tend rely on the files being uploaded and so only work on one file at a time.

Our preferred tool for validating XML is Microsoft's free [Visual Studio Code](https://code.visualstudio.com/). The following instructions describe how to configure and perform XML validation. A [video description](#video-demonstration) at the bottom of this page walks through these steps.

# Prerequisites

1. Install [Visual Studio Code](https://code.visualstudio.com/)
1. Install [Java Development Kit](https://developers.redhat.com/products/openjdk/download?sc_cid=701f2000000RWTnAAO) (JDK). On Windows it's recommended that you download and use the MSI installer to walk through the installation. At the time of writing the `jdk-8u252-x64 MSI` is the most appropriate download.
1. Install Red Hat XML Tools.
    1. Open Visual Studio Code.
    1. Switch to the extension Marketplace.
    1. Search for "Red Hat XML Tools".
    1. Click Install.
    1. Restart Visual Studio Code.

# XML Validation

Open the XML file that you want to validate. Ensure that the XML file refers to a schema namespace in the root XML tag of the file. Here's an example of a riverscapes project file referrring to the XSD file online in the GitHub repository. The namespace reference is on line 3:

```xml
<?xml version="1.0"?>
<Project xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance"
xsi:noNamespaceSchemaLocation="https://raw.githubusercontent.com/NorthArrowResearch/riverscapes-programs/master/Projects/BRAT/XSD/V1/Project.xsd">
	<Name>Riverscapes Context for HUC 17120007</Name>
	<ProjectType>RSContext</ProjectType>
	<Warehouse><Meta name="id">3f286d71-6191-4f5b-a6fc-468759e7f18e</Meta><Meta name="user">eeb79d24-68b5-405a-be55-8e23fdf929dc</Meta><Meta name="program">Anabranch</Meta></Warehouse><MetaData>
		<Meta name="ModelVersion">1.0.0</Meta>
		<Meta name="dateCreated">2020-05-06T12:29:43.807018</Meta>
		<Meta name="dateCreated">2020-05-06T12:29:43.817540</Meta>
		<Meta name="HUC8">17120007</Meta>
		<Meta name="Watershed">Warner Lakes</Meta>
	</MetaData>
	<Realizations>
....
```

Open the terminal pane (CTRL+J on Windows) and switch to the "Problems" tab. Any problems with the XML should be underlined in red and also appear in this Problems pane. Test that validation is working by writing some invalid XML (either a nonsense tag name or deleting an angle bracket etc.).

# Helpful Features

1. When typing XML tags use intellisense (CTRL+Space) to suggest valid tags and attributes.
1. Right click anywhere in the XML file to "reformat" the document. This will reindent the nested tags.

# Video Demonstration

<div class="responsive-embed">
<iframe width="560" height="315" src="https://www.youtube.com/embed/HMw2ki-bauQ" frameborder="0" allow="accelerometer; autoplay; encrypted-media; gyroscope; picture-in-picture" allowfullscreen></iframe>
</div>