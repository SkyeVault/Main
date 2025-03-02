# SkyeVault Ops: Ethical Hacking & Cloud Security Lab Guide  
*A Complete Guide to My AWS Security & Penetration Testing Project*  

---

## ** Introduction**  
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
└── skyevault-ops
    ├── README.md
    ├── __pycache__
    │   └── app.cpython-38.pyc
    ├── app.py
    ├── backend
    │   ├── api.py
    │   ├── config.py
    │   ├── ethical-hacking-penetration-testing-guide
    │   ├── main.py
    │   ├── reporting
    │   │   ├── __init__.py
    │   │   ├── generate_reports.py
    │   │   ├── s3_storage.py
    │   │   └── sns_alerts.py
    │   ├── security
    │   │   ├── SELECT
    │   │   ├── __init__.py
    │   │   ├── __pycache__
    │   │   │   └── database.cpython-38.pyc
    │   │   ├── blue_team
    │   │   │   ├── __pycache__
    │   │   │   │   ├── database.cpython-38.pyc
    │   │   │   │   └── logging.cpython-38.pyc
    │   │   │   ├── blue_team_logging.py
    │   │   │   ├── cloudtrail_checker.py
    │   │   │   ├── database.py
    │   │   │   ├── guardduty_check.py
    │   │   │   ├── iam_security_checker.py
    │   │   │   ├── s3_auditor.py
    │   │   │   └── security_reports.db
    │   │   ├── database.py
    │   │   ├── red_team
    │   │   │   ├── attack_simulation.py
    │   │   │   ├── network_scan.py
    │   │   │   ├── privilege_escalation.py
    │   │   │   ├── recon.py
    │   │   │   └── s3_exploit.py
    │   │   ├── security_reports.db
    │   │   └── view_reports.py
    │   ├── setup_skyevault_structure.py
    │   └── utils.py
    ├── docs
    │   ├── README.md
    │   ├── api_docs
    │   └── setup.md
    ├── frontend
    │   ├── package.json
    │   ├── public
    │   └── src
    ├── progress-log.md
    ├── requirements.txt
    ├── scripts
    ├── security_logs.json
    ├── security_reports.db
    ├── static
    │   ├── css
    │   │   └── style.css
    │   └── js
    │       └── main.js
    └── templates
        └── index.html


📝 Ethical Hacking Guidelines

✅ Allowed Penetration Tests (No AWS Approval Needed)
	•	EC2 Instances
	•	RDS (Databases)
	•	S3 Buckets
	•	CloudFront
	•	API Gateway
	•	AWS Aurora
	•	AWS Lightsail
	•	Elastic Beanstalk

🚫 Prohibited Without AWS Permission
	•	Denial of Service (DoS) Attacks
	•	Port Flooding
	•	DNS Zone Walking
	•	Stress Testing AWS Infrastructure

SkyeVault Ops: The Shift to Rust & DevOps Transparency

Vision Statement:
SkyeVault Ops is evolving into a fully Rust-based cloud security and automation project with a focus on high-performance security tooling and modern DevOps practices. To support this, we’re embracing transparent development workflows and exploring a transition to GitLab for CI/CD and project management.
