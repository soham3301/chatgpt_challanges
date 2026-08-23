
import random

class Transaction:
    def __init__(self):
        self.tran_id = None
        self.amount = None
        self.from_account_no = None
        self.to_account_no = None
        self.transaction_type = None

    def transfer_account_number(self, from_ac_no, to_ac_no):
        self.from_account_no = from_ac_no
        self.to_account_no = to_ac_no


    def generate_tran_id(self):
        self.tran_id = random.randint(10000, 99999)
        return self.tran_id

    def amount_and_type_setter(self, the_amount, the_type):
        self.amount = the_amount
        self.transaction_type = the_type