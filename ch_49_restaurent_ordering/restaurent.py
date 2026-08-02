
class Restaurent:
    def __init__(self):
        self.name = "Sun Down"
        self.list_of_tables = []
        self.list_of_items = []
        self.list_of_orders = []
        self.list_of_bills = []

    def add_table(self, a_table):
        self.list_of_tables.append(a_table)

    def add_item(self, an_item):
        self.list_of_items.append(an_item)

    def add_order(self, an_order):
        self.list_of_orders.append(an_order)

    def add_bill(self, the_bill):
        self.list_of_bills.append(the_bill)

    def table_chooser(self, table_no, number_of_people):
        for table in self.list_of_tables:
            if table.number == table_no and table.seat_capacity >= number_of_people:
                table.is_occupied = True
                return True
        return False

    def payment_checker(self, bill, user_payment):
        if bill == user_payment:
            return 0, True
        elif bill < user_payment:
            return user_payment - bill, True
        elif bill > user_payment:
            return 0, False

    def release_table(self, table_number):
        for table in self.list_of_tables:
            if table.number == table_number and table.is_occupied:
                table.is_occupied = False


