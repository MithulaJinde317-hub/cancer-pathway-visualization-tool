from pyvis.network import Network
import networkx as nx
import random

# Read extracted genes
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
            gene = parts[1]
            genes.append(gene)

# Remove duplicates
genes = list(set(genes))

# Limit for visualization clarity
genes = genes[:25]

# Create graph
G = nx.Graph()

# Add nodes with random mutation labels
for gene in genes:

    mutation_status = random.choice([
        "mutated",
        "tumor_suppressor",
        "normal"
    ])

    if mutation_status == "mutated":
        color = "red"

    elif mutation_status == "tumor_suppressor":
        color = "blue"

    else:
        color = "green"

    G.add_node(
        gene,
        color=color,
        title=f"{gene} ({mutation_status})"
    )

# Create random interactions
for i in range(len(genes) - 1):
    G.add_edge(genes[i], genes[i + 1])

# PyVis network
net = Network(
    height="800px",
    width="100%",
    bgcolor="#1e1e1e",
    font_color="white"
)

net.from_nx(G)

# Physics layout
net.barnes_hut()

# Save graph
net.save_graph("../output/real_cancer_network.html")

print("Real cancer pathway network created successfully!")