
class CoffeeMaker:
    def __init__(self):
        self.storage = {}
        self.storage_limits = {
            "water":150,
            "coffee":30,
            "milk":90,
        }

    def add_ingredient(self, the_ingredient_list):
        for ingredient in the_ingredient_list:
            limit = self.storage_limits[ingredient.name]
            self.storage[ingredient] = limit
        return self.storage





# drinks = {
#     "espresso":{
#         "ingredients":{
#             "water":50,
#             "coffee":18,
#             "milk":0
#         },
#         "price":90,
#     },
#     "latte":{
#         "ingredients":{
#             "water":200,
#             "coffee":24,
#             "milk":150,
#         },
#         "price":180,
#     },
#     "cappuccino":{
#         "ingredients":{
#             "water":250,
#             "coffee":24,
#             "milk":100,
#         },
#         "price":280,
#     },
# }
# machine_storage = {
#     "water":1500,
#     "coffee":300,
#     "milk":900,
# }
# ingredients_purchase_cost = {
#     "water":{
#         "price":32,
#         "quantity":100,
#     },
#     "coffee":{
#         "price":55,
#         "quantity":100,
#     },
#     "milk":{
#         "price":72,
#         "quantity":100,
#     },
# }
# notes_accepted = [10, 20, 50, 100]