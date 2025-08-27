# nmap-threatwatch-lab
Python-based Nmap lab for port scanning, service detection, and XML parsing. Built for Security+ learning, ThreatWatch integration, and portfolio impact.

This lab simulates a basic threat detection workflow using Nmap and Python. It scans a live HTTP service, parses the XML output, and extracts host status, port state, and service information. The goal is to build a reproducible, recruiter-ready cybersecurity project.

## 🔧 Lab Workflow

1. Start a Python HTTP server on port 8080
2. Run an Nmap scan and save output to XML
3. Parse the XML using Python to extract:
   - Host status
   - Port number and protocol
   - Service name and version
4. Display results in terminal


