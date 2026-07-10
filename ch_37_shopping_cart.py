available_items = {
    "Milk":{
        "price":40,
        "stock":20,
    },
    "Bread":{
        "price":15,
        "stock":45,
    },
    "Egg":{
        "price":12,
        "stock":30,
    },
    "Apple":{
        "price":45,
        "stock":55,
    },
    "Noodles":{
        "price":25,
        "stock":75,
    }
}

my_cart = {}

def display_board_and_user_input():
    print("Choose item from below:")
    for item in available_items:
        print(item)
    print("===========")
    return input("Choose Item: ").title()

def user_input():
    try:
        user_choice = int(input(f'''
1. Add Item
2. Remove Item
3. View Cart
4. Exit

Enter Number: '''))
        if user_choice == 4:
            print("Thanks for shopping with us.")
            return False, None
        elif user_choice in [1, 2, 3]:
            return True, user_choice
        else:
            print("Choose from the numbers above.")
            return True, None
    except ValueError:
        print("Invalid Input | Closing Application.")
        return False, None

def add_item():
    item_name = display_board_and_user_input()
    if item_name in available_items:
        try:
            print(f"We have {available_items[item_name]["stock"]} {item_name}s available")
            how_many = int(input(f"How many {item_name} do you need?\n"))
            item_stock = available_items[item_name]["stock"]
            if item_stock >= how_many:
                available_items[item_name]["stock"] -= how_many
                adding_to_cart(item_name, how_many)
                print(f"{how_many} {item_name}s are added into your cart.")
                print(f"Item remains: {available_items[item_name]["stock"]} in shop.")
            else:
                print(f"We only have {item_stock} number of {item_name} as of now.")
        except ValueError:
            print("Kindly Enter numerical value.")
    else:
        print("This item is not available in the shop as of now.")

def remove_item():
    item_name = display_board_and_user_input()
    if item_name in my_cart:
        try:
            print(f"You have {my_cart[item_name]["quantity"]} {item_name}s in your cart.")
            how_many = int(input(f"How many {item_name} you want to remove?\n"))
            item_quantity = my_cart[item_name]["quantity"]
            if how_many == item_quantity:
                my_cart.pop(item_name)
                removing_from_cart(item_name, how_many)
            elif item_quantity >= how_many:
                my_cart[item_name]["quantity"] -= how_many
                removing_from_cart(item_name, how_many)
                print(f"{how_many} {item_name}s are removed from your cart.")
                print(f"Item remains in cart: {my_cart[item_name]["quantity"]}")
            else:
                print(f"You have only {item_quantity} number of {item_name} inside your cart.")
        except ValueError:
            print("Kindly enter a numerical value.")
    else:
        print("This item is not inside your cart.")

def view_cart():
    item_number_counter = 0
    if len(my_cart) == 0:
        user_consent = input("Your cart is empty. Want to add some items? Y / N: ").lower()
        if user_consent == "y":
            add_item()
    else:
        for item in my_cart:
            item_number_counter += 1
            print(f"{item_number_counter}: {item} x {my_cart[item]["quantity"]}")
        checkout()

def bill_generator():
    total_bill = 0
    for item in my_cart:
        print(f" {item} x {my_cart[item]["quantity"]} = ${my_cart[item]["quantity"] * my_cart[item]["price"]}")
        total_bill += my_cart[item]["quantity"] * my_cart[item]["price"]
    print(f"Your total bill is: {total_bill}")
    return total_bill

def checkout():
    want_to_checkout = input("Want to checkout? Y / N : ").lower()
    if want_to_checkout == "y":
        bill_amount = bill_generator()
        try:
            confirm_purchase = input("Confirm Purchase? Y / N: ").lower()
            if confirm_purchase == "y":
                pay_bill = int(input("Enter the bill amount?\n"))
                if pay_bill == bill_amount:
                    my_cart.clear()
                    print(f"You paid ${pay_bill}. Your Purchase is Successful.")
                else:
                    print(f"You paid ${pay_bill} which is not equel to {bill_amount}. Purchase Unsuccessful.")
        except ValueError:
            print("Invalid Amount Entered.")
        return False
    else:
        return True

def adding_to_cart(product_name, product_quantity):
    if product_name in my_cart:
        my_cart[product_name]["quantity"] += product_quantity
    else:
        my_cart[product_name] = {
                "price": available_items[product_name]["price"],
                "quantity":product_quantity,
            }

def removing_from_cart(product_name, removed_quantity):
    total_stock = available_items[product_name]["stock"] + removed_quantity
    item_price = available_items[product_name]["price"]
    available_items[product_name] = {
        "price":item_price,
        "stock":total_stock
    }

def mapping_user_input(the_number):
    saved_functions = {
        1: add_item,
        2: remove_item,
        3: view_cart,
    }
    if the_number in saved_functions:
        saved_functions[the_number]()

def main():
    application_running = True
    while application_running:
        application_running, user_choosen_number = user_input()
        mapping_user_input(user_choosen_number)

main()
