
from member import Member
from book import Book
from borrow_record import BorrowRecord
from recorder import Recorder
from finance import Finance


class Library:
    def __init__(self):
        self.members = {}
        self.books = {}
        self.recorder = Recorder()
