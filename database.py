import sqlite3

conn = sqlite3.connect("voting.db")
cursor = conn.cursor()

# Voters table
cursor.execute("""
CREATE TABLE IF NOT EXISTS voters(
id INTEGER PRIMARY KEY AUTOINCREMENT,
name TEXT,
voter_id TEXT UNIQUE,
password TEXT,
voted TEXT
)
""")

# Candidates table
cursor.execute("""
CREATE TABLE IF NOT EXISTS candidates(
id INTEGER PRIMARY KEY,
name TEXT,
votes INTEGER
)
""")

# Insert candidates
cursor.execute("INSERT OR IGNORE INTO candidates VALUES (1,'Candidate A',0)")
cursor.execute("INSERT OR IGNORE INTO candidates VALUES (2,'Candidate B',0)")
cursor.execute("INSERT OR IGNORE INTO candidates VALUES (3,'Candidate C',0)")

conn.commit()

print("Database and tables created successfully")

conn.close()