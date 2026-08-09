
class Display:
    def __init__(self):
        self.name = "Display"

    def show_primary_user_interface(self):
        print('''
1. Book Room
2. Login (Already Booked)
3. Exit
''')

    def show_available_rooms(self, room_data):
        if len(room_data) == 0:
            print("No Rooms are available as of now")
        else:
            for room_no, room_details in room_data.items():
                print(f"Room No: {room_no} | Room Name: {room_details["room_name"]} | Price: {room_details["room_price"]}")

    def ask_room_number(self, purpose):
        print(f"Enter Room Number {purpose}")

    def ask_how_many_people(self):
        print("Enter How many Guests")

    def show_payment_amount(self, name_of_room, amount):
        print(f"Pay INR {amount}/- to book {name_of_room} room")

    def ask_guest_name(self):
        print("Enter Your Name")

    def ask_guest_birth_year(self):
        print("Enter Your Birth Year")

    def not_adult(self):
        print("You can't book a room as a Minor")

    def take_refund(self, refund):
        print(f"Here is your refund amount: INR {refund}/-")

    def booking_complete(self, key):
        print(f"Your Booking is complete. Here is your key: {key} | You can login now using this key.")

    def booking_incomplete(self, refund_amount):
        print(f"Your Booking is incomplete. Here is your full refund: INR {refund_amount}/-")
    










    def ask_room_key(self):
        print("Enter your room key")

    def invalid_key_entered(self):
        print("Invalid Key Entered")

    def welcome_into_room(self):
        print("Welcome in the room. Enjoy Your Stay")

    def show_facilities(self, data):
        if data["ac"]:
            print("AC Available")
        if data["breakfast"]:
            print("You have Complimentary Breakfast")
        if data["lanch_dinner"]:
            print("Your Lanch and Dinner is free")

    def show_available_foods(self, data):
        print("Available Foods")
        for name, price in data.items():
            print(f"Item Name: {name} | INR {price}/-")
        print("\nType Item Name to add Item")
        print("Type 'Order' for order")
        print("Type 'Cancel' for cancel order")

    def ask_number_of_food(self, food_name):
        print(f"How many {food_name} do you want?")

    def food_added_notice(self, name, number):
        print(f"{number} number of {name} added")

    def food_order_complete(self):
        print("Your Food Arrived")

    def empty_order(self):
        print("No Food order has been made")

    def order_cancelled(self):
        print("Your order has been cancelled")

    def food_not_exist(self, food_name):
        print(f"Sorry we don't have {food_name} as of now.")

    def show_bill(self, data):
        print(f"Paid amount: INR {data["paid"]}/- | Remaining amount: INR {data["unpaid"]}/-")

    def room_lock_notification(self):
        print("Room Locked.")

    def show_secondary_user_interface(self):
        print('''
1. Check Facilities
2. Order Food
3. Check Bill
4. Checkout
5. Exit Room
''')













    def room_not_exist(self):
        print("This room doesn't exist")


    def thank_you_display(self):
        print("Thanks for using Hotel Booking")

    def invalid_input(self):
        print("Invalid Input")


