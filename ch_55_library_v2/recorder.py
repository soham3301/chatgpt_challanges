
import json

class Recorder:
    def __init__(self):
        self.name = "RECORDER"

    def load_admin(self):
        try:
            with open("./data/admin.json") as admin_file:
                data = json.load(admin_file)
                return data
        except json.JSONDecodeError:
            return {}

    def save_admin(self, admin_dict):
        with open("./data/admin.json", mode="w") as admin_file:
            json.dump(admin_dict, admin_file, indent=4)

    def load_members(self):
        try:
            with open("./data/members.json") as member_file:
                data = json.load(member_file)
                return data
        except json.JSONDecodeError:
            return {}

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
        try:
            with open("./data/books.json") as book_file:
                data = json.load(book_file)
                return data
        except json.JSONDecodeError:
            return {}

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
        try:
            with open("./data/finance.json") as finance_file:
                data = json.load(finance_file)
                return data
        except json.JSONDecodeError:
            return {}

    def save_finance(self, fin_dict):
        with open("./data/finance.json", mode="w") as finance_file:
            json.dump(fin_dict, finance_file, indent=4)