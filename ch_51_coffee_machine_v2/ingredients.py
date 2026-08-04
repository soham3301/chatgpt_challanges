
class Ingredient:
    def __init__(self, name, cost_per_unit):
        self.name = name
        self.cost_per_unit = cost_per_unit

    def quantity_checker(self, purchase_cost):
        if purchase_cost <= 0:
            return 0
        else:
            return round((purchase_cost / self.cost_per_unit), 2)

    def cost_checker(self, purchase_quantity):
        if purchase_quantity <= 0:
            return 0
        else:
            return round((purchase_quantity * self.cost_per_unit), 2)