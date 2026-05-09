import streamlit as st
import streamlit.components.v1 as components
import pandas as pd
import matplotlib.pyplot as plt

# =========================
# PAGE CONFIG
# =========================

st.set_page_config(
    page_title="Cancer Pathway Visualization Tool",
    layout="wide"
)

# =========================
# SIDEBAR
# =========================

st.sidebar.title("Navigation")

section = st.sidebar.radio(
    "Go To",
    [
        "Dataset Overview",
        "Mutation Analysis",
        "AI Predictions",
        "Interactive Network"
    ]
)

# =========================
# LOAD SAMPLE DATA
# =========================

@st.cache_data
def load_data():

    df = pd.read_csv("sample_data.csv")

    return df

df = load_data()

# =========================
# MUTATION COUNTS
# =========================

gene_counts = df["Hugo_Symbol"].value_counts()

top_genes = gene_counts.head(15)

# =========================
# DATASET OVERVIEW
# =========================

if section == "Dataset Overview":

    st.title("Cancer Pathway Visualization Tool")

    st.subheader("Ovarian Cancer Mutation Dataset")

    st.write("Dataset Shape:")
    st.write(df.shape)

    st.write("Dataset Preview:")
    st.dataframe(df)

# =========================
# MUTATION ANALYSIS
# =========================

elif section == "Mutation Analysis":

    st.title("Mutation Analysis")

    fig, ax = plt.subplots(figsize=(12, 6))

    ax.bar(df["Gene"], df["Mutation_Count"])

    ax.set_title("Top Mutated Ovarian Cancer Genes")
    ax.set_xlabel("Genes")
    ax.set_ylabel("Mutation Frequency")

    plt.xticks(rotation=45)

    st.pyplot(fig)

# =========================
# AI PREDICTIONS
# =========================

elif section == "AI Predictions":

    st.title("AI-Based Biomarker Prioritization")

    df["Predicted_Risk"] = [
        "High Risk"
        if x > df["Mutation_Count"].median()
        else "Moderate Risk"
        for x in df["Mutation_Count"]
    ]

    st.dataframe(df)

    st.success("AI-based prioritization completed successfully.")

 
# =========================
# INTERACTIVE NETWORK
# =========================

elif section == "Interactive Network":

components.html(
    html_data,
    height=800,
    scrolling=True
)
    st.title("Interactive STRING Network")

    st.write(
        "Interactive ovarian cancer protein interaction network."
    )

    with open(
        "output/string_tcga_network.html",
        "r",
        encoding="utf-8"
    ) as f:

        html_data = f.read()

    components.html(
        html_data,
        height=800,
        scrolling=True
    )

st.markdown("""
## Biological Interpretation of the STRING Network

### Key Observations

- Large red nodes represent highly mutated ovarian cancer-associated hub genes.
- Highly connected genes may function as master regulators in tumor progression.
- Dense interaction regions indicate coordinated oncogenic pathway activity.
- TP53-centered interactions suggest disruption of DNA repair and apoptosis pathways.
- BRCA-associated interactions indicate genomic instability mechanisms.

### Systems Biology Interpretation

This interaction network demonstrates how ovarian cancer progression involves interconnected molecular signaling pathways rather than isolated gene mutations.

Genes with high connectivity and mutation frequency may serve as:

- candidate biomarkers
- therapeutic targets
- prognostic indicators
- pathway regulators

### Network Medicine Relevance

The network supports systems oncology analysis by identifying biologically important interaction hubs potentially involved in:

- tumor proliferation
- metastasis
- genomic instability
- pathway dysregulation
- treatment resistance
            
---
## Data Sources and Scientific Resources

- TCGA Ovarian Cancer Dataset accessed via cBioPortal
- STRING Protein Interaction Database
- Cytoscape Network Analysis Platform

### References

Cerami et al., *The cBio Cancer Genomics Portal: An Open Platform for Exploring Multidimensional Cancer Genomics Data*, Cancer Discovery (2012).

Gao et al., *Integrative Analysis of Complex Cancer Genomics and Clinical Profiles Using the cBioPortal*, Science Signaling (2013).

Szklarczyk et al., *STRING v11: Protein–Protein Association Networks with Increased Coverage*, Nucleic Acids Research (2019).
""")