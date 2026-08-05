
class MoneyMachine:
    def __init__(self):
        self.earning = 0
        self.spending = 0
        self.notes_accepted = [10, 20, 50, 100]
        self.collected_number_of_notes = []
        
    def cost_to_fill_up_storage(self, whole_storage):
        for key, value in whole_storage.items():
            self.spending += key.cost_checker(value)

    def calculate_bill(self, the_drink, number_of_that_drink):
        if number_of_that_drink > 0:
            bill = round(the_drink.selling_cost * number_of_that_drink)
            return bill
        else:
            return None

    def collect_payment(self, number_of_notes):
        self.collected_number_of_notes.append(abs(number_of_notes))

    def note_clearer(self):
        self.collected_number_of_notes.clear()

    def check_payment(self, bill):
        money_received = 0
        if len(self.notes_accepted) == len(self.collected_number_of_notes):
            for index in range(len(self.notes_accepted)):
                money_received += round(self.notes_accepted[index] * self.collected_number_of_notes[index])
            if money_received < bill:
                self.note_clearer()
                return False, money_received
            elif money_received == bill:
                self.note_clearer()
                return True, None
            else:
                self.note_clearer()
                return True, money_received - bill
        else:
            self.note_clearer()
            return False, None

    def add_earning(self, bill):
        self.earning += bill

    def add_spending(self, amount):
        self.spending += amount
