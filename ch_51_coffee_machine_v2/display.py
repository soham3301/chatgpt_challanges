
class Display:
    def __init__(self):
        self.name = "Display"

    def goodbye(self):
        print("Thanks for using Coffee Machine. Have a Productive Day")
    
    def invalid_input(self):
        print("Invalid Input")

    def user_display(self):
        print("What would you like to order? (espresso / latte / cappuccino)")

    def number_of_drink_needed(self, drink):
        print(f"How Many {drink.name} do you want? (eg: 1, 2, 3, etc etc...)")

    def storage_exceeds(self, the_drink, number_of_drink):
        print(f"{number_of_drink} no of {the_drink.name} can't be made. Storage Limitation.")

    def show_bill(self, the_bill):
        print(f"Here is your total cost: {the_bill}")

    def want_to_proceed_purchase(self):
        print("Want to proceed purchase? Type 'Y' for Yes / 'N' for No")

    def order_cancelled(self):
        print("Order has been cancelled.")
    
    def notes_accepted(self, notes_list):
        notes = ", ".join(map(str, notes_list))
        print(f"We only accept {notes} Notes.")

    def enter_number_of_notes(self, note):
        print(f"How many {note} rupees note you want to enter?")

    def purchase_status(self, purchase_sitaution, remaining_refund):
        if not purchase_sitaution and remaining_refund:
            print(f"Less amount paid. Order Cancelled | Here is your full refund: {remaining_refund} INR")
        elif purchase_sitaution and not remaining_refund:
            print("Purchase Successfull")
        elif purchase_sitaution and remaining_refund:
            print(f"Purchase Successfull. Here is your remaining amount: {remaining_refund} INR")
        else:
            self.invalid_input()

#? ----------------- ADMIN PANEL ----------------

    def enter_admin_password(self):
        print("Enter Admin Password")

    def incorrect_password(self):
        print("Incorrect Password")

    def admin_panel_display(self):
        print('''
1. Check money earned till now.
2. Check money spent till now.
3. Check storage.
4. Add ingredients in existing stock.
5. Clear stock and fillup ingredients.
''')

    def check_money_earned(self, amount):
        print(f"Money earned till now: {amount} INR")

    def check_money_spent(self, amount):
        print(f"Money spent till now: {amount} INR")

    def check_storage(self, the_storage):
        for ingredient, storage in the_storage.items():
            print(f"Ingredient: {ingredient.name} | Available Unit: {storage}")

    def admin_log_out(self):
        print("Logged Out from Admin Panel")