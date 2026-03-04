import sqlite3
import matplotlib.pyplot as plt

conn = sqlite3.connect("voting.db")
cursor = conn.cursor()

cursor.execute("SELECT name, votes FROM candidates")
data = cursor.fetchall()

names = []
votes = []

print("\nVoting Results")
print("----------------")

for row in data:
    print(row[0], ":", row[1], "votes")
    names.append(row[0])
    votes.append(row[1])

# Find winner
max_votes = max(votes)
winner_index = votes.index(max_votes)
winner = names[winner_index]

print("\nWinner of the Election:", winner)
print("Total Votes:", max_votes)

# Show bar graph
plt.bar(names, votes)
plt.title("Election Results")
plt.xlabel("Candidates")
plt.ylabel("Votes")

plt.show()

conn.close()