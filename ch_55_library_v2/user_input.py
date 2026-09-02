
class UserInput:
    def __init__(self):
        self.name = "INPUT"

    def text_input(self):
        return input(": ")

    def number_input(self):
        try:
            return int(input(": "))
        except ValueError:
            return None