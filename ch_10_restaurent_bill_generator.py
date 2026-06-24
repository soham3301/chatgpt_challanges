#Burger = ₹120
#Pizza = ₹250
#Pasta = ₹180

#What would you like?
#Burger/Pizza/Pasta

bill = 0

print("What would you like?")

item_name = input("Burger / Pizza / Pasta?\n").lower()

#How many items?

number_of_items = int(input(f"How many {item_name}s would you like to have?\n"))

#Do you want a cold drink? Y/N (₹40)

cold_drink = input("Do You want cold drink? Y / N\n").lower()

if item_name == "burger":
    bill += 120
elif item_name == "pizza":
    bill += 250
elif item_name == "pasta":
    bill += 180
else:
    print(f"We don't have {item_name} as of now")

if cold_drink == "y":
    bill = bill * number_of_items + 40
    print(f"Your total bill is: {bill}")
else:
    bill = bill * number_of_items
    print(f"Your total bill is: {bill}")