import os

# Define the folder structure
folders = [
    "backend/security/red_team",
    "backend/security/blue_team",
    "backend/reporting",
    "docs"
]

# Define the empty files to create
files = {
    "backend/security/red_team/recon.py": "# AWS Recon & Enumeration\n",
    "backend/security/red_team/network_scan.py": "# Network Scanning with Nmap\n",
    "backend/security/red_team/s3_exploit.py": "# S3 Bucket Exploitation\n",
    "backend/security/red_team/privilege_escalation.py": "# IAM Privilege Escalation\n",
    "backend/security/red_team/attack_simulation.py": "# Simulated AWS Attacks\n",
    "backend/security/blue_team/iam_checker.py": "# IAM Security Auditing\n",
    "backend/security/blue_team/cloudtrail_checker.py": "# CloudTrail & GuardDuty Verification\n",
    "backend/security/blue_team/s3_auditor.py": "# S3 Security Monitoring\n",
    "backend/security/blue_team/ec2_security.py": "# EC2 Security Group Analysis\n",
    "backend/security/blue_team/logging.py": "# Security Logging\n",
    "backend/reporting/generate_reports.py": "# Generate security & pentest reports\n",
    "backend/reporting/s3_storage.py": "# Store security logs in AWS S3\n",
    "backend/reporting/sns_alerts.py": "# Send security notifications via AWS SNS\n",
    "backend/config.py": "# Configuration settings\n",
    "backend/utils.py": "# Utility functions\n",
    "backend/main.py": "# Entry point for SkyeVault Ops\n",
    "docs/readme.md": "# Documentation for SkyeVault Ops\n"
}

# Create folders if they don't exist
for folder in folders:
    os.makedirs(folder, exist_ok=True)

# Create files with initial content
for file_path, content in files.items():
    with open(file_path, "w") as f:
        f.write(content)

print("✅ SkyeVault Ops folder structure is now set up!")
