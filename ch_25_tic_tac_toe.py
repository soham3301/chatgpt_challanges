import random

#* Decclaring Variables
the_board = '''
1 | 2 | 3
---------
4 | 5 | 6
---------
7 | 8 | 9'''
user_input_original_values = [1, 2, 3, 4, 5, 6, 7, 8, 9]
x_board = the_board
user_input_saved = user_input_original_values
# print(the_board)
# print(computer_guess)
# print(len(user_input_saved))
# print(x_board.index("8"))

#! Indexes of the numbers inside board
#!  1 | 5 | 9
#!  ---------
#!  21 | 25 | 29
#!  ---------
#!  41 | 45 | 49

#* The board update section.
def updating_board_from_user(choosen_number):
    global x_board
    x_board = x_board.replace(str(choosen_number), "X")

def updating_board_from_computer():
    global x_board, user_input_saved
    if len(user_input_saved) != 0:
        generated_no = random.choice(user_input_saved)
        user_computer_inputs_update(generated_no)
        x_board = x_board.replace(str(generated_no), "O")
    else:
        print("No place left to choose")
        return False

#* The board display & User Input.
def user_input():
    global user_input_saved
    user_input_number = int(input(f"""=+=+=+ TIC TAC TOE +=+=+=
      {x_board}

      Choose a place: """))
    user_computer_inputs_update(user_input_number)
    return user_input_number

#* Computer & User input update function.
def user_computer_inputs_update(input_number):
    global user_input_saved
    if input_number in user_input_saved:
        user_input_saved.remove(input_number)
    else:
        print("INVALID MOVE")

#* Detecting win.
def win_detection(entered_x_or_o, you_or_comp):
    global x_board
    for _ in range(0, 1):
        if x_board[1] == x_board[5] == x_board[9] == entered_x_or_o:
            print(f"=== {you_or_comp} WON ===")
        elif x_board[21] == x_board[25] == x_board[29] == entered_x_or_o:
            print(f"=== {you_or_comp} WON ===")
        elif x_board[41] == x_board[45] == x_board[49] == entered_x_or_o:
            print(f"=== {you_or_comp} WON ===")
        elif x_board[1] == x_board[21] == x_board[41] == entered_x_or_o:
            print(f"=== {you_or_comp} WON ===")
        elif x_board[5] == x_board[25] == x_board[45] == entered_x_or_o:
            print(f"=== {you_or_comp} WON ===")
        elif x_board[9] == x_board[29] == x_board[49] == entered_x_or_o:
            print(f"=== {you_or_comp} WON ===")
        elif x_board[1] == x_board[25] == x_board[49] == entered_x_or_o:
            print(f"=== {you_or_comp} WON ===")
        elif x_board[9] == x_board[25] == x_board[41] == entered_x_or_o:
            print(f"=== {you_or_comp} WON ===")
        else:
            return True

#* Play Again?
def game_reset_and_play_again():
    global x_board, user_input_saved
    x_board = the_board
    user_input_saved = user_input_original_values


#* The game loop.
def main():
    while True:
        draw_counter = 5
        while draw_counter != 0:
            position = user_input()
            updating_board_from_user(position)
            if not win_detection("X", "You"):
                print(f"{x_board}")
                break
            updating_board_from_computer()
            if not win_detection("O", "Computer"):
                print(f"{x_board}")
                break
            draw_counter -= 1
        else:
            print("Game Draw")
            break
main()

#TODO-1 Introduce the "Play Again" option for user.
#TODO-2 Bug fix for wrong user input.