import boto3

def list_ec2_instances():
    """List EC2 instances and their public IPs."""
    ec2_client = boto3.client("ec2")
    instances = ec2_client.describe_instances()

    print("\n🔍 EC2 Instances Found:")
    for reservation in instances["Reservations"]:
        for instance in reservation["Instances"]:
            instance_id = instance["InstanceId"]
            public_ip = instance.get("PublicIpAddress", "No Public IP")
            print(f"  - Instance: {instance_id} | Public IP: {public_ip}")

def list_s3_buckets():
    """List all available S3 buckets."""
    s3_client = boto3.client("s3")
    buckets = s3_client.list_buckets()

    print("\n📂 S3 Buckets Found:")
    for bucket in buckets["Buckets"]:
        print(f"  - {bucket['Name']}")

def list_iam_users():
    """List IAM users."""
    iam_client = boto3.client("iam")
    users = iam_client.list_users()

    print("\n👤 IAM Users Found:")
    for user in users["Users"]:
        print(f"  - {user['UserName']} | Created: {user['CreateDate']}")

def main():
    print("\n🚀 Running AWS Reconnaissance...")
    list_ec2_instances()
    list_s3_buckets()
    list_iam_users()

if __name__ == "__main__":
    main()
