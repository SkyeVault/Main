# AWS Certified Security – Specialty (SCS-C02) Practice Questions

This document contains **practice questions** covering key topics from the AWS Security Specialty exam. These questions will help reinforce your understanding of **IAM, encryption, logging, incident response, networking, and compliance**.

---

## **1. Identity and Access Management (IAM)**
### **1.1 IAM Users, Groups, and Roles**
1. What is the difference between an IAM role and an IAM user?
2. What is the purpose of IAM permission boundaries?
3. How can you enforce multi-factor authentication (MFA) for IAM users?
4. What is the benefit of using IAM Access Analyzer?
5. How do IAM policies evaluate **explicit deny, explicit allow, and implicit deny**?

### **1.2 AWS Organizations and SCPs**
6. What is the primary function of a Service Control Policy (SCP)?
7. Can SCPs grant permissions? Why or why not?
8. How do you restrict an AWS account from launching EC2 instances in a specific region?
9. What happens if an SCP blocks an action that an IAM policy allows?
10. How can you enforce **IAM role session duration limits**?

### **1.3 Cross-Account Access**
11. How do IAM roles enable cross-account access in AWS?
12. What is the difference between **resource-based policies** and **identity-based policies**?
13. How does AWS STS (Security Token Service) improve security?
14. What is the benefit of an **external ID** when using IAM roles with third-party applications?
15. How do you restrict **assume role** actions for specific AWS accounts?

---

## **2. Encryption & Data Protection**
### **2.1 AWS KMS (Key Management Service)**
16. What is the difference between a **Customer Managed Key (CMK)** and an **AWS Managed Key**?
17. How do you **restrict KMS key access** using policies?
18. What is the impact of enabling **automatic key rotation** for a CMK?
19. How can you securely share an encrypted S3 object with another AWS account?
20. How do **KMS grants** work, and why would you use them?

### **2.2 S3 Encryption & Data Protection**
21. What are the four S3 encryption options?
22. What is the difference between **SSE-S3**, **SSE-KMS**, **SSE-C**, and **Client-Side Encryption**?
23. How do you enforce S3 encryption using a **Bucket Policy**?
24. How does **Amazon Macie** help with data classification and protection?
25. What is **S3 Object Lock**, and how does it help with compliance?

### **2.3 AWS Secrets Manager**
26. What is the benefit of using **AWS Secrets Manager** over storing credentials in environment variables?
27. How do you **automatically rotate** RDS database credentials using Secrets Manager?
28. How does Secrets Manager encrypt secrets at rest?
29. What is the difference between **Secrets Manager** and **SSM Parameter Store**?
30. How do you retrieve a secret from Secrets Manager using the AWS CLI?

---

## **3. Logging & Monitoring**
### **3.1 AWS CloudTrail**
31. What are the different **types of CloudTrail events**?
32. How do you enforce **CloudTrail logging across all AWS regions**?
33. How do you secure **CloudTrail logs** in S3 to prevent tampering?
34. What AWS services integrate with CloudTrail for security monitoring?
35. How can you monitor CloudTrail logs for specific API calls?

### **3.2 AWS GuardDuty**
36. What types of threats does **AWS GuardDuty** detect?
37. How do you configure GuardDuty to **monitor multiple AWS accounts**?
38. What is the difference between **GuardDuty findings** classified as **Reconnaissance, Credential Access, and Privilege Escalation**?
39. How do you **automate GuardDuty threat response**?
40. What AWS service can **aggregate GuardDuty alerts across multiple regions**?

### **3.3 AWS Security Hub**
41. What is AWS Security Hub, and how does it integrate with GuardDuty and AWS Config?
42. How do you **prioritize security findings** in AWS Security Hub?
43. What compliance frameworks does Security Hub support?
44. How do you configure **automated remediation actions** for Security Hub findings?
45. What AWS service provides **automated security posture assessments**?

---

## **4. Incident Response**
46. What are the **six phases** of AWS’s **Incident Response Lifecycle**?
47. How do you use **AWS Lambda** for automated security response?
48. What is the best way to **contain a compromised EC2 instance**?
49. How can you **isolate a compromised IAM user**?
50. How do you detect and respond to **suspicious AWS API activity**?

---

## **5. Networking & Firewall Security**
### **5.1 VPC Security**
51. What is the difference between **Security Groups and Network ACLs**?
52. How do you enforce VPC **flow logs** to monitor network activity?
53. What is **AWS PrivateLink**, and how does it improve security?
54. How do you prevent **publicly accessible EC2 instances**?
55. How do you restrict outbound internet access from a VPC?

### **5.2 AWS WAF & Shield**
56. What are **rate-based rules** in AWS WAF?
57. How does **AWS Shield Advanced** provide DDoS protection?
58. What AWS services can integrate with AWS WAF?
59. How do **managed rules** in AWS WAF improve security?
60. What AWS service provides **DDoS cost protection**?

---

## **6. Compliance & Governance**
61. What is the **AWS Shared Responsibility Model**?
62. What AWS service can detect **compliance violations** in real-time?
63. What is the difference between **AWS Config and AWS Audit Manager**?
64. How do you enforce compliance using **AWS Organizations SCPs**?
65. What is the **difference between SOC 2 and ISO 27001 compliance**?

---

# **Final Exam Tips**
- **Focus on IAM, encryption, logging, and networking security.**
- **Understand real-world use cases for GuardDuty, CloudTrail, and AWS Config.**
- **Practice using AWS Security Hub and AWS WAF to mitigate threats.**
- **Read the AWS Security Best Practices whitepapers.**
- **Take multiple practice exams to get comfortable with the format.**

---

This practice question bank covers **all key topics** for the AWS Security Specialty exam. **Review these questions regularly** and test your knowledge using real-world AWS scenarios!
