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

def display_menu():
    user_input = int(input('''
1. Add Item
2. Sell Item
3. Restock Item
4. Show Inventory
5. Exit
'''))
    return user_input

def main():
    display_menu()

main()