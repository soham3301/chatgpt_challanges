
import random

class Order:
    def __init__(self, item, num_of_item):
        self.the_item = item
        self.item_numbers = num_of_item
        self.order_number = 0
        self.order_cost = 0
        self.generate_order_number()
        self.calculate_order_cost()

    def generate_order_number(self):
        #! NOTE - There is a chance to generate duplicate order numbers | Bug
        self.order_number = str(random.randint(0, 1000)) + self.the_item.name[0] + str(self.item_numbers)

    def calculate_order_cost(self):
        self.order_cost = self.the_item.price * self.item_numbers


    