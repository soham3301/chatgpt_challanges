
import random
from transaction import Transaction

class Account:
    def __init__(self, cust_id):
        self.number = None
        self.balance = 0
        self.is_locked = False
        self.attached_customer_id = cust_id
        self.transaction_history = {}                       #*  {tran_id: tran_object}

    def generate_ac_no(self):
        self.number = random.randint(1000000, 9999999)

    def load_recorded_details(self, no, bal, locked, tran_history_dict):
        self.number = no
        self.balance = bal
        self.is_locked = locked
        for transac_id, transac_details in tran_history_dict.items():
            loaded_transaction = Transaction()
            loaded_transaction.load_tran_data(int(transac_details["tran_id"]), int(transac_details["amount"]), transac_details["transaction_type"], transac_details["from_account_no"], transac_details["to_account_no"])
            self.transaction_history[int(transac_details["tran_id"])] = loaded_transaction

    def deposit(self, amount):
        if amount > 0:
            self.balance += amount
            return True
        else:
            return False

    def withdraw(self, amount):
        if amount > 0:
            if self.balance >= amount:
                self.balance -= amount
                return True
            else:
                return False
        else:
            return False

    def cash_deposit(self, amount):
        if self.deposit(amount):
            transaction = self.generate_cash_transaction(amount, "deposit")
            self.record_transaction(transaction)
            return True
        else:
            return False

    def cash_withdraw(self, amount):
        if self.withdraw(amount):
            transaction = self.generate_cash_transaction(amount, "withdraw")
            self.record_transaction(transaction)
            return True
        else:
            return False

    def receive_amount(self, amount, the_transaction):
        if self.deposit(amount=amount):
            self.record_transaction(the_transaction)        #? Both account keeps a record of the same transaction. Not a good looking solution.
            return True
        else:
            return False

    def send_amount(self, amount, to_account_no):
        if self.withdraw(amount=amount):
            transaction = self.generate_transfer_transaction(amount, self.number, to_account_no)
            self.record_transaction(transaction)
            return transaction
        else:
            return None

    def is_balance_sufficient(self, bal):
        return self.balance >= bal
            

    def check_balance(self):
        return self.balance

    def display_account_information(self):
        pass

    def check_transaction_history(self):
        pass

    def generate_cash_transaction(self, amount, transaction_type):
        the_transaction = Transaction()
        the_transaction.generate_tran_id()
        the_transaction.amount_and_type_setter(amount, transaction_type)
        return the_transaction

    def generate_transfer_transaction(self, amount, from_account_number, to_account_number):
        the_transaction = Transaction()
        the_transaction.generate_tran_id()
        the_transaction.amount_and_type_setter(amount, "transfer")
        the_transaction.transfer_account_number(from_account_number, to_account_number)
        return the_transaction

    def record_transaction(self, the_transaction_object):
        self.transaction_history[the_transaction_object.tran_id] = the_transaction_object


