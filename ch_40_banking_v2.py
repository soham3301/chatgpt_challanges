accounts = {
    "Soham":{
        "pin":1234,
        "balance":5000,
        "isLocked": False,
        "userOnline": False,
    },
    "Rahul":{
        "pin":4567,
        "balance":12000,
        "isLocked": False,
        "userOnline": False,
    },
    "Amitabh":{
        "pin":9436,
        "balance":57000,
        "isLocked": False,
        "userOnline": False,
    }
}

transfer_logbook = {}

#?=========================================  BEFORE LOGIN  ====================================================
def login_display_and_user_input():
    try:
        user_choice = int(input('''
1. Login
2. Open Account
3. Close Application
'''))
        if user_choice == 3:
            print("Thanks for using Banking V2.")
            return False, None
        elif user_choice in [1, 2]:
            return True, user_choice
        else:
            please_choose_number()
            return True, None
    except ValueError:
        print("Invalid Input | Closing Application.")
        return False, None

def login():
    max_login_attempt = 3
    username = getting_username()
    for _ in range(max_login_attempt):
        if username in accounts:
            pin = getting_pin()
            if not accounts[username]["isLocked"]:
                if accounts[username]["pin"] == pin:
                    print("Login Successful")
                    user_online_true(username)
                    welcome_greet()
                    record_initializer(username)
                    after_login_main()
                    user_online_false(username)
                    break
                else:
                    max_login_attempt -= 1
                    print(f"Wrong PIN. Attempts Left {max_login_attempt}.")
            else:
                print("Sorry Account is LOCKED now. Can't Login.")
                break
        else:
            user_not_exist()
            break
    if max_login_attempt == 0:
        accounts[username]["isLocked"] = True
        print("Account LOCKED for safety")

def open_account():
    print("Please Fill Up all the section carefully.")
    username = getting_username()
    if username not in accounts:
        pin = pin_setup()
        if pin != None:
            add_money = helper_add_amount()
            if add_money != None:
                accounts[username] = {
                    "pin":pin,
                    "balance":add_money,
                    "isLocked": False,
                    "userOnline": False
                }
                record_initializer(username)
                user_consent = input("Account Opened Successfully. Want to Login? Y / N\n").lower()
                if user_consent == "y":
                    login()                 #!  <<<---  User needs to enter username again. For security purpose. Not a Bug.
    else:
        print("This username is already taken. Choose another username.")

#?=========================================  AFTER LOGIN  ====================================================

def after_login_display():
    try:
        user_choice = int(input('''
1. Deposit
2. Withdraw
3. Transfer Money
4. Balance Check
5. Transaction History
6. Logout
'''))
        if user_choice == 6:
            print("Successfully Logged Out.")
            return False, None
        elif user_choice in [1, 2, 3, 4, 5]:
            return True, user_choice
        else:
            please_choose_number()
            return True, None
    except ValueError:
        print("Kindly Enter a numerical Value from above.")
        return True, None

def deposit():
    money_for_deposit = helper_add_amount()
    if money_for_deposit != None:
        username = user_online_checker()
        accounts[username]["balance"] += money_for_deposit
        deposit_withdraw_recorder(username, "Deposit", f"+{money_for_deposit}")
        print("Amount Deposited.")
    else:
        please_enter_valid_amount()

def withdraw():
    money_for_withdraw = helper_add_amount()
    if money_for_withdraw != None:
        username = user_online_checker()
        if accounts[username]["balance"] < money_for_withdraw:
            print("Insufficient Balance. Can't Proceed.")
        else:
            accounts[username]["balance"] -= money_for_withdraw
            deposit_withdraw_recorder(username, "Withdraw", f"-{money_for_withdraw}")
            print("Withdrawal Successful.")
    else:
        please_enter_valid_amount()

def money_transfer():
    print("Kindly Enter the Username of recepients account.")
    target_username = getting_username()
    if target_username in accounts:
        money_for_transfer = helper_add_amount()
        username = user_online_checker()
        if username == target_username:
            print("Can't Transfer Money to Yourself.")
        elif money_for_transfer != None:
                helper_money_transfer(username, target_username, money_for_transfer)
        else:
            please_enter_valid_amount()
    else:
        user_not_exist()

def balance_check():
    username = user_online_checker()
    print(f"Balance: {accounts[username]["balance"]}")

