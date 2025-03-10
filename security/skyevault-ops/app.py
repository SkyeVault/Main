import subprocess
import json
import os
from flask import Flask, render_template, jsonify

app = Flask(__name__, template_folder="templates", static_folder="static")

LOG_FILE = "security_logs.json"

def run_blue_team_scripts():
    """ Runs Blue Team security scripts and logs results. """
    scripts = [
        "backend/security/blue_team/iam_security_checker.py",
        "backend/security/blue_team/cloudtrail_checker.py",
        "backend/security/blue_team/guardduty_check.py",
        "backend/security/blue_team/s3_auditor.py"
    ]
    
    results = []
    
    for script in scripts:
        try:
            result = subprocess.run(["python3", script], capture_output=True, text=True)
            output = result.stdout.strip() if result.stdout else "No output"
            results.append({"script": script, "output": output})
        except Exception as e:
            results.append({"script": script, "output": f"Error running script: {str(e)}"})
    
    # Save results to a JSON log file
    with open(LOG_FILE, "w") as f:
        json.dump(results, f, indent=4)

@app.route('/')
def index():
    return render_template("index.html")

@app.route('/logs')
def logs():
    """ Fetch security logs from the JSON file. """
    if os.path.exists(LOG_FILE):
        with open(LOG_FILE, "r") as f:
            return jsonify(json.load(f))
    return jsonify([])

@app.route('/run-blue-team')
def run_blue_team():
    """ API to trigger the Blue Team security checks manually. """
    run_blue_team_scripts()
    return jsonify({"status": "Blue Team security scripts executed!"})

if __name__ == '__main__':
    run_blue_team_scripts()  # Run once at startup
    app.run(debug=True)
