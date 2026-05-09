import streamlit as st
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
        "AI Predictions"
    ]
)

# =========================
# LOAD DATA
# =========================

file_path = "tcga_data/ov_tcga_pan_can_atlas_2018/ov_tcga_pan_can_atlas_2018/data_mutations.txt"

@st.cache_data
def load_data():

    df = pd.read_csv(
        file_path,
        sep="\t",
        comment="#",
        low_memory=False
    )

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

    st.subheader("TCGA Ovarian Cancer Dataset")

    st.write("Dataset Shape:")
    st.write(df.shape)

    st.write("Dataset Preview:")
    st.dataframe(df.head())

# =========================
# MUTATION ANALYSIS
# =========================

elif section == "Mutation Analysis":

    st.title("Mutation Analysis")

    fig, ax = plt.subplots(figsize=(12, 6))

    top_genes.plot(kind="bar", ax=ax)

    ax.set_title("Top Mutated Ovarian Cancer Genes")
    ax.set_xlabel("Genes")
    ax.set_ylabel("Mutation Frequency")

    plt.xticks(rotation=45)

    st.pyplot(fig)

    st.write("Top Mutated Genes")

    st.dataframe(top_genes)

# =========================
# AI PREDICTIONS
# =========================

elif section == "AI Predictions":

    st.title("AI-Based Biomarker Prioritization")

    prediction_df = pd.DataFrame({
        "Gene": top_genes.index,
        "Mutation_Count": top_genes.values
    })

    prediction_df["Predicted_Risk"] = [
        "High Risk"
        if x > prediction_df["Mutation_Count"].median()
        else "Moderate Risk"
        for x in prediction_df["Mutation_Count"]
    ]

    st.dataframe(prediction_df)

    st.success("AI-based prioritization completed successfully.")