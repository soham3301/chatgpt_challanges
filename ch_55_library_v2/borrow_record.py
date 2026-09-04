
import random

class BorrowRecord:
    def __init__(self, book_id, borrow_duration, member_id):
        self.book_id = book_id
        self.borrow_duration = borrow_duration
        self.member_id = member_id
        self.return_duration = None
        self.tran_id = None

    def generate_tran_id(self):
        a_random_number = random.randint(1, 9)
        basic_id = self.book_id + self.member_id + str(self.borrow_duration) + str(a_random_number)
        self.tran_id = ''.join(random.sample(basic_id, len(basic_id)))
        return self.tran_id

    def update_return_duration(self, returned_after_this_duration):
        self.return_duration = returned_after_this_duration

    def check_late_status(self, book_holding_days):
        if book_holding_days > self.borrow_duration:
            return book_holding_days - self.borrow_duration
        else:
            return 0

    def to_dict(self):
        #? this to_dict method is nice. I should use it to send data of members and books into the recorder class
        return {
            "book_id": self.book_id,
            "borrow_duration": self.borrow_duration,
            "member_id": self.member_id,
            "return_duration": self.return_duration,
            "tran_id": self.tran_id
        }

    def load_borrow_data(self, data_dict):
        self.return_duration = data_dict["return_duration"]
        self.tran_id = data_dict["tran_id"]