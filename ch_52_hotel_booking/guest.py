
import random

class Guest:
    def __init__(self, name, birth_year, room_no, key):
        self.name = name
        self.birth_year = birth_year
        self.choosen_room_number = room_no
        self.key = key

    def booking_update_for_guest(self, booking_data):
        # example_data = {
        #     "room_no":5,
        #     "breakfast":True,
        #     "lanch_dinner":False
        # }
        self.choosen_room_number = booking_data["room_no"]
        self.breakfast_included = booking_data["breakfast"]
        self.lanch_dinner_included = booking_data["lanch_dinner"]
        self.checked_in = True

    def generate_key(self):
        first_random_number = random.randint(0, 9)
        first_letter = self.name[0]
        birth_year_number = self.birth_year
        second_random_number = random.randint(0, 9)
        customer_key = str(first_random_number) + first_letter + str(birth_year_number) + str(second_random_number)
        self.key = customer_key