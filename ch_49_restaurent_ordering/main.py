
from discount import Discount
from menuitem import MenuItem
from order import Order
from restaurent import Restaurent
from table import Table
from bill import Bill
from display import Display
from input import Input

restaurent = Restaurent()
display = Display()
user_input = Input()
discount = Discount()

items = [
    MenuItem("Pizza", 120),
    MenuItem("Pasta", 90),
    MenuItem("Lassi", 30),
    MenuItem("Eggroll", 40),
    MenuItem("Noodles", 70),
    MenuItem("Chicken65", 70),
    MenuItem("Biriyani", 160),
    MenuItem("Coke", 20),
]

tables = [
    Table(1, 2),
    Table(2, 2),
    Table(3, 4),
    Table(4, 4),
    Table(5, 4),
    Table(6, 4),
    Table(7, 6),
    Table(8, 6),
    Table(9, 8),
    Table(10, 8),
]

for item in items:
    restaurent.add_item(item)

for table in tables:
    restaurent.add_table(table)

table_selection = True

display.welcome_board()
number_of_people = user_input.ask_number_of_customers()
display.display_correct_tables(number_of_people, restaurent.list_of_tables)
choosen_table_number = user_input.choose_table_number()
if restaurent.table_chooser(choosen_table_number, number_of_people):
    while table_selection:
        display.display_menu(restaurent.list_of_items)
        menu_item, quantity = user_input.ask_item_details(restaurent.list_of_items)
        if menu_item == "Exit":
            table_selection = False
        elif menu_item and quantity:
            order = Order(menu_item, quantity)
            if order:
                restaurent.add_order(order)
        else:
            display.invalid_input()
    if restaurent.list_of_orders:
        the_bill = Bill(restaurent.list_of_orders)
        display.display_bill(the_bill)
        display.want_discount()
        if user_input.want_discount():
            the_discount_text = user_input.get_discount()
            if the_discount_text:
                if discount.check_discount(the_discount_text):
                    the_bill.apply_discount()
                    display.display_updated_bill(the_bill)
            else:
                display.invalid_input()
        restaurent.add_bill(the_bill)
        payment = user_input.ask_bill()
        if payment:
            the_return_amount, payment_complete = restaurent.payment_checker(the_bill.bill_amount, payment)
            if payment_complete and the_return_amount == 0:
                display.payment_done()
                restaurent.release_table(choosen_table_number)
            elif payment_complete:
                display.payment_done()
                display.take_return(the_return_amount)
                restaurent.release_table(choosen_table_number)
            else:
                display.payment_failed(the_bill.bill_amount, payment)
        else:
            display.invalid_input()
else:
    display.invalid_input()


        
        


