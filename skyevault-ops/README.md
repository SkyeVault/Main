# 🔥 SkyeVault Ops: Ethical Hacking & Cloud Security Lab Guide  
📌 *A Complete Guide to My AWS Security & Penetration Testing Project*  

---

## **🔍 Introduction**  
Welcome to **SkyeVault Ops**, a security automation and penetration testing framework designed for **ethical hacking, cloud security auditing, and AWS penetration testing**.  

This repository is a **live demonstration of my AWS security journey**, showing **real-world security automation, penetration testing, and ethical hacking workflows**.  

---

## **🎯 Mission: Ethical Hacking & Cloud Security Testing**  
The goal of **SkyeVault Ops** is to create a **self-sufficient security testing framework** that enables:  
✅ **Continuous AWS security monitoring**  
✅ **Automated penetration testing & Red Team exercises**  
✅ **Real-world vulnerability assessment & ethical hacking simulations**  

This project will grow as I continue **expanding my cybersecurity expertise** and developing **automation tools for AWS security**.

---

## **🛠️ Features & Capabilities**  

| **Feature**        | **Description** |
|--------------------|----------------|
| ✅ **Security Monitoring (Blue Team)**  | Automates AWS security audits (IAM, S3, EC2, CloudTrail) |
| 🚀 **Penetration Testing (Red Team)**  | Simulates cloud attacks, privilege escalation, network scans |
| 🔐 **IAM Security Auditing**  | Detects overprivileged users, misconfigured roles, and weak permissions |
| 🕵️ **AWS Recon & Enumeration** | Identifies EC2 instances, S3 buckets, exposed services |
| 🌐 **Network Scanning**  | Uses `nmap` to detect open ports & attack surfaces |
| 📂 **S3 Bucket Security** | Scans for public buckets, tests write access vulnerabilities |
| 🔒 **CloudTrail & GuardDuty Analysis**  | Ensures AWS logs & threat detection are working properly |
| 📊 **Automated Reports** | Generates security & pentest logs, stored in AWS S3 |

---

## **🔴 Red Team vs. 🔵 Blue Team Structure**  

To **separate offensive and defensive security**, SkyeVault Ops is organized into **two main security teams**:  

### **🔴 Red Team (Penetration Testing & Exploitation)**  
- **`recon.py`** → Identifies AWS resources (EC2, S3, IAM, API endpoints)  
- **`network_scan.py`** → Runs `nmap` on EC2 instances to detect open ports  
- **`s3_exploit.py`** → Tests public S3 buckets for write/read vulnerabilities  
- **`privilege_escalation.py`** → Identifies IAM roles that allow privilege escalation  
- **`attack_simulation.py`** → Runs AWS attack simulations to test GuardDuty & logging  

### **🔵 Blue Team (Security Monitoring & Defense)**  
- **`iam_checker.py`** → Scans for weak IAM roles, missing MFA, excessive permissions  
- **`cloudtrail_checker.py`** → Ensures logging & GuardDuty are enabled  
- **`s3_auditor.py`** → Detects publicly accessible S3 buckets  
- **`ec2_security.py`** → Audits EC2 security groups & firewall misconfigurations  
- **`logging.py`** → Tracks security events & pentest activity  

---

## **📂 Folder Structure**
```plaintext
skyevault-ops/
│── backend/
│   ├── security/
│   │   ├── red_team/   # Offensive Security (Pentesting)
│   │   │   ├── recon.py              
│   │   │   ├── network_scan.py       
│   │   │   ├── s3_exploit.py         
│   │   │   ├── privilege_escalation.py  
│   │   │   ├── attack_simulation.py  
│   │   │
│   │   ├── blue_team/  # Defensive Security (Monitoring)
│   │   │   ├── iam_checker.py        
│   │   │   ├── cloudtrail_checker.py 
│   │   │   ├── s3_auditor.py         
│   │   │   ├── ec2_security.py       
│   │   │   ├── logging.py            
│   │   │
│   │   ├── __init__.py
│   │
│   ├── reporting/  # Security logs & reporting
│   │   ├── generate_reports.py  
│   │   ├── s3_storage.py        
│   │   ├── sns_alerts.py        
│   │   ├── __init__.py
│   │
│   ├── config.py  # Configuration settings
│   ├── utils.py   # Shared helper functions
│   ├── main.py    # Toggles between Red Team & Blue Team testing
│
│── frontend/ (To be built later)
│── docs/ (Documentation & user guides)
│── README.md  (Project overview & setup instructions)
│── requirements.txt  (Python dependencies)
│── .gitignore