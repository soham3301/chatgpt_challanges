
class Display:
    def __init__(self):
        self.name = "Display"

    def show_primary_user_interface(self):
        print('''
1. Book Room
2. Login (Already Booked)
''')

    def show_available_rooms(self, room_data):
        for room_no, room_details in room_data.items():
            print(f"Room No: {room_no} | Room Name: {room_details["room_name"]} | Price: {room_details["room_price"]}")

    def ask_room_number(self):
        print("Enter Room Number for booking")

    def ask_how_many_people(self):
        print("Enter How many Guests")

    def show_payment_amount(self, amount):
        print(f"Pay {amount}")

    def thank_you_display(self):
        print("Thanks for using Hotel Booking")

    def invalid_input(self):
        print("Invalid Input")

    def show_secondary_user_interface(self):
        print('''
1. Order Food
2. Check Bill
3. Checkout
''')
