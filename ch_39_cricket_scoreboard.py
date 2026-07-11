import random
players = {
    "Virat":{
        "isOut":True,
        "score":84
    },
    "Rohit":{
        "isOut":False,
        "score":64
    },
    "Sachin":{
        "isOut":False,
        "score":102
    },
}

#? ================ Master Functions ================

def display_board_and_input():
    try:
        user_choice = int(input('''
1. Add Runs
2. Add Player
3. Show Scoreboard
4. Highest Scorer
5. Reset Match
6. Sort Scoreboard
7. Match Summary
8. Exit
'''))
        if user_choice == 8:
            print("Closing Scoreboard.")
            return False, None
        elif user_choice in [1, 2, 3, 4, 5, 6, 7]:
            return True, user_choice
        else:
            print("Kindly choose in between shown numbers.")
            return True, None
    except ValueError:
        print("Invalid Input. Closing Application.")
        return False, None

def add_runs():
    player_in_pitch = []
    print("Currently Playing ...")
    for player, details in players.items():
        if not details["isOut"]:
            player_in_pitch.append(player)
            print(player)
    player_name = helper_choose_player_name()
    if player_name in player_in_pitch:
        helper_add_run(player_name)
    else:
        user_consent = input("This player has not played yet. Want to add him in pitch? Y / N\n").lower()
        if user_consent == "y":
            helper_add_player(player_name)

def add_player():
    player_name = helper_choose_player_name()
    if player_name in players:
        print("This player already exist. Can't add.")
    else:
        helper_add_player(player_name)

def show_scoreboard():
    for player, score in players.items():
        if not players[player]["isOut"]:
            print(f"{player}: {score["score"]} Not Out")
        else:
            print(f"{player}: {score["score"]}")

def highest_scorer():
    highest_score = 0
    player_name = ""
    for player, details in players.items():
        if details["score"] > highest_score:
            highest_score = details["score"]
            player_name = player
    print(f"Highest Score: {highest_score} | Done by {player_name}")

def reset_match():
    players.clear()
    print("Match Reset Done")
    add_player()
    add_player()

def sort_scoreboard():
    sorted_scoreboard = {}
    players_copy = players.copy()
    for _ in range(len(players_copy)):
        score_tracker = 0
        player_name = ""
        for player, details in players_copy.items():
            if details["score"] > score_tracker:
                score_tracker = details["score"]
                player_name = player
        players_copy.pop(player_name)
        sorted_scoreboard[player_name] = score_tracker
    for name, score in sorted_scoreboard.items():
        print(f"{name}: {score}")

def match_summary():
    print("Match Summary")
    total_runs = 0
    total_player_got_out = 0
    for player, details in players.items():
        total_runs += details["score"]
        if details["isOut"]:
            total_player_got_out += 1
            print(f"{player}: {details["score"]}")
        else:
            print(f"{player}: {details["score"]}*")
    print(f"Total = {total_runs}/{total_player_got_out}")

#? ================ Mapper Function ================

def mapping_user_input(user_choice):
    saved_functions = {
        1: add_runs,
        2: add_player,
        3: show_scoreboard,
        4: highest_scorer,
        5: reset_match,
        6: sort_scoreboard,
        7: match_summary,
    }
    if user_choice in saved_functions:
        saved_functions[user_choice]()

#? ================ Helper Functions ================

def helper_add_player(the_name):
    if len(players) > 1:
        players[the_name] = {
            "isOut":False,
            "score":0
        }
        helper_player_out(the_name)
    else:
        players[the_name] = {
            "isOut":False,
            "score":0
        }
        print(f"{the_name} has arrived in the Pitch for a fresh match.")

def helper_choose_player_name():
    return input("Enter Player Name: ").title()

def helper_add_run(the_name):
    try:
        run = round(int(input("Enter run to add: ")))
        if run < 0:
            print("Sorry Negative runs can't be added.")
        else:
            players[the_name]["score"] += run
            print(f"{the_name} has scored {players[the_name]["score"]} as of now.")
    except ValueError:
        print("Please enter a numerical value.")

def helper_player_out(the_player_name):
    random_number = random.randint(0,1)
    player_in_pitch = []
    for player, details in players.items():
        if not details["isOut"]:
            player_in_pitch.append(player)
    players[player_in_pitch[random_number]]["isOut"] = True
    print(f"{the_player_name} has arrived in the Pitch. {player_in_pitch[random_number]} got out at {players[player_in_pitch[random_number]]["score"]}")

#? ================ MAIN Functions ================

def main():
    scoreboard_running = True
    while scoreboard_running:
        scoreboard_running, user_input = display_board_and_input()
        mapping_user_input(user_input)

main()