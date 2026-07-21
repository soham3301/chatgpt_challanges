
#! NOTE:- Mobile phone's inbox should not be accessed from ATM Machine. However, I am checking whether I can send OTP to user's mobile to unlock user account if it gets locked.

import random

logo = '''
 ▗▄▖  ▗▄▖ ▗▄▄▖      ▗▄▖▗▄▄▄▖▗▖  ▗▖
▐▌ ▐▌▐▌ ▐▌▐▌ ▐▌    ▐▌ ▐▌ █  ▐▛▚▞▜▌
▐▌ ▐▌▐▌ ▐▌▐▛▀▘     ▐▛▀▜▌ █  ▐▌  ▐▌
▝▚▄▞▘▝▚▄▞▘▐▌       ▐▌ ▐▌ █  ▐▌  ▐▌
'''

class Account:
    def __init__(self, name, mobile_number, opening_balance, pin):
        self.name = name
        self.mobile_no = mobile_number
        self.balance = opening_balance
        self.pin = pin
        self.account_number = round(random.random() * 1000000000)
        self.is_locked = False
        self.otp = 0
        self.transaction_list = []

class Mobile:
    def __init__(self, number, otp):
        self.number = number
        self.inbox = otp
    
    def display_inbox(self, mobile_no):
        if self.number == mobile_no:
            return self.inbox
        else:
            return None
    
    def otp_clearer(self):
        self.inbox = 0


class ATM:
    def __init__(self, ac_list):
        self.account_list = ac_list
    
    def find_account(self, mobile_no):
        for account in self.account_list:
            if account.mobile_no == mobile_no:
                return account
        return None
    
    def unlock_account(self, mobile_number, otp):
        the_account = self.find_account(mobile_number)
        if the_account:
            if the_account.otp == otp:
                the_account.is_locked = False
                return True
            else:
                return False
        else:
            return False
    
    def activate_transaction_list(self, the_ac):
        the_ac.transaction_list.append({
            "Opening Bal":the_ac.balance
        })
    
    def deposit_recorder(self, the_ac, the_amount):
        the_ac.transaction_list.append({
            "Deposit":the_amount
        })
    
    def withdraw_recorder(self, the_ac, the_amount):
        the_ac.transaction_list.append({
            "Withdraw":the_amount
        })


    def login(self, mobile_number, pin, attempt):
        the_account = self.find_account(mobile_number)
        if the_account:
            if the_account.is_locked:
                return False, Mobile(the_account.mobile_no, 0)
            else:               
                if the_account.mobile_no == mobile_number and the_account.pin == pin:
                    self.activate_transaction_list(the_account)
                    return True, None
                else:
                    if attempt == 0:
                        the_account.is_locked = True
                        the_otp = round(random.random() * 1000000)
                        the_account.otp += the_otp
                        the_inbox = Mobile(the_account.mobile_no, the_otp)
                        return False, the_inbox
                    else:
                        return False, None
        else:
            return False, None
    
    def deposit(self, amount, mobile_number):
        the_account = self.find_account(mobile_number)
        if the_account and amount:
            self.deposit_recorder(the_account, amount)
            the_account.balance += amount
            return True
        else:
            return False
    
    def withdraw(self, amount, mobile_number):
        the_account = self.find_account(mobile_number)
        if the_account and amount:
            if the_account.balance >= amount:
                self.withdraw_recorder(the_account, amount)
                the_account.balance -= amount
                return True
            else:
                return False
        else:
            return False

    def transfer(self, the_amount, the_ac_no, mobile_number):
        my_account = self.find_account(mobile_number)
        if my_account and the_amount and the_ac_no:
            if my_account.balance >= the_amount:
                for account in self.account_list:
                    if account.account_number == the_ac_no and account.name != my_account.name:
                        self.activate_transaction_list(account)
                        account.balance += the_amount
                        my_account.balance -= the_amount
                        return True
                return False
            else:
                return False
        else:
            return False
    
    def balance_check(self, mobile_number):
        the_account = self.find_account(mobile_number)
        return f"The Account Balance is: INR {the_account.balance} /-"
    
    def transaction_history(self, mobile_number):
        the_account = self.find_account(mobile_number)
        return the_account.transaction_list

def display_board():
    print('''
1. Login
2. Mobile Inbox
3. Unlock Existing Account
4. Open a New Bank Account
''')

def user_input():
    try:
        user_choice = int(input("Choose from above: "))
        if user_choice == 0:
            return False, None
        elif user_choice in [1, 2, 3, 4]:
            return True, user_choice
        else:
            helper_invalid_input()
            return True, None
    except ValueError:
        helper_invalid_input()
        return True, None

def helper_invalid_input():
    print("Invalid Input")

