import pandas as pd
import matplotlib.pyplot as plt

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
# COUNT MUTATIONS
# =========================

gene_counts = df["Hugo_Symbol"].value_counts()

top_genes = gene_counts.head(15)

print("\nTop Mutated Genes:\n")
print(top_genes)

# =========================
# VISUALIZATION
# =========================

plt.figure(figsize=(12,6))

top_genes.plot(kind="bar")

plt.title("Top Mutated Ovarian Cancer Genes")
plt.xlabel("Genes")
plt.ylabel("Mutation Frequency")

plt.xticks(rotation=45)

plt.tight_layout()

# Save figure
plt.savefig("../output/top_mutated_genes.png")

plt.show()