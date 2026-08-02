
class Table:
    def __init__(self, number, seat_capacity):
        self.number = number
        self.seat_capacity = seat_capacity
        self.is_occupied = False
        self.table_bill = 0

    def make_an_order(self, order_object):
        return order_object