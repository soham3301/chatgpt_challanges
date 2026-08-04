
from ingredients import Ingredient
from drinks import Drink
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine
from display import Display
from user_input import UserInput

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
        ...
    else:
        display.invalid_input()