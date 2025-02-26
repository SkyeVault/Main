import boto3
from database import save_report

ct = boto3.client('cloudtrail')

def check_cloudtrail_logs():
    """Verify if CloudTrail logging is enabled and save findings to database"""
    trails = ct.describe_trails()
    
    if not trails['trailList']:
        save_report("CloudTrail", "CloudTrail is NOT enabled!")
        return ["CloudTrail is NOT enabled"]

    active_trails = []
    for trail in trails['trailList']:
        log_info = f"{trail['Name']} (S3 Bucket: {trail['S3BucketName']})"
        active_trails.append(log_info)
        save_report("CloudTrail", log_info)

    return active_trails
