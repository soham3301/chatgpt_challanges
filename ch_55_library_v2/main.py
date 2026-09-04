
#? Note:- A thought, should the main.py do all the user interaction? Can I make another class just to tackle user interaction?

from display import Display
from user_input import UserInput
from library import Library

display = Display()
usr_input = UserInput()
library = Library()

#* === The Member Login ===
def login_flow():
    display.enter_id()
    member_id = usr_input.text_input()
    if member_id:
        if library.validate_member(member_id):
            display.enter_password()
            member_password = usr_input.text_input()
            if member_password:
                if library.validate_member_login(member_id, member_password):
                    return library.get_member(member_id)
                else:
                    display.incorrect_password()
                    return None
            else:
                display.invalid_input()
                return None
        else:
            display.member_not_found(member_id)
            return None
    else:
        display.invalid_input()
        return None

#* === The Member Sign Up ===
def sign_up_flow():
    display.enter_name()
    member_name = usr_input.text_input()
    if member_name:
        display.enter_age()
        member_age = usr_input.number_input()
        if member_age:
            if Library.validate_age(round(member_age)):
                while True:
                    display.enter_user_id()
                    member_user_id = usr_input.text_input()
                    if member_user_id:
                        if library.validate_member(member_user_id):
                            #? Note:- Here, validate member is serving a different purpose. In member login, it is checking whether the member ID exists or not. Here it is checking this user_id is taken or not
                            display.user_id_taken(member_user_id)
                            continue
                        else:
                            display.enter_new_password()
                            member_password = usr_input.text_input()
                            if member_password:
                                display.confirm_password()
                                member_confirmed_password = usr_input.text_input()
                                if member_confirmed_password:
                                    if member_password == member_confirmed_password:
                                        library_fee = library.finance.check_library_fee()
                                        display.pay_library_fee(library_fee)
                                        paid_fee = usr_input.number_input()
                                        if paid_fee:
                                            if paid_fee == library_fee:
                                                library.finance.add_amount(paid_fee)
                                                account_creation_data = library.create_member(member_name, round(member_age), member_user_id, member_password)
                                                display.show_readymade_data(account_creation_data)
                                                library.save_data()
                                                return True
                                            else:
                                                display.incorrect_payment()
                                                return False
                                        else:
                                            display.invalid_input()
                                            return False
                                    else:
                                        display.incorrect_password()
                                        return False
                                else:
                                    display.invalid_input()
                                    return False
                            else:
                                display.invalid_input()
                                return False
                    else:
                        display.invalid_input()
                        return False
            else:
                display.age_restricted()
        else:
            display.invalid_input()
            return False
    else:
        display.invalid_input()
        return False

#* === Admin After Login ===
def admin_logged_in():
    #? Note:- I should have used a dispatcher function.
    while True:
        display.admin_primary_display()
        admin_input = usr_input.text_input()
        if admin_input.lower() == "exit":
            display.goodbye_screen()
            break
        elif admin_input == "1":
            display.enter_book_title()
            book_title = usr_input.text_input()
            if book_title:
                display.enter_book_price()
                book_price = usr_input.number_input()
                if book_price:
                    if library.finance.check_balance_available_or_not(book_price):
                        display.enter_author_name()
                        book_author = usr_input.text_input()
                        if book_author:
                            book_data = library.create_book(book_title, round(abs(book_price)), book_author)
                            display.show_readymade_data(book_data)
                            library.save_data()
                        else:
                            display.invalid_input()
                    else:
                        display.insufficient_fund()
                else:
                    display.invalid_input()
            else:
                display.invalid_input()
        elif admin_input == "2":
            display.enter_new_password()
            new_pass = usr_input.text_input()
            if new_pass:
                display.confirm_password()
                confirm_new_pass = usr_input.text_input()
                if confirm_new_pass:
                    if new_pass == confirm_new_pass:
                        library.admin.change_password(confirm_new_pass)
                        display.password_changed()
                        library.save_data()
                    else:
                        display.incorrect_password()
                else:
                    display.invalid_input()
            else:
                display.invalid_input()
        elif admin_input == "3":
            fund_data = library.finance.check_vault()
            display.show_fund(fund_data)
        elif admin_input == "4":
            late_fee_data = library.finance.late_fee_data()
            display.show_readymade_data(late_fee_data)
            display.enter_new_late_fee()
            new_late_fee = usr_input.number_input()
            if new_late_fee:
                changed_late_fee_data = library.finance.change_late_fee(round(abs(new_late_fee)))
                display.show_readymade_data(changed_late_fee_data)
                library.save_data()
            else:
                display.invalid_input()
        elif admin_input == "5":
            library_fee_data = library.finance.library_fee_data()
            display.show_readymade_data(library_fee_data)
            display.enter_new_library_fee()
            new_library_fee = usr_input.number_input()
            if new_library_fee:
                changed_library_fee_data = library.finance.change_library_fee(round(abs(new_library_fee)))
                display.show_readymade_data(changed_library_fee_data)
                library.save_data()
            else:
                display.invalid_input()
        else:
            display.invalid_input()


