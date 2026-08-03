
import random

class Match:
    def __init__(self):
        self.all_players_list = []
        self.players_on_pitch = []
        self.out_players = []

    def helper_add_all_players(self, the_player):
        self.all_players_list.append(the_player)

    def helper_add_first_two_players_on_pitch(self):
        self.players_on_pitch.append(self.all_players_list[0])
        self.players_on_pitch.append(self.all_players_list[1])
        for player in self.players_on_pitch:
            player.on_pitch = True
        return True

    def player_checker(self, player_name):
        for player in self.all_players_list:
            if player.name == player_name:
                return player
        return None

    def helper_match_ends(self):
        print("Match Complete")

    def helper_player_out(self):
        if len(self.players_on_pitch) > 1:
            random_player = random.choice(self.players_on_pitch)
            random_player.on_pitch = False
            random_player.is_out = True
            self.players_on_pitch.remove(random_player)
            self.out_players.append(random_player)
            return random_player
        else:
            self.match_summery()
            self.helper_match_ends()
            return None

    def add_player_on_pitch(self, player_name):
        the_player = self.player_checker(player_name)
        if the_player:
            if not the_player.on_pitch and not the_player.is_out:
                the_out_player = self.helper_player_out()
                self.players_on_pitch.append(the_player)
                the_player.on_pitch = True
                return the_player, the_out_player
            else:
                return None, None
        else:
            return None, None

    def reset_match(self, score_board):
        self.players_on_pitch.clear()
        self.out_players.clear()
        score_board.score = 0
        return True

    def match_summery(self):
        print("Here is your match summery")
