
class UserInput:
    def __init__(self):
        self.name = "User Input"

    def text_input(self):
        return input(": ").lower()

    def number_input(self):
        try:
            number = abs(round(int(input(": "))))
            return number
        except ValueError:
            return None