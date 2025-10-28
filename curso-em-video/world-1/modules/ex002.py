# Exercise 002: Modules
# Create a program to read the length of the opposite and adjacent legs of a right triangle. Calculate and display the length of the hypotenuse.

from math import hypot

opposite = float(input('Type to opposite length: '))
adjacent = float(input('Type to adjacent length: '))

hypotenuse = hypot(opposite, adjacent)

print(f'The hypotenuse is {hypotenuse:.2f}')