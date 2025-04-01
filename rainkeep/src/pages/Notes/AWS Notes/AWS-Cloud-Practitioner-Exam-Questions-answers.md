# AWS Certified Cloud Practitioner (CLF-C01) Practice Questions

This document contains **practice questions** covering the key topics for the **AWS Cloud Practitioner certification (CLF-C01)**. These questions will help reinforce your understanding of **AWS global infrastructure, pricing, billing, security, networking, and compute services**.

---

## **1. AWS Global Infrastructure**
### **1.1 Key Concepts**
1. What are the main components of the AWS Global Infrastructure?
2. How do **Regions** differ from **Availability Zones (AZs)**?
3. What is the purpose of **Edge Locations** in AWS?
4. Which AWS services are **Global** (not tied to a single region)?
5. What factors should you consider when selecting an AWS region?

---

## **2. AWS Compute Services**
### **2.1 Amazon EC2**
6. What is the difference between **EC2 On-Demand, Reserved Instances, and Spot Instances**?
7. What are **Dedicated Hosts**, and when would you use them?
8. How does **Auto Scaling** help improve availability and cost efficiency?
9. What AWS service allows you to run **serverless applications**?
10. How does **Elastic Load Balancing (ELB)** improve application performance?

### **2.2 AWS Lambda**
11. What is AWS Lambda, and how does it differ from EC2?
12. What triggers AWS Lambda functions?
13. How does AWS Lambda pricing work?
14. What AWS service is commonly used to invoke Lambda functions asynchronously?
15. What is the maximum execution time for an AWS Lambda function?

---

## **3. AWS Storage Services**
### **3.1 Amazon S3**
16. What are the four S3 storage classes?
17. How does **S3 Glacier** help optimize storage costs?
18. What is the purpose of **S3 Lifecycle Policies**?
19. How does AWS ensure **high availability** of S3 objects?
20. What is the difference between **S3 Standard** and **S3 Intelligent-Tiering**?

### **3.2 Amazon EBS & EFS**
21. What is the difference between **Amazon EBS (Elastic Block Store)** and **Amazon EFS (Elastic File System)**?
22. Which AWS storage service is best suited for **high-performance databases**?
23. How does AWS ensure **EBS durability**?
24. What is the main advantage of using **EFS** over EBS?
25. Can an **EBS volume be attached to multiple EC2 instances**?

---

## **4. AWS Pricing & Billing**
### **4.1 AWS Pricing Models**
26. What are the four main AWS pricing models?
27. What is the difference between **On-Demand and Reserved Instances**?
28. How do **Savings Plans** help reduce AWS costs?
29. How does AWS **charge for data transfer** between regions?
30. What AWS service helps estimate monthly cloud costs before deployment?

### **4.2 AWS Billing & Cost Management**
31. What is the AWS Free Tier, and how long does it last?
32. What is the purpose of **AWS Budgets**?
33. What AWS tool provides recommendations to help reduce cloud costs?
34. How does **AWS Cost Explorer** help businesses monitor expenses?
35. What AWS tool helps forecast future cloud spending?

---

## **5. AWS Security & Compliance**
### **5.1 IAM (Identity & Access Management)**
36. What are the main components of **AWS IAM**?
37. What is the difference between an **IAM user, group, and role**?
38. What is **Multi-Factor Authentication (MFA)**, and why is it important?
39. What AWS tool helps analyze IAM permissions and detect overprivileged access?
40. How do IAM **permission boundaries** work?

### **5.2 AWS Compliance & Shared Responsibility Model**
41. What is the **AWS Shared Responsibility Model**?
42. What security responsibilities belong to **AWS** and which belong to **customers**?
43. How does AWS **protect physical security** of its data centers?
44. What AWS service helps check for security vulnerabilities in EC2 instances?
45. What AWS service provides **automated security compliance checks**?

---

## **6. AWS Networking & Content Delivery**
### **6.1 Amazon VPC**
46. What is the **Amazon Virtual Private Cloud (VPC)**, and why is it important?
47. What is the difference between **Security Groups and Network ACLs**?
48. How can you create a **private subnet** in a VPC?
49. What is the difference between a **VPN and Direct Connect**?
50. How does AWS **Route 53** help with DNS management?

