import random

#? ===================================   CLASSES   ===================================
class BankAccount:
    master_pin = 12345      #! Only Manager knows this
    def __init__(self, name, username, opening_balance, pin):
        self.name = name
        self.username = username
        self.account_number = round(random.random() * 10000000000)
        self.account_locked = False
        self.balance = opening_balance
        self.pin = pin
        self.transaction_history = []
        self.transaction_history.append(f"Opening Balance: {self.balance} INR.")

class Login:
    def __init__(self, account_list):
        self.all_account_list = account_list
    
    def unlock_account(self, the_item):
        self.the_account = the_item
        try:
            the_master_pin = int(input("Account Locked. Enter Master PIN."))
            if the_master_pin == BankAccount.master_pin:
                self.the_account.account_locked = False
                print("Account Unlocked. You Can Login Now.")
                return False
        except ValueError:
            helper_invalid_input()
            return False

    def login(self):
        if len(self.all_account_list) == 0:
            print("No Account has been created as of now.")
            return False
        else:
            user_name = input("Enter Username: ")
            for item in self.all_account_list:
                if user_name == item.username:
                    if item.account_locked:
                        self.unlock_account(item)
                    else:
                        max_try = 3
                        while True:
                            try:
                                user_pin = int(input("Enter PIN: "))
                                max_try -= 1
                                if user_pin == item.pin:
                                    item.account_locked = False
                                    print("SUCCESS")
                                    print(f"Here is your account number: {item.account_number}")
                                    return item
                                else:
                                    print("Sorry PIN mismatch.")
                                    if max_try == 0:
                                        item.account_locked = True
                                        print("ACCOUNT LOCKED")
                                        return False
                            except ValueError:
                                max_try -= 1
                                print("Invalid Input.")
                                if max_try == 0:
                                    item.account_locked = True
                                    print("ACCOUNT LOCKED")
                                    return False
            print("Sorry this Username doesn't exist.")
            return False

class AccountFeatures:
    def __init__(self, the_account):
        self.account = the_account

    def deposit(self):
        try:
            deposit_amount = int(input("Enter Amount: "))
            self.account.balance += deposit_amount
            self.account.transaction_history.append(f"Deposit: {deposit_amount} INR | Final Balance: {self.account.balance} INR")
            print("Deposit Done")
        except ValueError:
            helper_invalid_input()

    def withdraw(self):
        try:
            withdraw_amount = int(input("Enter Amount: "))
            if withdraw_amount <= self.account.balance:
                self.account.balance -= withdraw_amount
                self.account.transaction_history.append(f"Withdraw: {withdraw_amount} INR | Final Balance: {self.account.balance} INR")
                print("Withdraw Done")
            else:
                print("Insufficient Balance. Operation failed.")
        except ValueError:
            helper_invalid_input()

    def check_bal(self):
        print(f"Account Balance: INR {self.account.balance}/-")

    def display_ac_info(self):
        print(f'''
Username: {self.account.username}
Account Holders Name: {self.account.name}
Account Number: {self.account.account_number}
Account Balance: {self.account.balance}/-
''')

    def transaction_history(self):
        for record in self.account.transaction_history:
            print(record)
    
    def calculate_interest(self):
        print("We Provide Simple Interest of 4% per year.")
        interest = round(self.account.balance * (4 / 100))
        print(f"INR {interest} /- generated till now.")

#? ===================================   FUNCTIONS USED INSIDE MAIN   ===================================

def display_board_and_input():
    print("Welcome to OOP Bank. Please choose one option from below.")
    try:
        user_choice = int(input('''
1. Login
2. Open Account
3. Close Application
'''))
    except ValueError:
        helper_invalid_input()
        return True, None
    if user_choice == 3:
        print("Thanks for using OOP Bank.")
        return False, None
    elif user_choice in [1, 2]:
        return True, user_choice
    else:
        helper_invalid_input()
        return True, None

def collect_user_details(whole_list):
    name = input("Enter your name: ").title()
    username = input("Create username: ").lower()
    all_usernames = []
    for account in whole_list:
        all_usernames.append(account.username)
    if username in all_usernames:
        print("Username already taken.")
    else:
        try:
            pin = int(input("Set PIN: "))
            confirm_pin = int(input("Confirm PIN: "))
            if pin == confirm_pin:
                opening_bal = int(input("Deposit initial amount (Min Rs: 500/-): "))
                if opening_bal >= 500:
                    print("Account Open Successful.")
                    return [name, username, opening_bal, pin]
                else:
                    print("At least Rs: 500/- is needed.")
                    return False
            else:
                print("PIN Mismatch. Try Again.")
                return None
        except ValueError:
            print("Sorry thats an Invalid Input.")
            return None

def after_login_display_and_user_input():
    try:
        user_choice = int(input('''
Choose services from below
1. Deposit
2. Withdraw
3. Check Balance
4. Display Account Info
5. Transaction History
6. Calculate Interest
7. Logout
'''))
        if user_choice == 7:
            print("Logged Out Successfully.")
            return False, None
        elif user_choice in [1, 2, 3, 4, 5, 6]:
            return True, user_choice
        else:
            helper_invalid_input()
            return True, None
    except ValueError:
        helper_invalid_input()
        return True, None


def helper_invalid_input():
    print("That's an Invalid Input. Try Again.")

#? ===================================   MAPPER AND MAIN   ===================================

def command_mapper(the_command, features):
    saved_commands = {
        1: features.deposit,
        2: features.withdraw,
        3: features.check_bal,
        4: features.display_ac_info,
        5: features.transaction_history,
        6: features.calculate_interest
    }
    if the_command in saved_commands:
        saved_commands[the_command]()

def main():
    bank_account_list = []
    the_login = Login(bank_account_list)
    while True:
        program_stopper, user_input = display_board_and_input()
        if not program_stopper:
            break
        elif user_input == 1:
            customers_account = the_login.login()
            if customers_account:
                all_features = AccountFeatures(customers_account)
                while True:
                    logout, user_command = after_login_display_and_user_input()
                    if not logout:
                        break
                    else:
                        command_mapper(user_command, all_features)
        elif user_input == 2:
            account_details = collect_user_details(bank_account_list)
            if account_details != None:
                bank_account_list.append(BankAccount(account_details[0], account_details[1], account_details[2], account_details[3]))

main()
