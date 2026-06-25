import random

cities = ["Delhi", "Mumbai", "Chennai", "Kolkata", "Hyderabad", "Pune", "Guwahati", "Chandigarh", "Bangaluru", "Goa"]

city_suggession = random.choice(cities)
print(f"Your next travel destination is: {city_suggession}")

user_input = input("Do you want another suggession? Y / N\n")

if user_input == "Y":
    while True:
        print(random.choice(cities))
        user_input_again = input("Do you want another suggession? Y / N\n")
        if user_input_again != "Y":
            print("Thanks. Enjoy Your Journey")
            break
elif user_input == "N":
    print("Thanks. Enjoy Your Journey")
else:
    print("You entered wrong input.")