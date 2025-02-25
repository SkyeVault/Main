import boto3
from datetime import datetime, timedelta

# Connect to IAM
iam = boto3.client("iam")

# Define cutoff (90 days ago)
cutoff_date = datetime.utcnow() - timedelta(days=90)

# Get list of IAM users
response = iam.list_users()

# Print header
print("🔍 Checking for inactive IAM users...\n")

# Track inactive users
inactive_users = []

for user in response['Users']:
    username = user['UserName']

    # Some users have never logged in
    if 'PasswordLastUsed' not in user:
        print(f"⚠️ {username} - NEVER LOGGED IN")
        inactive_users.append(username)
        continue
    
    # Convert login time to a comparable format
    last_used = user['PasswordLastUsed'].replace(tzinfo=None)

    # Check if user is inactive
    if last_used < cutoff_date:
        print(f"⚠️ {username} - Last login: {last_used}")
        inactive_users.append(username)

# Summary
print("\n🚨 Inactive IAM Users Found:", len(inactive_users))
if inactive_users:
    print("Consider disabling these accounts for security reasons.")

