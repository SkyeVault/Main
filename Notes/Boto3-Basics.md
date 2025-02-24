# **Getting Started with Boto3 (AWS SDK for Python)**

Boto3 is the **official AWS SDK for Python**. It allows you to interact with **AWS services** programmatically, making it essential for **cloud automation, security, and infrastructure management**.

---

## **1. Installing Boto3**
To install Boto3, run:
```sh
pip install boto3
```
Verify installation:
```sh
python -c "import boto3; print(boto3.__version__)"
```

---

## **2. Setting Up AWS Credentials**
Boto3 requires **AWS credentials** to authenticate and access services.

### **Option 1: Configure AWS CLI (Recommended)**
1. Install the AWS CLI:
   ```sh
   pip install awscli
   ```
2. Run the AWS configure command:
   ```sh
   aws configure
   ```
   Enter your **AWS Access Key**, **Secret Key**, and **default region**.
3. Credentials will be stored in `~/.aws/credentials` (Linux/macOS) or `%USERPROFILE%\.aws\credentials` (Windows).

### **Option 2: Manually Set Up Credentials**
Create the credentials file manually:
```
~/.aws/credentials  (Linux/macOS)
C:\Users\USERNAME\.aws\credentials  (Windows)
```
Add the following:
```
[default]
aws_access_key_id = YOUR_ACCESS_KEY
aws_secret_access_key = YOUR_SECRET_KEY
region = us-east-1
```

---

## **3. Connecting to AWS with Boto3**
### **Create a Boto3 Session**
```python
import boto3

session = boto3.Session()
s3_client = session.client("s3")  # Example: Connecting to S3
print(s3_client.list_buckets())
```

### **Alternative: Use Default Credentials**
```python
import boto3
s3_client = boto3.client("s3")  # Connect to S3 directly
```

---

## **4. Basic AWS Operations with Boto3**
### **S3: List Buckets**
```python
import boto3
s3 = boto3.client("s3")

response = s3.list_buckets()
for bucket in response["Buckets"]:
    print(bucket["Name"])
```

### **S3: Upload a File**
```python
s3.upload_file("local_file.txt", "my-bucket", "remote_file.txt")
```

### **EC2: List Running Instances**
```python
ec2 = boto3.client("ec2")
response = ec2.describe_instances()
for reservation in response["Reservations"]:
    for instance in reservation["Instances"]:
        print(f"Instance ID: {instance['InstanceId']} - State: {instance['State']['Name']}")
```

### **IAM: List Users**
```python
iam = boto3.client("iam")
response = iam.list_users()
for user in response["Users"]:
    print(f"Username: {user['UserName']} - Created: {user['CreateDate']}")
```

### **CloudTrail: List Trails**
```python
cloudtrail = boto3.client("cloudtrail")
response = cloudtrail.describe_trails()
for trail in response["trailList"]:
    print(f"Trail Name: {trail['Name']} - S3 Bucket: {trail['S3BucketName']}")
```

---

## **5. Error Handling in Boto3**
AWS APIs return errors, so it's best to handle them properly.
```python
import boto3
from botocore.exceptions import NoCredentialsError, PartialCredentialsError

try:
    s3 = boto3.client("s3")
    s3.list_buckets()
except NoCredentialsError:
    print("AWS credentials not found. Run 'aws configure' to set them up.")
except PartialCredentialsError:
    print("Incomplete AWS credentials. Check your AWS profile.")
except Exception as e:
    print(f"An error occurred: {e}")
```

---

## **6. Automating AWS Tasks with Boto3**
### **Example: Delete Old S3 Objects Automatically**
```python
import boto3
from datetime import datetime, timezone

s3 = boto3.client("s3")
bucket_name = "my-bucket"
days_threshold = 30

objects = s3.list_objects_v2(Bucket=bucket_name)
if "Contents" in objects:
    for obj in objects["Contents"]:
        last_modified = obj["LastModified"]
        age = (datetime.now(timezone.utc) - last_modified).days
        if age > days_threshold:
            print(f"Deleting {obj['Key']} (Last modified {age} days ago)")
            s3.delete_object(Bucket=bucket_name, Key=obj["Key"])
```

---

## **7. Best Practices for Using Boto3**
✔ **Use IAM roles** instead of hardcoded credentials.  
✔ **Handle exceptions** to avoid API failures.  
✔ **Use sessions** for better credential management.  
✔ **Optimize API calls** (e.g., batch requests instead of single calls).  
✔ **Follow AWS security best practices** (limit access permissions).  

---

## **8. Additional Resources**
- 📖 [Boto3 Documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/index.html)
- 🔗 [AWS SDK for Python (GitHub)](https://github.com/boto/boto3)
- 📚 [AWS Python Tutorials](https://aws.amazon.com/developer/language/python/)

---

## **Next Steps**
✅ **Test the basic commands** in Python.  
✅ **Try automating AWS tasks** like S3 uploads or EC2 instance management.  
✅ **Explore more AWS services** like Lambda, SNS, and DynamoDB with Boto3.  

🚀 **Master Boto3 and automate your AWS workflow!**

