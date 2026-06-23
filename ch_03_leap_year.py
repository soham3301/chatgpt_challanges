#Divisible by 4 → leap year
#BUT if divisible by 100 → not leap year
#EXCEPT if divisible by 400 → leap year

year = int(input("Enter the year: \n"))

if (year % 400 == 0):
    print("It's a LEAP YEAR")
elif (year % 100 == 0):
    print("No it's NOT")
elif (year % 4 == 0):
    print("Yeah It's a LEAP YEAR")
else:
    print("You entered the wrong digits")
