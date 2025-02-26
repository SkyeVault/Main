import boto3
import sys
import os
from datetime import datetime, timezone

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from database import save_report

cloudtrail = boto3.client('cloudtrail')

# Define security-sensitive events
SECURITY_EVENTS = [
    "ConsoleLogin",
    "GenerateDataKey",
    "ListAccessKeys",
    "ListUserPolicies",
    "DetachPolicy",
    "AttachUserPolicy",
    "DeleteUser",
    "DeleteBucket",
    "StopLogging"
]

def check_cloudtrail_security():
    """Check CloudTrail logs for security-related events."""
    try:
        response = cloudtrail.lookup_events(MaxResults=10)

        print("\n🔍 Retrieved CloudTrail Events (Raw Data):")
        print(response)  # Debugging step: print full response

        if "Events" not in response or not response["Events"]:
            print("❌ No events retrieved. Check AWS CloudTrail settings.")
            return []

        security_findings = []

        for event in response["Events"]:
            event_name = event["EventName"]
            event_time = event["EventTime"]
            user = event.get("Username", "Unknown User")

            # Debugging printout for each event
            print(f"\nEvent Found: {event_name} by {user} at {event_time}")

            # If event is in our list of security risks, save it
            if event_name in SECURITY_EVENTS:
                finding = f"🚨 Security Alert: {event_name} by {user} at {event_time}"
                print(finding)  # Print what should be saved
                security_findings.append(finding)
                save_report("CloudTrail", finding)

        return security_findings

    except Exception as e:
        print(f"⚠️ Error retrieving CloudTrail logs: {e}")
        return []

if __name__ == "__main__":
    print("🔍 Running CloudTrail Security Check...")
    findings = check_cloudtrail_security()

    if findings:
        print("\n🚨 Security Alerts from CloudTrail:")
        for alert in findings:
            print(f" - {alert}")
    else:
        print("\n✅ No suspicious CloudTrail activity detected!")
