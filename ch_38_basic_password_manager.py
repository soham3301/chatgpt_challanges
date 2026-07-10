passwords = {
    "www.gmail.com":{
        "username":"soham@gmail.com",
        "password":"abc123"
    },
    "www.facebook.com":{
        "username":"soham099009",
        "password":"303@soham"
    },
    "www.mybank.com":{
        "username":"fin03soham",
        "password":"Soham@1234"
    }
}

def display_board():
    print('''
1. Save Password
2. Search Website
3. Delete
4. Display
5. Exit
''')

def user_input():
    display_board()
    try:
        user_choice = int(input("Choose a number from above: "))
        if user_choice == 5:
            print("Thanks for using our Password Manager.")
            return False, None
        elif user_choice in [1, 2, 3, 4]:
            return True, user_choice
        else:
            print("Please choose from the numbers above.")
            return True, None
    except ValueError:
        print("That's not a number ! Closing Application")
        return False, None

def save_password():
    print("Password Saved")
    return True

def search_website():
    print("Website Searched")
    return True

def delete():
    print("Deleted")
    return True

def display():
    print("Displayed")
    return True

def mapping_user_input(user_input):
    saved_functions = {
        1: save_password,
        2: search_website,
        3: delete,
        4: display,
    }
    if user_input in saved_functions:
        saved_functions[user_input]()

def main():
    program_running = True
    while program_running:
        program_running, user_choice = user_input()
        mapping_user_input(user_choice)

main()