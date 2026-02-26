import sqlite3
import os

db_path = '../database/dns_filter.db'
if not os.path.exists(db_path):
    print(f"DB not found at {db_path}")
else:
    try:
        conn = sqlite3.connect(db_path)
        cursor = conn.cursor()
        cursor.execute("SELECT name FROM sqlite_master WHERE type='table';")
        tables = cursor.fetchall()
        print(f"Tables: {tables}")
        for table in tables:
            t = table[0]
            print(f"Schema for {t}:")
            cursor.execute(f"PRAGMA table_info({t})")
            cols = cursor.fetchall()
            for c in cols:
                print(c)
        conn.close()
    except Exception as e:
        print(f"Error: {e}")
