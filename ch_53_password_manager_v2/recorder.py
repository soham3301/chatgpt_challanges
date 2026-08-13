
import random
import csv
import json
from encryption import Encryption

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
        key = random.randint(1, 10)
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

    def write_cred_data(self, data):
        formatted_data = {}
        for url, user_cred in data.items():
            for username, cred in user_cred.items():
                key = self.generate_key()
                #! IMPORTANT:- The key should not be saved in same file with data - Need to fix it.
                en_url = self.security.encrypt(cred.website, self.saved_data, key)
                en_username = self.security.encrypt(cred.username, self.saved_data, key)
                en_password = self.security.encrypt(cred.password, self.saved_data, key)
                if en_url in formatted_data:
                    formatted_data[en_url][en_username] = [en_password, key]
                else:
                    formatted_data[en_url] = {
                        en_username: [en_password, key]
                    }
        with open("./data/credentials.json", mode="w") as cred_file_w:
            json.dump(formatted_data, cred_file_w, indent=4)

    def load_cred_data(self):
        try:
            loaded_data = {}
            with open("./data/credentials.json", mode="r") as cred_file_r:
                data = json.load(cred_file_r)
                for url, cred in data.items():
                    for username, password in cred.items():
                        key = password[1]
                        de_url = self.security.decrypt(url, self.saved_data, key)
                        de_username = self.security.decrypt(username, self.saved_data, key)
                        de_password = self.security.decrypt(password[0], self.saved_data, key)
                        if de_url in loaded_data:
                            loaded_data[de_url][de_username] = de_password
                        else:
                            loaded_data[de_url] = {
                                de_username: de_password
                            }
        except json.JSONDecodeError:
            loaded_data = {}
        return loaded_data