


from display import Display
from user_input import UserInput
from library import Library

display = Display()
usr_input = UserInput()
library = Library()

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
                            display.enter_password()
                            member_password = usr_input.text_input()
                            if member_password:
                                display.confirm_password()
                                member_confirmed_password = usr_input.text_input()
                                if member_confirmed_password:
                                    if member_password == member_confirmed_password:
                                        account_creation_data = library.create_member(member_name, round(member_age), member_user_id, member_password)
                                        display.show_readymade_data(account_creation_data)
                                        library.save_data()
                                        return True
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

def admin_logged_in():
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
                    display.enter_author_name()
                    book_author = usr_input.text_input()
                    if book_author:
                        book_data = library.create_book(book_title, round(abs(book_price)), book_author)
                        display.show_readymade_data(book_data)
                        library.save_data()
                    else:
                        display.invalid_input()
                else:
                    display.invalid_input()
            else:
                display.invalid_input()
        else:
            display.invalid_input()








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
                    #! Command Mapper needed with member object
                    ...
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