accounts = {
    "Soham":{
        "pin":1234,
        "balance":5000
    },
    "Rahul":{
        "pin":4567,
        "balance":12000
    },
    "Amitabh":{
        "pin":9436,
        "balance":57000,
    }
}

#? =========================== THE DISPLAY BOARD FUNCTION ===========================

def display_board_and_user_input():
    try:
        user_choice = int(input('''
1. Login
2. Deposit
3. Withdraw
4. Transfer Money
5. Balance Check
6. Transaction History
7. Logout
'''))
        if user_choice == 7:
            print("Thanks for using Banking CLI.")
            return False, None
        elif user_choice in [1, 2, 3, 4, 5, 6]:
            return True, user_choice
        else:
            print("Kindly choose numbers from above.")
            return True, None
    except ValueError:
        print("Invalid Input | Closing Applicaiton.")
        return False, None

#? =========================== THE MASTER FUNCTIONS START ===========================

def login():
    max_login_attempt = 3
    username = input("Enter Username: ").title()
    if username in accounts:
        try:
            pin = int(input("Enter PIN"))
        except ValueError:
            print("PIN contains only numbers. Kindly enter numerical values.")
            return False
        for name, details in accounts.items():
            if username == name:
                if pin == accounts[username]["pin"]:
                    print("Login Successful.")
                    return True
                else:
                    print("Wrong PIN.")
                    return False
    else:
        print("This Username doesn't exist.")
        return False

def deposit():
    print("Deposit Successful.")

def withdraw():
    print("Withdraw Successful.")

def transfer_money():
    print("Money Transfer Successful.")

def balance_check():
    print("Balance Check Successful.")

def transaction_history():
    print("Transaction history Showed Successfully.")

#? =========================== THE HELPER FUNCTION START ===========================

def want_to_login():
    return input("You need to login first. Type 'Y' for Yes or 'N' for No\n").lower()

def login_failure():
    print("Login Unsuccessful.")

#? =========================== THE MAPPER FUNCTION START ===========================

def mapping_user_input(user_choice, login_status):
    saved_functions = {
        1: login,
        2: deposit,
        3: withdraw,
        4: transfer_money,
        5: balance_check,
        6: transaction_history,
    }
    if user_choice == 1:
        login_status = saved_functions[user_choice]()
        return login_status
    elif user_choice in saved_functions and login_status:
        saved_functions[user_choice]()
        return True
    else:
        print("You need to login first.")
        return False

#! =========================== THE MAIN FUNCTION START ===========================

def main():
    login_situation = False
    program_running = True
    while program_running:
            program_running, user_input = display_board_and_user_input()
            login_situation = mapping_user_input(user_input, login_situation)

main()