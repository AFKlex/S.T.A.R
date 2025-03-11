import xml.etree.ElementTree as ET

class Port:
    def __init__(self, portid, protocol, state, service):
        self.portid = portid
        self.protocol = protocol
        self.state = state
        self.service = service
    
    def __repr__(self):
        return f"Port(portid={self.portid}, protocol={self.protocol}, state={self.state}, service={self.service})"

class Host:
    def __init__(self, address, status, ports):
        self.address = address
        self.status = status
        self.ports = ports
    
    def __repr__(self):
        return f"Host(address={self.address}, status={self.status}, ports={self.ports})"

class NmapScan:
    def __init__(self, hosts):
        self.hosts = hosts
    
    def __repr__(self):
        return f"NmapScan(hosts={self.hosts})"

def parse_nmap_xml(file_path):
    tree = ET.parse(file_path)
    root = tree.getroot()
    
    hosts = []
    for host in root.findall('host'):
        address = host.find("address").attrib.get("addr")
        status = host.find("status").attrib.get("state")
        
        ports = []
        for port in host.findall("ports/port"):
            portid = port.attrib.get("portid")
            protocol = port.attrib.get("protocol")
            state = port.find("state").attrib.get("state")
            service_elem = port.find("service")
            service = service_elem.attrib.get("name") if service_elem is not None else "unknown"
            
            ports.append(Port(portid, protocol, state, service))
        
        hosts.append(Host(address, status, ports))
    
    return NmapScan(hosts)

if __name__ == "__main__":
    file_path = "A_scan.txt"  # Change to your actual XML file
    scan_data = parse_nmap_xml(file_path)
    print(scan_data)

