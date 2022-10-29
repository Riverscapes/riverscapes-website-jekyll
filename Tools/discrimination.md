---
title: Tool Discrimination
weight: 4
---

# Tool Discrimination
Discriminating tools helps potential users of the tool or users of its outputs make informed decision about whether the tool and/or its ouputs are fit for _their_ purposes. The following are helpful concepts  the RC uses for discriminating model types:

Interface
Tool-Grade (using adaptation of NASA's Technological Readiness Levels)
Report Cards

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

## Tool Grade
We classify the grade of our tools according to their growth from innovative research ideas, through to operational tools in development that (with a little love and patience) can be run by someone other than the developer, on through to more broadly deployablle professional tools that are robust and usable by any user in very diffferent settings.

Our [RC Techncial Committee]({{ site.baseurl }}\About\) ranks a **tool's grade** using the following criteria:



| Technology<br>Readiness Level | Tool Status |Badge | Vetted in <br>Peer-Reviewed <br>Literature | Source Code <br>Documentation | Open Source | User <br>Documentation | Easy User <br>Interface | Scalability |
|:-----------------------------:|------------------------|:------------------------------------------------------:|:--------------------------------------------------------:|:------------------------------------------------------------------------------------------------------------------------:|:--------------------------------------------------------:|:-------------------------------------------------------------------------------------------------------------------------:|:-------------------------------------------------------------------------------------------------------------------------:|
| TR1 -TR2 |**Concept**|<img src="{{ site.baseurl }}/assets/images/tools/grade/TRL_1_32p.png"> | <i class="fa fa-battery-empty" aria-hidden="true"></i> | <i class="fa fa-battery-empty" aria-hidden="true"></i> | <i class="fa fa-battery-empty" aria-hidden="true"></i> | <i class="fa fa-battery-empty" aria-hidden="true"></i> | <i class="fa fa-battery-empty" aria-hidden="true"></i> | <i class="fa fa-battery-empty" aria-hidden="true"></i> |
| TR3 |**Proof of Concept**| <img src="{{ site.baseurl }}/assets/images/tools/grade/TRL_2_32p.png">  | <i class="fa fa-battery-full" aria-hidden="true"></i> | <i class="fa fa-battery-empty" aria-hidden="true"></i> | <i class="fa fa-battery-empty" aria-hidden="true"></i><br>to<br><i class="fa fa-battery-quarter" aria-hidden="true"></i> | <i class="fa fa-battery-empty" aria-hidden="true"></i> | <i class="fa fa-battery-empty" aria-hidden="true"></i> | <i class="fa fa-battery-empty" aria-hidden="true"></i> |
| TR4 |**Research Grade**|<img src="{{ site.baseurl }}/assets/images/tools/grade/TRL_3_32p.png">  | <i class="fa fa-battery-full" aria-hidden="true"></i> | <i class="fa fa-battery-quarter" aria-hidden="true"></i> | <i class="fa fa-battery-quarter" aria-hidden="true"></i> | <i class="fa fa-battery-quarter" aria-hidden="true"></i> | <i class="fa fa-battery-quarter" aria-hidden="true"></i> <br>to<br> <i class="fa fa-battery-half" aria-hidden="true"></i> | <i class="fa fa-battery-empty" aria-hidden="true"></i><br>to<br> <i class="fa fa-battery-quarter" aria-hidden="true"></i> |
| TR5-6 | **Operational Grade**|<img src="{{ site.baseurl }}/assets/images/tools/grade/TRL_4_32p.png">| <i class="fa fa-battery-full" aria-hidden="true"></i> | <i class="fa fa-battery-full" aria-hidden="true"></i> | <i class="fa fa-battery-full" aria-hidden="true"></i> | <i class="fa fa-battery-half" aria-hidden="true"></i> | <i class="fa fa-battery-half" aria-hidden="true"></i> | <i class="fa fa-battery-quarter" aria-hidden="true"></i> |
| TR7-8 |**Professional Grade**| <img src="{{ site.baseurl }}/assets/images/tools/grade/TRL_5_32p.png"> | <i class="fa fa-battery-full" aria-hidden="true"></i> | <i class="fa fa-battery-full" aria-hidden="true"></i> | <i class="fa fa-battery-full" aria-hidden="true"></i> | <i class="fa fa-battery-full" aria-hidden="true"> | <i class="fa fa-battery-full" aria-hidden="true"> | <i class="fa fa-battery-half" aria-hidden="true"></i> |
| TR8-9 |**Production Grade**|<img src="{{ site.baseurl }}/assets/images/tools/grade/TRL_6_32p.png">   | <i class="fa fa-battery-full" aria-hidden="true"></i> | <i class="fa fa-battery-full" aria-hidden="true"></i> | <i class="fa fa-battery-full" aria-hidden="true"></i> | <i class="fa fa-battery-full" aria-hidden="true"> | <i class="fa fa-battery-quarter" aria-hidden="true"></i> <br>to<br><i class="fa fa-battery-full" aria-hidden="true"> | <i class="fa fa-battery-full" aria-hidden="true"> |
| TR9 | **Commercial Grade**|<img src="{{ site.baseurl }}/assets/images/tools/grade/TRL_2_32p.png">  | <i class="fa fa-battery-full" aria-hidden="true"></i> | <i class="fa fa-battery-full" aria-hidden="true"></i> | <i class="fa fa-battery-full" aria-hidden="true"></i> | <i class="fa fa-battery-full" aria-hidden="true"> | <i class="fa fa-battery-full" aria-hidden="true"> | <i class="fa fa-battery-full" aria-hidden="true"> |

None or Not Applicable: <i class="fa fa-battery-empty" aria-hidden="true"></i> •
Minimal or In Progress: <i class="fa fa-battery-quarter" aria-hidden="true"></i> •
Functional: <i class="fa fa-battery-half" aria-hidden="true"></i> •
Fully Developed: <i class="fa fa-battery-full" aria-hidden="true"></i>  

**NOTE** - The RC does not track concepts or proof of concept tools in its listing. 

### 

### Technological Readiness Levels
These tool-grade ideas are based on the concept of [Technological Readiness Level](https://www.twi-global.com/technical-knowledge/faqs/technology-readiness-levels) (TRLs), as originally developed by NASA. The TRLs provide a way to discriminate between concepts and products that are in research phases, in development phases, or ready for deployment to broader audiences or makert. TRLs are  illustrated below (from [twi-global](https://www.twi-global.com/technical-knowledge)) and formally defined by the European Union:

<div align="center">
<a href=""><img src="{{ site.baseurl }}/assets/images/tools/TRL.png"></a></div>




------
# Why Bother? Why Go Beyond Research-Grade?
If you've gotten to the bottom of this page, you presumably scrolled through or read a bunch of detail trying to encourage investment in making tools Riverscapes-Compliant and hopefully profossional, production or commercialized. The reason is simple. If we believe our science is good enough to inform management, inspire the public to conserve and restore riverscapes, then **we need to make the tools that represent that science scalable and accessible**. If our science is only relevant to other scientists, then we at least should meet a standard of practice of transparency and reproducability.

Put another way, when we invest in scalability, and adhre to a shared set of common goals, bigger things can happen. One such example is, ironically, how Bezos led Amazon to operate. The video below is a recap of a point Philip Bailey made recently:

<div class="responsive-embed">
<iframe width="560" height="315" src="https://www.youtube.com/embed/H_2AiyabDo8" frameborder="0" allow="accelerometer; autoplay; encrypted-media; gyroscope; picture-in-picture" allowfullscreen></iframe>
</div>