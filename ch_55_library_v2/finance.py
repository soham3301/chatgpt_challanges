
class Finance:
    def __init__(self):
        self.vault = 100000
        self.late_fee = 2

    def calculate_late_fee(self, days):
        if days > 0:
            return self.late_fee * days

    def check_vault(self):
        return self.vault

    def check_balance_available_or_not(self, book_price):
        return self.vault > book_price

    def spend_amount(self, amount):
        self.vault -= amount

    def add_amount(self, amount):
        self.vault += amount

    def change_late_fee(self, new_fee):
        self.late_fee = new_fee

    def to_dict(self):
        return {
            "vault": self.vault,
            "late_fee": self.late_fee
        }

    def load_fin_data(self, data):
        self.vault = int(data["vault"])
        self.late_fee = int(data["late_fee"])