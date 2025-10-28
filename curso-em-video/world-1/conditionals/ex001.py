# Exercise 001: conditionals
# Create a program that select a random number between 0 and 5 and ask the user to guess it.

from random import randint
from time import sleep

computer = randint(0, 5)
number = int(input('Guess a number between 0 and 5: '))

print('Processing...')
sleep(2) # in Seconds

if number == computer:
    print('Congratulations! You guessed it right!')
else:
    print(f'Sorry, you missed it! The correct number was {computer}.')
