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