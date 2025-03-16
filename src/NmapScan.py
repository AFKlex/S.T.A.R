import xml.etree.ElementTree as ET

from src.NodeManager import NodeManager


class NmapScan():

    def __init__(self,file_path,node_manager:NodeManager) -> None:
        self.file_path = file_path 
        self.node_manager = node_manager
        self.parse_nmap_xml()

    def parse_nmap_xml(self):
        tree = ET.parse(self.file_path)
        root = tree.getroot()
        
        for host in root.findall('host'):
            address = host.find("address").attrib.get("addr")
            status = host.find("status").attrib.get("state")
            
            host_node = self.node_manager.create_host(name=address, ip_address=address) 

            for port in host.findall("ports/port"):
                portid =port.attrib.get("portid")
                protocol = port.attrib.get("protocol")
                state = port.find("state").attrib.get("state")
                service_elem = port.find("service")
                service = service_elem.attrib.get("name") if service_elem is not None else "unknown"
                port_node = self.node_manager.create_service(service,portid)

                self.node_manager.add_edge(port_node,host_node,portid)
            
        


