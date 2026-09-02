
class BorrowRecord:
    def __init__(self, book_id, borrow_duration, member_id):
        self.book_id = book_id
        self.borrow_duration = borrow_duration
        self.member_id = member_id
        self.return_duration = None

    def update_return_duration(self, returned_after_this_duration):
        self.return_duration = returned_after_this_duration

    def check_late_status(self, book_holding_days):
        if book_holding_days > self.borrow_duration:
            return book_holding_days - self.borrow_duration
        else:
            return None