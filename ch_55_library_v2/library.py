
from admin import Admin
from member import Member
from book import Book
from borrow_record import BorrowRecord
from recorder import Recorder
from finance import Finance

class Library:
    def __init__(self):
        self.admin = Admin()
        self.members = {}
        self.books = {}
        self.bookdata = {
            "author": {},
            "title": {},
        }
        self.borrow_record = {}
        self.finance = Finance()
        self.recorder = Recorder()
        self.load_data()


    def validate_member(self, user_id):
        if user_id in self.members:
            return True
        else:
            return False

    def get_member(self, member_id):
        return self.members[member_id]

    def validate_member_login(self, mem_id, mem_pass):
        the_member = self.get_member(mem_id)
        if the_member:
            return the_member.validate_login(mem_pass)
        else:
            return False

    def get_book(self, book_id):
        return self.books[book_id]

    def get_book_by_title(self, title):
        the_book_id = self.bookdata["title"][title]
        if the_book_id:
            return self.get_book(the_book_id)
        else:
            return None

    def get_books_by_author(self, author):
        book_id_list = self.bookdata["author"][author]
        if book_id_list:
            book_list = []
            for book_id in book_id_list:
                the_book = self.get_book(book_id)
                book_list.append(the_book)
            return book_list
        else:
            return []

    @staticmethod
    def validate_age(age):
        return age >= 18

    def create_member(self, name, age, u_id, password):
        new_member = Member(name, age, u_id, password)
        self.members[u_id] = new_member
        return f'''
{name}, Your Account Creation has been Successfully Completed
Login to Library using your ID: {u_id} and Password
'''

    def create_book(self, title, price, author):
        new_book = Book(title, price, author)
        self.finance.spend_amount(price)
        book_id = new_book.generate_book_id()
        self.books[book_id] = new_book
        return f'''
The Book has been successfully added to library.
Title: {title}
Author: {author}
Price: {price} INR
Book ID: {book_id}
'''

    def save_data(self):
        self.recorder.save_admin(self.admin.to_dict())
        self.recorder.save_members(self.members)
        self.recorder.save_books(self.books)
        self.recorder.save_bookdata()
        self.recorder.save_borrow_record()
        self.recorder.save_finance(self.finance.to_dict())

    def load_data(self):
        admin_data = self.recorder.load_admin()
        self.admin.load_data(admin_data)
        member_data = self.recorder.load_members()
        if member_data:
            for member_id in member_data:
                new_member = Member(member_data[member_id]["name"], member_data[member_id]["age"], member_data[member_id]["user_id"], member_data[member_id]["user_pass"])
                new_member.load_borrowed_book_ids(member_data[member_id]["borrowed_book_ids"])
                self.members[new_member.user_id] = new_member
        else:
            self.members = member_data
        book_data = self.recorder.load_books()
        if book_data:
            for book_id in book_data:
                new_book = Book(book_data[book_id]["title"], int(book_data[book_id]["price"]), book_data[book_id]["author"])
                new_book.load_book_id(book_data[book_id]["id"])
                self.books[new_book.id] = new_book
        else:
            self.books = book_data
        #* SPACE FOR BOOKDATA
        #* SPACE FOR BORROW RECORD
        finance_data = self.recorder.load_finance()
        self.finance.load_fin_data(finance_data)


