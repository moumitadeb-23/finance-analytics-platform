import sqlite3
import os

# Path to finance.db
db_path = os.path.join(os.path.dirname(__file__), "..", "finance.db")

# Connect to database
conn = sqlite3.connect(db_path)

cursor = conn.cursor()

# Read schema.sql
schema_path = os.path.join(os.path.dirname(__file__), "schema.sql")

with open(schema_path, "r") as file:
    cursor.executescript(file.read())

conn.commit()
conn.close()

print("Database Created Successfully!")