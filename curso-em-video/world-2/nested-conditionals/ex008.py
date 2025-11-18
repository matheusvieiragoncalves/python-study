# Exercise 008 - Nested Conditionals
# Write a program that read the weight and height of a person, calculate his/her BMI and show his/her status, according to the table below:
# - Below 18.5: UNDERWEIGHT
# - Between 18.5 and 25: NORMAL WEIGHT
# - Between 25 and 30: OVERWEIGHT
# - Between 30 and 40: OBESITY
# - Above 40: MORBID OBESITY

weight: float = float(input("Enter with your weight (kg): "))
height: float = float(input("Enter with your height (m): "))

bmi: float = weight / (height**2)

if bmi < 18.5:
    print("UNDERWEIGHT")
elif bmi >= 18.5 and bmi < 25:
    print("NORMAL WEIGHT")
elif bmi >= 25 and bmi < 30:
    print("OVERWEIGHT")
elif bmi >= 30 and bmi < 40:
    print("OBESITY")
else:
    print("MORBID OBESITY")

print(f"Your BMI is {bmi:.2f}")
