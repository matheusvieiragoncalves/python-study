# Exercise 002: Texts
# Create a program that reads a number between 0 and 9999 and display in screen each of the digits separated.
# For example, 1834:
# units: 4
# tens: 3
# hundreds: 8
# thousands: 1

number = str(input('Enter a number between 0 and 9999: '))

print(f'Units: {number[:1] or 0}')
print(f'Tens: {number[1:2] or 0}')
print(f'Hundreds: {number[2:3] or 0}')
print(f'Thousands: {number[3:4] or 0}')