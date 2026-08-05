
class Admin:
    def __init__(self):
        self.name = "Admin"
        self.password = 1234

    def check_login(self, input_password):
        return input_password == self.password