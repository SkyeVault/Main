# Setup Guide
# SkyeVault Ops Security Dashboard Setup Guide

## Directory Structure
```
SkyeVault-Ops/
│── backend/
│   │── app.py
│   │── database.py
│   ├── security/
│   │   ├── iam_security_check.py
│   │   ├── s3_security_check.py
│   │   ├── cloudtrail_check.py
│   │   ├── guardduty_check.py
│── templates/
│   ├── index.html
│── static/
│   ├── css/
│   │   ├── style.css
│   ├── js/
│   │   ├── main.js
│── security_reports.db
│── .gitignore
│── requirements.txt
```

## **1️⃣ Backend Files**

### **`backend/app.py`**
This is the Flask app that serves the security dashboard.
```python
from flask import Flask, render_template, jsonify
import sqlite3

app = Flask(__name__)

def get_security_logs():
    conn = sqlite3.connect("security_reports.db")
    c = conn.cursor()
    c.execute("SELECT service, findings, timestamp FROM reports ORDER BY timestamp DESC LIMIT 10")
    logs = [{"service": row[0], "status": "ALERT", "message": row[1], "timestamp": row[2]} for row in c.fetchall()]
    conn.close()
    return logs

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/logs')
def logs():
    return jsonify(get_security_logs())

if __name__ == '__main__':
    app.run(debug=True)
```

### **`backend/database.py`**
Handles storing security reports in SQLite.
```python
import sqlite3

DB_FILE = "security_reports.db"

def init_db():
    conn = sqlite3.connect(DB_FILE)
    c = conn.cursor()
    c.execute("""
        CREATE TABLE IF NOT EXISTS reports (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            service TEXT,
            findings TEXT,
            timestamp DATETIME DEFAULT CURRENT_TIMESTAMP
        )
    """)
    conn.commit()
    conn.close()

def save_report(service, findings):
    conn = sqlite3.connect(DB_FILE)
    c = conn.cursor()
    c.execute("INSERT INTO reports (service, findings) VALUES (?, ?)", (service, findings))
    conn.commit()
    conn.close()

def get_reports():
    conn = sqlite3.connect(DB_FILE)
    c = conn.cursor()
    c.execute("SELECT * FROM reports ORDER BY timestamp DESC")
    rows = c.fetchall()
    conn.close()
    return rows

init_db()
```

### **Security Checks (`backend/security/`)

Each security check script gathers AWS security data and saves it to the database.

#### **`backend/security/iam_security_check.py`**
```python
import boto3
from database import save_report

iam = boto3.client('iam')

def list_users_without_mfa():
    users = iam.list_users()
    users_without_mfa = []
    
    for user in users['Users']:
        user_name = user['UserName']
        mfa_devices = iam.list_mfa_devices(UserName=user_name)
        if not mfa_devices['MFADevices']:
            users_without_mfa.append(user_name)
            save_report("IAM", f"User {user_name} has no MFA enabled")

    return users_without_mfa

list_users_without_mfa()
```

#### **`backend/security/cloudtrail_check.py`**
```python
import boto3
from database import save_report

cloudtrail = boto3.client('cloudtrail')

def check_cloudtrail_events():
    response = cloudtrail.lookup_events(MaxResults=5)
    for event in response['Events']:
        save_report("CloudTrail", f"🚨 Security Alert: {event['EventName']} by {event.get('Username', 'Unknown')} at {event['EventTime']}")

check_cloudtrail_events()
```

#### **`backend/security/s3_security_check.py`**
```python
import boto3
from database import save_report

s3 = boto3.client('s3')

def check_s3_buckets():
    buckets = s3.list_buckets()
    for bucket in buckets['Buckets']:
        save_report("S3", f"Checked bucket {bucket['Name']} for security vulnerabilities.")

check_s3_buckets()
```

---

## **2️⃣ Frontend Files**

### **`templates/index.html`**
```html
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>SkyeVault Ops Security Dashboard</title>
    <link rel="stylesheet" href="{{ url_for('static', filename='css/style.css') }}">
    <script src="{{ url_for('static', filename='js/main.js') }}" defer></script>
</head>
<body>
    <div class="container">
        <h1>SkyeVault Ops Security Dashboard</h1>
        <div id="terminal">
            <pre id="log-output">Loading security logs...</pre>
        </div>
    </div>
</body>
</html>
```

### **`static/css/style.css`**
```css
body {
    background-color: black;
    color: #00ffcc;
    font-family: 'Courier New', monospace;
    text-align: center;
}

#terminal {
    background: rgba(0, 255, 204, 0.1);
    border: 1px solid #00ffcc;
    padding: 20px;
    width: 80%;
    margin: auto;
    text-align: left;
    min-height: 300px;
    overflow-y: auto;
}
```

### **`static/js/main.js`**
```javascript
document.addEventListener('DOMContentLoaded', function () {
    function fetchLogs() {
        fetch('/logs')
            .then(response => response.json())
            .then(data => {
                let logOutput = document.getElementById('log-output');
                logOutput.innerHTML = "";
                data.forEach(log => {
                    logOutput.innerHTML += `[${log.timestamp}] [${log.service}] ${log.status} - ${log.message}\n`;
                });
            })
            .catch(error => console.error('Error fetching logs:', error));
    }

    setInterval(fetchLogs, 5000);
    fetchLogs();
});
```

---

## **3️⃣ Running the Dashboard**
### **Install Dependencies:**
```sh
pip install flask boto3
```
### **Run the Flask App:**
```sh
python backend/app.py
```
### **View in Browser:**
- Open **http://127.0.0.1:5000/** in your browser.

---

## **4️⃣ Upload to GitHub**
```sh
git init
git add .
git commit -m "Initial commit for SkyeVault Ops Security Dashboard"
git branch -M main
git remote add origin https://github.com/SkyeVault/Main.git
git push -u origin main
```

