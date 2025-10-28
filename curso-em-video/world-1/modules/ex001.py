# Exercise 001: Modules
# Create a program that reads a real number and shows its whole portion.

from math import trunc

number = float(input('Type a breaked number (ex.: 6.234): '))

print(f'The whole portion of {number} is {trunc(number)}.')
