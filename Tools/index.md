---
title: Tools
index: 1
---

<img class="float-left" src="{{ site.baseurl }}/assets/images/rc/tool.png">The RC has been prolific in developing and vetting the [science]({{ site.baseurl }}/publications) and theoretical underpinnings essential to understanding and explaining how riverscapes work and are organized across a range of nested hierarchical spatial scales. We have also committed to building [open-source algorithms](https://github.com/Riverscapes) <i class="fa fa-github" aria-hidden="true"></i> tools to make it easier for researchers, professionals, practitioners and students to apply those concepts to their own riverscapes. 

All of our tools are based on [peer-reviewed]({{ site.baseurl }}/Science/publications) ), methods. When we have developed the methods ourselves, we aim to have them vetted, published and disseminate in the [peer-reviewed literature]({{ site.baseurl }}/Science/publications). We then also make sure to have a well documented website (typically with a URL that will take the form of `sometool.riverscapes.xyz`). For most users, the online help documentation and using the [tool]({{ site.baseurl }}/Tools)  'as is' is as far as they need to take it. However, for those so inclined, all of the underlying source-code for these tools, models and algorithms is available in its own GitHub <i class="fa fa-github" aria-hidden="true"></i> repository at [github.com/Riverscapes](https://github.com/Riverscapes).

## Riverscapes Compliant
<img class="float-right" src="{{ site.baseurl }}/assets/images/rc/RiverscapesCompliant_128.png">
Tools are designated as "*riverscapes-compliant*" <img  src="{{ site.baseurl }}/assets/images/rc/RiverscapesCompliant_24.png"> when they meet the following criteria:
- [Tool Status]({{ site.baseurl }}/Tools#tool-status) of **Operational-Grade** or Higher
- Code produces [riverscapes projects]({{ site.baseurl }}/Tools/Technical_Reference/Documentation_Standards/Riverscapes_Projects/) <img  src="{{ site.baseurl }}/assets/images/data/RiverscapesProject_24.png"> as output of all analyses
- Project Type is registered with [`program.xml`]({{ site.baseurl }}/Tools/Technical_Reference/Documentation_Standards/Riverscapes_Projects/Program/) in [Program Repo](https://github.com/Riverscapes/Program)  
- Has been vetted by the RS Science Committee


## Riverscapes Compliant Tools

|---|---|---|---|---|---|
| |Resolution|Extent|Language|[Interface]({{ site.baseurl }}/Tools/#interface)|[Status]({{ site.baseurl }}/Tools/#tool-status)|
|---|---|---|---|---|---|
|**Reach Scale Tools**||||||
|[GCD - Geomorphic Change Detection](http://gcd.riverscapes.xyz/)|Cell|Reach|C#|<i class="fa fa-desktop" aria-hidden="true"></i> , <img src="{{ site.baseurl }}/assets/images/tools/esri_icon.png">, <i class="fa fa-terminal" aria-hidden="true"></i>| Professional-Grade: <i class="fa fa-desktop" aria-hidden="true"></i> & <img src="{{ site.baseurl }}/assets/images/tools/esri_icon.png">; Production-Grade: <i class="fa fa-terminal" aria-hidden="true">|
|[GUT - Geomorphic Unit Toolkit](http://gut.riverscapes.xyz/)|Cell|Reach|Python|<i class="fa fa-terminal" aria-hidden="true"></i>, <img src="{{ site.baseurl }}/assets/images/tools/ArcPyToolbox.png">|Research-Grade|
|[FHM - Fish Habitat Model](http://habitat.northarrowresearch.com/)|Cell|Reach|C#/C++|<i class="fa fa-desktop" aria-hidden="true"></i> |Operational-Grade|
|**Network Scale Tools**||||||
|[BRAT - Beaver Restoration Assessment Tool](http://brat.riverscapes.xyz/)|Reach|Network|Python|<img src="{{ site.baseurl }}/assets/images/tools/ArcPyToolbox.png">|Research-Grade|
|[RCAT - Riparian Condition Assessment Tool](http://rcat.riverscapes.xyz/)|Reach|Network|Python|<img src="{{ site.baseurl }}/assets/images/tools/ArcPyToolbox.png">|Research-Grade|
|[GNAT - Geomorphic Network Assessment Tool](http://gnat.riverscapes.xyz/)|Reach|Network|Python|<img src="{{ site.baseurl }}/assets/images/tools/ArcPyToolbox.png">|Research-Grade|
|**Utilities**||||||
|[RAVE - Riverscapes Analysis Visualization Explorer](http://rave.riverscapes.xyz)|Any|Any|C#|<img src="{{ site.baseurl }}/assets/images/tools/esri_icon.png">|Production|
|**Legacy CHaMP Tools**||||||
|[CHaMP Topo Processing Tools](http://champtools.northarrowresearch.com/)|Reach|Reach|Python|<img src="{{ site.baseurl }}/assets/images/tools/esri_icon.png">|Production-Grade|
|[CHaMP Topo Metrics](https://github.com/SouthForkResearch/CHaMP_Metrics/wiki)|Reach|Network|Python|<img src="{{ site.baseurl }}/assets/images/tools/ArcPyToolbox.png">|Production-Grade|


### Popular Reach-Scale Tools

-----
## Tools Pending Riverscapes Compliance

<img class="float-right" src="{{ site.baseurl }}/assets/images/rc/RiverscapesCompliantPending_128.png">
Tools are designated as "*pending riverscapes-compliance*" <img  src="{{ site.baseurl }}/assets/images/rc/RiverscapesCompliantPending_28.png"> when the RS Science Committee has accepted the tool for consideration and they meet the following criteria:
- [Tool Status]({{ site.baseurl }}/Tools#tool-status) of **Resarch-Grade** or higher
- Developer has indicated intent to modify code to produce [riverscapes projects]({{ site.baseurl }}/Tools/Technical_Reference/Documentation_Standards/Riverscapes_Projects/) as output of all analyses - Moving up to **Operational-Grade**
- Developer has indicated intent to add Project Type registration with [`program.xml`]({{ site.baseurl }}/Tools/Technical_Reference/Documentation_Standards/Riverscapes_Projects/Program/) in [Program Repo](https://github.com/Riverscapes/Program) 


|---|---|---|---|---|---|
| |Resolution|Extent|Language|[Interface]({{ site.baseurl }}/Tools/#interface)|[Status]({{ site.baseurl }}/Tools/#tool-status)|
|---|---|---|---|---|---|
|**Reach Scale Tools**||||||
|[Fluvial Coridor Toolbox](https://github.com/EVS-GIS/Fluvial-Corridor-Toolbox-ArcGIS)|Cell|Reach|Python|<img src="{{ site.baseurl }}/assets/images/tools/ArcPyToolbox.png"> , <img src="{{ site.baseurl }}/assets/images/tools/QGIS_bw_24.png">|Operational-Grade|
|[MoRPHED - Model of Riverine Physical Habitat & Ecogeomorphic Dynamics](http://morphed.joewheaton.org/)|Cell|Reach|C++|<i class="fa fa-desktop" aria-hidden="true"></i> |Research-Grade|
|[NREI - Net Rate of Energy Intake](https://github.com/Riverscapes/NREI)|Cell|Reach|R|<i class="fa fa-terminal" aria-hidden="true"></i>|Research-Grade|
|[TAT - Topographic Analyis Toolkit](https://tat.riverscapes.xyz)|Cell|Reach|Python|<img src="{{ site.baseurl }}/assets/images/tools/esri_icon.png">|Operational-Grade|
|[ToPCAT - Topographic Point Cloud Analysis Toolkit](http://tat.riverscapes.xyz/Help/Analysis/roughness-analysis-submenu/simple-topcat-roughness.html)|Cell|Reach|C++|<img src="{{ site.baseurl }}/assets/images/tools/esri_icon.png">|Research-Grade|
|**Network Scale Tools**||||||
|[CASCADE Toolbox](http://cascade.deib.polimi.it/)|Reach|Network|Matlab| <i class="fa fa-desktop" aria-hidden="true"></i> |Opperational-Grade|
|[Catchment Tool](https://riverscapes.github.io/CatchmentTool/)|Reach|Network|Python|<img src="{{ site.baseurl }}/assets/images/tools/ArcPyToolbox.png">|Research-Grade|
|[Conductivity Tools](https://riverscapes.github.io/Conductivity/)|Reach|Network|Python|<img src="{{ site.baseurl }}/assets/images/tools/ArcPyToolbox.png">|Research-Grade|
|[GNAT - Geomorphic Network Assessment Tool](http://gnat.riverscapes.xyz/)|Reach|Network|Python|<img src="{{ site.baseurl }}/assets/images/tools/ArcPyToolbox.png">|Research-Grade|
|[Grain Size Tool](https://github.com/Riverscapes/grain-size-tool)|Reach|Network|Python|<img src="{{ site.baseurl }}/assets/images/tools/ArcPyToolbox.png">|Research-Grade|
|[Network Profiler Tool](https://riverscapes.github.io/NetworkProfiler/)|Reach|Network|Python|<img src="{{ site.baseurl }}/assets/images/tools/QGIS_bw_24.png">|Research-Grade|
|[Solar Stream Tools](https://riverscapes.github.io/SolarStream/)|Reach|Network|Python|<img src="{{ site.baseurl }}/assets/images/tools/ArcPyToolbox.png">|Research-Grade|
|[Tributary Impact](http://tributaryimpact.riverscapes.xyz/)|Reach|Network|Python|<img src="{{ site.baseurl }}/assets/images/tools/ArcPyToolbox.png">|Proof of Concept|
|[WRAT - Wood Restoration Assessment Tool](https://github.com/Riverscapes/WRAT)|Reach|Network|Python|<img src="{{ site.baseurl }}/assets/images/tools/ArcPyToolbox.png">|Proof of Concept|
|**Catchment Scale Tools**||||||
|[Connectivity Index](https://github.com/HydrogeomorphologyTools/Connectivity-Index-ArcGIS-toolbox)|Cell|Catchment|Python|<img src="{{ site.baseurl }}/assets/images/tools/ArcPyToolbox.png">|Research-Grade|
|[SedInConnect](https://github.com/HydrogeomorphologyTools/SedInConnect_2.3)|Cell|Catchment|Python|<i class="fa fa-desktop" aria-hidden="true"></i> |Operational-Grade|
|**Utilities**||||||
|[PointCloud2Raster](https://github.com/NorthArrowResearch/pointcloud2raster)|Point|Reach|C++|<i class="fa fa-terminal" aria-hidden="true"></i>|Proof of Concept|
|[PySESA - Spatially Explicit Spectral Analysis](https://github.com/dbuscombe-usgs/pysesa)|Point|Reach|Python|<i class="fa fa-terminal" aria-hidden="true"></i>|Research-Grade|
|[RasterMan](https://github.com/NorthArrowResearch/rasterman)|Cell|Catchment|C++|<i class="fa fa-terminal" aria-hidden="true"></i>|Research-Grade|
|**Legacy CHaMP Tools**||||||
|[CTT - CHaMP Transformation Tool](http://ctt.riverscapes.xyz/index.html)|Cell|Reach|C#|<img src="{{ site.baseurl }}/assets/images/tools/esri_icon.png">|Operational-Grade|
|[CHaMP Topo Processing Tools](http://champtools.northarrowresearch.com/)|Reach|Reach|Python|<i class="fa fa-desktop" aria-hidden="true"></i> |Operational-Grade|
|[CHaMP Workbench](http://workbench.northarrowresearch.com/)|Any|Any|C#|<i class="fa fa-desktop" aria-hidden="true"></i> |Professional-Grade|
|[CHaMP Hydraylic-Modelling Delft3D Automation](https://github.com/SouthForkResearch/Hydraulic-Modeling/wiki)|cell|Reach|R/C|<i class="fa fa-terminal" aria-hidden="true"></i>|Research-Grade|




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
We classify the status of our tools according to their growth from innovative research ideas, through to operational tools in development that (with a little love and patience) can be run by someone other than the developer, on through to more broadly deployablle professional tools that are robust and usable by any user in very diffferent settings.

Our [RC Techncial Committee]({{ site.baseurl }}\About\) ranks a **tool's status** using the following criteria:



| Technology<br>Readiness Level | Tool Status | Vetted in <br>Peer-Reviewed <br>Literature | Source Code <br>Documentation | Open Source | User <br>Documentation | Easy User <br>Interface | Scalability |
|:-----------------------------:|------------------------|:------------------------------------------------------:|:--------------------------------------------------------:|:------------------------------------------------------------------------------------------------------------------------:|:--------------------------------------------------------:|:-------------------------------------------------------------------------------------------------------------------------:|:-------------------------------------------------------------------------------------------------------------------------:|
| TR1 -TR2 | **Concept** <img src="{{ site.baseurl }}/assets/images/tools/TRL_badges_pngs/TRL_orange/2_badges+status/32px/TRL_1_orange_32.png">| <i class="fa fa-battery-empty" aria-hidden="true"></i> | <i class="fa fa-battery-empty" aria-hidden="true"></i> | <i class="fa fa-battery-empty" aria-hidden="true"></i> | <i class="fa fa-battery-empty" aria-hidden="true"></i> | <i class="fa fa-battery-empty" aria-hidden="true"></i> | <i class="fa fa-battery-empty" aria-hidden="true"></i> |
| TR3 | **Proof of Concept** <img src="{{ site.baseurl }}/assets/images/tools/TRL_badges_pngs/TRL_orange/2_badges+status/32px/TRL_2_orange_32.png"> | <i class="fa fa-battery-full" aria-hidden="true"></i> | <i class="fa fa-battery-empty" aria-hidden="true"></i> | <i class="fa fa-battery-empty" aria-hidden="true"></i><br>to<br><i class="fa fa-battery-quarter" aria-hidden="true"></i> | <i class="fa fa-battery-empty" aria-hidden="true"></i> | <i class="fa fa-battery-empty" aria-hidden="true"></i> | <i class="fa fa-battery-empty" aria-hidden="true"></i> |
| TR4 | **Research-Grade** <img src="{{ site.baseurl }}/assets/images/tools/TRL_badges_pngs/TRL_orange/2_badges+status/32px/TRL_3_orange_32.png">| <i class="fa fa-battery-full" aria-hidden="true"></i> | <i class="fa fa-battery-quarter" aria-hidden="true"></i> | <i class="fa fa-battery-quarter" aria-hidden="true"></i> | <i class="fa fa-battery-quarter" aria-hidden="true"></i> | <i class="fa fa-battery-quarter" aria-hidden="true"></i> <br>to<br> <i class="fa fa-battery-half" aria-hidden="true"></i> | <i class="fa fa-battery-empty" aria-hidden="true"></i><br>to<br> <i class="fa fa-battery-quarter" aria-hidden="true"></i> |
| TR5-6 | **Operational-Grade** <img src="{{ site.baseurl }}/assets/images/tools/TRL_badges_pngs/TRL_orange/2_badges+status/32px/TRL_4_orange_32.png">| <i class="fa fa-battery-full" aria-hidden="true"></i> | <i class="fa fa-battery-full" aria-hidden="true"></i> | <i class="fa fa-battery-full" aria-hidden="true"></i> | <i class="fa fa-battery-half" aria-hidden="true"></i> | <i class="fa fa-battery-half" aria-hidden="true"></i> | <i class="fa fa-battery-quarter" aria-hidden="true"></i> |
| TR7-8 | **Professional-Grade** <img src="{{ site.baseurl }}/assets/images/tools/TRL_badges_pngs/TRL_orange/2_badges+status/32px/TRL_5_orange_32.png"> | <i class="fa fa-battery-full" aria-hidden="true"></i> | <i class="fa fa-battery-full" aria-hidden="true"></i> | <i class="fa fa-battery-full" aria-hidden="true"></i> | <i class="fa fa-battery-full" aria-hidden="true"> | <i class="fa fa-battery-full" aria-hidden="true"> | <i class="fa fa-battery-half" aria-hidden="true"></i> |
| TR8-9 | **Production-Grade** <img src="{{ site.baseurl }}/assets/images/tools/TRL_badges_pngs/TRL_orange/2_badges+status/32px/TRL_6_orange_32.png">| <i class="fa fa-battery-full" aria-hidden="true"></i> | <i class="fa fa-battery-full" aria-hidden="true"></i> | <i class="fa fa-battery-full" aria-hidden="true"></i> | <i class="fa fa-battery-full" aria-hidden="true"> | <i class="fa fa-battery-quarter" aria-hidden="true"></i> <br>to<br><i class="fa fa-battery-full" aria-hidden="true"> | <i class="fa fa-battery-full" aria-hidden="true"> |
| TR9 | **Commercial-Grade** <img src="{{ site.baseurl }}/assets/images/tools/TRL_badges_pngs/TRL_orange/2_badges+status/32px/TRL_7_orange_32.png">| <i class="fa fa-battery-full" aria-hidden="true"></i> | <i class="fa fa-battery-full" aria-hidden="true"></i> | <i class="fa fa-battery-full" aria-hidden="true"></i> | <i class="fa fa-battery-full" aria-hidden="true"> | <i class="fa fa-battery-full" aria-hidden="true"> | <i class="fa fa-battery-full" aria-hidden="true"> |

None or Not Applicable: <i class="fa fa-battery-empty" aria-hidden="true"></i> •
Minimal or In Progress: <i class="fa fa-battery-quarter" aria-hidden="true"></i> •
Functional: <i class="fa fa-battery-half" aria-hidden="true"></i> •
Fully Developed: <i class="fa fa-battery-full" aria-hidden="true"></i>  

**NOTE** - The RC does not track concepts or proof of concept tools in its listing. Only 

### Technological Readiness Levels
These ideas are based on the concept of [Technological Readiness Level](https://www.twi-global.com/technical-knowledge/faqs/technology-readiness-levels) (TRLs), as originally developed by NASA. The TRLs provide a way to discriminate between concepts and products that are in research phases, in development phases, or ready for deployment to broader audiences or makert. TRLs are  illustrated below (from [twi-global](https://www.twi-global.com/technical-knowledge)) and formally defined by the European Union:

<div align="center">
<a href=""><img src="{{ site.baseurl }}/assets/images/tools/TRL.png"></a></div>

------
# Why Bother? Why Go Beyond Research Grade?
If you've gotten to the bottom of this page, you presumably scrolled through or read a bunch of detail trying to encourage investment in making tools Riverscapes-Compliant and hopefully profossional, production or commercialized. The reason is simple. If we believe our science is good enough to inform management, inspire the public to conserve and restore riverscapes, then **we need to make the tools that represent that science scalable and accessible**. If our science is only relevant to other scientists, then we at least should meet a standard of practice of transparency and reproducability.

Put another way, when we invest in scalability, and adhre to a shared set of common goals, bigger things can happen. One such example is, ironically, how Bezos led Amazon to operate. The video below is a recap of a point Philip Bailey made recently:

<div class="responsive-embed">
<iframe width="560" height="315" src="https://www.youtube.com/embed/H_2AiyabDo8" frameborder="0" allow="accelerometer; autoplay; encrypted-media; gyroscope; picture-in-picture" allowfullscreen></iframe>
</div>