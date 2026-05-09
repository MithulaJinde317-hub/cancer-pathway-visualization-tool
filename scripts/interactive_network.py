from pyvis.network import Network
import networkx as nx

# Create graph
G = nx.Graph()

# Gene data with mutation status
genes = {
    "TP53": "mutated",
    "BRCA1": "tumor_suppressor",
    "PIK3CA": "mutated",
    "KRAS": "mutated",
    "AKT1": "normal",
    "PTEN": "tumor_suppressor",
    "EGFR": "normal",
    "MYC": "mutated"
}

# Add nodes with colors
for gene, status in genes.items():

    if status == "mutated":
        color = "red"

    elif status == "tumor_suppressor":
        color = "blue"

    else:
        color = "green"

    G.add_node(gene, color=color)

# Interactions
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

# Create PyVis network
net = Network(
    height="750px",
    width="100%",
    bgcolor="#222222",
    font_color="white"
)

# Import graph
net.from_nx(G)

# Save visualization
net.save_graph("cancer_mutation_network.html")

print("Cancer mutation network created successfully!")