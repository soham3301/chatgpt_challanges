
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
        print("Enter Yuor Name: ")

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
        print(f'''
=== Your Account Open is succesfull ===
Here are your credentials
Customer ID:    {cust_id}
Password:       {cust_pass}
Use them for login
''')
    
    def ac_open_failed(self):
        print("Your Account Open Failed")

#?  ==================== AFTER LOGIN DISPLAYS =======================












#?  ==================== GENERIC DISPLAYS =======================

    def invalid_input(self):
        print("Invalid Input")

    def incorrect_password(self):
        print("Incorrect Password")
    
    def thanks_exit_screen(self):
        print("Thanks for using our services")