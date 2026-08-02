
class Display:
    def __init__(self):
        self.name = "Display"

    def welcome_board(self):
        print("Welcome to Sundown Restaurent")

    def invalid_input(self):
        print("Invalid Input")

    def display_correct_tables(self, people_nos, tables_list):
        if people_nos:
            perfect_tables = []
            possible_tables = []
            for table in tables_list:
                if not table.is_occupied:
                    if table.seat_capacity == people_nos:
                        perfect_tables.append(table)
                    elif table.seat_capacity > people_nos:
                        possible_tables.append(table)
            if perfect_tables or possible_tables:
                if perfect_tables:
                    for perf_table in perfect_tables:
                        print(f"Table Number: {perf_table.number} is suitable for your need")
                if possible_tables:
                    for poss_table in possible_tables:
                        print(f"You can also choose Table Number: {poss_table.number}")
            else:
                print("Sorry We don't have a suitable table for you as of now.")
        else:
            self.invalid_input()

    def display_bill(self, bill):
            print(f"Your Bill Amount is Rs. {bill.bill_amount} INR")

    def display_menu(self, item_list):
        for item in item_list:
            print(f"Name: {item.name} | Cost: {item.price} INR")
        print("Type Exit for Exit")

    def want_discount(self):
        print("Want Discount? We Have a Flat 20% Discount Offer")

    def display_updated_bill(self, new_bill):
        print(f"Your bill after Discount is Rs. {new_bill.bill_amount} INR")

    def payment_done(self):
        print("Your Order is Complete")

    def take_return(self, amount):
        print(f"Here is your Return: {amount} INR")
    
    def payment_failed(self, the_amount, the_payment):
        print(f"You Paid only {the_payment} INR. Whereas the bill was {the_amount} INR | Payment Failed")

    

        