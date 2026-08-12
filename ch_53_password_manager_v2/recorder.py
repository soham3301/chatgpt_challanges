
import random
import csv
from encryption import Encryption

#? credential saving format
# saved_creds_format = {
#     "website_name":{
#         "one_username":{
#             "random_key":"Credential_Object",
#         },
#         "another_username":{
#             "random_key":"Credential_Object",
#         },
#     },
#     "another_website_name":{
#         "one_username":{
#             "random_key":"Credential_Object",
#         },
#     },
# }

class Recorder:
    def __init__(self):
        self.security = Encryption()
        self.saved_data = {}
        self.load_letters_numbers_symbols()

    def load_letters_numbers_symbols(self):
        with open("./data/letters.csv") as letter_file:
            render_letters = csv.reader(letter_file)
            for row in render_letters:
                if row[0] == "a":
                    self.saved_data["small_letters"] = row
                else:
                    self.saved_data["capital_letters"] = row
        with open("./data/numbers.csv") as number_file:
            render_numbers = csv.reader(number_file)
            number_data = [number for number in render_numbers]
            self.saved_data["numbers"] = number_data[0]
        with open("./data/symbols.csv") as symbol_file:
            render_symbol = csv.reader(symbol_file)
            symbol_data = [symbol for symbol in render_symbol]
            self.saved_data["symbols"] = symbol_data[0]

    def generate_key(self):
        #! IMPORTANT:- value of key should be below 10. Otherwise IndexError comes from numbers.csv - Need to fix this part
        key = random.randint(0, 10)
        return key

    def write_admin_password(self, new_password):
        key = self.generate_key()
        encrypted = self.security.encrypt(new_password, self.saved_data, key)
        with open("./data/admin_pass.csv", mode="w") as admin_file:
            admin_writer = csv.writer(admin_file)
            admin_writer.writerow(
                [key, encrypted]
            )

    def load_admin_pass(self):
        with open("./data/admin_pass.csv") as file:
            render_admin_pass = csv.reader(file)
            for row in render_admin_pass:
                decrypted = self.security.decrypt(row[1], self.saved_data, int(row[0]))
            return decrypted
                

rec = Recorder()