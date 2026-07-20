
demo_products = [
    {
    "name": "Laptop",
    "price": 47599,
    "quantity":5,
    "category":"Electronics",
    "supplier":"Apple",
}, {
    "name":"Mobile",
    "price":25000,
    "quantity":20,
    "category":"Electronics",
    "supplier":"Google",
}, {
    "name":"Black Trackpant",
    "price":1900,
    "quantity":155,
    "category":"Clothing",
    "supplier":"Boldfit",
}, {
    "name":"Dry Fruit Muesli",
    "price":599,
    "quantity":50,
    "category":"Food",
    "supplier":"Saffola",
}
]

class Product:
    def __init__(self, name, price, quantity, category, supplier):
        self.name = name
        self.price = price
        self.quantity = quantity
        self.category = category
        self.supplier = supplier

class Inventory:
    def __init__(self, product_list):
        self.product_list = product_list
    
    def helper_product_finder(self, name_of_product):
        for product in self.product_list:
            if product.name == name_of_product:
                return product
    
    def add_quantity(self, product_name, how_many):
        the_product = self.helper_product_finder(product_name)
        the_product.quantity += how_many
        print(f"{how_many} {the_product.name}s Added.")
    
    def remove_quantity(self, product_name, how_many):
        the_product = self.helper_product_finder(product_name)
        if how_many <= the_product.quantity:
            the_product.quantity -= how_many
            print(f"{how_many} {the_product.name}s Removed.")
        else:
            print(f"Stock is only {the_product.quantity}. Can't remove {how_many} out of {the_product.quantity}.")
    
    def search_product(self, product_name):
        the_product = self.helper_product_finder(product_name)
        if the_product:
            print(f"Product Found | We have {the_product.quantity} {the_product.name}s in our inventory right now | This {the_product.category} product is priced at INR {the_product.price} and came from {the_product.supplier}")
            return
        else:
            print(f"We don't have {product_name} in our inventory as of now.")
    
    def show_inventory(self):
        for product in self.product_list:
            print(f"Name: {product.name}, Price: {product.price}, Quantity: {product.quantity}, Category: {product.category}, Supplier: {product.supplier}")
    
    def check_low_stock(self, number):
        low_stock_items = []
        for product in self.product_list:
            if product.quantity < number:
                low_stock_items.append(product)
        if len(low_stock_items) > 0:
            for item in low_stock_items:
                print(f"We have only {item.quantity} {item.name}s")
        else:
            print("We have sufficient number of all products as of now.")
    
    def check_category(self):
        category_set = set()
        for product in self.product_list:
            category_set.add(product.category)
        print("We have these categories")
        for category in category_set:
            print(f"{category}")
    
    def check_supplier(self):
        supplier_set = set()
        for product in self.product_list:
            supplier_set.add(product.supplier)
        print("These are our supplier")
        for supplier in supplier_set:
            print(f"{supplier}")
    
    def add_a_new_product(self, the_product):
        self.product_list.append(the_product)
        print("Product Added to Inventory")
    
    def remove_existing_product(self, product_name):
        the_product = self.helper_product_finder(product_name)
        self.product_list.remove(the_product)
        print("Item Removed from Inventory")

def helper_invalid_input():
    print("Invalid Input")

def display_board():
    print('''
1. Add Quantity
2. Remove Quantity
3. Search Product
4. Show Inventory
5. Check Low Stock
6. Check Category
7. Check Supplier
8. Add a new Product
9. Remove an existing Product
0. Exit
''')

def user_input():
    try:
        user_choice = int(input("Choose from above: "))
        if user_choice == 0:
            print("Closing Application.")
            return False, None
        elif user_choice in [1, 2, 3, 4, 5, 6, 7, 8, 9]:
            return True, user_choice
        else:
            helper_invalid_input()
            return True, None
    except ValueError:
        helper_invalid_input()
        return True, None

def get_product(whole_inventory):
    product_name = input("Enter Product Name: ").title()
    for product in whole_inventory.product_list:
        if product.name == product_name:
            try:
                product_quantity = int(input("Enter Product Quantity: "))
                return product_name, product_quantity
            except ValueError:
                helper_invalid_input()
                return None, None
    print("Sorry we don't have this product")
    return None, None

def get_product_name_only(whole_inventory):
    product_name = input("Enter Product Name: ").title()
    for product in whole_inventory.product_list:
        if product.name == product_name:
            return product_name
    print("Sorry we don't have this product")
    return None

def add_product_details():
    name = input("Enter Product Name: ").title()
    try:
        price = abs(round(int(input("Enter Product Price: "))))
        quantity = abs(round(int(input("Enter Quantity: "))))
    except ValueError:
        helper_invalid_input()
    category = input("Enter Which Category this Product belongs: ").title()
    supplier = input("Enter Supplier Name: ").title()
    if name and price and quantity and category and supplier:
        return Product(name, price, quantity, category, supplier)
    else:
        return None

def low_stock_number():
    try:
        the_number = abs(round(int(input("Enter the standard quantity of products: "))))
        if the_number:
            return the_number
        else:
            return None
    except ValueError:
        helper_invalid_input()
        return None

def command_mapper(the_inventory, user_input):
    saved_functions = {
        1: get_product,
        2: get_product,
        3: get_product_name_only,
        4: the_inventory.show_inventory,
        5: low_stock_number,
        6: the_inventory.check_category,
        7: the_inventory.check_supplier,
        8: add_product_details,
        9: get_product_name_only,
    }
    functions_with_user_interaction = {
        1: the_inventory.add_quantity,
        2: the_inventory.remove_quantity,
        3: the_inventory.search_product,
        5: the_inventory.check_low_stock,
        8: the_inventory.add_a_new_product,
        9: the_inventory.remove_existing_product,
    }
    if user_input in [1, 2]:
        product_name, product_quantity = saved_functions[user_input](the_inventory)
        if product_name:
            functions_with_user_interaction[user_input](product_name, product_quantity)
    elif user_input in [3, 9]:
        product_name = saved_functions[user_input](the_inventory)
        if product_name:
            functions_with_user_interaction[user_input](product_name)
    elif user_input == 8:
        added_product = saved_functions[user_input]()
        if added_product:
            functions_with_user_interaction[user_input](added_product)
        else:
            print("Wrong Value Entered. Can't Proceed")
    elif user_input == 5:
        the_number = saved_functions[user_input]()
        if the_number:
            functions_with_user_interaction[user_input](the_number)
    elif user_input in saved_functions:
        saved_functions[user_input]()

def main():
    product_list = []
    for product in demo_products:
        product_list.append(Product(product["name"], product["price"], product["quantity"], product["category"], product["supplier"]))
    inventory = Inventory(product_list)
    while True:
        display_board()
        program_running, user_choice = user_input()
        if not program_running:
            break
        else:
            command_mapper(inventory, user_choice)

main()

    