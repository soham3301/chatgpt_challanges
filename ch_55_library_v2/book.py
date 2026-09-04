
import random

class Book:
    def __init__(self, title, price, author):
        self.title = title
        self.price = price
        self.author = author
        self.id = None
        self.borrowed = False

    def generate_book_id(self):
        first_l = self.title[0]
        second_l = self.author[0]
        third_l = self.title[-1]
        fourth_l = self.author[-1]
        fifth_l = self.price
        a_random_number = random.randint(1, 9)
        the_random_id = first_l + second_l + third_l + fourth_l + str(fifth_l) + str(a_random_number)
        self.id = ''.join(random.sample(the_random_id, len(the_random_id)))
        return self.id

    def load_book_data(self, b_id, borrow_condition):
        self.id = b_id
        self.borrowed = borrow_condition

    def borrow_book(self):
        self.borrowed = True

    def book_returned(self):
        self.borrowed = False