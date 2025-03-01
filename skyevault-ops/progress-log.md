# SkyeVault Ops Development Log

## 📅 Date: February 26, 2025

This document records all major development steps, fixes, and future plans for **SkyeVault Ops** security automation. Use this as a reference for future improvements and troubleshooting.

---

## ✅ **1. Git & Project Setup**
### **Fixing Git Issues & Repo Cleanup**
- **Issue:** `skyevault-ops` was mistakenly treated as a submodule, causing issues with Git tracking.
- **Solution:**
  1. Removed `.git` folder inside `skyevault-ops`.
  2. Deleted incorrect `skyevault-ops` references in Git.
  3. Recreated `skyevault-ops` as a standard directory.
  4. Cleaned up `.gitignore` to prevent tracking SQLite database (`security_reports.db`).
  5. Successfully pushed all cleaned files to GitHub.

#### **Commands Used:**
```sh
rm -rf skyevault-ops.git  # Remove submodule directory
rm -rf .git/modules/skyevault-ops  # Remove lingering Git tracking
rm -rf skyevault-ops  # Delete local folder

git add .
git commit -m "Fully removed SkyeVault Ops submodule"
git push origin main --force  # Force update repo structure
```

---

## ✅ **2. AWS Security Automation Scripts**

### **🔹 IAM Security Check (`iam_security_check.py`)**
- **Checks IAM users for:**
  - Users **without MFA enabled** 🚨
  - **Inactive users** (90+ days without login) ⚠️
- **Findings logged in** `security_reports.db`.
- **Test Output:**
```sh
🔍 Running IAM Security Check...
🚨 Users without MFA enabled:
 - SkyeVaultUser
✅ IAM Security Check Complete!
```

---

### **🔹 S3 Security Check (`s3_security_check.py`)**
- **Scans all AWS S3 buckets for public access.**
- **Test Output:**
```sh
🔍 Running S3 Security Check...
✅ All S3 buckets are secure!
```

---

### **🔹 GuardDuty Security Check (`guardduty_check.py`)**
- **Pulls threat alerts from AWS GuardDuty.**
- **Needs additional validation of results.**

---

### **🔹 CloudTrail Security Check (`cloudtrail_check.py`)**
- **Monitors AWS CloudTrail logs for risky events:**
  - 🚨 `GenerateDataKey` by unknown users.
  - 🚨 `ListAccessKeys` by **root**.
- **Findings logged in** `security_reports.db`.
- **Test Output:**
```sh
🔍 Running CloudTrail Security Check...
🚨 Security Alert: GenerateDataKey by Unknown User at 2025-02-26 16:48:22
🚨 Security Alert: ListAccessKeys by root at 2025-02-26 16:46:52
```

---

## ✅ **3. Database Integration (`database.py`)**
- **SQLite database created:** `security_reports.db`
- **Stores security alerts from all scripts.**
- **Verification Command:**
```python
from database import get_reports
print(get_reports())
```
- **Example Database Output:**
```sh
[(1, 'IAM', 'User SkyeVaultUser has no MFA enabled', '2025-02-26 21:28:41'),
 (2, 'CloudTrail', '🚨 Security Alert: ListAccessKeys by root at 2025-02-26 16:46:52', '2025-02-26 21:50:39')]
```

### **🔹 Fix Needed: CloudTrail Duplicate Entries**
- **Issue:** CloudTrail logs are being saved **multiple times** when rerunning the script.
- **Fix:** Before saving a new event, check if it **already exists in the database**.

---

## 🔥 **Next Steps: UI Development**
### **1️⃣ Frontend Dashboard (Security Visualization)**
- **Tech Stack:**
  - **Frontend:** React.js or Flask
  - **Backend:** Python (Flask or FastAPI)
  - **Database:** SQLite (Upgrade to DynamoDB later)
  - **Security Reports API:** JSON endpoints for UI

