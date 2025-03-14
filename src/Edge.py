from src.Node import * 
class Edge(): 
    def __init__(self,point1:Node, point2:Node, label:str) -> None:
        self.a = point1 
        self.b = point2
        self.attributes = {
                "label": label
                }
