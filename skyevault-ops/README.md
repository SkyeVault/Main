# **SkyeVault Ops: Ethical Hacking & Cloud Security Lab**  
*A Security Testing & Automation Framework for AWS*  

---

## **Introduction**  
**SkyeVault Ops** is a security automation and penetration testing framework designed for **ethical hacking, cloud security auditing, and AWS penetration testing**.  

This repository is a **live development environment** showcasing **real-world security automation, penetration testing, and ethical hacking workflows**. The project is in **early development** and will continue to evolve with improvements in **automation, security tooling, and DevOps integration**.  

---

## **Project Status**  
✅ **Working Frontend & Backend** – Basic implementation in place.  
⚠ **Still in Development** – Security tooling and automation workflows need further work.  
🔄 **Transition to Rust** – Moving core security tools and automation from Python to Rust.  
📌 **Upcoming Enhancements** – CI/CD pipeline integration, advanced pentesting automation, and structured reporting.  

---

## **Project Goals**  

SkyeVault Ops is being built as a **self-sufficient security testing framework** with the following objectives:  

- **Continuous AWS Security Monitoring** – Automate security checks for IAM, S3, EC2, CloudTrail, and GuardDuty.  
- **Penetration Testing & Red Team Simulations** – Simulate real-world attack scenarios on cloud environments.  
- **Secure AWS Auditing & Reporting** – Generate automated security assessments and compliance reports.  
- **Cloud Security Tooling** – Build lightweight, Rust-based security tools for automation and defense.  

---

## **Key Features**  

| **Feature**        | **Description** |
|--------------------|----------------|
| **Security Monitoring (Blue Team)**  | Automates AWS security audits for IAM, S3, EC2, CloudTrail |
| **Penetration Testing (Red Team)**  | Simulates cloud attacks, privilege escalation, network scanning |
| **IAM Security Auditing**  | Detects overprivileged users, misconfigured roles, and weak permissions |
| **AWS Recon & Enumeration** | Identifies EC2 instances, S3 buckets, and exposed services |
| **Network Scanning**  | Uses `nmap` to detect open ports and attack surfaces |
| **S3 Bucket Security** | Scans for public S3 buckets and tests write access vulnerabilities |
| **CloudTrail & GuardDuty Analysis**  | Ensures AWS logs and threat detection are properly configured |
| **Automated Security Reports** | Generates pentest logs and stores reports in AWS S3 |

---

## **Red Team vs. Blue Team Structure**  

To separate **offensive and defensive security**, SkyeVault Ops is organized into **two main sections**:  

### **Red Team (Penetration Testing & Exploitation)**  
- `recon.py` → Identifies AWS resources (EC2, S3, IAM, API endpoints)  
- `network_scan.py` → Runs `nmap` scans on EC2 instances  
- `s3_exploit.py` → Tests public S3 buckets for misconfigurations  
- `privilege_escalation.py` → Identifies IAM privilege escalation paths  
- `attack_simulation.py` → Runs AWS attack simulations to test security response  

### **Blue Team (Security Monitoring & Defense)**  
- `iam_checker.py` → Scans for weak IAM roles, missing MFA, and overprivileged accounts  
- `cloudtrail_checker.py` → Ensures logging and GuardDuty configurations are correct  
- `s3_auditor.py` → Detects publicly accessible S3 buckets and misconfigurations  
- `ec2_security.py` → Audits EC2 security groups and firewall settings  
- `logging.py` → Tracks security events and pentest activity  

---

## **Folder Structure**  
```plaintext
skyevault-ops/
├── README.md
├── app.py
├── backend/
│   ├── api.py
│   ├── config.py
│   ├── security/
│   │   ├── red_team/
│   │   │   ├── attack_simulation.py
│   │   │   ├── network_scan.py
│   │   │   ├── privilege_escalation.py
│   │   │   ├── recon.py
│   │   │   ├── s3_exploit.py
│   │   ├── blue_team/
│   │   │   ├── cloudtrail_checker.py
│   │   │   ├── guardduty_check.py
│   │   │   ├── iam_security_checker.py
│   │   │   ├── s3_auditor.py
│   ├── reporting/
│   │   ├── generate_reports.py
│   │   ├── s3_storage.py
│   │   ├── sns_alerts.py
│   ├── utils.py
├── docs/
│   ├── setup.md
│   ├── api_docs/
├── frontend/
│   ├── package.json
│   ├── src/
├── scripts/
├── requirements.txt
├── security_logs.json
└── templates/
    └── index.html
```

---

## **Ethical Hacking Guidelines**  

### **Allowed AWS Security Tests (No Prior Approval Needed)**  
- **EC2 Instances**  
- **RDS Databases**  
- **S3 Buckets**  
- **CloudFront**  
- **API Gateway**  
- **AWS Aurora & Lightsail**  
- **Elastic Beanstalk**  

### **Prohibited Without AWS Authorization**  
- **Denial of Service (DoS) Attacks**  
- **Port Flooding & Network Stress Testing**  
- **DNS Zone Walking**  
- **Excessive API Requests That Violate AWS TOS**  

---

## **SkyeVault Ops: The Shift to Rust & DevOps Transparency**  

### **Vision Statement**  
SkyeVault Ops is evolving into a **fully Rust-based cloud security and automation project** with a focus on:  
- **High-performance security tooling**  
- **Automated security workflows**  
- **Transparent development workflows**  
- **Modern DevOps integration**  

To support this, the project will begin integrating **Rust-based security automation tools** and transitioning to **GitLab for CI/CD and project management**.  

---

## **Next Steps**  
- **Refactor security scripts to Rust for better performance**.  
- **Implement automated CI/CD workflows for security testing**.  
- **Develop structured AWS attack simulation reports**.  
- **Enhance frontend with security visualization dashboards**.  
- **Deploy a working test environment on AWS Free Tier**.  

---

## **Contributing**  
This is an **independent security research project**, and contributions are currently limited. Future plans include:  
- **Open-sourcing specific security automation tools**.  
- **Providing AWS security testing labs** for learning and experimentation.  
- **Creating in-depth documentation for self-hosted security analysis**.  

If you’re interested in security automation, cloud penetration testing, or Rust-based security tooling, stay tuned for future updates.  

---

## **Final Notes**  
This project is a **work in progress** and will continue to evolve as development progresses. **The focus remains on building an ethical security framework for AWS testing and automation** while ensuring compliance with **AWS penetration testing policies**.  