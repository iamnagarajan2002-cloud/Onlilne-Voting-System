import os

print("ONLINE VOTING SYSTEM")
print("1. Register")
print("2. Login")
print("3. Vote")
print("4. View Results")

choice = input("Enter your choice: ")

if choice == "1":
    os.system("python register.py")

elif choice == "2":
    os.system("python login.py")

elif choice == "3":
    os.system("python vote.py")

elif choice == "4":
    os.system("python result.py")

else:
    print("Invalid choice")