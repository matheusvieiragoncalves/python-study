# Exercise 005 - Nested Conditionals
# Write a program that read two grades of a student and calculate his/her average. Show a message at the end, according to the average:
# - Average below 5.0: REPROVED
# - Average between 5.0 and 6.9: RECOVERY
# - Average 7.0 or higher: APPROVED

MIN_AVARAGE_TO_APROVE: int = 7

grade_1: float = float(input("Please provide your first grade: "))
grade_2: float = float(input("Please provide your second grade: "))

avarage: float = (grade_1 + grade_2) / 2

if avarage < 5:
    print("Reproved!")
elif avarage >= 5 and avarage < 7:
    print("Recovery!")
else:
    print("Approved")
