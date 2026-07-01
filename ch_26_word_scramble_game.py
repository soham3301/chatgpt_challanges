import random

#? All Variables
word_list = ["tiger", "shark", "universe", "amazon", "chatGPT", "diamond", "casino", "kolkata"]
total_chance = 3
win_checker = True
var_play_again = True
hint_list = ["True king of Jungle", "Jaws that everyone fear", "It started with the big bang", "Want to order something? or just search for el dorado", "The place where you go to know everything", "A gift that lasts forever", "Where Mr. Bond faced Le Chiffre", "Felu Da's hometown"]

#? Functions
def word_generation_and_scrambler():
    random_word = random.choice(word_list)
    scrambled_word = "".join(random.sample(random_word, len(random_word)))
    return random_word, scrambled_word

def hint_generator(random_word):
    for word in word_list:
        if word == random_word:
            index_of_word = word_list.index(word)
            the_hint = hint_list[index_of_word]
            return the_hint

def user_input_and_display(random_word, scrambled_word):
    global total_chance, win_checker
    print(f"Word: {scrambled_word}")
    for _ in range(0, 3):
        user_input = str(input(f'''Chances left: {total_chance}
Guess: '''))
        if user_input == random_word:
            print("*** ** * Excellent. You WON * ** ***")
            win_checker = False
            break
        else:
            total_chance -= 1
            if total_chance != 0:
                print("Try Again.")
        if total_chance == 1:
            print(f"Hint: {hint_generator(random_word)}")
        if total_chance == 0:
            print("=== Game OVER ===")

#? Play again function
def play_again():
    global var_play_again, total_chance, win_checker
    user_consent = str(input("Do you want to play again? Y / N\n")).lower()
    if not user_consent == "y":
        print("Thanks for playing with us")
        var_play_again = False
    else:
        win_checker = True
        total_chance = 3

#? The main function
def main():
    while var_play_again:
        random_word, scrambled_word = word_generation_and_scrambler()
        while total_chance != 0 and win_checker:
            user_input_and_display(random_word, scrambled_word)
        else:
            play_again()

main()