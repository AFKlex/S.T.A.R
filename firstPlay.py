import networkx as nx
from pyvis.network import Network

# Create a directed attack graph
G = nx.DiGraph()

# Add attack nodes
nodes = [
    ("Attacker", "red"),
    ("Web Server", "blue"),
    ("Database Server", "blue"),
    ("Weak Credentials", "orange"),
    ("CVE-2023-XXXX", "yellow"),
    ("Admin Account", "green"),
]

# Add nodes with colors
for node, color in nodes:
    G.add_node(node, color=color)

# Define attack paths (edges)
edges = [
    ("Attacker", "Web Server", "Exploits CVE-2023-XXXX"),
    ("Web Server", "Database Server", "Lateral Movement"),
    ("Web Server", "Weak Credentials", "Steals Passwords"),
    ("Weak Credentials", "Database Server", "Privilege Escalation"),
    ("Database Server", "Admin Account", "Admin Access Gained"),
]

# Add edges with labels
for src, dst, label in edges:
    G.add_edge(src, dst, label=label)

# Create a pyvis network
net = Network(directed=True)

# Add nodes with colors
for node, attributes in G.nodes(data=True):
    net.add_node(node, color=attributes["color"])

# Add edges with labels
for src, dst, attributes in G.edges(data=True):
    net.add_edge(src, dst, title=attributes["label"])

# Generate interactive visualization and explicitly set notebook=False
net.show("attack_graph.html", notebook=False)  # Explicitly set notebook=False

