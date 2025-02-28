import boto3
from datetime import datetime, timezone, timedelta
from database import save_report  # Import database functions

# Initialize AWS IAM client
iam = boto3.client('iam')

def list_users_without_mfa():
    """Check IAM users who do not have MFA enabled and save to database"""
    users = iam.list_users()
    users_without_mfa = []

    for user in users['Users']:
        user_name = user['UserName']
        mfa_devices = iam.list_mfa_devices(UserName=user_name)

        if not mfa_devices['MFADevices']:
            users_without_mfa.append(user_name)
            save_report("IAM", f"User {user_name} has no MFA enabled")

    return users_without_mfa

def list_inactive_users(days=90):
    """Find IAM users who haven't logged in for a set number of days and save to database"""
    users = iam.list_users()
    inactive_users = []
    threshold_date = datetime.now(timezone.utc) - timedelta(days=days)

    for user in users['Users']:
        if 'PasswordLastUsed' in user:
            last_used = user['PasswordLastUsed']
            if last_used < threshold_date:
                inactive_users.append(user['UserName'])
                save_report("IAM", f"User {user['UserName']} is inactive (last login {last_used})")

    return inactive_users

if __name__ == "__main__":
    print("🔍 Running IAM Security Check...")

    no_mfa_users = list_users_without_mfa()
    inactive_users = list_inactive_users()

    print("\n🚨 Users without MFA enabled:")
    for user in no_mfa_users:
        print(f" - {user}")

    print("\n⚠️ Inactive users (no login in 90+ days):")
    for user in inactive_users:
        print(f" - {user}")

    print("\n✅ IAM Security Check Complete!")
