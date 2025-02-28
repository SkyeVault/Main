import sqlite3
import json
from database import get_reports

def display_reports():
    """Fetch and display stored security reports."""
    reports = get_reports()

    if not reports:
        print("\n✅ No security findings recorded in the database.")
        return

    print("\n🚀 Security Reports:")
    for report in reports:
        print(f"[{report[3]}] [{report[1]}] {report[2]}")

def export_reports_to_json(filename="security_reports.json"):
    """Export security reports to a JSON file."""
    reports = get_reports()
    data = [{"timestamp": r[3], "service": r[1], "findings": r[2]} for r 
in reports]

    with open(filename, "w") as f:
        json.dump(data, f, indent=4)
    
    print(f"\n📂 Reports exported to {filename}")

if __name__ == "__main__":
    print("\n🔍 Retrieving Security Reports...")
    display_reports()
    export_reports_to_json()

