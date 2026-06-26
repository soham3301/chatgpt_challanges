print("=== WELCOME TO PY-ECOMMERCE-APP")
product_list = ["Apple", "Banana", "Milk", "Bread", "Rice"]
lowercase_product_list = [products.lower() for products in product_list]
print(f"Today we have {product_list}")
how_many = abs(int(input("How many type of products do you need?\n")))

cart_list = []
individual_item_numbers = []

for _ in range(0, how_many):
    product_name = str(input("Which product do you need? Type here: ")).lower()
    if product_name in lowercase_product_list:
        if product_name in cart_list:
            print(f"{product_name} is already in your cart")
        else:
            how_many_items = int(input(f"How many {product_name}s do you need?\n"))
            cart_list.append(product_name)
            individual_item_numbers.append(how_many_items)
    else:
        print(f"{product_name} doesn't exist")

if how_many == 0:
    print("You have entered 0 items.")
else:
    print("Your Shopping Cart:")

for counter in range(0, len(cart_list)):
    print(f"{counter + 1}. {cart_list[counter]} x {individual_item_numbers[counter]}\n")