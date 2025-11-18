# Exercise 005 - Nested Conditionals
# Write a program taht read the year of birth of a swimmer and show according to his/her age, the category:
# - Up to 9 years old: MIRIM
# - Up to 14 years old: CHILDREN
# - Up to 19 years old: JUNIOR
# - Up to 20 years old: SENIOR
# - Above 20 years old: MASTER

from datetime import datetime

year_of_birth = int(input("Enter with your year of birht: "))

current_year: int = datetime.now().year

age: int = current_year - year_of_birth

if age <= 9:
    print("MIRIM")
elif age <= 14:
    print("CHILDREN")
elif age <= 19:
    print("JUNIOR")
elif age <= 20:
    print("SENIOR")
else:
    print("MASTER")
