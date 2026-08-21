
#? NOTE:- I never used set. I don't know this is an appropriate case or not. Just trying.

from customer import Customer
from account import Account

class Bank:
    def __init__(self):
        self.accounts = {}
        self.customers = {}
        self.email_mobile_set = set()

    def add_account(self, the_account):
        self.accounts[the_account.number] = the_account

    def add_customer(self, the_customer):
        self.customers[the_customer.cust_id] = the_customer

    def user_validation(self, customer_id, customer_password):
        if customer_id in self.customers:
            self.customers[customer_id].check_login(customer_id, customer_password)
            return True
        else:
            return False

    def create_customer(self, name, age, email_id, mobile_number):
        new_customer = Customer(name, age, email_id, mobile_number)
        new_customer.generate_customer_id_and_password()
        self.add_customer(new_customer)
        self.email_mobile_set.add(new_customer.email)
        self.email_mobile_set.add(new_customer.mobile)
        return new_customer

    def create_account(self, first_deposit_amount, customer_id):
        new_account = Account(first_deposit_amount, customer_id)
        new_account.generate_ac_no()
        self.add_account(new_account)
        return new_account


    def lock_account(self):
        pass

    def unlock_account(self):
        pass

    @staticmethod
    def validate_age(age):
        return age >= 18

    @staticmethod
    def validate_first_deposit(amount):
        return amount >= 500

    def is_data_exist(self, data):
        if data in self.email_mobile_set:
            return True
        else:
            return False

    @staticmethod
    def validate_email(email):
        if "@" in email and "@" != email[0] and "@" != email[-1]:
            return True
        else:
            return False

    @staticmethod
    def validate_mobile(number):
        if number > 0 and len(str(number)) == 10:
            return True
        else:
            return False
