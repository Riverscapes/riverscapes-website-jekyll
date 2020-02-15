---
title: Data Warehouses
---

Riverscapes organizes and serves data via *data warehouses*. These data warehouses provide access to both the underlying data (packaged in riverscapes projects) as well as serving these data as interactive web maps.

As of January 2020, we have not made any of the *data warehouses* fully public facing as they are in Beta Testing. 

# CHaMP

Much of the 
[CHaMP Warehouse](https://northarrowresearchlabs.github.io/riverscapes/#/CHaMP)

# Beaver Restoration Assessment Tool (BRAT)

[BRAT](https://northarrowresearchlabs.github.io/riverscapes/#/BRAT_OREGON)





Product StatusWe refer to ‘products’ as specific geospatial products or outputs within the family of products produced by our various analyses, tools and workflows within the CHaMP/ISEMP realm.
![FamilyOfProducts.png](https://lh5.googleusercontent.com/MrlolkkwfO0OC1pZNKDKkCcoebKTYbGKbVpO5H2vpd7ItVFi-6lVvmUNY9o4TMK1UxQizAGkZwaoBuLntsZvO8mfE4gsh9ohNmfxxhZBG0owahyAr_Tv_eUdt31REXy-MPKEeSMR)

We produce a plethora of products, some of which go no further than an exploratory analysis and some which are carefully documented, vetted, and validated before being made for external consumption. Not all products will proceed sequentially through all stages of product status below and some stages are reiterated (e.g. after expert calibration, an output may be requeued for QA/QC assurance. 


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