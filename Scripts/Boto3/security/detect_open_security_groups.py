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
