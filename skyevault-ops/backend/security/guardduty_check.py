import boto3

# Initialize GuardDuty client
gd = boto3.client('guardduty')

def list_guardduty_findings():
    """List active GuardDuty security findings"""
    detectors = gd.list_detectors()
    
    if not detectors['DetectorIds']:
        print("🚨 GuardDuty is NOT enabled!")
        return

    detector_id = detectors['DetectorIds'][0]
    findings = gd.list_findings(DetectorId=detector_id)

    if not findings['FindingIds']:
        print("✅ No GuardDuty security threats detected.")
    else:
        print("\n🚨 GuardDuty Threat Alerts Found:")
        for finding_id in findings['FindingIds']:
            finding = gd.get_findings(DetectorId=detector_id, FindingIds=[finding_id])
            print(f" - {finding['Findings'][0]['Title']} (Severity: {finding['Findings'][0]['Severity']})")

if __name__ == "__main__":
    list_guardduty_findings()
