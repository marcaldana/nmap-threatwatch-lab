# nmap-threatwatch-lab
Python-based Nmap lab for port scanning, service detection, and XML parsing. Built for Security+ learning, ThreatWatch integration, and portfolio impact.

This lab simulates a basic threat detection workflow using Nmap and Python. It scans a live HTTP service, parses the XML output, and extracts host status, port state, and service information. The goal is to build a reproducible, recruiter-ready cybersecurity project.

## 🖥️ Environment

This lab was built and tested using:

## 🛠️ Tools Used

- Python 3.11
- Nmap 7.95
- Kali Linux
- VMware Workstation

## 🔧 Lab Workflow

1. Start a Python HTTP server on port 8080
![HTTP Server](Start_python_server_8.png)

2. Run an Nmap scan and save output to XML
![Nmap Scan](Nmap_scan.png)

3. Parse the XML using Python to extract:
![Parser Output](Run_python_parser.png)
   - Host status
   - Port number and protocol
   - Service name and version
5. Display results in terminal


