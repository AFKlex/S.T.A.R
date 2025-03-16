#!/home/afklex/OneDrive/07_Software/Tools/Eigenentwicklung/STAR/venv3/bin/python3
from src.Node import * 
from src.GraphManager import *

if __name__ == "__main__":
    manager = GraphManager()

    host_a = Node("Host_A",serverity=9.5)

    host_a.set_attribute({"IP":"10.10.10.10","OS":"Windows 10"})

    host_b = Node("Host_B",serverity=5.9)
    host_c = Node("Host_C")

    manager.add_node(host_a)
    manager.add_node(host_b)
    manager.add_node(host_c)

    edge = Edge(host_a,host_b, label="Fuck you")
    edge2 = Edge(host_a,host_c, label="Fuck you")
    edge3 = Edge(host_a,host_a, label="Fuck you 2")

    manager.add_edge(edge)
    manager.add_edge(edge2)
    manager.add_edge(edge3)

    manager.generate_graph()



