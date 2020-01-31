---
title: Riverscapes Projects
weight: 3
---
## The Problem
One of the most significant barriers to effective collaboration and leveraging of past work is being able to access and share any tool or model output or analysis, within the transparent context of the inputs and methods from which it was produced.  "Just send me the data", is rarely actually that simple. Plus, one of the halmarks of scientific rigor is *reproducability*, and in our opinion all scientific publications should provide the data they were produced with. However, given the complexity of so many of the tools and workflows, this is an easy thing to say, but a very difficult thing to do properly. **The Riverscapes community desperately needs data standards and simple tools for sharing data** ([Fryirs et al. 2019](http://dx.doi.org/10.1002/wat2.1372). In an era of "big data", it is easy to get overwhelmed without appropriate context. Unforunately, context means metadata, and very few researchers and practitioners have the time or are likely to produce that metadata manually.

## Riverscapes Projects 
We developed a data standard for packaging up riverscapes analyses (i.e. outputs of any [RC compliant tool]({{ site.baseurl }})/Tools) into **riverscapes projects**. 

[Riverscapes-compliant tools](({{ site.baseurl }})/Tools) automatically produce datasets that we call "projects". Each project is accompanied by metadata documentation in the form of an [XML project file](). These project files have specific requirements and must comply with the [riverscapes project schema](). In addition, the projects have a simple, standardized folder structure in which all data files are saved and or modified to disc (I/O). 

Riverscape projects can also be manually produced for any dataset and analysis to provide it context. For datasets that you want to share with a large audience, but may not produce that many times, it still may be worth the investment.

### Glorified Housekeeping?
Yes, but who has time for it? Going to the effort of making your tool riverscapes-compliant turns the process of file management and metadata production and curation automatic for every analysis and write operation in your tools. 

![RAVE]({{ site.baseurl}}/assets/images/tools/rave.png)

## What are the Benefits?
Beyond better organization and transparency, the major benefits of riverscapes projects are:
- **Easy Visualization in GIS** - sharing and opening any project in the [RAVE](http://rave.riverscapes.xyz/) (Riverscapes Analysis Visualization Explorer) Tool - *A ArcGIS Add-In and QGIS Plugin for visualizing any project and adding to map any output, intermediate or input and exploring results.*
- **Easy Sharing & Discovery** - riverscapes projects can be stored in [Riverscapes Warehouses]({{ site.baseurl }}/Data_Warehouses) and made publicly available. - *Riverscapes projects in a warehouse can be discovered through websites,  webGIS maps, APIs, web mapping tile servies (e.g. WMS or WMST).*
- **Scalable Analysis & Interoperabiliy** - riverscapes projects can be accessed, modified and populated with cloud computing because querying, and batching operations are possible with a consistent data standard and storage. Plus, other riverscape-compliant projects can easily reference each other. 

## References
- Fryirs KA, Wheaton JM, Bizzi S, Williams R, Brierley GJ. 2019. To plug-in or not to plug-in? Geomorphic analysis of rivers using the River Styles Framework in an era of big data acquisition and automation. Wiley Interdisciplinary Reviews: Water 6 : e1372. DOI: [10.1002/wat2.1372](http://dx.doi.org/10.1002/wat2.1372)