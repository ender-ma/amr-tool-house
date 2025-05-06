# database/db_manager.py

import sqlite3

def get_connection():
    return sqlite3.connect("amr.db")

def fetch_tools():
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute("SELECT id, name, description FROM tools")
    results = cursor.fetchall()
    conn.close()
    return results
