from src.Node import * 

class NodeManager():

    def __init__(self) -> None:
        self.nodes = {}  # Dictionary to store nodes by name or other identifiers 

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

    def display_node(self, node_name):
        """Display the node's attributes."""
        node = self.get_node(node_name)
        if node:
            print(node.attributes)
        else:
            print(f"Node {node_name} not found.")
