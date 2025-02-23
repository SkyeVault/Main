# AWS Shared Responsibility Model

The **AWS Shared Responsibility Model** defines **security and compliance responsibilities** between AWS and customers. AWS secures the **cloud infrastructure**, while customers are responsible for securing **their data, applications, and configurations**.

---

## **1. AWS Responsibilities ("Security OF the Cloud")**
AWS is responsible for securing the **infrastructure that runs AWS services**, including:
- **Data centers** (physical security, power, climate control)
- **Network security** (firewalls, DDoS protection)
- **Hypervisor & virtualization security** (for EC2 and managed services)
- **Global infrastructure** (Regions, Availability Zones, Edge Locations)
- **Hardware security** (AWS-designed servers and networking)

AWS provides **security compliance certifications**, such as:
- **SOC 2, ISO 27001, FedRAMP, HIPAA, GDPR compliance**

---

## **2. Customer Responsibilities ("Security IN the Cloud")**
Customers are responsible for **securing their own AWS workloads**, including:
- **IAM & Access Management** (Users, Roles, Policies)
- **Data Protection** (Encryption, Key Management, Backups)
- **Application Security** (Patch management, securing APIs)
- **Network Security** (Configuring Security Groups, VPCs, NACLs)
- **Monitoring & Incident Response** (CloudTrail, GuardDuty, Security Hub)

### **Customer Responsibilities by Service Type**
| **Service Type** | **AWS Responsibility** | **Customer Responsibility** |
|-----------------|----------------------|---------------------------|
| **EC2, VPC, RDS (IaaS)** | Infrastructure security, Physical hosts | OS security, Network configuration, IAM policies |
| **Lambda, DynamoDB, S3 (PaaS)** | Service-level security, Serverless runtime | Data security, IAM permissions, API protection |
| **SaaS (Managed Services like RDS, S3, Aurora)** | Full service management | Access control, Data encryption, Compliance configurations |

---

## **3. Examples of Shared Responsibilities**
| **Scenario** | **AWS Responsibility** | **Customer Responsibility** |
|-------------|----------------------|---------------------------|
| **A hacker tries to break into AWS data centers** | AWS secures physical facilities | N/A (Customer has no control) |
| **An EC2 instance is compromised due to an unpatched vulnerability** | AWS secures the hardware & hypervisor | Customer must **update OS and apply security patches** |
| **S3 bucket is accidentally left public** | AWS secures the storage infrastructure | Customer must **configure bucket permissions** correctly |
| **Unauthorized access to an IAM user** | AWS ensures IAM service is secure | Customer must **enforce MFA & strong policies** |
| **Data exfiltration from an RDS database** | AWS secures the managed database service | Customer must **encrypt data and control access** |

---

## **4. AWS Security & Compliance Tools**
### **Security & Identity**
- **IAM** (Identity & Access Management) – Controls user permissions and roles.
- **AWS Organizations & SCPs** – Manages permissions across multiple AWS accounts.
- **AWS Secrets Manager** – Securely stores API keys and passwords.

### **Data Protection**
- **AWS KMS** (Key Management Service) – Encrypts data at rest & in transit.
- **S3 Block Public Access** – Prevents accidental data exposure.
- **AWS Backup** – Automates backups for disaster recovery.

### **Threat Detection & Monitoring**
- **AWS GuardDuty** – Detects security threats and anomalies.
- **AWS Security Hub** – Aggregates security alerts and compliance findings.
- **AWS CloudTrail** – Logs API activity for security audits.

---

## **5. Best Practices for Shared Security**
✅ **Enable Multi-Factor Authentication (MFA)** for IAM users.  
✅ **Use IAM roles instead of long-term access keys**.  
✅ **Encrypt sensitive data** using AWS KMS.  
✅ **Apply least privilege access** with IAM policies.  
✅ **Use Security Groups & Network ACLs** to control traffic.  
✅ **Monitor CloudTrail logs for suspicious activity**.  
✅ **Regularly patch and update your EC2 instances**.  

---

## **6. AWS Compliance Certifications**
AWS maintains compliance with **global security standards**, including:
- **SOC 1, SOC 2, SOC 3**
- **ISO 27001, ISO 9001**
- **HIPAA (Health Information Security)**
- **FedRAMP (US Government Cloud Security)**
- **PCI DSS (Payment Card Industry Data Security Standard)**

Customers must **configure their AWS workloads** to meet industry compliance standards.

---

## **7. Summary**
| **Responsibility** | **AWS (Security OF the Cloud)** | **Customer (Security IN the Cloud)** |
|-----------------|----------------------|---------------------------|
| **Physical Security** | Protects data centers, global infrastructure | N/A |
| **Network Security** | Protects AWS backbone, DDoS mitigation | Configures VPC, Security Groups, NACLs |
| **Data Protection** | Encrypts AWS storage & network | Encrypts customer data, manages access |
| **IAM & Access Control** | Manages IAM as a service | Configures users, roles, permissions |
| **Compliance & Audits** | Provides compliance reports & tools | Ensures internal compliance with policies |

---

## **8. Additional Resources**
- [AWS Shared Responsibility Model](https://aws.amazon.com/compliance/shared-responsibility-model/)
- [AWS Security Best Practices](https://aws.amazon.com/security/)
- [AWS Well-Architected Framework](https://aws.amazon.com/architecture/well-architected/)

---

This Markdown file provides a **clear breakdown** of the **AWS Shared Responsibility Model**. **Use this guide to understand security ownership in AWS!**
