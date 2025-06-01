import os
import boto3

def get_public_ips():
    """Retrieve public IPs of running EC2 instances."""
    ec2_client = boto3.client("ec2")
    instances = ec2_client.describe_instances()
    
    public_ips = []
    for reservation in instances["Reservations"]:
        for instance in reservation["Instances"]:
            if "PublicIpAddress" in instance:
                public_ips.append(instance["PublicIpAddress"])
    
    return public_ips

def run_nmap_scan(ip):
    """Run an nmap scan on the given IP."""
    print(f"\n🔍 Scanning {ip} for open ports...")
    os.system(f"nmap -sV {ip} -oN scan_results_{ip}.txt")

def main():
    print("\n🚀 Running Network Scanning on EC2 Instances...")
    ips = get_public_ips()
    
    if not ips:
        print("⚠️ No public EC2 instances found.")
    else:
        for ip in ips:
            run_nmap_scan(ip)

if __name__ == "__main__":
    main()
