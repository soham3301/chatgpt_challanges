
class Guest:
    def __init__(self, name, birth_year, room_no, key):
        self.name = name
        self.birth_year = birth_year
        self.choosen_room_number = room_no
        self.key = key

    @staticmethod
    def adult_checker(birth_year):
        return 2026 - birth_year >= 18

    def guest_login(self, entered_key):
        if entered_key == self.key:
            return True
        else:
            return False
