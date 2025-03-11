import networkx as nx
from pyvis.network import Network

# Create a directed attack graph
G = nx.DiGraph()

# Add attack nodes with additional attributes (IP, open ports, versions)
nodes = [
    ("Attacker", "red", {"IP": "192.168.1.10", "Open Ports": "None", "Version": "N/A"}),
    ("Web Server", "blue", {"IP": "192.168.1.20", "Open Ports": "80, 443", "Version": "Apache 2.4"}),
    ("Database Server", "blue", {"IP": "192.168.1.30", "Open Ports": "3306", "Version": "MySQL 8.0"}),
    ("Weak Credentials", "orange", {"IP": "N/A", "Open Ports": "None", "Version": "N/A"}),
    ("CVE-2023-XXXX", "yellow", {"IP": "N/A", "Open Ports": "N/A", "Version": "N/A"}),
    ("Admin Account", "green", {"IP": "N/A", "Open Ports": "None", "Version": "N/A"}),
]

# Add nodes with colors and additional attributes
for node, color, attributes in nodes:
    G.add_node(node, color=color, **attributes)

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

# Add nodes with custom attributes
for node, attributes in G.nodes(data=True):
    # Create a readable tooltip with simple line breaks
    tooltip = f"IP Address: {attributes['IP']}\nOpen Ports: {attributes['Open Ports']}\nVersion: {attributes['Version']}"
    net.add_node(node, 
                 color=attributes["color"], 
                 size=20, 
                 font={'size': 14, 'color': 'black'}, 
                 shape='dot', 
                 title=tooltip)  # Use title to show the better formatted tooltip

# Add edges with custom labels
for src, dst, attributes in G.edges(data=True):
    net.add_edge(src, dst, title=attributes["label"], width=2, color='gray')

# Set the layout for better visualization
net.force_atlas_2based(gravity=0.1, central_gravity=0.1, spring_length=100, spring_strength=0.05, damping=0.9)

# Apply physics settings for better arrangement
net.show_buttons(filter_=['physics'])

# Generate interactive visualization and explicitly set notebook=False
net.show("attack_graph_with_simple_tooltip.html", notebook=False)

