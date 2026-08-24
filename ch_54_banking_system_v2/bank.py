
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

    def get_customer(self, customer_id):
        if customer_id:
            if customer_id in  self.customers:
                return self.customers[customer_id]
            else:
                return None
        return None

    def get_account(self, account_number):
        if account_number:
            if account_number in self.accounts:
                return self.accounts[account_number]
            else:
                return None
        else:
            return None

    def create_customer(self, name, age, email_id, mobile_number):
        new_customer = Customer(name, age, email_id, mobile_number)
        new_customer.generate_customer_id_and_password()
        self.add_customer(new_customer)
        self.email_mobile_set.add(new_customer.email)
        self.email_mobile_set.add(str(new_customer.mobile))
        return new_customer

    def create_account(self, customer_id):
        new_account = Account(customer_id)
        new_account.generate_ac_no()
        self.add_account(new_account)
        return new_account

    def lock_account(self, cust_id):
        the_account = self.get_account(self.get_customer(cust_id).account_number)
        the_account.is_locked = True

    def is_account_locked(self, customer_id):
        the_account = self.get_account(self.get_customer(customer_id).account_number)
        if the_account:
            return the_account.is_locked

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

    def validate_customer_id(self, the_id):
        if the_id in self.customers:
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
                loaded_customer = Customer(customer_details["name"], int(customer_details["age"]), customer_details["email"], int(customer_details["mobile"]))
                loaded_customer.load_customer_ac_id_pass(int(customer_details["account_number"]), customer_details["cust_id"], customer_details["password"])
                self.add_customer(loaded_customer)
        else:
            self.customers = {}
        loaded_account_data = self.recorder.load_account_data()
        if loaded_account_data:
            for ac_no, ac_details in loaded_account_data.items():
                loaded_account = Account(ac_details["attached_customer_id"])
                loaded_account.load_recorded_details(int(ac_details["number"]), int(ac_details["balance"]), ac_details["is_locked"], ac_details["transaction_history"])
                self.add_account(loaded_account)
        else:
            self.accounts = {}
        loaded_email_mobile_data = self.recorder.load_email_mobile_set()
        if loaded_email_mobile_data:
            self.email_mobile_set = loaded_email_mobile_data
        else:
            self.email_mobile_set = set()
