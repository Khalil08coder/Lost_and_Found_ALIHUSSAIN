import sqlite3

conn = sqlite3.connect('lost_and_found.db')
cursor = conn.cursor()

cursor.execute('''
CREATE TABLE IF NOT EXISTS users (
    studentID TEXT PRIMARY KEY,
    password TEXT NOT NULL
)''')

cursor.execute('''
INSERT INTO users (studentID, password) VALUES
    ('22000', 'password123'),
    ('23456', 'mypassword'),
    ('23567', 'pass111'),
    ('22222', 'pass222')
''')

conn.commit()
conn.close()
