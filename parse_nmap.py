import xml.etree.ElementTree as ET

cvss_db = {
    "OpenSSH 8.2p1": {"cve": "CVE-2021-41617", "score": 7.5},
    "SimpleHTTPServer 0.6": {"cve": "CVE-2019-12345", "score": 5.3},
    "Apache 2.4.49": {"cve": "CVE-2021-41773", "score": 9.8},
    "Telnet": {"cve": "CVE-2001-0674", "score": 10.0}
}

def parse_nmap_xml(file_path):
    print(f"Parsing {file_path}...\n")
    tree = ET.parse(file_path)
    root = tree.getroot()

    for host in root.findall('host'):
        status = host.find('status').get('state')
        print(f"Host status: {status}")

        for port in host.findall('.//port'):
            port_id = port.get('portid')
            protocol = port.get('protocol')
            state = port.find('state').get('state')
            service = port.find('service').get('name')
            print(f"Port {port_id}/{protocol} is {state} running {service}")


           
            if service in cvss_db:
                score = cvss_db[service]["score"]
                cve = cvss_db[service]["cve"]
                risk = "High" if score >= 7 else "Medium" if score >= 4 else "Low"
                print(f"→ CVSS Score: {score} ({risk}) – {cve}")
            else:
                print("→ No CVSS data available for this service.")

if __name__ == "__main__":
    parse_nmap_xml("scan8080.xml")
