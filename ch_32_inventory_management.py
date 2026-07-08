inventory = {
    "Apple": {
        "price":120,
        "stock":25
    },
    "Banana":{
        "price":40,
        "stock":80
    }
}

treasury = {
    "cash_balance": 10000,
}

def display_menu():
    user_input = int(input('''
1. Add Item
2. Sell Item
3. Restock Item
4. Show Inventory
5. Show Cash Balance
6. Exit
'''))
    return user_input

def add_item():
    item_name = str(input("Enter Item Name: ")).title()
    item_price = int(input("Enter Item Price: "))
    item_stock = int(input("Enter Item Stock: "))
    if item_name not in inventory:
        total_buying_cost = item_price * item_stock
        if total_buying_cost > treasury["cash_balance"]:
            print(f"You only have ${treasury['cash_balance']} in hand. Can't add Item.")
        elif total_buying_cost <= 0:
            print("Sorry Invalid Input")
        else:
            inventory[item_name] = {
                "price": item_price,
                "stock": item_stock,
            }
            cash_spent = item_price * item_stock
            print(f"{item_stock} {item_name}s added into your Inventory. ${cash_spent} spent.")
            treasury["cash_balance"] -= cash_spent

def sell_item():
    item_name = input("Enter Item Name: ").title()
    if item_name in inventory:
        how_many = int(input(f"How many {item_name}s do you need?: "))
        if how_many <= 0:
            print("Please enter a valid number for purchase.")
        elif how_many > inventory[item_name]["stock"]:
            print(f"We have limited stocks. Kindly choose less than {inventory[item_name]["stock"]} {item_name}s")
        else:
            inventory[item_name]["stock"] -= how_many
            cash_received = inventory[item_name]["price"] * how_many
            print(f"{how_many} {item_name}s Sold. {inventory[item_name]["stock"]} remains in stock. ${cash_received} earned.")
            treasury["cash_balance"] += cash_received
    else:
        print("Sorry. We don't have this item yet.")

def restock_item():
    item_name = input("Enter Item Name: ").title()
    if item_name in inventory:
        item_stock = int(input(f"How many {item_name}s you want to re-stock?: "))
        total_cost = inventory[item_name]["price"] * item_stock
        if total_cost <= 0:
            print("Please enter a valid number for re-stock.")
        elif treasury["cash_balance"] < total_cost:
            print(f"Our have limited cash balance. Kindly choose less {item_name}s for re-stock.")
        else:
            inventory[item_name]["stock"] += item_stock
            print(f"{item_stock} {item_name}s re-stocked. ${total_cost} spent.")
            treasury["cash_balance"] -= total_cost
    else:
        print("We don't have this Item in our Inventory Yet.")
        add_item_to_stock = str(input("Want to add this Item in stock? 'Y' for YES, 'N' for NO.\n")).lower()
        if add_item_to_stock == "y":
            add_item()

def show_inventory():
    for key, value in inventory.items():
        print(f"{key}")
        for details, numbers in value.items():
            print(f"{details}: {numbers}")

def show_cash_balance():
    print(f"You have ${treasury['cash_balance']} in hand.")

def mapping_user_input(user_choice):
    saved_functions = {
        1: add_item,
        2: sell_item,
        3: restock_item,
        4: show_inventory,
        5: show_cash_balance,
    }
    if user_choice == 6:
        print("Thanks for using Soham's Inventory Management.")
        return False
    elif user_choice in saved_functions:
        saved_functions[user_choice]()
        return True
    else:
        print("Invalid Input | Closing Applicaiton.")
        return False, None

def main():
    application_stopper = True
    while application_stopper:
        user_input = display_menu()
        application_stopper = mapping_user_input(user_input)

main()