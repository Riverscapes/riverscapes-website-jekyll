---
title: Data Warehouses
---

The Riverscapes Consoritum organizes and serves data via  *data warehouses* <img src="{{ site.baseurl }}/assets/images/data/RiverscapesWarehouseCloud_24.png">. These data warehouses provide access to both the underlying data (packaged in [riverscapes projects]({{ site.baseurl }}/Tools/Technical_Reference/Documentation_Standards/Riverscapes_Projects/)) as well as serving these data as interactive web maps. We only serve and host data packaged in fully  [Riverscapes-Compliant]({{ site.baseurl }}/Tools) <img  src="{{ site.baseurl }}/assets/images/rc/RiverscapesCompliant_24.png">  [Riverscapes Projects]({{ site.baseurl }}/Tools/Technical_Reference/Documentation_Standards/Riverscapes_Projects/) <img  src="{{ site.baseurl }}/assets/images/data/RiverscapesProject_24.png">.

<div class="row small-up-2 medium-up-2">
  <div class="column">
    <div class="card">
      <div class="card-section">
        <h4>GOAL</h4>
        <img class="float-left" src="{{ site.baseurl }}/assets/images/data/RiverscapesWarehouseCloud_128.png">
        <p>Make it easier to catalog, share, discover and retrieve the products of riverscapes analysis and modelling. </p>
      </div>
    </div>
  </div>

</div>
## Advantages

