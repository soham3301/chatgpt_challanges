
class Display:
    def __init__(self):
        self.name = "DISPLAY"

    def primary_screen(self):
        print('''
1. Sign In
2. Sign Up
''')

    def enter_id(self):
        print("Enter Your ID")

    def enter_password(self):
        print("Enter Your Password")

    def enter_new_password(self):
        print("Enter New Password")

    def password_changed(self):
        print("Password Changed Successfully")

    def member_not_found(self, member_id):
        print(f"This member ID {member_id} does not exist")

    def incorrect_password(self):
        print("Incorrect Password")

    def goodbye_screen(self):
        print("Thanks for visiting library. See you again")

    def welcome_screen(self, name):
        print(f"Welcome to the Library {name}")

    def after_login_display(self):
        print(f'''
1. Search Book by Author
2. Search Book by Title
3. Search Book by ID
4. Borrow Book
5. Return Book
''')

    def logged_out(self, name):
        print(f"Thanks {name} for visiting our Library")

    def show_readymade_data(self, data):
        print(data)

    def invalid_input(self):
        print("Invalid Input")

    def enter_name(self):
        print("Enter Your Name")

    def enter_age(self):
        print("Enter Your Age")

    def age_restricted(self):
        print(f"You are not an adult. Sorry.")

    def enter_user_id(self):
        print("Enter User ID. This will be your member ID")

    def user_id_taken(self, the_id):
        print(f"This user id: {the_id}, has been taken. Enter a new one.")

    def confirm_password(self):
        print("Confirm Password")

    def admin_primary_display(self):
        print(f'''
1. Add Book
2. Change Password
3. Check Library Fund
4. Change Late Fee
''')

    def show_fund(self, amount):
        print(f"The Library has Rs:- {amount}/- Fund Left")

    def enter_new_late_fee(self):
        print("Enter new Late Fee")

    def insufficient_fund(self):
        print("Insufficient Fund")

    def enter_book_title(self):
        print("Enter Book Title")

    def enter_author_name(self):
        print("Enter Author Name")

    def enter_book_price(self):
        print("Enter Book Price")