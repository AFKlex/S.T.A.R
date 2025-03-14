class Node():
    def __init__(self,name):
        self.name = name
        self.color = "#a7a7a7"
        self.attributes={
                }
        
    def __str__(self):
        return f"{self.name}"

    def get_attribute(self):
        return self.attributes

    def add_attribute(self, key,value):
        self.attributes[key] = value 

    def set_attribute(self, dictonary:dict):
        self.attributes = dictonary
