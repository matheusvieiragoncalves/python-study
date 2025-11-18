# Exercise 004 - Nested Conditionals
# Write a program that reads the year of birth of a young person and shows according to his/her age:
# - if he's still going to enlist
# - if it's time to enlist
# - if he has already passed the time of enlistment

from datetime import datetime

year_of_birth = int(input("Enter with your year of birht: "))

current_year: int = datetime.now().year

age: int = current_year - year_of_birth

MIN_AGE_TO_ENLIST: int = 18

if age < MIN_AGE_TO_ENLIST:
    print(
        f"There are still {MIN_AGE_TO_ENLIST - age} years left before you can enlist."
    )
elif age == MIN_AGE_TO_ENLIST:
    print("It's time to enlist")
else:
    print("You should have already enlisted.")
