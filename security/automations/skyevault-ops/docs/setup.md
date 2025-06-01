# AWS Security Dashboard Integration Guide

## Project Structure
```
Main/
│── skyevault-ops/
│   ├── backend/
│   │   ├── app.py  # Flask application
│   │   ├── database.py  # SQLite database handling
│   │   ├── config.py  # Configuration settings
│   │   ├── security/
│   │   │   ├── iam_security_check.py  # IAM security script
│   │   │   ├── s3_security_check.py  # S3 security script
│   │   │   ├── guardduty_check.py  # GuardDuty security script
│   │   │   ├── cloudtrail_check.py  # CloudTrail security script
│   │   ├── static/
│   │   │   ├── css/style.css  # Frontend styling
│   │   │   ├── js/main.js  # Frontend interactivity
│   │   ├── templates/
│   │   │   ├── index.html  # Frontend layout
```

## 1️⃣ Backend (Flask App)
**File:** `backend/app.py`
```python
from flask import Flask, render_template, jsonify
from database import get_reports

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/logs')
def logs():
    return jsonify(get_reports())

if __name__ == '__main__':
    app.run(debug=True)
```

## 2️⃣ Database Handling
**File:** `backend/database.py`
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
    return [{"service": row[1], "status": "ALERT", "message": row[2]} for row in rows]

init_db()
```

## 3️⃣ Frontend (HTML)
**File:** `backend/templates/index.html`
```html
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>SkyeVault Security Dashboard</title>
    <link rel="stylesheet" href="{{ url_for('static', filename='css/style.css') }}">
    <script src="{{ url_for('static', filename='js/main.js') }}" defer></script>
</head>
<body>
    <div class="container">
        <h1>SkyeVault Security Dashboard</h1>
        <div id="terminal">
            <pre id="log-output">Loading security logs...</pre>
        </div>
    </div>
</body>
</html>
```

## 4️⃣ CSS (Cyberpunk Styling)
**File:** `backend/static/css/style.css`
```css
body {
    background-color: black;
    color: #00ffcc;
    font-family: 'Courier New', monospace;
    text-align: center;
    padding: 20px;
}

h1 {
    text-shadow: 0 0 10px #00ffcc;
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
    font-size: 16px;
    box-shadow: 0 0 15px #00ffcc;
}

pre {
    white-space: pre-wrap;
}
```

## 5️⃣ JavaScript (Logs Fetching)
**File:** `backend/static/js/main.js`
```javascript
document.addEventListener('DOMContentLoaded', function () {
    function fetchLogs() {
        fetch('/logs')
            .then(response => response.json())
            .then(data => {
                let logOutput = document.getElementById('log-output');
                logOutput.innerHTML = "";
                data.forEach(log => {
                    logOutput.innerHTML += `[${log.service}] ${log.status} - ${log.message}\n`;
                });
            })
            .catch(error => console.error('Error fetching logs:', error));
    }

    setInterval(fetchLogs, 5000);
    fetchLogs();
});
```

## 6️⃣ Running the Project
### Install Flask:
```sh
pip install flask
```

### Run Flask App:
```sh
python backend/app.py
```

### Open in Browser:
Go to `http://127.0.0.1:5000/`

## 7️⃣ Upload to GitHub
```sh
git add .
git commit -m "Integrated SkyeVault AWS Security Dashboard"
git push origin main
