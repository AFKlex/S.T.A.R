from src.Node import * 
from src.GraphManager import *
from src.NmapScan import * 

if __name__ == "__main__":
    graph_manager = GraphManager()
    node_manager = NodeManager()

    #host_a = Node("Host_A",serverity=9.5)

    #host_a.set_attribute({"IP":"10.10.10.10","OS":"Windows 10"})

    #host_b = Node("Host_B",serverity=5.9)
    #host_c = Node("Host_C")

    #graph_manager.add_node(host_a)
    #graph_manager.add_node(host_b)
    #graph_manager.add_node(host_c)

    #edge = Edge(host_a,host_b, label="Fuck you")
    #edge2 = Edge(host_a,host_c, label="Fuck you")
    #edge3 = Edge(host_a,host_a, label="Fuck you 2")

    #graph_manager.add_edge(edge)
    #graph_manager.add_edge(edge2)
    #graph_manager.add_edge(edge3)

    NmapScan("./data/nmap.xml",node_manager)

    for entry in node_manager.list_nodes():
        print(entry)

    graph_manager.load_node_manager(node_manager)
    
    graph_manager.generate_graph()



