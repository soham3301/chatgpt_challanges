
import random

class Transaction:
    def __init__(self, amount, type_of_transaction):
        self.tran_id = None
        self.amount = amount
        self.from_account_no = None
        self.to_account_no = None
        self.transaction_type = type_of_transaction

    def transfer_account_number(self, from_ac_no, to_ac_no):
        self.from_account_no = from_ac_no
        self.to_account_no = to_ac_no

    def generate_tran_id(self):
        self.tran_id = random.randint(10000, 100000)
