
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

    def calculate_interest(self):
        #* Note:- Interest is calculated on current balance and flat 4% simple interest. However, real bank interest is calculated on every month's average balance, not current balance
        #* Note:- Account Opening Date is missing. It's an important data.
        interest = round(self.balance * 4 / 100)
        return interest

    def send_account_information(self):
        interest = self.calculate_interest()
        account_data = {
            "number": self.number,
            "balance": self.balance,
            "interest_gained": interest,
            "customer_id": self.attached_customer_id,
            "total_transactions": len(self.transaction_history)
        }
        return account_data

    def check_transaction_history(self):
        transaction_list = []
        new_balance = 0
        for transac_id, transac_object in self.transaction_history.items():
            if transac_object.transaction_type == "deposit":
                new_balance += transac_object.amount
            elif transac_object.transaction_type == "withdraw":
                new_balance -= transac_object.amount
            elif transac_object.transaction_type == "transfer" and transac_object.from_account_no == self.number:
                new_balance -= transac_object.amount
            elif transac_object.transaction_type == "transfer" and transac_object.to_account_no == self.number:
                new_balance += transac_object.amount
            transaction_list.append({
                "amount": transac_object.amount,
                "type": transac_object.transaction_type,
                "tran_id": transac_object.tran_id,
                "to_account": transac_object.to_account_no,
                "from_account": transac_object.from_account_no,
                "balance": new_balance
            })
        return transaction_list, new_balance



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


