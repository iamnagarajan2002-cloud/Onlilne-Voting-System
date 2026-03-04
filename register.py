import sqlite3

name = input("Enter your name: ")
voter_id = input("Enter voter ID: ")
password = input("Enter password: ")

conn = sqlite3.connect("voting.db")
cursor = conn.cursor()

cursor.execute(
"INSERT INTO voters(name,voter_id,password,voted) VALUES(?,?,?,?)",
(name, voter_id, password, "No")
)

conn.commit()
conn.close()

print("Registration successful")