
import csv
from food import Food
from room import Room
from guest import Guest

# with open("./data_csv/room.csv", mode="w") as file:
#     writter = csv.writer(file)
#     writter.writerows(room_list)


class Hotel:
    def __init__(self):
        self.name = "The Pan Pacific"
        self.foods = []
        with open("./data_csv/food.csv") as food_file:
            render_food = csv.reader(food_file)
            for food_row in render_food:
                self.foods.append(Food(food_row[0], int(food_row[1]), int(food_row[2])))
        self.rooms = []
        with open("./data_csv/room.csv") as room_file:
            render_room = csv.reader(room_file)
            for room_row in render_room:
                self.rooms.append(Room(room_row[0], int(room_row[1]), int(room_row[2]), bool(room_row[3]), bool(room_row[4]), bool(room_row[5])))
        self.guests = []
        with open("./data_csv/guest.csv") as guest_file:
            render_guest = csv.reader(guest_file)
            for guest_row in render_guest:
                self.guests.append(Guest(guest_row[0], guest_row[1], guest_row[2], guest_row[3]))

    def clear_csv_data(aelf):
        with open("./data_csv/guest.csv", mode="w") as clear_file:
            pass

    def write_guest_data(self, the_guest):
        with open("./data_csv/guest.csv", mode="a") as file:
            writer = csv.writer(file)
            writer.writerows([
                [the_guest.name, str(the_guest.birth_year), str(the_guest.choosen_room_number), str(the_guest.key)],
            ])

    def guest_data_keeper(self):
        self.clear_csv_data()
        for guest in self.guests:
            self.write_guest_data(guest)

    def generate_guest(self, guest_data_list):
        new_guest = Guest(guest_data_list[0], int(guest_data_list[1]), int(guest_data_list[2]), 0)
        new_guest.generate_key()
        self.guests.append(new_guest)

    def send_available_rooms(self):
        available_room_info = {}
        for room in self.rooms:
            if not room.is_booked:
                available_room_info[room.number] = {
                    "room_name":room.name,
                    "room_price":room.price
                }
                # print(f"Room Name: {room.name} | Room Number: {room.number} | Room Price: {room.price}")
        # print(available_room_info)
        return available_room_info
