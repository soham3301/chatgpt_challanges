
from admin import Admin
from ingredients import Ingredient
from drinks import Drink
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine
from display import Display
from user_input import UserInput

admin = Admin()
money_machine = MoneyMachine()
coffee_maker = CoffeeMaker()
display = Display()
user_input = UserInput()

ingredient_list = [
    Ingredient("water", 3.2),
    Ingredient("coffee", 5.5),
    Ingredient("milk", 7.2),
]
drink_list = [
    Drink(name="espresso", water_quantity=5, coffee_quantity=1.8, milk_quantity=0),
    Drink(name="latte", water_quantity=20, coffee_quantity=2.4, milk_quantity=15),
    Drink(name="cappuccino", water_quantity=25, coffee_quantity=2.4, milk_quantity=10)
]
for drink in drink_list:
    drink.add_ingredient(ingredient_list)
coffee_maker.add_available_drinks(drink_list)
the_storage = coffee_maker.add_ingredient(ingredient_list)
money_machine.cost_to_fill_up_storage(the_storage)

machine_running = True
while machine_running:
    display.user_display()
    user_choice = user_input.take_text_input()
    if user_choice == "exit":
        display.goodbye()
        machine_running = False
    elif user_choice in ["espresso", "latte", "cappuccino", "admin"]:
        if user_choice == "admin":
            display.enter_admin_password()
            admin_logged_in = admin.check_login(user_input.take_number_input())
            while admin_logged_in:
                display.admin_panel_display()
                user_command = user_input.take_text_input()
                if user_command == "exit":
                    display.admin_log_out()
                    admin_logged_in = False
                elif user_command in ["1", "2", "3", "4", "5"]:
                    if user_command == "1":
                        display.check_money_earned(money_machine.earning)
                    elif user_command == "2":
                        display.check_money_spent(money_machine.spending)
                    elif user_command == "3":
                        display.check_storage(coffee_maker.storage)
                else:
                    display.invalid_input()
            else:
                display.incorrect_password()
        else:
            the_drink = coffee_maker.get_drink(user_choice)
            if the_drink:
                display.number_of_drink_needed(the_drink)
                number_of_drink = user_input.take_number_input()
                if number_of_drink:
                    if not coffee_maker.storage_checker(user_choice, number_of_drink):
                        the_bill = money_machine.calculate_bill(the_drink, number_of_drink)
                        if the_bill:
                            display.show_bill(the_bill)
                            display.want_to_proceed_purchase()
                            user_consent = user_input.take_text_input()
                            if user_consent == "y":
                                display.notes_accepted(money_machine.notes_accepted)
                                for note in money_machine.notes_accepted:
                                    display.enter_number_of_notes(note)
                                    number_of_note = user_input.take_number_input()
                                    money_machine.collect_payment(number_of_note)
                                purchase_done_or_not, refund = money_machine.check_payment(the_bill)
                                display.purchase_status(purchase_done_or_not, refund)
                                if purchase_done_or_not:
                                    coffee_maker.storage_reducer(the_drink, number_of_drink)
                                    money_machine.add_earning(the_bill)
                            else:
                                display.order_cancelled()
                        else:
                            display.invalid_input()
                    else:
                        display.storage_exceeds(the_drink, number_of_drink)
                else:
                    display.invalid_input()
            else:
                display.invalid_input()
    else:
        display.invalid_input()