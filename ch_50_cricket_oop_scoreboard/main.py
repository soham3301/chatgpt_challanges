
from player import Player
from match import Match
from scoreboard import Scoreboard
from display import Display
from user_input import Input

player_data = ["Virat", "Rohit", "Sachin", "Sourav", "Dravid", "Sehwag", "Yuvraj", "Nehra", "Agarwal", "Zaheer", "Dhoni"]

match = Match()
display = Display()
user_input = Input()
scoreboard = Scoreboard()

for player_name in player_data:
    match.helper_add_all_players(Player(player_name))
match.helper_add_first_two_players_on_pitch()

match_is_on = True
while match_is_on:
    display.the_main_display()
    user_consent = user_input.ask_user_input()
    if user_consent == "8":
        display.exit_message()
        match_is_on = False
    elif user_consent in ["1", "2", "3", "4", "5", "6", "7"]:
        if user_consent == "1":
            display.currently_playing(match.players_on_pitch)
            player_name = user_input.get_player_name()
            the_player = match.player_checker(player_name)
            if the_player:
                if the_player.on_pitch:
                    runs_to_add = user_input.get_runs()
                    if runs_to_add:
                        the_player.add_run(runs_to_add)
                        scoreboard.helper_add_score(runs_to_add)
                        display.single_player_runs(the_player)
                    else:
                        display.invalid_input()
                else:
                    display.invalid_input()
            else:
                display.invalid_input()
        elif user_consent == "2":
            display.available_players(match.all_players_list)
            name_of_player = user_input.get_player_name()
            added_player, out_player = match.add_player_on_pitch(name_of_player)
            if added_player and out_player:
                display.arrival_announcment(added_player, out_player)
            else:
                display.invalid_input()
        elif user_consent == "3":
            players_list_with_runs = scoreboard.show_scoreboard(match.players_on_pitch, match.out_players)
            display.scoreboard_display(players_list_with_runs)
        elif user_consent == "4":
            highest_scorer_player = scoreboard.highest_scorer(match.all_players_list)
            if highest_scorer_player:
                display.highest_scorer_display(highest_scorer_player)
            else:
                display.match_has_started()
        elif user_consent == "5":
            match.reset_match(scoreboard)
            display.match_reset_done()
        elif user_consent == "6":
            the_sorted_list = scoreboard.sort_scoreboard(match.all_players_list)
            display.show_sorted_list(the_sorted_list)
        elif user_consent == "7":
            summery_data = match.match_summery(scoreboard.score)
            display.summery_display(summery_data)
    else:
        display.invalid_input()