### **6.2 AWS CloudFront & Content Delivery**
51. What is the purpose of **Amazon CloudFront**?
52. How does CloudFront improve website performance?
53. What AWS service provides **DDoS protection**?
54. How does **AWS WAF** protect web applications?
55. What AWS service helps accelerate content delivery across the globe?

---

## **7. AWS Databases**
### **7.1 Amazon RDS & DynamoDB**
56. What is the difference between **Amazon RDS and DynamoDB**?
57. What is the purpose of **Multi-AZ deployments in RDS**?
58. How does **Amazon Aurora** differ from standard RDS?
59. What AWS database service is **fully serverless**?
60. How does DynamoDB provide **high scalability**?

---

## **8. AWS Support Plans**
### **8.1 AWS Support Tiers**
61. What are the four AWS Support plans?
62. What AWS Support plan provides a **Technical Account Manager (TAM)**?
63. How much does the **AWS Basic Support Plan** cost?
64. What is the maximum response time for AWS **Enterprise Support**?
65. What AWS tool provides **automated Trusted Advisor checks**?

---

## **9. AWS Well-Architected Framework**
### **9.1 Well-Architected Pillars**
66. What are the **five pillars** of the AWS Well-Architected Framework?
67. What is the **Security Pillar**, and what does it focus on?
68. How does the **Reliability Pillar** improve system availability?
69. What AWS service helps review workloads based on Well-Architected principles?
70. What is the difference between the **Performance Efficiency and Cost Optimization Pillars**?

---

# **Final Exam Tips**
- **Focus on AWS Free Tier Limits**: Know what is always free vs. 12-month free.
- **Understand the Shared Responsibility Model**: AWS vs. customer responsibilities.
- **Learn AWS Pricing & Cost Optimization**: On-Demand vs. Reserved Instances vs. Savings Plans.
- **Review AWS Global Infrastructure**: Regions, AZs, Edge Locations.
- **Take practice exams**: Familiarize yourself with AWS multiple-choice question styles.

---
# Answers

# AWS Certified Cloud Practitioner (CLF-C01) Practice Questions & Answers

This document contains **practice questions** covering the key topics for the **AWS Cloud Practitioner certification (CLF-C01)**. Each question is followed by its corresponding answer.

---

## **1. AWS Global Infrastructure**
### **1.1 Key Concepts**
1. **What are the main components of the AWS Global Infrastructure?**  
   - AWS Regions  
   - Availability Zones (AZs)  
   - Edge Locations  
   - Local Zones  

2. **How do Regions differ from Availability Zones (AZs)?**  
   - **Regions** are geographic areas with multiple AZs.  
   - **Availability Zones** are **isolated** data centers within a region, providing **high availability**.

3. **What is the purpose of Edge Locations in AWS?**  
   - Edge Locations are used for **content caching** with Amazon CloudFront to reduce latency.

4. **Which AWS services are Global (not tied to a single region)?**  
   - IAM, Route 53, CloudFront, WAF, and Security Hub.

5. **What factors should you consider when selecting an AWS region?**  
   - Latency, compliance requirements, cost, and available services.

---

## **2. AWS Compute Services**
### **2.1 Amazon EC2**
6. **What is the difference between EC2 On-Demand, Reserved Instances, and Spot Instances?**  
   - **On-Demand**: Pay-as-you-go. Best for short-term workloads.  
   - **Reserved Instances**: Commit to **1 or 3 years** for lower cost. Best for steady workloads.  
   - **Spot Instances**: Up to **90% discount**, but can be interrupted by AWS.

7. **What are Dedicated Hosts, and when would you use them?**  
   - A **physical EC2 server** dedicated to a single customer. Used for **compliance** or software licensing.

8. **How does Auto Scaling help improve availability and cost efficiency?**  
   - It **automatically scales** EC2 instances **up/down** based on demand.

9. **What AWS service allows you to run serverless applications?**  
   - AWS Lambda.

10. **How does Elastic Load Balancing (ELB) improve application performance?**  
   - It **distributes traffic** across multiple EC2 instances to **increase availability**.

