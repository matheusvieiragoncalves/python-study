# Exercise 008: conditionals
# Create a program that reads three straight lines and tells if they can or not form a triangle.

line1 = float(input('Enter a first line: '))
line2 = float(input('Enter a second line: '))
line3 = float(input('Enter a third line: '))

isPossible = True

if line1 + line2 <= line3:
    isPossible = False

if line1 + line3 <= line2:
    isPossible = False

if line2 + line3 <= line1:
    isPossible = False

print(f'Is {'not' if not isPossible else ''} possible')

