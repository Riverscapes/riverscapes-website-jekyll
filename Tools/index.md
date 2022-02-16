---
title: Tools
weight: 3
---

<img class="float-left" src="{{ site.baseurl }}/assets/images/rc/tool.png">The RC has been prolific in developing and vetting the [science]({{ site.baseurl }}/publications) and theoretical underpinnings essential to understanding and explaining how riverscapes work and are organized across a range of nested hierarchical spatial scales. We have also committed to building [open-source algorithms](https://github.com/Riverscapes) <i class="fa fa-github" aria-hidden="true"></i> tools to make it easier for researchers, professionals, practitioners and students to apply those concepts to their own riverscapes.

All of our tools are based on [peer-reviewed]({{ site.baseurl }}/Science/publications), methods. When we have developed the methods ourselves, we aim to have them vetted, published and disseminate in the [peer-reviewed literature]({{ site.baseurl }}/Science/publications). We then also make sure to have a well documented website (typically with a URL that will take the form of `tools.riverscapes.xyz/sometool`). For most users, the online help documentation and using the tool 'as is' is as far as they need to take it. However, for those so inclined, all of the underlying source-code for these tools, models and algorithms is available in its own GitHub <i class="fa fa-github" aria-hidden="true"></i> repository at [github.com/Riverscapes](https://github.com/Riverscapes).

<div align="center">

<a class="hollow button" href="https://tools.riverscapes.xyz/"> <img src="{{ site.baseurl }}/assets/images/tools/grade/TRL_6_32p.png"> Learn more about RC's<br> <b>Production-Grade Network-Scale Tools</b>  </a>
<a class="hollow button" href="https://github.com/Riverscapes"> <i class="fa fa-github" aria-hidden="true"></i> RC <b>Open Source</b><br> Tools on Github </a>
<a class="hollow button" href="{{ site.baseurl }}/Tools/toolStandards.html"> <img src="{{ site.baseurl }}/assets/images/rc/RiverscapesCompliant_32.png">  Learn more about RC-Compliant <br> <b>Tool Standards</b> <i class="fa fa-wrench" aria-hidden="true"></i></a>

</div>
-------

# Riverscapes Compliant
<img class="float-right" src="{{ site.baseurl }}/assets/images/rc/RiverscapesCompliant_128.png">
Tools are designated as "*riverscapes-compliant*"  when they meet the following criteria:
- [Tool Status]({{ site.baseurl }}/Tools/discrimination#tool-grade) of **Operational-Grade** or Higher
- Code produces [riverscapes projects]({{ site.baseurl }}/Tools/Technical_Reference/Documentation_Standards/Riverscapes_Projects/) <img  src="{{ site.baseurl }}/assets/images/data/RiverscapesProject_24.png"> as output of all analyses
- Project Type is registered with [`program.xml`]({{ site.baseurl }}/Tools/Technical_Reference/Documentation_Standards/Riverscapes_Projects/Program/) in [Program Repo](https://github.com/Riverscapes/RiverscapesXML)  
- Has been vetted by the RS Science Committee (i.e. has a "Report Card")


## Riverscapes Compliant Tools

|---|---|---|---|---|---|
| |Resolution|Extent|Language|[Interface]({{ site.baseurl }}/Tools/discrimination#interface)|[Status]({{ site.baseurl }}/Tools/discrimination#tool-grade)|
|---|---|---|---|---|---|
|**Exploratory Tools for Visualizing Riverscapes Projects**||||||
|[WebRAVE](http://rave.riverscapes.xyz/)|Any|Any|react, javascript|<i class="fa fa-chrome" aria-hidden="true"></i>|Commercial Grade <img src="{{ site.baseurl }}/assets/images/tools/grade/TRL_7_32p.png">|
|[QRAVE](http://rave.riverscapes.xyz/)|Any|Any|Python|<img src="{{ site.baseurl }}/assets/images/tools/QGIS_bw_24.png">|Professional-Grade <img src="{{ site.baseurl }}/assets/images/tools/grade/TRL_4_32p.png"> |
|[ArcRAVE](http://rave.riverscapes.xyz/)|Any|Any|C#|<img src="{{ site.baseurl }}/assets/images/tools/esri_icon.png">|Professional-Grade <img src="{{ site.baseurl }}/assets/images/tools/grade/TRL_4_32p.png"> |
|**Reach Scale Tools**||||||
|[GCD - Geomorphic Change Detection](http://gcd.riverscapes.xyz/)|Cell|Reach|C#|<i class="fa fa-desktop" aria-hidden="true"></i> , <img src="{{ site.baseurl }}/assets/images/tools/esri_icon.png">, <i class="fa fa-terminal" aria-hidden="true"></i>| Professional-Grade: <i class="fa fa-desktop" aria-hidden="true"></i> & <img src="{{ site.baseurl }}/assets/images/tools/esri_icon.png">; Production-Grade: <i class="fa fa-terminal" aria-hidden="true">|
|[GUT - Geomorphic Unit Toolkit](http://gut.riverscapes.xyz/)|Cell|Reach|Python|<i class="fa fa-terminal" aria-hidden="true"></i>, <img src="{{ site.baseurl }}/assets/images/tools/ArcPyToolbox.png">|Research-Grade|
|[FHM - Fish Habitat Model](http://habitat.northarrowresearch.com/)|Cell|Reach|C#/C++|<i class="fa fa-desktop" aria-hidden="true"></i> |Operational-Grade|
|**Network Scale Tools**||||||
|[Riverscapes Context](http://tools.riverscapes.xyz/rscontext) - RS_Context 1.2.2 |Reach|Network|Python|<i class="fa fa-terminal" aria-hidden="true"></i>  |[Production-Grade](https://tools.riverscapes.xyz/Status/ReportCard_1.2.2.html) <img src="{{ site.baseurl }}/assets/images/tools/grade/TRL_6_32p.png">|
|[Channel Area Tool](http://tools.riverscapes.xyz/channel)  1.1.1 |Reach|Network|Python|<i class="fa fa-terminal" aria-hidden="true"></i>  |[Production-Grade](https://tools.riverscapes.xyz/Status/ReportCard_1.1.1.html) <img src="{{ site.baseurl }}/assets/images/tools/grade/TRL_6_32p.png">|
|[TauDEM - Terrain Analysis Using Digital Elevation Models](http://tools.riverscapes.xyz/taudem) - TauDEM 1.0.2 |Reach|Network|Python|<i class="fa fa-terminal" aria-hidden="true"></i>  |[Production-Grade](https://tools.riverscapes.xyz/Status/ReportCard_1.0.2.html) <img src="{{ site.baseurl }}/assets/images/tools/grade/TRL_6_32p.png">|
|[VBET - Valley Bottom Extraction Tool](http://tools.riverscapes.xyz/vbet) - VBET 0.5.1 Beta|Reach|Network|Python|<i class="fa fa-terminal" aria-hidden="true"></i>  |[Production-Grade](https://tools.riverscapes.xyz/vbet/Status/ReportCard_0.5.1.html) <img src="{{ site.baseurl }}/assets/images/tools/grade/TRL_6_32p.png">|
|[BRAT - Beaver Restoration Assessment Tool](http://tools.riverscapes.xyz/brat) - sqlBRAT 4.3.2|Reach|Network|Python|<i class="fa fa-terminal" aria-hidden="true"></i> |[Production-Grade](https://tools.riverscapes.xyz/brat/Status/ReportCard_4.3.2.html) <img src="{{ site.baseurl }}/assets/images/tools/grade/TRL_6_32p.png">|
|[pyBRAT - Beaver Restoration Assessment Tool](http://brat.riverscapes.xyz/) - pyBRAT 3.1.0|Reach|Network|Python|<img src="{{ site.baseurl }}/assets/images/tools/ArcPyToolbox.png">|[Operational-Grade](http://brat.riverscapes.xyz/Documentation/Status/Tool_ReportCard_3-1-00) <img src="{{ site.baseurl }}/assets/images/tools/grade/TRL_4_32p.png">|
|[RCAT - Riparian Condition Assessment Tool](http://rcat.riverscapes.xyz/)|Reach|Network|Python|<img src="{{ site.baseurl }}/assets/images/tools/ArcPyToolbox.png">|Research-Grade|
|[GNAT - Geomorphic Network Assessment Tool](http://gnat.riverscapes.xyz/)|Reach|Network|Python|<img src="{{ site.baseurl }}/assets/images/tools/ArcPyToolbox.png">|Research-Grade|
|**Legacy CHaMP Tools**||||||
|[CHaMP Topo Processing Tools](http://champtools.northarrowresearch.com/)|Reach|Reach|Python|<img src="{{ site.baseurl }}/assets/images/tools/esri_icon.png">|Production-Grade|
|[CHaMP Topo Metrics](https://github.com/SouthForkResearch/CHaMP_Metrics/wiki)|Reach|Network|Python|<img src="{{ site.baseurl }}/assets/images/tools/ArcPyToolbox.png">|Production-Grade|



-----
## Tools Pending Riverscapes Compliance

<img class="float-right" src="{{ site.baseurl }}/assets/images/rc/RiverscapesCompliantPending_128.png">
Tools are designated as "*pending riverscapes-compliance*" <img  src="{{ site.baseurl }}/assets/images/rc/RiverscapesCompliantPending_28.png"> when the RS Science Committee has accepted the tool for consideration and they meet the following criteria:
- [Tool Status]({{ site.baseurl }}/Tools/discrimination#tool-grade) of **Resarch-Grade** or higher
- Developer has indicated intent to modify code to produce [riverscapes projects]({{ site.baseurl }}/Tools/Technical_Reference/Documentation_Standards/Riverscapes_Projects/) as output of all analyses - Moving up to **Operational-Grade**
- Developer has indicated intent to add Project Type registration with [`program.xml`]({{ site.baseurl }}/Tools/Technical_Reference/Documentation_Standards/Riverscapes_Projects/Program/) in [Program Repo](https://github.com/Riverscapes/RiverscapesXML)


|---|---|---|---|---|---|
| |Resolution|Extent|Language|[Interface]({{ site.baseurl }}/Tools/discrimination#interface)|[Status]({{ site.baseurl }}/Tools/discrimination#tool-grade)|
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
|[SedInConnect](https://github.com/HydrogeomorphologyTools/SedInConnect_2.3)|Cell|Catchment|Python|<i class="fa fa-desktop" aria-hidden="true"></i> |Operational-Grade |
|**Utilities**||||||
|[PointCloud2Raster](https://github.com/NorthArrowResearch/pointcloud2raster)|Point|Reach|C++|<i class="fa fa-terminal" aria-hidden="true"></i>|Proof of Concept|
|[PySESA - Spatially Explicit Spectral Analysis](https://github.com/dbuscombe-usgs/pysesa)|Point|Reach|Python|<i class="fa fa-terminal" aria-hidden="true"></i>|Research-Grade|
|[RasterMan](https://github.com/NorthArrowResearch/rasterman)|Cell|Catchment|C++|<i class="fa fa-terminal" aria-hidden="true"></i>|Research-Grade|
|**Legacy CHaMP Tools**||||||
|[CTT - CHaMP Transformation Tool](http://ctt.riverscapes.xyz/index.html)|Cell|Reach|C#|<img src="{{ site.baseurl }}/assets/images/tools/esri_icon.png">|Operational-Grade|
|[CHaMP Topo Processing Tools](http://champtools.northarrowresearch.com/)|Reach|Reach|Python|<i class="fa fa-desktop" aria-hidden="true"></i> |Operational-Grade|
|[CHaMP Workbench](http://workbench.northarrowresearch.com/)|Any|Any|C#|<i class="fa fa-desktop" aria-hidden="true"></i> |Professional-Grade|
|[CHaMP Hydraylic-Modelling Delft3D Automation](https://github.com/SouthForkResearch/Hydraulic-Modeling/wiki)|cell|Reach|R/C|<i class="fa fa-terminal" aria-hidden="true"></i>|Research-Grade|




####  [Model Discrimination]({{ site.baseurl }}/Tools/discrimination)
We discriminate our tools based on their [interface]({{ site.baseurl }}/Tools/discrimination#interface) and [tool grade]({{ site.baseurl }}/tools/discrimination#tool-grade).

<div align="center">

<a class="hollow button" href="{{ site.baseurl }}/discrimination#tool-grade"> <img src="{{ site.baseurl }}/assets/images/tools/grade/TRL_1_32p.png">  Learn more about RC-Compliant <br> <b>Tool Discrimination</b>  <img src="{{ site.baseurl }}/assets/images/tools/grade/TRL_7_32p.png"> </a>

</div>


##### Tool Grade
We classify the  [grade]({{ site.baseurl }}/Tools/discrimination#tool-grade) of our tools according to their growth from innovative research ideas, through to operational tools in development that (with a little love and patience) can be run by someone other than the developer, on through to more broadly deployable professional tools that are robust and usable by any user in very different settings.
