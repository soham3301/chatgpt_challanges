
#? Important Note:- Displaying Password is not good practice. Here it should be considered as equivalent of sending the customer id, pass to customers email

class Display:
    def __init__(self):
        self.name = "Display"

    def the_first_screen(self):
        print('''
1. Login
2. Create Account
0. Exit
''')

#?  ==================== CREATE ACCOUNT DISPLAYS =======================

    def account_creation_rules(self):
        print('''
1. Age should be greater than 18
2. Minimum Deposit should be at least Rs:- 500/-
''')

    def enter_name(self):
        print("Enter Your Name: ")

    def enter_age(self):
        print("Enter Your Age: ")

    def age_problem(self):
        print("You must be 18 years of age to open a bank account.")

    def enter_email(self):
        print("Enter Your eMail ID: ")

    def email_already_exist(self, email):
        print(f"This email: {email} already exist.")

    def email_format_problem(self):
        print("An email should be like abc@something.com etc etc")

    def enter_mobile_number(self):
        print("Enter Mobile Number: ")

    def mobile_already_exist(self, mobile):
        print(f"This mobile number: {mobile} already exist.")

    def mobile_format_problem(self):
        print("Mobile Number should be 10 digits long")

    def enter_first_deposit(self):
        print("Enter First Deposit: ")

    def deposit_amount_problem(self):
        print("Your first deposit should not be less than Rs: 500/-")

    def ac_open_successfull(self, cust_id, cust_pass):
        #? Note:- The system should send the id and pass to the customer's email id. Security Bug
        print(f'''
=== Your Account Open is succesfull ===
Here are your credentials
Customer ID:    {cust_id}
Password:       {cust_pass}
Use them for login
''')
    
    def ac_open_failed(self):
        print("Your Account Open Failed")

#?  ==================== BEFORE LOGIN DISPLAYS =======================

    def enter_customer_id(self):
        print("Enter Customer ID")

    def id_not_exist(self):
        print("This Customer ID doesn't exist")

    def enter_password(self, chance):
        print(f"Enter Password | You have {chance} chances left")

    def login_failed(self):
        print("Account Login Failed")

#?  ==================== AFTER LOGIN DISPLAYS =======================

    def welcome_screen(self, cust_name, ac_no):
        print(f"\nWelcome {cust_name} | Account Number: {ac_no}")

    def after_login_activity_screen(self):
        print('''
1. Deposit
2. Withdraw
3. Transfer
4. Check Balance
5. Show Transaction History
6. Change Password
7. Show Account Details
8. Show Customer Details
9. Get Loan
0. Exit
''')

    def logged_out(self):
        print("Logged Out")

    def enter_amount(self):
        print("Enter Amount")

    def show_balance(self, balance):
        print(f"Your Account Balance is Rs:- {balance}/-")

    def deposit_successfull(self, amount):
        print(f"Your deposit of Rs:- {amount}/- has been successfull")

    def withdraw_successfull(self, amount):
        print(f"Your withdraw of Rs:- {amount} has been successfull")

    def enter_recepients_account_number(self):
        print("Enter Recepients Account Number")

    def transaction_successfull(self, amount, to_number):
        print(f"Rs:- {amount} has been sent from your account to {to_number}")

    def account_not_exist(self, to_ac):
        print(f"This Account bearing Number {to_ac} does not exist")

    def insufficient_balance(self):
        print("Insufficient Balance. Transaction Cancelled")

    def enter_old_password(self):
        print("Enter Your Old Password")

    def enter_new_password(self):
        print("Enter New Password")

    def confirm_password(self):
        print("Enter the same Password again")

    def password_doesnot_match(self):
        print("Password doesn't match.")

    def pass_changed(self):
        print("Your Password has successfully changed")









#?  ==================== GENERIC DISPLAYS =======================

    def comfirm_amount(self, amount, tran_type):
        print(f"You are about to {tran_type} Rs:- {amount}/-. To Confirm type 'Y'.")

    def transaction_unsuccessfull(self, tran_type):
        print(f"The {tran_type} was unsuccessfull")

    def transaction_cancelled(self):
        print("The Transaction has been cancelled.")

    def account_locked(self):
        print("Your Account is Locked | Contact Manager to Unlock Account")

    def invalid_input(self):
        print("Invalid Input")

    def incorrect_password(self):
        print("Incorrect Password")
    
    def thanks_exit_screen(self):
        print("Thanks for using our services")