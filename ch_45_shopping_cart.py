
#! Note:- Here user can't add products to the shop. The user can only add, remove, increase quantity or decrease quantity of products from the cart.
#! This application is from completely users perspective.
#! When users adds a product inside cart, it's default quantity is set to 1. After that the user can increase or decrease items inside cart.

logo = '''
▗▖ ▗▖▗▄▄▄▖▗▖    ▗▄▄▖ ▗▄▖ ▗▖  ▗▖▗▄▄▄▖    ▗▄▄▄▖▗▄▖     ▗▄▄▄▖▗▖ ▗▖▗▄▄▄▖     ▗▄▄▖ ▗▄▖ ▗▄▄▖▗▄▄▄▖
▐▌ ▐▌▐▌   ▐▌   ▐▌   ▐▌ ▐▌▐▛▚▞▜▌▐▌         █ ▐▌ ▐▌      █  ▐▌ ▐▌  █      ▐▌   ▐▌ ▐▌▐▌ ▐▌ █  
▐▌ ▐▌▐▛▀▀▘▐▌   ▐▌   ▐▌ ▐▌▐▌  ▐▌▐▛▀▀▘      █ ▐▌ ▐▌      █  ▐▌ ▐▌  █      ▐▌   ▐▛▀▜▌▐▛▀▚▖ █  
▐▙█▟▌▐▙▄▄▖▐▙▄▄▖▝▚▄▄▖▝▚▄▞▘▐▌  ▐▌▐▙▄▄▖      █ ▝▚▄▞▘      █  ▝▚▄▞▘▗▄█▄▖    ▝▚▄▄▖▐▌ ▐▌▐▌ ▐▌ █  
'''

class Product:
    def __init__(self, name, price, quantity):
        self.name = name
        self.price = price
        self.quantity = quantity

class ProductInsideCart(Product):
    def __init__(self, name, price, quantity):
        super().__init__(name, price, quantity)

class Cart:
    def __init__(self, product_list):
        self.list_from_shop = product_list
        self.list_for_checkout = []
    
    def find_product_from_shop(self, name):
        for product in self.list_from_shop:
            if product.name == name:
                return product
        return None
    
    def find_product_from_checkout_list(self, name):
        for product in self.list_for_checkout:
            if product.name == name:
                return product
        return None
    
    def cart_checker(self, product):
        for items in self.list_for_checkout:
            if items.name == product.name:
                return True
        return False

    def add_product(self, the_name):
        the_product = self.find_product_from_shop(the_name)
        if the_product:
            if not self.cart_checker(the_product):
                inside_cart_product = ProductInsideCart(the_product.name, the_product.price, 1)
                the_product.quantity -= 1               #! Needs a stock Checker
                self.list_for_checkout.append(inside_cart_product)
                return True
            else:
                return False
        else:
            return False

    def remove_product(self, the_name):
        the_product = self.find_product_from_shop(the_name)
        if the_product:
            if self.cart_checker(the_product):
                for item in self.list_for_checkout:
                    if item.name == the_product.name:
                        self.list_for_checkout.remove(item)
                        the_product.quantity += 1
                        return True
                return False
            else:
                return False
        else:
            return False

    def increase_quantity(self, the_name, the_quantity):
        the_product = self.find_product_from_shop(the_name)
        the_product_from_checkout = self.find_product_from_checkout_list(the_name)
        if the_product and the_product_from_checkout:
            if the_product.quantity >= the_quantity:
                the_product_from_checkout.quantity += the_quantity
                the_product.quantity -= the_quantity
                return True
            else:
                return False
        else:
            return False

    def decrease_quantity(self, the_name, the_quantity):
        the_product = self.find_product_from_shop(the_name)
        the_product_from_checkout = self.find_product_from_checkout_list(the_name)
        if the_product and the_product_from_checkout:
            if the_product_from_checkout.quantity > the_quantity:
                the_product_from_checkout.quantity -= the_quantity
                the_product.quantity += the_quantity
                return True
            else:
                return False
        else:
            return False
    
    def clear_cart(self):
        for product in self.list_from_shop:
            for product_for_sale in self.list_for_checkout:
                if product_for_sale.name == product.name:
                    quantity = product_for_sale.quantity
                    product.quantity += quantity
                    self.list_for_checkout.remove(product_for_sale)
        return True

    def show_all_products(self):
        return self.list_from_shop
    
    def show_cart(self):
        return self.list_for_checkout

class Checkout:
    def __init__(self, product_list_for_checkout):
        self.product_list = product_list_for_checkout
    
    def total_bill(self):
        bill = 0
        if self.product_list:
            for item in self.product_list:
                bill += item.price * item.quantity
            return bill
        else:
            return False
    
    def checkout(self):
        self.product_list.clear()

