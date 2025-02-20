# SkyeVault Security Lab - AWS & Linux Command Documentation

## Overview
Welcome to the SkyeVault Security Lab! This repo is my personal documentation of setting up an AWS security lab from scratch. The goal is to gain hands-on experience with AWS security tools, IAM management, SSH authentication, and firewall rules. This is a real-world learning process, complete with troubleshooting, fixes, and improvements.

---

## **AWS CLI Commands**
### **🔹 Configuring AWS CLI**
```bash
aws configure
```
- **Why?** Sets up AWS CLI with an **Access Key and Secret Key** to interact with AWS services securely.

### **🔹 Checking AWS S3 Buckets**
```bash
aws s3 ls
```
- **Why?** This confirms that AWS CLI is working correctly by listing available S3 buckets.

### **🔹 Managing IAM Users**
```bash
aws iam list-users
```
- **Why?** Displays all IAM users, ensuring that **SkyeVaultUser** is correctly set up.

```bash
aws iam list-policies
```
- **Why?** Lists all available IAM policies to verify the right permissions are attached.

---

## **SSH & Key Authentication Commands**
### **🔹 Connecting to EC2 via SSH**
```bash
ssh -i ~/Downloads/skyvault.pem ubuntu@44.222.212.40
```
- **Why?** This is how I attempt to log into my EC2 instance securely using SSH.

### **🔹 Troubleshooting SSH Issues**
```bash
ls -l ~/Downloads/skyvault.pem
```
- **Why?** Checks whether the private key exists and has the correct file permissions.

```bash
chmod 400 ~/Downloads/skyvault.pem
```
- **Why?** AWS requires strict read-only permissions for private keys.

```bash
nano ~/.ssh/authorized_keys
```
- **Why?** Opens the file to verify if the correct public key is stored inside EC2.

```bash
sudo systemctl restart ssh
```
- **Why?** Restarts the SSH service after making changes to authentication settings.

```bash
cat /var/log/auth.log | grep ssh
```
- **Why?** Checks log files for authentication errors when troubleshooting SSH failures.

```bash
ssh-keygen -y -f ~/Downloads/skyvault.pem
```
- **Why?** Extracts the public key from the private **.pem** file to ensure they match.

---

## **Firewall (UFW) Security Rules**
### **🔹 Checking Firewall Rules**
```bash
sudo ufw status
```
- **Why?** Displays active firewall rules to confirm what's open and closed.

### **🔹 Allowing Secure Connections**
```bash
sudo ufw allow 22/tcp
```
- **Why?** Enables SSH access on port 22 so I can connect securely.

```bash
sudo ufw allow 80/tcp
```
- **Why?** Allows HTTP traffic for potential web applications later.

```bash
sudo ufw enable
```
- **Why?** Turns on the firewall to enforce security rules.

---

## **Fixing Permissions for Secure Authentication**
### **🔹 Adjusting SSH Directory Permissions**
```bash
chmod 600 ~/.ssh/authorized_keys
```
- **Why?** Ensures only the owner can modify the `authorized_keys` file.

```bash
chmod 700 ~/.ssh
```
- **Why?** Secures the `.ssh` directory from unauthorized access.

```bash
chown ubuntu:ubuntu ~/.ssh -R
```
- **Why?** Ensures the `.ssh` directory is owned by the correct user.

---

## ** What’s Next?**
🔹 **Fix the final SSH authentication issue** so I can log in directly from my Mac.  
🔹 **Expand firewall security** with stricter rules and logging.  
🔹 **Document best practices for IAM roles & policies** in AWS security.  
🔹 **Add VPN & Tor configurations** for security testing.  

**This repo is tracking my progress in AWS Cloud Security.** 
