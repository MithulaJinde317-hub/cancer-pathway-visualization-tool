genes = []

with open("../data/ovarian_cancer_pathway.txt", "r", encoding="utf-8") as file:
    lines = file.readlines()

capture = False

for line in lines:

    if line.startswith("GENE"):
        capture = True

    if capture:

        if line.startswith("COMPOUND"):
            break

        parts = line.strip().split()

        if len(parts) > 1:
            gene_name = parts[1]
            genes.append(gene_name)

# Remove duplicates
unique_genes = list(set(genes))

print("Total Genes Extracted:", len(unique_genes))

print("\nSample Genes:\n")

for gene in unique_genes[:20]:
    print(gene)