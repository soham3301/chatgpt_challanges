
import random

#! Important:- Strong Password Rules has not been set. it's a big diversion from challenge goal. Hence, ignoring it for this challenge. However, it's a bug
#? Note:- For simplicity purpose, one customer can avail 1 loan at a time. However, in real banks, customers can avail multiple loans altogether.

class Customer:
    def __init__(self, name, age, email_id, mobile_number):
        self.name = name
        self.age = age
        self.email = email_id
        self.mobile = mobile_number
        self.account_number = None
        self.cust_id = None
        self.password = None
        self.loan_account_number = None

    def check_login(self, customer_id, customer_password):
        if customer_id and customer_password:
            if customer_id == self.cust_id and customer_password == self.password:
                return True
            else:
                return False
        else:
            return False

    def generate_customer_id_and_password(self):
        the_letter = self.name[0]
        id_number = random.randint(10, 99)
        the_id = the_letter + str(id_number) + str(self.age)
        self.cust_id = the_id
        pass_number = random.randint(1000, 9999)
        self.password = self.name + str(pass_number)

    def attach_account_number(self, the_account):
        self.account_number = the_account.number

    def validate_password(self, received_pass):
        return self.password == received_pass

    def change_password(self, new_password):
        self.password = new_password

    def load_customer_ac_id_pass(self, ac_no, cust_id, cust_password, loan_ac_no):
        self.account_number = ac_no
        self.cust_id = cust_id
        self.password = cust_password
        self.loan_account_number = loan_ac_no

    def check_customer_details(self):
        customer_data = {
            "name": self.name,
            "age": self.age,
            "email": self.email,
            "mobile": self.mobile,
            "account_number": self.account_number,
            "loan_account_number": self.loan_account_number,
            "customer_id": self.cust_id,
            "password": self.password
        }
        return customer_data

    def send_customer_info_for_manager(self):
        return {"name": self.name, "age": self.age}

    def issue_loan(self, loan_number):
        self.loan_account_number = loan_number

    def clear_loan(self):
        self.loan_account_number = None

    def prepare_loan_data(self, loan_object):
        #? Note:- I could have used loan_object.attribute instead of __dict__.copy().
        loan_obj = loan_object.__dict__.copy()
        data = f'''
Loan Account Number: {loan_obj["loan_account_number"]}  |       Loan Tenure: {loan_obj["loan_tanure_in_months"]} months     |       Loan Amount: {loan_obj["loan_amount"]}/-
Unpaid Amount: {loan_obj["repayment_amount"]}/-         |       Paid Amount: {loan_obj["amount_paid_till_now"]}/-
EMI: {loan_obj["emi_amount"]}/- per Month
Paid EMI: {loan_obj["emi_status"]["paid"]} nos          |       Unpaid EMI: {loan_obj["emi_status"]["unpaid"]} nos
'''
        return data