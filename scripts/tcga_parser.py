import pandas as pd

# Load TCGA mutation dataset
file_path = r"M:\short projects\project 2\tcga_data\ov_tcga_pan_can_atlas_2018\ov_tcga_pan_can_atlas_2018\data_mutations.txt"
# Read dataset
df = pd.read_csv(
    file_path,
    sep="\t",
    comment="#",
    low_memory=False
)

print("TCGA Mutation Dataset Loaded Successfully!\n")

# Display shape
print("Dataset Shape:")
print(df.shape)

# Extract mutated genes
mutated_genes = df["Hugo_Symbol"]

# Count mutation frequency
gene_counts = mutated_genes.value_counts()

print("\nTop 20 Most Mutated Genes:\n")

print(gene_counts.head(20))