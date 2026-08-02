
class Input:
    def __init__(self):
        self.name = "User Input"

    def ask_number_of_customers(self):
        try:
            customer_number = round(int(input("How Many people are in your Group?\n")))
            if customer_number > 0:
                return customer_number
            else:
                return None
        except ValueError:
            return None
    
    def choose_table_number(self):
        try:
            table_number = round(int(input("Choose Table Number: \n")))
            if table_number > 0:
                return table_number
            else:
                return None
        except ValueError:
            return None

    def ask_item_details(self, item_list):
        item_name = input("Enter Item Name: ").title()
        if item_name == "Exit":
            return item_name, 0
        else:
            for item in item_list:
                if item.name == item_name:
                    try:
                        number_of_item = round(int(input(f"How Many {item_name}: ")))
                        if number_of_item > 0:
                            return item, number_of_item
                    except ValueError:
                        return None, 0
            return None, 0

    def want_discount(self):
        consent = input("Enter 'Y' for 'Yes'\n").lower()
        if consent == "y":
            return True
        else:
            return False

    def get_discount(self):
        discount_text = input("Enter Discount Coupon Code: ")
        return discount_text

    def ask_bill(self):
            try:
                bill = round(int(input("Enter Bill Amount: ")))
                if bill > 0:
                    return bill
                else:
                    return None
            except ValueError:
                return None