### **2.2 AWS Lambda**
11. **What is AWS Lambda, and how does it differ from EC2?**  
   - Lambda is a **serverless compute service** that automatically scales without provisioning instances.

12. **What triggers AWS Lambda functions?**  
   - API Gateway, S3, DynamoDB, CloudWatch, SNS, and more.

13. **How does AWS Lambda pricing work?**  
   - You pay for **execution time** and number of requests.

14. **What AWS service is commonly used to invoke Lambda functions asynchronously?**  
   - Amazon SNS (Simple Notification Service).

15. **What is the maximum execution time for an AWS Lambda function?**  
   - 15 minutes.

---

## **3. AWS Storage Services**
### **3.1 Amazon S3**
16. **What are the four S3 storage classes?**  
   - Standard, Intelligent-Tiering, Glacier, and S3 One Zone-IA.

17. **How does S3 Glacier help optimize storage costs?**  
   - It provides **low-cost archival storage** for infrequently accessed data.

18. **What is the purpose of S3 Lifecycle Policies?**  
   - Automates data movement between storage classes based on rules.

19. **How does AWS ensure high availability of S3 objects?**  
   - Objects are replicated across **multiple Availability Zones (AZs).**

20. **What is the difference between S3 Standard and S3 Intelligent-Tiering?**  
   - Intelligent-Tiering automatically moves objects between cost-effective storage tiers.

### **3.2 Amazon EBS & EFS**
21. **What is the difference between Amazon EBS and Amazon EFS?**  
   - **EBS** is block storage for **single EC2 instances**.  
   - **EFS** is a managed file system for **multiple instances**.

22. **Which AWS storage service is best suited for high-performance databases?**  
   - Amazon EBS (Provisioned IOPS).

23. **How does AWS ensure EBS durability?**  
   - EBS volumes are **replicated within an Availability Zone**.

24. **What is the main advantage of using EFS over EBS?**  
   - EFS supports **multiple EC2 instances** accessing the same file system.

25. **Can an EBS volume be attached to multiple EC2 instances?**  
   - No, an EBS volume can only be attached to **one instance at a time** (except for EBS Multi-Attach).

---

## **4. AWS Pricing & Billing**
### **4.1 AWS Pricing Models**
26. **What are the four main AWS pricing models?**  
   - On-Demand, Reserved, Spot, and Savings Plans.

27. **What is the difference between On-Demand and Reserved Instances?**  
   - **On-Demand**: Pay per hour. **Reserved**: Commit for **1 or 3 years** for a discount.

28. **How do Savings Plans help reduce AWS costs?**  
   - They provide flexible **discounts** based on long-term commitments.

29. **How does AWS charge for data transfer between regions?**  
   - **Outbound transfers** between regions are **not free** and incur costs.

30. **What AWS service helps estimate monthly cloud costs before deployment?**  
   - AWS Pricing Calculator.

---

## **5. AWS Security & Compliance**
### **5.1 IAM (Identity & Access Management)**
36. **What are the main components of AWS IAM?**  
   - IAM users, groups, roles, and policies.

37. **What is the difference between an IAM user, group, and role?**  
   - **User**: Individual login.  
   - **Group**: Collection of users with shared policies.  
   - **Role**: Temporary access for AWS services.

38. **What is Multi-Factor Authentication (MFA), and why is it important?**  
   - MFA adds a **second layer of authentication** for security.

39. **What AWS tool helps analyze IAM permissions and detect overprivileged access?**  
   - IAM Access Analyzer.

40. **How do IAM permission boundaries work?**  
   - They **limit the maximum permissions** an IAM user/role can have.

---

# **Final Exam Tips**
- **Understand AWS Free Tier Limits.**
- **Learn the Shared Responsibility Model.**
- **Review AWS Pricing Models & Cost Optimization Strategies.**
- **Study IAM, CloudFront, S3, and EC2 services.**
- **Take multiple practice exams.**

---

This **AWS Cloud Practitioner (CLF-C01) Q&A** study guide provides a structured way to review the exam topics. **Use this to reinforce your learning and track your progress!**
