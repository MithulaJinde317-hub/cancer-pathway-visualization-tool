import pandas as pd
import networkx as nx
from pyvis.network import Network

# =========================
# LOAD TCGA MUTATION DATA
# =========================

file_path = r"M:\short projects\project 2\tcga_data\ov_tcga_pan_can_atlas_2018\ov_tcga_pan_can_atlas_2018\data_mutations.txt"

df = pd.read_csv(
    file_path,
    sep="\t",
    comment="#",
    low_memory=False
)

# =========================
# TOP MUTATED GENES
# =========================

gene_counts = df["Hugo_Symbol"].value_counts()

top_genes = gene_counts.head(20)

print("Top Mutated Genes:\n")
print(top_genes)

# =========================
# CREATE NETWORK
# =========================

G = nx.Graph()

# Add nodes
for gene in top_genes.index:
    G.add_node(gene)

# Add simple connections
genes = list(top_genes.index)

for i in range(len(genes)-1):
    G.add_edge(genes[i], genes[i+1])

# =========================
# PYVIS VISUALIZATION
# =========================

net = Network(height="750px", width="100%", bgcolor="#222222", font_color="white")

net.from_nx(G)

# Highlight top genes
for node in net.nodes:
    node["color"] = "red"
    node["size"] = 25

# Save GraphML for Cytoscape
nx.write_graphml(G, "../output/tcga_network.graphml")

# Save interactive HTML
net.save_graph("../output/tcga_mutation_network.html")

print("\nTCGA Mutation Network Created Successfully!")