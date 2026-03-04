import sqlite3

voter_id = input("Enter your voter ID: ")

conn = sqlite3.connect("voting.db")
cursor = conn.cursor()

cursor.execute("SELECT voted FROM voters WHERE voter_id=?", (voter_id,))
status = cursor.fetchone()

if status[0] == "Yes":
    print("You have already voted")
else:
    print("1. Candidate A")
    print("2. Candidate B")
    print("3. Candidate C")

    choice = int(input("Select candidate number: "))

    cursor.execute(
        "UPDATE candidates SET votes = votes + 1 WHERE id=?",
        (choice,)
    )

    cursor.execute(
        "UPDATE voters SET voted='Yes' WHERE voter_id=?",
        (voter_id,)
    )

    conn.commit()

    print("Vote recorded successfully")

conn.close()