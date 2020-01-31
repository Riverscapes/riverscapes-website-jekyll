---
title: Tools
---

Our consortium has been prolific in developing and vetting the [science]({{ site.baseurl }}/publications) and theoretical underpinnings essential to understanding and explaining how riverscapes work and are organized across a range of nested hierarchical spatial scales. We have also committed to building [open-source algorithms](https://github.com/Riverscapes) <i class="fa fa-github" aria-hidden="true"></i> tools to make it easier for researchers, professionals, practitioners and students to apply those concepts to their own riverscapes. 

All of our tools are based on [peer-reviewed](({{ site.baseurl }}/publications) ), methods. When we have developed the methods ourselves, we aim to have them vetted, published and disseminate in the [peer-reviewed literature](({{ site.baseurl }}/publications) ). We then also make sure to have a well documented website (you'll find them from RC-Tools menu above and the URL will take the form of sometool.riverscapes.xyz). For most users, the online help documentation and using the tool]({{ site.baseurl }}/Tools)  'as is' is as far as they need to take it. However, for those so inclined, all of the underlying source-code for these tools, models and algorithms is available in its own GitHub repository at [github.com/Riverscapes](https://github.com/Riverscapes).

|---|---|---|---|---|---|
| |Resolution|Extent|Language|Interface|Status|
|---|---|---|---|---|---|
|**Reach Scale Tools**||||||
|[GCD](http://gcd.riverscapes.xyz/)|Cell|Reach|C#|GUI|Production|
|[GUT](http://gut.riverscapes.xyz/)|Cell|Reach|Python|CLI|Operational|
|[MoRPHED](http://morphed.joewheaton.org/)|Cell|Reach|C++|GUI|Research|
|[FHM - Fish Habitat Model](http://habitat.northarrowresearch.com/)|Cell|Reach|C#/C++|GUI|Operational|
|[NREI - Net Rate of Energy Intake](https://github.com/Riverscapes/NREI)|Cell|Reach|R|CLI|Research|
|**Network Scale Tools**||||||
|[BRAT](http://brat.riverscapes.xyz/)|Reach|Network|Python|Toolbox|Operational|
|[RCAT](http://rcat.riverscapes.xyz/)|Reach|Network|Python|Toolbox|Operational|
|[GNAT](http://gnat.riverscapes.xyz/)|Reach|Network|Python|Toolbox|Operational|
|[Catchment Tool](https://riverscapes.github.io/CatchmentTool/)|Reach|Network|Python|Toolbox|Operational|
|**Utilities**||||||
|[RAVE Toolbar](http://rave.riverscapes.xyz)|||C#|ArcGIS AddIn|Production|
|**Legacy CHaMP Tools**||||||
|[CTT - CHaMP Transformation Tool](http://ctt.riverscapes.xyz/index.html)|Reach|Reach|C#|GUI|Production|
|[CHaMP Topo Processing Tools](http://champtools.northarrowresearch.com/)|Reach|Reach|Python|GUI|Production|
|[CHaMP Topo Metrics](https://github.com/SouthForkResearch/CHaMP_Metrics/wiki)|Reach|Network|Python|Toolbox|Operational|
|[CHaMP Hydraylic-Modelling Delft3D Automation](https://github.com/SouthForkResearch/Hydraulic-Modeling/wiki)|cell|Reach|R/C|CLI|Operational|

* **Interface**
    * CLI = [command line interface](https://en.wikipedia.org/wiki/Command-line_interface)
    * GUI = [graphical user interface](https://en.wikipedia.org/wiki/Graphical_user_interface)
    * Web = interactive web site
    * API = [application programming interface](https://en.wikipedia.org/wiki/Application_programming_interface)
    * PWA = [progressive web app](https://en.wikipedia.org/wiki/Progressive_web_application)
* **Tool Status** - We classify the status of our tools according to their growth from innovative research ideas, through operational tools that (with a little love) can be run more broadly to production tools that are robust and usable by anyone.