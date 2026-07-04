import random

def random_no_generator():
    secret_no_list = [654, 275, 547, 890, 780, 109, 916, 201, 802, 321, 495, 167, 528, 924, 945, 753, 926, 714, 598, 427]
    secret_no = random.choice(secret_no_list)
    return str(secret_no)

def user_input():
    user_choice = int(input("Guess: "))
    return str(user_choice)

def correct_position_checker(secret_no, user_choice):
    correct_position_counter = 0
    for position_checker in range(0, len(secret_no)):
        if secret_no[position_checker] == user_choice[position_checker]:
            correct_position_counter += 1
    print(f"Correct Position: {correct_position_counter}")

def wrong_position_checker(secret_no, user_choice):
    wrong_position_counter = 0
    for position_holder in range(0, len(secret_no)):
        if secret_no[position_holder] != user_choice[position_holder]:
            for char_checker in range(0, len(user_choice)):
                if secret_no[position_holder] == user_choice[char_checker]:
                    wrong_position_counter += 1
    print(f"Wrong Position: {wrong_position_counter}")

def game_stopper(sec_no, user_ans):
    if sec_no == user_ans:
        print("+++ === +++ Guess MATCHED +++ === +++")
        return False
    else:
        return True

def play_again():
    user_consent = str(input("Play Again? Y / N\n")).lower()
    if user_consent != "y":
        print("Thanks for playing with Us. ^_^")
        return False
    else:
        return True

def main():
    game_continues = True
    while game_continues:
        game_running = True
        print("=== MINI MASTERMIND ===\nHint: 3 digits")
        secret_no_generated = random_no_generator()
        while game_running:
            user_input_generated = user_input()
            correct_position_checker(secret_no_generated, user_input_generated)
            wrong_position_checker(secret_no_generated, user_input_generated)
            game_running = game_stopper(secret_no_generated, user_input_generated)
        game_continues = play_again()

main()


