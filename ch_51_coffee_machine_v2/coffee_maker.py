
class CoffeeMaker:
    def __init__(self):
        self.stock = {}
        self.store_limits = {
            "water":150,
            "coffee":30,
            "milk":90,
        }
        self.saved_drinks = {}

    def add_ingredient(self, the_ingredient_list):
        for ingredient in the_ingredient_list:
            limit = self.store_limits[ingredient.name]
            self.stock[ingredient] = limit
        return self.stock

    def add_available_drinks(self, drink_list):
        for drink in drink_list:
            self.saved_drinks[drink.name] = drink

    def get_drink(self, name_of_drink):
        return self.saved_drinks[name_of_drink]

    def storage_checker(self, drink_name, drink_number):
        storage_limit_exceeds = False
        for ingredient, ingredient_quantity in self.saved_drinks[drink_name].ingredients.items():
            if self.stock[ingredient] >= ingredient_quantity * drink_number:
                continue
            else:
                storage_limit_exceeds = True
        return storage_limit_exceeds

    def storage_reducer(self, the_drink, number_of_that_drink):
        for ingredient in the_drink.ingredients:
            self.stock[ingredient] -= round(the_drink.ingredients[ingredient] * number_of_that_drink)

    def stock_cleaner_and_add_ingredients(self, ingredient_list):
        self.stock.clear()
        return self.add_ingredient(ingredient_list)


    def check_spent_stock(self):
        amount_to_refill = 0
        stock_spent = {}
        for ingredient in self.stock:
            if self.store_limits[ingredient.name] - self.stock[ingredient]:
                stock_spent[ingredient] = self.store_limits[ingredient.name] - self.stock[ingredient]
                amount_to_refill += ingredient.cost_checker(self.store_limits[ingredient.name] - self.stock[ingredient])
        return stock_spent, amount_to_refill