
class Input:
    def __init__(self):
        self.name = "Input Class"

    def ask_user_input(self):
        user_choice = input("Choose from above: ")
        return user_choice

    def get_player_name(self):
        name_of_player = input("Enter Player Name: ").title()
        return name_of_player

    def get_runs(self):
        try:
            run = round(int(input("Enter runs to add: ")))
            if run > 0:
                return run
            else:
                return 0
        except ValueError:
            return 0