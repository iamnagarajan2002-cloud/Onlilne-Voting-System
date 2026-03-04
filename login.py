import sqlite3

print("=== Voter Login ===")

voter_id = input("Enter Voter ID: ")
password = input("Enter Password: ")

conn = sqlite3.connect("voting.db")
cursor = conn.cursor()

cursor.execute(
    "SELECT * FROM voters WHERE voter_id=? AND password=?",
    (voter_id, password)
)

user = cursor.fetchone()

if user:
    print("Login Successful")
else:
    print("Invalid Voter ID or Password")

conn.close()