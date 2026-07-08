contacts = {
    "Alice":"9876543210",
    "Bob":"9988776655",
    "Soham":"9774495544",
}

def user_input():
    user_choice = int(input(f'''
1. Add Contact
2. Search Contact
3. Update Number
4. Delete Contact
5. Display All
6. Exit
'''))
    return user_choice

def add_contact():
    user_name = getting_user_name()
    if user_name in contacts:
        user_consent = input("Contact already exist. Update Instead? Y / N: ").lower()
        if user_consent == "y":
            update_number()
    else:
        mobile_no = input("Enter Number: ")
        contacts[user_name] = mobile_no
        print("Contact Added")

def search_contact():
    contacts_copy = contacts.copy()
    contacts_copy_lower = {}
    for key in contacts_copy:
        contacts_copy_lower[key.lower()] = contacts_copy[key]
    user_name = getting_user_name().lower()
    if user_name in contacts_copy_lower:
        print(f"Contact Found | Name: {user_name.title()}, Number: {contacts_copy[user_name.title()]}")
    else:
        contact_not_exist()
    return None

def update_number():
    user_name = getting_user_name()
    if user_name in contacts:
        user_mobile_no = str(input("Enter Mobile No: "))
        contacts[user_name] = user_mobile_no
        print("Contact Updated")
    else:
        contact_not_exist()
    return None

def delete_contact():
    user_name = getting_user_name()
    if user_name in contacts:
        contacts.pop(user_name)
        print("Contact Deleted")
    else:
        contact_not_exist()
    return None

def display_all():
    for key, value in contacts.items():
        print(f"{key}: {value}")
    return None

def getting_user_name():
    user_name = input("Enter Name: ").title()
    return user_name

def contact_not_exist():
    print("This contact doesn't exist.")

def mapping_user_input(user_choice):
    saved_functions = {
        1: add_contact,
        2: search_contact,
        3: update_number,
        4: delete_contact,
        5: display_all,
    }
    if user_choice == 6:
        print("Thanks for using Contact Book.")
        return False
    elif user_choice in saved_functions:
        saved_functions[user_choice]()
        return True
    else:
        print("Please enter valid Input.")
        return True

def main():
    program_continues = True
    while program_continues:
        user_choice = user_input()
        program_continues = mapping_user_input(user_choice)

main()