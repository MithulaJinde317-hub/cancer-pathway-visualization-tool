# Cancer Pathway Visualization Tool
Author:Mithula J

## Overview

The Cancer Pathway Visualization Tool is a bioinformatics-based computational biology project designed to analyze and visualize cancer-related molecular pathways using KEGG pathway data.

This project integrates pathway retrieval, gene extraction, mutation annotation, and interactive network visualization to study oncogenic interactions involved in reproductive cancers.

This project is an AI-assisted bioinformatics platform for ovarian cancer mutation analysis, biomarker prioritization, and systems biology visualization. The platform integrates TCGA-derived genomics datasets, STRING protein interaction networks, Cytoscape-based network analysis, and interactive Streamlit deployment.

The application enables users to:

- Explore ovarian cancer mutation profiles
- Visualize protein interaction networks
- Interpret systems biology relationships
- Identify highly mutated hub genes
- Perform AI-based biomarker prioritization
- Interact with dynamic cancer pathway visualizations

---

## Features

### TCGA Mutation Analysis
- Mutation frequency visualization
- Ovarian cancer-associated gene analysis
- Candidate biomarker identification

### Interactive STRING Network
- Protein-protein interaction visualization
- Dynamic network exploration
- Hub gene interpretation
- Systems oncology analysis

### AI-Based Biomarker Prioritization
- Mutation-driven risk categorization
- Candidate therapeutic target identification
- Translational bioinformatics interpretation

### Scientific Interpretation Layer
- Biological pathway interpretation
- Network medicine context
- Systems biology explanations
- Research-oriented annotations

---

## Technologies Used

- Python
- Streamlit
- Pandas
- Matplotlib
- PyVis
- NetworkX
- Cytoscape
- STRING Database
- TCGA/cBioPortal datasets

---

## Project Structure

```text
cancer-pathway-visualization-tool/
│
├── app.py
├── README.md
├── requirements.txt
├── sample_data.csv
│
├── output/
│   └── string_tcga_network.html
│
├── scripts/
│   ├── tcga_parser.py
│   ├── string_network.py
│   └── network_visualization.py
│
└── images/

#Scientific Workflow


TCGA ovarian cancer mutation data collection
Mutation frequency analysis
STRING interaction network generation
Cytoscape network interpretation
AI-based biomarker prioritization
Interactive Streamlit deployment
Biological Interpretation

The interaction network highlights highly connected ovarian cancer-associated hub genes such as TP53, TTN, and MUC16. Dense interaction regions suggest coordinated oncogenic pathway dysregulation, genomic instability, and potential therapeutic vulnerabilities.

Large nodes represent genes with elevated mutation frequencies, while highly connected nodes indicate possible systems-level regulatory importance in ovarian cancer progression.

#Applications

Computational oncology
Systems biology
Biomarker discovery
Network medicine
Translational bioinformatics
Cancer pathway analysis
Deployment

#Streamlit Cloud Deployment:
https://cancer-pathway-visualization-tool-fuygqkjnbciynwuq2mq8pa.streamlit.app/

#GitHub Repository:
https://github.com/MithulaJinde317-hub/cancer-pathway-visualization-tool

#Scientific Data Sources


TCGA ovarian cancer datasets via cBioPortal
STRING protein interaction database
Cytoscape systems biology platform

#References

Cerami E, Gao J, Dogrusoz U, et al.
The cBio Cancer Genomics Portal: An Open Platform for Exploring Multidimensional Cancer Genomics Data. Cancer Discovery. 2012.
Gao J, Aksoy BA, Dogrusoz U, et al.Integrative Analysis of Complex Cancer Genomics and Clinical Profiles Using the cBioPortal.Science Signaling. 2013.
Cytoscape: A Software Environment for Integrated Models of Biomolecular Interaction Networks.Genome Research. 2003.
String database: Szklarczyk, D., Kirsch, R., Koutrouli, M., Nastou, K., Mehryary, F., Hachilif, R., Gable, A. L., Fang, T., Doncheva, N. T., Pyysalo, S., Bork, P., Jensen, L. J., & von Mering, C. (2023). The STRING database in 2023: protein-protein association networks and functional enrichment analyses for any sequenced genome of interest. Nucleic acids research, 51(D1), D638-D646. https://doi.org/10.1093/nar/gkac1000
