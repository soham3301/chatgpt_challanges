
import json

class Recorder:
    def __init__(self):
        self.name = "RECORDER"

    def load_admin(self):
        pass

    def save_admin(self):
        pass

    def load_members(self):
        pass

    def save_members(self, members_dict):
        formatted_members = {}
        for member_id in members_dict:
            formatted_members[member_id] = {
                "name": members_dict[member_id].name,
                "age": members_dict[member_id].age,
                "user_id": members_dict[member_id].user_id,
                "user_pass": members_dict[member_id].user_pass,
                "borrowed_book_ids": members_dict[member_id].borrowed_book_ids
            }
        with open("./data/members.json", mode="w") as member_file:
            json.dump(formatted_members, member_file, indent=4)

    def load_books(self):
        pass

    def save_books(self, books_dict):
        formatted_books = {}
        for book_id in books_dict:
            formatted_books[book_id] = {
                "title": books_dict[book_id].title,
                "price": books_dict[book_id].price,
                "author": books_dict[book_id].author,
                "id": books_dict[book_id].id
            }
        with open("./data/books.json", mode="w") as books_file:
            json.dump(formatted_books, books_file, indent=4)

    def load_bookdata(self):
        pass

    def save_bookdata(self):
        pass

    def load_borrow_record(self):
        pass

    def save_borrow_record(self):
        pass

    def load_finance(self):
        pass

    def save_finance(self):
        pass