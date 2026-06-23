number1 = int(input("Enter the first number: "))

print("Type '1' for addition")
print("Type '2' for subtraction")
print("Type '3' for multiplication")
print("Type '4' for division")

operation = int(input("Type here: "))

number2 = int(input("Enter the second number: "))

if operation == 1:
    print("The result is:", (number1 + number2))
elif operation == 2:
    print("The result is:", (number1 - number2))
elif operation == 3:
    print("The result is:", (number1 * number2))
elif operation == 4:
    if number2 == 0:
        print("Division by 0 is not allowed")
    else:
        print("The result is:", (number1 / number2))
else:
    print("Invalid Entry")