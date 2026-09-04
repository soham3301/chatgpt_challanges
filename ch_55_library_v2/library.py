
#? Note:- There is no Stock Tracking the number of books. Missed this concept.

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
        if book_id in self.books:
            return self.books[book_id]
        else:
            return None

    def get_book_by_title(self, title):
        if title in self.bookdata["title"]:
            the_book_id = self.bookdata["title"][title]
            return self.get_book(the_book_id)
        else:
            return None

    def get_books_by_author(self, author):
        if author in self.bookdata["author"]:
            book_id_list = self.bookdata["author"][author]
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
        if new_book.author in self.bookdata["author"]:
            self.bookdata["author"][new_book.author].append(new_book.id)
        else:
            self.bookdata["author"][new_book.author] = []
            self.bookdata["author"][new_book.author].append(new_book.id)
        self.bookdata["title"][new_book.title] = new_book.id
        return f'''
The Book has been successfully added to library.
Title: {title}
Author: {author}
Price: {price} INR
Book ID: {book_id}
'''

    def borrow_book_by_customer(self, cart, days, member):
        #? Note:- Here, physical books will be taken by member but the book object will remain in library, only the data changes while borrowing.
        if cart:
            for book_id in cart:
                borrow_transaction = BorrowRecord(book_id, days, member.user_id)
                the_tran_id = borrow_transaction.generate_tran_id()
                cart[book_id].borrow_book()
                self.borrow_record[the_tran_id] = borrow_transaction
                member.append_book_tran_id(the_tran_id)
            return f"{member.name}, Thanks for borrowing these {len(cart)} books for {days} days. Enjoy Reading."
        else:
            return f"No Book is added to the cart."

    def get_borrow_transaction(self, tran_id):
        if tran_id in self.borrow_record:
            return self.borrow_record[tran_id]
        else:
            return None

    def get_book_id_by_borrow_tran(self, tran_id):
        the_transaction = self.get_borrow_transaction(tran_id)
        if the_transaction:
            return the_transaction.book_id
        else:
            return None

    def check_late_fee(self, tran_id, holding_days):
        the_transaction = self.get_borrow_transaction(tran_id)
        extra_days = the_transaction.check_late_status(holding_days)
        late_fee = self.finance.calculate_late_fee(extra_days)
        if late_fee > 0:
            return True, late_fee
        else:
            return False, None

    def accept_late_fee(self, fee):
        self.finance.add_amount(fee)
        return f"Rs:- {fee}/- Paid as Late Fee."

    def accept_book_return(self, mem, b_id, t_id, days):
        the_borrow_transaction = self.get_borrow_transaction(t_id)
        the_borrow_transaction.update_return_duration(days)
        the_book = self.get_book(b_id)
        the_book.book_returned()
        mem.clear_book_tran_id(t_id)
        return f"The return of {the_book.title} written by {the_book.author} after {days} days has been accepted by the Library from {mem.name}"

    def save_data(self):
        self.recorder.save_admin(self.admin.to_dict())
        self.recorder.save_members(self.members)
        self.recorder.save_books(self.books)
        self.recorder.save_bookdata(self.bookdata)
        self.recorder.save_borrow_record(self.borrow_record)
        self.recorder.save_finance(self.finance.to_dict())

    def load_data(self):
        #? Note:- Here I am loading all data as soon as the server runs. But in a real library, there will be millions of books.
        #? Note:- I think the book data should remain in database and when customer asks, only then the book data should be fetched to backend code.
        admin_data = self.recorder.load_admin()
        self.admin.load_data(admin_data)
        member_data = self.recorder.load_members()
        if member_data:
            for member_id in member_data:
                new_member = Member(member_data[member_id]["name"], member_data[member_id]["age"], member_data[member_id]["user_id"], member_data[member_id]["user_pass"])
                new_member.load_borrowed_book_tran_ids(member_data[member_id]["borrowed_book_tran_id"])
                self.members[new_member.user_id] = new_member
        else:
            self.members = member_data
        book_data = self.recorder.load_books()
        if book_data:
            for book_id in book_data:
                new_book = Book(book_data[book_id]["title"], int(book_data[book_id]["price"]), book_data[book_id]["author"])
                new_book.load_book_data(book_data[book_id]["id"], book_data[book_id]["borrowed"])
                self.books[new_book.id] = new_book
        else:
            self.books = book_data
        bookdata_data = self.recorder.load_bookdata()
        self.bookdata = bookdata_data
        borrow_record_data = self.recorder.load_borrow_record()
        if borrow_record_data:
            for borrow_tran in borrow_record_data:
                new_borrow_transaction = BorrowRecord(borrow_record_data[borrow_tran]["book_id"], borrow_record_data[borrow_tran]["borrow_duration"], borrow_record_data[borrow_tran]["member_id"])
                new_borrow_transaction.load_borrow_data(borrow_record_data[borrow_tran])
                self.borrow_record[new_borrow_transaction.tran_id] = new_borrow_transaction
        else:
            self.borrow_record = borrow_record_data
        finance_data = self.recorder.load_finance()
        self.finance.load_fin_data(finance_data)


