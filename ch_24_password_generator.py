import random

letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

your_letters = 0
your_numbers = 0
your_symbols = 0

print("=== WELCOME TO THE PY-PASSWORD-GENERATOR ===")

def get_user_input():
    global your_letters
    global your_numbers
    global your_symbols
    your_letters = abs(int(input("How many letters would you like in your Password?\n")))
    your_numbers = abs(int(input("How many numbers would you like in your Password?\n")))
    your_symbols = abs(int(input("How many symbols would you like in yuor Password?\n")))

def generate_letters():
    password_only_letters = []
    for _ in range(0, your_letters):
        random_no_for_letters = random.randint(0, len(letters) - 1)
        password_only_letters.append(letters[random_no_for_letters])
        only_letters = "".join(password_only_letters)
    return only_letters

def generate_numbers():
    password_only_numbers = []
    for _ in range(0, your_numbers):
        random_no_for_numbers = random.randint(0, len(numbers) - 1)
        password_only_numbers.append(numbers[random_no_for_numbers])
        numbers_to_string = [str(num) for num in password_only_numbers]
        only_numbers = "".join(numbers_to_string)
    return only_numbers

def generate_symbols():
    password_only_symbols = []
    for _ in range(0, your_symbols):
        random_no_for_symbols = random.randint(0, len(symbols) - 1)
        password_only_symbols.append(symbols[random_no_for_symbols])
        symbols_to_string = [str(num) for num in password_only_symbols]
        only_symbols = "".join(symbols_to_string)
    return only_symbols

def create_password():
    final_password = []
    final_password.append(generate_letters())
    final_password.append(generate_numbers())
    final_password.append(generate_symbols())
    password_in_string_form = "".join(final_password)
    shuffled_password = "".join(random.sample(password_in_string_form, len(password_in_string_form)))
    return shuffled_password

def main():
    get_user_input()
    print(f"Your password will be: {create_password()}")

main()