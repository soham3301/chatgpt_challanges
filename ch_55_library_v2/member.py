

#? Note:- There should be a system to track when this account is created.

class Member:
    def __init__(self, name, age, user_id, user_password):
        self.name = name
        self.age = age
        self.user_id = user_id
        self.user_pass = user_password
        self.borrowed_book_tran_id = []

    def validate_login(self, password):
        return self.user_pass == password

    def load_borrowed_book_tran_ids(self, id_list):
        self.borrowed_book_tran_id = id_list

    def append_book_tran_id(self, tran_id):
        self.borrowed_book_tran_id.append(tran_id)

    def clear_book_tran_id(self, tran_id):
        self.borrowed_book_tran_id.remove(tran_id)

    def to_dict(self):
        return {
            "name": self.name,
            "age": self.age,
            "user_id": self.user_id,
            "user_pass": self.user_pass,
            "borrowed_book_tran_id": self.borrowed_book_tran_id
        }