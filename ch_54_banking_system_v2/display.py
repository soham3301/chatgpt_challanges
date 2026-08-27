
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
        #? Note:- The system should send the id and pass to the customer's email id. Not display as plain text. Security Bug
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

    def account_locked(self):
        print("Your Account is Locked | Contact Manager to Unlock Account")

#?  ==================== CUSTOMER AFTER LOGIN DISPLAYS =======================

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
9. Apply for Loan
10. Show Loan Status
11. Repay Loan
12. Request for Loan Closure
0. Exit
''')

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

    def show_transactions(self):
        print("DEPOSIT WITHDRAW SENT RECEIVED BALANCE | TRAN ID")

    def tran_show_deposits(self, amount, balance, the_id):
        print(f"+{amount}/- ________ ____ ________ Rs: {balance}/- | {the_id}")

    def tran_show_withdraws(self, amount, balance, the_id):
        print(f"_______ -{amount}/- ____ ________ Rs: {balance}/- | {the_id}")

    def tran_show_sent(self, amount, balance, the_id, to_ac):
        print(f"_______ ________ -{amount} ________ Rs: {balance}/- | {the_id} | To Account: {to_ac}")

    def tran_show_received(self, amount, balance, the_id, from_ac):
        print(f"_______ ________ ____ +{amount} Rs: {balance}/- | {the_id} | From Account: {from_ac}")

    def show_final_balance(self, balance):
        print(f"Your Final Balance is Rs: {balance}/-")

    def show_ac_info(self, number, balance, int_gained, cust_id, total_trans):
        print(f'''
Account Number: {number}
Account Balance: {balance}/-
Interest Gained: {int_gained}/-
Customer ID: {cust_id}
Total number of Transactions: {total_trans}
''')

#! NOTE:- Displaying Password in plain text is not secured.
    def show_customer_info(self, name, age, email, mobile, ac_no, loan_ac_no, cust_id, password):
        print(f'''
Name: {name}
Age: {age}
email ID: {email}
Mobile Number: {mobile}
Account Number: {ac_no}
Loan Account Number: {loan_ac_no}
Customer ID: {cust_id}
Password: {password}
''')


#?  ==================== LOAN DISPLAYS =======================

    def loan_application_started(self):
        print("Your Loan Application has been started | Fill all the inputs carefully.")

    def how_much_loan_you_need(self):
        print("Please Enter How Much Amount you need as Loan")

    def monthly_income(self):
        print("Tell us how much do you earn Monthly")

    def not_eligible_for_loan(self):
        print("Sorry. Currently no Loan offer is available. Try lowering the requested loan amount")

    def show_possible_loans(self, serial_no, loan_amount, repayment_amount, tenure, interest, emi):
        print(f"Serial No: {serial_no}. Loan Amount:- {loan_amount}/- -- Repayment Amount: {repayment_amount} -- Repay in {tenure} Months -- Monthly EMI: {emi} -- Interest Applied: {interest}%")

    def choose_the_loan_number(self):
        print("Choose the serial number for apply. eg: 1, 2, 3 etc etc...")

    def apply_loan_confirmation(self, loan_amount, repayment_amount, tenure, interest, emi):
        print(f'''
You are about to apply for a loan of Rs: {loan_amount}/-
The Monthly EMI would be Rs: {emi}/- and the tenure is {tenure} Months.
Total Repayment Amount would be Rs: {repayment_amount}/- and {interest}% interest is applied

To Confirm this, Type 'Y' for 'YES'
''')

    def loan_applied_successfully(self):
        print("Your Loan Application is successfully applied")

    def loan_application_cancelled(self):
        print("Your Loan Application Process has been cancelled")

    def already_have_loan(self):
        print("You already have an ongoing loan. Close the loan by repaying the remaining amount for further loan request")

    def already_applied(self):
        print("You have already applied for a loan. Kindly wait before applying again.")

    def no_loan_available(self):
        print("You don't have any active loan as of now")

    def show_loan_status(self, status):
        print(status)

    def repay_full_or_only_emi(self, full_amount, emi_amount):
        print(f'''
