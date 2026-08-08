
class Room:
    def __init__(self, name, number, price, ac, breakfast, lanch_dinner):
        self.name = name
        self.number = number
        self.price = price
        self.ac_available = ac
        self.breakfast_included = breakfast
        self.lanch_dinner_included = lanch_dinner
        self.is_booked = False
        self.guest = None
        self.bill = 0

    def book_room(self):
        pass

    def leave_room(self):
        pass
