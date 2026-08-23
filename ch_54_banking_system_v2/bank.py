
#? NOTE:- I never used set. I don't know this is an appropriate case or not. Just trying.

from customer import Customer
from account import Account
from recorder import Recorder

class Bank:
    def __init__(self):
        self.accounts = {}                          #*  {ac_no: ac_object}
        self.customers = {}                         #*  {cust_id: cust_object}
        self.email_mobile_set = set()
        self.recorder = Recorder()
        self.load_data()

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

    def create_account(self, customer_id):
        new_account = Account(customer_id)
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

    def save_data(self):
        self.recorder.write_customer_data(self.customers)
        self.recorder.write_account_data(self.accounts)
        self.recorder.write_email_mobile_set(self.email_mobile_set)

    def load_data(self):
        loaded_customer_data = self.recorder.load_customer_data()
        if loaded_customer_data:
            for customer_id, customer_details in loaded_customer_data.items():
                new_customer = Customer(customer_details["name"], int(customer_details["age"]), customer_details["email"], int(customer_details["mobile"]))
                new_customer.load_customer_ac_id_pass(customer_details["account_number"], customer_details["cust_id"], customer_details["password"])
                self.add_customer(new_customer)
        else:
            self.customers = {}
