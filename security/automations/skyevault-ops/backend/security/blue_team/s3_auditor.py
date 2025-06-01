import boto3
import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from database import save_report

s3 = boto3.client('s3')

def check_s3_security():
    """Check S3 security settings and save findings to database"""
    buckets = s3.list_buckets()
    insecure_buckets = []

    for bucket in buckets['Buckets']:
        bucket_name = bucket['Name']
        try:
            acl = s3.get_public_access_block(Bucket=bucket_name)
            if not acl['PublicAccessBlockConfiguration']['BlockPublicAcls']:
                finding = f"Bucket {bucket_name} is public"
                print(finding)  # 🔹 Debugging print statement
                insecure_buckets.append(finding)
                save_report("S3", finding)  # Ensure save_report is actually being called
        except Exception as e:
            error_message = f"Error checking {bucket_name}: {str(e)}"
            print(error_message)  # 🔹 Print errors
            save_report("S3", error_message)

    return insecure_buckets

if __name__ == "__main__":
    print("🔍 Running S3 Security Check...")
    issues = check_s3_security()
    
    if issues:
        print("\n🚨 Insecure S3 Buckets Found:")
        for issue in issues:
            print(f" - {issue}")
    else:
        print("\n✅ All S3 buckets are secure!")
