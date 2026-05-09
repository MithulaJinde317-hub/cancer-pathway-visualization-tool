import networkx as nx
import matplotlib.pyplot as plt

# Sample cancer-related genes
genes = [
    "TP53",
    "BRCA1",
    "PIK3CA",
    "KRAS",
    "AKT1",
    "PTEN",
    "EGFR",
    "MYC"
]

# Create graph
G = nx.Graph()

# Add genes as nodes
for gene in genes:
    G.add_node(gene)

# Add biological interactions
interactions = [
    ("TP53", "BRCA1"),
    ("TP53", "PIK3CA"),
    ("PIK3CA", "AKT1"),
    ("PTEN", "AKT1"),
    ("KRAS", "EGFR"),
    ("MYC", "TP53"),
    ("BRCA1", "PTEN")
]

G.add_edges_from(interactions)

# Draw network
plt.figure(figsize=(10, 8))

nx.draw(
    G,
    with_labels=True,
    node_size=3000,
    font_size=10
)

plt.title("Cancer Pathway Gene Interaction Network")

plt.show()