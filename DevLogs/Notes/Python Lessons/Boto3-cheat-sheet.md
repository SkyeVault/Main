# Boto3 Cheat Sheet

## What is Boto3?
Boto3 is the AWS SDK for Python that allows developers to interact with AWS services programmatically. It provides an interface to services such as S3, EC2, IAM, DynamoDB, and more.

## Installation
```bash
pip install boto3
```

## Configuration
Set up AWS credentials using the AWS CLI:
```bash
aws configure
```
Or manually create `~/.aws/credentials`:
```
[default]
aws_access_key_id=YOUR_ACCESS_KEY
aws_secret_access_key=YOUR_SECRET_KEY
region=us-east-1
```

## Initialize Boto3 Client and Resource
### Using a Client
```python
import boto3
s3_client = boto3.client('s3')
```
### Using a Resource
```python
import boto3
s3_resource = boto3.resource('s3')
```

## Common Boto3 Services and Examples

### 1. Amazon S3 (Simple Storage Service)
#### List All Buckets
```python
for bucket in s3_client.list_buckets()['Buckets']:
    print(bucket['Name'])
```
#### Upload a File
```python
s3_client.upload_file('local_file.txt', 'my-bucket', 's3_object_name')
```
#### Download a File
```python
s3_client.download_file('my-bucket', 's3_object_name', 'local_file.txt')
```

### 2. EC2 (Elastic Compute Cloud)
#### List Running Instances
```python
ec2_client = boto3.client('ec2')
instances = ec2_client.describe_instances()
for reservation in instances['Reservations']:
    for instance in reservation['Instances']:
        print(instance['InstanceId'], instance['State']['Name'])
```
#### Start an Instance
```python
ec2_client.start_instances(InstanceIds=['i-1234567890abcdef0'])
```
#### Stop an Instance
```python
ec2_client.stop_instances(InstanceIds=['i-1234567890abcdef0'])
```

### 3. IAM (Identity and Access Management)
#### List Users
```python
iam_client = boto3.client('iam')
for user in iam_client.list_users()['Users']:
    print(user['UserName'])
```
#### Create a New User
```python
iam_client.create_user(UserName='new-user')
```

### 4. DynamoDB
#### List Tables
```python
dynamodb_client = boto3.client('dynamodb')
print(dynamodb_client.list_tables())
```
#### Get an Item
```python
dynamodb = boto3.resource('dynamodb')
table = dynamodb.Table('my-table')
response = table.get_item(Key={'id': '123'})
print(response['Item'])
```

## Quick Guide: Using Boto3 in an Application

1. **Install and configure AWS CLI**
   ```bash
   aws configure
   ```
2. **Install Boto3**
   ```bash
   pip install boto3
   ```
3. **Set up IAM roles and permissions** (if using EC2, attach the necessary permissions)
4. **Use Boto3 clients/resources in your Python script**
5. **Run and deploy your script**
   ```bash
   python my_script.py
   ```

## Additional Tips
- Use `boto3.session.Session()` to manage multiple AWS profiles.
- Use `try-except` blocks to handle errors gracefully.
- Use pagination for listing large sets of data.

### Example of Pagination:
```python
s3_paginator = s3_client.get_paginator('list_objects_v2')
for page in s3_paginator.paginate(Bucket='my-bucket'):
    for obj in page.get('Contents', []):
        print(obj['Key'])