def transaction_history():
    username = user_online_checker()
    closing_bal_recorder(username)
    print(f"Opening Bal: Rs: {transfer_logbook[username]["Opening Balance"]}/- INR")
    if len(transfer_logbook[username]["Transaction History"]) > 0:
        for items in transfer_logbook[username]["Transaction History"]:
            for key, value in items.items():
                print(f"{key}: {value}/- INR")
    print(f"Current Bal: Rs: {transfer_logbook[username]["Current Balance"]}/- INR")

#*=========================================  HELPERS  ========================================================
def getting_username():
    return input("Enter Username: ")

def getting_pin():
    try:
        pin = int(input("Enter PIN: "))
        return pin
    except ValueError:
        print("Invalid Input. Enter Numerical Values only as PIN")
        return None

def pin_setup():
    try:
        setup_pin = int(input("Enter PIN: "))
        confirm_pin = int(input("Enter PIN Again: "))
        if setup_pin == confirm_pin:
            return setup_pin
        else:
            print("PIN didn't match.")
            return None
    except ValueError:
        print("Invalid Input. Enter Numerical Values only as PIN")
        return None

def helper_add_amount():
    try:
        money = int(input("Enter Amount: "))
        if money >= 0:
            return round(money)
        else:
            print("Negative amount won't be accepted.")
            return None
    except ValueError:
        print("Invalid Input")
        return None

def helper_money_transfer(from_user, to_user, amount):
    if accounts[from_user]["balance"] >= amount:
        deposit_withdraw_recorder(to_user, f"From {from_user}", f"+{amount}")
        deposit_withdraw_recorder(from_user, f"To {to_user}", f"-{amount}")
        accounts[from_user]["balance"] -= amount
        accounts[to_user]["balance"] += amount
        print(f"Rs: {amount}/- successfully transferred to {to_user}s account.")

def opening_bal_recorder(user_name):
    if not user_name in transfer_logbook:
        opening_balance = accounts[user_name]["balance"]
        transfer_logbook[user_name] = {
            "Opening Balance": opening_balance
        }

def closing_bal_recorder(user_name):
    transfer_logbook[user_name]["Current Balance"] = accounts[user_name]["balance"]

def transaction_history_recorder(user_name):
    if not user_name in transfer_logbook:
        transfer_logbook[user_name]["Transaction History"] = []
    elif len(transfer_logbook[user_name]) <= 2:
        transfer_logbook[user_name]["Transaction History"] = []

def deposit_withdraw_recorder(user_name, deposit_or_withdraw, amount):
    if user_name in transfer_logbook:
        transfer_logbook[user_name]["Transaction History"].append({
            deposit_or_withdraw:amount
        })
    else:
        record_initializer(user_name)
        transfer_logbook[user_name]["Transaction History"].append({
            deposit_or_withdraw:amount
        })

def record_initializer(name_of_user):
    opening_bal_recorder(name_of_user)
    closing_bal_recorder(name_of_user)
    transaction_history_recorder(name_of_user)

def please_enter_valid_amount():
    return print("Please enter a valid amount.")

def user_not_exist():
    return print("This Username doesn't exist. Try another Username.")

def please_choose_number():
    return print("Please Choose a number from above.")

def welcome_greet():
    print("                         === WELCOME TO BANK v2 ===")

def user_online_true(account_holder):
    accounts[account_holder]["userOnline"] = True

def user_online_false(account_holder):
    accounts[account_holder]["userOnline"] = False

def display_username_all_time():
    username = user_online_checker()
    print(f"                          | Logged in as: {username} |")

def user_online_checker():
    for username, details in accounts.items():
        if details["userOnline"]:
            return username

#!=====================================   MAPPERS AND MAIN   =================================================

def mapping_user_input_from_login_page(user_choice):
    saved_functions_01 = {
        1: login,
        2: open_account,
    }
    if user_choice in saved_functions_01:
        return saved_functions_01[user_choice]()

def mapping_user_input_from_after_login(user_choice):
    saved_functions_02 = {
        1: deposit,
        2: withdraw,
        3: money_transfer,
        4: balance_check,
        5: transaction_history,
    }
    if user_choice in saved_functions_02:
        saved_functions_02[user_choice]()

def after_login_main():
    isLoggedIn = True
    while isLoggedIn:
        display_username_all_time()
        isLoggedIn, user_input = after_login_display()
        mapping_user_input_from_after_login(user_input)

def main():
    app_running = True
    while app_running:
        app_running, user_input = login_display_and_user_input()
        mapping_user_input_from_login_page(user_input)

main()