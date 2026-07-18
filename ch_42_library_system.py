import random
book_stored = [
    {
        "title":"Pride and Prejudice",
        "author":"Jane Austen",
        "category":"fiction",
    },
    {
        "title":"1984",
        "author":"George Orwell",
        "category":"dystopian",
    },
    {
        "title":"The Great Gatsby",
        "author":"F. Scott Fitzgerald",
        "category":"tragedy",
    },
    {
        "title":"To Kill a Mockingbird",
        "author":"Harper Lee",
        "category":"courtroom drama",
    },
    {
        "title":"One Hundred Years of Solitude",
        "author":"Gabriel Garcia Marquez",
        "category":"magical realism",
    },
]

class Book:
    def __init__(self, title, author, category):
        self.title = title
        self.author = author
        self.category = category
        self.is_borrowed = False
        self.id = round(random.random() * 100000)               #! Bug - There is a chance that 2 books gets same ID
        self.due_days = 0
    
    def return_days(self):
        try:
            days = int(input("For how many days you are borrowing this book?\n"))
            if days > 0:
                self.due_days += days
        except ValueError:
            helper_invalid_input()

class Library:
    def __init__(self, book_list):
        self.book_list = book_list
    
    def collect_book_details(self):
        the_title = input("Enter Book Title: ")
        the_author = input("Enter the Author Name: ").title()
        the_category = input("Enter category of the book: ").lower()
        return the_title, the_author, the_category
    
    def search_by_id(self):
        try:
            book_id = int(input("Enter Book ID: "))
            for book in self.book_list:
                if book.id == book_id:
                    return book
            print("Book Not Found")
            return None
        except ValueError:
            helper_invalid_input()
            return None
    
    def add_book(self):
        the_title, the_author, the_category = self.collect_book_details()
        self.book = Book(the_title, the_author, the_category)
        self.book_list.append(self.book)
    
    def show_book(self):
        for book in self.book_list:
            print(f'''
Book ID: {book.id} | Available: {not book.is_borrowed}
Title: {book.title} by {book.author} | It's a {book.category} book.''')

    def borrow_book(self):
        the_book = self.search_by_id()
        if the_book:
            if not the_book.is_borrowed:
                the_book.return_days()
                the_book.is_borrowed = True
                print("Book Borrowed")
            else:
                print(f"Sorry this book is already borrowed by someone else. It will be availabe within {the_book.due_days + 1} days.")

    def return_book(self):
        the_book = self.search_by_id()
        if the_book:
            if the_book.is_borrowed:
                the_book.due_days = 0
                the_book.is_borrowed = False
                print("Book Returned")
            else:
                print(f"We already have {the_book.title} in our library. No need to return.")

    def due_date(self):
        serial_no = 1
        for book in self.book_list:
            if book.due_days > 0:
                print(f"{serial_no}: '{book.title}' by {book.author} has been borrowed by someone and will be available within {book.due_days + 1} days.")
                serial_no += 1

    def search_by_author(self):
        author_name = input("Enter Author Name: ").title()
        book_list_by_author = []
        for book in self.book_list:
            if book.author == author_name:
                book_list_by_author.append(book)
        if len(book_list_by_author) == 0:
            print(f"Sorry we don't have any book of {author_name}")
        else:
            print(f"{author_name} books")
            for authors_book in book_list_by_author:
                if authors_book.is_borrowed == True:
                    print(f"Already borrowed: '{authors_book.title}' | Will be available within {authors_book.due_days + 1} days.")
                if authors_book.is_borrowed == False:
                    print(f"Available Book: '{authors_book.title}' | ID: '{authors_book.id}'")

def display_and_user_input():
    try:
        user_choice = int(input('''
1. Add Book
2. Show Books
3. Borrow Book
4. Return Book
5. Check Due Dates
6. Search by Author
7. Exit Library
'''))
        if user_choice == 7:
            print("Thanks for using OOP Library")
            return False, None
        elif user_choice in [1, 2, 3, 4, 5, 6]:
            return True, user_choice
        else:
            helper_invalid_input()
            return True, None
    except ValueError:
        helper_invalid_input()
        return True, None

def helper_invalid_input():
    print("Sorry, Invalid Input")

def command_mapper(user_command, the_library):
    saved_commands = {
        1: the_library.add_book,
        2: the_library.show_book,
        3: the_library.borrow_book,
        4: the_library.return_book,
        5: the_library.due_date,
        6: the_library.search_by_author,
    }
    if user_command in saved_commands:
        saved_commands[user_command]()

def main():
    the_main_list = []
    for book in book_stored:
        the_main_list.append(Book(book["title"], book["author"], book["category"]))
    my_library = Library(the_main_list)
    while True:
        application_stopper, user_input = display_and_user_input()
        if not application_stopper:
            break
        else:
            command_mapper(user_input, my_library)

main()