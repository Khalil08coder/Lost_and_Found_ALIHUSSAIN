# This fix was used with help from the internet to fix the issue of
# the database not being created when running setup_db.py. The issue
# was that the database file was not being created in the correct
# directory. The fix was to change the path of the database file to
# be relative to the setup_db.py file.
"""
Run this file ONCE to (re)create a clean lost_and_found.db next to it.

"""

from dbinformation import get_connection

conn = get_connection()
cur = conn.cursor()

cur.execute('''
CREATE TABLE IF NOT EXISTS users (
    studentID TEXT PRIMARY KEY,
    password TEXT NOT NULL
)''')

cur.execute('''
CREATE TABLE IF NOT EXISTS ItemTable (
    ItemID INTEGER PRIMARY KEY AUTOINCREMENT,
    ItemName TEXT NOT NULL,
    DateLost TEXT,
    LocationLost TEXT,
    DateFound TEXT,
    LocationFound TEXT,
    ItemValue REAL,
    ItemStatus TEXT
)''')

cur.execute("SELECT COUNT(*) FROM users")
if cur.fetchone()[0] == 0:
    cur.executemany(
        "INSERT INTO users (studentID, password) VALUES (?, ?)",
        [
            ('22000', 'password123'),
            ('23456', 'mypassword'),
            ('23567', 'pass111'),
            ('22222', 'pass222'),
        ]
    )
    print("Seeded 4 test users.")
else:
    print("users table already has data — left it alone.")

conn.commit()
conn.close()
print("Database is ready at:", __import__("dbinformation").DB_FILE)