<img class="float-right" src="{{ site.baseurl }}/assets/images/data/Riverscapes Warehouse Loggin.png">The advantages of  [riverscapes projects]({{ site.baseurl }}/Tools/Technical_Reference/Documentation_Standards/Riverscapes_Projects/)  being hosted in a data warehouse can include:
- Searable and querable Warehouse Explorer Catalog <i class="fa fa-filter" aria-hidden="true"></i>
- Secure cloud hosting  (typically in <a href="https://aws.amazon.com"><img  src="{{ site.baseurl }}/assets/images/data/AWS_24.png"></a> [S3](https://aws.amazon.com/s3/faqs/)) <i class="fa fa-cloud" aria-hidden="true"></i> with:
  - Easy public sharing <i class="fa fa-share-alt" aria-hidden="true"></i>
  - Full user <i class="fa fa-user-circle-o" aria-hidden="true"></i> access permission control <i class="fa fa-key" aria-hidden="true"></i>
- Full <a href="https://aws.amazon.com"><img  src="{{ site.baseurl }}/assets/images/data/AWS_24.png"></a>  integration with [EC2](https://aws.amazon.com/ec2/?nc2=type_a) and [Lambda](https://aws.amazon.com/lambda/?nc2=type_a) for cloud-computing of [Production-Grade](https://riverscapes.github.io/riverscapes-website/Tools/#tool-status) Riverscapes Models.
-  [Creative Commons licensing](https://creativecommons.org/licenses/) of datasets <i class="fa fa-creative-commons" aria-hidden="true"></i>
- Ability to mint [DOIs](https://www.doi.org/faq.html) <a href="https://www.doi.org/faq.html"><img  src="{{ site.baseurl }}/assets/images/data/DOI_24.png"></a> to make datasets citeable
- [OGC API](http://www.ogcapi.org/) access to riverscapes projects and warehouse for programmers <img  src="{{ site.baseurl }}/assets/images/data/api_24.png"> 
-  [OGC Web Map Tile Services](https://www.opengeospatial.org/standards/wmts) access to your datasets <i class="fa fa-map-o" aria-hidden="true"></i>
- Searchable and discoverable in [RAVE](http://rave.riverscapes.xyz) GIS Toolbars


**NOTE** - As of January 2020, we have not made any of the *data warehouses* fully public facing as they are still in Beta Testing. 

-----
# Riverscape Warehouse Concepts
##  Warehouse Explorer Concept
<a href="https://northarrowresearchlabs.github.io/riverscapes/#/"><img src="{{ site.baseurl }}/assets/images/data/RC_WarehouseExplorer.png"></a>

Part of the advantage of serving and hosting data in a Riverscapes Warehouse  <img src="{{ site.baseurl }}/assets/images/data/RiverscapesWarehouseCloud_24.png"> is the ability to catalog and index the data so it easily searchable,  queried and discoverable. 
<div align="center">
<img src="{{ site.baseurl }}/assets/images/data/WarehouseCHAMP.png">
<br><em>Eample view of a fully searchable and querable data warehouse. </em>
</div>

### CHaMP Example
When the [Columbia Habitat Monitoring Program](http://champmonitoring.org) (CHaMP) was operational, the program produced an immense amount of raw monitoring data, derivative products, model analysis products, and various outputs. For example, from 2011 to 2017, over 958 sites were monitored for fish habitat producing (ISEMP/CHAMP, 2018)., CHaMP crews conducted over 5000 visits to over 950 sites producing a mountain of monitoring data. All of the visit and topographic data was made available in [cm.org](http://champmonitoring.org). However, the program produced a much richer range of reach scale, network scale and population scale analysis and synthesis products, which cm.org was not designed to accomodate. To test the utility of the Riverscapes Warehouse context, we created a warehouse explorer for the [CHaMP Riverscapes Warehouse](https://northarrowresearchlabs.github.io/riverscapes/#/CHaMP). Some of its utlity is illustrated in the video below.

<div class="responsive-embed">
<iframe width="560" height="315" src="https://www.youtube.com/embed/llGthTDUjfo" frameborder="0" allow="accelerometer; autoplay; encrypted-media; gyroscope; picture-in-picture" allowfullscreen></iframe>
<br><em>Video explaining data warehouse concepts and illustrating some of its utility. </em>
</div>
- ISEMP/CHAMP. (2018) [Integrated Status and Effectiveness Monitoring Program (BPA Project 2003-017-00) and Columbia Habitat Monitoring Program (BPA Project 2011-006-00) . Final Technical Report for Bonneville Power Administration](https://www.researchgate.net/publication/329514287_Integrated_Status_and_Effectiveness_Monitoring_Program_BPA_Project_2003-017-00_and_Columbia_Habitat_Monitoring_Program_BPA_Project_2011-006-00_Final_Technical_Report_for_Bonneville_Power_Administration). 1280 pages.


-----
## Web-Map and PWA Enabled
<img class="float-right" src="{{ site.baseurl }}/assets/images/data/BRAT_Risk.png">
One of the real values in hosting your [Riverscapes Projects]({{ site.baseurl }}/Tools/Technical_Reference/Documentation_Standards/Riverscapes_Projects/) <img  src="{{ site.baseurl }}/assets/images/data/RiverscapesProject_24.png"> in a Riverscapes Warehouse  <img src="{{ site.baseurl }}/assets/images/data/RiverscapesWarehouseCloud_24.png">, is that web-maps can be produced that allow non-GIS users and non-modelers to interact with  riverscape project outputs and explore them.


 and progressive web-apps

### Example of BRAT
<img class="float-left" src="{{ site.baseurl }}/assets/images/data/BratMapTab.png">

[BRAT](https://riverscapes.github.io/BratMap/#/idaho)

<div align="center">
<img src="{{ site.baseurl }}/assets/images/data/IdahoBRATMap.png">
</div>



-----
## Product Status
We refer to ‘products’ as specific geospatial products or outputs within the family of products produced by our various analyses, tools and workflows within the CHaMP/ISEMP realm.
![FamilyOfProducts.png](https://lh5.googleusercontent.com/MrlolkkwfO0OC1pZNKDKkCcoebKTYbGKbVpO5H2vpd7ItVFi-6lVvmUNY9o4TMK1UxQizAGkZwaoBuLntsZvO8mfE4gsh9ohNmfxxhZBG0owahyAr_Tv_eUdt31REXy-MPKEeSMR)

We produce a plethora of products, some of which go no further than an exploratory analysis and some which are carefully documented, vetted, and validated before being made for external consumption. Not all products will proceed sequentially through all stages of product status below and some stages are reiterated (e.g. after expert calibration, an output may be requeued for QA/QC assurance. 

## Data Product Status

We have three status tags: 
1) Overall Status, 
2)  QA/QC Review, and 
3_Data Generation 

to track the development of a product. However, it is the Overall Status of a product that is most important for tracking its progression within the ISEMP/CHaMP Warehouse.

| Status Tags | Overall Status | QA/QC Review | Data Generation |
|-------------|----------------|-------------------|-----------------|
|  |  | None | None |
|  | Exploratory | Automated Testing | End-User |
|  | Provisional | Manual Testing | Manual |
|  | Final | Expert Calibrated | Automated-Local |
|  | Extenral | Validated | Automated-Cloud |

- **Overall Status** - Where in the life cycle of a product the product exists. The four status choices represent a progression.
  - **Exploratory** - Preliminary products produced by an analyst to explore how well a particular analysis works, or to what extent a product gives insights into specific questions (e.g., an individual model run used for a talk). 
  - **Provisional** - A product that has undergone some degree of automated or manual QA/QC testing. 
  - **Final** - A product that has been validated and is trusted for inclusion in the ISEMP/CHaMP warehouse. Upon elevation to a finalized status a product is available for use by ISEMP/CHaMP team members and authorized partners. At this point the product has a DOI assigned so a static version is available for later reference.
  - **External** - A product promoted from a finalized warehouse output to ready for external consumption. The degree of documentation and vetting is generally higher than finalized outputs. Examples may include any products used in the preparation of a basin or restoration plan or peer-reviewed paper. For the Bi-Op, these will be the capacity estimates we hand off to other life-cycle modeling groups. 
- **QA/QC Review** - The degree of quality assurance and quality control checks that a product has been subjected to. The choices are not a progression per se, and a product may undergo just one or all four of these states. 
  - **Automated Testing -** All tool-generated outputs undergo some degree of quality assurance and quality control checking to flag outliers and mistakes. When a product has received QA/QC evaluation in an automated, centralized, production mode (e.g., GCD results checked for outliers) it is automatically queued for manual editing, checking and fixing.
  - **Manual Testing** - A manual, expert evaluation of a product and its reporting. 
  - **Expert Calibrated** - An optional step of modifying model outputs by model iteration or analysis to produce new output based on expert modification of inputs and/or parameters to more realistic values. 
  - **Validated**- A product can be considered validated after it has undergone some form of testing and the relative quality of that product has been assessed and reported. If the inputs and/or parameters have been calibrated or modified with expert insights and the product generation has been iterative, the reporting includes how product quality has changed with that calibration process. 
- **Data Generation** - How the data products were generated
  - .**Automated Local**- Generated via batch processing using local tools and workbench.
  - **Automated Cloud -** Generated via cloud processing engines (e.g., EC2 or Lambda AWS)
  -  **Manual** - Generated via local tools on an individual basis.