from flask import Flask, render_template, jsonify

app = Flask(__name__, template_folder="templates", static_folder="static")  # Ensure correct folders

# Simulated AWS security logs (Replace with real AWS API calls later)
def get_security_logs():
    return [
        {"service": "IAM", "status": "WARNING", "message": "Excessive IAM permissions detected."},
        {"service": "CloudTrail", "status": "INFO", "message": "New API call recorded."},
        {"service": "GuardDuty", "status": "CRITICAL", "message": "Possible credential compromise detected!"},
        {"service": "WAF", "status": "INFO", "message": "Web request blocked by firewall."}
    ]

@app.route('/')
def index():
    return render_template("index.html")  # Ensure Flask renders the template properly

@app.route('/logs')
def logs():
    return jsonify(get_security_logs())  # Fixed function returning logs properly

if __name__ == '__main__':
    app.run(debug=True)  # Run Flask locally with debugging
