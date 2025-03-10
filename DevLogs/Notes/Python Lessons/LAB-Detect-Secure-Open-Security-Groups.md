# **AWS Security Lab: Detect & Secure Open Security Groups**

## **📌 Overview**
This lab covers how to detect, analyze, and secure AWS **EC2 security groups** that allow public access (`0.0.0.0/0`).

---

## **🔍 Step 1: Detect Open Security Groups**
### **1️⃣ Create the Python Script**
Create a new file in your **scripts/boto3/security/** directory:
```bash
nano scripts/boto3/security/detect_open_security_groups.py
```

Paste the following code:
```python
import boto3

# Connect to EC2
ec2 = boto3.client("ec2")

# Get all security groups
response = ec2.describe_security_groups()

print("🔍 Checking for open security groups...\n")

# Track open security groups
open_sg_list = []

for sg in response['SecurityGroups']:
    sg_id = sg['GroupId']
    sg_name = sg.get('GroupName', 'Unknown')

    for rule in sg['IpPermissions']:
        for ip_range in rule.get('IpRanges', []):
            if ip_range.get('CidrIp') == "0.0.0.0/0":
                print(f"🚨 Security Group {sg_name} ({sg_id}) allows open access!")
                open_sg_list.append(f"{sg_name} ({sg_id})")

# Summary
if open_sg_list:
    print("\n🚨 Open Security Groups Found:", len(open_sg_list))
    print("⚠️ Consider restricting access to these security groups.")
else:
    print("✅ No open security groups found.")
```

### **2️⃣ Run the Script**
```bash
python3 scripts/boto3/security/detect_open_security_groups.py
```
✅ If public security groups exist, they will be listed.
✅ If no open groups exist, you will see `✅ No open security groups found.`

---

## **🔐 Step 2: Secure Open Security Groups**
### **1️⃣ Check Current Security Group Rules**
```bash
aws ec2 describe-security-groups --group-ids sg-XXXXXXXXXXXXX --query "SecurityGroups[*].IpPermissions"
```
🔹 Replace `sg-XXXXXXXXXXXXX` with your actual **Security Group ID**.
🔹 Look for **`"CidrIp": "0.0.0.0/0"`**, which indicates **public access**.

### **2️⃣ Remove Public Access**
Run this command to revoke unrestricted access:
```bash
aws ec2 revoke-security-group-ingress --group-id sg-XXXXXXXXXXXXX --protocol all --port -1 --cidr 0.0.0.0/0
```

#### **(Optional) Restrict to Specific IP**
If you need access, allow **only your IP**:
```bash
aws ec2 authorize-security-group-ingress --group-id sg-XXXXXXXXXXXXX --protocol tcp --port 22 --cidr YOUR_IP/32
```
🔹 Replace `YOUR_IP/32` with your **actual IP address**.

---

## **📌 Step 3: Verify That Security Group is Fixed**
Run your script again:
```bash
python3 scripts/boto3/security/detect_open_security_groups.py
```
✅ If you now see:
```
✅ No open security groups found.
```
🎉 **Success! Your security group is now locked down.**

---

## **🚀 Step 4: Push Your Updates to GitHub**
### **1️⃣ Stage the Updated Script**
```bash
git add scripts/boto3/security/detect_open_security_groups.py
```
### **2️⃣ Commit the Changes**
```bash
git commit -m "Added security group detection script"
```
### **3️⃣ Push to GitHub**
```bash
git push origin main
```
✅ Your latest security script is now **version-controlled** in GitHub.

---

## **📌 Next Steps**
- ✅ **Automate this script in AWS Lambda** to run every day.
- ✅ **Send an SNS alert** when open security groups are found.
- ✅ **Expand it** to check other security misconfigurations.

🚀 **You now have a fully functional AWS security script!** 🎉

