from math import sqrt, ceil
from random import randint

# number = int(input('Type a number: '))
number = randint(1, 10)

rootSquare = ceil(sqrt(number))

print(f'The root square of {number} is {rootSquare}')

# to menager external modules use packmenager pip
