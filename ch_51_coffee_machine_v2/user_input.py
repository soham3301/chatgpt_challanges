
class UserInput:
    def __init__(self):
        self.name = "User Input"

    def take_text_input(self):
        return input(": ").lower()

    def take_number_input(self):
        try:
            return  int(input(": "))
        except ValueError:
            return None