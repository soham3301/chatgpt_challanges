#Age <= 12      → ₹100
#Age 13-59      → ₹200
#Age 60+        → ₹150
#Popcorn        → ₹60

age = int(input("Enter your age: \n"))
bill = 0
popcorn = input("Do you want to add 'Popcorn'? y / n\n")

if (age <= 12):
    bill += 100
    print(f"Your bill is ₹{bill}")
elif (age < 60):
    bill += 200
    print(f"Your bill is ₹{bill}")
else:
    bill += 150
    print(f"Your bill is {150}")

if (popcorn == "y"):
    bill += 60
    print(f"Your bill with popcorn is {bill}")