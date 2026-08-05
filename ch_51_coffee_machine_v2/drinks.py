
class Drink:
    def __init__(self, name, water_quantity, coffee_quantity, milk_quantity):
        self.name = name
        self.quantities = [water_quantity, coffee_quantity, milk_quantity]
        self.selling_cost = 0
        self.ingredients = {}
        self.making_cost = 0

    def find_making_cost(self):
        for key, value in self.ingredients.items():
            self.making_cost += key.cost_checker(value)

    def set_selling_cost(self):
        #NOTE Default 10% Profit Applied
        self.selling_cost = self.making_cost + round((self.making_cost * 10 / 100))

    def add_ingredient(self, ingredient_list):
        for index in range(len(ingredient_list)):
            self.ingredients[ingredient_list[index]] = self.quantities[index]
        self.find_making_cost()
        self.set_selling_cost()

    def check_profit_loss(self):
        return self.selling_cost, self.making_cost

    def change_selling_cost(self, new_cost):
        self.selling_cost = new_cost