def get_mobile_number():
    try:
        mobile_no = int(input("Enter Mobile No: "))
        return mobile_no
    except ValueError:
        helper_invalid_input()
        return None

def get_pin():
    try:
        pin = int(input("Enter PIN: "))
        return pin
    except ValueError:
        helper_invalid_input()
        return None

def get_otp():
    try:
        otp = int(input("Enter OTP: "))
        return otp
    except ValueError:
        helper_invalid_input()
        return None

def after_login_display():
    print(f'''
1. Deposit
2. Withdraw
3. Transfer
4. Balance Check
5. Transaction History
6. Logout
''')

def after_login_user_command():
    try:
        user_choice = int(input("Enter from above: "))
        if user_choice == 6:
            return False, None
        elif user_choice in [1, 2, 3, 4, 5]:
            return True, user_choice
        else:
            helper_invalid_input()
            return True, None
    except ValueError:
        helper_invalid_input()
        return True, None

def get_amount():
    try:
        amount = abs(round(int(input("Enter Amount: "))))
        return amount
    except ValueError:
        helper_invalid_input()
        return None

def get_ac_no(the_atm):
    #! In real world, user needs to know the ac no of another user to transfer money.
    for account in the_atm.account_list:
        print(f"{account.account_number} -- {account.name}")
    try:
        ac_no = abs(round(int(input("Enter Recepient's Account Number: "))))
        amount = get_amount()
        return ac_no, amount
    except ValueError:
        helper_invalid_input()
        return None

def command_mapper(user_choice, atm, mobile_no):
    atm_functions = {
        1: atm.deposit,
        2: atm.withdraw,
        3: atm.transfer,
        4: atm.balance_check,
        5: atm.transaction_history,
    }
    print_signals = {
        "success": {
            1: "Deposit Done",
            2: "Withdraw Done",
            3: "Transfer Done",
        },
        "failure": {
            1: "Deposit Failed",
            2: "Withdraw Failed",
            3: "Transfer Failed",
        }
    }
    if user_choice in [1, 2]:
        the_amount = get_amount()
        if the_amount:
            if atm_functions[user_choice](the_amount, mobile_no):
                print(f"{print_signals["success"][user_choice]}")
            else:
                print(f"{print_signals["failure"][user_choice]}")
        else:
            helper_invalid_input()
    elif user_choice == 3:
        ac_no, amount = get_ac_no(atm)
        if amount and ac_no:
            if atm_functions[user_choice](amount, ac_no, mobile_no):
                print(f"{print_signals["success"][user_choice]}")
            else:
                print(f"{print_signals["failure"][user_choice]}")
        else:
            helper_invalid_input()
    elif user_choice in [4, 5]:
        the_report = atm_functions[user_choice](mobile_no)
        print(the_report)
    else:
        helper_invalid_input()

def main():
    demo_account_list = [
        Account("Soham", 8787692757, 1200, 1234),
        Account("Amitabh", 9436221475, 800, 1221),
        Account("Akash", 8131889475, 5000, 4521),
        Account("Debasish", 7085009823, 600, 9989),
    ]
    oop_atm = ATM(demo_account_list)
    print(logo)
    while True:
        display_board()
        atm_running, user_choice = user_input()
        if not atm_running:
            break
        elif user_choice == 1:
            mobile_no = get_mobile_number()
            login_attempt = 3
            if mobile_no:
                while login_attempt >= 0:
                    the_pin = get_pin()
                    login_attempt -= 1
                    login_condition, the_inbox = oop_atm.login(mobile_no, the_pin, login_attempt)
                    if login_condition:
                        print("Logged In")
                        login_attempt = -1
                        while True:
                            after_login_display()
                            is_logged_in, user_command = after_login_user_command()
                            if not is_logged_in:
                                print("Successfully Logged Out.")
                                break
                            elif user_choice:
                                command_mapper(user_command, oop_atm, mobile_no)
                            else:
                                continue
                    else:
                        if login_attempt == 0:
                            print("Account Locked. Check OTP for Unlock.")
                            print("WARNING: Attempting Login in a Locked Account Will Override the OTP.")
                            break
                        print(f"Login Failed | Attempts Remain: {login_attempt}")
        elif user_choice == 2:
            if the_inbox:
                mobile_number = get_mobile_number()
                the_otp = the_inbox.display_inbox(mobile_number)
                print(f"Here is your OTP: {the_otp}")
            else:
                print("Your Account is not Locked.")
        elif user_choice == 3:
            if the_inbox:
                mob_no = get_mobile_number()
                otp = get_otp()
                if oop_atm.unlock_account(mob_no, otp):
                    print("Account Unlocked")
                    the_inbox.otp_clearer()
                else:
                    helper_invalid_input()
            else:
                print("Your Account is not Locked.")
        elif user_choice == 4:
            ...
        else:
            helper_invalid_input()

main()
