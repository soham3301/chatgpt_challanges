
class Player:
    def __init__(self, name):
        self.name = name
        self.on_pitch = False
        self.is_out = False
        self.score = 0

    def add_run(self, runs):
        self.score += runs