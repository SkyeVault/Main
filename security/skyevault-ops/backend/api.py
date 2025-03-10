from flask import Flask, jsonify
import sqlite3

app = Flask(__name__)

DB_PATH = "security/security_reports.db"

def get_reports():
    """Retrieve all security reports from the database."""
    conn = sqlite3.connect(DB_PATH)
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM reports ORDER BY timestamp DESC")
    reports = cursor.fetchall()
    conn.close()
    return reports

@app.route("/api/reports", methods=["GET"])
def fetch_reports():
    """API Endpoint: Get all security reports."""
    reports = get_reports()
    
    if not reports:
        return jsonify({"message": "No reports found"}), 404

    report_list = [
        {"id": r[0], "service": r[1], "findings": r[2], "timestamp": r[3]}
        for r in reports
    ]

    return jsonify(report_list), 200

if __name__ == "__main__":
    app.run(debug=True, host="0.0.0.0", port=5000)
