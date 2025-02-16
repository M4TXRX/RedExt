# db_setup.py

import sqlite3

def setup_database():
    conn = sqlite3.connect('c2_server.db')
    cursor = conn.cursor()

    # Agents table (with optional columns for status, hostname, etc.)
    cursor.execute('''
    CREATE TABLE IF NOT EXISTS agents (
        agent_id TEXT PRIMARY KEY,
        hostname TEXT,
        status TEXT DEFAULT 'offline',
        last_seen TIMESTAMP DEFAULT CURRENT_TIMESTAMP
    )
    ''')

    # Tasks table
    cursor.execute('''
    CREATE TABLE IF NOT EXISTS tasks (
        task_id INTEGER PRIMARY KEY AUTOINCREMENT,
        agent_id TEXT NOT NULL,
        description TEXT,
        command TEXT NOT NULL,
        parameters TEXT,
        status TEXT DEFAULT 'pending',
        assigned_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
        FOREIGN KEY (agent_id) REFERENCES agents(agent_id)
    )
    ''')

    # Data records for exfiltrated data
    cursor.execute('''
    CREATE TABLE IF NOT EXISTS data_records (
        data_id INTEGER PRIMARY KEY AUTOINCREMENT,
        agent_id TEXT NOT NULL,
        data_type TEXT,
        payload TEXT,
        created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
        FOREIGN KEY (agent_id) REFERENCES agents(agent_id)
    )
    ''')

    conn.commit()
    conn.close()
    print("Database setup complete.")

if __name__ == "__main__":
    setup_database()
