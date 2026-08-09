
class Room:
    def __init__(self, name, number, price, ac, breakfast, lanch_dinner, key):
        self.name = name
        self.number = number
        self.price = price
        self.ac_available = ac
        self.breakfast_included = breakfast
        self.lanch_dinner_included = lanch_dinner
        self.key = key
        self.is_booked = False
        self.guest = None
        self.bill = 0

    def validate_key(self, the_key):
        if self.guest:
            return self.guest.guest_login(the_key)
        else:
            return False

    def book_room(self, the_guest):
        self.is_booked = True
        self.guest = the_guest

    def check_facilities(self):
        facilities_data = {
            "ac":self.ac_available,
            "breakfast":self.breakfast_included,
            "lanch_dinner":self.lanch_dinner_included
        }
        return facilities_data

    def check_bill(self):
        bill_data = {
            "paid":self.price,
            "unpaid":self.bill
        }
        return bill_data

    def order_food(self, food_data):
        for food_name, food_record in food_data.items():
            for order_quantity, food_object in food_record.items():
                self.bill += food_object.price * order_quantity
                food_object.quantity -= order_quantity

    def leave_room(self):
        pass
