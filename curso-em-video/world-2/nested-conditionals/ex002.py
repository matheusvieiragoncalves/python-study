# Exercise 002: Nested Conditionals
# Type a program to read a any integer number and ask the user to choose what will be the basis for conversion.
# The options are:
# 1 for binary
# 2 for octal
# 3 for hexadecimal

choosed_number = int(input('Enter a number to convert: '))

binary = bin(choosed_number)
octal = oct(choosed_number)
hexadecimal = hex(choosed_number)

print('-=' * 20)

print(f'Binary: {binary}')
print(f'Octal: {octal}')
print(f'Hexadecimal: {hexadecimal}')
