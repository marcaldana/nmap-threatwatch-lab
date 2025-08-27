# nmap-threatwatch-lab
Python-based Nmap lab for port scanning, service detection, and XML parsing. Built for Security+ learning, ThreatWatch integration, and portfolio impact.

This lab simulates a basic threat detection workflow using Nmap and Python. It scans a live HTTP service, parses the XML output, and extracts host status, port state, and service information. The goal is to build a reproducible, recruiter-ready cybersecurity project.

## 🖥️ Environment

This lab was built and tested using:

- **Kali Linux 2023.2** running inside a **VMware Workstation** virtual machine
- Python 3.13 and Nmap 7.95
- Local HTTP server on port 8080 for scan simulation

Using Kali in a VM ensures a safe, isolated environment for testing and documentation, and mirrors real-world penetration testing setups.

## 🔧 Lab Workflow

1. Start a Python HTTP server on port 8080
2. Run an Nmap scan and save output to XML
3. Parse the XML using Python to extract:
   - Host status
   - Port number and protocol
   - Service name and version
4. Display results in terminal


