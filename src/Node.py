import numpy as np 
import matplotlib.colors as mcolors

class Node():
    def __init__(self,name, serverity = 1.0):
        self.name = name
        self.severity = serverity
        self.color = self.severity_to_color() 
        self.attributes={
                }
        
    def __str__(self):
        return f"{self.name}"

    def get_attribute(self):
        return self.attributes

    def add_attribute(self, key,value):
        self.attributes[key] = value 

    def set_attributes(self, dictonary:dict):
        self.attributes = dictonary

    def set_severity(self,serverity):
        self.severity = serverity
        self.severity_to_color()

    def severity_to_color(self):
        """Map severity (0-10) to a color between green, yellow, and red, and return as hex."""
        severity = np.clip(self.severity, 0, 10)  # Ensure severity is within bounds
        hue = (1 - (severity / 10)) * 120  # Green (120°) to Red (0°) in HSV
        rgb = mcolors.hsv_to_rgb([hue / 360, 1, 1])  # Convert HSV to RGB
        return mcolors.to_hex(rgb)  # Convert to HEX format 
