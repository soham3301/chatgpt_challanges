
class Bill:
    def __init__(self, order_list):
        self.bill_amount = 0
        self.the_order_list = order_list
        self.generate_bill()

    def generate_bill(self):
        for order in self.the_order_list:
            self.bill_amount += order.order_cost

    def apply_discount(self):
        the_discount = self.bill_amount * 20 / 100
        self.bill_amount -= the_discount



