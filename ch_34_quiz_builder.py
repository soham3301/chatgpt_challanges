import random
quiz = {
    "Capital of India": "Delhi",
    "Value of PI": "3.14",
    "Largest Ocean": "Pacific",
    "Smallest Country": "Vatican City",
    "Fastest Animal": "Cheetah",
    "Biggest Animal": "Blue Whale",
    "First Man on the Moon": "Neil Armstrong",
    "Maximum time football world Champion": "Brazil",
    "Largest City by Population": "Jakarta",
    "Currency of UK": "Pound",
    "Where would you be if you were standing on the Spanish Steps?": "Rome",
    "What city is known as 'The Eternal City'?": "Rome",
    "What is the capital of Ireland?": "Dublin",
    "What is the largest Spanish-speaking city in the world?": "Mexico City",
    "What colors is the flag of the United Nations?": "Blue and White",
}

def shuffled_question():
    quiz_copy = quiz.copy()
    quiz_items = list(quiz_copy.items())
    random.shuffle(quiz_items)
    shuffled_quiz = dict(quiz_items)
    return shuffled_quiz

def welcome_board():
    print('''
=== WELCOME TO QUIZ ===
RULES
1. Every Correct Answer Gains +1 Score.
2. Every Wrong Answer Loses -1 Score.
''')
    return int(input("How many questions do you want to answer?\n"))

def program_stopper():
    user_consent = input("Want to play another quiz game? Y / N\n").lower()
    if user_consent == "y":
        return True
    else:
        print("Thanks for playing the quiz game. See You.")
        return False

def asking_quiz_question(shuffled, the_score):
    for random_question, the_answer in shuffled.items():
        user_answer = input(f"{random_question}?\n").strip().lower()
        if user_answer == the_answer.lower():
            the_score += 1
            print(f"CORRECT Answer. Score: {the_score}")
            shuffled.pop(random_question)
            return the_score
        else:
            the_score -= 1
            print(f"WRONG Answer. Score: {the_score}")
            shuffled.pop(random_question)
            return the_score

def round_checker(the_rounds, max_round):
    if the_rounds >= max_round:
        print("Game Completes")
        return False
    else:
        return True

def quiz_result(total_score, all_rounds):
    if total_score <= 0:
        print(f"Your Score is in Negative. You Lost this game. Score {total_score}")
    else:
        win_percent = round((total_score / all_rounds), 2) * 100
        print(f'''
Here is your result:
Score: {total_score}
Total Rounds: {all_rounds}
Win Percentage: {win_percent}
''')

def main():
    program_continues = True
    while program_continues:
        shuffled_quiz_questions = shuffled_question()
        score = 0
        total_rounds = 0
        maximum_rounds = welcome_board()
        quiz_continues = True
        while quiz_continues:
            score = asking_quiz_question(shuffled_quiz_questions, score)
            total_rounds += 1
            quiz_continues = round_checker(total_rounds, maximum_rounds)
        quiz_result(score, total_rounds)
        program_continues = program_stopper()

main()
