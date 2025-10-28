# Exercise 006: conditionals
# Create a program that reads a three numbers and shows the largest and smallest one.

num1 = float(input('Enter a number one: '))
num2 = float(input('Enter a number two: '))
num3 = float(input('Enter a number three: '))

num_list = [num1, num2, num3]

num_list.sort()

print(f'Largest: {num_list[2]}')
print(f'Smallest: {num_list[0]}')
