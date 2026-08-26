
#? Note:- This total application is for customers. A Manager should use another system, not the same. However, hardcoding password into the application is wrong.
#? Note:- Didn't Focused on login security of Manager. Here I introduced manager just to approve loans and unlock accounts.
#? Note:- Bank became too large, Hence the entire loan section is shifted to Manager. Otherwise, Loan should be inside Bank.
#? Note:- In an ideal scenario, there will be multiple managers who are handling different types of loans according to their authority and role.
#? Note:- In that ideal scenario, Bank should have different Loan Instances and different Managers Instances. (Inheritence is good option here to create different types of loans and different types of managers maybe)
#? Note:- Manager could have so much authority, altering details of accounts or customers upon request. However, not introducing these features as of now.

from loan import Loan

class Manager:
    def __init__(self):
        self.password = None
        self.locked_account_numbers = []
        self.loan_applications = {}
        self.approved_loans = {}

    def change_password(self, new_password):
        self.password = new_password

    def is_this_customer_applied(self, cust_id):
        if cust_id in self.loan_applications:
            return True
        else:
            return False

    def is_already_applied(self, customer_id):
        if customer_id in self.loan_applications:
            return True
        else:
            return False

    def validate_login(self, entered_password):
        return entered_password == self.password

    def receive_loan_application(self, loan_data, customer_id):
        self.loan_applications[customer_id] = loan_data

    def get_possible_loan_data(self, customer_id, requested_amount, monthly_income, bank_balance):
        new_loan = Loan(customer_id)
        possible_loans = new_loan.check_loan_possibility(requested_amount, monthly_income, bank_balance)
        return possible_loans

    def get_locked_account_numbers(self):
        return self.locked_account_numbers

    def unlock_account(self, the_account):
        the_account.account_unlock()
        self.locked_account_numbers.remove(the_account.number)

    def show_loan_applications(self):
        return self.loan_applications

    def show_approved_loan(self, loan_ac_number):
        if loan_ac_number in self.approved_loans:
            return self.approved_loans[loan_ac_number]
        else:
            return None

    def approve_loan(self, application, customer, account):
        loan = Loan(customer.cust_id)
        loan.generate_loan_ac_number(account.number, customer.name, customer.age, application["tanure_in_months"], application["monthly_emi"])
        loan.populate_loan_details(application["loan_amount"], application["repayment_amount"], application["monthly_emi"], application["tanure_in_months"])
        self.approved_loans[loan.loan_account_number] = loan
        customer.issue_loan(loan.loan_account_number)
        the_transaction = account.generate_transfer_transaction(loan.loan_amount, loan.loan_account_number, account.number)
        account.receive_amount(loan.loan_amount, the_transaction)
        del self.loan_applications[customer.cust_id]
        return loan.loan_account_number

    def load_data(self, received_password, locked_ac_numbers, submitted_loan_applications, loans_already_approved):
        self.password = received_password
        self.locked_account_numbers = locked_ac_numbers
        self.loan_applications = submitted_loan_applications
        if len(loans_already_approved) > 0:
            for loan_ac_number, loan_dict in loans_already_approved.items():
                loan = Loan(loan_dict["attached_customer"])
                loan.load_previous_data(loan_dict)
                self.approved_loans[loan_ac_number] = loan