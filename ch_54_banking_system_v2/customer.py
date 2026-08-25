
import random

#! Important:- Strong Password Rules has not been set. it's a big diversion from challenge goal. Hence, ignoring it for this challenge. However, it's a bug

class Customer:
    def __init__(self, name, age, email_id, mobile_number):
        self.name = name
        self.age = age
        self.email = email_id
        self.mobile = mobile_number
        self.account_number = None
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

    def attach_account_number(self, the_account):
        self.account_number = the_account.number

    def validate_password(self, received_pass):
        return self.password == received_pass

    def change_password(self, new_password):
        self.password = new_password

    def display_customer_information(self):
        pass

    def load_customer_ac_id_pass(self, ac_no, cust_id, cust_password):
        self.account_number = ac_no
        self.cust_id = cust_id
        self.password = cust_password

    def check_customer_details(self):
        customer_data = {
            "name": self.name,
            "age": self.age,
            "email": self.email,
            "mobile": self.mobile,
            "account_number": self.account_number,
            "customer_id": self.cust_id,
            "password": self.password
        }
        return customer_data