import sqlite3

DB_FILE = "security_reports.db"

def connect_db():
    return sqlite3.connect(DB_FILE)

def create_tables():
    """Ensure security report database tables exist."""
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

# Ensure table is created at startup
create_tables()
