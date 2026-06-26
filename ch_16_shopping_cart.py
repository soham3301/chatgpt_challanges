print("=== WELCOME TO PY-ECOMMERCE-APP")
product_list = ["Apple", "Banana", "Milk", "Bread", "Rice"]
print(f"Today we have {product_list}")
how_many = int(input("How many type of products do you need?\n"))

cart_list = []
individual_item_numbers = []

for _ in range(0, how_many):
    product_name = str(input("Which product do you need? Type here: "))
    if product_name in product_list:
        how_many_items = int(input(f"How many {product_name}s do you need?\n"))
        cart_list.append(product_name)
        individual_item_numbers.append(how_many_items)
    else:
        print("Choose items from the list above only")

print("Your Shopping Cart:")

for counter in range(0, len(cart_list)):
    print(f"{counter + 1}. {cart_list[counter]} x {individual_item_numbers[counter]}\n")