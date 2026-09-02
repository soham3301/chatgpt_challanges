
class Admin:
    def __init__(self):
        self.name = "ADMIN"
        self.password = "123"

    def check_login(self, entered_pass):
        return entered_pass == self.password