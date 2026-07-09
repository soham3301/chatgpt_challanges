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
}

cart = {}

def display_board():
    print("Choose item from below:")
    item_number = 0
    for item in available_items:
        item_number += 1
        print(f"{item_number}: {item}")

def user_input():
    try:
        user_choice = int(input(f'''
1. Add Item
2. Remove Item
3. View Cart
4. Checkout
5. Exit
'''))
        if user_choice == 5:
            print("Thanks for shopping with us.")
            return False, None
        elif user_choice in [1, 2, 3, 4]:
            return True, user_choice
        else:
            print("Choose from the numbers above.")
            return True, None
    except ValueError:
        print("Invalid Input | Closing Application.")
        return False, None

def add_item():
    display_board()
    print("===========")
    try:
        item_no = int(input("Choose Item No: "))
    except ValueError:
        print("Invalid Input | Try Again.")

def remove_item():
    print("Item Removed.")

def view_cart():
    print("Cart Viewed.")

def checkout():
    print("Checked Out.")

def mapping_user_input(the_number):
    saved_functions = {
        1: add_item,
        2: remove_item,
        3: view_cart,
        4: checkout,
    }
    if the_number in saved_functions:
        saved_functions[the_number]()

def main():
    application_running = True
    while application_running:
        application_running, user_choosen_number = user_input()
        mapping_user_input(user_choosen_number)

main()
