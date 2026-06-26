import random

# Creating a list from 1 to 100
full_list = []
for counter in range(1, 101):
    full_list.append(counter)

# Randomly selecting 5 unique numbers
random_numbers_list = []
for _ in range(0, 5):
    random_numbers_list.append(random.sample(full_list, k=5))

# Asking user for 5 guesses
print("Guess 5 numbers and enter them one by one | (1 to 100)")
user_guess_list = []
for _ in range(0, 5):
    user_guess_list.append(int(input("Enter a number: ")))

# Comparing items of both lists and creating the result
correct_number_counter = 0
for number in random_numbers_list:
    for counter in range(0, 5):
        if user_guess_list[counter] == number:
            correct_number_counter += 1

print(f"You have guessed {correct_number_counter} numbers correctly")


