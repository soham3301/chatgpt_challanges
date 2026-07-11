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

display_password = "123@321"

def display_board():
    print('''
1. Save Password
2. Update Password
3. Search Website
4. Delete
5. Display
6. Exit
''')

def user_input():
    display_board()
    try:
        user_choice = int(input("Choose a number from above: "))
        if user_choice == 6:
            print("Thanks for using our Password Manager.")
            return False, None
        elif user_choice in [1, 2, 3, 4, 5]:
            return True, user_choice
        else:
            print("Please choose from the numbers above.")
            return True, None
    except ValueError:
        print("That's not a number ! Closing Application")
        return False, None

def getting_the_url():
    return input("Enter website URL: ").lower()

def getting_user_credentials():
    website_username = input("Enter Username: ")
    website_password = input("Enter Password: ")
    user_credentials = {
            "username":website_username,
            "password":website_password
        }
    return user_credentials

def display_password_checker():
    your_display_password = input("Enter Password to View: ")
    if your_display_password == display_password:
        return True
    else:
        print("Sorry Password didn't match.")
        return False

def display_single_details(the_url):
    print(f'''
Website: {the_url}
Username: {passwords[the_url]["username"]} | Password: {passwords[the_url]["password"]}''')

def display_all_details():
    for url in passwords:
        print(f"Website: {url} >>> Username: {passwords[url]["username"]} | Password: {passwords[url]["password"]}")

def save_credentials(the_url):
    user_creds = getting_user_credentials()
    passwords[the_url] = user_creds
    print("Credentials Saved")

def update_credentials(the_url):
    old_password = input(f"Enter your old password for '{passwords[the_url]["username"]}': ")
    if old_password == passwords[the_url]["password"]:
        new_password = input("Enter your new Password: ")
        passwords[the_url]["password"] = new_password
        print(f"Password Updated for {passwords[the_url]["username"]} Username.")
    else:
        print("Password didn't match. Try later.")

def save_password():
    website_url = getting_the_url()
    if website_url in passwords:
        want_to_update = input(f"Username and Password for {website_url} are already saved. Want to Update? Y / N\n").lower()
        if want_to_update == "y":
            update_credentials(website_url)
    else:
        save_credentials(website_url)

def update_password():
    website_url = getting_the_url()
    if website_url in passwords:
        update_credentials(website_url)
    else:
        user_consent = input(f"No login credentials found for {website_url}. Want to Save? Y / N\n").lower()
        if user_consent == "y":
            save_credentials(website_url)
    return True

def search_website():
    website_url = getting_the_url()
    if website_url in passwords:
        want_details = input(f"Website Found | You have saved login credentials for {website_url}. Want to view the login credentials? Y / N\n").lower()
        if want_details == "y":
            if display_password_checker():
                display_single_details(website_url)
    else:
        want_to_add = input("No Credentials found. Want to add? Y / N\n").lower()
        if want_to_add == "y":
            save_credentials(website_url)
    return True

def delete():
    website_url = getting_the_url()
    if website_url in passwords:
        ask_user = input(f"You want to delete saved password of {website_url}? Y / N\n").lower()
        if ask_user == "y":
            passwords.pop(website_url)
            print(f"Login Credentials DELETED for {website_url}")
    else:
        print(f"You don't have any saved credentials of {website_url}")
    return True

def display():
    if display_password_checker():
        items_counter = 1
        url_list = []
        for item in passwords:
            print(f"{items_counter}: {item}")
            items_counter += 1
            url_list.append(item)
        print(f"{items_counter}: All of the above.")
        try:
            choose_number = int(input("Choose a number from Above: "))
            if choose_number == items_counter:
                display_all_details()
            elif choose_number >= 1 and choose_number <= len(url_list):
                display_single_details(url_list[choose_number - 1])
            else:
                print("Wrong Input.")
        except ValueError:
            print("Invalid Input.")

def mapping_user_input(user_input):
    saved_functions = {
        1: save_password,
        2: update_password,
        3: search_website,
        4: delete,
        5: display,
    }
    if user_input in saved_functions:
        saved_functions[user_input]()

def main():
    program_running = True
    while program_running:
        program_running, user_choice = user_input()
        mapping_user_input(user_choice)

main()