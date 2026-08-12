
class Input:
    def __init__(self):
        self.name = "Console Input"

    def text_input(self):
        return input(": ")

    def number_input(self):
        try:
            return abs(round(int(input(": "))))
        except ValueError as error:
            return error