import random

rock_paper_scissor_list = ["Rock", "Paper", "Scissor"]
play_continues = True
user_score = 0
computer_score = 0
total_rounds = 0

def user_input():
    user_input = int(input(f'''
=== Best of 5 ===
Type 1 for {rock_paper_scissor_list[0]}
Type 2 for {rock_paper_scissor_list[1]}
Type 3 for {rock_paper_scissor_list[2]}
Type Here: '''))
    if user_input == 1 or user_input == 2 or user_input == 3:
        return rock_paper_scissor_list[user_input - 1]
    else:
        print("Invalid Input")

def computer_output():
    computer_output = random.choice(rock_paper_scissor_list)
    return computer_output

def game_score_check(user_input, computer_output):
    global user_score, computer_score
    if user_input == computer_output:
        print(f"DRAW, You both choosed {computer_output}")
    elif user_input == "Rock":
        if computer_output == "Paper":
            computer_score += 1
            print(f"You: {user_input}")
            print(f"Computer: {computer_output}")
        else:
            user_score += 1
            print(f"You: {user_input}")
            print(f"Computer: {computer_output}")
    elif user_input == "Paper":
        if computer_output == "Rock":
            user_score += 1
            print(f"You: {user_input}")
            print(f"Computer: {computer_output}")
        else:
            computer_score += 1
            print(f"You: {user_input}")
            print(f"Computer: {computer_output}")
    else:
        if computer_output == "Rock":
            computer_score += 1
            print(f"You: {user_input}")
            print(f"Computer: {computer_output}")
        else:
            user_score += 1
            print(f"You: {user_input}")
            print(f"Computer: {computer_output}")

def round_tracker():
    global total_rounds
    total_rounds += 1
    print(f"Rounds: {total_rounds}")

def game_result_check():
    print(f"User Score: {user_score} | Computer Score: {computer_score}")
    if total_rounds == 5:
        if user_score == computer_score:
            print("Match DRAW")
        elif user_score > computer_score:
            print("*** You WON ***")
        else:
            print("=== Computer WON ===")
    

def play_again():
    global play_continues, user_score, computer_score, total_rounds
    user_consent = str(input("Play Again? Y / N\n"))
    if not user_consent == "y":
        print("Thanks for playing with us.")
        play_continues = False
    else:
        total_rounds = 0
        user_score = 0
        computer_score = 0
        play_continues = True

def main():
    while play_continues:
        while total_rounds < 5:
            user_selection = user_input()
            computer_selection = computer_output()
            game_score_check(user_selection, computer_selection)
            round_tracker()
            game_result_check()
        play_again()
main()