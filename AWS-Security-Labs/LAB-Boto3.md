# AWS Security Automation Lab with Boto3

## **Overview**
This lab documents all the steps taken to set up AWS CLI, troubleshoot macOS issues, install Boto3, and automate AWS security tasks. This serves as a structured guide for future reference and portfolio building.

---

## **1. Setting Up AWS CLI on macOS**
### **Problem Encountered:**
- `aws command not found`
- **Cause:** AWS CLI was not installed.

### **Solution: Installing AWS CLI**
Run the following command to install AWS CLI via Homebrew:
```bash
brew install awscli
```

### **Verifying Installation**
After installation, check if AWS CLI is properly installed:
```bash
aws --version
```
**Expected Output:**
```
aws-cli/2.x.x Python/x.x.x Darwin/x86_64 source
```

### **Configuring AWS Credentials**
To authenticate AWS CLI, run:
```bash
aws configure
```
Enter the following details:
```
AWS Access Key ID [None]: YOUR_ACCESS_KEY
AWS Secret Access Key [None]: YOUR_SECRET_KEY
Default region name [None]: us-east-1
Default output format [None]: json
```

### **Test AWS Connection**
To verify that AWS CLI is properly configured:
```bash
aws sts get-caller-identity
```

**Expected Output:**
```
{
    "UserId": "XXXXXXXXXX",
    "Account": "123456789012",
    "Arn": "arn:aws:iam::123456789012:user/SkyeVaultUser"
}
```

---

## **2. Installing Python & Boto3**
### **Verifying Python Installation**
Check if Python is installed:
```bash
python3 --version
```
If not installed, install Python using Homebrew:
```bash
brew install python3
```

### **Installing Boto3 (AWS SDK for Python)**
```bash
pip3 install boto3
```

### **Verifying Boto3 Installation**
```python
import boto3
print(boto3.__version__)
```

---

## **3. Writing and Running a Boto3 IAM Script**
### **Creating the Script**
Create a new Python script named `list_iam_users.py`:
```bash
nano list_iam_users.py
```
Paste the following code:
```python
import boto3

# Create IAM client
iam = boto3.client("iam")

# Get list of IAM users
response = iam.list_users()

# Print IAM users with creation dates
print("IAM Users in AWS Account:")
for user in response['Users']:
    print(f"User: {user['UserName']}, Created On: {user['CreateDate']}")
```
Save and exit: `CTRL + X`, then `Y`, then `Enter`

### **Running the Script**
```bash
python3 list_iam_users.py
```

**Expected Output:**
```
IAM Users in AWS Account:
User: SkyeVaultUser, Created On: 2025-02-18 17:22:24+00:00
```

---

## **4. Troubleshooting macOS Issues**
### **Issue 1: Homebrew Not Found on macOS 12**
#### **Problem:**
- `brew: command not found`
- **Cause:** Homebrew was missing or incorrectly installed.

#### **Solution: Reinstalling Homebrew**
Run:
```bash
/bin/bash -c "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/HEAD/install.sh)"
```
Then restart the terminal and run:
```bash
brew --version
```

---

## **5. Expanding the Script for Security Checks**
### **List Inactive IAM Users (Next Task)**
Modify the script to find IAM users who haven’t logged in for 90+ days:
```python
import boto3
from datetime import datetime, timedelta

# Create IAM client
iam = boto3.client("iam")

# Get list of IAM users
response = iam.list_users()

# Define cutoff date (90 days ago)
cutoff_date = datetime.utcnow() - timedelta(days=90)

print("Inactive IAM Users (No Login for 90+ Days):")
for user in response['Users']:
    if 'PasswordLastUsed' in user:
        last_used = user['PasswordLastUsed'].replace(tzinfo=None)
        if last_used < cutoff_date:
            print(f"User: {user['UserName']}, Last Used: {last_used}")
    else:
        print(f"User: {user['UserName']}, Never Logged In")
```

Run it with:
```bash
python3 list_inactive_iam_users.py
```

---

## **6. Pushing to GitHub**
### **Create a Repository**
```bash
git init
git add list_iam_users.py
```

### **Commit and Push**
```bash
git commit -m "Added IAM user listing script"
git branch -M main
git remote add origin YOUR_GITHUB_REPO_URL
git push -u origin main
```

---

## **7. Summary of Accomplishments**
✅ Installed and configured AWS CLI on macOS  
✅ Fixed Homebrew issues on macOS 12  
✅ Installed Boto3 and verified Python setup  
✅ Wrote and executed a Boto3 script to list IAM users  
✅ Expanded the script for security automation (inactive user detection)  
✅ Documented the entire process for future use  
✅ Prepared the project for GitHub publication  

---

### **🚀 Next Steps**
- [ ] Automate IAM security checks and alerts
- [ ] Scan S3 buckets for public access risks
- [ ] Implement AWS logging and monitoring with Boto3
- [ ] Continue building an AWS security GitHub portfolio

---
This lab serves as a **real-world AWS security automation project** and a **step-by-step learning resource** for mastering AWS & Boto3!
