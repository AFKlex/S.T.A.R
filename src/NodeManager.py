from src.Node import * 
from src.Edge import * 

class NodeManager():

    def __init__(self) -> None:
        self.nodes = {}  # Dictionary to store nodes by name or other identifiers 
        self.edges = []

    def add_node(self, node):
        """Add a node to the manager."""
        self.nodes[node.name] = node

    def remove_node(self, node_name):
        """Remove a node by name."""
        if node_name in self.nodes:
            del self.nodes[node_name]
        else:
            print(f"Node {node_name} not found.")

    def get_node(self, node_name):
        """Retrieve a node by name."""
        return self.nodes.get(node_name, None)

    def create_host(self, name, ip_address, severity=1.0):
        """Create and add a Host node."""
        node = Node(name, severity)
        node.set_attributes({"type": "Host", "IP-Address": ip_address})
        self.add_node(node)
        return node

    def create_service(self, name, port, severity=1.0):
        """Create and add a Service node."""
        node = Node(name, severity)
        node.set_attributes({"type": "Service", "Port": port})
        self.add_node(node)
        return node

    def update_severity(self, node_name, severity):
        """Update the severity of an existing node."""
        node = self.get_node(node_name)
        if node:
            node.set_severity(severity)
        else:
            print(f"Node {node_name} not found.")

    def list_nodes(self):
        """List all nodes."""
        return list(self.nodes.values())

    def add_edge(self,from_node:Node, to_node:Node, label:str):
        """Create a Edge between two Nodes"""
        self.edges.append(Edge(from_node,to_node, label))


    def get_edges(self):
        """ Get all Edges"""
        return self.edges




