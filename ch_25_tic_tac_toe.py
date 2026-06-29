import random

#? All Variables
the_board = '''
1 | 2 | 3
---------
4 | 5 | 6
---------
7 | 8 | 9'''
x_board = the_board
user_input_saved = [1, 2, 3, 4, 5, 6, 7, 8, 9]
# print(the_board)
# print(computer_guess)
# print(len(user_input_saved))

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

#? Display Board & taking user input
def user_input():
    global user_input_saved
    user_input_number = int(input(f"""=+=+=+ TIC TAC TOE +=+=+=
      {x_board}

      Choose a place: """))
    user_computer_inputs_update(user_input_number)
    return user_input_number

def user_computer_inputs_update(input_number):
    global user_input_saved
    if input_number in user_input_saved:
        user_input_saved.remove(input_number)
    else:
        print("INVALID MOVE | TRY AGAIN")

while True:
    position = user_input()
    updating_board_from_user(position)
    updating_board_from_computer()
