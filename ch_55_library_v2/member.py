
class Member:
    def __init__(self, name, age, user_id, user_password):
        self.name = name
        self.age = age
        self.user_id = user_id
        self.user_pass = user_password
        self.borrowed_book_ids = []