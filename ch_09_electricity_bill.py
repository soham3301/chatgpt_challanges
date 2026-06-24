#0–100 units → ₹5/unit
#101–200 → ₹7/unit
#201+ → ₹10/unit

unit_used = round(abs(float(input("Enter the electricity unit here: \n"))))
bill = 0

if unit_used <= 100:
    print(f"Your bill is {unit_used * 5}")
elif unit_used <= 200:
    print(f"Your bill is {unit_used * 7}")
elif unit_used > 200:
    print(f"Your bill is {unit_used * 10}")
else:
    print("Enter correct amount")