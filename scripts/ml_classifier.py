import pandas as pd
from sklearn.ensemble import RandomForestClassifier
from sklearn.model_selection import train_test_split
from sklearn.metrics import classification_report

# =========================
# LOAD TCGA DATA
# =========================

file_path = r"M:\short projects\project 2\tcga_data\ov_tcga_pan_can_atlas_2018\ov_tcga_pan_can_atlas_2018\data_mutations.txt"

df = pd.read_csv(
    file_path,
    sep="\t",
    comment="#",
    low_memory=False
)

# =========================
# MUTATION COUNTS
# =========================

gene_counts = df["Hugo_Symbol"].value_counts()

# Create dataframe
data = pd.DataFrame({
    "Gene": gene_counts.index,
    "Mutation_Count": gene_counts.values
})

# =========================
# CREATE LABELS
# =========================

# High-risk genes = mutation count > median
median_value = data["Mutation_Count"].median()

data["High_Risk"] = (
    data["Mutation_Count"] > median_value
).astype(int)

# =========================
# FEATURES & LABELS
# =========================

X = data[["Mutation_Count"]]
y = data["High_Risk"]

# Split data
X_train, X_test, y_train, y_test = train_test_split(
    X,
    y,
    test_size=0.2,
    random_state=42
)

# =========================
# TRAIN MODEL
# =========================

model = RandomForestClassifier()

model.fit(X_train, y_train)

# Predictions
y_pred = model.predict(X_test)

# =========================
# RESULTS
# =========================

print("\nClassification Report:\n")

print(classification_report(y_test, y_pred))

# =========================
# PREDICT TOP GENES
# =========================

data["Prediction"] = model.predict(X)

print("\nPredicted High-Risk Genes:\n")

print(
    data[data["Prediction"] == 1]
    .head(20)
)