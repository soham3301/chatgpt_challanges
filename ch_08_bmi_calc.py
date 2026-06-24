# BMI = weight / (height * height)

#BMI	Category
#<18.5	Underweight
#18.5–24.9	Normal
#25–29.9	Overweight
#≥30	Obese

weight = float(input("What's your weight in kg: "))
height = float(input("What's your height in meter: "))

bmi = round(float(weight / height ** 2), 2)

if (bmi < 18.5):
    print("You are underweight")
elif (bmi >= 30):
    print("You are obese")
elif (bmi <= 24.9):
    print("You are normal")
elif (bmi <= 29.9):
    print("You are overweight")
else:
    print("Enter a correct number")