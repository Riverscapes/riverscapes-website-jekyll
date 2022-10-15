---
title: Riverscapes Projects
weight: 3
---
## The Problem
One of the most significant barriers to effective collaboration and leveraging of past work is being able to access and share any tool or model output or analysis, within the transparent context of the inputs and methods from which it was produced (Wilkinson et al. 2016).  "Just send me the data", is rarely actually that simple. Plus, one of the hallmarks of scientific rigor is *reproducibility*, and in our opinion, all scientific publications should provide the data they were produced with (. However, given the complexity of so many of the tools and workflows, this is an easy thing to say, but a very difficult thing to do properly. **The Riverscapes community desperately needs data standards and simple tools for sharing data** ([Fryirs et al. 2019](http://dx.doi.org/10.1002/wat2.1372)). In an era of "big data", it is easy to get overwhelmed without appropriate context. Unfortunately, context means metadata, and very few researchers and practitioners have the time or are likely to produce that metadata manually. However, failure to do so contributes to "dark knowledge" (censu [Jeschke et al. 2019](https://dx.doi.org/10.1139/facets-2019-0007)) through *inaccessible data and information*, and we *can* do better.

<div class="row small-up-2 medium-up-2">
  <div class="column">
    <div class="card">
      <div class="card-section">
        <h4>GOALS</h4>
        <img class="float-right" src="{{ site.baseurl }}/assets/images/data/RiverscapesProject_48.png">
        <ol>
        <li>Make it <b>easier to produce, curate and organize riverscapes analyses</b> in the context of the inputs and intermediates they were produced from. - i.e. make exploreable in <a href="https://rave.riverscapes.xyz">RAVE</a> </li> 
        <li> <i class="fa fa-share-alt" aria-hidden="true"></i> Foster transparency, reproducibility and sharing. </li>
         <li></li>
        </ol>
      </div>
    </div>
  </div>

</div>
To achieve the above goals, we propose packaging data as  **riverscapes projects** <img  src="{{ site.baseurl }}/assets/images/data/RiverscapesProject_24.png">.

A secondary goal of packaging analyses as  **riverscapes projects** <img  src="{{ site.baseurl }}/assets/images/data/RiverscapesProject_24.png"> is to facilitate the contribution of Riverscapes Data  to a [**DATA** Warehouses]({{ site.baseurl }}/Data_Warehouses) for sharing <i class="fa fa-share-alt" aria-hidden="true"></i> and achieve **F**-**A**-**I**-**R**.  With our [RAVE tools](https://rave.riverscapes.xyz) and [Warehouse](]({{ site.baseurl }}/Data_Warehouses) ) we strive to make it easy to contribute your data as a riverscapes project , which are  [**F**](https://force11.org/info/the-fair-data-principles/#elementor-toc__heading-anchor-2)indable,   [**A**](https://force11.org/info/the-fair-data-principles/#elementor-toc__heading-anchor-3)ccessible, and *ideally* [**I**](https://force11.org/info/the-fair-data-principles/#elementor-toc__heading-anchor-4)nteroperable and  [**R**](https://force11.org/info/the-fair-data-principles/#elementor-toc__heading-anchor-5)e-useable. There are many other platforms and warehouses where full or partial **F**-**A**-**I**-**R** can be achieved (e.g. [zeondo](https://zenodo.org/), [HydroShare](https://www.hydroshare.org/), [FigShare](https://figshare.com/) or [OpenAIRE](https://openaire.com/)). These systems will not necessarily have awareness of what a **riverscapes projects** <img  src="{{ site.baseurl }}/assets/images/data/RiverscapesProject_24.png"> is, but they can handle uploading the data as a zip file, and at least the F, A and R parts of FAIR. 

Note the **F**-**A**-**I**-**R**, correspond to the **f**indable, **a**ccessible, **i**nteroperable and **r**e-useable [Principles](https://force11.org/info/the-fair-data-principles/) (Wilkinson et al. [2016](https://www.nature.com/articles/sdata201618)), which the RC strives towards and helps facilitate the riverscapes community follow. 




## Riverscapes Projects 
We developed a data standard for packaging up riverscapes analyses (i.e. outputs of any [RC compliant tool]({{ site.baseurl }}/Tools) into **riverscapes projects** <img  src="{{ site.baseurl }}/assets/images/data/RiverscapesProject_24.png">. 

[Riverscapes-compliant tools]({{ site.baseurl }}/Tools) <img  src="{{ site.baseurl }}/assets/images/rc/RiverscapesCompliant_24.png"> automatically produce datasets that we call "projects". Each project is accompanied by metadata documentation in the form of an [XML project file]({{ site.baseurl }}/Tools/Technical_Reference/Documentation_Standards/Riverscapes_Projects/Project/projectxml.html). These project files have specific requirements and must comply with the [riverscapes project schema]({{ site.baseurl }}/Tools/Technical_Reference/Documentation_Standards/Riverscapes_Projects/Program/). In addition, the projects have a simple, standardized folder structure in which all data files are saved and or modified to disc (I/O). 

Riverscape projects can also be manually produced for any dataset and analysis to provide it context. For datasets that you want to share with a large audience, but may not produce that many times, it still may be worth the investment.

This five minute video explains the basics.

<div class="responsive-embed">
<iframe width="560" height="315" src="https://www.youtube.com/embed/YvWwaFFzulo" frameborder="0" allow="accelerometer; autoplay; encrypted-media; gyroscope; picture-in-picture" allowfullscreen></iframe>
</div>

### Glorified Housekeeping?
Yes, but who has time for it? Going to the effort of making your tool riverscapes-compliant turns the process of file management and metadata production and curation automatic for every analysis and write operation in your tools. 

![RAVE]({{ site.baseurl}}/assets/images/tools/rave.png)

## What are the Benefits of Riverscapes Projects?
Beyond better organization and transparency, the major benefits of riverscapes projects <img  src="{{ site.baseurl }}/assets/images/data/RiverscapesProject_24.png"> are:
- **Easy Visualization in GIS** - sharing and opening any project in the [RAVE](http://rave.riverscapes.net/) (Riverscapes Analysis Visualization Explorer) Tool - *A ArcGIS Add-In and QGIS Plugin for visualizing any project and adding to map any output, intermediate or input and exploring results.*
- **Easy Sharing & Discovery** - riverscapes projects can be stored in [Riverscapes Warehouses]({{ site.baseurl }}/Data_Warehouses) and made publicly available. - *Riverscapes projects in a warehouse can be discovered through websites,  webGIS maps, APIs, web mapping tile servies (e.g. WMS or WMST).*
- **Scalable Analysis & Interoperabiliy** - riverscapes projects can be accessed, modified and populated with cloud computing because querying, and batching operations are possible with a consistent data standard and storage. Plus, other riverscape-compliant projects can easily reference each other. 

## References
- Fryirs KA, Wheaton JM, Bizzi S, Williams R, Brierley GJ. 2019. To plug-in or not to plug-in? Geomorphic analysis of rivers using the River Styles Framework in an era of big data acquisition and automation. Wiley Interdisciplinary Reviews: Water 6 : e1372. DOI: [10.1002/wat2.1372](http://dx.doi.org/10.1002/wat2.1372)
- Jeschke JM, Lokatis S, Bartram I, Tockner K. 2019. Knowledge in the dark: scientific challenges and ways forward. FACETS.  DOI: [10.1139/facets-2019-0007](https://dx.doi.org/10.1139/facets-2019-0007)
- Wilkinson MD et al. 2016. The FAIR Guiding Principles for scientific data management and stewardship. Scientific Data 3 : 160018. DOI: [10.1038/sdata.2016.18](http://dx.doi.org/10.1038/sdata.2016.18)
