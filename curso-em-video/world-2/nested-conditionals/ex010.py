# Exercise 010 - Nested Conditionals
# Create a program that play jokenpô (rock, paper and scissors) with the computer.

from random import randint
from time import sleep

options: tuple[str, str, str] = ("Rock", "Paper", "Scissors")
computer_choice: int = randint(0, 2)

print("Your options:")
for i, option in enumerate(options):
    print(f"{i} - {option}")

user_choice: int = int(input("Enter with your choice (0, 1 or 2): "))

print("JO")
sleep(1)

print("KEN")
sleep(1)

print("PÔ!!!")
sleep(1)

print(f"Computer chose {options[computer_choice]}")
print(f"You chose {options[user_choice]}")

if computer_choice == user_choice:
    print("It's a tie!")
elif (
    (computer_choice == 0 and user_choice == 2)
    or (computer_choice == 1 and user_choice == 0)
    or (computer_choice == 2 and user_choice == 1)
):
    print("Computer wins!")
else:
    print("You win!")