1. Pay only one EMI.                Rs:- {emi_amount}/-
2. Pay Full Repayment Amount:       Rs:- {full_amount}/-
''')


    def ask_user_to_repay(self, amount, full_or_emi):
        print(f"Want to pay {full_or_emi} of Rs:- {amount}/- ? The amount will be deducted from your Account. Type 'Y' for 'YES'")

    def loan_payment_cancelled(self, emi_or_full):
        print(f"Your {emi_or_full} Procedure has been cancelled")

    def no_pending_emi(self):
        print("You don't have any pending EMI left. You can proceed to Loan Closure Now.")

    def pay_loan_amount(self, amount):
        print(f"Kindly enter the exact amount of Rs:- {amount}/-")

    def wrong_amount_paid(self, paid, emi, emi_or_full):
        print(f"Sorry you paid Rs:- {paid}/- which doesn't match the {emi_or_full} of Rs:- {emi}/- | Transaction Cancelled")

    def emi_payment_successfull(self, unpaid, repay_amt):
        print(f"EMI payment successfull. Now you have {unpaid} EMIs left. Loan remains Rs:- {repay_amt}/-")

    def loan_full_repayment_successfull(self, repay_amt):
        print(f"You re-paid the entire loan successfully. Total Amount Paid Rs:- {repay_amt}/- | You may now initiate the Loan Closure Procedure")
    
    def emis_not_cleared(self, unpaid_emis, unpaid_amount):
        print(f"Can't initiate Loan Closure. You still have {unpaid_emis} pending EMIs worth Rs:- {unpaid_amount}/-")

    def loan_closure_application_submitted(self, loan_ac_no):
        print(f"Your Loan (Loan Account Number: {loan_ac_no}) closure request has been submitted to the Manager. Kindly wait 1 to 2 Business Days for the Loan Closure.")













#?  ==================== MANAGER DISPLAYS =======================

    def enter_managers_password(self):
        print("Enter Password")

    def managers_screen(self):
        print('''
1. Unlock Account
2. Check Pending Loan Applications
3. Approve Loan
4. Reject Loan Application
5. Check Loan Status
6. Close Loan
7. Check Total Available Accounts
8. Check Total Available Customers
9. Change Password
0. Exit
''')

    def show_locked_accounts(self, account_number):
        print(f"Locked Account Number: {account_number}")

    def enter_account_number(self):
        print("Enter a Account Number from above")

    def account_unlocked(self, ac_no):
        print(f"The Account: {ac_no}, has been unlocked successfully")

    def nothing_to_unlock(self):
        print("No Account is Locked as of now.")

    def no_pending_loan_application(self):
        print("No pending Loan Application available for now")
    
    def pending_applications_screen(self):
        print("These are the pending loan applications")

    def view_pending_loan_applications(self, c_id, req_amount, emi, repay_amount):
        print(f"Customer ID: {c_id} | Loan Ammount Requested: {req_amount}/- | Monthly EMI: {emi}/- | Total Repayment Amount: {repay_amount}/-")

    def varify_loan_display(self, name, age, loan_amt, repay_amt, tanure, emi, ac_no, bal, total_trans, income):
        print(f'''
Customer Name:                  {name}
Customer Age:                   {age}
Customer Account Number:        {ac_no}
Current Account Balance:        {bal}/-
Total Transactions Till Now:    {total_trans}
Requested Loan Amount:          {loan_amt}/-
EMI:                            {emi}/-
Monthly Income:                 {income}/-
Total Repayment Amount:         {repay_amt}/-
Loan Tanure (in months):        {tanure}
''')

    def loan_approval_confirmation(self, name, amount):
        print(f"Type 'Y' to CONFIRM the Rs: {amount}/- loan of {name}")

    def loan_approved(self, number):
        print(f"The loan has been approved. Loan Account Nunber: {number}")

    def loan_processing_cancelled(self, name):
        print(f"Loan Application of {name} has been cancelled as of now")













    def no_closing_application_exist(self):
        print("No application has been submitted for loan closure")

    def show_loan_closure_applications(self, loan_ac_no):
        print(f"Application submitted for loan closure. Loan Account Number: {loan_ac_no}")
    
    def choose_loan_number_for_closure(self):
        print("\nChoose a Loan from above for further procedure | Type the exact Loan Account Number below")

    def show_loan_status_by_manager(self, status_loan):
        print(status_loan)

    def close_this_loan_account(self):
        print("Press 'Y' to close this Loan.")

    def loan_account_close_halted(self, loan_ac_no):
        print(f"Closure of the Loan Account ({loan_ac_no}) is Halted. Investigate Further.")

    def loan_closed_successfully(self, loan_ac_no):
        print(f"The Loan ({loan_ac_no}) has been successfully Closed")




#?  ==================== GENERIC DISPLAYS =======================

    def logged_out(self):
        print("Logged Out")

    def confirm_amount(self, amount, tran_type):
        print(f"You are about to {tran_type} Rs:- {amount}/-. To Confirm type 'Y'.")

    def transaction_unsuccessfull(self, tran_type):
        print(f"The {tran_type} was unsuccessfull")

    def transaction_cancelled(self):
        print("The Transaction has been cancelled.")

    def invalid_input(self):
        print("Invalid Input")

    def incorrect_password(self):
        print("Incorrect Password")
    
    def thanks_exit_screen(self):
        print("Thanks for using our services")