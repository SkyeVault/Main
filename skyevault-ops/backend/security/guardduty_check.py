import boto3
from database import save_report

gd = boto3.client('guardduty')

def list_guardduty_findings():
    """List active GuardDuty security findings and save them to database"""
    detectors = gd.list_detectors()
    
    if not detectors['DetectorIds']:
        save_report("GuardDuty", "GuardDuty is NOT enabled!")
        return ["GuardDuty is NOT enabled"]

    detector_id = detectors['DetectorIds'][0]
    findings = gd.list_findings(DetectorId=detector_id)

    if not findings['FindingIds']:
        return ["No GuardDuty security threats detected."]

    alert_list = []
    for finding_id in findings['FindingIds']:
        finding = gd.get_findings(DetectorId=detector_id, FindingIds=[finding_id])
        alert = f"{finding['Findings'][0]['Title']} (Severity: {finding['Findings'][0]['Severity']})"
        alert_list.append(alert)
        save_report("GuardDuty", alert)

    return alert_list
