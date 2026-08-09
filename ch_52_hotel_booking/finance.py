
class Cashbox:
    def __init__(self, amount):
        self.earning = amount

    def receive_amount(self, amount):
        self.earning += amount