
class Admin:
    def __init__(self):
        self.password = None

    def check_login(self, entered_pass):
        return entered_pass == self.password

    def change_password(self, new_pass):
        self.password = new_pass

    def to_dict(self):
        return {
            "password": self.password
        }

    def load_data(self, data):
        self.password = data["password"]