### **2️⃣ Automate Notifications**
- **Send alerts for high-risk security events.**
- **Potential integrations:**
  - Email alerts 📧
  - Slack/Webhooks 🔗
  - SMS/Phone notifications 📱

### **3️⃣ Improve CloudTrail Event Filtering**
- **Check if an event exists before logging it.**
- Prevent duplicate security alerts.

---

## 🚀 **Final Notes**
✅ **All scripts are working and saving security events.**
✅ **Git repository is clean and synced with GitHub.**
✅ **Database logging works as expected.**
 

# 📜 SkyeVault Ops Setup & Debugging Log
**Date:** *February 28, 2025*  
**Objective:** *Set up and debug the Cyberpunk AWS Security Dashboard using Flask, HTML, CSS, JavaScript, and Python API.*  

---

## 1️⃣ Project Initialization  
### ✅ Step 1: Set Up Flask & Directory Structure  
📌 First, we set up the **Flask app structure** with `templates/` for HTML and `static/` for CSS & JS.  

### **Project Structure**  
```
/skyevault-ops
│── /templates
│    ├── index.html  # Flask HTML template
│── /static
│    ├── /css
│    │    ├── style.css  # UI styling
│    ├── /js
│    │    ├── main.js  # JavaScript for logs & graphs
│── app.py  # Flask backend
│── requirements.txt  # Python dependencies
│── README.md  # Project Documentation
```
---

## 2️⃣ Flask Backend - `app.py`  
### ✅ Step 2: Creating the Flask API  
created the Flask app (`app.py`) to:  
- **Render the dashboard (`index.html`)**  
- **Serve security logs as JSON (`/logs`)**  
- **Load static files (`style.css`, `main.js`)**  

### **Final `app.py`**  
```python
from flask import Flask, render_template, jsonify

app = Flask(__name__, template_folder="templates", static_folder="static")

# Simulated AWS security logs
def get_security_logs():
    return [
        {"service": "IAM", "status": "WARNING", "message": "Excessive IAM permissions detected."},
        {"service": "CloudTrail", "status": "INFO", "message": "New API call recorded."},
        {"service": "GuardDuty", "status": "CRITICAL", "message": "Possible credential compromise detected!"},
        {"service": "WAF", "status": "INFO", "message": "Web request blocked by firewall."}
    ]

@app.route('/')
def index():
    return render_template("index.html")  # Serve the HTML Dashboard

@app.route('/logs')
def logs():
    return jsonify(get_security_logs())  # Serve logs as JSON

if __name__ == '__main__':
    app.run(debug=True)
```

3️⃣ HTML - index.html

✅ Step 3: Creating the Dashboard Layout

📌 We added sections for logs, graphs, and Red Team buttons.

Final index.html
```
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Cyberpunk AWS Security Dashboard</title>
    <link rel="stylesheet" href="{{ url_for('static', filename='css/style.css') }}">
    <script src="https://cdn.jsdelivr.net/npm/chart.js"></script> <!-- Graphs -->
    <script src="{{ url_for('static', filename='js/main.js') }}" defer></script>
</head>
<body>
    <div class="container">
        <h1>⚡ Cyberpunk AWS Security Dashboard ⚡</h1>

        <!-- Security Logs -->
        <div class="box">
            <h2>📜 Security Logs</h2>
            <div id="terminal">
                <pre id="log-output">Loading security logs...</pre>
            </div>
        </div>

        <!-- Graphs -->
        <div class="box">
            <h2>📊 Security Insights</h2>
            <canvas id="securityGraph"></canvas>
        </div>

        <!-- Red Team Tools -->
        <div class="box">
            <h2>🛠️ Red Team Tools</h2>
            <button class="red-button" onclick="launchScan()">🔍 Network Scan</button>
            <button class="red-button" onclick="privilegeEscalation()">⚠️ Privilege Escalation Test</button>
            <button class="red-button" onclick="runExploit()">💥 Exploit S3 Bucket</button>
        </div>
    </div>
</body>
</html>


This log documents everything from setting up Flask to debugging 

`  
```




