
class CoffeeMaker:
    def __init__(self):
        self.storage = {}
        self.store_limits = {
            "water":150,
            "coffee":30,
            "milk":90,
        }
        self.saved_drinks = {}

    def add_ingredient(self, the_ingredient_list):
        for ingredient in the_ingredient_list:
            limit = self.store_limits[ingredient.name]
            self.storage[ingredient] = limit
        return self.storage

    def add_available_drinks(self, drink_list):
        for drink in drink_list:
            self.saved_drinks[drink.name] = drink

    def get_drink(self, name_of_drink):
        return self.saved_drinks[name_of_drink]

    def storage_checker(self, drink_name, drink_number):
        storage_limit_exceeds = False
        for ingredient, ingredient_quantity in self.saved_drinks[drink_name].ingredients.items():
            if self.store_limits[ingredient.name] >= ingredient_quantity * drink_number:
                continue
            else:
                storage_limit_exceeds = True
        return storage_limit_exceeds

    def storage_reducer(self, the_drink, number_of_that_drink):
        for ingredient in the_drink.ingredients:
            self.storage[ingredient] -= the_drink.ingredients[ingredient] * number_of_that_drink