def display_board():
    print('''
1. Add Products
2. Remove Products
3. Increase Quantity
4. Decrease Quantity
5. Show All Products
6. Show Cart
7. Clear Cart
8. Check Total Bill
9. Checkout
0. Exit
''')

def user_input():
    try:
        user_choice = int(input("Choose from above: "))
        if user_choice == 0:
            print("Thanks for using TUI Cart.")
            return False, None
        elif user_choice in [1, 2, 3, 4, 5, 6, 7, 8, 9]:
            return True, user_choice
        else:
            helper_invalid_input()
            return True, None
    except ValueError:
        helper_invalid_input()
        return True, None

def helper_invalid_input():
    print("Invalid Input")

def get_product_name():
    name = input("Enter Product Name: ")
    if name:
        return name
    else:
        helper_invalid_input()
        return None

def get_product_name_and_quantity():
    name = get_product_name()
    try:
        quantity = int(input("Enter Product Quantity: "))
        return name, quantity
    except ValueError:
        helper_invalid_input()
        return None, None

def display_shop(shop_product_list):
    for product in shop_product_list:
        print(f"{product.name} x {product.quantity}")

def display_cart(cart_product_list):
    for product in cart_product_list:
        print(f"{product.name} x {product.quantity} | Total: {product.quantity * product.price} INR")

def command_mapper(user_input, the_cart):
    saved_functions = {
        1: get_product_name,
        2: get_product_name,
        3: get_product_name_and_quantity,
        4: get_product_name_and_quantity,
        5: the_cart.show_all_products,
        6: the_cart.show_cart,
        7: the_cart.clear_cart,
    }
    functions_with_interaction = {
        1: the_cart.add_product,
        2: the_cart.remove_product,
        3: the_cart.increase_quantity,
        4: the_cart.decrease_quantity,
    }
    display_successfull_notices = {
        1: "Product Added",
        2: "Product Removed",
        3: "Quantity Increased",
        4: "Quantity Decreased",
        5: display_shop,
        6: display_cart,
    }
    display_failed_notices = {
        1: "Failed to Add Product",
        2: "Failed to Remove Product",
        3: "Failed to Increase Quantity",
        4: "Failed to Decrease Quantity",
        5: "Failed to Display All Shop Products",
        6: "Cart is empty as of now"
    }
    if user_input in [1, 2]:
        name = saved_functions[user_input]()
        if name:
            if functions_with_interaction[user_input](name):
                print(f"{display_successfull_notices[user_input]}")
            else:
                print(f"{display_failed_notices[user_input]}")
        else:
            helper_invalid_input()
    elif user_input in [3, 4]:
        the_name, how_many = saved_functions[user_input]()
        if the_name and how_many:
            if functions_with_interaction[user_input](the_name, how_many):
                print(f"{display_successfull_notices[user_input]}")
            else:
                print(f"{display_failed_notices[user_input]}")
    elif user_input in [5, 6]:
        received_list = saved_functions[user_input]()
        if received_list:
            display_successfull_notices[user_input](received_list)
        else:
            print(f"{display_failed_notices[user_input]}")
    else:
        saved_functions[user_input]()
        print("Cart Cleared")

def pay_bill(total_amount):
    try:
        pay = abs(round(int(input("Enter Amount: "))))
        if pay >= total_amount:
            if pay > total_amount:
                print(f"Here is your refund: INR {pay - total_amount} /-")
                return True
            return True
        else:
            return False
    except ValueError:
        helper_invalid_input()
        return False

def main():
    demo_products_list = [
        Product("IPhone", 88000, 35),
        Product("Compression T Shirt", 1599, 100),
        Product("Mango", 75, 550),
        Product("Milk", 200, 220),
        Product("Sports Shoe", 3550, 150),
    ]
    my_cart = Cart(demo_products_list)
    print(logo)
    while True:
        display_board()
        application_running, user_choice = user_input()
        if not application_running:
            break
        elif user_choice in [1, 2, 3, 4, 5, 6, 7]:
            command_mapper(user_choice, my_cart)
        elif user_choice in [8, 9]:
            checkout_list = my_cart.show_cart()
            if checkout_list:
                the_checkout = Checkout(checkout_list)
                total_bill = the_checkout.total_bill()
                if user_choice == 8 and total_bill:
                    print(f"Here is your Total Bill: INR {total_bill}/-")
                else:
                    if pay_bill(total_bill):
                        the_checkout.checkout()
                        print("Purchase Successfull.")
                    else:
                        print("Purchase Unsuccessfull.")
            else:
                print("Your cart is Empty as of now.")

main()