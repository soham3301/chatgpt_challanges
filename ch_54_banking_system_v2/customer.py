
import random

class Customer:
    def __init__(self, name, age, email_id, mobile_number):
        self.name = name
        self.age = age
        self.email = email_id
        self.mobile = mobile_number
        self.account = None
        self.cust_id = None
        self.password = None

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

    def attach_account(self, the_account):
        self.account = the_account

    def change_password(self, new_password):
        self.password = new_password

    def display_customer_information(self):
        pass