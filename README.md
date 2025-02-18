# LessonsLearned
AWS learning journey. Documenting hands-on projects in IAM, S3 security, Tor, VPNs, and firewalls.

# SkyeVault Security Lab - AWS & Linux Command Documentation

## 📌 Overview
This repository documents the AWS security lab setup and command-line operations performed to establish and secure an EC2 instance. The goal is to build hands-on AWS security experience, configure IAM users, set up SSH authentication, and apply firewall rules.

---

## **1️⃣ AWS CLI Commands**
### **🔹 Configuring AWS CLI**
```bash
aws configure
```
- **Purpose:** Set up AWS CLI with **Access Key and Secret Key** for authentication.

### **🔹 Listing AWS S3 Buckets**
```bash
aws s3 ls
```
- **Purpose:** Verify AWS CLI authentication by listing available S3 buckets.

### **🔹 Managing IAM Users**
```bash
aws iam list-users
```
- **Purpose:** Display all IAM users, confirming **SkyeVaultUser** was created.

```bash
aws iam list-policies
```
- **Purpose:** List available IAM policies to verify **permission assignments**.

---

## **2️⃣ SSH & Key Authentication Commands**
### **🔹 Connecting to EC2 via SSH**
```bash
ssh -i ~/Downloads/skyvault.pem ubuntu@44.222.212.40
```
- **Purpose:** Attempt SSH login using the **private key**.

### **🔹 Checking Key Permissions**
```bash
ls -l ~/Downloads/skyvault.pem
```
- **Purpose:** Ensure the **private key exists** and has correct permissions.

```bash
chmod 400 ~/Downloads/skyvault.pem
```
- **Purpose:** Restrict key file access for security compliance.

### **🔹 Debugging SSH Issues**
```bash
nano ~/.ssh/authorized_keys
```
- **Purpose:** Open and verify if the correct public key is stored inside EC2.

```bash
sudo systemctl restart ssh
```
- **Purpose:** Restart the SSH service after modifying permissions.

```bash
cat /var/log/auth.log | grep ssh
```
- **Purpose:** Check SSH **log files** for authentication errors.

```bash
ssh-keygen -y -f ~/Downloads/skyvault.pem
```
- **Purpose:** Extract and compare the public key from the private **.pem** file.

---

## **3️⃣ Firewall (UFW) Security Rules**
### **🔹 Checking Firewall Status**
```bash
sudo ufw status
```
- **Purpose:** Display active firewall rules.

### **🔹 Allowing Secure Connections**
```bash
sudo ufw allow 22/tcp
```
- **Purpose:** Enable **SSH access** on port 22.

```bash
sudo ufw allow 80/tcp
```
- **Purpose:** Allow **HTTP traffic** for web applications.

```bash
sudo ufw enable
```
- **Purpose:** Activate **firewall protections**.

---

## **4️⃣ File & Permission Fixes**
### **🔹 Fixing SSH Directory Permissions**
```bash
chmod 600 ~/.ssh/authorized_keys
```
- **Purpose:** Restrict access to **authorized_keys** file.

```bash
chmod 700 ~/.ssh
```
- **Purpose:** Secure the **.ssh** directory.

```bash
chown ubuntu:ubuntu ~/.ssh -R
```
- **Purpose:** Ensure the `.ssh` directory is owned by the correct user.

---

## **📝 Next Steps**
1️⃣ Finalize **SSH authentication troubleshooting** to enable direct connection.  
2️⃣ Expand **firewall security rules** for advanced protection.  
3️⃣ Add **Tor & VPN configurations** for anonymity and security testing.  
4️⃣ Document **IAM role best practices** for AWS security management.  

🚀 **This repo tracks my journey in AWS Cloud Security!** 🚀
