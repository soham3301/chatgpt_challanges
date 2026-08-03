
class Scoreboard:
    def __init__(self):
        self.name = "Scoreboard"
        self.score = 0

    def helper_add_score(self, player_list):
        for player in player_list:
            self.score += player.score

    def show_scoreboard(self, on_pitch_list, out_list):
        received_players = []
        if out_list:
            for player in out_list:
                received_players.append(player)
        if on_pitch_list:
            for current_player in on_pitch_list:
                received_players.append(current_player)
        return received_players

    def highest_scorer(self, player_list):
        the_player = None
        score_counter = 0
        for player in player_list:
            if player.score > score_counter:
                the_player = player
                score_counter = player.score
            elif player.score < score_counter:
                continue
        return the_player

    def sort_scoreboard(self, player_list):
        print("Scoreboard Sorted")