#* === Member After Login ===
def search_book_by_author():
    display.enter_author_name()
    the_author_name = usr_input.text_input()
    if the_author_name:
        book_list = library.get_books_by_author(the_author_name)
        if book_list:
            display.check_individual_book(the_author_name)
            book_serial = 0
            for book in book_list:
                book_serial += 1
                display.show_book_with_id(book_serial, book.title, book.id)
        else:
            display.no_book_by_author(the_author_name)
    else:
        display.invalid_input()

def search_book_by_title():
    display.enter_book_title()
    the_book_title = usr_input.text_input()
    if the_book_title:
        the_book = library.get_book_by_title(the_book_title)
        if the_book:
            if not the_book.borrowed:
                book_data = f'''
Title:  {the_book.title}
Price:  {the_book.price}/-
Author: {the_book.author}
ID:     {the_book.id}
    '''
                display.show_readymade_data(book_data)
            else:
                display.borrowed_by_someone(the_book.title)
        else:
            display.no_book_available(the_book_title)
    else:
        display.invalid_input()

def search_book_by_id():
    #? Note:- Here some code repeats. Ignoring it for now.
    display.enter_book_id()
    the_book_id = usr_input.text_input()
    if the_book_id:
        the_book = library.get_book(the_book_id)
        if the_book:
            if not the_book.borrowed:
                book_data = f'''
Title:  {the_book.title}
Price:  {the_book.price}/-
Author: {the_book.author}
ID:     {the_book.id}
    '''
                display.show_readymade_data(book_data)
            else:
                display.borrowed_by_someone(the_book.title)
        else:
            display.invalid_book_id(the_book_id)
    else:
        display.invalid_input()

def borrow_book(mem):
    cart = {}
    while True:
        display.borrow_books_primary_display()
        display.books_in_cart(len(cart))
        display.enter_book_id()
        entered_book_id = usr_input.text_input()
        if entered_book_id:
            if entered_book_id.lower() == "cancel":
                display.borrow_procedure_terminated()
                break
            elif entered_book_id.lower() == "checkout":
                display.about_to_borrow()
                for book_id in cart:
                    display.show_book_for_borrow(cart[book_id].title, cart[book_id].author)
                checkout_consent = usr_input.text_input()
                if checkout_consent:
                    if checkout_consent.lower() == "confirm":
                        late_fee = library.finance.check_late_fee()
                        display.for_how_many_days(late_fee)
                        borrow_days = usr_input.number_input()
                        #? Note:- A person can borrow a book for unlimited days. No upper time limit has been set.
                        if borrow_days:
                            borrow_data = library.borrow_book_by_customer(cart, round(abs(borrow_days)), mem)
                            display.show_readymade_data(borrow_data)
                            library.save_data()
                            break
                        else:
                            display.invalid_input()
                    elif checkout_consent.lower() == "remove":
                        display.books_in_cart(len(cart))
                        display.about_to_remove_from_cart()
                        display.enter_book_id()
                        book_id_for_removal = usr_input.text_input()
                        if book_id_for_removal:
                            if book_id_for_removal in cart:
                                removed_book = cart.pop(book_id_for_removal)
                                display.book_removed_from_cart(removed_book.title)
                            else:
                                display.invalid_book_id(book_id_for_removal)
                        else:
                            display.invalid_input()
                    elif checkout_consent.lower() == "cancel":
                        display.borrow_procedure_terminated()
                        break
                    else:
                        display.invalid_input()
                else:
                    display.invalid_input()
            else:
                the_book = library.get_book(entered_book_id)
                if the_book:
                    if the_book.id in cart:
                        display.already_inside_cart(the_book.title, the_book.author)
                    elif the_book.borrowed:
                        display.borrowed_by_someone(the_book.title)
                    else:
                        cart[the_book.id] = the_book
                        display.book_added_to_cart(the_book.title)
                else:
                    display.invalid_book_id(entered_book_id)
        else:
            display.invalid_input()

