
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
        self.recorder.save_admin()
        self.recorder.save_members(self.members)
        self.recorder.save_books(self.books)
        self.recorder.save_bookdata()
        self.recorder.save_borrow_record()
        self.recorder.save_finance()

    def load_data(self):
        ...

