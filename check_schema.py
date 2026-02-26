import sqlite3

conn = sqlite3.connect("database/dns_filter.db")
cursor = conn.cursor()

print("=== QUERIES TABLE SCHEMA ===")
cursor.execute("PRAGMA table_info(queries)")
for col in cursor.fetchall():
    print(col)

print("\n=== QUERIES SAMPLE ===")
cursor.execute("SELECT * FROM queries LIMIT 5")
for row in cursor.fetchall():
    print(row)

print("\n=== BLOCKED TABLE SCHEMA ===")
cursor.execute("PRAGMA table_info(blocked)")
for col in cursor.fetchall():
    print(col)

print("\n=== BLOCKED SAMPLE ===")
cursor.execute("SELECT * FROM blocked LIMIT 5")
for row in cursor.fetchall():
    print(row)

print("\n=== COUNTS ===")
cursor.execute("SELECT COUNT(*) FROM blocked")
print("Blocked domains:", cursor.fetchone()[0])
cursor.execute("SELECT COUNT(*) FROM queries")
print("Total queries:", cursor.fetchone()[0])
cursor.execute("SELECT COUNT(*) FROM queries WHERE action='blocked'")
print("Blocked queries:", cursor.fetchone()[0])
cursor.execute("SELECT COUNT(*) FROM queries WHERE action='allowed'")
print("Allowed queries:", cursor.fetchone()[0])

conn.close()
