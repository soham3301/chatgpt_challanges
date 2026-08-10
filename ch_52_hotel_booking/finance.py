
class Cashbox:
    def __init__(self, amount):
        self.earning = amount

    def receive_amount(self, amount):
        self.earning += amount

    def check_payment(self, amount, price):
        if amount > price:
            return True, amount - price
        elif amount == price:
            return True, None
        else:
            return False, amount

    def bill_clear(self, amount, bill):
        if amount > bill:
            return amount - bill
        else:
            return 0