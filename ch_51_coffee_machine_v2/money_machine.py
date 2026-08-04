
class MoneyMachine:
    def __init__(self):
        self.earning = 0
        self.spending = 0

    def cost_to_fill_up_storage(self, whole_storage):
        for key, value in whole_storage.items():
            self.spending += key.cost_checker(value)
        print(self.spending)

    