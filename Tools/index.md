---
title: Tools
index: 1
---

<img class="float-left" src="{{ site.baseurl }}/assets/images/rc/tool.png">The RC has been prolific in developing and vetting the [science]({{ site.baseurl }}/publications) and theoretical underpinnings essential to understanding and explaining how riverscapes work and are organized across a range of nested hierarchical spatial scales. We have also committed to building [open-source algorithms](https://github.com/Riverscapes) <i class="fa fa-github" aria-hidden="true"></i> tools to make it easier for researchers, professionals, practitioners and students to apply those concepts to their own riverscapes. 

All of our tools are based on [peer-reviewed]({{ site.baseurl }}/Science/publications) ), methods. When we have developed the methods ourselves, we aim to have them vetted, published and disseminate in the [peer-reviewed literature]({{ site.baseurl }}/Science/publications). We then also make sure to have a well documented website (typically with a URL that will take the form of `sometool.riverscapes.xyz`). For most users, the online help documentation and using the [tool]({{ site.baseurl }}/Tools)  'as is' is as far as they need to take it. However, for those so inclined, all of the underlying source-code for these tools, models and algorithms is available in its own GitHub <i class="fa fa-github" aria-hidden="true"></i> repository at [github.com/Riverscapes](https://github.com/Riverscapes).

## Riverscapes Compliant
<img class="float-right" src="{{ site.baseurl }}/assets/images/rc/RiverscapesCompliant_128.png">
Tools are designated as "*riverscapes-compliant*" <img  src="{{ site.baseurl }}/assets/images/rc/RiverscapesCompliant_24.png"> when they meet the following criteria:
- [Tool Status]({{ site.baseurl }}/Tools/status) of Research-Grade or Higher
- Code produces [riverscapes projects]({{ site.baseurl }}/Tools/Technical_Reference/Documentation_Standards/Riverscapes_Projects/) as output of all analyses
- Project Type is registered with [`program.xml`]({{ site.baseurl }}/Tools/Technical_Reference/Documentation_Standards/Riverscapes_Projects/Program/) in [Program Repo](https://github.com/Riverscapes/Program)  
- Has been vetted by the RS Science Committee


## Riverscapes Compliant Tools

|---|---|---|---|---|---|
| |Resolution|Extent|Language|[Interface]({{ site.baseurl }}/Tools/#interface)|[Status]({{ site.baseurl }}/Tools/#tool-status)|
|---|---|---|---|---|---|
|**Reach Scale Tools**||||||
|[GCD - Geomorphic Change Detection](http://gcd.riverscapes.xyz/)|Cell|Reach|C#|<i class="fa fa-desktop" aria-hidden="true"></i> , <img src="{{ site.baseurl }}/assets/images/tools/esri_icon.png">, <i class="fa fa-terminal" aria-hidden="true"></i>|Production|
|[GUT - Geomorphic Unit Toolkit](http://gut.riverscapes.xyz/)|Cell|Reach|Python|<i class="fa fa-terminal" aria-hidden="true"></i>, <img src="{{ site.baseurl }}/assets/images/tools/ArcPyToolbox.png">|Research Grade|
|[FHM - Fish Habitat Model](http://habitat.northarrowresearch.com/)|Cell|Reach|C#/C++|<i class="fa fa-desktop" aria-hidden="true"></i> |Operational|
|**Network Scale Tools**||||||
|[BRAT - Beaver Restoration Assessment Tool](http://brat.riverscapes.xyz/)|Reach|Network|Python|<img src="{{ site.baseurl }}/assets/images/tools/ArcPyToolbox.png">|Research-Grade|
|[RCAT - Riparian Condition Assessment Tool](http://rcat.riverscapes.xyz/)|Reach|Network|Python|<img src="{{ site.baseurl }}/assets/images/tools/ArcPyToolbox.png">|Research-Grade|
|[GNAT - Geomorphic Network Assessment Tool](http://gnat.riverscapes.xyz/)|Reach|Network|Python|<img src="{{ site.baseurl }}/assets/images/tools/ArcPyToolbox.png">|Research-Grade|
|**Utilities**||||||
|[RAVE - Riverscapes Analysis Visualization Explorer](http://rave.riverscapes.xyz)|Any|Any|C#|<img src="{{ site.baseurl }}/assets/images/tools/esri_icon.png">|Production|
|**Legacy CHaMP Tools**||||||
|[CHaMP Topo Processing Tools](http://champtools.northarrowresearch.com/)|Reach|Reach|Python|<img src="{{ site.baseurl }}/assets/images/tools/esri_icon.png">|Production|
|[CHaMP Topo Metrics](https://github.com/SouthForkResearch/CHaMP_Metrics/wiki)|Reach|Network|Python|<img src="{{ site.baseurl }}/assets/images/tools/ArcPyToolbox.png">|Operational|


### Popular Reach-Scale Tools

-----
## Tools Pending Riverscapes Compliance

<img class="float-right" src="{{ site.baseurl }}/assets/images/rc/RiverscapesCompliantPending_128.png">
Tools are designated as "*pending riverscapes-compliance*" <img  src="{{ site.baseurl }}/assets/images/rc/RiverscapesCompliantPending_28.png"> when the RS Science Committee has accepted the tool for consideration and they meet the following criteria:
- [Tool Status]({{ site.baseurl }}/Tools/status) of Prototype or Higher
- Developer has indicated intent to modify code to produce [riverscapes projects]({{ site.baseurl }}/Tools/Technical_Reference/Documentation_Standards/Riverscapes_Projects/) as output of all analyses
- Developer has indicated intent to add Project Type registration with [`program.xml`]({{ site.baseurl }}/Tools/Technical_Reference/Documentation_Standards/Riverscapes_Projects/Program/) in [Program Repo](https://github.com/Riverscapes/Program) 


|---|---|---|---|---|---|
| |Resolution|Extent|Language|[Interface]({{ site.baseurl }}/Tools/#interface)|[Status]({{ site.baseurl }}/Tools/#tool-status)|
|---|---|---|---|---|---|
|**Reach Scale Tools**||||||
|[Fluvial Coridor Toolbox](https://github.com/EVS-GIS/Fluvial-Corridor-Toolbox-ArcGIS)|Cell|Reach|Python|<img src="{{ site.baseurl }}/assets/images/tools/ArcPyToolbox.png"> , <img src="{{ site.baseurl }}/assets/images/tools/QGIS_bw_24.png">|Operational|
|[MoRPHED - Model of Riverine Physical Habitat & Ecogeomorphic Dynamics](http://morphed.joewheaton.org/)|Cell|Reach|C++|<i class="fa fa-desktop" aria-hidden="true"></i> |Research Grade|
|[NREI - Net Rate of Energy Intake](https://github.com/Riverscapes/NREI)|Cell|Reach|R|<i class="fa fa-terminal" aria-hidden="true"></i>|Research Grade|
|[TAT - Topographic Analyis Toolkit](https://github.com/Riverscapes/NREI)|Cell|Reach|R|<img src="{{ site.baseurl }}/assets/images/tools/esri_icon.png">|Operational|
|[ToPCAT - Topographic Point Cloud Analysis Toolkit](https://github.com/Riverscapes/NREI)|Cell|Reach|R|<img src="{{ site.baseurl }}/assets/images/tools/esri_icon.png">|Opeartional|
|[ToPCAT - Topographic Point Cloud Analysis Toolkit](https://github.com/Riverscapes/NREI)|Cell|Reach|R|<img src="{{ site.baseurl }}/assets/images/tools/esri_icon.png">|Research|
|**Network Scale Tools**||||||
|[CASCADE Toolbox](http://cascade.deib.polimi.it/)|Reach|Network|Matlab| <i class="fa fa-desktop" aria-hidden="true"></i> |Opperational|
|[Catchment Tool](https://riverscapes.github.io/CatchmentTool/)|Reach|Network|Python|<img src="{{ site.baseurl }}/assets/images/tools/ArcPyToolbox.png">|Prototype|
|[Conductivity Tools](https://riverscapes.github.io/Conductivity/)|Reach|Network|Python|<img src="{{ site.baseurl }}/assets/images/tools/ArcPyToolbox.png">|Prototype|
|[GNAT - Geomorphic Network Assessment Tool](http://gnat.riverscapes.xyz/)|Reach|Network|Python|<img src="{{ site.baseurl }}/assets/images/tools/ArcPyToolbox.png">|Research Grade|
|[Grain Size Tool](https://github.com/Riverscapes/grain-size-tool)|Reach|Network|Python|<img src="{{ site.baseurl }}/assets/images/tools/ArcPyToolbox.png">|Prototype|
|[Network Profiler Tool](https://riverscapes.github.io/NetworkProfiler/)|Reach|Network|Python|<img src="{{ site.baseurl }}/assets/images/tools/QGIS_bw_24.png">|Prototype|
|[Solar Stream Tools](https://riverscapes.github.io/SolarStream/)|Reach|Network|Python|<img src="{{ site.baseurl }}/assets/images/tools/ArcPyToolbox.png">|Prototype|
|[Tributary Impact](http://tributaryimpact.riverscapes.xyz/)|Reach|Network|Python|<img src="{{ site.baseurl }}/assets/images/tools/ArcPyToolbox.png">|Prototype|
|[WRAT - Wood Restoration Assessment Tool](https://github.com/Riverscapes/WRAT)|Reach|Network|Python|<img src="{{ site.baseurl }}/assets/images/tools/ArcPyToolbox.png">|Prototype|
|**Catchment Scale Tools**||||||
|[Connectivity Index](https://github.com/HydrogeomorphologyTools/Connectivity-Index-ArcGIS-toolbox)|Cell|Catchment|Python|<img src="{{ site.baseurl }}/assets/images/tools/ArcPyToolbox.png">|Research Grade|
|[SedInConnect](https://github.com/HydrogeomorphologyTools/SedInConnect_2.3)|Cell|Catchment|Python|<i class="fa fa-desktop" aria-hidden="true"></i> |Operational|
|**Utilities**||||||
|[PointCloud2Raster](https://github.com/NorthArrowResearch/pointcloud2raster)|Point|Reach|C++|<i class="fa fa-terminal" aria-hidden="true"></i>|Prototype|
|[PySESA - Spatially Explicit Spectral Analysis](https://github.com/dbuscombe-usgs/pysesa)|Point|Reach|Python|<i class="fa fa-terminal" aria-hidden="true"></i>|Research Grade|
|[RasterMan](https://github.com/NorthArrowResearch/rasterman)|Cell|Catchment|C++|<i class="fa fa-terminal" aria-hidden="true"></i>|Research Grade|
|**Legacy CHaMP Tools**||||||
|[CTT - CHaMP Transformation Tool](http://ctt.riverscapes.xyz/index.html)|Cell|Reach|C#|<img src="{{ site.baseurl }}/assets/images/tools/esri_icon.png">|Production|
|[CHaMP Topo Processing Tools](http://champtools.northarrowresearch.com/)|Reach|Reach|Python|<i class="fa fa-desktop" aria-hidden="true"></i> |Production|
|[CHaMP Workbench](http://workbench.northarrowresearch.com/)|Any|Any|C#|<i class="fa fa-desktop" aria-hidden="true"></i> |Operational|
|[CHaMP Hydraylic-Modelling Delft3D Automation](https://github.com/SouthForkResearch/Hydraulic-Modeling/wiki)|cell|Reach|R/C|<i class="fa fa-terminal" aria-hidden="true"></i>|Operational|

<i class="fab fa-creative-commons-zero"></i>


# Model Discrimination
The following concpets are helpful for discriminating model types.

## Interface

RC tools are deployed to users thorugh a variety of interfaces:
* <img src="{{ site.baseurl }}/assets/images/tools/esri_icon.png"> :  [ArcGIS AddIn](https://desktop.arcgis.com/en/arcmap/10.7/guide-books/python-addins/sharing-and-installing-add-ins.htm)  ArcGIS [AddIn Toolbar](https://desktop.arcgis.com/en/arcmap/10.7/analyze/python-addins/sharing-and-installing-add-ins.htm) in ArcGIS
* <img src="{{ site.baseurl }}/assets/images/tools/ArcPyToolbox.png">:  [ArcPy Toolbox in ArcGIS](https://desktop.arcgis.com/en/arcmap/10.7/analyze/creating-tools/a-quick-tour-of-python-toolboxes.htm)
* <img src="{{ site.baseurl }}/assets/images/tools/QGIS_bw_24.png"> [QGIS Plugin](https://plugins.qgis.org/) = Toolbar in [QGIS](https://qgis.org)
* <i class="fa fa-terminal" aria-hidden="true"></i> : CLI = [Command Line Interface](https://en.wikipedia.org/wiki/Command-line_interface)
* <i class="fa fa-desktop" aria-hidden="true"></i> : GUI = [Graphical User Interface](https://en.wikipedia.org/wiki/Graphical_user_interface)
* <i class="fa fa-chrome" aria-hidden="true"></i>: Web = interactive web site
* <img  src="{{ site.baseurl }}/assets/images/data/api_24.png"> : API = [Application Programming Interface](https://en.wikipedia.org/wiki/Application_programming_interface)
* <img src="{{ site.baseurl }}/assets/images/tools/PWA.png">:  PWA = [Progressive Web App](https://en.wikipedia.org/wiki/Progressive_web_application)

Most tools have just one deployment interface, some have multiple. 

## Tool Status
We classify the status of our tools according to their growth from innovative research ideas, through operational tools that (with a little love) can be run more broadly to professional tools that are robust and usable by any user in very diffferent settings.

Our RC Techncial Committee ranks the status of tools using the following criteria:

The status of tools. The same adjectives for ‘tools’ can be applied to the overall model or family of commands within in a tool or specific commands within a toolbar. 

| Tool Status | Technological<br>Readiness Level | Source Code <br>Documentation | Open Source | User <br>Documentation | Easy User <br>Interface |  |
|--------------------|:--------------------------------:|:-------------------------------------------------------------:|:-------------------------------------------------------:|:-------------------------------------------------------:|-------------------------|---|
| Concept | TR1 | <i class="fa fa-exclamation-triangle" aria-hidden="true"></i> |  |  |  |  |
| Proof of Concept | TR2 | <i class="fa fa-exclamation-triangle" aria-hidden="true"></i> |  |  |  |  |
| Research-Grade | TR3 | <i class="fa fa-check-square-o" aria-hidden="true"></i> |  |  |  |  |
| Operational | TR4 | <i class="fa fa-check-square-o" aria-hidden="true"></i> | <i class="fa fa-check-square-o" aria-hidden="true"></i> | <i class="fa fa-check-square-o" aria-hidden="true"></i> |  |  |
| Professional-Grade | TR5 | <i class="fa fa-check-square-o" aria-hidden="true"></i> | <i class="fa fa-check-square-o" aria-hidden="true"></i> | <i class="fa fa-check-square-o" aria-hidden="true"></i> |  |  |
| Production-Grade | TR6 | <i class="fa fa-check-square-o" aria-hidden="true"></i> | <i class="fa fa-check-square-o" aria-hidden="true"></i> | <i class="fa fa-check-square-o" aria-hidden="true"></i> |  |  |
| Commercial-Grade | TR7 | <i class="fa fa-check-square-o" aria-hidden="true"></i> | <i class="fa fa-check-square-o" aria-hidden="true"></i> | <i class="fa fa-check-square-o" aria-hidden="true"></i> |  |  |

<i class="fa fa-exclamation-triangle" aria-hidden="true"></i> - No  
<i class="fa fa-check-square-o" aria-hidden="true"></i> - Yes

1. **Concept** - A tool in which the algorithm has been developed, the method proposed, and perhaps it has been manually implemented, but it has not been packaged into a ‘tool’, which others can apply.
2. **Proof of Concept** - A tool in which the algorithm has been developed, but it has not been fully documented and may only work with particular data types.
3. **Research Grade** - A tool that has been developed into a reusable piece of code, that the analysts or developers can apply, but has not been well documented, is not yet distributable, and generally lacks a wrapper, toolbox, or GUI to make it easy for others to apply. Such prototype tools also are generally simple scripts (e.g. in Python or R), which have not yet been written a manner that facilitates easy batch processing nor has it been optimized for computational efficiency.
4. **Operational** - A tool that can be applied by other analysts and is ready for limited distribution, but does not necessarily have a polished, easy-to-use user interface. Such tools are good for one-off analyses (e.g. network analysis), and generally acceptable to be used by the team of CHaMP/ISEMP analysts and partners. Operational tools all have the source code in an open-source GIT repository with code documentation, and have at least a basic help website available with basic background and tutorials.
5. **Professional**
6. **Production** - A tool that has both been optimized for batch processing and running over entire CHaMP domain (typically on AWS). These tools produce outputs that can be viewed, manipulated and re-run in the operational tools. 
7. **Commercialized** - A tool that has at least ‘operational’ , but potentially also ‘production’ status that also has a well developed user interface (GUI) that allows non-expert consumers of the products to view the outputs either in the tool or in the Analyst Toolbar. Production-level tools also generally are backed up by methods that have been vetted in the literature and may even have a publication specifically on this tool. 

These ideas are based on the concept of [Technological Readiness Level](https://www.twi-global.com/technical-knowledge/faqs/technology-readiness-levels)

<div class="responsive-embed">
<img src="https://www.twi-global.com/image-library/FAQs/Technology-Readiness-Level-TRL-Infographic.jpg"></div>