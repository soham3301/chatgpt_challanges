initial_balance = 5000
# user_input = 0

def menu():
    user_input = int(input("""
===== ATM =====

1. Check Balance
2. Deposit
3. Withdraw
4. Exit
"""))
    return user_input

def check_balance():
    print(f"Your Account Balance is: {initial_balance}")

def deposit():
    deposit_amount = int(input("Enter Amount: "))
    global initial_balance
    initial_balance += deposit_amount

def withdrawal():
    withdraw_amount = int(input("Enter Amount: "))
    global initial_balance
    if withdraw_amount <= initial_balance:
        initial_balance -= withdraw_amount
    else:
        print("Insufficient Balance.")

while True:
    user_input = menu()
    if user_input == 1:
        check_balance()
    elif user_input == 2:
        deposit()
    elif user_input == 3:
        withdrawal()
    elif user_input == 4:
        print("Thank you for using our ATM")
        break
    else:
        print("Invalid Choice")


