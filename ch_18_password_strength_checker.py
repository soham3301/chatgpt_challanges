# Initializing Strength Indicator
strength_indicator = 0

# Taking user input
user_input = input("Enter your password to check it's strength?\n")

# Condition 1 -> Password Length
length = len(user_input)
if length >= 8:
    strength_indicator += 1
    #print(strength_indicator)

# Condition 2 -> Contains Uppercase
for char in user_input:
    if char.isupper():
        strength_indicator += 1
        break

# Condition 3 -> Contains Lowercase
for char in user_input:
    if char.islower():
        strength_indicator += 1
        break

# Condition 4 -> Contains Numbers
for num in user_input:
    if num.isdigit():
        strength_indicator += 1
        break

# Condition 5 -> Contains Symbols
if user_input.isalnum() == False:
    strength_indicator += 1

if strength_indicator <= 2:
    print("Your Password strength is WEAK")
elif strength_indicator <= 4:
    print("Your Password strength is MEDIUM")
else:
    print("You have a STRONG Password")