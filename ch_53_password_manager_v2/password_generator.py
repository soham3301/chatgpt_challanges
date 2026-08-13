
import random
class PasswordGenerator:
    def __init__(self):
        self._easy_length = 8
        self._medium_length = 12
        self._strong_length = 16
        self.random_holder = []

    def password_length_chooser(self, strength):
        password_length = 0
        if strength == "1":
            password_length = self._easy_length
        elif strength == "2":
            password_length = self._medium_length
        else:
            password_length = self._strong_length
        return password_length

    def generate_password(self, data, password_strength):
        generated_password = ""
        if password_strength == "1":
            the_length = self.password_length_chooser(password_strength)
            generated_password = self.password_maker(data, the_length)
        elif password_strength == "2":
            the_length = self.password_length_chooser(password_strength)
            generated_password = self.password_maker(data, the_length)
        else:
            the_length = self.password_length_chooser(password_strength)
            generated_password = self.password_maker(data, the_length)
        return generated_password

    def password_maker(self, the_data, length):
        for _ in range(round(length/4)):
            self.random_holder.append(random.choice(the_data["small_letters"]))
        for _ in range(round(length/4)):
            self.random_holder.append(random.choice(the_data["capital_letters"]))
        for _ in range(round(length/4)):
            self.random_holder.append(random.choice(the_data["numbers"]))
        for _ in range(round(length/4)):
            self.random_holder.append(random.choice(the_data["symbols"]))
        random.shuffle(self.random_holder)
        the_password = "".join(self.random_holder)
        self.random_holder.clear()
        return the_password
