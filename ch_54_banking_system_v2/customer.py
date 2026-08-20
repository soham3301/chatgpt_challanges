
class Customer:
    def __init__(self, name, age, initial_deposit_amount, account_number, customer_id, customer_password):
        self.name = name
        self.age = age
        self.first_deposit = initial_deposit_amount
        self.ac_no = account_number
        self.cust_id = customer_id
        self.password = customer_password

    def check_login(self, customer_id, customer_password):
        if customer_id and customer_password:
            if customer_id == self.cust_id and customer_password == self.password:
                return True
            else:
                return False
        else:
            return False