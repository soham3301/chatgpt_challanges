
import csv
from display import Display
from user_input import UserInput
from finance import Cashbox
from hotel import Hotel

display = Display()
user_input = UserInput()
cash_box = Cashbox()
hotel = Hotel()

application_running = True
while application_running:
    display.show_primary_user_interface()
    user_consent_primary = user_input.text_input()
    if user_consent_primary == "exit":
        display.thank_you_display()
        hotel.guest_data_keeper()
        break
    elif user_consent_primary == "1":
        room_data = hotel.send_available_rooms()
        display.show_available_rooms(room_data)
    elif user_consent_primary == "2":
        print("Login Section")
    else:
        display.invalid_input()