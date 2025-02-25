import boto3

# Create IAM client
iam = boto3.client("iam")

# Get list of IAM users
response = iam.list_users()

# Print user names
print("IAM Users in AWS Account:")
for user in response['Users']:
    print(user['UserName'])

