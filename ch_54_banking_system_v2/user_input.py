
class UserInput:
    def __init__(self):
        self.name = "User Input"

    def text_input(self):
        return input(": ")

    def number_input(self):
        try:
            return round(int(input(": ")))
        except ValueError:
            return None