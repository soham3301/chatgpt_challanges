chests = ["Gold", "Silver", "Diamond", "Pearl"]

user_input = int(input("Enter a chest number: 0, 1, 2 or 3\n"))

if user_input == 0 or user_input == 1 or user_input == 2 or user_input == 3:
    print(f"You selected chest {user_input}")
    print(f"This chest contains {chests[user_input]}")
else:
    print("Invalid Chest Number")