def return_book(mem):
    borrowed_book_id_with_tran_id = {}
    for tran_id in mem.borrowed_book_tran_id:
        book_id = library.get_book_id_by_borrow_tran(tran_id)
        borrowed_book_id_with_tran_id[book_id] = tran_id
    if borrowed_book_id_with_tran_id:
        display.book_return_primary_screen()
        display.enter_book_id()
        entered_book_id = usr_input.text_input()
        if entered_book_id:
            if entered_book_id in borrowed_book_id_with_tran_id:
                display.after_how_many_days()
                number_of_days = usr_input.number_input()
                #? Note:- This number (how many days have passed) should be system / librarian generated. Here I am asking the user, avoiding date time module.
                if number_of_days:
                    is_late_fee_needed, the_late_fee = library.check_late_fee(borrowed_book_id_with_tran_id[entered_book_id], number_of_days)
                    if is_late_fee_needed:
                        display.enter_the_late_fee(the_late_fee)
                        entered_late_fee = usr_input.number_input()
                        if entered_late_fee:
                            if the_late_fee == entered_late_fee:
                                late_fee_data = library.accept_late_fee(the_late_fee)
                                display.show_readymade_data(late_fee_data)
                                return_book_data = library.accept_book_return(mem, entered_book_id, borrowed_book_id_with_tran_id[entered_book_id], number_of_days)
                                display.show_readymade_data(return_book_data)
                                library.save_data()
                            else:
                                display.late_fee_didnot_match(the_late_fee, entered_late_fee)
                        else:
                            display.invalid_input()
                    else:
                        return_book_data_without_fee = library.accept_book_return(mem, entered_book_id, borrowed_book_id_with_tran_id[entered_book_id], number_of_days)
                        display.show_readymade_data(return_book_data_without_fee)
                        library.save_data()
                else:
                    display.invalid_input()
            else:
                display.not_borrowed(entered_book_id)
        else:
            display.invalid_input()
    else:
        display.nothing_to_return()

def command_mapper(member, mem_input):
    saved_commands = {
        "1": search_book_by_author,
        "2": search_book_by_title,
        "3": search_book_by_id,
        "4": borrow_book,
        "5": return_book,
    }
    if mem_input in ["1", "2", "3"]:
        saved_commands[mem_input]()
    else:
        saved_commands[mem_input](member)

#* === The Main Program ===
library_open = True
while library_open:
    display.primary_screen()
    first_input = usr_input.text_input()
    if first_input == "1":                                  #* LOGIN SECTION
        the_member = login_flow()
        if the_member:
            display.welcome_screen(the_member.name)
            member_logged_in = True
            while member_logged_in:
                display.after_login_display()
                member_input = usr_input.text_input()
                if member_input.lower() == "exit":
                    member_logged_in = False
                    display.logged_out(the_member.name)
                elif member_input in ["1", "2", "3", "4", "5"]:
                    command_mapper(the_member, member_input)
                else:
                    display.invalid_input()
        else:
            continue
    elif first_input == "2":                                #* SIGN UP SECTION
        sign_up_flow()
    elif first_input.lower() == "admin":                    #* ADMIN SECTION
        display.enter_password()
        admin_pass = usr_input.text_input()
        if admin_pass:
            if library.admin.check_login(admin_pass):
                admin_logged_in()
            else:
                display.incorrect_password()
        else:
            display.invalid_input()
    elif first_input.lower() == "exit":
        library_open = False
        display.goodbye_screen()
    else:
        display.invalid_input()