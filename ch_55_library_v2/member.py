

#? Note:- There should be a system to track when this account is created.

class Member:
    def __init__(self, name, age, user_id, user_password):
        self.name = name
        self.age = age
        self.user_id = user_id
        self.user_pass = user_password
        self.borrowed_book_ids = []

    def validate_login(self, password):
        return self.user_pass == password

    def load_borrowed_book_ids(self, id_list):
        self.borrowed_book_ids = id_list

    def append_book_ids(self, book_id):
        self.borrowed_book_ids.append(book_id)

    def clear_book_ids(self, book_id):
        self.borrowed_book_ids.remove(book_id)