import random

#* VARIABLES
questions = ["What is the Capital of Brazil?", "Kaka is a famous ________", "In World War II, Germany, Itely and which country made the axis group?", "'Tupac Shakur' is related to which art form?", "Which country got independence in 1948?", "Who was the first person to go to space?", "The river Nile originates where?", "Which person got the Noble and Oscar prize both?", "What is the name of world's second highest mmountain peak?", "Comodo island is famous for it's _______"]
correct_answers = ["Brasília", "Footballer", "Japan", "Rap Music", "Sri Lanka", "Yuri Gagarin", "Lake Victoria", "George Bernard Shaw", "K2", "Dragons"]
incorrect_options = [["Toronto", "Rio De Janeiro", "Buenos Aires"], ["Cricketer", "F1 Racer", "Basketball Player"], ["Spain", "Russia", "Egypt"], ["Dancing", "Acting", "Painting"], ["Indonesia", "Congo", "Iraq"], ["Valentina Tereshkova", "Neil Armstrong", "Buzz Aldrin"], ["Mount Kilimanjaro", "Lake Titicaca", "The Congo Basin"], ["Marie Curie", "Satyajit Ray", "Alexander Fleming"], ["Nanga Parvat", "Kangchenjunga", "Makalu"], ["Snakes", "Horses", "Eagles"]]

#! NOT FOR MAIN - Inside board_and_user_input()
def options_display():
    mixed_answers = []
    index_for_correct_answers = 0
    for incorrect in incorrect_options:
        incorrect.append(correct_answers[index_for_correct_answers])
        index_for_correct_answers += 1
        random.shuffle(incorrect)
        mixed_answers.append(incorrect)
    return mixed_answers

#! NOT FOR MAIN - Inside start_the_game
def first_display():
    start_exam = input('''
=== == = WELCOME TO SSC CGL EXAMINATION = == ===
Rule 1: There will be total 10 questions.
Rule 2: Type A, B, C or D to choose your answer.
Rule 3: Correct Answer will gain 4 Marks.
Rule 4: Wrong Answer will deduct 1 Mark.
Rule 5: Total Marks is 40.
Rule 6: Below 20 means FAIL | 20 to 30 means PRILIMS CLEAR | 30 above is JOB CONFIRM

Start EXAM ? (Press 'Y' for YES and 'N' for NO)
''').lower()
    return start_exam

#! NOT FOR MAIN - Inside start_the_game()
def board_and_user_input():
    shuffled_answers = options_display()
    index_of_correct_answer = 0
    user_answer_list = []
    correct_answer_list = []
    for counter in range(0, len(questions)):
        user_choice = str(input(f'''
[{counter + 1}] {questions[counter]}

A. {shuffled_answers[counter][0]}
B. {shuffled_answers[counter][1]}
C. {shuffled_answers[counter][2]}
D. {shuffled_answers[counter][3]}

Choose: ''')).lower()
        user_answer_list.append(user_answer_display(user_choice, shuffled_answers, counter, index_of_correct_answer))
        correct_answer_list.append(correct_answers[index_of_correct_answer])
        print(f"Correct Answer: {correct_answers[index_of_correct_answer]}")
        index_of_correct_answer += 1
    return user_answer_list, correct_answer_list

#! NOT FOR MAIN - Inside board_and_user_input()
def user_answer_display(user_choice, shuffled_answers, counter, index_of_correct_answer):
        if user_choice == "a":
            print(f"Your Answer: {shuffled_answers[counter][0]}")
            return shuffled_answers[counter][0]
        elif user_choice == "b":
            print(f"Your Answer: {shuffled_answers[counter][1]}")
            return shuffled_answers[counter][1]
        elif user_choice == "c":
            print(f"Your Answer: {shuffled_answers[counter][2]}")
            return shuffled_answers[counter][2]
        elif user_choice == "d":
            print(f"Your Answer: {shuffled_answers[counter][3]}")
            return shuffled_answers[counter][3]
        else:
            print("Invalid Input")
            return "Wrong Input", "You LOST 1 Mark"

#? Inside MAIN
def play_again():
    user_consent = str(input("Do you want to try again? Type 'Y' for YES and 'N' for NO\n")).lower()
    if user_consent == "y":
        return True
    elif user_consent == "n":
        return False
    else:
        print("Invalid Input.")
        return False

#! NOT FOR MAIN - Inside start_the_exam()
def final_result(user_answer, correct_answer):
    score = 0
    announcment = ""
    for checker_index in range(0, len(user_answer)):
        if user_answer[checker_index] == correct_answer[checker_index]:
            score += 4
        else:
            score -= 1
    if score < 20:
        announcment = "You Failed this written exam."
    elif score <= 30:
        announcment = "Start Preparing for VIVA."
    else:
        announcment = "Congratulations for your new JOB"
    return score, announcment

#? Inside Main
def start_the_exam():
    exam_starter = first_display()
    if exam_starter == "y":
        user_answer, correct_answer = board_and_user_input()
        score, announcment = final_result(user_answer, correct_answer)
        print(f"Score: {score}/40 | {announcment}")
        return True
    else:
        print("Study Hard and Comeback Strongly. See you again")
        return False

def main():
    user_consent_check = True
    while user_consent_check:
        if start_the_exam():
            user_consent_check = play_again()

main()





#! Testing Block
# print(board_and_user_input())
# print(board_and_user_input())

