import networkx as nx 
from src.NodeManager import NodeManager
from pyvis.network import Network
from src.Node import * 
from src.Edge import * 

class GraphManager():
    def __init__(self):
        self.graph = nx.DiGraph()
        self.net = Network(directed=True)


    def add_node(self,node:Node):
        self.graph.add_node(node.name,color=node.color, **node.attributes)

    def add_edge(self, edge:Node):
        self.graph.add_edge(edge.a.name, edge.b.name, label=edge.attributes["label"])

    def load_node_manager(self,node_manager:NodeManager):

        for node in node_manager.list_nodes():
            self.add_node(node)

        for edge in node_manager.get_edges():
            self.add_edge(edge)

    def generate_graph(self):            
        # Add nodes with colors
        for node, attributes in self.graph.nodes(data=True):

            tooltip = ""
            for key, value in attributes.items():
                if key == "color":
                    continue
                tooltip += f"{key}: {value}\n"


            self.net.add_node(node, color=attributes["color"], title=tooltip)  # Added title for tooltip

        # Add edges with labels
        for src, dst, attributes in self.graph.edges(data=True):
            print(attributes)
            self.net.add_edge(src, dst, title=attributes["label"])

        # Apply physics settings for better arrangement
        self.net.show_buttons(filter_=['physics'])

        # Generate interactive visualization and explicitly set notebook=False
        self.net.show("attack_graph.html", notebook=False)  # Explicitly set notebook=False


