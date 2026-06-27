import random
print("=== Guess The Number between 1 to 50 ===")

def guess_it():
    secret_number = random.randint(1, 50)
    attempt_counter = 0
    while True:
        attempt_counter += 1
        guess_number = int(input("Guess: "))
        if guess_number > secret_number:
            print("Too High")
        elif guess_number < secret_number:
            print("Too Low")
        else:
            print("Correct Guess. Congrats")
            print(f"Total attempts taken: {attempt_counter}")
            user_consent = input("Play Again? Y / N\n").lower()
            if user_consent == "y":
                return True
            else:
                return False

user_consent = True

while user_consent:
    user_consent = guess_it()
else:
    print("Thanks for playing this amezing game. See You")
