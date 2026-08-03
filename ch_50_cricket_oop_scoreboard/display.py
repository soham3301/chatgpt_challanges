
class Display:
    def __init__(self):
        self.name = "Display"

    def the_main_display(self):
        print('''
1. Add Runs
2. Add Player on Pitch
3. Show Scoreboard
4. Highest Scorer
5. Reset Match
6. Sort Scoreboard
7. Match Summary
8. Exit
''')

    def invalid_input(self):
        print("Invalid Input")

    def exit_message(self):
        print("Thanks for using Cricket Scoreboard")

    def currently_playing(self, player_list):
        print("Currently Playing...")
        for player in player_list:
            print(player.name)

    def single_player_runs(self, player):
        print(f"{player.name} has scored {player.score} as of now.")

    def available_players(self, the_list):
        print("Available Players from Dressing Room")
        for player in the_list:
            if not player.is_out and not player.on_pitch:
                print(player.name)

    def arrival_announcment(self, arrived_player, depart_player):
        print(f"{arrived_player.name} has arrived on the Pitch. {depart_player.name} got out at {depart_player.score}")

    def scoreboard_display(self, players_list):
        for player in players_list:
            if player.is_out:
                print(f"{player.name}: {player.score}")
            if not player.is_out:
                print(f"{player.name}: {player.score}*")

    def highest_scorer_display(self, the_player):
        print(f"Highest Scorer: {the_player.name} | Score is: {the_player.score}")

    def match_has_started(self):
        print("The match has started now. No run is made till now.")

    def match_reset_done(self):
        print("Match has been Reset.")

    def show_sorted_list(self, sorted_list):
        for player in sorted_list:
            if player.is_out or player.on_pitch:
                if player.is_out:
                    print(f"{player.name} | {player.score}")
                else:
                    print(f"{player.name} | {player.score}*")

    def summery_display(self, data):
        print("Here is your Match Summery")
        total_score = 0
        out_player_number = 0
        for key, value in data.items():
            if key == "player_data":
                for player in value:
                    if player.on_pitch:
                        print(f"{player.name} | {player.score}*")
                    else:
                        print(f"{player.name} | {player.score}")
            elif key == "total_score":
                total_score = value
            elif key == "out_player_number":
                out_player_number = value
        print(f"Total Score: {total_score} / {out_player_number}")
            
            