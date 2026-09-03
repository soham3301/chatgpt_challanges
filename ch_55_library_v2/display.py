
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

    def enter_author_name(self):
        print("Enter the name of the Author")

    def enter_book_id(self):
        print("Enter Book ID")

    def invalid_book_id(self, the_id):
        print(f"This ID {the_id} doesn't exist")

    def enter_book_title(self):
        print("Enter the Book Title")

    def no_book_available(self, the_title):
        print(f"Sorry We don't have {the_title} as of now")
    
    def no_book_by_author(self, author):
        print(f"Sorry we don't have any book of {author}")

    def check_individual_book(self, author):
        print(f"Here is a list of books written by {author}. Check individual book details by Book Title or Book ID\n")

    def borrow_books_primary_display(self):
        print("Add books to your cart by enterting book id one after anohter. Type 'Checkout' for further procedure. Type 'Cancel' for CANCELLING the whole process.")

    def already_inside_cart(self, title, author):
        print(f"{title} by {author} is already inside your cart.")

    def book_added_to_cart(self, title):
        print(f"{title} has been added to your cart.")

    def borrow_procedure_terminated(self):
        print("Your Process of borrowing books is cancelled.")

    def books_in_cart(self, number):
        print(f"Books inside your cart: {number}")

    def about_to_borrow(self):
        print("You are about to borrow these books. Type 'Confirm' to CONFIRM. Type 'Remove' to REMOVE any book. Type 'Cancel' for CANCELLING the whole process.")

    def for_how_many_days(self, fee):
        print(f"Enter how many days you are planning to hold these books. If late, than a late fee of Rs:- {fee}/- will be added for every consequtive day.")

    def about_to_remove_from_cart(self):
        print("You are about to remove a book from your cart.")

    def book_removed_from_cart(self, title):
        print(f"{title} has been Removed from your Cart.")

    def show_book_for_borrow(self, title, author):
        print(f"{title} by {author}")

    def show_book_with_id(self, serial, title, b_id):
        print(f"{serial}. {title} | ID: {b_id}")

    def borrowed_by_someone(self, title):
        print(f"{title} has been borrowed by someone. Check again after a few days")

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

    def pay_library_fee(self, fee):
        print(f"Pay Rs:- {fee}/- as Library Fee. This will be renewed after a year. Enter the Exact Amount.")

    def incorrect_payment(self):
        print("Payment Failed")

    def admin_primary_display(self):
        print(f'''
1. Add Book
2. Change Password
3. Check Library Fund
4. Change Late Fee
5. Change Library Fee
''')

    def show_fund(self, amount):
        print(f"The Library has Rs:- {amount}/- Fund Left")

    def enter_new_late_fee(self):
        print("Enter new Late Fee")

    def enter_new_library_fee(self):
        print("Enter New Library Fee")

    def insufficient_fund(self):
        print("Insufficient Fund")

    def enter_book_title(self):
        print("Enter Book Title")

    def enter_author_name(self):
        print("Enter Author Name")

    def enter_book_price(self):
        print("Enter Book Price")