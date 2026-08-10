
import csv
from food import Food
from room import Room
from guest import Guest
from finance import Cashbox

#? NOTE:- This hotel.py became a God Object. Creating a Recorder class for handling csv data is needed.

class Hotel:
    def __init__(self):
        self.name = "The Pan Pacific"
        self.foods = {}
        with open("./data_csv/food.csv") as food_file:
            render_food = csv.reader(food_file)
            for food_row in render_food:
                self.foods[food_row[0]] = Food(food_row[0], int(food_row[1]), int(food_row[2]))
        self.rooms = {}
        with open("./data_csv/room.csv") as room_file:
            render_room = csv.reader(room_file)
            for room_row in render_room:
                self.rooms[room_row[1]] = Room(room_row[0], int(room_row[1]), int(room_row[2]), room_row[3].lower() == "true", room_row[4].lower() == "true", room_row[5].lower() == "true", room_row[6])
        self.guests = {}
        with open("./data_csv/guest.csv") as guest_file:
            render_guest = csv.reader(guest_file)
            for guest_row in render_guest:
                self.guests[guest_row[3]] = Guest(guest_row[0], int(guest_row[1]), int(guest_row[2]), guest_row[3])
        with open("./data_csv/cash.csv") as cash_file:
            render_cash = csv.reader(cash_file)
            for cash_row in render_cash:
                self.cash_box = Cashbox(int(cash_row[0]))
        self.fix_booked_rooms()
        self.food_dispatcher = {}

    def clear_guest_data(self):
        with open("./data_csv/guest.csv", mode="w") as clear_file:
            pass

    def clear_ordered_food_data(self, room_number):
        remaining_order_rows = []
        with open("./data_csv/ordered_food.csv") as food_order_file:
            render_order = csv.reader(food_order_file)
            for row in render_order:
                if row and row[0] != str(room_number):
                    remaining_order_rows.append(row)
        with open("./data_csv/ordered_food.csv", mode="w") as order_file:
            order_writer = csv.writer(order_file)
            order_writer.writerows(remaining_order_rows)

    def write_food_data(self):
        with open("./data_csv/food.csv", mode="w") as food_file:
            food_writer = csv.writer(food_file)
            for food_name, food_object in self.foods.items():
                food_writer.writerows([
                    [food_object.name, food_object.price, food_object.quantity]
                ])

    def write_food_order(self, the_order):
        with open("./data_csv/ordered_food.csv", mode="a") as ordered_food_file:
            order_writer = csv.writer(ordered_food_file)
            for room_no, order_list in the_order.items():
                for order in order_list:
                    order_writer.writerows([
                        [room_no, order["name"], order["quantity"], order["price"]]
                    ])

    def fetch_food_order_from_csv(self, room_number):
        list_of_recorded_order = []
        with open("./data_csv/ordered_food.csv") as fetch_order_file:
            render_order = csv.reader(fetch_order_file)
            for order_row in render_order:
                if order_row[0] == str(room_number):
                    list_of_recorded_order.append([order_row[1], order_row[2], order_row[3]])
        return list_of_recorded_order

    def write_guest_data(self, the_guest):
        with open("./data_csv/guest.csv", mode="a") as file:
            writer = csv.writer(file)
            writer.writerows([
                [the_guest.name, str(the_guest.birth_year), str(the_guest.choosen_room_number), str(the_guest.key)],
            ])

    def write_guest_data_for_record_keeping(self, the_guest):
        with open("./data_csv/guest_record.csv", mode="a") as guest_record_file:
            guest_writer = csv.writer(guest_record_file)
            guest_writer.writerows([
                [the_guest.name, str(the_guest.birth_year), str(the_guest.choosen_room_number)]
            ])

    def write_cash_data(self):
        with open("./data_csv/cash.csv", mode="w") as cash_file:
            cash_writer = csv.writer(cash_file)
            cash_writer.writerows([
                [self.cash_box.earning]
            ])

    def write_booked_room_data(self):
        with open("./data_csv/booked_room.csv", mode="w") as booked_room_file:
            room_writer = csv.writer(booked_room_file)
            for room_no, room_object in self.rooms.items():
                if room_object.is_booked:
                    room_writer.writerows([
                        [room_object.number, room_object.bill, room_object.guest.name, room_object.guest.key]
                    ])

    def fix_booked_rooms(self):
        with open("./data_csv/booked_room.csv") as booked_room_file:
            render_booked_room = csv.reader(booked_room_file)
            for row in render_booked_room:
                if row:
                    self.rooms[row[0]].is_booked = True
                    self.rooms[row[0]].bill = int(row[1])
                    self.rooms[row[0]].guest = self.guests[row[3]]

    def data_keeper(self):
        self.clear_guest_data()
        for guest_key in self.guests:
            self.write_guest_data(self.guests[guest_key])
        self.write_cash_data()
        self.write_booked_room_data()

    def generate_guest(self, guest_name, guest_birth_year, room_no, room_key):
        self.guests[room_key] = Guest(guest_name, guest_birth_year, room_no, room_key)

    def send_available_rooms(self):
        available_room_info = {}
        for room_no, room_object in self.rooms.items():
            if not room_object.is_booked:
                available_room_info[room_no] = {
                    "room_name":room_object.name,
                    "room_price":room_object.price
                }
        return available_room_info

    def get_room(self, room_number):
        for room_no in self.rooms:
            if room_no == room_number:
                return self.rooms[room_no]
        return None

    def complete_booking(self, the_guest_name, the_guest_birth_year, room):
        self.generate_guest(the_guest_name, the_guest_birth_year, room.number, room.key)
        room.book_room(self.guests[room.key])
        self.cash_box.receive_amount(room.price)

    def initiate_checkout(self, room):
        the_guest = self.guests.pop(room.key)
        self.write_guest_data_for_record_keeping(the_guest)
        self.clear_ordered_food_data(room.number)
        self.cash_box.receive_amount(room.bill)
        room.leave_room()

    def send_available_foods(self):
        available_food_info = {}
        for food_name, food_object in self.foods.items():
            if food_object.quantity > 0:
                available_food_info[food_name] = food_object.price
        return available_food_info

    def prepare_food(self, food_name, food_number, room_number):
        for name_of_food, food_object in self.foods.items():
            if name_of_food == food_name:
                if food_object.quantity >= food_number:
                    self.food_dispatcher[room_number][food_object.name] = {
                        food_number:food_object
                    }
                    return True
                else:
                    return False
        return False

    def send_food_to_room(self, room_number):
        return self.food_dispatcher[room_number]

    def initiate_food_dispatcher(self, room_number):
        self.food_dispatcher[room_number] = {}

    def empty_food_dispatcher(self, room_number):
        self.food_dispatcher[room_number].clear()

