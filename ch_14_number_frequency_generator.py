print("You have to enter 10 numbers")

numbers_list = []
for numbers in range(0, 10):
    user_input = int(input("Enter the numbers one by one:\n"))
    numbers_list.append(user_input)

#Largest number:
largest_number = 0
for counter in numbers_list:
    if largest_number < counter:
        largest_number = counter
print(f"Largest Number: {largest_number}")

#Smallest number:
smallest_number = numbers_list[0]
for counter in numbers_list:
    if smallest_number > counter:
        smallest_number = counter
print(f"Smallest Number: {smallest_number}")

#Average:
total = 0
for counter in numbers_list:
    total += counter
average = total / len(numbers_list)
print(f"Average: {average}")