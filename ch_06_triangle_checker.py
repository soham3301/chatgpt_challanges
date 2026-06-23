# Equilateral = all sides equal
# Isosceles = two sides equal
# Scalene = Scalene

side_one = int(input("Enter length of first side: \n"))
side_two = int(input("Enter length of second side: \n"))
side_three = int(input("Enter length of third side: \n"))

if (side_one == side_two and side_one == side_three):
    print("It's an Equilateral Triangle")
elif (side_one == side_two or side_one == side_three):
    print("It's an Isosceles Triangle")
else:
    print("It's a Scalene Triangle")