
#* Note: Right now there is only 1 type of bill, food bill. Later other services will be added to generate more bill

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

    def check_bill(self, list_of_orders):
        total_bill = self.price + self.bill
        order_data = {}
        food_bill = 0
        for order in list_of_orders:
            food_bill += int(order[2])
            order_data.update({
                f"{order[0]} x {order[1]}":order[2]
            })
        bill_data = {
            "paid":self.price,
            "unpaid":self.bill
        }
        return bill_data, order_data, total_bill, food_bill

    def decrease_bill(self, received_amount):
        self.bill -= received_amount

    def order_food(self, food_data):
        ordered_food_record = {
            self.number:[]
        }
        for food_name, food_record in food_data.items():
            for order_quantity, food_object in food_record.items():
                if food_object.name == "Breakfast" and self.breakfast_included:
                    self.bill += 0
                    food_object.quantity -= order_quantity
                    ordered_food_record[self.number].append({
                        "name":food_object.name,
                        "quantity":order_quantity,
                        "price":0
                    })
                elif food_object.name == "Lanch" and self.lanch_dinner_included:
                    self.bill += 0
                    food_object.quantity -= order_quantity
                    ordered_food_record[self.number].append({
                        "name":food_object.name,
                        "quantity":order_quantity,
                        "price":0
                    })
                elif food_object.name == "Dinner" and self.lanch_dinner_included:
                    self.bill += 0
                    food_object.quantity -= order_quantity
                    ordered_food_record[self.number].append({
                        "name":food_object.name,
                        "quantity":order_quantity,
                        "price":0
                    })
                else:
                    self.bill += food_object.price * order_quantity
                    food_object.quantity -= order_quantity
                    ordered_food_record[self.number].append({
                        "name":food_object.name,
                        "quantity":order_quantity,
                        "price":food_object.price * order_quantity
                    })
        return ordered_food_record

    def leave_room(self):
        self.bill = 0
        self.guest = None
        self.is_booked = False