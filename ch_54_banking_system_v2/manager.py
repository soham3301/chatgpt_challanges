
#? Note:- This application is for customers. A Manager should use another system, not the same. However, hardcoding password into the application is wrong.
#? Note:- Didn't Focused on login security of Manager. Here I introduced manager just to approve loans and unlock accounts.
#? Note:- Bank became too large, Hence the entire loan section is shifted to Manager
#? Note:- Manager could have so much authority, altering details of accounts or customers upon request. However, not introducing these features as of now.

from loan import Loan

class Manager:
    def __init__(self):
        self.name = "Manager"
        self.password = "12345"
        self.locked_account_numbers = []
        self.loan_applications = {}
        self.approved_loans = {}

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