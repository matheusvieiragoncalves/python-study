# Exercise 001: Arithmetic Operators
# Create a program that reads a number and shows its successor and predecessor.

num = int(input('Type a number: '))

print('The successor of {} is {}.'.format(num, num + 1))
print('The predecessor of {} is {}.'.format(num, num - 1))