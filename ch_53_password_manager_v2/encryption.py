
class Encryption:
    def __init__(self):
        self.small_letters = []
        self.cap_letters = []
        self.numbers = []
        self.symbols = []
        self.target_smalls = []
        self.target_caps = []
        self.target_nums = []
        self.target_syms = []
        self.result_list = []

    def encrypt(self, for_encryption, value_set, received_key):
        encrypted_data = self.the_cipher(for_encryption, value_set, received_key)
        self.clear_lists()
        return encrypted_data

    def decrypt(self, for_decryption, value_set, received_key):
        decrypted_data = self.the_cipher(for_decryption, value_set, -received_key)
        self.clear_lists()
        return decrypted_data

    def the_cipher(self, received_data, values, value_of_key):
        for char in received_data:
            if char in values["small_letters"]:
                self.populate_data(char, self.small_letters)
                self.populate_garbage("/", self.cap_letters, self.numbers, self.symbols)
            elif char in values["capital_letters"]:
                self.populate_data(char, self.cap_letters)
                self.populate_garbage("/", self.small_letters, self.numbers, self.symbols)
            elif char in values["numbers"]:
                self.populate_data(char, self.numbers)
                self.populate_garbage("/", self.small_letters, self.cap_letters, self.symbols)
            elif char in values["symbols"]:
                self.populate_data(char, self.symbols)
                self.populate_garbage("/", self.small_letters, self.cap_letters, self.numbers)
            else:
                return None
        self.index_mover(self.small_letters, self.target_smalls, values, "small_letters", len(values["small_letters"]) - 1, value_of_key)
        self.index_mover(self.cap_letters, self.target_caps, values, "capital_letters", len(values["capital_letters"]) - 1, value_of_key)
        self.index_mover(self.numbers, self.target_nums, values, "numbers", len(values["numbers"]) - 1, value_of_key)
        self.index_mover(self.symbols, self.target_syms, values, "symbols", len(values["symbols"]) - 1, value_of_key)
        for index in range(len(received_data)):
            if self.target_smalls[index] != "/":
                self.result_list.append(self.target_smalls[index])
            elif self.target_caps[index] != "/":
                self.result_list.append(self.target_caps[index])
            elif self.target_nums[index] != "/":
                self.result_list.append(self.target_nums[index])
            elif self.target_syms[index] != "/":
                self.result_list.append(self.target_syms[index])
        result_data = "".join(self.result_list)
        return result_data

    def index_mover(self, base_list, target_list, original_data, keyword, limiter, keys_value):
        for item in base_list:
            if item != "/":
                actual_index = original_data[keyword].index(item)
                new_index = actual_index + keys_value
                if new_index > limiter:
                    new_index -= (limiter + 1)
                new_item = original_data[keyword][new_index]
                target_list.append(new_item)
            else:
                target_list.append(item)

    def populate_data(self, character, list_to_populate_data):
        list_to_populate_data.append(character)

    def populate_garbage(self, garbage, *lists_to_populate_garbage):
        for one_list in lists_to_populate_garbage:
            one_list.append(garbage)

    def clear_lists(self):
        self.small_letters.clear()
        self.cap_letters.clear()
        self.numbers.clear()
        self.symbols.clear()
        self.target_smalls.clear()
        self.target_caps.clear()
        self.target_nums.clear()
        self.target_syms.clear()
        self.result_list.clear()