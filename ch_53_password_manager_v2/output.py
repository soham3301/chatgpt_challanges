
class Output:
    def __init__(self):
        self.name = "Console Output"

    def password_rules(self):
        print('''
* Password must be at least 8 characters long
* Should contain Upper Case Letters, Lower Case Letters, Numbers and Symbols
* Forward Slash or " / " is not allowed in Password
''')

    def primary_display(self):
        print('''
1. Save Credential
2. Update Credential
3. Search Credential
4. Delete Credential
0. Back
''')

    def login(self):
        print('''
1. Login
2. Reset Password
0. Back
''')

    def enter_url(self):
        print("Enter URL")

    def enter_username(self):
        print("Enter Username")

    def enter_password(self):
        print("Enter Password")

    def confirm_password(self):
        print("Confirm Password")

    def previous_password(self):
        print("Enter Previous Password")

    def new_password(self):
        print("Enter New Password")


    def password_changed(self, password):
        print(f"Your password has been changed. New Password: {password}")

    def generate_password(self):
        print("Want to generate a new password? Type 'Y' for 'Yes' | 'N' for 'No'")

    def password_category(self):
        print("Which Category Password do you want?")
        print('''
1. Easy Password
2. Medium Password
3. Strong Password
''')


    def incorrect_password(self):
        print("Incorrect Password")

    def invalid_entry(self):
        print("That's an invalid entry")

    def short_password(self):
        print("Your Password deos not follow Criteria")