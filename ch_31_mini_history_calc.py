def display_board():
    print('''
Choose from Below:
1. Addition
2. Substraction
3. Multiplication
4. Division
5. History
6. Exit
''')

def user_decision():
    user_choice = int(input("Choose: "))
    if user_choice in [1, 2, 3, 4, 5, 6]:
        if user_choice == 1:
            return "+"
        elif user_choice == 2:
            return "-"
        elif user_choice == 3:
            return "*"
        elif user_choice == 4:
            return "/"
        elif user_choice == 5 or user_choice == 6:
            return user_choice
    else:
        print("Invalid Input")
        return 0

def user_input_first():
    user_choice_first = int(input("Enter the first number: "))
    user_choice_second = int(input("Enter the second number: "))
    return user_choice_first, user_choice_second

def calculations(decision, first_number, second_number):
    if decision == "+":
        return first_number + second_number
    elif decision == "-":
        return first_number - second_number
    elif decision == "*":
        return first_number * second_number
    elif decision == "/":
        if second_number != 0:
            return first_number / second_number
        else:
            return "Unknowable"
    else:
        print("Invalid Input. Please choose from the given list.")

def history_storer(decision, first_number, second_number, result):
    history_list = []
    history_list.append(first_number)
    history_list.append(decision)
    history_list.append(second_number)
    history_list.append("=")
    history_list.append(result)
    return history_list    

def display_result(result):
    if result == "Unknowable":
        print("Sorry, Can't divide by 0")
    else:
        print(f"Here is the result: {result}")

def history_display(history_stored):
    history_simply_shown_full = ""
    for single_history in history_stored:
        history_simply_shown_single = ""
        for _ in single_history:
            history_simply_shown_single = " ".join(str(item) for item in single_history)
        history_simply_shown_full += "\n" + history_simply_shown_single
    print(f'''
History:
{history_simply_shown_full}
''')

def main():
    game_stopper = True
    full_history_list = []
    while game_stopper:
        display_board()
        user_decision_input = user_decision()
        if user_decision_input == 6:
            game_stopper = False
            print("Thanks for using History Calculator")
        elif user_decision_input == 0:
            game_stopper = False
        elif user_decision_input == 5:
            history_display(full_history_list)
        else:
            first_user_input, second_user_input = user_input_first()
            calculation_result = calculations(user_decision_input, first_user_input, second_user_input)
            full_history_list.append(history_storer(user_decision_input, first_user_input, second_user_input, calculation_result))
            display_result(calculation_result)

main()