#0–100 units → ₹5/unit
#101–200 → ₹7/unit
#201+ → ₹10/unit

unit_used = round(abs(float(input("Enter the electricity unit here: \n"))))
bill = 0
tracker = 0

if unit_used <= 100:
    tracker = 5
    bill = unit_used * tracker
    print(f"Your bill is {bill}")
elif unit_used <= 200:
    tracker = 7
    bill = unit_used * tracker
    print(f"Your bill is {bill}")
elif unit_used > 200:
    tracker = 10
    bill = unit_used * tracker
    print(f"Your bill is {bill}")
else:
    print("Enter correct amount")