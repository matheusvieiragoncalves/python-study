# Exercise 003:
# Write a program that reads two numbers and comapres them, showing on the screen a message:
# - The first number is greater
# - The second number is greater
# - There is no greater, both are equal

num1 = float(input('Enter a number: '))
num2 = float(input('Enter a other number: '))

if num1 == num2:
  print('Numbers is equal!')
elif num1 > num2:
  print(f'Number {num1} is greate than {num2}')
else:
  print(f'Number {num2} is greate than {num1}')