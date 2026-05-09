import pandas as pd
import requests
import networkx as nx
from pyvis.network import Network

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
# TOP MUTATED GENES
# =========================

gene_counts = df["Hugo_Symbol"].value_counts()

top_genes = list(gene_counts.head(15).index)

print("Top TCGA Genes:")
print(top_genes)

# =========================
# STRING API REQUEST
# =========================

genes_string = "%0d".join(top_genes)

url = f"https://string-db.org/api/tsv/network?identifiers={genes_string}&species=9606"

response = requests.get(url)

lines = response.text.strip().split("\n")

# =========================
# CREATE NETWORK
# =========================

G = nx.Graph()

for line in lines[1:]:
    data = line.split("\t")

    protein1 = data[2]
    protein2 = data[3]

    G.add_edge(protein1, protein2)

# =========================
# EXPORT GRAPHML
# =========================

nx.write_graphml(G, "../output/string_tcga_network.graphml")

# =========================
# PYVIS VISUALIZATION
# =========================

net = Network(
    height="750px",
    width="100%",
    bgcolor="#222222",
    font_color="white"
)

net.from_nx(G)

for node in net.nodes:
    node["color"] = "red"
    node["size"] = 20

net.save_graph("../output/string_tcga_network.html")

print("\nSTRING Interaction Network Created Successfully!")