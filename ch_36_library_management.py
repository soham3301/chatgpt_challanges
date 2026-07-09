books = {
    "Python":{
        "available":True
    },
    "Harry Potter":{
        "available":False
    },
    "Game of Thrones":{
        "available":True
    },
    "Sonar Kella":{
        "available":True
    },
}

def display_board():
    user_choice = int(input('''
1. Borrow Book
2. Return Book
3. Display Books
4. Exit
'''))
    if user_choice == 4:
        print("Thanks for using Library Management System.")
        return False, user_choice
    else:
        return True, user_choice

def book_available_or_not():
    available_books = {}
    not_available_books = {}
    available_book_key = 0
    not_available_book_key = 0
    for book_name in books:
        if books[book_name]["available"]:
            available_book_key += 1
            available_books.update({
                available_book_key: book_name
            })
        if not books[book_name]["available"]:
            not_available_book_key += 1
            not_available_books.update({
            not_available_book_key: book_name
            })
    return available_books, not_available_books

def library_status(status):
    status_list = []
    for book_name in books:
        status_list.append(books[book_name]["available"])
    if status in status_list:
        return True
    else:
        return False

def show_books_for_interaction(book_dictionary):
    for key, value in book_dictionary.items():
            print(f"{key}: {value}")

def interaction_book(activity):
    return int(input(f"Which Book do You want to {activity}? Enter the numner: "))

def borrow_or_return_work(book_number, book_dictionary, true_or_false):
    if book_number in book_dictionary:
        books[book_dictionary[book_number]]["available"] = true_or_false
        print(f"{book_dictionary[book_number]} borrowed")
    else:
        print("Invalid number entered.")

def borrow_book():
    if library_status(True):
        available_books, not_available_books = book_available_or_not()    
        show_books_for_interaction(available_books)
        which_book = interaction_book("borrow")
        borrow_or_return_work(which_book, available_books, False)
    else:
        print("The Library is Empty. No book available for borrow.")

def return_book():
    if library_status(False):
        available_books, not_available_books = book_available_or_not()
        show_books_for_interaction(not_available_books)
        which_book = interaction_book("return")
        borrow_or_return_work(which_book, not_available_books, True)
    else:
        print("The Library is Full. No book needed as of now.")

def display_books():
    for book_name in books:
        if books[book_name]["available"]:
            print(f"{book_name} is Available")
        else:
            print(f"{book_name} is Not Available as of Now.")

def mapping_user_input(user_choice):
    saved_functions = {
        1: borrow_book,
        2: return_book,
        3: display_books,
    }
    if user_choice == 4:
        return None
    elif user_choice in saved_functions:
        saved_functions[user_choice]()
    else:
        print("Wrong Input")

def main():
    library_running = True
    while library_running:
        library_running, user_input = display_board()
        mapping_user_input(user_input)

main()