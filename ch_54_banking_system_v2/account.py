
import random
from transaction import Transaction

class Account:
    def __init__(self, balance):
        #! AC No should be random
        self.number = None
        self.balance = balance
        self.is_locked = False
        self.attached_customer_id = None
        self.transaction_number = 0
        self.transaction_history = {}

    def transaction_recorder(self, amount, the_type, *args):
        self.transaction_number += 1
        if args:
            transfer_transaction = Transaction(amount, the_type)
            transfer_transaction.generate_tran_id()
            if args[0] == "received":
                transfer_transaction.transfer_account_number(args[1], self.number)
                self.transaction_history[self.transaction_number] = {
                    args[0]: transfer_transaction
                }
            else:
                transfer_transaction.transfer_account_number(self.number, args[1])
                self.transaction_history[self.transaction_number] = {
                    args[1]: transfer_transaction
                }
        else:
            cash_transaction = Transaction(amount, the_type)
            cash_transaction.generate_tran_id()
            self.transaction_history[self.transaction_number] = {
                the_type: cash_transaction
            }


    def deposit(self, amount):
        if amount > 0:
            self.balance += amount
            self.transaction_recorder(amount, "deposit")
            return True
        else:
            return False

    def withdraw(self, amount):
        if amount > 0:
            if self.balance >= amount:
                self.balance -= amount
                self.transaction_recorder(self.send_amount, "withdraw")
                return True
            else:
                return False
        else:
            return False

    def receive_amount(self, amount, from_account):
        if self.deposit(amount=amount):
            self.transaction_recorder(amount, "transfer", "received", from_account)
            return True
        else:
            return False

    def send_amount(self, amount, to_account):
        if self.withdraw(amount):
            self.transaction_recorder(amount, "transfer", "sent", to_account)
        else:
            return False

    def check_balance(self):
        return self.balance

    def display_account_information(self):
        pass

    def check_transaction_history(self):
        pass

