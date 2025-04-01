# Command-Line Prompts Guide

This document provides a reference for the command-line prompts used in various AWS, GitHub, and GitLab projects.

## Git and GitHub/GitLab Commands

### 1. **Initialize a Git Repository**
```bash
git init
```
- Initializes a new Git repository in the current directory.

### 2. **Clone a Repository**
```bash
git clone <repository_url>
```
- Creates a local copy of a remote repository.

### 3. **Check Git Status**
```bash
git status
```
- Displays changes in the working directory.

### 4. **Add Files to Staging**
```bash
git add <file_or_directory>
```
- Stages a file or directory for commit.

### 5. **Commit Changes**
```bash
git commit -m "Commit message"
```
- Saves changes with a descriptive message.

### 6. **Push Changes to Remote Repository**
```bash
git push origin <branch_name>
```
- Uploads committed changes to a remote repository.

### 7. **Pull Latest Changes**
```bash
git pull origin <branch_name>
```
- Fetches and integrates updates from the remote repository.

### 8. **Create and Switch to a New Branch**
```bash
git checkout -b <new_branch_name>
```
- Creates and switches to a new branch.

### 9. **Merge a Branch**
```bash
git merge <branch_name>
```
- Merges a specified branch into the current branch.

## AWS CLI Commands

### 10. **Configure AWS CLI**
```bash
aws configure
```
- Sets up AWS credentials and default settings.

### 11. **List S3 Buckets**
```bash
aws s3 ls
```
- Displays all available S3 buckets.

### 12. **Create an S3 Bucket**
```bash
aws s3 mb s3://<bucket_name>
```
- Creates a new S3 bucket.

### 13. **Upload a File to S3**
```bash
aws s3 cp <local_file> s3://<bucket_name>/
```
- Uploads a file to an S3 bucket.

### 14. **Download a File from S3**
```bash
aws s3 cp s3://<bucket_name>/<file> <local_path>
```
- Downloads a file from an S3 bucket.

### 15. **List IAM Users**
```bash
aws iam list-users
```
- Displays all IAM users in the AWS account.

### 16. **Check EC2 Instances**
```bash
aws ec2 describe-instances
```
- Lists EC2 instances and their statuses.

## Linux Commands for AWS and Security

### 17. **Update Packages (Ubuntu/Debian)**
```bash
sudo apt update && sudo apt upgrade -y
```
- Updates and upgrades system packages.

### 18. **Check Open Ports**
```bash
sudo netstat -tulnp
```
- Lists active network connections and open ports.

### 19. **Enable UFW Firewall and Allow SSH**
```bash
sudo ufw enable
sudo ufw allow 22/tcp
```
- Activates firewall and allows SSH access.

### 20. **Install Required Packages (Ubuntu)**
```bash
sudo apt install <package_name>
```
- Installs a software package.

## AWS EC2 & Remote Desktop Commands

### 21. **Connect to an EC2 Instance via SSH**
```bash
ssh -i <keyfile.pem> ubuntu@<ec2-public-ip>
```
- Establishes an SSH connection to an AWS EC2 instance.

### 22. **Install a GUI on EC2 (Ubuntu)**
```bash
sudo apt install xfce4 xfce4-goodies -y
```
- Installs XFCE desktop environment.

### 23. **Set Up a Remote Desktop on EC2**
```bash
sudo apt install xrdp -y
sudo systemctl enable xrdp
sudo systemctl start xrdp
```
- Installs and enables a remote desktop server.

## Python & Boto3 Commands

### 24. **Install Boto3 for AWS**
```bash
pip install boto3
```
- Installs the AWS SDK for Python.

### 25. **List S3 Buckets using Python**
```python
import boto3

s3 = boto3.client('s3')
buckets = s3.list_buckets()

for bucket in buckets['Buckets']:
    print(bucket['Name'])
```
- Lists all S3 buckets using Boto3.

## Notes
- Replace `<repository_url>`, `<bucket_name>`, `<file>`, `<branch_name>`, `<package_name>`, and `<ec2-public-ip>` with actual values.
- Use these commands to streamline AWS, Git, and Linux operations.