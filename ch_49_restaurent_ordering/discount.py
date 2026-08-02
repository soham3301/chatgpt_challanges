
class Discount:
    def __init__(self):
        self.discounts = ["abcd001", "efgh002", "ijkl003", "mnop004", "qrst005", "uvwx006"]

    def check_discount(self, user_text):
        if user_text in self.discounts:
            self.discounts.remove(user_text)
            return True
        else:
            return False