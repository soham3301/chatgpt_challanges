
from display import Display
from user_input import UserInput
from hotel import Hotel
from guest import Guest

display = Display()
user_input = UserInput()
hotel = Hotel()

print("IMPORTANT: Giving Lanch / Dinner / Breakfast - Free of cost remains")

application_running = True
while application_running:
    display.show_primary_user_interface()
    user_consent_primary = user_input.text_input()
    if user_consent_primary == "3":
        display.thank_you_display()
        hotel.data_keeper()
        application_running = False
    elif user_consent_primary == "1":
        room_data = hotel.send_available_rooms()
        display.show_available_rooms(room_data)
        display.ask_room_number("for booking")
        room_number = user_input.text_input()
        the_room = hotel.get_room(room_number)
        if the_room:
            display.ask_guest_name()
            guest_name = user_input.text_input()
            display.ask_guest_birth_year()
            guest_birth_year = user_input.number_input()
            if guest_birth_year:
                if Guest.adult_checker(guest_birth_year):
                    display.show_payment_amount(the_room.name, the_room.price)
                    paid_amount = user_input.number_input()
                    if paid_amount:
                        booking_status, any_refund = hotel.check_booking(paid_amount, the_room)
                        if booking_status:
                            if any_refund:
                                display.take_refund(any_refund)
                            hotel.complete_booking(guest_name, guest_birth_year, the_room)
                            display.booking_complete(the_room.key)
                        else:
                            display.booking_incomplete(any_refund)
                    else:
                        display.invalid_input()
                else:
                    display.not_adult()
            else:
                display.invalid_input()
        else:
            display.room_not_exist()
    elif user_consent_primary == "2":
        display.ask_room_number("to enter")
        room_number_for_login = user_input.text_input()
        room_for_login = hotel.get_room(room_number_for_login)
        if room_for_login:
            display.ask_room_key()
            room_key = user_input.text_input()
            if room_for_login.validate_key(room_key):
                display.welcome_into_room()
                guest_logged_in = True
                while guest_logged_in:
                    display.show_secondary_user_interface()
                    user_consent_secondary = user_input.text_input()
                    if user_consent_secondary == "5":
                        display.room_lock_notification()
                        guest_logged_in = False
                    elif user_consent_secondary == "1":
                        facilities = room_for_login.check_facilities()
                        display.show_facilities(facilities)
                    elif user_consent_secondary == "2":
                        hotel.initiate_food_dispatcher(room_for_login.number)
                        #* This feature (food dispatcher with room number) is added to handle multiple guest ordering food together
                        while True:
                            food_data = hotel.send_available_foods()
                            display.show_available_foods(food_data)
                            name_of_food = user_input.text_input()
                            if name_of_food == "order":
                                ordered_food = hotel.send_food_to_room(room_for_login.number)
                                if len(ordered_food) > 0:
                                    room_for_login.order_food(ordered_food)
                                    hotel.empty_food_dispatcher(room_for_login.number)
                                    hotel.write_food_data()
                                    display.food_order_complete()
                                else:
                                    display.empty_order()
                                break
                            elif name_of_food == "cancel":
                                hotel.empty_food_dispatcher(room_for_login.number)
                                display.order_cancelled()
                                break
                            else:
                                display.ask_number_of_food(name_of_food.title())
                                quantity_of_food = user_input.number_input()
                                if quantity_of_food:
                                    if hotel.prepare_food(name_of_food.title(), quantity_of_food, room_for_login.number):
                                        display.food_added_notice(name_of_food.title(), quantity_of_food)
                                        continue
                                    else:
                                        display.food_not_exist(name_of_food)
                                else:
                                    display.invalid_input()
                    elif user_consent_secondary == "3":
                        bill_data = room_for_login.check_bill()
                        display.show_bill(bill_data)
                    elif user_consent_secondary == "4":
                        print("Checkout Section")
                    else:
                        display.invalid_input()
            else:
                display.invalid_key_entered()
        else:
            display.room_not_exist()
    elif user_consent_primary == "admin":
        print("This is Admin Section | Entry Restricted")
    else:
        display.invalid_input()