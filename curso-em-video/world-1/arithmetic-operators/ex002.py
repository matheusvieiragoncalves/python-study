# Exercise 002: Arithmetic Operators
# Create a algorithm that reads a number and show your double, triple and square root.

num = int(input('Type a number: '))

print(f'The number selected is: {num}')
print(f'The double of {num} is {num * 2}')
print(f'The triple of {num} is {num * 3}')
print(f'The square root of {num} is {num ** (1/2):.0f}')
