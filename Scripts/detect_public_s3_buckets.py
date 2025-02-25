import boto3

# Connect to S3 and SNS
s3 = boto3.client('s3')
sns = boto3.client('sns')

# Your SNS Topic ARN (Replace with your actual ARN)
SNS_TOPIC_ARN = "arn:aws:sns:us-east-1:820242919187:PublicS3Alert"

# Get list of all S3 buckets
buckets = s3.list_buckets()

# Print header
print("🔍 Checking for public S3 buckets...\n")

# Track public buckets
public_buckets = []

# Check each bucket's permissions
for bucket in buckets['Buckets']:
    bucket_name = bucket['Name']
    
    # Get bucket ACL
    try:
        acl = s3.get_bucket_acl(Bucket=bucket_name)
        
        # Check each grant to see if public access is allowed
        for grant in acl['Grants']:
            grantee = grant.get('Grantee', {})
            
            if 'URI' in grantee and 'AllUsers' in grantee['URI']:
                print(f"🚨 PUBLIC BUCKET FOUND: {bucket_name}")
                public_buckets.append(bucket_name)
    
    except Exception as e:
        print(f"❌ Could not check {bucket_name}: {e}")

# Summary
print("\n🚨 Public S3 Buckets Found:", len(public_buckets))
if public_buckets:
    print("⚠️ Consider restricting access to these buckets.\n")

    # Send an SNS alert
    alert_message = f"🚨 ALERT: {len(public_buckets)} public S3 buckets detected:\n" + "\n".join(public_buckets)
    
    try:
        response = sns.publish(
            TopicArn=SNS_TOPIC_ARN,
            Message=alert_message,
            Subject="AWS Security Alert: Public S3 Buckets Found"
        )
        print("📩 SNS Alert Sent!")
    except Exception as e:
        print(f"❌ Failed to send SNS alert: {e}")

# Automatically block public access
for bucket_name in public_buckets:
    try:
        # First, check if public access is already blocked
        block_settings = s3.get_public_access_block(Bucket=bucket_name)
        config = block_settings.get('PublicAccessBlockConfiguration', {})

        if config.get('BlockPublicAcls') and config.get('BlockPublicPolicy'):
            print(f"✅ {bucket_name} is already private.")
        else:
            print(f"🔒 Blocking public access for {bucket_name}...")
            s3.put_public_access_block(
                Bucket=bucket_name,
                PublicAccessBlockConfiguration={
                    'BlockPublicAcls': True,
                    'IgnorePublicAcls': True,
                    'BlockPublicPolicy': True,
                    'RestrictPublicBuckets': True
                }
            )
            print(f"✅ {bucket_name} is now private.")

    except Exception as e:
        print(f"❌ Could not update {bucket_name}: {e}")

