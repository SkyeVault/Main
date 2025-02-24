# AWS KMS Key Lab

This lab will guide you through the process of creating and managing an AWS KMS key (Customer Managed Key). KMS keys are used to encrypt data and control access to encrypted resources in your AWS environment.

---

## Lab Objectives

- Create a Customer Managed Key (CMK) in AWS KMS.
- Configure key policies and administrative permissions.
- Enable automatic key rotation.
- Verify the key creation and capture a screenshot for documentation.

---

## Prerequisites

- An AWS account with permissions to create and manage KMS keys.
- Basic familiarity with the AWS Management Console.
- (Optional) AWS CLI installed and configured for command-line verification.

---

## Part 1: Creating an AWS KMS Key

### Step 1: Navigate to AWS KMS

1. Sign in to the AWS Management Console.
2. Open the **Key Management Service (KMS)** console.

### Step 2: Create a New Customer Managed Key

1. In the KMS console, click **Create key**.
2. Choose **Symmetric** for the key type (recommended for most encryption use cases).
3. Select **Encrypt and decrypt** as the key usage.
4. Click **Next**.

### Step 3: Configure Key Details

1. **Key Alias and Description:**  
   - Provide a unique alias (e.g., `my-lab-key`) and a brief description.
2. **Key Administrative Permissions:**  
   - Specify the IAM users or roles that will have administrative control over this key.
3. **Key Usage Permissions:**  
   - Define which IAM principals can use this key for cryptographic operations.
4. Click **Next** after configuring permissions.

### Step 4: Enable Automatic Key Rotation

1. On the rotation settings page, enable automatic key rotation if desired.  
   (Automatic rotation rotates the key every year, enhancing security.)
2. Click **Next** and review your settings.
3. Click **Finish** to create the key.

---

## Part 2: Verifying and Documenting Your KMS Key

### Step 1: Verify Key Creation

1. Return to the KMS dashboard.
2. Locate your new key (e.g., `my-lab-key`) in the list.
3. Click on the key to view its details, including key policies and rotation status.

### Step 2: Capture a Screenshot

1. **Decide What to Capture:**  
   - Capture the key details page that shows the alias, key ID, status, and automatic rotation setting.
2. **Take the Screenshot:**  
   - **Windows:** Use `Win + Shift + S` or `PrtScn`.
   - **macOS:** Use `Cmd + Shift + 4` or `Cmd + Shift + 3`.
   - **Linux:** Use the `PrtScn` key or a screenshot tool.
3. **Edit if Necessary:**  
   - Crop the image to focus on key details and remove any sensitive information.
  
   - *Note: I captured screenshots during this lab to verify that everything worked as expected. However, I have not published these screenshots in the repository for privacy reasons.*



