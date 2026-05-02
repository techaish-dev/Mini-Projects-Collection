# 🛡️ VulnScan - Advanced Vulnerability Assessment Tool

[![Python](https://img.shields.io/badge/Python-3.7+-blue.svg?style=for-the-badge&logo=python&logoColor=white)](https://python.org)
[![License](https://img.shields.io/badge/License-MIT-yellow.svg?style=for-the-badge)](LICENSE)
[![Security](https://img.shields.io/badge/Security-Research-red.svg?style=for-the-badge)](https://github.com/techaish-dev)

---

## 📋 Overview

**VulnScan** is a comprehensive vulnerability assessment tool designed for educational and authorized security assessments. It performs multiple scanning techniques including port scanning, subdomain enumeration, OS fingerprinting, and integrates with Shodan & VirusTotal APIs for enhanced threat intelligence.

> ⚠️ **Legal Disclaimer**: This tool is intended for **educational and authorized vulnerability assessments only**. Always obtain explicit permission before scanning any system. Unauthorized use may be illegal.

---

## ✨ Features

| Category | Features |
|----------|----------|
| **Network Scanning** | Hostname to IP resolution, Ping availability, OS fingerprinting |
| **Port Scanning** | SYN scan, TCP Connect scan, UDP scan |
| **Web Discovery** | Subdomain enumeration, Directory brute-forcing |
| **Information Gathering** | WHOIS lookup, SSL certificate analysis, Geolocation via ipinfo.io |
| **Threat Intelligence** | VirusTotal reputation check, Shodan device intelligence |
| **Service Detection** | Nmap integration for advanced service fingerprinting |

---

## 🛠️ Tech Stack

| Component | Technology |
|-----------|------------|
| Language | Python 3.x |
| Network Scanning | Scapy, python-nmap |
| DNS Resolution | dnspython |
| WHOIS Lookup | python-whois |
| Threat Intel | Shodan API, VirusTotal API |
| Geolocation | ipinfo.io API |
| Packet Capture | Npcap (Windows) |

---

## 📦 Installation

### Prerequisites

| Requirement | Version |
|-------------|---------|
| Python | 3.7 or higher |
| pip | Latest version |
| Npcap | Latest (Windows only) |
| Administrator/Root | For SYN scans |

### Step 1: Install Python Libraries

```bash
# Install required packages
pip install python-whois
pip install python-nmap
pip install scapy
pip install dnspython
pip install shodan
pip install requests
```

### Step 2: Install Npcap (Windows Only)
Download from: https://npcap.com

During installation, check:

✅ "Install Npcap in WinPcap API-compatible mode"

✅ "Allow all users to access Npcap"

Restart your system

### Step 3: Verify Installation
Check installed packages
```bash
pip list | findstr "scapy nmap shodan"
```

Should show:
scapy
python-nmap
shodan

### Basic Usage

```bash
Run the scanner
python scanner.py

Enter target when prompted
Enter the target IP or website (e.g., 192.168.1.1 or example.com): example.com
```