import sqlite3

DB_FILE = "security_reports.db"

def connect_db():
    return sqlite3.connect(DB_FILE)

def create_tables():
    conn = connect_db()
    cursor = conn.cursor()
    cursor.execute("""
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
    conn = connect_db()
    cursor = conn.cursor()
    cursor.execute("INSERT INTO reports (service, findings) VALUES (?, ?)", (service, findings))
    conn.commit()
    conn.close()

def get_reports():
    conn = connect_db()
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM reports ORDER BY timestamp DESC")
    rows = cursor.fetchall()
    conn.close()
    return rows

# Initialize the database
create_tables()
