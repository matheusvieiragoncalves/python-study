
print('### Arithmetic Operators in Python ###\n')

print(5 + 2 == 7)      # Addition
print(5 - 2 == 3)      # Subtraction
print(5 * 2 == 10)     # Multiplication
print(5 / 2 == 2.5)    # Division
print(5 // 2 == 2)     # Floor Division
print(5 % 2 == 1)      # Modulus
print(5 ** 2 == 25)    # Exponentiation
print(81 ** (1/2) == 9.0)  # Square Root
print(27 ** (1/3) == 3.0)  # Cube Root

print('\n### Operator Precedence ###\n')

print('First we have parentheses -> ()')
print('Then we have exponentiation -> **')
print('Then we have multiplication, division, floor division, and modulus -> *, /, //, %')
print('Finally we have addition and subtraction -> +, -')

print('\n### Examples of operator precedence ###\n')

# Demonstrating operator precedence
print(5 + 2 * 3 == 11)         # Multiplication before Addition
print((5 + 2) * 3 == 21)       # Parentheses change precedence
print(5 + 2 ** 2 == 9)         # Exponentiation before Addition
print(5 ** 2 + 3 == 28)        # Exponentiation before Addition
print(5 + 10 / 2 == 10)        # Division before Addition
print((5 + 10) / 2 == 7.5)     # Parentheses change precedence

# Extra - Formatting print output
print('\n### Formatted Output ###\n')

# Using f-strings for formatted output

print('=' * 40)
print('{:40}'.format(' RESULTADOS '))
print('{:^40}'.format(' RESULTADOS '))
print('{:>40}'.format(' RESULTADOS '))
print('{:<40}'.format(' RESULTADOS '))
print('\n{:=^40}\n'.format(' RESULTADOS '))

print('\n{:=^40}\n'.format(' Format Numbers '))

num1 = 5
num2 = 3

print('division {} / {} = {}'.format(num1, num2, num1/num2))
print('division {} / {} = {:.2f}'.format(num1, num2, num1/num2))
print('division {num1} / {num2} = {result:.2f}'.format(num1=num1, num2=num2, result=num1/num2))
print('division {} / {} = {result:.2f}'.format(num1, num2, result=num1/num2))


print('\n### Break lines ###')

print('This is the first line.\nThis is the second line.')
print('This is the first part of the line.', end=' >>> ')
print('This is the continuation of the same line.')