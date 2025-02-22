# AWS CloudTrail and GuardDuty Lab

This lab will guide you through the steps of configuring AWS CloudTrail and GuardDuty to enhance your AWS account's security. CloudTrail logs account activity, while GuardDuty provides continuous threat detection.

---

## Lab Objectives

- Enable and configure CloudTrail across all regions.
- Secure CloudTrail log files in an S3 bucket.
- Enable GuardDuty and review its security findings.
- Verify that both services are functioning correctly.

---

## Prerequisites

- An AWS account with sufficient permissions (e.g., an IAM user with administrative rights).
- Basic familiarity with the AWS Management Console.
- (Optional) AWS CLI installed and configured for command-line verification.

---

## Part 1: Configuring CloudTrail

### Step 1: Create a CloudTrail Trail

1. **Sign in to AWS Console**  
   Log in to your AWS account and navigate to the **CloudTrail** service.

2. **Create a New Trail**  
   - In the CloudTrail dashboard, select **Trails** in the left-hand menu.
   - Click **Create trail**.
   - Enter a trail name (e.g., `MultiRegionTrail`).

3. **Apply Trail to All Regions**  
   - Choose **Yes** for "Apply trail to all regions" to capture activity from every region.

4. **Set Up Storage Location**  
   - Create a new S3 bucket (e.g., `my-cloudtrail-logs-<accountID>`) or select an existing one.
   - Enable log file validation to ensure your log files are not tampered with.

5. **Complete the Trail Creation**  
   - Review the settings and click **Create trail**.

### Step 2: Verify CloudTrail Setup

1. **Generate Activity**  
   - Perform some actions in your AWS account (for example, launch or stop an EC2 instance).

2. **Check the S3 Bucket**  
   - After a few minutes, navigate to the S3 bucket specified during setup.
   - Verify that new log files have been added and that log file validation is active.

---

## Part 2: Configuring GuardDuty

### Step 1: Enable GuardDuty

1. **Navigate to GuardDuty**  
   - In the AWS Console, go to the **GuardDuty** service.

2. **Start GuardDuty**  
   - Click **Get Started** (if this is your first time) or **Enable GuardDuty**.
   - Follow the prompts to enable GuardDuty for your account.
   - For accounts in multiple regions, ensure GuardDuty is enabled in each region or use AWS Organizations for centralized management.

### Step 2: Review GuardDuty Findings

1. **Wait for Analysis**  
   - Allow a few minutes for GuardDuty to begin analyzing your account activity.

2. **View Findings**  
   - Navigate to the **Findings** section in the GuardDuty dashboard.
   - Review any alerts or findings. In a clean environment, you might not see any findings immediately, which is normal.

---

## Part 3: Lab Verification and Wrap-up

- **CloudTrail Verification:**  
  Check that log files are being created in your designated S3 bucket and that they include validation information.

- **GuardDuty Verification:**  
  Confirm that GuardDuty is active by reviewing its dashboard. Even without findings, the service should show that it is monitoring your environment.

- **Next Steps:**  
  Consider exploring further integrations, such as sending CloudTrail logs to CloudWatch Logs for real-time alerts or setting up automated responses using AWS Lambda.

---

## Troubleshooting Tips

- **No CloudTrail Logs?**  
  Ensure that the trail is configured for all regions and that the correct S3 bucket is specified.

- **No GuardDuty Findings?**  
  A lack of findings may simply mean no threats were detected. You can simulate traffic or review configuration settings if needed.

---

## Conclusion

By completing this lab, you've gained hands-on experience in setting up CloudTrail and GuardDuty. These tools are vital for monitoring AWS activity and detecting potential security issues, forming a key part of your AWS security strategy.
