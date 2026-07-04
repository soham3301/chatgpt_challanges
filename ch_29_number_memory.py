import time
import random

def random_no_generator(length_modifier):
    random_no = (round(random.random() * 100 * length_modifier))
    return random_no

def checking_user_input(user_choice, generated_no):
    if user_choice == generated_no:
        print("Correct Answer")
        return True
    else:
        print("Wrong Answer")
        return False

def user_input():
    user_choice = int(input("Enter: "))
    return user_choice

def display_board():
    random_no_length_modifier = 1
    round_counter = 1
    game_stopper = True
    while game_stopper:
        display_random_no = random_no_generator(random_no_length_modifier)
        print(f"Round {round_counter}")
        print(display_random_no, end="", flush=True)
        time.sleep(3)
        print("\r" + "*" * len(str(display_random_no)))
        user_choice = user_input()
        game_stopper = checking_user_input(user_choice, display_random_no)
        random_no_length_modifier *= 10
        round_counter += 1
    return round_counter

def result_board(total_round):
    print(f"You played {total_round} rounds.")

def play_again():
    user_consent = str(input("Play Again? Y / N\n")).lower()
    if user_consent != "y":
        print("Thanks for playing with us.")
        return False
    else:
        return True

def main():
    game_running = True
    while game_running:
        total_rounds = display_board()
        result_board(total_rounds)
        game_running = play_again()

main()




